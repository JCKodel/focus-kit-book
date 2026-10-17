# docs06-legend

**Objective.** A reader of the queue's legend finds `[>]` defined as docs/05 §4 defines it: completely defined and ready for /apply. Finding D5 of `m14-review` (C8), re-checked.

**Behaviour.**

* docs/06:3 reads "`[>]` completely defined, `work/<slug>.md` ready for /apply" where it read "`[>]` defined, `work/<slug>.md` exists". Held: docs/05:106 gives `[>]` as "completely defined, page ready for /apply, set by /propose when §3 is complete", and a draft page can exist under `[ ]`, `[~]` or `[?]` with `resume: propose` (docs/05:34, 72, 123), so "exists" is true of lines that are not `[>]`.
* The other five marks and the `[?]` suffix text of the legend are unchanged.
* The legend stays one line, as the queue's file keeps it.
* Fails: a legend that lets "page exists" stand for "defined".

**Contract.** None. One clause of line 3 of `docs/06-Queue.md`; no mark, slug or suffix on any queue line changes.

**Out of scope.**

* docs/03:30 (`mark` row), which names the six states in short ("defined"): it makes no claim about the page.
* The legend's other marks: `[ ]` "not yet defined" and `[~]` "being defined" already agree with docs/05 §4.
* Any queue line: marks change only as docs/05 §4 says; this page does not touch them.

**Done when.**

* [x] `grep -n "defined, \`work/<slug>.md\` exists" docs/06-Queue.md` finds nothing; line 3 holds the new clause.
* [x] `make verify` green.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and only the legend's hunk of docs/06 (the line's own mark is another hunk), commit message in a `commit` block.

**In flight.** Every delivery edits docs/06, but only its own line's mark; no page in `work/` edits the legend. The legend is line 3, far from any queue line, so the hunks do not join; /apply stages this hunk alone (docs/05 §4, §6).

**Decisions in the review.** Choices made alone.

* "ready for /apply" is docs/05's own wording (docs/05:106), kept word for word so the two places cannot drift.

**Divergences.** None. docs/06:3 read as the page said when /apply started; only the `[>]` clause changed, and the legend stays one line.

**Omissions.** None.

**Proof.** `grep -n "defined, \`work/<slug>.md\` exists" docs/06-Queue.md` finds nothing; line 3 reads "`[>]` completely defined, `work/<slug>.md` ready for /apply". `make verify` green. `git diff --cached --name-only` holds `docs/06-Queue.md` and the page's move, and no path under `book/`. No chapter changed, so no `make book`.

**Decisions in /apply.** Choices made alone.

* docs/06 is staged whole: the tree was clean at HEAD, so its two hunks, the legend and this line's mark, are both this delivery's.

```commit
docs(docs06-legend): the queue's legend defines `[>]` as docs/05 §4 does

- docs/06 legend: `[>]` is completely defined, page ready for /apply

work/done/docs06-legend.md
```
