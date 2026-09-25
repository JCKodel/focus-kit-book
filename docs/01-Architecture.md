# Architecture

## Design in one sentence

One Markdown file per chapter per edition, built into a bilingual website by MkDocs Material and into PDF and EPUB by pandoc, checked by one `make verify`.

## Stack

| Piece | Choice | Why, when there was an alternative |
|---|---|---|
| Source | Markdown, one sentence per line | Diffs show sentences; the two editions compare line by line. |
| Website | MkDocs Material with the static i18n plugin | Bilingual navigation, search, light and dark themes, native Mermaid. Chosen over a GitHub wiki (ADR-0001) and over Quarto (ADR-0002). |
| PDF and EPUB | pandoc and weasyprint, run by `scripts/build_book.py`; fonts from `pandoc/fonts/` | A pipeline the author already runs for books. The PDF is A5 in Merriweather, Google Sans and Iosevka Term, loaded from the repository so any machine sets the same pages; the EPUB carries no fonts, so the reader's device chooses. |
| Diagrams | not decided | Decided by the first chapter with a diagram, on a real one (ADR-0002, amendment). |
| Automation | GitHub Actions, one workflow with three jobs | `verify` on every push; `pages` after it on `main`; `release` after it on a `v*` tag, with pandoc 3.11 and WeasyPrint 69.0 as the local build (ADR-0014). |
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
scripts/build_book.py    PDF and EPUB of both editions into output/ (rule "book")
scripts/check_disclosure.py no term of the disclosure list in a file path or text file (rule "disclosure"; ADR-0012)
scripts/patterns.py      compile_entry: the entry syntax (plain or re:) shared by the prose and disclosure checks
scripts/markdown.py      front_matter: the fields and the body, shared by parity and the book build; mask: front matter, code and HTML comments as spaces, shared by the prose and link checks
scripts/repo_files.py    the files the checks read: tracked, plus untracked and not ignored
pandoc/pdf.css           the PDF: A5, margins, page numbers, the fonts by @font-face
pandoc/epub.css          the EPUB: no @font-face
pandoc/fonts/            Merriweather (4 styles), Google Sans (variable), Iosevka Term Regular; <Family>-OFL.txt each
.github/workflows/verify.yml  jobs verify (make verify on every push, the list from the secret DISCLOSURE_DENYLIST), pages (main only) and release (v* tags only), each after verify
mkdocs.yml               the site: MkDocs Material, i18n in folder structure, footnotes, no nav: key
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
| `make book` | `scripts/build_book.py`: for each edition, a PDF and an EPUB in `output/` (`one-page-at-a-time.*`, `uma-pagina-de-cada-vez.*`), then their paths. Needs pandoc and weasyprint; not part of `make verify`. Each file: title page, rights page, table of contents, chapters in `NN-` order, appendices in `A<n>-` order; a draft carries its banner, notes end their chapter. Title and subtitle come from `book/<edition>/index.md`, author, rights and banner from `mkdocs.yml`. |
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
`scripts/build_book.py` does the same for pandoc and weasyprint: a message that names a chapter prints as `book/<edition>/<file>:<line>: book: message`, at the chapter's own line; any other as `Makefile:1: book: message`. A failure is one such line and exit 1; a warning is printed and the build goes on. A missing pandoc or weasyprint prints `Makefile:1: book: <tool> not found; install it (see README)`.

## Environments

| Name | What runs there | How it is updated |
|---|---|---|
| local | `make serve` (site), `make book` (PDF and EPUB into `output/`, never committed) | by hand |
| GitHub Actions | `make verify` on every push, any branch, with the list from the secret `DISCLOSURE_DENYLIST` | the author sets the secret; runs on push |
| GitHub Pages | the website, from `main` | job `pages`, on every push to `main` once `verify` is green; one deploy at a time, a stale queued one dropped. Pages source set to "GitHub Actions" once by the author |
| GitHub Release | PDF and EPUB, both editions, under the names of `make book`, so `releases/latest/download/<file>` is the newest | job `release`, on a `v*` tag the author creates, once `verify` is green; a tag with `-` makes a pre-release. The author uploads the files to books.kodel.com.br |

## Tried and removed on purpose

* A GitHub wiki, as the book or as a mirror (ADR-0001).
* Code examples in many languages (ADR-0008).
* A link shortener or playground server for code snippets: the guided project's tagged repository does that job.
* Reusing text from the author's earlier books (ADR-0005).
* The `[?]` mark (ADR-0013).
