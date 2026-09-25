# Architecture

## Design in one sentence

One Markdown file per chapter per edition, built into a bilingual website by MkDocs Material and into PDF and EPUB by pandoc, checked by one `make verify`.

## Stack

| Piece | Choice | Why, when there was an alternative |
|---|---|---|
| Source | Markdown, one sentence per line | Diffs show sentences; the two editions compare line by line. |
| Website | MkDocs Material with the static i18n plugin | Bilingual navigation, search, light and dark themes, native Mermaid. Chosen over a GitHub wiki (ADR-0001) and over Quarto (ADR-0002). |
| PDF and EPUB | pandoc, weasyprint, mermaid-cli | A pipeline the author already runs for books; installed on the author's machine. |
| Diagrams | Mermaid in the Markdown | Text in the repository, rendered by both outputs. |
| Automation | GitHub Actions | `make verify` on every push; Pages on push to `main`; Release on a `v*` tag (ADR-0014). |
| Scripts | Make, and Python 3 for checks | Nothing to install beyond what the build already needs. |

## How the repository is organized

FOCUS does not apply: there is no product code, only content and a few build scripts (ADR-0011).

```
book/en/NN-<slug>.md     English edition, the source (A1-<slug>.md for appendices)
book/pt/NN-<slug>.md     Portuguese edition, same file names
book/assets/             images and figures shared by both editions; site.css (the draft mark in the navigation)
overrides/main.html      theme override: the draft banner
scripts/build.py         strict site build, warnings as findings (rule "build")
scripts/check_parity.py  the two editions: same chapters, heading levels and status (rule "parity")
scripts/check_em_dash.py no em dash in any text file (rule "em-dash")
scripts/check_prose.py   the prose rules of docs/04 in both editions and both READMEs (rule "prose")
scripts/check_links.py   every external URL in both editions, both READMEs and mkdocs.yml still answers (rule "links")
scripts/check_disclosure.py no term of the disclosure list in a file path or text file (rule "disclosure"; ADR-0012)
scripts/patterns.py      compile_entry: the entry syntax (plain or re:) shared by the prose and disclosure checks
scripts/markdown.py      mask: front matter, code and HTML comments as spaces, shared by the prose and link checks
scripts/repo_files.py    the files the checks read: tracked, plus untracked and not ignored
.github/workflows/verify.yml  make verify on every push, the list from the secret DISCLOSURE_DENYLIST
mkdocs.yml               the site: MkDocs Material, i18n in folder structure, no nav: key
requirements.txt         mkdocs-material and mkdocs-static-i18n, exact versions
Makefile                 the targets below
docs/, work/             the process documents and the deliveries
README.md, README.pt.md  what the book is, where to read it, how to build and contribute, which license covers what
LICENSE                  AGPL-3.0 text: scripts, build and site configuration (ADR-0003)
LICENSE-TEXT             CC BY-SA 4.0 legal code: the book, docs/, work/, the READMEs (ADR-0003)
.venv/                   created by make from requirements.txt; ignored
site/                    the built site; ignored
output/                  PDF and EPUB; ignored
__pycache__/             written by Python when a check imports a module of scripts/; ignored
```

| Target | Does |
|---|---|
| `.venv` | `python3 -m venv .venv` and `pip install -r requirements.txt`; rebuilt when `requirements.txt` changes. Only Python 3 is needed beforehand. |
| `make serve` | `mkdocs serve`, at `http://127.0.0.1:8000/`, which redirects to `/focus-kit-book/` (the path of `site_url`); Portuguese under `pt/`. |
| `make build` | `scripts/build.py`: `mkdocs build --strict` into `site/`. |
| `make verify` | build, then parity, then em dash, then prose, then links, then disclosure; stops at the first failing group. The link check needs the network: offline it is skipped locally and fails in Actions (`CI` set). |
| `make scan` | the disclosure scan alone. The list is `FKB_DENYLIST`, or `~/.config/focus-kit-book/denylist.txt`; one entry per line, `#` comments, `re:<pattern>` for a regular expression. Without a list it is skipped locally and fails in Actions (`CI` set). A finding names the file, the line and the entry's number in the list, never the term; a matched part of a path prints as `***`. |

The navigation comes from the file names in `NN-` order, with each chapter's H1 as its title.

The file name of a chapter is the same in both editions, so parity is checked by name.
Code of the guided project lives in its own repository (OD-2); the book shows it by quoting a tagged file, never by keeping a copy here.

## Data

There is no data store.
The disclosure list, the terms that must never appear in the repository, lives outside it (ADR-0012).
Source material for the cases lives in the author's private folders and is never linked from here.

## How errors travel

Every check prints `file:line: rule: message` and exits non-zero.
`make verify` runs them all and stops at the first failing group.
The site build runs with `--strict`, so a broken link or a missing page fails the build.
MkDocs has its own message format, so `scripts/build.py` rewrites each warning as `file:line: build: message`: the doc file MkDocs names, at the line of the broken link, or line 1 when there is none; a warning that names no file points to `mkdocs.yml:1`.

## Environments

| Name | What runs there | How it is updated |
|---|---|---|
| local | `make serve` (site), `make book` (PDF and EPUB into `output/`, never committed) | by hand |
| GitHub Actions | `make verify` on every push, any branch, with the list from the secret `DISCLOSURE_DENYLIST` | the author sets the secret; runs on push |
| GitHub Pages | the website, from `main` | Actions, on every push to `main` |
| GitHub Release | PDF and EPUB, both editions | Actions, on a `v*` tag the author creates; the author uploads them to books.kodel.com.br |

## Tried and removed on purpose

* A GitHub wiki, as the book or as a mirror (ADR-0001).
* Code examples in many languages (ADR-0008).
* A link shortener or playground server for code snippets: the guided project's tagged repository does that job.
* Reusing text from the author's earlier books (ADR-0005).
* The `[?]` mark (ADR-0013).
