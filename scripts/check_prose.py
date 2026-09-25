#!/usr/bin/env python3
"""Check the text a reader reads against the prose rules of docs/04.

The rules live only in docs/04, section "## Prose rules"; this script holds no pattern.
Prints one line per finding as `file:line: prose: message`; exits 1 when anything is printed.
"""

import re
import sys

from patterns import compile_entry
from repo_files import ROOT, repo_files

CONVENTIONS = "docs/04-Conventions.md"
SECTION = "## Prose rules"
RULE = re.compile(r"### ([a-z-]+)\s*$")
PATTERNS = re.compile(r"\* (en|pt|both):")
SPAN = re.compile(r"`([^`]+)`")


def load():
    """Return (rules, findings): rules as a list of (id, message, language, compiled pattern)."""
    lines = (ROOT / CONVENTIONS).read_text(encoding="utf-8").split("\n")
    headings, entries, findings = [], [], []
    start = next((i for i, line in enumerate(lines) if line.rstrip() == SECTION), None)
    if start is not None:
        for number, line in enumerate(lines[start + 1:], start + 2):
            if line.startswith("## "):
                break
            heading = RULE.match(line)
            if heading:
                headings.append({"id": heading.group(1), "line": number, "message": None})
                continue
            if not headings or not line.strip():
                continue
            rule = headings[-1]
            kind = PATTERNS.match(line)
            if kind:
                for entry in SPAN.findall(line):
                    try:
                        entries.append((rule, kind.group(1), compile_entry(entry)))
                    except re.error:
                        findings.append(f"{CONVENTIONS}:{number}: prose: invalid regular expression")
            elif rule["message"] is None and not line.lstrip().startswith(("* ", "- ")):
                rule["message"] = line.strip()
    if not headings:
        return [], [f'{CONVENTIONS}:1: prose: section "{SECTION}" missing or has no rule']
    for rule in headings:
        if rule["message"] is None:
            findings.append(f"{CONVENTIONS}:{rule['line']}: prose: rule {rule['id']} has no message")
    return [(r["id"], r["message"] or "", language, pattern) for r, language, pattern in entries], findings


def language_of(path):
    name = path.as_posix()
    if name == "README.md" or (name.startswith("book/en/") and name.endswith(".md")):
        return "en"
    if name == "README.pt.md" or (name.startswith("book/pt/") and name.endswith(".md")):
        return "pt"
    return None


def blank(text):
    return " " * len(text)


def prose_lines(text):
    """Return the lines of text with front matter, code, link targets and HTML comments as spaces."""
    lines = text.split("\n")
    out = []
    front = bool(lines) and lines[0].strip() == "---"
    fence = None
    comment = False
    for index, line in enumerate(lines):
        if front:
            out.append(blank(line))
            if index > 0 and line.strip() == "---":
                front = False
            continue
        if fence:
            out.append(blank(line))
            if line.lstrip().startswith(fence):
                fence = None
            continue
        if not comment:
            opening = re.match(r"\s*(`{3,}|~{3,})", line)
            if opening:
                fence = opening.group(1)
                out.append(blank(line))
                continue
        kept, comment = mask_inline(line, comment)
        out.append(kept)
    return out


def mask_inline(line, comment):
    """Blank inline code, link targets and HTML comments; return (line, still inside a comment)."""
    chars = list(line)
    i = 0
    while i < len(line):
        if comment:
            end = line.find("-->", i)
            stop = len(line) if end < 0 else end + 3
            chars[i:stop] = blank(line[i:stop])
            i = stop
            comment = end < 0
            continue
        if line.startswith("<!--", i):
            comment = True
            continue
        if line[i] == "`":
            run = re.match(r"`+", line[i:]).group(0)
            end = line.find(run, i + len(run))
            if end < 0:
                i += len(run)
                continue
            stop = end + len(run)
            chars[i:stop] = blank(line[i:stop])
            i = stop
            continue
        if line.startswith("](", i):
            depth, j = 0, i + 1
            while j < len(line):
                if line[j] == "(":
                    depth += 1
                elif line[j] == ")":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            chars[i + 1:j + 1] = blank(line[i + 1:j + 1])
            i = j + 1
            continue
        i += 1
    return "".join(chars), comment


def check(rules):
    findings = []
    for path in repo_files():
        language = language_of(path)
        if language is None:
            continue
        text = (ROOT / path).read_text(encoding="utf-8")
        for number, line in enumerate(prose_lines(text), 1):
            line = line.strip()
            if not line:
                continue
            for rule_id, message, rule_language, pattern in rules:
                if rule_language not in (language, "both"):
                    continue
                for match in pattern.finditer(line):
                    findings.append(f'{path}:{number}: prose: {rule_id}: "{match.group(0)}": {message}')
    return findings


def main():
    rules, findings = load()
    findings += check(rules)
    for finding in findings:
        print(finding)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
