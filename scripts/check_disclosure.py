#!/usr/bin/env python3
"""Check that no term of the disclosure list appears in the repository (ADR-0012).

The list lives outside the repository: `FKB_DENYLIST`, or `~/.config/focus-kit-book/denylist.txt`.
Prints one line per finding as `file:line: disclosure: message`; exits 1 when anything is printed.
A finding never shows the term or the matched text: a matched part of a path is printed as `***`.

With no argument it scans the files and every commit message, and fails when the hooks are off.
`--staged` scans the staged files (the pre-commit hook); `--message <file>` scans a commit message
(the commit-msg hook). Both fail when the list is missing.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

from patterns import compile_entry
from repo_files import ROOT, repo_files

DEFAULT_LIST = Path.home() / ".config" / "focus-kit-book" / "denylist.txt"
MASK = "***"
HOOKS = ".githooks"
SCISSORS = "# ------------------------ >8 ------------------------"


def list_path():
    return Path(os.environ.get("FKB_DENYLIST") or DEFAULT_LIST)


def load(path):
    """Return (entries, findings): entries as (list line number, compiled pattern)."""
    entries, findings = [], []
    for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
        entry = line.strip()
        if not entry or entry.startswith("#"):
            continue
        try:
            entries.append((number, compile_entry(entry)))
        except re.error:
            findings.append(f"{path}:{number}: disclosure: invalid regular expression")
    return entries, findings


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=True).stdout


def decode(data):
    if b"\0" in data:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return None


def scan_lines(entries, where, lines, message="matches list entry"):
    """`lines` as (line number, text)."""
    findings = []
    for line_number, line in lines:
        for number, pattern in entries:
            if pattern.search(line):
                findings.append(f"{where}:{line_number}: disclosure: {message} {number}")
    return findings


def scan_file(entries, name, text):
    """A path and its text, or None for a binary file."""
    shown = name
    for _, pattern in entries:
        shown = pattern.sub(MASK, shown)
    findings = [
        f"{shown}:1: disclosure: file path matches list entry {number}"
        for number, pattern in entries if pattern.search(name)
    ]
    if text is not None:
        findings += scan_lines(entries, shown, enumerate(text.split("\n"), 1))
    return findings


def scan_repo(entries):
    findings = []
    for path in repo_files():
        findings += scan_file(entries, path.as_posix(), decode((ROOT / path).read_bytes()))
    return findings


def scan_history(entries):
    if subprocess.run(["git", "rev-parse", "-q", "--verify", "HEAD"], cwd=ROOT, capture_output=True).returncode:
        return []
    fields = git("log", "--format=%H%x00%B%x00").decode("utf-8", "replace").split("\0")
    findings = []
    for sha, body in zip(fields[0::2], fields[1::2]):
        findings += scan_lines(
            entries, sha.strip()[:12], enumerate(body.split("\n"), 1), "commit message matches list entry"
        )
    return findings


def scan_staged(entries):
    names = git("diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z").decode("utf-8").split("\0")
    findings = []
    for name in filter(None, names):
        findings += scan_file(entries, name, decode(git("show", f":{name}")))
    return findings


def scan_message(entries, name):
    lines = []
    for number, line in enumerate(Path(name).read_text(encoding="utf-8", errors="replace").split("\n"), 1):
        if line == SCISSORS:
            break
        if not line.startswith("#"):
            lines.append((number, line))
    return scan_lines(entries, name, lines)


def hooks_off():
    found = subprocess.run(["git", "config", "core.hooksPath"], cwd=ROOT, capture_output=True, text=True)
    return found.stdout.strip() != HOOKS


def main(args):
    path = list_path()
    if not path.is_file():
        if not args and not os.environ.get("CI"):
            print("disclosure: skipped, no list", file=sys.stderr)
            return 0
        findings = [f"{path}:1: disclosure: list is missing or has no entry"]
    else:
        entries, findings = load(path)
        if not entries and not findings:
            findings = [f"{path}:1: disclosure: list is missing or has no entry"]
        if args[:1] == ["--staged"]:
            findings += scan_staged(entries)
        elif args[:1] == ["--message"] and len(args) == 2:
            findings += scan_message(entries, args[1])
        elif args:
            findings.append("Makefile:1: disclosure: usage: check_disclosure.py [--staged | --message <file>]")
        else:
            findings += scan_repo(entries) + scan_history(entries)
            if not os.environ.get("CI") and hooks_off():
                findings.append("Makefile:1: disclosure: hooks are off; run make hooks")
    for finding in findings:
        print(finding)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
