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
| Automation | GitHub Actions | Pages on push to `main`; Release on a `v*` tag (ADR-0014). |
| Scripts | Make, and Python 3 for checks | Nothing to install beyond what the build already needs. |

## How the repository is organized

FOCUS does not apply: there is no product code, only content and a few build scripts (ADR-0011).

```
book/en/NN-<slug>.md     English edition, the source (A1-<slug>.md for appendices)
book/pt/NN-<slug>.md     Portuguese edition, same file names
book/assets/             images and figures shared by both editions
scripts/                 build and check scripts
mkdocs.yml, Makefile     created by site-skeleton
docs/, work/             the process documents and the deliveries
```

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

## Environments

| Name | What runs there | How it is updated |
|---|---|---|
| local | `make serve` (site), `make book` (PDF and EPUB into `output/`, never committed) | by hand |
| GitHub Pages | the website, from `main` | Actions, on every push to `main` |
| GitHub Release | PDF and EPUB, both editions | Actions, on a `v*` tag the author creates; the author uploads them to books.kodel.com.br |

## Tried and removed on purpose

* A GitHub wiki, as the book or as a mirror (ADR-0001).
* Code examples in many languages (ADR-0008).
* A link shortener or playground server for code snippets: the guided project's tagged repository does that job.
* Reusing text from the author's earlier books (ADR-0005).
* The `[?]` mark (ADR-0013).
