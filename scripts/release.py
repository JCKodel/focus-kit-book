#!/usr/bin/env python3
"""Publish the book: push main and a new v* tag, so the release job builds the PDF and EPUB of both editions.

Usage: release.py [patch|minor|major] (patch by default). The next tag bumps the newest vX.Y.Z tag.
Refuses unless on main with a clean tree, not behind origin/main, with commits since the newest tag and
`make verify` green; asks before pushing. Prints `Makefile:1: release: message` and exits 1 on a refusal.
"""

import re
import subprocess
import sys

TAG = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")
BUMPS = ("patch", "minor", "major")
REPOSITORY = "https://github.com/JCKodel/focus-kit-book"


def fail(message):
    print(f"Makefile:1: release: {message}")
    sys.exit(1)


def git(*args):
    result = subprocess.run(["git", *args], capture_output=True, text=True)
    if result.returncode != 0:
        fail(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def next_tag(tags, bump):
    """Return the tag after the newest vX.Y.Z in tags, and that newest tag (None when there is none)."""
    versions = sorted(tuple(int(n) for n in match.groups()) for match in map(TAG.match, tags) if match)
    if not versions:
        return "v1.0.0", None
    major, minor, patch = versions[-1]
    newest = f"v{major}.{minor}.{patch}"
    if bump == "major":
        return f"v{major + 1}.0.0", newest
    if bump == "minor":
        return f"v{major}.{minor + 1}.0", newest
    return f"v{major}.{minor}.{patch + 1}", newest


def main():
    bump = sys.argv[1] if len(sys.argv) > 1 else "patch"
    if bump not in BUMPS:
        fail(f"BUMP must be one of {', '.join(BUMPS)}, not {bump!r}")

    if git("rev-parse", "--abbrev-ref", "HEAD") != "main":
        fail("not on main; the book is released from main")
    if git("status", "--porcelain"):
        fail("the tree has uncommitted changes; commit or stash them first")
    git("fetch", "--quiet", "--tags", "origin")
    if int(git("rev-list", "--count", "main..origin/main")):
        fail("main is behind origin/main; pull first")

    tag, newest = next_tag(git("tag", "--list", "v*").splitlines(), bump)
    if newest and git("rev-parse", f"{newest}^{{commit}}") == git("rev-parse", "HEAD"):
        fail(f"main is already released as {newest}; nothing new to publish")

    if subprocess.run(["make", "verify"]).returncode != 0:
        fail("make verify is not green; the release job would refuse the tag")

    since = git("log", "--oneline", f"{newest}..HEAD") if newest else git("log", "--oneline")
    print(f"\nRelease {tag} (after {newest or 'no tag'}) from main at {git('rev-parse', '--short', 'HEAD')}:")
    print(since)
    if input(f"\nPush main and tag {tag}? [y/N] ").strip().lower() not in ("y", "yes", "s", "sim"):
        fail("cancelled; nothing was pushed")

    git("push", "origin", "main")
    git("tag", "-a", tag, "-m", tag)
    git("push", "origin", tag)
    print(f"\n{tag} pushed. The release job builds it: {REPOSITORY}/actions")
    print(f"When it ends, the files are at {REPOSITORY}/releases/tag/{tag}")


if __name__ == "__main__":
    main()
