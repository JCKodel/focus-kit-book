# site-skeleton

**Objective.** The author runs `make serve` and reads the book as a bilingual website, English at the root and Portuguese at `/pt/`, with unfinished chapters marked as drafts, and `make verify` fails when the build breaks, the editions drift or an em dash appears.

**Behaviour.**

* On a fresh clone, `make serve` creates `.venv` from `requirements.txt` and serves the site at `http://127.0.0.1:8000/`; no global install is needed beyond Python 3.
* The English edition is at `/`, the Portuguese at `/pt/`; the language switcher leads to the same page in the other edition.
* Each edition has a home page (title, subtitle, author, one line saying it is free in both languages) and chapter 1 as a draft placeholder.
* The navigation is generated from the file names, in `NN-` order, with the chapter's H1 as its title.
* Search works in each edition, in its language; the reader can switch between light and dark themes.
* A page with `status: draft` in its front matter shows a banner at the top and a draft marker next to its entry in the navigation, in the edition's language; removing the line removes both.
* `make verify` on the clean tree is green and exits 0.
* `make verify` fails, printing `file:line: rule: message` and exiting non-zero, when:
  * a page links to a page that does not exist (strict build);
  * a chapter exists in one edition and not the other;
  * the two editions of a chapter differ in the sequence of heading levels, or one is a draft and the other is not;
  * any text file in the repository contains an em dash.
* `make verify` stops at the first failing group, in the order build, parity, em dash.

**Contract.**

Files created:

```
requirements.txt          mkdocs-material and mkdocs-static-i18n, exact versions (==)
mkdocs.yml                the site
overrides/main.html       the draft banner (theme custom_dir)
book/assets/site.css      the draft marker in the navigation
book/en/index.md          home page, English
book/pt/index.md          home page, Portuguese
book/en/01-why-process.md chapter 1 placeholder, draft
book/pt/01-why-process.md chapter 1 placeholder, draft
scripts/build.py          rule "build" (added in /apply, see What happened)
scripts/check_parity.py   rule "parity"
scripts/check_em_dash.py  rule "em-dash"
Makefile                  targets below
.gitignore                .venv/, site/, output/
```

`mkdocs.yml`:

* `site_name: One Page at a Time`; Portuguese override `Uma Página de Cada Vez`.
* `site_url: https://jckodel.github.io/focus-kit-book/`, `site_author: J.C. Ködel`.
* `docs_dir: book`; `theme.name: material`, `custom_dir: overrides`, palette with a light and a dark scheme and a toggle.
* plugins: `search`, `i18n` with `docs_structure: folder`, languages `en` (default, `name: English`) and `pt` (`name: Português`, search in Portuguese).
* no `nav:` key; the navigation comes from the files.

Front matter of a draft page, the draft marker every later chapter delivery removes when done:

```yaml
---
status: draft
---
```

Banner text: en `Draft: this chapter is still being written.` · pt `Rascunho: este capítulo ainda está sendo escrito.`
Navigation tooltip: en `Draft` · pt `Rascunho`.

Pages:

| File | H1 |
|---|---|
| `book/en/index.md` | `One Page at a Time`, subtitle `Delivering Software and Projects with Coding Agents`, `J.C. Ködel`, `Free, in English and Portuguese.` |
| `book/pt/index.md` | `Uma Página de Cada Vez`, subtitle `entregando software e projetos com agentes de IA`, `J.C. Ködel`, `Gratuito, em inglês e português.` |
| `book/en/01-why-process.md` | `Why process, when AI writes fast` (draft, H1 only) |
| `book/pt/01-why-process.md` | `Por que processo, quando a IA escreve rápido` (draft, H1 only) |

Checks: Python 3 standard library only; exit 0 when clean, 1 when anything is printed; one line per finding.

`scripts/check_parity.py` compares `book/en/*.md` and `book/pt/*.md` by file name. Headings are ATX lines (`#` to `######`) outside fenced code.

```
book/en/02-x.md:1: parity: no Portuguese counterpart book/pt/02-x.md
book/pt/02-x.md:1: parity: no English counterpart book/en/02-x.md
book/pt/01-x.md:<line>: parity: heading level 3, English has level 2 at book/en/01-x.md:<line>
book/pt/01-x.md:<last line>: parity: 4 headings, English has 5
book/pt/01-x.md:1: parity: status "none", English has "draft"
```

`scripts/check_em_dash.py` reads every file from `git ls-files --cached --others --exclude-standard` with extension `.md`, `.yml`, `.yaml`, `.html`, `.css`, `.py`, `.txt`, `.toml`, and names the character by its Python escape (backslash, `u2014`), never literally, so the check passes on itself.

```
<path>:<line>: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
```

`Makefile` targets:

| Target | Does |
|---|---|
| `.venv` (file target) | `python3 -m venv .venv` and `pip install -r requirements.txt`; rebuilt when `requirements.txt` changes |
| `serve` | `mkdocs serve` |
| `build` | `scripts/build.py`: `mkdocs build --strict` into `site/`, warnings printed as `file:line: build: message` |
| `verify` | `build`, then `check_parity.py`, then `check_em_dash.py`; stops at the first failure |

**States.** The defaults of MkDocs Material; the only added state is the draft banner.

**Visual reference.** The default MkDocs Material theme, no custom design; viewports 1280 and 390 pixels wide.

**Out of scope.**

* Mermaid: enters with the first chapter that has a diagram.
* Parts as navigation sections: enter when Part I has more than one chapter.
* `make book`, PDF and EPUB: `pdf-epub`.
* Actions and GitHub Pages: `pages-and-release`.
* External link check: `link-check`.
* Disclosure scan and prose rules: their own deliveries add their groups to `make verify`.
* License and README: `license-and-readme`.
* Chapter 1's content: `chapter-template`.

**Done when.**

* [x] `make verify` green from a fresh clone with only Python 3 installed.
* [x] Each failure of Behaviour reproduced once (delete a pt file, change a heading level, remove `status: draft` from one edition, add an em dash, add a broken link); output recorded in the page, then reverted.
* [x] Screenshots of the home page and of chapter 1 with its banner, both editions, at 1280 and 390: `work/done/site-skeleton-<edition>-<page>-<width>.png`.
* [x] Language switcher, search in each edition and the theme toggle checked by hand.
* [x] docs/01 updated: the tree shows `requirements.txt`, `overrides/`, `.venv/` and `site/`, and the `make` targets.
* [x] docs/05 §5 names `status: draft` as the draft marker.
* [x] docs/06: `site-skeleton` marked `[x]`; page moved to `work/done/site-skeleton.md`.
* [x] Changes staged, commit message suggested, nothing committed.

**What happened.**

Diverged from the plan:

* `scripts/build.py` added. `mkdocs build --strict` prints its own format (`WARNING -  Doc file '...' contains a link ...`), not `file:line: rule: message` as Behaviour and docs/01 require. Asked; the author chose to translate: the script runs the strict build and rewrites each warning with the doc file and the line of the broken link (line 1 when not found; `mkdocs.yml:1` when no file is named). Recorded in docs/01 "How errors travel". No ADR: docs/01 owns the rule.
* `make serve` answers at `http://127.0.0.1:8000/` with a redirect to `/focus-kit-book/`, the path of `site_url`; Portuguese is at `/focus-kit-book/pt/`. Kept: the local paths match GitHub Pages, so a base path bug shows locally.
* The em dash constant is written as its Python escape (backslash, `u2014`), as the Contract says; the file writing tool turned the escape into the character on the first attempt, and the check caught itself.
* Draft marker: Material's own page status (`extra.status`, overridden per language by the i18n plugin) gives the navigation mark and its tooltip; `book/assets/site.css` only supplies the icon (a pencil). The banner text lives in `extra.draft_banner`, one per language, read by `overrides/main.html`.
* The theme toggle's tooltips are translated in the Portuguese palette (`Mudar para o modo claro` / `escuro`).

Nothing dropped.

The proof found:

* `make verify` green from a copy of the tree with no `.venv/` and no `site/` (only Python 3.14 installed): the `.venv` target installed mkdocs-material 9.7.7 and mkdocs-static-i18n 1.3.1, then build, parity and em dash passed, exit 0.
* Each failure, reproduced on the clean tree and reverted (`make -s verify`, make's own `Error` line omitted):

```
# broken link: "See [the next chapter](02-missing.md)." appended to book/en/01-why-process.md
book/en/01-why-process.md:7: build: Doc file 'en/01-why-process.md' contains a link '02-missing.md', but the target 'en/02-missing.md' is not found among documentation files.
# book/pt/01-why-process.md deleted (the build passes: the plugin falls back to English)
book/en/01-why-process.md:1: parity: no Portuguese counterpart book/pt/01-why-process.md
# "### Section" in en, "## Section" in pt
book/pt/01-why-process.md:7: parity: heading level 2, English has level 3 at book/en/01-why-process.md:7
# status: draft removed from pt only
book/pt/01-why-process.md:1: parity: status "none", English has "draft"
# an em dash in a sentence of book/en/01-why-process.md
book/en/01-why-process.md:7: em-dash: em dash found; use a comma, a colon, parentheses or a new sentence
# extra check: one more heading in en; a "#" line inside a fenced block ignored
book/pt/01-why-process.md:7: parity: 2 headings, English has 3
```

  Every run exited non-zero; the broken link stopped at `build`, so the later groups did not run.
* `status: draft` removed from both editions: verify green, no banner and no mark in the built HTML of either edition; restored.
* Screenshots in `work/done/site-skeleton-<edition>-<page>-<width>.png`, against the default Material theme: no divergence. They render in the dark scheme because the machine prefers dark. Headless Chrome will not open a window narrower than 500 pixels, so the 390 shots render the page in a 390 pixel iframe and crop it; the first 390 attempt showed a 500 pixel layout cut on the right.
* By hand, in Chrome on `make serve`: the switcher on chapter 1 (English) opens chapter 1 in Portuguese, with the Portuguese banner and the `Rascunho` tooltip; the theme toggle switches both ways; search answers in each edition's language (`1 resultado encontrado` for `processo` on `/pt/`).
* Search finding: the i18n plugin builds one index for both editions, so a search from `/pt/` for `writes` also returns the English chapter. Accepted as the plugin's default; stemming and interface are per edition. If per-edition results matter, it is a queue line, not part of this delivery.

Decisions: build warnings translated by `scripts/build.py` (the author's answer); "draft marker" entered docs/03 as a term.
