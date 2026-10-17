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
    """Return every (file, line) of a MkDocs message: the doc file and each line holding the link, when named."""
    doc = DOC_FILE.search(message)
    if not doc:
        return [(CONFIG, 1)]
    path = DOCS / doc.group(1)
    link = LINK.search(message)
    if link and (ROOT / path).is_file():
        target = re.compile(r"(?:\(<?|\]:\s*)" + re.escape(link.group(1)) + r"(?=$|[\s)>])")
        lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
        found = [(path, number) for number, line in enumerate(lines, 1) if target.search(line)]
        if found:
            return found
    return [(path, 1)]


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
            for path, number in locate(message):
                finding = f"{path}:{number}: build: {message}"
                if finding not in findings:
                    findings.append(finding)
    if result.returncode != 0 and not findings:
        last = next((line.strip() for line in reversed(output) if line.strip()), "build failed")
        findings.append(f"{CONFIG}:1: build: {last}")
    for finding in findings:
        print(finding)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
