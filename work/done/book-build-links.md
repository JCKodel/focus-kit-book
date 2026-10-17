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

* [x] In a scratch copy, each Behaviour case prints what is stated, the output recorded on the page; the heading link, the missing image and the three note cases show the before and the after.
* [x] `make book` on the tree builds both editions as before: the same lines, the same page counts, exit 0, and both PDF paths are given to the author.
* [x] `parity-notes-readmes` is `[x]` before this starts; if it is not, the line waits as `[?]`.
* [x] docs/01: the `make book` row says a link to a heading that does not exist, or any weasyprint error, fails the build, and appendices come in numeric order; §How errors travel says the same of `build_book.py` and that both editions build first; the `scripts/build_book.py` row names the note patterns as shared.
* [x] `make verify` green. No screen changes for today's book, so no screenshot.

**Decisions in the review.**

* The check reads weasyprint's error and does not parse the HTML for ids: weasyprint is the tool that cannot place the link, its wording is fixed by the pinned version (ADR-0014), and the code stays short (recommendation of this session).
* Every weasyprint `ERROR:` fails, not only the anchor one: weasyprint logs an error for what it could not do, docs/01 says a failure is one line and exit 1, and the book has none today.
* The line depends on `parity-notes-readmes` (it creates the shared patterns and says this line imports them): the driver should add `· after parity-notes-readmes` to this line in docs/06. `NOTE_MENTION` is imported, not `mentions(line)`, because the build edits the line at the match positions.
* `12a-quick-guide.md` is not matched by `chapters()` today, so `quick-guide`'s Done-when (the chapter in the PDF contents and the EPUB) cannot be proved until the glob reads `NN` followed by letters, or `renumber-chapters` runs. Left to the author: widening it here would add a scope the finding did not name.
* Pages in flight: none edits `scripts/build_book.py`. `parity-notes-readmes` edits `scripts/markdown.py` (first). docs/01 rows are shared with `site-build-anchors` and `epub-chapter-links` in other rows: stage by hunk (docs/05 §6).

## What happened

**The error it catches** (docs/05 §7): a link to a heading that does not exist built a PDF and an EPUB with exit 0; weasyprint's `ERROR:` line went by as one more `Makefile:1:` line, and pandoc's EPUB writes the same link without a word. A second mention of a note whose key held an uppercase letter or a `.`, or that stood before a `:` mid-line, was printed as a second note, and every note after it took a wrong number. Appendices would have come as `A1`, `A10`, `A2`.

**Built.**

* `scripts/build_book.py`: `run(..., errors=True)` returns weasyprint's `ERROR:` lines instead of printing them; `located` turns each into findings, a `No anchor #<file>__<anchor>` error at each chapter line holding `](<target>#<anchor>` (masked, so a link quoted in code is not found), once per line, and any other as `Makefile:1: book: ERROR: <text>`. `build` returns them with the contents guard's finding, and `main` prints them after both editions, exit 1, no path.
* `prepare` reads notes with `NOTE_DEFINITION` and `NOTE_MENTION` from `scripts/markdown.py` (the first use was `check_parity.py`, by `parity-notes-readmes`); its own `NOTE_REF` and `NOTE_DEFINITION` are gone. Mentions are read after the definition marker; the id span goes after the colon and every space after it.
* `chapters` sorts appendices by the number after `A`, then by name.
* docs/01: the `make book` row, §How errors travel, and the `build_book.py` and `markdown.py` rows.

**Diverged from the contract.** Nothing.

**Proof.** Each case ran in its own fresh copy: before, a `git archive HEAD`; after, the tracked files of the working tree with this delivery's changes. Lines are appended to chapter 2 (112 lines) after a blank line, so they land on 114, 116 and 118. The two `user-select` warnings print in every case and are left out below. The scratch folder's path is shortened to `<scratch>`.

1. `[b](10-the-documents.md#no-such-heading)` on en 114. Before, exit 0 and the four paths:

        Makefile:1: book: ERROR: No anchor #the-documents.md__no-such-heading for internal URI reference

    After, exit 1, no path:

        book/en/02-how-agents-see.md:114: book: 10-the-documents.md#no-such-heading names no heading

2. The same link on en 114 and 118. Before, two identical `Makefile:1:` lines, exit 0. After, exit 1:

        book/en/02-how-agents-see.md:114: book: 10-the-documents.md#no-such-heading names no heading
        book/en/02-how-agents-see.md:118: book: 10-the-documents.md#no-such-heading names no heading

3. Two different broken links in en (114 and 116) and the first in pt (114). Before, three `Makefile:1:` lines, exit 0. After, both editions built, then, exit 1:

        book/en/02-how-agents-see.md:114: book: 10-the-documents.md#no-such-heading names no heading
        book/en/02-how-agents-see.md:116: book: 13-queue-and-milestones.md#also-missing names no heading
        book/pt/02-how-agents-see.md:114: book: 10-the-documents.md#no-such-heading names no heading

4. `[g](10-the-documents.md#one-place-per-fact)` on 114 and `[h](10-the-documents.md#one-place)` on 116. After, exit 1, line 114 not found:

        book/en/02-how-agents-see.md:116: book: 10-the-documents.md#one-place names no heading

    The valid link alone on 114: the four paths, exit 0, before and after.

5. `![x](../assets/no-such.png)` on en 114. Before, exit 0 with the paths; after, exit 1, no path, pandoc's EPUB warning still printed as it goes:

        Makefile:1: book: [WARNING] Could not fetch resource ../assets/no-such.png: PandocResourceNotFound "../assets/no-such.png"
        Makefile:1: book: ERROR: Failed to load image at 'file://<scratch>/book/assets/no-such.png': URLError: <urlopen error [Errno 2] No such file or directory: '<scratch>/book/assets/no-such.png'>

6. A link found in no chapter: `[s](#no-such-here)` on en 114, a link to the chapter's own page, whose target is empty. After, exit 1:

        Makefile:1: book: ERROR: No anchor #how-agents-see.md__no-such-here for internal URI reference

7. B8, `prepare` on a scratch `book/en/n.md`. Before:

        First[^Abc] and again[^Abc].
        Colon[^low]: then text, and again[^low].
        Normal[^ok] and[^2^](#note-n-ok){.footnote-ref}.

        [^Abc]: Abc note.
        [^low]: []{#note-n-low}Low note.
        [^ok]: []{#note-n-ok}Ok note.

    After:

        First[^Abc] and again[^1^](#note-n-Abc){.footnote-ref}.
        Colon[^low]: then text, and again[^2^](#note-n-low){.footnote-ref}.
        Normal[^ok] and[^3^](#note-n-ok){.footnote-ref}.

        [^Abc]: []{#note-n-Abc}Abc note.
        [^low]: []{#note-n-low}Low note.
        [^ok]: []{#note-n-ok}Ok note.

8. The other keys, `prepare` on a scratch `book/en/e.md`. After (before, `Key.2` and `k_1` were never linked, nor the indented definition given its id):

        Dot[^Key.2] and[^1^](#note-e-Key.2){.footnote-ref}, under[^k_1] and[^2^](#note-e-k_1){.footnote-ref}, space[^a b].
        First b[^b].

        [^a]: []{#note-e-a}text[^3^](#note-e-b){.footnote-ref}
           [^ind]: []{#note-e-ind}indented.
        [^Key.2]: []{#note-e-Key.2}Dot note.
        [^k_1]: []{#note-e-k_1}Under note.
        [^b]: []{#note-e-b}Bee note.

    pandoc reads `[]{#note-e-Key.2}` as `id="note-e-Key.2"` and the link as `href="#note-e-Key.2"`.

9. B9, scratch `A1-x.md`, `A2-x.md`, `A10-x.md` in `book/en`; the last six of `chapters("en")`. Before `... 26-asking-for-more.md A1-x.md A10-x.md A2-x.md`; after `... 26-asking-for-more.md A1-x.md A2-x.md A10-x.md`.

10. Today's tree. `prepare`, before and after, gives the same lines for all 54 chapters of both editions. `make book` on the tree, before and after: the two `user-select` warnings and the four paths, exit 0; the English PDF has 202 pages and the Portuguese 213, as before. `make verify` green.

**Noted, not fixed.** A link to a heading of its own chapter, `[s](#x)`, fails the build as `Makefile:1:` (case 6), not at its line: the Contract matches a link with a target. The site build reports it at its line (`site-build-anchors`), and `make verify` runs that.

**Dropped.** Nothing.

**Decisions.**

* Taken alone in this batch: only weasyprint's `ERROR:` lines are collected (`run(..., errors=True)`); pandoc's calls print their lines as before, since pandoc writes `[WARNING]` and fails with a non-zero exit.
* Taken alone in this batch: a link with an empty target (`](#x)`) is not matched to its own chapter; it prints as `Makefile:1:` as the Contract says of a link found in no chapter (case 6, Noted).
* Taken alone in this batch: `<file>` is compared lower-cased with the lower-cased target, so an appendix `A1-...` matches whatever case pandoc gives its id; a link in a code span is not matched, since the chapter is read through `mask`.
* Taken alone in this batch: a weasyprint error stops nothing; the edition's PDF and EPUB are still written, as with the contents guard, and no path is printed.
* No screenshot, no ADR and no manual: the book renders as before, and nothing a person does by hand changes. The READMEs say `make book` writes the files and are unchanged.
* No queue line is resolved by this one: none waits on `book-build-links`.

```commit
fix(book-build-links): fail on missing headings, link every note

- build_book.py fails on a link to a heading that does not exist, at each line
- any other weasyprint ERROR fails the book; both editions build first
- notes read with markdown.py's shared patterns, whatever the key
- appendices come in numeric order
- docs/01 says so

work/done/book-build-links.md
```
