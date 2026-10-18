# fence-commonmark

**Objective.** Every check that reads a fenced block (the prose, link, parity and width checks and the book build) opens and closes it where CommonMark does for a fence at the margin, and docs/01 says so. Found by `m16-review` (work/done/m16-review.md, build-4 latent: "`scripts/markdown.py:35-36`, `closes` takes a closing fence with text after the run; none exists"; build-5 latent: "`scripts/markdown.py:11` opens a fence on a backtick info string with a backtick, or on four spaces of indent; none exists").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The reference is CommonMark's spec, §4.5 Fenced code blocks, as the queue line says, and not what one renderer accepts beyond it: the site's Python-Markdown and the book's pandoc each read fences their own way, and the checks need one rule. Source: the queue line; docs/01 Stack (MkDocs Material and pandoc).
2. The rule is CommonMark's for a fence at the margin, its indent counted from the start of the line. CommonMark counts a fence's indent from its container's content (a list item, a blockquote); reading containers means a Markdown parser, which docs/01's "Python 3 for checks, nothing to install" and markdown.py's line-by-line reading do not have. No file a check reads has an indented fence: the only fences indented four spaces or more in the repository sit under list items of four pages in `work/done/` and in one recorded run, which no check reads (`check_prose.py` `language_of`: the editions and the READMEs; the link check adds `mkdocs.yml`). Source: docs/01 Stack and the markdown.py row; a scan of every tracked `.md` file when this page was written.
3. What changes, clause by clause of CommonMark §4.5:
   * an opening fence has at most three spaces of indent; a tab, which CommonMark reads as four columns, or four spaces make it no fence;
   * a backtick fence whose info string holds a backtick is no fence; a tilde fence's info string may hold anything;
   * a closing fence has at most three spaces of indent, is a run of the opening's character at least as long as the opening run, and has nothing after it but spaces or tabs;
   * an unclosed fence runs to the end of the text, as today.
   Source: CommonMark spec 0.31.2, §4.5.
4. The names and their shape stay: `FENCE_OPENING`, group 1 the run and group 2 the info string, and `closes(line, run)`, so `line_kinds` (from `width-comment-fence`) and every reader keep working without a change of their own. Source: scripts/markdown.py; work/width-comment-fence.md Contract.
5. Simulated on the 55 files the checks read (both editions, both READMEs, `mkdocs.yml`), the new rule gives `mask` the same output as the old one, with and without targets: nothing in the tree is read differently. Source: a run of `mask` under both rules when this page was written.
6. No docs/03 term, no new queue line, no split. Source: docs/03; docs/05 §1.

**Behaviour.**

Each case is run by /apply through `mask` and `check_width.check` on scratch text, or on a scratch file under `book/en/` removed afterwards; "measured" means a 75-column row gives the finding `<path>:<n>: width: 75 columns; a code block keeps to 74 (docs/04)` and `mask` blanks it, and "prose" means no finding and `mask` keeps its words.

* A three-backtick block holding a line ```` ```text ````, then a 75-column row, then a line of three backticks: the ```` ```text ```` line does not close it; the row is measured (build-4).
* A closing line of three backticks followed by two spaces and a tab closes; a 75-column line after it is prose.
* A closing line of four backticks closes a three-backtick fence; a closing line of two backticks, or of three tildes, does not.
* A closing line indented three spaces closes; one indented four spaces does not.
* An opening fence indented three spaces opens; one indented four spaces, or by a tab, does not, and the 75-column row after it is prose (build-5).
* An opening line ```` ``` a`b ```` is no fence and its next 75-column row is prose; an opening line ```` ~~~ a`b ```` opens a fence and its row is measured (build-5).
* An unclosed fence: its last 75-column row is measured.
* Unchanged: a four-backtick `markdown` block whose inner three-backtick block holds a 75-column row: one finding, at that row; a `ts` block's 90-column row: nothing.
* On the tree: `mask`, for both values of `keep_targets`, gives the same lines before and after on every file the checks read; `python3 scripts/check_width.py` prints nothing.
* Fails: a closer with text after its run that closes; a four-space or tab-indented fence that opens; a backtick fence whose info string holds a backtick that opens.

**Contract.**

scripts/markdown.py:

* `FENCE_OPENING` matches at the start of a line: at most three spaces, then either a run of three or more backticks followed by an info string with no backtick, or a run of three or more tildes followed by any info string. Group 1 is the run, group 2 the info string, as today. Its comment says so and names CommonMark §4.5.
* `closes(line, run)` is true when `line` is at most three spaces, then a run of `run`'s character at least `len(run)` long, then only spaces or tabs to its end. Its docstring says so.
* No other function changes; `line_kinds` and `mask` call these two as before.

docs/01:39, the markdown.py row: within the `line_kinds` clause that `width-comment-fence` writes, "the fence rule, a run of three or more backticks or tildes after any indent closed by a line that starts with the same run" becomes "the fence rule as CommonMark reads it at the margin, a run of three or more backticks or tildes after at most three spaces, a backtick run's info string holding no backtick, closed by a line of at most three spaces and a run of the same character at least as long, with nothing after it but spaces or tabs"; the rest stays.

No new term; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* A fence inside a list item or a blockquote, its indent counted from the container: no file a check reads has one, and reading containers needs a parser (decision 2).
* CommonMark's removal of the opening fence's indent from the content lines: the width check measures the raw line, and no measured block is indented.
* What pandoc or Python-Markdown accept beyond CommonMark (decision 1).
* The rest of docs/01's markdown.py row: `docs01-helpers`.

**Order with the other slugs of this batch.** Third, after `width-comment-fence`, which introduces `line_kinds` around `FENCE_OPENING` and `closes` and writes the docs/01:39 clause whose fence-rule words this page replaces. `docs01-helpers`, fourth, rewrites docs/01:39 whole, keeping this page's fence-rule words.

**Done when.**

* [x] `FENCE_OPENING` and `closes` follow the Contract; no other code in scripts/ changes.
* [x] Each case of Behaviour run and its output recorded on this page; scratch files removed.
* [x] `mask` identical before and after on every file the checks read, with and without targets.
* [x] docs/01:39 changed as the Contract says.
* [x] `make verify` green; no em dash.
* [x] No screenshot: no rendered change (docs/05 §5 Proof of a screen; `code-width` the precedent).
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its own hunk of docs/06 (docs/05 §6), other sessions' changes left unstaged; commit message in a `commit` block.

**Proof.** Each case of Behaviour ran on scratch text passed straight to `check_width.check` as `book/en/scratch.md` and to `mask`, with no file written; a finding below is `book/en/scratch.md:<n>: width: 75 columns; a code block keeps to 74 (docs/04)`, and in every case with a finding `mask` blanked the row, in every case with none it kept the row's words (the `ts` row aside, which is code and blanked):

* a three-backtick block holding ```` ```text ````, then the row, then three backticks: one finding, line 3 (build-4);
* a closer of three backticks, two spaces and a tab, then the row: nothing;
* a closer of four backticks, then the row: nothing; a line of two backticks, then the row: one finding, line 3; a line of three tildes, then the row: one finding, line 3;
* a closer indented three spaces, then the row: nothing; one indented four spaces, then the row: one finding, line 3;
* an opening indented three spaces: one finding, line 2; indented four spaces: nothing; indented by a tab: nothing (build-5);
* ```` ``` a`b ````, then the row: nothing; ```` ~~~ a`b ````, then the row: one finding, line 2 (build-5);
* an unclosed fence, its last line the row: one finding, line 3;
* a four-backtick `markdown` block whose inner three-backtick block holds the row: one finding, line 3; a 90-column row in a `ts` block: nothing.

The fails cases ran through `mask` under the old `scripts/markdown.py`, copied aside before the edit, and the new one: the old rule kept the row after a closer with text after its run and in build-4's block, and blanked it after a four-space or tab-indented opening and after ```` ``` a`b ````; the new rule does the opposite in each.

The exit code ran on a scratch file, `book/en/zz-scratch.md`, build-4's block: one finding, `book/en/zz-scratch.md:3`, and exit 1; the file was removed, and `python3 scripts/check_width.py` printed nothing and exited 0.

`mask` and `line_kinds`, old and new, on the 55 files the checks read (both editions, both READMEs, `mkdocs.yml`), with `keep_targets` True and False: 0 differences. On every `.md` file of the repository, tracked or untracked and not ignored (493), 6 files are read differently, none of them read by a check: four pages of `work/done/` (`ch08-09-review-slot`, `ch15-brief-printed`, `ch18-19-only-apply`, `ch18-log-evidence`), one recorded run (`ask-for-more-experiment-run/audience/run-2/questions.md`) and one page waiting in `work/` (`ch08-update-2026-10-18`, written after this page), each a fence indented under a list item (decision 2).

`make verify` green: build, parity, em dash, prose, width, links, disclosure.

**Divergences.** None from the Contract.

**Omissions.** None.

**Decisions taken in /apply.**

* The backtick rule lives in `FENCE_OPENING` itself, a lookahead after the backtick run, so the pattern keeps two groups and `line_kinds` reads it unchanged; the lookahead is checked at every length the run backtracks to, so four backticks before `` a`b `` open no fence either.
* `closes` builds its pattern from the run's character and length on each call: the rule depends on the opening, and no reader calls it more than once per line.

**Review.** Delivery review by a read-only Opus agent on the diffs of scripts/markdown.py and docs/01, this delivery's line of docs/06 and this page, against the page, docs/04 and AGENTS.md. No findings. It reran every Behaviour case through `check_width.check` and `mask` under the old and new module and the comparison on the 55 files (0 differences) and on every `.md` file (the same 6 files, none read by a check). It noted the repository then held 492 `.md` files, not 493, as other sessions' untracked pages changed meanwhile; the count above is the one this page's run saw. `make verify` green again after it.

```commit
fix(fence-commonmark): read fences as CommonMark does at the margin

- markdown.py: a fence opens after at most three spaces, no backtick in a backtick info string
- markdown.py: a closer is a run at least as long, then only spaces or tabs
- docs/01: the markdown.py row states the CommonMark fence rule

work/done/fence-commonmark.md
```
