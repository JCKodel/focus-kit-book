#!/usr/bin/env python3
"""Check that the two editions of the book have the same chapters, heading levels, status and note keys,
and that the two READMEs have the same headings at the same levels.

Prints one line per finding as `file:line: parity: message`; exits 1 when anything is printed.
"""

import re
import sys
from collections import Counter
from pathlib import Path

from markdown import NOTE_DEFINITION, front_matter, mask, mentions

ROOT = Path(__file__).resolve().parent.parent
EN = Path("book/en")
PT = Path("book/pt")
README_EN = Path("README.md")
README_PT = Path("README.pt.md")

HEADING = re.compile(r"^ {0,3}(#{1,6})(?:\s|$)")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")


def notes(path):
    """Return (count of mentions per key, first line of each key): mentions outside code, definition lines as fallback."""
    text = (ROOT / path).read_text(encoding="utf-8")
    counts, mentioned, defined = Counter(), {}, {}
    for number, line in enumerate(mask(text, keep_targets=False), 1):
        definition = NOTE_DEFINITION.match(line)
        if definition:
            defined.setdefault(definition.group(1), number)
        for key in mentions(line):
            counts[key] += 1
            mentioned.setdefault(key, number)
    return counts, {**defined, **mentioned}


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
    en_counts, _ = notes(en)
    pt_counts, pt_first = notes(pt)
    for key in sorted(en_counts.keys() | pt_counts.keys()):
        if en_counts[key] != pt_counts[key]:
            findings.append(
                f"{pt}:{pt_first.get(key, 1)}: parity: [^{key}] cited {pt_counts[key]} times, "
                f"{en_counts[key]} in {en}"
            )
    return findings


def pair(en, pt):
    """Compare en and pt when both exist; else the finding of the one missing."""
    has_en, has_pt = (ROOT / en).is_file(), (ROOT / pt).is_file()
    if has_en and has_pt:
        return compare(en, pt)
    if has_en:
        return [f"{en}:1: parity: no Portuguese counterpart {pt}"]
    if has_pt:
        return [f"{pt}:1: parity: no English counterpart {en}"]
    return []


def main():
    en_names = {p.name for p in (ROOT / EN).glob("*.md")}
    pt_names = {p.name for p in (ROOT / PT).glob("*.md")}
    findings = []
    for name in sorted(en_names | pt_names):
        findings.extend(pair(EN / name, PT / name))
    findings.extend(pair(README_EN, README_PT))
    for finding in findings:
        print(finding)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
