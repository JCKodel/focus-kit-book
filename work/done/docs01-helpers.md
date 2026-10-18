# docs01-helpers

**Objective.** Whoever reads docs/01 finds every helper scripts/markdown.py shares, `target_end` among them, with every script that uses each, and learns that the width check reads the prose check's files through `check_prose.py`'s `language_of`. Found by `m16-review` (work/done/m16-review.md, doc-2 seen: "docs/01:31 and :39, `mask` is said shared by the prose and link checks; `check_parity.py` and `build_book.py` use it too, `target_end` is not named, nor `check_width.py`'s use of `language_of`").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The row lists the names another piece of code calls: the ones other scripts import (`front_matter`, `mask`, `line_kinds`, `target_end`, `NOTE_DEFINITION`, `NOTE_MENTION`, `mentions`) and the ones those are built from that the row already names or that a reader of the fence rule needs (`FENCE_OPENING`, `closes`, `mask_inline`). `blank` and `FIELD`, a few characters each and read by nothing outside their own function, are left out, as today. Source: docs/01:39; the imports of scripts/*.py when this page was written.
2. Users as the imports give them, after `width-comment-fence` and `fence-commonmark`: `front_matter` by parity and the book build; `mask` by the prose, link and parity checks and the book build; `line_kinds` by `mask` and the width check; `mask_inline` by `mask` and `line_kinds`; `target_end` by `mask_inline` and the link check; `NOTE_DEFINITION` and `mentions` by parity, `NOTE_DEFINITION` and `NOTE_MENTION` by the book build. Source: scripts/check_prose.py:11, check_links.py:20, check_parity.py:13, build_book.py:22, check_width.py (as `width-comment-fence` leaves it).
3. The width check's use of `language_of` goes on its own row (line 31), where a reader looks for what the width check reads, not on markdown.py's. Source: scripts/check_width.py:12, :46.
4. This page writes both rows whole, from the text the two earlier slugs leave, keeping `fence-commonmark`'s fence-rule words as they are and `width-comment-fence`'s description of `line_kinds`, now split into one entry per name so each gets its users. Source: work/width-comment-fence.md and work/fence-commonmark.md, their Contracts.
5. No docs/03 term, no new queue line, no split. Source: docs/03; docs/05 §1.

**Behaviour.**

* After the delivery, docs/01's markdown.py row names `front_matter`, `mask`, `line_kinds`, `FENCE_OPENING`, `closes`, `mask_inline`, `target_end`, `NOTE_DEFINITION`, `NOTE_MENTION` and `mentions`, each with what it does and every script or function that uses it.
* A check /apply runs: for each name the row gives, `grep -n "<name>" scripts/*.py` finds an import or a call in each user the row names and in no script the row leaves out.
* docs/01's `check_width.py` row says the width check reads the files the prose check reads, chosen by `check_prose.py`'s `language_of`.
* Edge: no other row of docs/01 changes, and no script changes.
* Fails: a script that imports a markdown.py name the row does not give it; a row naming a user that does not use the name.

**Contract.** docs/01, two rows of the folder layout replaced whole, on one line each as today.

Line 31:

```
scripts/check_width.py   every fenced block but TypeScript, outside front matter and HTML comments, in the files the prose check reads, both editions and both READMEs, chosen by check_prose.py's language_of, keeps to 74 columns, a tab to the next multiple of 8 (rule "width")
```

Line 39:

```
scripts/markdown.py      front_matter: the fields and the body, used by parity and the book build; mask: front matter, code and HTML comments as spaces, used by the prose, link and parity checks and the book build; line_kinds: each line as front matter, a fence, code with its fence's info string, or text with whether it starts inside an HTML comment, used by mask and the width check; FENCE_OPENING and closes: the fence rule as CommonMark reads it at the margin, a run of three or more backticks or tildes after at most three spaces, a backtick run's info string holding no backtick, closed by a line of at most three spaces and a run of the same character at least as long, with nothing after it but spaces or tabs, used by line_kinds; mask_inline: one line's inline code, link targets and HTML comments as spaces, carrying whether the line ends inside a comment, used by mask and line_kinds; target_end: the `)` that closes a link target, its inner parentheses counted, used by mask_inline and the link check; NOTE_DEFINITION, NOTE_MENTION and mentions: a note's definition marker, its mention with any key pandoc reads, and the keys cited on a masked line, NOTE_DEFINITION and mentions used by parity, the two patterns by the book build
```

If /apply finds that `width-comment-fence` or `fence-commonmark` landed with other words or other users, it writes these rows from what the code then does and records the difference under Divergences.

No new term; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* scripts/markdown.py's module docstring: it names the module's purpose, not its users.
* `blank` and `FIELD` (decision 1).
* The rows of the other scripts: doc-2 names only these two.

**Order with the other slugs of this batch.** Fourth, and last of the three that touch docs/01: after `width-comment-fence`, which adds `line_kinds` and edits lines 31 and 39, and `fence-commonmark`, which changes the fence-rule words of line 39. This page rewrites both lines whole from what they leave.

**Done when.**

* [x] docs/01:31 and :39 are the Contract's two rows, byte for byte (or as the Contract's last paragraph allows, recorded), and nothing else in docs/01 changes.
* [x] The grep check of Behaviour run for every name and its result recorded on this page.
* [x] `make verify` green; no em dash.
* [x] No screenshot: no rendered change (docs/05 §5 Proof of a screen).
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its own hunk of docs/06 (docs/05 §6), other sessions' changes left unstaged; commit message in a `commit` block.

**Proof.** The rows of docs/01:31 and :39 compared with the Contract's two blocks by `diff`: identical, before the review's two fixes below. `git diff --stat docs/01-Architecture.md`: 2 insertions, 2 deletions, those two lines.

The grep check, `grep -nw "<name>" scripts/*.py` for each name the row gives, read against the function each hit stands in:

* `front_matter`: imported and called by check_parity.py:13, :42 and build_book.py:22, :131, :170; no other script.
* `mask`: imported and called by check_prose.py:11, :71, check_links.py:20, :44, check_parity.py:13, :29 and build_book.py:22, :172, :315; check_width.py names it only in its docstring.
* `line_kinds`: called by `mask` (markdown.py:91) and imported and called by check_width.py:14, :26.
* `FENCE_OPENING` and `closes`: called only inside `line_kinds` (markdown.py:75, :68).
* `mask_inline`: called by `line_kinds` (markdown.py:81) and `mask` (markdown.py:93); no script imports it.
* `target_end`: called by `mask_inline` (markdown.py:139) and imported and called by check_links.py:20, :59.
* `NOTE_DEFINITION`: imported and used by check_parity.py:13, :30 and build_book.py:22, :180. `NOTE_MENTION`: imported and used by build_book.py:22, :186. `mentions`: imported and called by check_parity.py:13, :33. Inside markdown.py, `mentions` reads both patterns (:150, :153).
* `language_of`: imported and called by check_width.py:13, :41, which skips every file for which it returns None, as the prose check does (check_prose.py:67): the two READMEs and the `.md` files of book/en/ and book/pt/.

No script imports a markdown.py name the row does not give it, and every user the row names uses the name.

`make verify` green: build, parity, em dash, prose, width, links, disclosure.

**Divergences.** `width-comment-fence` and `fence-commonmark` landed with the words and users the Contract assumed. Line 39 differs from the Contract in two places, both fixed after the review, both truer to the code:

* `mask_inline`: "one line's inline code, HTML comments and, when asked, link targets as spaces" for "one line's inline code, link targets and HTML comments as spaces": it blanks a target only when `keep_targets` is False (scripts/markdown.py:140), and `line_kinds` calls it with True.
* the note entry ends "the two patterns by mentions and the book build" for "the two patterns by the book build": `mentions` reads both (scripts/markdown.py:150, :153), and the row names every other function that uses a name.

**Omissions.** None.

**Decisions taken in /apply.** None beyond the page's.

**Review.** Delivery review by a read-only Opus agent on the diff of docs/01, this delivery's line of docs/06 and this page, against the page, docs/04 and AGENTS.md. Three findings, all fixed: the note entry left out that `mentions` reads both patterns, and the `mask_inline` entry said it always blanks link targets (both under Divergences); the last Done when item was ticked before the line was `[x]` and staged, true once this page closed. Everything else checked out: the imports and users, the descriptions against scripts/markdown.py, the check_width.py row against `language_of`, the Proof's line numbers, no em dash. `make verify` green again after the fixes.

```commit
docs(docs01-helpers): name every markdown.py helper and its users

- docs/01: the markdown.py row gives each shared name, target_end among them, and every user
- docs/01: the check_width.py row reads the prose check's files through language_of

work/done/docs01-helpers.md
```
