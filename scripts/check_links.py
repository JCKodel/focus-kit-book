#!/usr/bin/env python3
"""Check that every external URL a reader can follow still answers.

Reads both editions of the book, both READMEs and mkdocs.yml; code, HTML comments and the
front matter of a Markdown file are not read, because an artifact shown is real.
Prints one line per finding as `file:line: links: <url>: <reason>`; exits 1 when anything is printed.
Offline (every URL fails at DNS or connection) it is skipped locally and fails in Actions (`CI` set).
"""

import http.client
import os
import re
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from markdown import mask, target_end
from repo_files import ROOT, repo_files

CONFIG = "mkdocs.yml"
READMES = ("README.md", "README.pt.md")
SKIPPED_HOSTS = ("localhost", "127.0.0.1", "example.com", "example.org", "example.net")
USER_AGENT = "focus-kit-book link-check (+https://github.com/JCKodel/focus-kit-book)"
TIMEOUT = 15
WORKERS = 8
PASSING = (401, 403, 429)
URL = re.compile(r"https?://[^\s<>\"'`]+")
TRAILING = ".,;:!?)"


def site_url():
    match = re.search(r"^site_url:\s*[\"']?([^\s\"']+)", (ROOT / CONFIG).read_text(encoding="utf-8"), re.M)
    return match.group(1) if match else None


def files():
    for path in repo_files():
        name = path.as_posix()
        if (name.startswith("book/") and name.endswith(".md")) or name in READMES:
            yield path, mask((ROOT / path).read_text(encoding="utf-8"), keep_targets=True)
        elif name == CONFIG:
            yield path, (ROOT / path).read_text(encoding="utf-8").split("\n")


def urls_in(line):
    """Return (column, url) for each URL on the line; a link target keeps its balanced parentheses."""
    found = []
    chars = list(line)
    i = line.find("](")
    while i >= 0:
        end = target_end(line, i)
        target = (line[i + 2:end].split() or [""])[0]
        if target.startswith(("http://", "https://")):
            found.append((i + 2, target))
            chars[i + 2:end] = " " * (end - i - 2)
        i = line.find("](", end)
    rest = "".join(chars)
    for match in URL.finditer(rest):
        url = match.group(0).rstrip(TRAILING)
        if len(url) > len("https://"):
            found.append((match.start(), url))
    return sorted(found)


def skipped(url, own):
    if own and url.startswith(own):
        return True
    host = (urllib.parse.urlsplit(url).hostname or "").lower()
    return any(host == name or host.endswith("." + name) for name in SKIPPED_HOSTS)


def fetch_once(url):
    """Return (kind, reason): kind is ok, http, dns, connection, timeout or invalid."""
    request = urllib.request.Request(
        urllib.parse.quote(url, safe=":/?#[]@!$&'()*+,;=%~"),
        headers={"User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            status = response.status
    except urllib.error.HTTPError as error:
        status = error.code
    except urllib.error.URLError as error:
        return failure(error.reason)
    except (OSError, http.client.HTTPException) as error:
        return failure(error)
    except ValueError as error:
        return "invalid", f"connection failed: {error}"
    if 200 <= status < 300 or status in PASSING:
        return "ok", None
    return "http", f"HTTP {status}"


def failure(reason):
    if isinstance(reason, socket.gaierror):
        return "dns", "host not found"
    if isinstance(reason, (TimeoutError, socket.timeout)):
        return "timeout", "timed out"
    return "connection", f"connection failed: {reason}"


def fetch(url):
    kind, reason = fetch_once(url)
    if kind == "timeout" or reason and reason.startswith("HTTP 5"):
        kind, reason = fetch_once(url)
    return kind, reason


def main():
    own = site_url()
    places = {}
    for path, lines in files():
        for number, line in enumerate(lines, 1):
            for column, url in urls_in(line):
                if skipped(url, own):
                    continue
                places.setdefault(url.split("#")[0], []).append((path.as_posix(), number, column, url))
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = dict(zip(places, pool.map(fetch, places)))
    offline = results and all(kind in ("dns", "connection") for kind, _ in results.values())
    if offline and not os.environ.get("CI"):
        print("links: skipped, no network", file=sys.stderr)
        return 0
    findings = []
    for target, (kind, reason) in results.items():
        if kind != "ok":
            findings += [(name, number, column, url, reason) for name, number, column, url in places[target]]
    for name, number, _, url, reason in sorted(findings):
        print(f"{name}:{number}: links: {url}: {reason}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
