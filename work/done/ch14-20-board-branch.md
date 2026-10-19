# ch14-20-board-branch

**Objective.** After chapters 14 and 20 a reader can say what a board refreshed by a push shows when the work runs on a branch or a worktree per delivery: the mark at once, but in the queue of the branch whose command pushed it, since each push carries only that branch's queue, so the other branches' marks reach that board with their own push or at the merge; least change, both editions.

**Behaviour.**

* Reading chapter 14's "At the moment the work changes", the reader learns that a project's own one-way mirror, refreshed by the commands when a mark changes, shows the mark at once, and that each push carries the queue of the branch the command ran on, so with a branch or a worktree per delivery the board shows the queue of the branch that pushed last, not every branch's marks together.
* Reading chapter 20's "Boards", the reader learns the same in that section's terms: since the push runs inside the command that changed the mark, the board shows it at once, in the queue of the branch the delivery is on; another delivery's push shows its own branch's queue, and the marks meet at the merge.
* Every other sentence of both chapters stays, the Key points included.
* Fails if: a changed sentence still says or implies the board shows every branch's marks at once; it claims the push merges queues, diffs them or keeps a card from an earlier push; it says how a project should push (from which branch, on which event); it names Case A's branch strategy; it names a version, a date, a before and after or this repository's own Git choice; it narrates a run; a title changes; it holds an em dash.

**Contract.**

The same two passages in both editions, `book/en/` and `book/pt/`. Wording is /apply's within the sense below; the Portuguese reuses the phrasing the two chapters already use ("espelho ... numa só direção", "na hora", "a fila do próprio branch", "quando é feito o merge").

Chapter 14, `14-queue-states.md`, §"At the moment the work changes" / §"No momento em que o trabalho muda":

* Line 62 (pt 63): "The exception is a project's own one-way mirror, refreshed by the commands when a mark changes: it shows the mark at once on any branch." must now assert: the mirror, refreshed by the commands when a mark changes, shows the mark at once; each push carries the queue of the branch the command ran on, so on a branch the board shows that branch's queue, the one that pushed last, and the other branches' marks reach it with their own push or at the merge. "The exception" does not open the sentence any more: the mirror is no longer a full exception to line 61, and the opening word is what misleads. One sentence, or two if one cannot hold it plainly.
* Stays: lines 58 to 61 (pt 59 to 62), and the Key points bullet at line 183 (pt 184), which describes a board that reads the queue, not a pushed mirror, and holds as written.

Chapter 20, `20-team-tools.md`, §"Boards" / §"Quadros":

* Line 60 (pt 60): "Since the push runs inside the command that changed the mark, the board shows the mark at once, on any branch the delivery is on." keeps its first clause and replaces "on any branch the delivery is on" with: in the queue of the branch the delivery is on, since each push carries only that branch's queue, so another delivery's push shows its own branch's queue and the marks meet at the merge. No pointer to chapter 19 is added unless the sentence cannot read without it (docs/04, "Chapter pointers": a pointer back stays only where the sentence leans on a specific detail).
* Stays: line 59 (the slot sentence), lines 61 and 62, and the board Key point at line 87 (pt 87), which makes no branch claim.

Terms of docs/03 used: queue, mark, kanban board, slot, trunk, worktree. No new docs/03 row. No number, footnote, private case or lending library example added. Sources cited: none new.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* docs/05 §4 (lines 119 to 121) and docs/03's `kanban board` row (line 31): marked latent by m21-review's checker; they speak of a board that reads the queue, and any change is the driver's call.
* docs/06: the driver owns the queue line.
* How a project should push its queue (from the main branch only, on merge, per branch): no repository document gives a rule.
* The pointers to chapter 14 in chapter 18 (line 25) and chapter 19 (line 181), and chapter 14 line 164: still correct.
* Chapter 20's roles and pull-request text: done in `ch20-roles-and-points`.

**Decisions from the documents.**

* The finding and its lines: `work/done/m21-review.md`, O2, confirmed by the author; queue line in docs/06.
* A mark on a branch lives in that branch's queue until the merge: chapter 19 line 180, docs/05 §4.
* Chapter 20's board Key point is this delivery's to judge: `work/done/ch20-roles-and-points.md`, Out of scope.
* Pointer rule: docs/04, "Chapter pointers".
* No before/after, version or date; teach the kit as it is: AGENTS.md, `work/done/kit-2026-10-19.md`.

**Decisions taken alone.**

* The sense of the fix: the board shows the queue of the branch that pushed last; other branches' marks arrive with their own push or at the merge. Nothing more is claimed about how a mirror handles cards.
* Chapter 14's sentence drops "The exception": the mirror now only partly differs from line 61.
* Chapter 20's board Key point (line 87) and chapter 14's Key point (line 183, pt 184) stay: neither makes the false claim.
* The case stays general: no document says on which Git strategy Case A ran.
* No docs/03 row: no new term.

**Done when.**

* [x] Both editions changed in the two listed passages, every other sentence the same.
* [x] `git diff -U0` of each chapter shows hunks only at chapter 14 line 62 (pt 63) and chapter 20 line 60 (pt 60); the Key points sections unchanged.
* [x] `grep -rn "any branch\|qualquer branch" book/` finds nothing.
* [x] Both chapters open with their value, as before; no filler, nothing useful cut.
* [x] No new number, footnote or case; no em dash.
* [x] `make verify` green.
* [x] `make book` built, both PDF paths given: run once by the driver for the batch.

**Proof.**

* `git diff -U0 HEAD` of chapter 14, each edition: one hunk, line 62 (pt 63), which becomes two lines (the Contract allows two sentences); the Key points bullet, now line 184 (pt 185), unchanged in text.
* `git diff -U0 HEAD` of chapter 20, each edition: one hunk, line 60; lines 59, 61, 62 and the board Key point at line 87 unchanged.
* `grep -rn "any branch\|qualquer branch" book/` finds nothing.
* No em dash, number, footnote, case, version, date, push rule or Case A branch strategy added.
* `make verify` green after the review's fixes. `make book` is run once by the driver for the batch.
* Staging and the docs/06 hunk are the driver's in this batch.

**Divergences.** Chapter 14's sentence became two, as the Contract allows: one sentence held the mirror, the refresh and the board only with a colon and about sixty words.

**Delivery review.** A read-only Opus agent read this delivery's hunks against this page, docs/04 and chapter 19 line 181: no blocking finding. Three style notes, all fixed: chapter 14's long sentence split at the colon; chapter 14 says "refresh" (pt "atualização") instead of "push" (pt "envio"), since the chapter never says what the push is and the reader could take it for a `git push`, while chapter 20 names the command that pushes the queue and keeps "push"; chapter 20's "another delivery's push shows" became "puts its own branch's queue on the board" (pt "põe no quadro"), so the board is what shows.

**Decisions taken alone in /apply.**

* Chapter 14 uses "refresh" for what the commands do to the mirror, the word its sentence already uses; chapter 20 keeps "push", its own word.

```commit
docs(ch14-20-board-branch): a pushed board shows its branch's queue

- ch14: the mirror shows the queue of the branch that refreshed it last
- ch20 boards: each push carries its branch's queue; marks meet at merge

work/done/ch14-20-board-branch.md
```
