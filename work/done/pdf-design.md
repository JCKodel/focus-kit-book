# pdf-design

**Objective.** A reader of either edition opens a PDF set in the design the author chose (direction C, "Noturno"): night blue and amber as on the cover, titles in Instrument Serif, body in Merriweather, code in Iosevka Term, a contents page of chapters only, and each note at the foot of the page that cites it.

**Behaviour.**

* The contents page lists the prologue and the chapters only, one line each (number, title, page), on a night-blue page under the title `Contents` (pt: `Sumário`); sections stay in the PDF's outline, as today.
* A chapter opens on a new page with a night-blue block that bleeds to the top, left and right edges and holds the label `Chapter` (pt: `Capítulo`), the chapter's number inside the outline of a page, the title without its number, and the chapter's first paragraph in italic.
* An H1 with no leading number (the prologue; an appendix when one exists) opens with the same block, without label and without numeral.
* A draft chapter's banner follows the block, and its first paragraph is then ordinary text.
* Every page of a chapter but its first carries a running head (the number on an amber rectangle, the title in italic, a rule below) and every chapter page a page number at the outer bottom corner; title page, rights page and contents carry neither.
* An H2 has a short amber bar above it; H2 and H3 are in Instrument Serif.
* A code block is cream on night blue, keywords amber, strings and numbers light blue, comments grey and italic; a wrapped line still starts at the margin.
* A note sits at the foot of the page of its first mention, under a short amber bar, at 66% of the body and in italic, with links, quotations and code upright, as today; notes number from 1 per chapter; a later mention of the same key shows that number and links to the note, as today; no notes block ends a chapter.
* The note box (blockquote) is a cream box with an amber bar on top and no left border.
* The title page stays light: title in Instrument Serif, subtitle in Merriweather italic, author.
* `pdffonts` on both PDFs lists only Merriweather, Instrument Serif and Iosevka Term, all embedded; Google Sans is in neither PDF nor the repository.
* The EPUB and the site look as they do today.

**Contract.**

Colors: night `#0B1626` (text on paper, blocks, code ground), cream `#F3EEE2` (text on night, note box ground), amber `#F2A33A` (never text on white), rule on night `#26334A`, code strings and numbers `#8FC1FF`, code comments `#8A97AD`, external links `#1A4F8B` (unchanged), chapter links in the text's color (unchanged).

Fonts in `pandoc/fonts/`: `InstrumentSerif-Regular.ttf`, `InstrumentSerif-Italic.ttf`, `InstrumentSerif-OFL.txt` enter (from `google/fonts`, `ofl/instrumentserif`); `GoogleSans-Variable.ttf` and `GoogleSans-OFL.txt` leave; Merriweather (4 styles) and Iosevka Term Regular stay.

Page: A5, margins 18mm 15mm 20mm 15mm, as today. Body Merriweather 9pt/1.55, justified, hyphenated, night.

| Element | Setting |
|---|---|
| Opening block | padding 39pt top, 25.5pt bottom; label Iosevka Term 7pt, uppercase, spaced 0.2em, amber; frame 69pt by 97.5pt, 1.1pt amber, numeral Instrument Serif 72pt amber, at the right; title Instrument Serif 33pt/34.5pt cream; first paragraph Merriweather italic 10pt/15.5pt cream |
| H2, H3 | bar 30pt by 2.25pt amber, then Instrument Serif 18pt/19.5pt; H3 Instrument Serif 14pt, no bar |
| Running head | rectangle 9.75pt by 13.5pt amber with the number in Iosevka Term 6.75pt night; title Instrument Serif italic 9.75pt; rule 0.75pt night |
| Page number | Instrument Serif italic 10.5pt, outer bottom corner |
| Code block | Iosevka Term 8pt/1.4, padding 9pt; inline code as today |
| Notes | 66% of the body, italic; bar 30pt by 2.25pt amber above the first note of a page |
| Contents | title Instrument Serif 48pt cream, bar 33pt by 2.25pt amber; row: number Instrument Serif italic 12pt amber, title Merriweather 9pt cream, page Iosevka Term 7pt amber, rule 0.75pt `#26334A` |
| Note box | ground cream, top bar 2.25pt amber, no left border |
| Table | header row bold with a 0.75pt night rule; rows as today |

Chapter number: from the H1 `# <N>. <Title>` (docs/04); it feeds the numeral, the contents row and the running head; the PDF outline keeps `<N>. <Title>`.

Strings, in `scripts/build_book.py` per edition: `Contents` / `Sumário`, `Chapter` / `Capítulo`.

Documents: docs/01 (the PDF row's fonts; `pandoc/pdf.css`; `pandoc/fonts/`; `make book`: "table of contents" becomes "table of contents of chapters", and "notes end their chapter" becomes "in the PDF a note sits at the foot of the page of its first mention, in the EPUB notes end their chapter"); `README.md` and `README.pt.md`, the fonts row; docs/06.

**Visual reference.** The author's design canvas, direction C, kept outside the repository: artboards "C · Sumário", "C · Abertura de capítulo" and "C · Página de texto", A5 at 559 by 794 px. This page overrides it in three places: body in Merriweather, code in Iosevka Term, notes in italic.

**Out of scope.**

* The cover: the author's Affinity file, already on both PDFs.
* The EPUB's and the site's styles: the reader's device and MkDocs Material set them.
* Any chapter's text: only how it is set changes.
* Page breaks tuned by hand per chapter: the build has none today.
* A light variant for printing: nobody asked for one (docs/05 §7).

**Done when.**

* [x] `make book` builds both editions; `make verify` green.
* [x] `pdffonts` on both PDFs: only Merriweather, Instrument Serif and Iosevka Term, all embedded.
* [x] Screenshots of the PDF, both editions, in `work/done/pdf-design-<edition>-<what>.png`: contents, the prologue's opening, chapter 5's opening, a page with code and notes, a page with a table, a page with a note box.
* [x] In both PDFs: the contents is chapters only; no chapter ends on a notes block; chapter 5's first notes are at the foot of the page that cites them; a key cited twice prints one note.
* [x] `git diff` shows no change in `pandoc/epub.css`, `book/assets/site.css` or `book/`, but for the font list of the two diagrams, which the author decided (see What happened).
* [x] docs/01, both READMEs and docs/06 updated; the author is given both PDF paths.

**What happened.**

Built as the page says, on WeasyPrint 69.0 and pandoc 3.11, the versions of the release job.
`scripts/build_book.py` puts each note where it is first cited (`notes_at_foot`) and turns each chapter's H1 and first paragraph into the opening block, with the contents before the first (`openings`); `pandoc/pdf.css` does the rest.
No abstraction was created, and no dependency or tool added.

Decided by the author during the build, both asked by the agent:

* The diagram of chapter 2 asked for Google Sans, and without it WeasyPrint set it in Arial, a font of the machine: `pdffonts` listed it, against the contract. The two SVGs now open their font list with Merriweather, so `book/assets/02-context-window.<edition>.svg` changed, one attribute each, against the fifth line of Done when. The site shows the diagram as before on a machine without Merriweather; the EPUB carries the same two files. docs/04 §Files has the rule. The diagram's Merriweather comes from `pdf.css` and not from the machine: none is installed where this was built, and a test page showed WeasyPrint giving an SVG a font the page declares by `@font-face`, so the release job sets the same diagram.
* The page number counts the cover as page 1. Before, the title page was page 1, and the cover that pypdf prepends made every odd page a left-hand one, so the outer corner of the canvas (odd on the right) would have been the inner one. Now the printed number is the page of the file, and every number is one more than before.

What diverged from the canvas, and why:

* The running head sits inside the 18mm top margin the contract keeps: 8.25pt between its rule and the text, where the canvas has 12pt.
* The contents page has a top margin of 42pt, as on the canvas; it is the one page whose margin is not the contract's.
* The number of a note, in the text and at the foot, is Iosevka Term regular at 6pt; the canvas has a semi-bold at 5.6pt. The repository has only the regular, and at 5.6pt WeasyPrint broke one line of chapter 4 inside a word and stretched it across the page; at 6pt no line of either edition is stretched.
* The title page: title at 33pt, the chapter title's size, subtitle at 11pt; the contract names the fonts, not the sizes.
* The note box, the table rows, the draft banner, lists and figures keep the sizes they had.
* A note has no return arrow: it is on the page that cites it.

Decisions taken:

* A code block never breaks across pages (the longest has 34 lines and fits one). A block that broke left its first part filling the rest of the page in night blue. The cost is white at the foot of the page before a long block; the worst is the page before chapter 14's example page. One line of `pdf.css` reverses it.
* `--toc` goes to the EPUB only, since the build writes the PDF's contents; `--reference-location=section` leaves and `--wrap=none` enters the PDF's pandoc call, which the patterns that read its HTML rely on.
* The chapter's number leaves the H1, so the H1 carries `data-outline` and `bookmark-label` gives the PDF's outline `<N>. <Title>`.
* No ADR: no decision here closes an alternative a later session might reopen without this page.

What the proof found:

* `pdffonts`, both PDFs: Merriweather (regular, italic, bold, bold italic), Instrument Serif (regular, italic), Iosevka Term (regular, and the bold and the oblique WeasyPrint synthesizes from it), all embedded.
* Notes, checked on the real layout with an anchor at every call: 82 notes and 44 later mentions per edition, no notes block left, one note per key. 80 of the 82 sit at the foot of the page of their first mention; two per edition sit at the foot of the next page (en: `anthropic-context-2025` in chapter 2, `vocke-pyramid` in chapter 8; pt: `pro-git-history` and `git-revert` in chapter 19). WeasyPrint, to keep the first two lines of a paragraph together at the foot of a page, sends that page's last note to the next page, and no CSS turns that off for a paragraph. `footnote-policy: line` and `orphans: 99` on the blocks that never break took the count from seven to two in English. Which notes are hit changes with the text; this line of Behaviour is not fully met.
* A pointer to a chapter printed in link blue before this delivery, though docs/04 said it printed in the text's color: pandoc prefixes the id with the file's name, and the selector `a[href^="#chapter-"]` never matched. `a[href*="__chapter-"]` matches.
* The EPUB, compared file by file with the one built from the previous commit: the same, but for the two diagrams and the id and the date pandoc writes on every build.
* The PDF's outline: 252 entries in each edition, before and after, each chapter as `<N>. <Title>`.
* Pages: English 151 to 165, Portuguese 164 to 175.
* The warning `user-select: none`, from pandoc's own style, prints as before.
* No chapter is a draft today, so the draft's line of Behaviour was checked in `openings` (the banner is a `div`, which the pattern of the first paragraph cannot take) and on no built page.
* Screenshots: `work/done/pdf-design-<edition>-<what>.png`, with `<what>` one of `contents`, `prologue`, `chapter-5`, `code-and-notes`, `table`, `note-box`.

Nothing was dropped.
