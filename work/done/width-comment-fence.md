# width-comment-fence

**Objective.** `make verify`'s width check measures only the fenced blocks a reader is shown: a fence inside an HTML comment, or inside the front matter, is skipped, as `mask` already skips it, because both read the lines through one shared helper. Found by `m16-review` (work/done/m16-review.md, build-3 latent: "`scripts/check_width.py:35` measures a fence inside an HTML comment, which `mask` skips; none exists").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. One line reader, shared. The walk over a file's lines that tells front matter, a fence, code and text apart lives in `mask` (scripts/markdown.py), the first occurrence; `check_width.py` is the second, and today it repeats only part of it, which is the fault. So the walk moves into markdown.py as one helper, `line_kinds`, which `mask` and the width check both use, instead of a second comment tracker in the width check. Source: AGENTS.md (abstraction on the second concrete occurrence); `code-width` decision 5, which moved the fence rule into markdown.py for the same reason; docs/01 (markdown.py is the Markdown reading the scripts share).
2. This reverses one decision of `code-width`'s /apply ("The check skips no front matter or HTML comment separately: no fence sits in either today, and mask's comment rule is not the width rule's concern"): build-3 shows the two readings disagree, and a block in a comment is shown to no reader of the site, the PDF or the EPUB, so it has nothing to keep to 74 columns for. Source: work/done/code-width.md, Decisions taken in /apply; m16-review build-3.
3. Front matter comes with it. The line says "as `mask` does", and `mask` skips front matter as it skips a comment; the shared reader gives both for the same price, and leaving it out would keep a second latent gap of the same kind. Source: the queue line; scripts/markdown.py `mask`.
4. The comment state is `mask_inline`'s: a comment opens on `<!--` outside inline code and closes on `-->`, a marker inside a fenced block opens nothing, and a fence opens only on a line that does not start inside a comment, exactly as `mask` reads it today. The width check's output on every file in the tree stays empty, and `mask`'s output stays identical, byte for byte. Source: scripts/markdown.py:59-71, :89-121.
5. The rule that the width check skips commented and front matter blocks belongs to docs/01's `check_width.py` row, not docs/04: docs/04's rule is about what a reader sees, and a commented block is seen by none. So docs/04 stays as `docs04-width-rule` leaves it. Source: docs/04 **Width of a block**; docs/01:31.
6. No docs/03 term, no new queue line, no split. Source: docs/03; docs/05 §1.

**Behaviour.**

Each case is run by /apply through `check_width.check` on scratch text, or on a scratch file under `book/en/` removed afterwards; a "finding" is `<path>:<n>: width: 75 columns; a code block keeps to 74 (docs/04)` at the row's line, and the whole run exits 1 when anything is printed.

* A line `<!--`, then a three-backtick fence holding a 75-column row, its closing fence, then `-->`: nothing.
* The same fence after the line `-->` that closes the comment: one finding, at the row.
* A comment opened and closed on one line (`<!-- note -->`), then the fence: one finding.
* A line whose inline code holds `` `<!--` ``, then the fence: one finding (inline code opens no comment, as `mask` reads it).
* A fence whose own content holds `<!--`, closed, then a second fence with a 75-column row: one finding, at the second fence's row (a marker inside code opens nothing).
* A front matter between two `---` lines that holds a line of three backticks and a 75-column line, and nothing after it: nothing.
* Unchanged: a 90-column row in a `ts` block, nothing; a 75-column row in a bare block, one finding; a 75-column row in a three-backtick block inside a four-backtick `markdown` block, one finding at that row; a tab followed by 67 characters, one finding.
* On the tree: `python3 scripts/check_width.py` prints nothing and exits 0, before and after.
* `mask(text, keep_targets)`, for both values, gives the same lines before and after on every `.md` file of the repository (the editions, the READMEs, docs/, work/).
* Fails: a fence inside a comment or the front matter that is measured; any change in `mask`'s output; a width check that keeps its own comment rule beside the shared one.

**Contract.**

scripts/markdown.py gains one function, and `mask` uses it:

* `line_kinds(text)`: for each line of `text.split("\n")`, in order, yields a pair `(kind, info)`, `info` being the fence's info string for a fence or code line and the comment state for a text line (/apply may split it into two fields if the code reads better, and records it):
  * `"front"`: a line of the front matter, its opening and closing `---` included; the front matter opens only when the first line is `---`, and, unclosed, runs to the end of the text (as `mask` today);
  * `"fence"`: a line that opens a fenced block, by `FENCE_OPENING`, or closes the open one, by `closes`; `info` is the opening's info string (group 2), `""` on a closing line;
  * `"code"`: a line inside a fenced block; `info` is its opening's info string;
  * `"text"`: any other line; `info` is `True` when the line starts inside an HTML comment, else `False`.
  * The comment state is carried by calling `mask_inline` on each `"text"` line; a fence opens only on a line that does not start inside a comment.
* `mask(text, keep_targets)` keeps its signature and output: `"front"`, `"fence"` and `"code"` lines blanked, a `"text"` line given to `mask_inline` with its starting comment state and `keep_targets`.

scripts/check_width.py imports `line_kinds` instead of `FENCE_OPENING` and `closes`, and measures each `"code"` line whose `info`'s first word, lower-cased, is not in `UNMEASURED`. Its message, its limit, its tab size, `UNMEASURED`, the files it reads and its exit code do not change. Its docstring says it skips front matter and HTML comments, as `mask` does.

docs/01, two edits:

* line 31, the `check_width.py` row: "every fenced block but TypeScript, in both editions and both READMEs" becomes "every fenced block but TypeScript, outside front matter and HTML comments, in both editions and both READMEs"; the rest stays.
* line 39, the markdown.py row: the clause "FENCE_OPENING and closes: the fence rule, a run of three or more backticks or tildes after any indent closed by a line that starts with the same run, shared by mask and the width check" becomes "line_kinds: each line as front matter, a fence, code with its fence's info string, or text with whether it starts inside an HTML comment, read by FENCE_OPENING and closes, the fence rule, a run of three or more backticks or tildes after any indent closed by a line that starts with the same run, shared by mask and the width check"; the rest stays.

No new term; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* docs/04: the rule is a reader's, and no reader sees a commented block (decision 5).
* The fence rule itself, which `FENCE_OPENING` and `closes` keep as they are: `fence-commonmark`.
* The rest of docs/01's markdown.py row, its other helpers and users: `docs01-helpers`.
* The prose, link and parity checks and the book build: they call `mask`, whose output does not change.

**Order with the other slugs of this batch.** Second, after `docs04-width-rule`, which edits docs/04 alone and leaves `check_width.py` unchanged. `fence-commonmark`, third, changes `FENCE_OPENING` and `closes` inside the `line_kinds` this page introduces, and the fence-rule words of docs/01:39's clause; `docs01-helpers`, fourth, rewrites docs/01:31 and :39 whole, from the text this page and `fence-commonmark` leave.

**Done when.**

* [x] scripts/markdown.py has `line_kinds` as the Contract says and `mask` uses it; scripts/check_width.py uses `line_kinds` and holds no fence or comment rule of its own.
* [x] Each case of Behaviour run and its output recorded on this page; scratch files removed.
* [x] `mask` identical before and after on every `.md` file of the repository, with and without targets, so the prose, link and parity checks and the book build, which read through `mask`, read what they read before.
* [x] docs/01:31 and :39 changed as the Contract says.
* [x] `make verify` green, the width check included; no em dash.
* [x] No screenshot: no rendered change (docs/05 §5 Proof of a screen; `code-width` the precedent).
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its own hunk of docs/06 (docs/05 §6), other sessions' changes left unstaged; commit message in a `commit` block.

**Proof.** Each case of Behaviour ran on scratch text passed straight to `check_width.check` as `book/en/scratch.md`, with no file written; a finding below is `book/en/scratch.md:<n>: width: 75 columns; a code block keeps to 74 (docs/04)`:

* a fence inside `<!--` ... `-->`: nothing;
* the same fence after the line `-->`: one finding, line 4, the row;
* `<!-- note -->`, then the fence: one finding, line 3;
* inline code holding `` `<!--` ``, then the fence: one finding, line 3;
* a fence holding `<!--`, closed, then a second fence with the row: one finding, line 5, the second fence's row;
* a front matter holding a line of three backticks and a 75-column line: nothing;
* a 90-column row in a `ts` block: nothing; a 75-column row in a bare block: one finding, line 2; inside a four-backtick `markdown` block: one finding, line 3, the row; a tab and 67 characters: one finding, line 2.

The exit code ran on a scratch file, `book/en/zz-scratch.md`, a commented fence and then an uncommented one, each with a 75-column row: one finding, `book/en/zz-scratch.md:8`, the second fence's row, and exit 1; the file was removed. On the tree, `python3 scripts/check_width.py` printed nothing and exited 0, before and after.

`mask`: the old `scripts/markdown.py`, copied aside before the edit, and the new one ran on the same text of every `.md` file of the repository, tracked or untracked and not ignored (492 files: the editions, the READMEs, docs/, work/), with `keep_targets` True and False: 0 differences.

`make verify` green: build, parity, em dash, prose, width, links, disclosure.

**Divergences.** None from the Contract: `line_kinds` yields one pair `(kind, info)`, not two fields; `info` is `None` on a `"front"` line, which the Contract leaves open.

**Omissions.** None.

**Decisions taken in /apply.**

* `line_kinds` carries the comment state with `mask_inline(line, comment, True)`: whether a line ends inside a comment does not depend on `keep_targets`, which only chooses what is blanked, so `mask` calls `mask_inline` again with its own `keep_targets` for the text it keeps.
* The width check's docstring also says the unmeasured test reads the first word of the info string, whatever its case, as docs/04 says: `docs04-width-rule`'s review noted the docstring did not, and gave it to this page, which edits that docstring. The module docstring of markdown.py names the kind of each line among what it shares.

**Review.** Delivery review by a read-only Opus agent on the diffs of scripts/markdown.py, scripts/check_width.py and docs/01, this delivery's line of docs/06 and this page, against the page, docs/04 and AGENTS.md. No findings. It reran the `mask` comparison on the 492 files (0 differences) and the Behaviour cases, and found the shared reader also closes two gaps the old width check had: a comment opened mid-line before a fence, and a closed front matter holding three backticks, both now read as `mask` reads them. One optional note, that the `line_kinds` docstring did not say `info` is `None` on a front matter line, was taken: the docstring now says so. `make verify` green again after it.

```commit
fix(width-comment-fence): skip fences in comments and front matter

- markdown.py: line_kinds, the line reader mask and the width check share
- check_width.py measures only code lines line_kinds gives it
- docs/01: the width check and markdown.py rows name the shared reader

work/done/width-comment-fence.md
```
