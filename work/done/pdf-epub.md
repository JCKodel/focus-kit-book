# pdf-epub

**Objective.** The author runs `make book` and gets, in `output/`, a PDF and an EPUB of each edition, built from the same `book/<edition>/*.md` the site reads, with the same fonts on any machine.

**Behaviour.**

* `make book` writes four files to `output/` and prints their paths; it does not run as part of `make verify`.
* Each file holds, in order: a title page, a rights page, a table of contents, the chapters in `NN-` order, then the appendices in `A<n>-` order. `index.md` is not a chapter; its content feeds the title page.
* A chapter with `status: draft` is included, with the edition's `draft_banner` text as the first paragraph after its H1, as the site shows it.
* The front matter never appears as text.
* A footnote appears at the end of its own chapter. The same key used in two chapters gives two different notes.
* A link to another chapter, with or without `#anchor`, lands on that chapter or that heading in both the PDF and the EPUB.
* A `$` in prose is printed as a dollar sign, never as mathematics: "costs $5 and pays $6 dollars" comes out as written.
* An image under `book/assets/` shows in the PDF and the EPUB.
* A code line longer than the page wraps inside its block. It is never cut and never runs past the margin.
* The PDF is A5, hyphenated in the edition's language (English, Brazilian Portuguese), set in Merriweather (body), Google Sans (headings) and Iosevka Term (code), loaded from the repository and never from the system.
* The EPUB is EPUB 3, one file per chapter, with no embedded fonts, so the reader's device chooses.
* When `pandoc` or `weasyprint` is missing, `make book` prints `Makefile:1: book: <tool> not found; install it (see README)` and exits 1. A pandoc or weasyprint error prints as `<file>:<line>: book: <message>` when it names a file, `Makefile:1: book: <message>` when it does not, and exits 1.

**Contract.**

Files:

```
scripts/build_book.py     rule "book"; Python 3 standard library; runs pandoc and weasyprint
scripts/markdown.py       + front_matter(text) -> (fields dict, body lines), moved out of check_parity.py
scripts/check_parity.py   reads status through front_matter; behaviour unchanged
pandoc/pdf.css            A5 page, margins, page numbers, fonts via @font-face, pre { white-space: pre-wrap }
pandoc/epub.css           EPUB styling, no @font-face
pandoc/fonts/             Merriweather Regular, Italic, Bold, BoldItalic; Google Sans Regular, Bold;
                          Iosevka Term Regular; one OFL.txt per family (<Family>-OFL.txt)
Makefile                  book target: python3 scripts/build_book.py
README.md, README.pt.md   Build locally: brew and apt lines for pandoc and weasyprint; License: the fonts row
docs/01-Architecture.md   stack (Diagrams, PDF and EPUB rows), tree, the make book row
docs/adr/ADR-0002-...md   amended: Mermaid removed (dated amendment, text above it unchanged)
docs/06-Queue.md          pdf-epub [x]
```

`front_matter` is the second concrete occurrence of front matter reading. The first is `check_parity.py`, delivery `site-skeleton`.

Output, exact names (`pages-and-release` uploads these):

```
output/one-page-at-a-time.pdf        output/one-page-at-a-time.epub
output/uma-pagina-de-cada-vez.pdf    output/uma-pagina-de-cada-vez.epub
```

`scripts/build_book.py`, per edition (`en`, `pt`):

* Metadata, read from what exists, never a third copy:
  * `title`: the H1 of `book/<edition>/index.md`.
  * `subtitle`: its first line in `**...**`.
  * `author`: `site_author` of `mkdocs.yml`.
  * `lang`: `en` or `pt-BR`.
  * `rights`: that edition's `copyright` of `mkdocs.yml` (the i18n one for `pt`), HTML turned into text with the URLs kept.
* Inputs: `book/<edition>/[0-9][0-9]-*.md` sorted, then `A[0-9]*-*.md` sorted. Each one is copied under its own file name to a temporary directory, with the front matter removed (`front_matter`) and, when `status` is `draft`, the edition's `draft_banner` (from `mkdocs.yml`) inserted after the H1.
* pandoc: `-f markdown-tex_math_dollars`, `--file-scope`, `--toc`, `--reference-location=section`, `--resource-path=book/<edition>:book`.
  * `--file-scope` keeps same-key footnotes apart and rewrites `NN-x.md#y` links into the combined document; a scratch test with pandoc 3.11 showed both. A link to a chapter with no `#anchor` gets a target the script provides.
  * `-f markdown-tex_math_dollars`: an earlier build of the author's hit `$` turning prose into mathematics.
* PDF: pandoc to HTML with `pandoc/pdf.css`, then `weasyprint`. EPUB: pandoc `-t epub3` with `--css pandoc/epub.css`.
* Google Sans is published only as a variable font. If WeasyPrint does not select its weights from the variable file, the repository holds static Regular and Bold instances cut from it with fonttools, and the page records it.

**Out of scope.**

* Mermaid, and how diagrams are drawn (a tool such as /design, labels per edition, the dark theme): decided by the first chapter with a diagram, on a real one.
* A cover image: the line `cover` in M7, before `launch`.
* Running `make book` in Actions: `pages-and-release`.
* Fonts embedded in the EPUB: e-readers let the reader choose; it adds megabytes.
* Nerd Font icons: the book uses none, and their glyphs carry other licenses.
* A check that the PDF and EPUB match the site: no drift has happened yet (docs/05 §7).

**Done when.**

* [x] With untracked `book/en/98-probe.md`, `book/en/99-probe.md` and their `pt` twins (so parity passes), holding `status: draft`, a link from 98 to `99-probe.md#<heading>` and one to `99-probe.md`, the same footnote key in both, the "$5 ... $6 dollars" line, a code line of 120 characters and an image from `book/assets/`: every behaviour above holds in all four files. What was seen is recorded here, and the probes are removed.
* [x] `pdffonts` on both PDFs lists only Merriweather, Google Sans and Iosevka Term, all embedded.
* [x] `epubcheck` reports zero errors on both EPUBs.
* [x] With `pandoc` hidden from `PATH`: the not-found line, exit 1.
* [x] `check_parity.py` gives the same output as before on the `site-skeleton` probes after `front_matter` moves.
* [x] Proof: `pdftoppm` PNGs of the title page, the table of contents, the first page of chapter 1 and its notes, in both editions, saved as `work/done/pdf-epub-<edition>-<what>.png`.
* [x] `make verify` green; `git status` shows nothing under `output/`.
* [x] docs/01, ADR-0002 and both READMEs updated; docs/06 line marked `[x]`.

## What happened

**Diverged from the plan.**

* `--reference-location=section` puts a note at the end of the innermost section that holds its call, an H2, not at the end of the chapter; notes are numbered through the whole book. The EPUB drops the option: pandoc's default already ends each chapter file with its own notes, numbered from 1. The PDF keeps it, and `build_book.py` moves each chapter's notes to the chapter's end and numbers them from 1 (`notes_at_chapter_end`).
* `--file-scope` rewrites links only when pandoc gets the file names as written in the links, so pandoc runs inside the temporary directory with bare names; given absolute paths, the EPUB kept `99-probe.md` as a link and epubcheck failed (RSC-007).
* The prefix `--file-scope` gives ids drops a leading number: both `98-probe.md` and `99-probe.md` prefix with `probe.md__`. A chapter-level target named after the prefix alone would collide, so the target the script provides is an explicit id on each H1, `chapter-<file stem>` (`#probe.md__chapter-99-probe`), and a link to a chapter without `#anchor` is pointed to it. A link to a chapter's H1 by its automatic id no longer lands; no such link exists.
* Google Sans: WeasyPrint 69 selects weight 700 from the variable file (a separate `Google-Sans-Bold` instance in the PDF, real bold forms, not synthetic), so the repository holds the variable file `GoogleSans-Variable.ttf` and no static cuts.
* pandoc's note return arrow is `↩` plus U+FE0E; no font has U+FE0E and only Iosevka Term has `↩`, so WeasyPrint added `.LastResort` from the system. The script removes U+FE0E from the PDF's HTML and `pdf.css` sets the arrow in Iosevka Term. That is why Iosevka Term is embedded in a PDF with no code block.
* The rights page: the EPUB shows `rights` in pandoc's title page, on a page of its own by CSS. The PDF's HTML template shows no `rights`, so the script writes the title page and the rights page as `--include-before-body` and gives pandoc only `pagetitle`.
* mkdocs.yml is read without a YAML library (standard library only): `site_author`, `copyright` and `draft_banner` by indentation, top level for English, under `- locale: pt` for Portuguese.
* `front_matter` returns no fields for a front matter never closed; the old parity reader took `status` from it anyway. The site build fails on such a file first.
* A failure prints as one line: pandoc's multi-line message is joined, and the copy's `(line, column)` becomes the chapter's own line (front matter and banner accounted for). Warnings (a missing image) print in the same shape and do not fail.

* Font sources, fetched 2026-09-25: Merriweather Regular, Italic, Bold, BoldItalic from `SorkinType/Merriweather`, `fonts/ttf` (the static cuts; `google/fonts` holds only variable files), with its `OFL.txt`; Google Sans `GoogleSans[GRAD,opsz,wght].ttf` and `OFL.txt` from `google/fonts`, `ofl/googlesans`, saved as `GoogleSans-Variable.ttf`; Iosevka Term Regular from `PkgTTF-Unhinted-IosevkaTerm-34.8.1.zip` of the Iosevka releases, with the repository's `LICENSE.md` as `IosevkaTerm-OFL.txt`.

**Dropped.** Nothing of the page.

**Proof.**

* Probes (`98-probe.md`, `99-probe.md` in both editions, `book/assets/99-probe.png`), in all four files: title page, rights page, contents, chapter 1, 98, 99, in that order; the draft banner of each edition under the H1 of 98 and 99; no front matter text; notes "Note of chapter ninety-eight." at the end of 98 and "...ninety-nine." at the end of 99, both numbered 1; "It costs $5 and pays $6 dollars." as written; the image shown (EPUB `media/file0.png`); the 120-character line wrapped inside its block at the margin; `status:` found 0 times in the text of both PDFs and in the EPUBs' chapter files; in the PDF both links go to page 8, where 99 and its heading are, and in the EPUB to `ch003.xhtml#probe.md__target-heading` and `ch003.xhtml#probe.md__chapter-99-probe`. The Portuguese PDF hyphenates ("expli-car", "de-senvolvedores"). Probes removed.
* `pdffonts`, both PDFs: Google-Sans, Google-Sans-Bold, Merriweather, Merriweather-Bold, Iosevka-Term, all `emb yes`, plus Merriweather-Italic with the probes.
* `epubcheck` 5: `0 fatals / 0 errors / 0 warnings / 0 infos` on both EPUBs.
* `PATH=~/.local/bin:/usr/bin:/bin make book`: `Makefile:1: book: pandoc not found; install it (see README)`, the script exits 1 (make then reports `Error 1` and exits 2). With pandoc and no weasyprint: `Makefile:1: book: weasyprint not found; install it (see README)`, exit 1.
* A broken YAML block added to 98: `book/en/98-probe.md:23: book: Error parsing YAML metadata: YAML parse exception at line 2, column 0, while parsing a flow sequence: did not find expected ',' or ']'`, exit 1; line 23 is the block's `---` in the source.
* `check_parity.py` on the site-skeleton scenarios (one edition only, a level changed, a heading less, a status removed, the other edition only, clean): output identical before and after the move.
* Screens: `work/done/pdf-epub-<en|pt>-<title|toc|chapter-1|notes>.png`.

**Decisions.** No ADR beyond the amendment of ADR-0002 the page asked for.
