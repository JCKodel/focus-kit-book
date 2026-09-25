#!/usr/bin/env python3
"""Check that the two editions of the book have the same chapters, heading levels and status.

Prints one line per finding as `file:line: parity: message`; exits 1 when anything is printed.
"""

import re
import sys
from pathlib import Path

from markdown import front_matter

ROOT = Path(__file__).resolve().parent.parent
EN = Path("book/en")
PT = Path("book/pt")

HEADING = re.compile(r"^ {0,3}(#{1,6})(?:\s|$)")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")


def read(path):
    """Return (lines, headings, status): headings as (level, line number), status or "none"."""
    text = (ROOT / path).read_text(encoding="utf-8")
    fields, body = front_matter(text)
    lines = text.splitlines()
    start = len(lines) - len(body)
    status = fields.get("status") or "none"
    headings = []
    fence = None
    for number, line in enumerate(lines[start:], start + 1):
        match = FENCE.match(line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is None:
            match = HEADING.match(line)
            if match:
                headings.append((len(match.group(1)), number))
    return lines, headings, status


def compare(en, pt):
    findings = []
    _, en_headings, en_status = read(en)
    pt_lines, pt_headings, pt_status = read(pt)
    if pt_status != en_status:
        findings.append(f'{pt}:1: parity: status "{pt_status}", English has "{en_status}"')
    for (en_level, en_line), (pt_level, pt_line) in zip(en_headings, pt_headings):
        if en_level != pt_level:
            findings.append(
                f"{pt}:{pt_line}: parity: heading level {pt_level}, "
                f"English has level {en_level} at {en}:{en_line}"
            )
    if len(pt_headings) != len(en_headings):
        findings.append(
            f"{pt}:{max(len(pt_lines), 1)}: parity: {len(pt_headings)} headings, "
            f"English has {len(en_headings)}"
        )
    return findings


def main():
    en_names = {p.name for p in (ROOT / EN).glob("*.md")}
    pt_names = {p.name for p in (ROOT / PT).glob("*.md")}
    findings = []
    for name in sorted(en_names | pt_names):
        if name not in pt_names:
            findings.append(f"{EN / name}:1: parity: no Portuguese counterpart {PT / name}")
        elif name not in en_names:
            findings.append(f"{PT / name}:1: parity: no English counterpart {EN / name}")
        else:
            findings.extend(compare(EN / name, PT / name))
    for finding in findings:
        print(finding)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
