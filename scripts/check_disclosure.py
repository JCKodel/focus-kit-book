#!/usr/bin/env python3
"""Check that no term of the disclosure list appears in the repository (ADR-0012).

The list lives outside the repository: `FKB_DENYLIST`, or `~/.config/focus-kit-book/denylist.txt`.
Prints one line per finding as `file:line: disclosure: message`; exits 1 when anything is printed.
A finding never shows the term or the matched text: a matched part of a path is printed as `***`.
"""

import os
import re
import sys
from pathlib import Path

from patterns import compile_entry
from repo_files import ROOT, repo_files

DEFAULT_LIST = Path.home() / ".config" / "focus-kit-book" / "denylist.txt"
MASK = "***"


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


def text_of(path):
    data = (ROOT / path).read_bytes()
    if b"\0" in data:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return None


def scan(entries):
    findings = []
    for path in repo_files():
        name = path.as_posix()
        shown = name
        for _, pattern in entries:
            shown = pattern.sub(MASK, shown)
        for number, pattern in entries:
            if pattern.search(name):
                findings.append(f"{shown}:1: disclosure: file path matches list entry {number}")
        text = text_of(path)
        if text is None:
            continue
        for line_number, line in enumerate(text.split("\n"), 1):
            for number, pattern in entries:
                if pattern.search(line):
                    findings.append(f"{shown}:{line_number}: disclosure: matches list entry {number}")
    return findings


def main():
    path = list_path()
    if not path.is_file():
        if not os.environ.get("CI"):
            print("disclosure: skipped, no list", file=sys.stderr)
            return 0
        findings = [f"{path}:1: disclosure: list is missing or has no entry"]
    else:
        entries, findings = load(path)
        if not entries and not findings:
            findings = [f"{path}:1: disclosure: list is missing or has no entry"]
        findings += scan(entries)
    for finding in findings:
        print(finding)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
