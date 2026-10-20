# ch20-merge-and-marks

**Objective.** After chapter 20's "Boards" section the reader can say that, with a branch or a worktree per delivery, the command that pushes the queue to a board reads each slug's line from its worktree or its branch, and that one push carries the other deliveries' marks only as far as it can see them: a worktree's at once, a branch's once committed on it, a remote branch's once pushed, as chapter 14 teaches.

**Behaviour.** What the reader can do or explain after the chapter:

* With a worktree per delivery, `reservations` marked `[~]` in its worktree: a push from `search-catalog`'s command carries `[~]` for `reservations` the moment the mark changes, since it reads that worktree's file.
* With a branch per delivery and no worktree, `lend-book` marked `[*]` but not yet committed on its branch: a push from another delivery's command still shows `lend-book` as its branch last committed it; the chapter promises no mark that was not committed, and none from another machine that was not pushed.
* Say why "branch" alone was too narrow: a worktree is the other way to keep a branch per delivery (chapter 19), and its file is where a mark is seen first (chapter 14).
* Find it in the key points: the board bullet says "with a branch or a worktree per delivery, read from each slug's worktree or branch".
* Edge: on trunk nothing changes; the sentence's first clause, "the board shows that mark at once", stays true for the mark the command itself changed.
* The chapter's source keeps one sentence per line (docs/04): the problem section's first line, which holds two sentences, becomes two lines with the same words.

**Contract.** Two files, `book/en/20-team-tools.md` and `book/pt/20-team-tools.md`, same changes in both editions; line numbers are those at `838f737`.

* "The problem", line 8 (en and pt), candidate 13: split after the first sentence into two source lines, words unchanged.
  * en: line 8 `The kit assumes one person who proposes a delivery, uses it and reviews it: by default the staged diff, before committing it, or, when the Git slot's word lets the agent commit, the commit, after it lands.` and line 9 `The kit splits those roles no further; how a team splits them is the team's own practice.`
  * pt: line 8 `O kit assume uma pessoa que propõe uma entrega, usa a entrega e a revisa: por padrão o diff em stage, antes de fazer o commit, ou, quando a palavra do slot Git deixa o agente fazer o commit, o commit, depois que ele entra.` and line 9 `O kit não divide esses papéis além disso; como um time os divide é prática do próprio time.`
* "Boards" / "Quadros", line 60 (en and pt), candidate 10, replaced whole:
  * en: `Since the push runs inside the command that changed the mark, the board shows that mark at once; with a branch or a worktree per delivery the command that pushes reads each slug's line from its worktree or its branch, so one delivery's push carries every other delivery's mark as far as it can see it: a worktree's the moment it changes, a branch's once committed on it, a remote branch's once pushed.`
  * pt: `Como o envio roda dentro do comando que mudou a marca, o quadro mostra essa marca na hora; com um branch ou um worktree por entrega o comando que envia lê a linha de cada slug no worktree ou no branch dele, então o envio de uma entrega leva a marca de cada outra entrega até onde consegue vê-la: a de um worktree no momento em que ela muda, a de um branch quando entra em um commit nele, a de um branch remoto quando esse commit é enviado.`
* "Key points" / "Pontos-chave", the board bullet, line 87 (en and pt), candidate 10: only its last clause changes.
  * en: `and, with a branch per delivery, read from each slug's own branch.` becomes `and, with a branch or a worktree per delivery, read from each slug's worktree or branch.`
  * pt: `e, com um branch por entrega, lido do branch de cada slug.` becomes `e, com um branch ou um worktree por entrega, lido do worktree ou do branch de cada slug.`
* Terms of docs/03: board mirror, kanban board, branch, worktree, trunk, slug. No new term.
* Sources: chapter 14, "At the moment the work changes" (en lines 61 to 63, pt 62 to 64: a worktree's file at once, a branch once committed, a remote branch once pushed); docs/05 §4. No footnote: the reader gains nothing to open.
* Cases: Case A's sentences (57, 58) are untouched; the changed sentence speaks of a project's slot in general, as now. No number.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change beyond the text.

**Out of scope.**

* The review sentences of lines 8, 10, 33, 34 and 85 ("by default", who reviews before the merge): `ch08-13-20-default-review`, after this line; here line 8 is only split.
* Step 4 of the pull request list (line 25) and step 1 (line 21): a pull request needs a branch, and a worktree holds one, so "a branch" there stays true.
* Chapter 14 and its FACE paragraph: `ch14-face-retired`. Chapters 8, 13, 17 and 23: `ch08-13-17-next-line`.
* Chapter 20's opening, gain section and every other sentence: unchanged and still true.
* Line 32's two quoted sentences: a quotation, kept whole.

**Done when.**

* [x] Both editions changed as the Contract says, and nowhere else.
* [x] One sentence per source line in both editions of chapter 20, quotations aside; no em dash.
* [x] The gain section and the opening are still true; no number, version or before and after of the kit added.
* [x] `make verify` green.
* [x] `make book` built both editions: `work/done/m23-review.md` records the build at `8a87b0c`, whose chapter 20 is as this delivery left it, with both PDF paths (`output/one-page-at-a-time.pdf`, `output/uma-pagina-de-cada-vez.pdf`).
* [x] Only this delivery's files staged, by the batch's driver from its own index (Divergences), with the suggested commit message; no commit by this lane.

**Decisions from the documents.**

* "As far as it can see": a worktree's mark at once, a branch's once committed, a remote branch's once pushed, the words of chapter 14 (en :63) and docs/05 §4, which the finding cites.
* "Branch or worktree": docs/05 §4 and docs/03's `kanban board` row say "a branch or a worktree per delivery".
* Line 8's split: docs/04, "One sentence per line"; candidate 13 shares this line by m22-review's Findings table.
* Taught as the kit is today, with no version or before and after: AGENTS.md and the M22 rule.

**Decisions taken alone** (the author chose recommended answers):

* "every other delivery's mark as far as it can see it" replaces "the other deliveries' latest marks": "latest" promised a mark the push may not see.
* The visibility list goes inline in the same sentence, not a pointer "as chapter 14 says": the next line (61) already links chapter 14, and the reader gets the rule where it applies.
* In Portuguese, "no worktree ou no branch dele", as the sentence and chapter 14 (pt :62) already write it, "dele" being the slug's.
* Line 8 is split with words unchanged, leaving its wording to `ch08-13-20-default-review`, which runs after this line on the same file.
* No docs/03 change: every term exists.

**Proof.**

* `git diff HEAD` of chapter 20, each edition: three hunks, the problem section's first line split in two with words unchanged (line 8), the push sentence (line 60) and the board key point (line 87), same lines in both editions. Its commit `9c2e490` holds four hunks per edition, 7 insertions and 6 deletions each: these three and `ch08-13-20-default-review`'s sentence at :35, the second by position, with that delivery's :11 and :86 inside the first and last.
* A search for a sentence end followed by a capital inside one source line finds, in both editions of chapter 20, only line 33's quotation.
* No em dash, number, footnote, case, version or date added; the opening, the gain section and Case A's sentences are unchanged.
* `make verify` green after the last edit of the chapters (exit 0).
* This lane did not run `make book`; `work/done/m23-review.md` records the build at `8a87b0c`, which holds chapter 20 as this delivery left it, with both PDF paths. Staging and the commit are the driver's in this batch.

**Divergences.**

* Done when's `make book` and staging items are not this lane's: the build is the one `work/done/m23-review.md` records, and the driver commits each delivery from its own index.
* The delivery review did not run in a separate read-only agent: this lane had no tool to start one, so it went through the session's advisor; no review by a read-only agent, as docs/05 §5 says, is recorded for it.

**Delivery review.** The session's advisor read this delivery's hunks of chapter 20, both editions, and its docs/06 hunk against this page and docs/04: the chapter text matches the Contract word for word in both editions, Case A's sentences and step 4 are untouched, no em dash; nothing in the chapters changed. Fixed on this page: a divergence that was the Contract applied ("that mark") was dropped, the decisions below were listed, and the commit subject made imperative. Chapter 14's hunks in the tree are another lane's (`ch14-face-retired`), not read as this delivery's.

**Decisions taken alone in /apply.**

* The review went through the session's advisor, since no agent could be started from this lane.
* `make book` and staging are left to the driver, as the batch's rule says; their Done when items name the build `work/done/m23-review.md` records and the driver's index.

```commit
docs(ch20-merge-and-marks): carry the marks a board push can see

- ch20: the push reads each slug's line from its worktree or its branch
- ch20: a worktree's mark at once, a branch's once committed or pushed
- ch20: the board key point names a branch or a worktree per delivery
- ch20: the problem section's first line holds one sentence per line

work/done/ch20-merge-and-marks.md
```
