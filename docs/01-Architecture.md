# Architecture

## Design in one sentence

One Markdown file per chapter per edition, built into a bilingual website by MkDocs Material and into PDF and EPUB by pandoc, checked by one `make verify`.

## Stack

| Piece | Choice | Why, when there was an alternative |
|---|---|---|
| Source | Markdown, one sentence per line | Diffs show sentences; the two editions compare line by line. |
| Website | MkDocs Material with the static i18n plugin | Bilingual navigation, search, light and dark themes. Chosen over a GitHub wiki (ADR-0001) and over Quarto (ADR-0002). |
| PDF and EPUB | pandoc, weasyprint and pypdf, run by `scripts/build_book.py`; fonts from `pandoc/fonts/`; covers from `book/assets/` | A pipeline the author already runs for books. The PDF is A5 in Merriweather (body), Instrument Serif (titles) and Iosevka Term (code), loaded from the repository so any machine sets the same pages, and opens on the edition's cover, a one-page A5 PDF that pypdf prepends (weasyprint cannot place a PDF); the EPUB carries no fonts, so the reader's device chooses, and takes the cover as a PNG through pandoc. |
| Diagrams | SVG written by hand, one per edition, in `book/assets/` | No tool to install, and the site, the PDF and the EPUB show SVG as they are; Mermaid would bring mermaid-cli and a browser back into the build (ADR-0002, amendment of `how-agents-see`). |
| Automation | GitHub Actions, one workflow with three jobs | `verify` on every push; `pages` after it on `main`; `release` after it on a `v*` tag, with pandoc 3.11 and WeasyPrint 69.0 as the local build (ADR-0014). |
| Scripts | Make, and Python 3 for checks | Nothing to install beyond what the build already needs. |

## How the repository is organized

FOCUS does not apply: there is no product code, only content and a few build scripts (ADR-0011).

```
book/en/NN-<slug>.md     English edition, the source (A1-<slug>.md for appendices)
book/pt/NN-<slug>.md     Portuguese edition, same file names
book/assets/             images shared by both editions, diagrams one per edition (NN-<what>.<edition>.svg); screenshots one for both (NN-<what>.png); the covers, cover-<edition>.pdf (A5, one page, the PDF's first page), cover-<edition>.png (the EPUB's cover image) and cover-<edition>.af (their source, Affinity); site.css (the draft mark in the navigation, a border and a width for PNGs, the note box, notes at 66%, italic, links, quotations and code upright)
overrides/main.html      theme override: the draft banner
scripts/build.py         strict site build, warnings as findings (rule "build")
scripts/check_parity.py  the two editions: same chapters, heading levels and status, and the same note keys, each cited as many times (rule "parity")
scripts/check_em_dash.py no em dash in any text file but the evidence of the runs, work/done/*-run/ (rule "em-dash")
scripts/check_prose.py   the prose rules of docs/04 in both editions and both READMEs (rule "prose")
scripts/check_links.py   every external URL in both editions, both READMEs and mkdocs.yml still answers (rule "links")
scripts/build_book.py    PDF (cover first) and EPUB (cover image) of both editions into output/ (rule "book")
scripts/release.py       the author's publish: checks main, clean and not behind, verify green, then pushes main and the next v* tag (rule "release")
scripts/check_disclosure.py no term of the disclosure list in a file path, a text file or a commit message; --staged and --message for the hooks (rule "disclosure"; ADR-0012)
.githooks/pre-commit     check_disclosure.py --staged: the staged paths and their staged text; POSIX sh, executable
.githooks/commit-msg     check_disclosure.py --message: the commit message, without git's # lines and the diff below the scissors line of commit -v
scripts/patterns.py      compile_entry: the entry syntax (plain or re:) shared by the prose and disclosure checks
scripts/markdown.py      front_matter: the fields and the body, shared by parity and the book build; mask: front matter, code and HTML comments as spaces, shared by the prose and link checks
scripts/repo_files.py    the files the checks read: tracked, plus untracked and not ignored
pandoc/pdf.css           the PDF: A5, margins, the fonts by @font-face, night blue, cream and amber as on the cover; the contents page, on one page with room for two more rows, its chapter number at the size of the row's title and page number; the chapter's opening block, its running head and the page number at the outer corner; code on night blue, a block on one page, a wrapped line starting at the margin; a border and a width for PNGs; the note box; notes at the foot of the page at 66%, italic, links, quotations and code upright
pandoc/epub.css          the EPUB: no @font-face; a wrapped code line starts at the margin; a border and a width for PNGs; the note box; notes at 66%, italic, links, quotations and code upright
pandoc/fonts/            Merriweather (4 styles), Instrument Serif (regular and italic), Iosevka Term Regular; <Family>-OFL.txt each
.github/workflows/verify.yml  jobs verify (make verify on every push, the full history, the list from the secret DISCLOSURE_DENYLIST), pages (main only) and release (v* tags only), each after verify
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
| `make verify` | build, then parity, then em dash, then prose, then links, then disclosure (files and every commit message, as `make scan`); stops at the first failing group. The link check needs the network: offline it is skipped locally and fails in Actions (`CI` set). |
| `make book` | `scripts/build_book.py`: for each edition, a PDF and an EPUB in `output/` (`one-page-at-a-time.*`, `uma-pagina-de-cada-vez.*`), then their paths. Needs pandoc, weasyprint and pypdf; not part of `make verify`. Each file: the edition's cover (the PDF's first page, prepended by pypdf from `book/assets/cover-<edition>.pdf`; the EPUB's cover image from `cover-<edition>.png`), title page, rights page, table of contents of chapters on one page (the rendered PDF is counted, and a second page fails the build), chapters in `NN-` order, appendices in `A<n>-` order; a draft carries its banner; in the PDF a note sits at the foot of the page of its first mention, in the EPUB notes end their chapter, one per key, every mention showing its number; the PDF's page numbers count the cover as page 1, so a number is the page of the file and an odd page is a right-hand one; a heading's id drops its accents, as MkDocs does, so a link to `NN-<slug>.md#<anchor>` resolves on the site and in the book. Title and subtitle come from `book/<edition>/index.md`, author, rights and banner from `mkdocs.yml`. |
| `make hooks` | `git config core.hooksPath .githooks`, once per clone: the pre-commit hook refuses a commit whose staged paths or staged text match the list, the commit-msg hook one whose message does. Both refuse every commit when the list is missing. A clean commit prints nothing; `git commit --no-verify` skips them, and `make scan` then finds the commit. |
| `make release` | `scripts/release.py $(BUMP)`, run by the author only: on `main` with a clean tree, not behind `origin/main`, with commits since the newest `vX.Y.Z` tag, and `make verify` green, it shows the next tag (`BUMP=patch`, the default, `minor` or `major` bumps the newest), the commits since the last one, and asks; on yes it pushes `main`, then an annotated tag, which starts the job `release`. A refusal is `Makefile:1: release: message` and exit 1, with nothing pushed. |
| `make scan` | the disclosure scan alone: the files, then the message of every commit in the history (`<sha, 12 chars>:<line>: disclosure: commit message matches list entry <n>`, line 1 the subject); with a list and without `CI`, it also fails while the hooks are off (`Makefile:1: disclosure: hooks are off; run make hooks`). The list is `FKB_DENYLIST`, or `~/.config/focus-kit-book/denylist.txt`; one entry per line, `#` comments, `re:<pattern>` for a regular expression. Without a list it is skipped locally and fails in Actions (`CI` set). A finding names the file, the line and the entry's number in the list, never the term; a matched part of a path prints as `***`. |

The navigation comes from the file names in `NN-` order, with each chapter's H1 as its title.

The file name of a chapter is the same in both editions, so parity is checked by name.
Code of the guided project lives in its own repository, `JCKodel/focus-kit-clinic` (ADR-0008); the book shows it by quoting a file at a chapter tag, `https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/<chapter-slug>/<path>`, never by keeping a copy here.
Code of the brownfield project lives in the fork `JCKodel/clahub`; the book quotes the project as upstream left it at tag `book-v1`, and what a chapter added at its chapter tag, `https://github.com/JCKodel/clahub/blob/book-v1-<chapter-slug>/<path>` (`book-v1-analyze` first), never copies it (ADR-0009).

## Data

There is no data store.
The disclosure list, the terms that must never appear in the repository, lives outside it (ADR-0012).
Source material for the cases lives in the author's private folders and is never linked from here.

## How errors travel

Every check prints `file:line: rule: message` and exits non-zero.
`make verify` runs them all and stops at the first failing group.
The site build runs with `--strict`, so a broken link or a missing page fails the build.
MkDocs has its own message format, so `scripts/build.py` rewrites each warning as `file:line: build: message`: the doc file MkDocs names, at the line of the broken link, or line 1 when there is none; a warning that names no file points to `mkdocs.yml:1`.
`scripts/build_book.py` does the same for pandoc and weasyprint: a message that names a chapter prints as `book/<edition>/<file>:<line>: book: message`, at the chapter's own line; any other as `Makefile:1: book: message`. A failure is one such line and exit 1; a warning is printed and the build goes on. A missing pandoc, weasyprint or pypdf prints `Makefile:1: book: <tool> not found; install it (see README)`; a missing cover, or one with more than one page, prints a finding at the cover's own path. An edition whose rendered contents runs past one page prints `Makefile:1: book: <edition> contents takes <n> pages; it must fit on one`; both editions are built first, so each reports, then exit 1.

## Environments

| Name | What runs there | How it is updated |
|---|---|---|
| local | `make serve` (site), `make book` (PDF and EPUB into `output/`, never committed) | by hand |
| GitHub Actions | `make verify` on every push, any branch, with the list from the secret `DISCLOSURE_DENYLIST` | the author sets the secret; runs on push |
| GitHub Pages | the website, from `main` | job `pages`, on every push to `main` once `verify` is green; one deploy at a time, a stale queued one dropped. Pages source set to "GitHub Actions" once by the author |
| GitHub Release | PDF and EPUB, both editions, under the names of `make book`, so `releases/latest/download/<file>` is the newest | job `release`, on a `v*` tag the author creates with `make release`, once `verify` is green; a tag with `-` makes a pre-release. |

## Tried and removed on purpose

* A GitHub wiki, as the book or as a mirror (ADR-0001).
* Code examples in many languages (ADR-0008).
* A link shortener or playground server for code snippets: the guided project's tagged repository does that job.
* Reusing text from the author's earlier books (ADR-0005).
