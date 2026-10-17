# epub-chapter-links

**Objective.** A reader of either edition's EPUB sees a pointer to a chapter in the colour of the text around it, as in the PDF and as docs/04 already says, and it still opens the chapter.

**Behaviour.**

The proof uses a scratch copy of the tree and the EPUBs it builds, never the tree's `output/` as evidence of the old state. Finding B4 was re-read first and holds.

* Today (seen): in the unzipped `one-page-at-a-time.epub`, a chapter pointer is `<a href="ch016.xhtml#apply.md__chapter-15-apply">`. pandoc puts the file's name before `__chapter-` in the target, so the rule `a[href*="#chapter-"]` of `pandoc/epub.css` matches none of the 72 pointers of the English edition (73 in the Portuguese) and each keeps the reader's link colour.
* After the change, the stylesheet inside the EPUB reads `section a[href*="__chapter-"] { color: inherit; text-decoration: none; }`; it matches every chapter pointer in the text of a chapter, as many as the edition's source holds `](NN-<slug>.md)` links at /apply time (72 en, 73 pt today), and the link still has its `href`.
* Rendered, a pointer in a paragraph shows in the paragraph's colour with no underline (`inherit` is also why a reader's night mode follows the text; the proof shows the light page); a link to a heading of a chapter (`...md__where-the-idea-comes-from`), a bare address in a source note and any other link keep the link colour.
* The EPUB's contents page (`nav.xhtml`) is untouched: its 27 chapter entries and its section entries look as before, because the rule starts at `section`, and the contents page has none.
* The PDF, the site and the text of the chapters do not change.

**Contract.** `pandoc/epub.css`, the rule and its comment:

    /* A pointer to a chapter reads in the text's color, as in the PDF; it still works as a link. pandoc prefixes a target with the file's name, so the id is matched by its `__chapter-` part, and only in a chapter's text, not on the contents page. */
    section a[href*="__chapter-"] { color: inherit; text-decoration: none; }

No other file, message or output name changes.

**Visual reference.** The PDF: `pandoc/pdf.css` already uses `a[href*="__chapter-"] { color: inherit; }`. Viewport: an EPUB reflows to the reader's screen, so a width pair adds nothing.

**Out of scope.**

* The contents page's link style: a reader's own, and the PDF has its own contents design.
* A link to a heading of a chapter, or an address in a note: neither is a pointer to a chapter (docs/04).
* An EPUB validator: `epubcheck` is installed, but nothing in the delivery changes the structure.

**Done when.**

* [x] In a scratch build of both editions, the unzipped stylesheet holds the new rule, and a script in the scratchpad counts the `<a>` whose `href` has `__chapter-` inside a `section` of `EPUB/text/`: as many as the source's `](NN-<slug>.md)` links of each edition at that time (72 and 73 today); `nav.xhtml` is not inside a `section`.
* [x] Proof of a screen (docs/05 §5), rendered from the unzipped chapter files and the EPUB's own stylesheet in Chrome, which is installed, since no EPUB reader is: one chapter page of each edition where a pointer stands in a paragraph, before and after, saved as `work/done/epub-chapter-links-<en|pt>-<before|after>.png`, and the contents page once, `work/done/epub-chapter-links-en-contents.png`. The author confirms the pointer in the text's colour, and may open the built EPUB in Apple Books to see it there.
* [x] docs/01: the `pandoc/epub.css` row says a chapter pointer prints in the text's colour. docs/04 line 40 is unchanged, as this makes its sentence true.
* [x] `make verify` green and `make book` builds both editions; the author gets the paths of both EPUBs.

**Decisions in the review.**

* The rule starts at `section`, so the contents page keeps its link colour: a bare `__chapter-` selector would also strip 27 entries of the EPUB's contents of their colour, a change nobody asked for (recommendation of this session).
* The comment says why the id is matched by its `__chapter-` part, since the old selector failed for lack of that knowledge (`pdf-design` recorded the same cause for the PDF).
* One screenshot per edition and state, not the 1280 and 390 pair of docs/05 §5: that slot describes the site; an EPUB has no fixed width (recommendation of this session).
* Pages in flight: none edits `pandoc/epub.css`. docs/01's `pandoc/epub.css` row is not edited by another line; `site-build-anchors` and `book-build-links` edit other rows (stage by hunk, docs/05 §6).

**Proof.**

Two scratch copies of the tree, `git archive HEAD` before the change and the same with the new `pandoc/epub.css` after, each built with `scripts/build_book.py`; the four EPUBs unzipped. A script in the scratchpad counts, with Python's HTML parser, the `<a>` whose `href` holds `__chapter-` inside and outside a `section` of `EPUB/text/`, and the source's `](NN-<slug>.md)` links of each edition:

```text
== before
en: source links 72; in a section of text/ 72; outside a section 0; nav has <section> False; nav __chapter- links 27; new rule False; old rule True
pt: source links 73; in a section of text/ 73; outside a section 0; nav has <section> False; nav __chapter- links 27; new rule False; old rule True
== after
en: source links 72; in a section of text/ 72; outside a section 0; nav has <section> False; nav __chapter- links 27; new rule True; old rule False
pt: source links 73; in a section of text/ 73; outside a section 0; nav has <section> False; nav __chapter- links 27; new rule True; old rule False
```

Every chapter pointer stands inside a `section`, and each keeps its `href` (`ch016.xhtml#apply.md__chapter-15-apply`). The contents page has no `section`, so its 27 chapter entries, which an unscoped selector would have matched, keep the link colour. Between before and after, the files of `EPUB/text/` and `nav.xhtml` are byte for byte the same in both editions, and the PDFs keep their 202 (en) and 213 (pt) pages: only the stylesheet changed.

Screens, rendered by headless Chrome from the unzipped chapter 1 file (`ch002.xhtml`) with the EPUB's own stylesheet, 720 pixels wide, cropped to the part with the pointers:

* `work/done/epub-chapter-links-en-before.png`, `-pt-before.png`: "chapter 14", "chapter 15", "chapter 3" and "chapter 9" (pt "capítulo") blue and underlined.
* `work/done/epub-chapter-links-en-after.png`, `-pt-after.png`: the same four in the paragraph's black, no underline; the note marks 1 and 2 and the two addresses of the source notes stay blue and underlined.
* `work/done/epub-chapter-links-en-contents.png`: the contents page, chapter and section entries blue as before; the screenshot of the old build is the same file, byte for byte.

The author confirms the pointer in the text's colour, and may open `output/one-page-at-a-time.epub` in Apple Books to see it there.

**Divergences.** The book has no link from a chapter's text to a heading of a chapter today: the text's internal links are chapter pointers, note marks and code line anchors (`#cb1-1`). The case of the Behaviour (`...md__where-the-idea-comes-from`) is seen on the contents page, whose section entries keep the link colour; in the text, the selector cannot match such a link, since its id has no `__chapter-`.

**Noted, not fixed.** Nothing.

**Dropped.** Nothing.

**Decisions.**

* The proof crops one tall screenshot of each chapter file instead of scrolling to a heading: headless Chrome rendered a blank page when given the heading's fragment (decision of this session).
* docs/01's row says "a chapter pointer in the text's colour", placed before the notes, in the order the rules stand in the stylesheet.
* No ADR and no manual: the change makes the EPUB do what docs/04 already said, and nothing a person does by hand changed.

```commit
fix(epub-chapter-links): match pandoc's chapter ids in the EPUB rule

- the EPUB's rule matches pandoc's `__chapter-` ids, only inside a chapter's section
- the contents page keeps its link colour
- docs/01's epub.css row says so

work/done/epub-chapter-links.md
```
