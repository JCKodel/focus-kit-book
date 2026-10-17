#!/usr/bin/env python3
"""Check that no row of a fenced block runs past what an A5 page of the PDF holds.

Reads the files the prose check reads: both editions and both READMEs.
Every fenced block is measured but TypeScript (`ts`, `typescript`), which may wrap (docs/04, "Width of a block").
A column is a character; a tab runs to the next multiple of 8.
Prints one line per finding as `file:line: width: message`; exits 1 when anything is printed.
"""

import sys

from check_prose import language_of
from markdown import FENCE_OPENING, closes
from repo_files import ROOT, repo_files

# docs/04 "Width of a block": 74 columns is what an A5 page holds at the PDF's code size.
LIMIT = 74
# pandoc/pdf.css sets no tab-size, so the browser's default of 8 applies.
TAB_SIZE = 8
UNMEASURED = {"ts", "typescript"}


def check(path, text):
    findings = []
    fence, measured = None, False
    for number, line in enumerate(text.split("\n"), 1):
        if fence:
            if closes(line, fence):
                fence = None
                continue
            width = len(line.expandtabs(TAB_SIZE))
            if measured and width > LIMIT:
                findings.append(f"{path}:{number}: width: {width} columns; a code block keeps to {LIMIT} (docs/04)")
            continue
        opening = FENCE_OPENING.match(line)
        if opening:
            fence = opening.group(1)
            words = opening.group(2).split()
            measured = not words or words[0].lower() not in UNMEASURED
    return findings


def main():
    findings = []
    for path in repo_files():
        if language_of(path) is None:
            continue
        findings += check(path, (ROOT / path).read_text(encoding="utf-8"))
    for finding in findings:
        print(finding)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
