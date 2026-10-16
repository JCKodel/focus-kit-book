# docs03-current-rows

**Objective.** A reader of docs/03 finds the waiting mark and tag rows saying what docs/05 says today, and every "docs/04 §..." pointer in it naming a section or a rule that exists. Findings D1, D6 and the docs/03 part of D7 of `m14-review` (C8); each re-checked against the files.

**Behaviour.**

* Row `waiting mark` (docs/03:103, today): the clause "`resume: apply` back to `[>]` only when its page is still complete" is gone. docs/05 §4 returns `resume: apply` to `[>]` with no condition (a draft is saved with `resume: propose` until §3 is complete, so a complete page is how a line gets that suffix), and returns a line whose scope became undecided to `[ ]`. The row says the same: `resume: propose` back to `[ ]`, `resume: apply` back to `[>]`, and `[ ]` when scope became undecided. Held: docs/05:123 to 129 against docs/03:103.
* Row `tag` (docs/03:76): "the book's chapter tags are tags" is gone. The row `chapter tag` (retired, ADR-0017) says no chapter cites one, so the `tag` row must not call them live. The row ends with what a tag does in this repository today: the book's releases are tags `vX.Y.Z` (docs/manuals/release-the-book.md, docs/01 job `release`). Held.
* Row `running example` (docs/03:96): "(docs/04 §Evidence)" reads "(docs/04 §Writing the book, Evidence)", the form docs/04:6 already uses for the same rule. `Evidence` is a bold rule of §Writing the book, not a heading; one explicit form removes the doubt. Held in part: it resolves by the repository's habit of citing a rule by its bold name, so the change is for precision.
* Row `source note` (docs/03:118): "(docs/04 §Source notes)" reads "(docs/04 §Chapter shape, Source notes)". No heading or rule is named "Source notes"; the rule is the bullet "Source notes:" under §Chapter shape (docs/04:136). Held.
* Every other "docs/0N §..." in docs/03 (lines 33, 40, 109, 113, 119) already names a heading that exists; checked, unchanged.
* Fails: a `tag` row that mentions chapter tags; a `waiting mark` row that keeps the condition; a pointer to a name that is neither a heading nor a bold rule of the file it cites.

**Contract.** None. Four rows of one file, edited in place; no new term, so docs/03 gains no row. The Portuguese column of each row is unchanged.

**Out of scope.**

* chapter 16's two sentences on `resume: apply` (finding L1): the line `ch16-resume-apply` owns them.
* docs/03:30 (`mark` row, "defined"): names the states in short and says nothing false.
* The "docs/04 §..." pointers in `work/` pages and ADRs: history and pages in flight, not this document.
* docs/04's own pointers (`docs04-gain-number`) and docs/05 (`docs05-no-exercises`).

**Done when.**

* [ ] The four rows read as Behaviour says, in `docs/03-Domain.md` only.
* [ ] `grep -n "only when its page is still complete\|chapter tags are tags" docs/03-Domain.md` finds nothing; `grep -n "§Evidence\|§Source notes" docs/03-Domain.md` finds only the two explicit forms.
* [ ] Every "docs/04 §X" and "docs/05 §N" of docs/03 resolves to a heading, or to a rule named in the section it cites.
* [ ] `make verify` green, disclosure scan included.
* [ ] Page in `work/done/`, line `[x]`, staged by its paths and its hunks of docs/03 and docs/06, commit message in a `commit` block.

**In flight.** Pages in `work/` that touch docs/03 are `focus-and-slices` (FOCUS, orchestrator, use case, repository and view rows), `simplicity-and-results` and `renumber-chapters` (rows that name a chapter) and `prologue-and-why`. None edits rows 76, 96, 103 or 118, and those four name no chapter. Two of them (rows 96 and 118) sit near rows others edit, so git can join the hunks: /apply stages by hunk and does not take another delivery's. `docs04-gain-number` edits docs/04, not this file.

**Decisions in the review.** Choices made alone.

* The `tag` row ends on the release tag `vX.Y.Z` rather than only losing the clause, because a glossary row on a git term should say what it is used for here (docs/manuals/release-the-book.md).
* The pointer form is "docs/04 §<heading>, <rule>", copying docs/04:6; the alternative, renaming docs/04's rules into headings, changes how every page cites them and is not taken.
* `waiting mark` follows docs/05 §4 and drops the condition, not the other way: docs/05 is the owner of the marks (docs/03 row `waiting mark` cites it; docs/05 §4 says "These are the marks of focus-kit 2026.10.05").
