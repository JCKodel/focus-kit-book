# pdf-footnote-numbers

**Objective.** A reader who opens either edition's PDF in Preview on macOS sees the notes at the foot of the page as `pdf-design` drew them: plain numbers and text under a short amber bar, with no amber block over the first words of every note.

**Behaviour.**

* The cause is in `pandoc/pdf.css`, not in the numbers. The short amber bar above the notes (`@page` → `@footnote`, lines 22 to 28) is a `linear-gradient` cut to 2.25pt tall by `background-size`. Poppler keeps that cut, so `pdftoppm` shows only the bar. Preview (PDFKit) ignores it and paints the 30pt-wide gradient over the whole height of the notes area, which hides the note numbers and the first letters of every note. The author saw this on every page that has notes, in both editions.
* The defect is reproduced before the fix: page 10 of `output/one-page-at-a-time.pdf` (chapter 1, notes 1 and 2) is rendered with PDFKit, the engine Preview uses, through a script in the scratchpad, never in the repository. The amber block shows, as in the author's screenshots.
* After the fix, the same render of the same page shows no block. The numbers 1 and 2 and the words "METR" and "DORA" are on the cream page in their usual colours, and the amber bar is still there above the first note: 30pt wide, 2.25pt tall, 10.5pt above the notes with 8.25pt of padding before them, as today.
* The same holds in `output/uma-pagina-de-cada-vez.pdf` on a page with several notes (the page of notes 2 to 4 of chapter 2 in the author's screenshot).
* Poppler's render of the same pages is unchanged: the bar, the numbers and the notes look as they do today.
* The bar is drawn without a gradient. The way (an SVG or a solid-colour background image of 30pt × 2.25pt, no-repeat, or another way that PDFKit and poppler both draw the same) is /apply's choice, and the CSS comment above `@footnote` says which and why: a gradient's `background-size` is not respected by Preview.
* Nothing else in the PDF changes: the note numbers and the calls in the text (Iosevka Term, 6pt, superscript), the note text, the chapter openings, the contents, the running heads and the cover stay the same. Page numbering does not move. The EPUB and the site are not touched; neither has the bar.

**Contract.** None. No message, file name or output path changes.

**Out of scope.**

* The degenerate link rectangles of a note's second mention (zero height, or y reversed) seen in page 10's annotations: Preview showed no defect there, and nobody reported one.
* A new look for the notes: the author reported a rendering defect, not a design change.
* Other PDF viewers (Acrobat, browsers): checked only if /apply's render shows they differ; the author reads in Preview.
* A check in `make book` that forbids gradients: one occurrence, and the cause is written in the CSS comment.

**Done when.**

* [x] The PDFKit render of page 10 (en) is saved before the fix as `work/done/pdf-footnote-numbers-en-before.png`, showing the block.
* [x] After the fix, PDFKit renders of page 10 (en) and of the chapter 2 page with notes 2 to 4 (pt) are saved as `work/done/pdf-footnote-numbers-en-after.png` and `work/done/pdf-footnote-numbers-pt-after.png`, with no block and with the bar.
* [x] A poppler render of the same en page, at the same resolution, shows the bar at the same place and size as before.
* [x] docs/01's `pandoc/pdf.css` entry says how the notes' bar is drawn, if it names the technique.
* [x] `make verify` is green, `make book` builds both editions, and the author gets the paths of both PDFs and confirms in Preview that no note has the block.

## What happened

* **The cause, exactly.** weasyprint drew the bar as an axial shading painted with `sh` over the whole notes area (clip 446pt × 48pt on page 10), with a luminosity soft mask whose gradient stops it at 30pt. The 2.25pt height lived only in the mask group's BBox (`0 0 446 3`). Preview's live view clamps the mask at that edge instead of treating outside it as transparent, so the 30pt column ran the whole height of the notes.
* **Reproduction diverged from the plan.** PDFKit offline (`PDFPage.draw`, its thumbnail, CoreGraphics `drawPDFPage`, an offscreen `PDFView`) drew the bar correctly every time. Only Preview itself showed the block, so the before and after images are captures of a Preview window opening that one page, extracted to a PDF in the scratchpad. The page in Preview is white, not cream: the PDF has no page colour, so "the cream page" in Behaviour was a slip of the page, not a change.
* **The fix.** `@footnote`'s background is an inline SVG of one amber rectangle, 30pt × 2.25pt, `no-repeat 0 0 / 30pt 2.25pt`; the CSS comment says why not a gradient. No other gradient is in `pandoc/`.
* **Proof.** Preview after the fix: page 10 (en) and page 16 (pt, chapter 2, notes 2 to 4) show the numbers and the first words on the page, with the bar above the first note. Poppler at 216 dpi, before against after, on both pages: the only pixels that differ are inside the bar's own rectangle (x 127 to 217, same place, same 30pt width). Before, the mask's 3pt BBox gave about 8 hard pixel rows; now 6 full rows and 2 anti-aliased ones, which is 2.25pt exactly. Page counts: 180 (en), 190 (pt).
* **docs/01** names no technique for the bar, so it is unchanged.
* **Left to the author:** confirming in Preview, on the full PDFs, that no note has the block.
