# ch19-partial-branch-commits

**Objective.** After chapter 19 the reader knows what happens when `/apply` blocks in a delivery's worktree: it may stage the partial work for the reader to commit on the branch with a partial message, and the branch stays unmerged until the delivery is whole.

**Behaviour.**

* Given `/apply return-book` (pt `devolver-livro`) blocked in its worktree on an answer nobody has given, the reader says what the agent does: marks the line `[?]` with `· resume: apply` and the reason, writes on the page what was built, may stage the partial work for the reader to commit there (docs/05 §6 says "may") and shows a partial message in a `commit` block.
* The reader commits that work on `focus-kit/return-book` when they choose, with the partial message: it says it is partial, names the blocker, never implies verify passed, and its last line is `work/return-book.md`, where the page waits (chapter 13).
* Asked to merge the branch while the line is `[?]`, the reader does not merge: the branch stays unmerged until the delivery is done, so one `git merge --no-ff` still brings the whole delivery to `main`.
* When `/apply` resumes in the same worktree and the folder is clean, the reader knows the work so far is in those commits and that the delivery review reads them against the branch's base (chapter 13).
* The reader contrasts trunk: there a blocked `/apply` stages nothing and the work stays uncommitted until it is whole (chapter 13).
* A partial commit is not the use-first commit of the finished delivery: the reader still uses the whole delivery and reads its staged diff before the commit that completes it.

**Contract.** Files: `book/en/19-worktrees.md` and `book/pt/19-worktrees.md`.

* "Worktrees in the kit" / "Worktrees no kit": one short paragraph after the sentence "You use the delivery, review and commit on the branch, merge into `main` with `--no-ff`, remove the worktree and delete the branch." (pt the matching sentence), saying the Behaviour above; it reconciles with the paragraph's later "ask for the commit once you have used the delivery and the staged diff holds only it" by naming the partial commit as the one exception, a commit of unfinished work whose message says so.
* "Key points" / "Pontos-chave": the worktree bullet gains one clause: a blocked `/apply` there may stage its partial work for you to commit on the branch, which stays unmerged until the delivery is done.

Slugs and branch are the chapter's existing lending-library example, written for the chapter, `return-book` / `devolver-livro` on `focus-kit/<slug>`. Sources: docs/05 §6 ("On a delivery branch or worktree, partial changes may be staged and suggested for the person to commit there. Keep the branch unmerged until the delivery is complete"), the installed apply skill, docs/05 §5 Delivery review; chapter 13's "When the work cannot go on", its partial message and its delivery review, which already point here. Terms of docs/03: worktree, branch, stage, waiting mark, delivery review; no new term, no number, no private case.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** Chapter 13: its pointer "(chapter 19)" already stands and becomes true with this delivery. A branch per delivery without a worktree (chapter 18): the queue line names chapter 19. Moving a partial trunk delivery to its own branch when a prerequisite must be built first (docs/05 §6): a separate rule the line does not name.

**Decisions from the documents.** The paragraph goes in "Worktrees in the kit", where `/apply` stages and the person commits, not in "The life of a worktree", whose steps are plain git (docs/05 §6 places it under the kit's commands). The partial commit is named as an exception to use-first, since the kit's next steps after a block are commit-or-wait, not use (docs/05 §6, chapter 13).

**Done when.**

* [x] Both editions written, same hunks; each Behaviour line checked against both; chapter 13's "(chapter 19)" pointer now leads to the case.
* [x] The chapter opens with its value; no filler and nothing useful cut; every number and quoted artifact keeps its source; terms follow docs/03; no em dash; no run narrated.
* [x] No Case A or Case B passage changed or added, so the author's OD-3 approval is inapplicable.
* [x] `make verify` green after the last edit; `make book` builds both editions and the page gives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the author's review.
* [x] Delivery review by a read-only Opus agent per docs/05 §5, its candidates answered on this page; page archived and commit message suggested.

## What happened

**Built.** Chapter 19, "Worktrees in the kit": a new paragraph after "You use the delivery, review and commit on the branch..." follows `/apply return-book` (pt `devolver-livro`) blocked in its worktree on an unanswered question, `· resume: apply · blocked: what if the copy comes back damaged?`: what the agent writes and shows, the partial commit on `focus-kit/return-book` with its partial message ending in `work/return-book.md`, named as the one exception to using the delivery before its commit; no merge while the line is `[?]`, so one `git merge --no-ff` still brings the whole delivery; on resume, a clean working folder means the work is in those commits, which the delivery review reads against the branch's base; on trunk, no partial commit. Key points: the worktree bullet gains the clause. Both editions, same two hunks. Chapter 13's "(chapter 19)" pointer now leads to the case.

**First occurrence.** None: no abstraction; chapter 13 states the rule, chapter 19 shows it in a worktree.

**Divergences.** None.

**Proof.** `make verify` green after the last edit. `make book` is run once by the batch driver at the end of this batch, which gives the author `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Review.** One read-only Opus context over both chapter files against this page and docs/04. Findings: (1) "On trunk none of this happens" overstated, since trunk still marks `[?]` and shows the partial message; now "On trunk there is no partial commit" (pt "No trunk não há commit parcial"), fixed. (2) The partial message's rule left out "or that the delivery is done" (docs/05 §6); added in both, fixed. (3) pt subjunctive "voltar danificado" and "trava ... esperando uma resposta"; fixed. (4) pt chapter 13 says both "bloqueado" (line 74) and "travado" (line 249) for a blocked `/apply`; chapter 19 keeps "travado", as chapter 13's partial message does; chapter 13 is out of scope, queued as a new line. (5) "a clean folder" now "a clean working folder" (pt "pasta de trabalho limpa"), as chapter 13 says; fixed.

**Decisions.** The blocked reason is a question about a damaged copy, not a fine: fines are out of the library's scope (chapters 12 and 17). The "asked to merge" Behaviour is said as "do not merge the branch, whoever asks". No Case A or Case B passage changed.

```commit
docs(ch19-partial-branch-commits): commit blocked work on its branch

- Chapter 19: a blocked /apply in a worktree may stage its partial
  work for a partial commit on the branch, which stays unmerged
- The partial commit is the one exception to use-first; on resume
  the review reads those commits against the branch's base
- Key points follow; both editions

work/done/ch19-partial-branch-commits.md
```
