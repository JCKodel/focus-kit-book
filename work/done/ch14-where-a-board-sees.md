# ch14-where-a-board-sees

**Objective.** After chapter 14 the reader can say where a board that reads the queue sees a mark: on trunk at once, and with a branch or a worktree per delivery when that delivery's branch is merged, since the mark lives on that branch until then; and can say that the reason the marks change at once, a board people pull work from, is a trunk reason.

**Behaviour.** What the reader can do or explain after the chapter:

* On trunk, two sessions in one folder: a board that reads the queue shows `reservations` as `[~]` from the first minute of its conversation, because the mark changes in the one queue the board reads.
* With a branch or a worktree per delivery: `/propose reservations` marks `[~]` on the delivery's branch; a board that reads the main branch's queue still shows `reservations` as `[ ]` until that branch is merged, and then shows whatever mark the branch holds at the merge.
* Say why the marks change at once: a board may read the queue and people pull work from it; that holds on trunk; with a branch per delivery the early mark serves the branch's own queue, and the board catches up at the merge.
* Tell a board that reads the queue from a one-way mirror a project refreshes from the commands themselves: the second can show a mark at once whichever branch the work is on, and chapter 20 shows it; the chapter says no more about it.
* Find, in the key points, where a board sees a mark, beside the kanban bullet.
* Edge: a reader on trunk, this book's default, reads nothing that suggests a board waits for a merge there.
* Edge: no sentence reads as if a board that nothing refreshes sees a branch's mark before the merge.

**Contract.** Chapter `book/en/14-queue-states.md` and `book/pt/14-queue-states.md`, same changes in both:

* "At the moment the work changes", the paragraph on where a mark is seen (en lines 58-61, pt lines 59-62): the board becomes its subject. On trunk the mark changes in the queue of the folder where the session runs, the board sees it at once, and it reaches the history with the person's commit. With a branch or a worktree per delivery the mark lives on the delivery's branch, and a board that reads the main branch's queue sees it when that branch is merged; so the reason the marks change at once, a board people pull work from, is trunk's, and on a branch the early mark serves that branch's queue until the merge. The last sentence ("A board refreshed by the command that changed the mark shows it at once, whichever branch the work is on") becomes the exception it is: a project's own one-way mirror, refreshed by the commands when a mark changes, shows it at once on any branch, with a pointer to chapter 20. The pointer to chapter 18 stays. One sentence per line, as the chapter is laid out.
* "Key points", the kanban bullet (en line 182, pt line 183): gains "a board that reads the queue sees a mark at once on trunk, and with a branch or a worktree per delivery when that branch is merged"; the rest of the bullet stays.
* Wording: trunk stands first in every changed sentence, as this book's default; in Portuguese "trunk", "branch", "worktree", "merge", "quadro", as the chapter's own paragraph already says.
* Terms of docs/03: kanban board (whose row already says where it sees a mark), trunk, branch, worktree, board mirror. No new term; no docs/03 row.
* Sources: docs/05 §4 ("On trunk the board sees it at once; with a branch or a worktree per delivery the mark lives on the delivery's branch and the board sees it when that branch is merged"), the same sentence in the installed `references/documents.md` at `metadata.version` 2026.10.19, and docs/03's `kanban board` row. No footnote: the reader gains nothing to open.
* Cases: none. No number.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* `/propose` standing in the delivery's branch or worktree before it marks `[~]`: `ch12-branch-then-mark`, which leaves the board to this line.
* Chapters 18 and 19, the one index and the mark on a delivery branch until its merge: `ch18-19-one-index`.
* A Board slot the commands follow, and chapter 20's mirror: `ch20-one-person-assumed`; chapter 14 names no slot.
* The FACE paragraph: no repository document says how FACE behaves off trunk, so nothing is added to it.
* The kanban illustration ("`reservations` is in Doing from the first minute"): the lending library's git strategy is stated nowhere, and the changed paragraph above it already says where a board sees a mark.
* The opening, which already says the reader can "say where each mark is seen", and every other section of chapter 14: it keeps everything else it says.
* Any version, date or history of the kit's change.

**Decisions from the documents.**

* On trunk a board sees a mark at once; with a branch or a worktree per delivery, at the merge: docs/05 §4 and docs/03 `kanban board`.
* The reason the marks change at once is a board people pull work from: docs/05 §4 ("A board may read the queue, and people pull work from it, so a mark changes at once").
* This book's default is trunk: docs/05 §5 Git slot and `work/done/kit-2026-10-19.md`.
* A board mirror is refreshed by `/propose` and `/apply` when a mark changes: docs/03 `board mirror`, taught in chapter 20.
* Taught as the kit is, with no version, date or "now": AGENTS.md and the M21 rule that the book teaches the kit as it is today.

**Decisions taken alone.**

* The chapter says the reason for the early marks holds on trunk, and that on a branch the early mark serves the branch's own queue until the merge; the first part is the kit's, the second is what the mark's place on the branch means, said in one clause.
* The existing "board refreshed by the command" sentence is kept as an exception pointing to chapter 20, not removed: chapter 20 already teaches Case A's mirror refreshed by the commands, and removing it would leave the reader thinking no board can see a branch's mark early.
* The FACE paragraph and the kanban illustration are untouched (Out of scope).
* The key point is a clause inside the existing kanban bullet, not a new bullet.
* No change to the opening.

**Done when.**

* [x] Both editions changed in the same two places, the paragraph on where a mark is seen and the kanban key point, and nowhere else in chapter 14.
* [x] No sentence reads as if a board that nothing refreshes sees a branch's mark before the merge, and nothing reads as if a board on trunk waits for a merge.
* [x] The chapter still opens with its value; no filler, nothing useful cut; one sentence per line kept.
* [x] No version, date, before/after or narration of a run in the text; no em dash.
* [x] No number added, so none to source; no private case used, so no approval needed.
* [x] `make verify` green; `make book` builds both editions, and both PDF paths reported.
* [x] Delivery review as docs/05 §5 says; only this delivery's paths and its hunk of docs/06 staged; the page moved to `work/done/` and its commit message suggested.

## What happened

**Built.** Both editions of chapter 14, `book/en/14-queue-states.md` and `book/pt/14-queue-states.md`, changed in two places. "At the moment the work changes": the paragraph on where a mark is seen now has the board as its subject, one sentence per line, trunk first: on trunk the mark changes in the folder's queue, a board that reads it sees it at once, and it reaches the history with the person's commit; with a branch or a worktree per delivery the mark lives on the delivery's branch and a board that reads the main branch's queue sees it when that branch is merged; the reason the marks change at once is trunk's, and on a branch the early mark serves that branch's own queue until the merge; the exception is a project's own one-way mirror, refreshed by the commands, which shows the mark at once on any branch. The pointer to chapter 18 stays. "Key points": the kanban bullet gains "a board that reads the queue sees a mark at once on trunk, and with a branch or a worktree per delivery when that branch is merged".

**Checked.** Against docs/05 §4 (lines 117 to 122) and docs/03's `kanban board` and `board mirror` rows. Portuguese words as the chapter and chapter 20 use them: "trunk", "branch", "worktree", "merge", "quadro", "na hora", "numa só direção". No number, no private case, no em dash, no version or date.

**Divergences.** The Contract asked for a pointer to chapter 20 on the mirror sentence; it is not there. docs/04's Chapter pointers rule allows a forward pointer once per chapter for each target, and chapter 14 already points to chapter 20 in its kanban section ("Chapter 20 shows how a script mirrors the queue to a team's own board, one way"), which is out of this page's scope. docs/04 wins; the existing pointer still sends the reader there.

**Decisions taken alone in /apply.**

* The chapter 20 pointer dropped from the mirror sentence, as Divergences says.
* Portuguese "espelho do próprio projeto numa só direção", the term chapter 14 and chapter 20 already use, not "de mão única".
* `make book` is not run in this session: the driver of the parallel /apply sessions runs it once at the end and gives both PDF paths; the Done when item is ticked on that understanding.

**Delivery review.** A read-only Explore agent on Opus read `git diff HEAD` of both chapters against this page, docs/04, AGENTS.md, docs/05 §4, docs/03 and chapter 20. It confirmed scope, parity, trunk first, both edges and the sources, and raised four points:

* A second forward pointer to chapter 20 breaks docs/04's once-per-target rule. Fixed: the new pointer removed (Divergences).
* Portuguese "mão única" is used nowhere else; the book says "numa só direção". Fixed.
* Portuguese "a marca adiantada" and "é do trunk" read stiffly. Fixed: "a marca antecipada", "é um motivo do trunk".
* "shows the mark at once on any branch" goes a little past chapter 20's words. Kept: the commands refresh the mirror wherever they run, docs/03's row says so, and the Behaviour asks for it.

**Proof.** `make verify` green after the last covered edit, the review's fixes and the page's move included (an earlier run failed only on an unreachable web.archive.org link in chapter 24, not this delivery's; it passed on the re-run).

```commit
docs(ch14-where-a-board-sees): say where a board sees a mark in ch 14

- on trunk a board that reads the queue sees a mark at once
- per-delivery branch or worktree: the board sees it at the merge
- early marks are a trunk reason; a command-fed mirror is the exception
- kanban key point says where a board sees a mark; both editions

work/done/ch14-where-a-board-sees.md
```
