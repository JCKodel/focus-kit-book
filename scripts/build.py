#!/usr/bin/env python3
"""Build the site with `mkdocs build --strict` and report its warnings as findings.

Run with the Python of `.venv`. Prints one line per finding as `file:line: build: message`;
exits 1 when anything is printed or the build fails.
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = Path("book")
CONFIG = "mkdocs.yml"

PROBLEM = re.compile(r"^(?:WARNING|ERROR)\s+-\s+(.*)$")
DOC_FILE = re.compile(r"Doc file '([^']+)'")
LINK = re.compile(r"contains a link '([^']+)'")


def locate(message):
    """Return (file, line) for a MkDocs message: the doc file and the line of the link, when named."""
    doc = DOC_FILE.search(message)
    if not doc:
        return CONFIG, 1
    path = DOCS / doc.group(1)
    link = LINK.search(message)
    if link and (ROOT / path).is_file():
        lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
        for number, line in enumerate(lines, 1):
            if f"({link.group(1)}" in line or f"]: {link.group(1)}" in line:
                return path, number
    return path, 1


def main():
    result = subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict"],
        cwd=ROOT, capture_output=True, text=True,
    )
    output = (result.stdout + result.stderr).splitlines()
    findings = []
    for line in output:
        match = PROBLEM.match(line.strip())
        if match:
            message = " ".join(match.group(1).split())
            path, number = locate(message)
            findings.append(f"{path}:{number}: build: {message}")
    if result.returncode != 0 and not findings:
        last = next((line.strip() for line in reversed(output) if line.strip()), "build failed")
        findings.append(f"{CONFIG}:1: build: {last}")
    for finding in findings:
        print(finding)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
