# link-check

**Objective.** The author runs `make verify` and it fails, naming the file, the line and the URL, when a text a reader reads points to an external page that is gone; the strict build already does the same for internal links.

**Behaviour.**

* On the clean tree, with network, `python3 scripts/check_links.py` prints nothing and exits 0.
* A URL in `book/en/`, `book/pt/`, `README.md`, `README.pt.md` or `mkdocs.yml` that answers 404, 410 or a 5xx, whose host does not resolve, or whose connection or TLS handshake fails, or that times out, prints `file:line: links: <url>: <reason>` and exits 1.
* A URL that answers 2xx after redirects, or 401, 403 or 429 (the server exists and refuses scripts), passes.
* A 5xx or a timeout is tried once more before it is a finding.
* A URL inside a fenced code block, an inline code span, an HTML comment or the front matter is not checked: an artifact shown is real and may hold URLs that only lived on the author's machine.
* URLs under the site's own `site_url` (from `mkdocs.yml`), `localhost`, `127.0.0.1` and the `example.com`, `example.org` and `example.net` domains are not checked: the first are this repository's pages, not yet published until `pages-and-release`; the others are not meant to answer.
* The same URL in several places is fetched once and reported at each place.
* Offline, locally: when every URL fails at DNS or connection, the check prints `links: skipped, no network` on stderr and exits 0. With `CI` set, the same situation is findings and exit 1, as the disclosure scan does without its list.
* `make verify` runs build, parity, em dash, prose, links, disclosure, in that order, and stops at the first failing group.

**Contract.**

Files:

```
scripts/check_links.py    rule "links"; Python 3 standard library only (urllib, concurrent.futures)
scripts/markdown.py       mask(text, keep_targets) -> list of lines, moved out of check_prose.py
scripts/check_prose.py    imports mask with keep_targets=False; behaviour unchanged
Makefile                  verify runs python3 scripts/check_links.py after the prose check
docs/01-Architecture.md   tree and the make verify row updated
docs/04-Conventions.md    §Tests: "links" names what it checks
```

`mask` is the second concrete occurrence of the Markdown masking (the first is `check_prose.py`, delivery `prose-rules`): it blanks the front matter, fenced code blocks, inline code spans and HTML comments with spaces, keeping line numbers; with `keep_targets=False` it also blanks link and image targets `](…)`, as `check_prose.py` does today.

`scripts/check_links.py`:

* Files: from `repo_files()`, `book/**/*.md`, `README.md`, `README.pt.md` and `mkdocs.yml`. Markdown files go through `mask(text, keep_targets=True)`; `mkdocs.yml` is read as is.
* A URL starts with `http://` or `https://` and runs until whitespace, `<`, `>`, `"`, `'`, a backtick or the end of the line, with trailing `.,;:!?)` stripped; inside a `](…)` target, the URL is the target up to its matching closing parenthesis, so a URL with balanced parentheses survives.
* Skipped: a URL starting with the `site_url` of `mkdocs.yml`; hosts `localhost`, `127.0.0.1`, `example.com`, `example.org`, `example.net` and their subdomains. The `#fragment` is dropped before fetching and never checked.
* Fetch: `GET`, redirects followed, timeout 15 s, header `User-Agent: focus-kit-book link-check (+https://github.com/JCKodel/focus-kit-book)`, body not read. Up to 8 URLs at a time.
* Result per URL: 2xx, 401, 403, 429 pass. 404, 410, other 4xx, DNS failure, connection or TLS error are findings at once; 5xx and timeout after a second try.
* Offline: every fetched URL failed with a DNS or connection error, and there was at least one URL. Without `CI`, print the skip line on stderr, exit 0. With `CI`, the findings as usual.
* Output on stdout, sorted by file and line, exit 1 when there is any:

```
<file>:<line>: links: <url>: HTTP <status>
<file>:<line>: links: <url>: host not found
<file>:<line>: links: <url>: connection failed: <reason>
<file>:<line>: links: <url>: timed out
```

**Out of scope.**

* Anchors (`#section`): need the page parsed; no broken anchor has happened yet.
* Relative links in the READMEs (`LICENSE`, `README.pt.md`): the build does not see them, but none has broken (docs/05 §7).
* An allowlist of URLs that fail: added when the first false positive happens.
* `docs/` and `work/`: process documents, not read by a reader of the book.
* A cache between runs: a few dozen URLs take seconds.

**Done when.**

* [x] With an untracked `book/en/99-probe.md` and `book/pt/99-probe.md` holding a 200, a 404, a 410, a 403, an unresolvable host, a URL under `site_url`, a `localhost` URL, and the 404 again inside a code fence, an inline code span and an HTML comment, the output is exactly the 404 (at each prose place, not in code), the 410 and the host finding, exit 1. Output recorded on this page; probes removed.
* [x] With the network off (or DNS pointed nowhere), locally: the skip line, exit 0; with `CI=true`: findings, exit 1.
* [x] `check_prose.py` gives the same result as before on its recorded probes after `mask` moves.
* [x] The existing chapters, both READMEs and `mkdocs.yml` pass; any finding there is fixed in both editions and recorded here.
* [x] `make verify` green; with a 404 probe planted, it stops at links.
* [ ] The verify workflow in Actions green on the push that brings this delivery (the author pushes; the run is recorded here).
* [x] docs/01 and docs/04 updated; docs/06 line marked `[x]`.

**What happened.**

Diverged from the plan:

* `scripts/markdown.py` also exports `target_end`, the matching-parenthesis scan of a `](…)` target: `mask` uses it to blank a target, and `check_links.py` uses it to take a target whole, so a URL with balanced parentheses survives.
* A link target is the target up to its first whitespace, so `[a](url "title")` gives `url`.
* A malformed URL that `urllib` refuses prints as `connection failed: <reason>` and does not count toward "offline".
* The offline proof did not turn the machine's network off: `http_proxy` and `https_proxy` pointed at a closed port (`127.0.0.1:9`) and at an unresolvable host (`nowhere.invalid`) make every fetch fail at connection or DNS, which is the situation the check tests.

Nothing dropped.

The proof found:

```
clean tree                       python3 scripts/check_links.py: no output, exit 0, under a second

book/en/99-probe.md and book/pt/99-probe.md, untracked: a 200 (<https://www.google.com/>, and again
with #top), the 404 (github.com/JCKodel/does-not-exist-probe) in prose, a 410 as a link target
(httpbin.org/status/410), a 403 (httpbin.org/status/403), no-such-host.invalid, a URL under site_url,
localhost, 127.0.0.1 and www.example.org, a Wikipedia link with balanced parentheses; the 404 again
in the front matter, a ``` fence, an inline code span and an HTML comment; the pt probe holds the 404
as a link target with a title, and the 410 in a ~~~ fence:
book/en/99-probe.md:7: links: https://github.com/JCKodel/does-not-exist-probe: HTTP 404
book/en/99-probe.md:8: links: https://httpbin.org/status/410: HTTP 410
book/en/99-probe.md:10: links: https://no-such-host.invalid/page: host not found
book/pt/99-probe.md:3: links: https://github.com/JCKodel/does-not-exist-probe: HTTP 404
                                 exit 1; the trailing "." after the en 404 stripped; probes removed

offline, http(s)_proxy at 127.0.0.1:9:       links: skipped, no network (stderr), exit 0
offline, http(s)_proxy at nowhere.invalid:9: links: skipped, no network (stderr), exit 0
the same with CI=true:                       one "host not found" per URL place
                                             (READMEs, mkdocs.yml, the probes), exit 1

retries, fetch_once counted:     503: 2 tries, HTTP 503; timeout (1 s against a 5 s delay): 2 tries,
                                 timed out; 404: 1 try; 429: 1 try, passes

check_prose.py after mask moved: the prose-rules probes rebuilt from its page give the same 14 lines,
                                 byte for byte; mask(keep_targets=False) gives the same lines as the old
                                 prose_lines on every Markdown file of book/, docs/, work/ and the READMEs
```

* The existing chapters, both `index.md`, both READMEs and `mkdocs.yml` pass: nothing to fix. Their URLs today are books.kodel.com.br, github.com (the method's repository and this one's releases), creativecommons.org and gnu.org; the README's `http://127.0.0.1:8000/` and the `site_url` ones are skipped.
* `make verify` green, links run between prose and disclosure; with a 404 planted in `book/en/99-probe.md` (and a clean pt twin, so parity passes) it ran build, parity, em dash and prose, then stopped at `book/en/99-probe.md:3: links: https://github.com/JCKodel/does-not-exist-probe: HTTP 404`, exit 2 from make; removed, green.
* The Actions run is left open: the author pushes, and records the run here.
* No screen changes, so no screenshot: the proof is the runs above.

Decisions: none beyond the page. No ADR.

Documents this delivery changed: docs/01 (tree, `make verify`), docs/04 (§Tests), docs/06.
