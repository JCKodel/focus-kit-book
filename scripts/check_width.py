#!/usr/bin/env python3
"""Check that no row of a fenced block runs past what an A5 page of the PDF holds.

Reads the files the prose check reads: both editions and both READMEs.
Every fenced block is measured but TypeScript (`ts` or `typescript` as the first word of the info string, whatever its case), which may wrap (docs/04, "Width of a block").
Front matter and HTML comments are skipped, as `mask` skips them: no reader is shown a block there.
A column is a character; a tab runs to the next multiple of 8.
Prints one line per finding as `file:line: width: message`; exits 1 when anything is printed.
"""

import sys

from check_prose import language_of
from markdown import line_kinds
from repo_files import ROOT, repo_files

# docs/04 "Width of a block": 74 columns is what an A5 page holds at the PDF's code size.
LIMIT = 74
# pandoc/pdf.css sets no tab-size, so the browser's default of 8 applies.
TAB_SIZE = 8
UNMEASURED = {"ts", "typescript"}


def check(path, text):
    findings = []
    for number, (line, (kind, info)) in enumerate(zip(text.split("\n"), line_kinds(text)), 1):
        if kind != "code":
            continue
        words = info.split()
        if words and words[0].lower() in UNMEASURED:
            continue
        width = len(line.expandtabs(TAB_SIZE))
        if width > LIMIT:
            findings.append(f"{path}:{number}: width: {width} columns; a code block keeps to {LIMIT} (docs/04)")
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
