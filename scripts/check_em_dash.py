#!/usr/bin/env python3
"""Check that no text file in the repository contains an em dash.

Prints one line per finding as `file:line: em-dash: message`; exits 1 when anything is printed.
"""

import sys

from repo_files import ROOT, repo_files

EM_DASH = "\u2014"
EXTENSIONS = {".md", ".yml", ".yaml", ".html", ".css", ".py", ".txt", ".toml"}
MESSAGE = "em dash found; use a comma, a colon, parentheses or a new sentence"


def main():
    findings = []
    for path in repo_files():
        if path.suffix not in EXTENSIONS:
            continue
        text = (ROOT / path).read_text(encoding="utf-8", errors="replace")
        for number, line in enumerate(text.splitlines(), 1):
            if EM_DASH in line:
                findings.append(f"{path}:{number}: em-dash: {MESSAGE}")
    for finding in findings:
        print(finding)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
