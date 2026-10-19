# ch14-20-read-branches

**Objective.** After chapters 14 and 20 the reader can say how the queue is read with a branch or a worktree per delivery: the main branch shows each line as it was until the merge, so a board, or a session picking free lines or resolving an `after`, takes each slug's line from its worktree or its branch, local or remote, adds the lines only a branch has, and reconciles them by slug, each line at its latest state, never one branch's whole file.

**Behaviour.** What the reader can do or explain after the chapters:

* On trunk, nothing changes: a board that reads the folder's queue shows `reservations` as `[~]` from the first minute of its conversation, and a session reads every line from the one docs/06.
* With a branch or a worktree per delivery, `/propose reservations` marks `[~]` on the delivery's branch; the main branch's docs/06 still shows `reservations` as `[ ]`, and a board that reads each slug's line from its worktree or its branch shows `[~]`.
* Say why the main branch's copy is not enough: `[~]`, `[>]`, `[*]` and `[?]` are set on the delivery's branch and reach the main branch only with the merge, so read there alone, held and waiting work looks not started.
* A session asked for the next delivery, with `lend-book` being built on its own branch: read from the main branch alone, `lend-book` would read `[ ]`, free and held by no one, and the answer would name it; read from each slug's branch, it is `[*]`, held, and the answer is `search-catalog`, as the chapter's example already says.
* A session resolving `return-book`'s `· after lend-book` reads `lend-book`'s mark from `lend-book`'s branch, not from the main branch's copy.
* Edge: a line only a branch has, such as a fix line `/apply` added on its delivery's branch, appears in the queue read this way, matched by its slug; it is not missing because the main branch lacks it.
* Edge: where a worktree's file and an older copy disagree on a slug, the line at its latest state wins; one branch's whole file never replaces the others, and a done line is never put back from a stale copy.
* Edge: a worktree's file shows a mark the moment it changes; a branch shows what was committed on it, and a remote branch what was pushed. No sentence promises a reader on another machine a mark nobody committed and pushed.
* A project's one-way mirror, refreshed by the commands when a mark changes, pushes the queue read the same way, each slug's line from its own branch, so a refresh from one delivery's branch carries every other delivery's latest mark too, instead of putting its branch's copy on the board with the others' lines as they were.
* Find it in the key points: chapter 14's kanban bullet and chapter 20's board bullet.

**Contract.** Four files, `book/en/14-queue-states.md`, `book/pt/14-queue-states.md`, `book/en/20-team-tools.md`, `book/pt/20-team-tools.md`, same changes in both editions, one sentence per line as the chapters are laid out:

* Chapter 14, "At the moment the work changes", the paragraph on where a mark is seen (en lines 58-63, pt lines 59-64). Kept: the first sentence with its pointer to chapter 18, and the trunk sentence. Replaced, not joined:
  * "a board that reads the main branch's queue sees it when that branch is merged" becomes: with a branch or a worktree per delivery the mark lives on the delivery's branch, and the main branch shows the line as it was until the merge; so whoever reads the queue there, a board or a session picking free lines or resolving an `after`, takes each slug's line from its worktree, or from its branch, local or remote, adds the lines only a branch has, and reconciles them by slug, each line at its latest state, never one branch's whole file.
  * "So the reason the marks change at once ... is trunk's; on a branch, the early mark serves that branch's own queue until the merge" becomes the reason restated for both: the marks change at once for a board people pull work from, on trunk in the one queue, and with a branch per delivery for whoever reads each slug's line on its branch. One clause says where the mark is visible: a worktree's file at once, a branch once committed on it, a remote branch once pushed.
  * The two mirror sentences of `ch14-20-board-branch` ("each refresh carries the queue of the branch the command ran on"; "the board shows the queue of the branch that refreshed it last") become one: a project's own one-way mirror, refreshed by the commands when a mark changes, shows the mark at once, and with a branch per delivery it pushes the queue read the same way, so each refresh carries every delivery's latest mark, not its own branch's copy.
* Chapter 14, "The next line, and which run together" (en lines 65-71, pt lines 66-72): after the sentence on the next delivery ("a new session's next delivery is `search-catalog`"), one or two sentences: with a branch or a worktree per delivery, the session judges free lines and `after` from each slug's line read as the section above says; from the main branch's copy alone `lend-book` would read `[ ]`, free and held by no one, and the answer would name a delivery another session is building. Portuguese slugs as the chapter has them: `emprestar-livro`, `buscar-catalogo`, `devolver-livro`.
* Chapter 14, "Key points", the kanban bullet (en line 184, pt line 185): "and with a branch or a worktree per delivery when that branch is merged" becomes "and with a branch or a worktree per delivery from each slug's own worktree or branch, since the main branch shows the line as it was until the merge", docs/03's `kanban board` wording; the free-line bullet (en 181, pt 182) gains nothing, the kanban bullet carries the reading for both.
* Chapter 20, "Boards", the push sentence (en and pt line 60): "in the queue of the branch the delivery is on: each push carries only that branch's queue, so another delivery's push puts its own branch's queue on the board, and the marks meet at the merge" becomes: the board shows the mark at once; with a branch per delivery the command that pushes reads each slug's line from its own branch, so one delivery's push carries the other deliveries' latest marks too. No "as chapter 14 says": the next sentence already links chapter 14. Said of a project's slot in general, never of Case A, whose git strategy the chapter does not state.
* Chapter 20, step 4 of the pull request list (en and pt line 25): "a `[~]` or `[*]` set on a branch shows there only (chapter 14)" becomes "a `[~]` or `[*]` set on a branch is on that branch only, where a board or a session reads it (chapter 14)"; "shows there only" would read as "is seen only there", which chapter 14 now denies. The existing plain pointer stays; no new one.
* Chapter 20, "Key points", the board bullet (en and pt line 87): gains "and, with a branch per delivery, read from each slug's own branch"; the rest stays.
* Portuguese: "trunk", "branch", "worktree", "merge", "slug", "quadro", "na hora", "espelho ... numa só direção", "linha livre", as chapters 14, 19 and 20 already write them; "com cada linha no seu estado mais recente", "nunca o arquivo inteiro de um branch".
* Terms of docs/03: kanban board (whose row already carries this reading), board mirror, free line, trunk, branch, worktree. No new term in the chapters.
* Sources: docs/05 §4 ("With a branch or a worktree per delivery the mark lives on the delivery's branch and the main branch shows the line as it was until the merge, so whoever reads the queue there, a board or a session picking free lines or resolving an `after`, takes each slug's line from its worktree's file, or from its branch, local or remote, and the lines only a branch has, reconciled by slug as below"); the installed kit template's §4 at 2026.10.19.1 (`references/documents.md`: "reconcile docs/06 by slug, keeping every line at its latest state, never one side's whole file"); docs/03 `kanban board`. No footnote: the reader gains nothing to open.
* Cases: none. No number.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 12, what `/propose` does when it starts its worktree from the main branch's `HEAD`: `ch12-free-lines-branches`. Chapter 14 teaches where a line is read; chapter 12 teaches the command.
* Chapter 8, the update example: `ch08-update-2026-10-19-1`.
* The project's own rule that a dependency stays blocked until its completed changes reach the branch that needs it: docs/05 §4 carries it, the kit's template does not, so the book does not teach it as the kit's.
* Chapters 18 and 19: their sentences ("`main`'s queue shows the line as it was until the merge", "each worktree's queue shows its own branch's state", "keep both marks") stay true, and their pointers to chapter 14 land on the changed paragraph.
* Chapter 17's manager session, which answers "where are we?" from docs/06 on the lending library, whose git strategy no chapter states: true on trunk, reported to the driver.
* Chapter 7's lending library Board slot (`npm run board` pushes docs/06): true on trunk; untouched.
* The kanban illustration, the FACE paragraph, the opening and every other section of chapters 14 and 20.
* Any version, date, count or history of the kit's change.

**Decisions from the documents.**

* The main branch shows each line as it was until the merge, and a board or a session picking free lines or resolving an `after` reads each slug's line from its worktree or branch, local or remote, with the lines only a branch has, reconciled by slug: docs/05 §4 and the kit's 2026.10.19.1 template.
* Reconciled means each line at its latest state, never one side's whole file: the kit template's worktree paragraph and docs/05 §4.
* The `kanban board` key point mirrors docs/03's row, already migrated by `kit-2026-10-19-1`.
* Taught as the kit is today, with no version, number or before and after: AGENTS.md, the task's rule for M22.
* The new text replaces the sentences of `ch14-20-board-branch` and `ch14-where-a-board-sees` it makes false, rather than sitting beside them: the line's own instruction and `work/done/ch14-20-board-branch.md`.

**Decisions taken alone.**

* "The reason the marks change at once is trunk's" is removed, not kept: once a board reads each slug's line from its branch, the early mark serves it on a branch too.
* The mirror is "whoever reads the queue": its push reads the queue the same way, so the two `ch14-20-board-branch` sentences about the last refresher's branch are replaced by one, in chapter 14 and in chapter 20.
* One clause says a worktree's file shows a mark at once, a branch once committed, a remote branch once pushed: without it, "at once" would promise a reader on another machine a mark that exists only in an uncommitted file.
* The next-line example uses `lend-book`, already `[*]` in the chapter's queue, so no new line or slug is added to the example.
* No new chapter pointer in either chapter: chapter 14 already points to 18, 19 and 20, chapter 20 to 14 (docs/04, Chapter pointers), and its changed sentences add no reference to chapter 14.
* Chapter 20's step 4 is reworded, not kept: its "shows there only" would contradict chapter 14's new paragraph for a reader.
* No change to either opening: chapter 14's "say where each mark is seen" and chapter 20's "keep issues and a board in step with the queue" already cover it.
* The gain sections stay as written: both are true, and truer, with the reading.

**Done when.**

* [ ] Both editions changed in the same places: chapter 14's paragraph on where a mark is seen, its next-line section, its kanban key point; chapter 20's step 4, push sentence and board key point; nowhere else.
* [ ] No sentence left that says a board on a branch sees a mark only at the merge, that the early mark's reason is trunk's alone, or that a board shows the queue of the branch that refreshed it last.
* [ ] Nothing reads as if a reader on trunk does anything new, or as if Case A's script read branches.
* [ ] Both chapters still open with their value; gain sections true; no filler, nothing useful cut; one sentence per line kept.
* [ ] No version, date, number, before and after or narration of a run; no em dash.
* [ ] No number added, so none to source; no private case newly used, so no approval needed.
* [ ] `make verify` green; `make book` builds both editions, and both PDF paths reported.
* [ ] Delivery review as docs/05 §5 says; only this delivery's paths and its hunk of docs/06 staged; the page moved to `work/done/` and its commit message suggested.
