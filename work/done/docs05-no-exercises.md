# docs05-no-exercises

**Objective.** A reader of docs/05 §3 finds a chapter page's Contract listing sections, terms, sources and cases, and no exercises, as ADR-0017 retired them. Finding D3 of `m14-review` (C8), re-checked.

**Behaviour.**

* The paragraph "For a chapter, the page reads this way" (docs/05:79 to 87, today) says **Contract** lists "the sections, the terms of docs/03 it introduces, the sources it cites and the cases it draws on", with no "the exercises". Held: the words are at docs/05:82 to 83; docs/04:133 ("There are no exercises (ADR-0017)"), docs/00:24, docs/03's `exercise` row (retired) and AGENTS.md's "Do not rebuild" all say the opposite.
* Nothing else of the paragraph changes: Objective, Behaviour and Done when read as today.
* Fails: a mention of exercises left in docs/05 as an instruction.

**Contract.** None. One clause of one sentence in `docs/05-Process.md`; the line wraps as the file already does.

**Out of scope.**

* docs/03's `exercise` row, docs/00:24, docs/04:133 and AGENTS.md: they already say exercises are retired; the row stays as the history the glossary keeps for retired terms.
* The `/propose` and `/apply` skills: no mention of exercises (grep of `.claude/` finds none).
* docs/06 lines and `work/done/` pages that name exercises: history.

**Done when.**

* [x] `grep -n -i "exercise" docs/05-Process.md` finds nothing.
* [x] `make verify` green.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**In flight.** No page in `work/` edits docs/05; `m15-review` and others only cite it. No overlap.

**Decisions in the review.** Choices made alone.

* The list is shortened ("the sources it cites and the cases it draws on") and not given a replacement item: ADR-0017 retired the exercises without adding anything to a page (docs/04:133).

**Divergences.** None. docs/05:79 to 86 read as the page said when /apply started, and only the Contract clause changed; the sentence was rewrapped from the clause to its end (docs/05:83 to 86) so no line is left short.

**Omissions.** None.

**Proof.** `grep -n -i "exercise" docs/05-Process.md` finds nothing; `make verify` green; `git diff --cached --name-only` holds `docs/05-Process.md`, `docs/06-Queue.md` and the page's move, and no path under `book/`. No chapter changed, so no `make book`.

**Decisions in /apply.** Choices made alone.

* The rewrap reaches the sentence's last three lines, past the clause, so the paragraph keeps the file's line width; Objective, Behaviour and Done when keep every word.

```commit
docs(docs05-no-exercises): docs/05's chapter Contract lists no exercises

- docs/05 §3: a chapter page's Contract lists sections, terms, sources and cases

work/done/docs05-no-exercises.md
```
