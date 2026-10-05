# pdf-contents-one-page

**Objective.** A reader of either edition's PDF finds all 27 rows of the contents on one page, the Prologue and chapters 1 to 26, and the chapter numbers there are no taller than the page numbers beside them. `make book` fails if a later chapter pushes the contents onto a second page.

**Behaviour.**

* In `output/one-page-at-a-time.pdf` the contents is page 4 only. Page 5 is the Prologue's opening, and "26 Asking for more 174" (or its new page number) is on page 4. Today that row sits alone on page 5.
* The same holds in `output/uma-pagina-de-cada-vez.pdf`: "26 Pedir mais" is on page 4.
* Every row shows its number, its title and its page number. A title that wraps today ("15 /apply: build, verify, prove, never commit", "22 As ferramentas do time: pull requests, issues e quadros") still wraps cleanly, and its page number never touches the title.
* The chapter number is still Instrument Serif italic in amber, but smaller than today's 12pt: it is set at the size of the row's title text. In the PDF, at a glance, its figures are no taller than the page number's figures (Iosevka Term, amber) on the same row. "Prologue" has no number and keeps its row as it is.
* The row text is a little smaller than today's 8.5pt, and the space between rows is a little tighter. The 48pt "Contents" / "Sumário" title, its amber rule, the night-blue page, the row borders and the colours stay as `pdf-design` left them.
* There is headroom: the CSS fits the 27 rows with room for at least 2 more rows of one line each, so the next chapter does not bring the orphan back.
* When the contents of an edition takes more than one page, `make book` prints the finding below and exits 1. The count comes from the rendered PDF, not from the number of rows.
* Nothing else in the PDF changes: chapter openings, running heads, notes, code and the cover stay the same. The EPUB and the site are not touched.

**Contract.** The new finding of `scripts/build_book.py`, rule "book", for an edition whose contents spans more than one page:

    Makefile:1: book: <edition> contents takes <n> pages; it must fit on one

`<edition>` is `en` or `pt`, and `<n>` is the number of pages from the contents title to the page before the first chapter's opening. Exit 1, like every other book failure (docs/01 §How errors travel). No other message, file name or output path changes.

**Out of scope.**

* Footnote numbers with a coloured block behind them: that is `pdf-footnote-numbers`, the next line.
* Appendices in the contents: per `pdf-design`, it lists chapters only.
* The EPUB's table of contents and the site's navigation: neither has this defect.
* A smaller title or a new look for the contents page: the author chose only a smaller font.
* Page numbers of the chapters: they shift by one page because the orphan page is gone, which is expected and is not a change of design.

**Done when.**

* [x] `make book` builds both editions, and each contents is one page (Behaviour 1 and 2).
* [x] The guard is proved once and the proof recorded on this page. Force a second contents page temporarily (for example a large row font), watch `make book` print the Contract line for both editions and exit 1, then undo it.
* [x] Screenshots of the contents page in both editions are saved as `work/done/pdf-contents-one-page-en-contents.png` and `work/done/pdf-contents-one-page-pt-contents.png`. The author confirms that the numbers are no larger than the page numbers.
* [x] docs/01 is updated: the `pandoc/pdf.css` entry (the contents fits one page, the number at the row's size), the `make book` row (the one-page guard) and §How errors travel (the new finding).
* [x] `make verify` is green, and the author gets the paths of both PDFs.

**What happened.**

* The sizes. Instrument Serif's figures are 0.730 of its size and Iosevka Term's 0.743, so a number at the title's size and a page number at today's 7pt would make the number the taller one. Number, title and page number now share the row's size, 7.5pt (from 8.5pt; the page number goes from 7pt to 7.5pt), so the number is set at the title's size and its figures are a little shorter than the page's. Rows take a 10.5pt line (from 12pt) and 1.25pt of padding (from 1.5pt). The number's own 12pt size and 10pt line are gone; every cell now shares the row's line.
* At 7.5pt no title wraps any more, "15 /apply: build, verify, prove, never commit" and "22 As ferramentas do time: pull requests, issues e quadros" included, so the wrap of Behaviour 3 is not seen in this build.
* The result: in both editions the contents is page 4 and the Prologue opens on page 5; "26 Asking for more" is on page 4 at 173, "26 Pedir mais" at 182. Every chapter's page moved back by one, as Out of scope expected.
* Headroom, proved: a run with two extra one-line rows (a copy of row 26 as 27 and 28, added by a script in the scratchpad, not in the repository) kept both contents on one page; the screenshots show room for several more.
* The guard counts the rendered PDF: the contents carries `id="contents"`, and the count runs from that destination's page to the first outline entry after it. It returns its finding instead of raising, so both editions are built and both report before exit 1; docs/01 says so.
* The guard, proved once: a 14pt row font was tried first and only `pt` failed, because the fixed line height kept English rows short; the proof that counts set the cells' padding to 6pt, and `make book` printed `Makefile:1: book: en contents takes 2 pages; it must fit on one` and the same for `pt`, and exited 1. The padding went back to 1.25pt.
* The screenshots, `work/done/pdf-contents-one-page-en-contents.png` and `-pt-contents.png`, are page 4 at 200 dpi. At that resolution the border above row 16 renders a pixel thicker than the rest; it is the same 0.75pt rule, rounded by the rasteriser. The author confirms the numbers against the page numbers.
* No abstraction, dependency or tool was added; no ADR.
