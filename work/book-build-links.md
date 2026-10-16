# book-build-links

**Objective.** The author runs `make book` and it fails, naming the chapter and line, when a link points to a heading that does not exist; a source note is linked at every mention, whatever its key; and appendices come in numeric order.

**Behaviour.**

The proof uses a scratch copy of the tree with scratch edits, never the tree itself. Findings B2 (book part), B8 (book part) and B9 were re-read first and hold.

* Today (seen): a scratch `[b](10-the-documents.md#no-such-heading)` in `book/en/02-how-agents-see.md` makes weasyprint print `ERROR: No anchor #the-documents.md__no-such-heading for internal URI reference` (pandoc drops the file's leading digits from the id), which `make book` shows as `Makefile:1: book: ERROR: ...` and still exits 0, with all four files written. A missing image does the same (`ERROR: Failed to load image at ...`).
* After the change, the same link prints one finding per chapter line it stands on, and the build exits 1 after both editions were built, so each reports:

      book/en/02-how-agents-see.md:114: book: 10-the-documents.md#no-such-heading names no heading

* The same link on lines 114 and 118 prints two findings; two different broken links print two. A valid `[g](10-the-documents.md#one-place-per-fact)` prints nothing, and a broken `#one-place` is not found on a line holding only `#one-place-per-fact`.
* The EPUB reads the same prepared chapters, so the one check covers it: pandoc writes an unresolvable EPUB link without a word.
* Any other weasyprint `ERROR:` line fails the build as `Makefile:1: book: ERROR: <text>` (the missing image); a `WARNING:` line is printed and the build goes on, as today. An anchor error whose link is found in no chapter prints as that same `Makefile:1:` line.
* B8: with a scratch chapter holding `First[^Abc] and again[^Abc]`, `Colon[^low]: then text, and again[^low]`, `Normal[^ok] and[^ok]` and the three definitions, the prepared text links the second mention of each key to its note (`again[^1^](#note-n-Abc){.footnote-ref}`), the third note's second mention shows `[^3^]`, and each definition carries its `[]{#note-n-<key>}`. Today the uppercase key is never linked, the mid-line `:` is not counted as a mention, and the numbers run short (`ok` shows 2).
* A key with `.` or `_` (`[^Key.2]`) is a key; a key with a space is not a note. A definition indented up to three spaces gets its id; a mention later on a definition line (`[^a]: text[^b]`) counts for `b`.
* B9: scratch files `A1-x.md`, `A2-x.md` and `A10-x.md` come after chapter 26 in the order A1, A2, A10 (today A1, A10, A2). Numbered chapters keep their order.
* Nothing changes for today's tree: `make book` prints the same lines (two `user-select` warnings on pandoc's highlighting styles, the four paths), exits 0, and each PDF has the same number of pages as before. Checked read-only in a scratch copy: `book/` holds no link with `.md#`, and no `ERROR:` line today.

**Contract.** `scripts/build_book.py`, rule "book":

* A finding for an unresolved heading link: `book/<edition>/<NN-slug.md>:<line>: book: <target>#<anchor> names no heading`, `<target>` as written in the link. A weasyprint `ERROR: No anchor #<file>__<anchor> ...` is matched to a link `](<target>#<anchor>` of a chapter of the edition, followed by `)`, a space or `>`, when `<file>` ends the lower-cased `<target>` (the id drops leading digits).
* Any other `ERROR:` line of weasyprint: `Makefile:1: book: ERROR: <text>`. Both kinds are collected for the edition, the other edition is built, then everything prints and the exit is 1, as the contents guard does (docs/01 §How errors travel). No path is printed on failure.
* `scripts/markdown.py` gives `NOTE_DEFINITION` and `NOTE_MENTION` (`parity-notes-readmes`' Contract). `build_book.py` drops its own `NOTE_REF` and `NOTE_DEFINITION`; in `prepare`, a mention is every `NOTE_MENTION` match after the definition marker of the line, and the id span goes after the definition's colon and the spaces that follow it, where it is today.
* `chapters(edition)` sorts the appendices by the integer after the `A`, then by name.

**Out of scope.**

* `check_parity.py`'s own pattern: `parity-notes-readmes`, which runs first.
* The site's navigation, which sorts file names as text (`A10-` before `A2-`) and has no appendix today: a finding of its own if one is added.
* A chapter whose number carries a letter, `12a-quick-guide.md` (`quick-guide`): `chapters()` and `CHAPTER_LINK` read `NN-` and `A<n>-` only, so `make book` leaves it out until `renumber-chapters`. Not widened here; see Decisions.
* Checking book links inside `make verify`: the site build now fails the same links (`site-build-anchors`), and `make book` is not part of verify (docs/01).
* The `user-select` warning on pandoc's highlighting styles.

**Done when.**

* [ ] In a scratch copy, each Behaviour case prints what is stated, the output recorded on the page; the heading link, the missing image and the three note cases show the before and the after.
* [ ] `make book` on the tree builds both editions as before: the same lines, the same page counts, exit 0, and both PDF paths are given to the author.
* [ ] `parity-notes-readmes` is `[x]` before this starts; if it is not, the line waits as `[?]`.
* [ ] docs/01: the `make book` row says a link to a heading that does not exist, or any weasyprint error, fails the build, and appendices come in numeric order; §How errors travel says the same of `build_book.py` and that both editions build first; the `scripts/build_book.py` row names the note patterns as shared.
* [ ] `make verify` green. No screen changes for today's book, so no screenshot.

**Decisions in the review.**

* The check reads weasyprint's error and does not parse the HTML for ids: weasyprint is the tool that cannot place the link, its wording is fixed by the pinned version (ADR-0014), and the code stays short (recommendation of this session).
* Every weasyprint `ERROR:` fails, not only the anchor one: weasyprint logs an error for what it could not do, docs/01 says a failure is one line and exit 1, and the book has none today.
* The line depends on `parity-notes-readmes` (it creates the shared patterns and says this line imports them): the driver should add `· after parity-notes-readmes` to this line in docs/06. `NOTE_MENTION` is imported, not `mentions(line)`, because the build edits the line at the match positions.
* `12a-quick-guide.md` is not matched by `chapters()` today, so `quick-guide`'s Done-when (the chapter in the PDF contents and the EPUB) cannot be proved until the glob reads `NN` followed by letters, or `renumber-chapters` runs. Left to the author: widening it here would add a scope the finding did not name.
* Pages in flight: none edits `scripts/build_book.py`. `parity-notes-readmes` edits `scripts/markdown.py` (first). docs/01 rows are shared with `site-build-anchors` and `epub-chapter-links` in other rows: stage by hunk (docs/05 §6).
