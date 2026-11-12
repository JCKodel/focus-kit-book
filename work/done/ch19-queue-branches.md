# ch19-queue-branches

**Objective.** After chapter 19 a reader running a worktree per delivery can ask the kit's queue script what may run now from `main/` or from any worktree, and read its answer right: each delivery's line taken from that delivery's branch on origin, the mark further along kept, so a merged or in-flight line never shows as free, and the lines that exist only on a branch listed apart; and the reader knows the one thing the tree does not show, a branch whose first mark has not been pushed yet.

**Behaviour.** What the reader can do or explain after the chapter, in both editions:

* Asked "what may run now?" in a worktree layout, runs the queue script with the Git slot's word, `git -c "alias.fq=!sh .agents/skills/propose/scripts/queue.sh" fq worktree .focus-kit focus-kit/`, the hidden folder and prefix the slot names, and explains that it fetches origin, reads every line from the default branch on origin and each delivery's line from `origin/<prefix><slug>`, and edits nothing.
* Reads the chapter's example run from `main/`: `return-book` shows `[*] · in flight: apply` and `overdue-list` `[>] · apply now`, though `main/`'s own queue still shows both `[ ]`, because each line was read from its branch; `m2-review` sits under `overdue-list` with `+ after return-book`; and `damaged-copy`, a line `return-book`'s session added on its branch, appears under "only on a branch" with the branch's slug in brackets.
* Explains "the mark further along": where the folder's copy, the default branch on origin and the delivery's branch disagree on a line, the script keeps the mark furthest along the flow, so in `overdue-list`'s worktree, whose queue still shows `return-book` as `[ ]`, the line merged as `[x]` into `main` on origin no longer appears as free.
* Edge, must fail: typed with `trunk` in that layout, the script fetches nothing and reads only the folder's own copy: in `overdue-list`'s worktree it offers `return-book`, already merged, as `propose now`. The reader says why: the word must be the Git slot's.
* Edge: the script reads branches on origin only, as last fetched; a mark committed in a worktree and not pushed, or a branch never pushed, is not seen from another folder. When `git fetch` fails it prints `note: git fetch origin failed; branches as last fetched` and goes on.
* Edge: a line whose branch is on origin with no mark pushed yet, the moment just after `/propose` claims it, shows as the main branch has it, `[ ] · propose now`; the branch is still the claim (chapter 14), and the claim script tells the next `/propose` with `claim: existing`. The reader does not take a line as free from the tree alone while its branch exists on origin.
* Says where this sits beside what chapter 19 already teaches: `main/`'s queue shows a line as it was until the merge and each worktree's its own branch's state; the script is how a session or a person reads all of them at once.

**Contract.**

* Sections: one passage in "Worktrees in the kit", after the paragraph on where the marks are written (:193-194 in both editions), with the example block; one clause in the worktree bullet of "Key points". No new section, no change to "What the team gains" (the agent chose: the example itself shows what the reading avoids, and the chapter's gain, two deliveries at once, each one change, is unchanged; ADR-0015 asks one gain per chapter, not per passage). Nothing in "Proposing in a batch" or "When parallel stops paying" says how free lines are picked in worktrees, so neither changes.
* Terms of docs/03: queue tree / árvore da fila (docs/03 :119, already holding the branch reading since kit-2026-10-24), free line, worktree, claim script. No new term.
* Sources: the installed `.agents/skills/propose/scripts/queue.sh` (focus-kit 2026.10.24, SETUP §3.7 at `51ff062`) and its changelog entry 2026.10.24 ("keeping the further mark, so a worktree's older copy does not show a merged line as free"). No source note: the reader has the script after chapter 8, which already points to the changelog (docs/04's rule on source notes). The chapter links [chapter 14](14-queue-states.md) only as it does now (:24, :194), not a section of chapters 11 to 14, which ch11-14-queue-tree is changing.
* The example, "written for this chapter", on the lending library; the script's words stay in English in both editions (docs/04), slugs in Portuguese in the Portuguese edition. Each block was produced by the installed script on a scratch repository shaped as below, run from `main/`: a bare origin; on `main`, docs/06 holding under `## M2. Returns` (`## M2. Devoluções`) the four lines `[x] lend-book (PA)`, `[ ] return-book (PA) · after lend-book`, `[ ] overdue-list (PA) · after lend-book` and `[ ] m2-review · after return-book, overdue-list`, with no token, each with a description, Portuguese slugs in the Portuguese run; `return-book` and `overdue-list` claimed with the claim script's `worktree .focus-kit focus-kit/`; `return-book`'s branch committed and pushed at `[*]` with `[ ] damaged-copy (PA)` added just above `m2-review`; `overdue-list`'s at `[>]`. In the bracket after a line only on a branch the script names a branch that holds it, not the only one. English:

  ```
  milestone: M2. Returns
  [*] return-book (PA) · in flight: apply
  [>] overdue-list (PA) · apply now
   └[ ] m2-review + after return-book · waits: after overdue-list

  free for /apply, together: overdue-list
  free for /propose, together: none
  only on a branch:
    damaged-copy (return-book)
  ```

  Portuguese, M2. Devoluções, `emprestar-livro`, `devolver-livro`, `lista-de-atrasos`, `exemplar-danificado`, `m2-review` (the kit's `<milestone>-review` stays, docs/04):

  ```
  milestone: M2. Devoluções
  [*] devolver-livro (PA) · in flight: apply
  [>] lista-de-atrasos (PA) · apply now
   └[ ] m2-review + after devolver-livro · waits: after lista-de-atrasos

  free for /apply, together: lista-de-atrasos
  free for /propose, together: none
  only on a branch:
    exemplar-danificado (devolver-livro)
  ```

  The Portuguese tree's fourth line is 70 columns, within docs/04's 74; /apply does not reflow it. The other runs the Behaviour cites, from `overdue-list`'s worktree after `return-book`'s merge, with the slot's word and with `trunk`, are described in prose, not shown.
* Cases: none.
* `work/kit-proposals.md`: one entry under "For the next focus-kit version", the next free number when /apply runs, "from ch19-queue-branches": `queue.sh` reads a line's mark only, so a line whose branch is on origin with no mark pushed shows as free, while docs/05 §4 counts the branch as the claim; and its order of marks, `[ ]`, `[~]`, `[?]`, `[>]`, `[*]`, `[x]`, puts `[?]` before `[>]`, so in a worktree a `[?] · resume: apply` not yet pushed shows as the branch's `[>]` on origin, `apply now`; and it reads `origin/*` only, while docs/05 §4 reads each slug's line from its branch "local or remote". The next version counts a branch on origin as the line taken, keeps a `[?]` reached after `[>]` or `[*]`, and either reads local branches too or says in docs/05 §4 that the script reads origin. Chapter 19 keeps the kit's behaviour until then.

**Out of scope.**

* The tree's shape, the free lines offered as one command and its cost, and the commands with no slug: ch11-14-queue-tree's, in chapters 11 to 14.
* Chapters 12 and 14 saying the queue is read from each branch "local or remote" while the script reads origin only: they keep docs/05 §4's rule, which holds for whoever reads the queue by hand, and the difference goes into the kit proposal above (the author's answer in the /propose session).
* Any change to `queue.sh`, `claim.sh` or the kit: the book teaches the kit as it is.
* A second example block for the worktree and `trunk` runs: the prose carries them; one block teaches the reading.
* docs/03, docs/05, ADRs: unchanged; the queue tree row already says what this chapter teaches.

**Done when.**

* [x] Both editions written, same file name, parity green; the passage opens from the reader's problem (which lines are taken when each mark lives on its branch) and states its value, no filler and nothing useful cut.
* [x] Both example blocks match, byte for byte, a run of the installed `queue.sh` on a scratch repository shaped as the Contract says; the prose claims about the worktree run after the merge, the `trunk` run, the unpushed branch and the failed fetch each match a scratch run; recorded on this page.
* [x] The `work/kit-proposals.md` entry written as the Contract says.
* [x] No passage says the script reads local branches or counts a branch as taken; no em dash; no run narrated.
* [x] `make verify` green; then `make book`, and the paths of both PDFs given to the author.
* [x] The Delivery review as docs/05 §5 says.
* [x] Staged: this page moved to `work/done/`, both chapter files, `work/kit-proposals.md` and this line's own hunk of docs/06, nothing else.

**Decided without the person.** This page was written by a subagent of `/propose ch08-update-2026-10-24 ch11-14-queue-tree ch19-queue-branches`, which could not ask; the agent chose each of these from the documents named:

1. Where the passage goes and that no section is added (chapter 19's own structure; docs/05 §3's chapter Contract).
2. To teach the unpushed-branch gap in the chapter rather than leave it out, worded as chapter 14 :61-64 already does, the tree showing a mark once it is pushed and the branch being the claim (AGENTS.md: every claim real; the memory rule that the book teaches the kit as it is today).
3. Not to teach the `[?]` order quirk in the chapter, only in the kit proposal: it shows only in the delivery's own worktree before its mark is pushed, where the session knows its own state.
4. The `(PA)` token stays: the definition took nothing from the sibling pages, and the build touches only chapter 19, this page, `work/kit-proposals.md` and its own queue line; should a sibling also add a kit proposal, the two entries are separate lines, not a conflict (docs/05 §4).
5. Staging: /propose stages nothing in a batch (docs/06 `ch19-batch-staging`; chapter 19 :329).

**What happened (/apply, stopped).** /apply marked the line `[*]` and built the Contract's scratch repository: a bare origin, a container with `main/` and `.focus-kit/`, both lines claimed with the claim script's `worktree .focus-kit focus-kit/`, `return-book`'s branch pushed at `[*]` with `damaged-copy` added, `overdue-list`'s at `[>]`. Run from `main/` with the slot's word, the installed `queue.sh` prints both of the Contract's blocks byte for byte, in each language.

It stopped before writing either chapter: the page contradicts docs/04. The Portuguese tree's fourth line, ` └[ ] m2-review (--) + after devolver-livro · waits: after lista-de-atrasos`, is 75 columns, not 74: the script pads one space before `└`, and counted from `└` the line is 74. docs/04's **Width of a block** keeps a block to 74, `scripts/check_width.py` measures it so, and `make verify` would fail on it. No fix lies inside /apply: the slugs are docs/03's running-example words, `m2-review` is the kit's `<milestone>-review`, Behaviour puts `m2-review` under `overdue-list` with `+ after return-book`, and swapping the two lines in the queue only swaps the slugs. The person's choice, each a page or a document change:

1. Page: the scratch queue's `m2-review` line without its `(--)` token, in both runs: the line prints ` └[ ] m2-review + after devolver-livro · waits: after lista-de-atrasos`, 70 columns, with the same state, since `waits:` is decided before the token is read (checked on a scratch run). It changes the Contract's fixture, whose `m2-review` line carried `(--)`, and the Contract's fourth line in both blocks; decision 4 is this line's own `(PA)` token and stays.
2. Page and docs/03: another shape or slug, which changes docs/03's running example, shared with other deliveries.
3. Document: docs/04 and `check_width.py` exempt a command's verbatim output from the width rule, a toolchain change this page's scope does not hold.

**The person's answer.** Option 1 ("Tirar (--)"), given in the session that typed the command: the scratch queue's `m2-review` line carries no token in both runs, changing the Contract's fixture for that line only, not decision 4, because the Portuguese line was 75 columns against docs/04's 74. The Contract above now says so, and its two blocks are the runs of that fixture. /apply resumed on the command's word.

**Proof.** On the fixture without the token, in each language, the installed `queue.sh` run from `main/` printed the Contract's two blocks byte for byte, the widest line 63 columns in English and 70 in Portuguese. The prose's other claims, each a run on a copy of the same fixture, both languages alike:

* After `return-book`'s branch was marked `[x]`, merged into `main` with `--no-ff` and pushed, `overdue-list`'s worktree still showed `return-book` `[ ]`; the script with the slot's word, run there, left `return-book` out of the tree, with `[>] overdue-list (PA) · apply now` and ` └[ ] m2-review · waits: after overdue-list`. With `trunk` there it printed `[ ] return-book (PA) · propose now` and `free for /propose, together: return-book`.
* `overdue-list` committed at `[*]` in its worktree without a push, and a branch `focus-kit/m2-review` committed at `[~]` and never pushed: from `main/` the script showed `[>] overdue-list (PA) · apply now` and `m2-review` at `[ ]`.
* With origin's URL pointing nowhere, it printed `note: git fetch origin failed; branches as last fetched`, drew the same tree as before and exited 0.
* With both lines claimed and no mark pushed, it showed both `[ ] · propose now`; the claim script run again for `return-book` printed `claim: existing`, and `git branch -r` in `main/` listed `origin/focus-kit/return-book`.

Found and left as the kit is, not taught: after the merge, `damaged-copy`, merged into `main` too, still appears in the worktree's run under "only on a branch", since the worktree's own copy lacks it; the bracket then names the branch, which git lists before `main`. It fits the page's "names a branch that holds it" and the chapter teaches the run from `main/` only.

`make verify` green, then `make book`: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Built.** In both editions of chapter 19, after the sentence on where a board sees the marks in "Worktrees in the kit": four paragraphs and the example block, from the reader's problem (no folder's queue shows every delivery) to the script's reading, the mark further along, the `trunk` word, what it does not see and the claim the tree does not show; and one clause in the worktree bullet of "Key points". Entry 14 of `work/kit-proposals.md`, the next free number. No section added, "What the team gains" unchanged, no new link to chapters 11 to 14.

**Delivery review** (one read-only agent on Opus, over this delivery's paths and its docs/06 line). No finding on the queue line or the kit proposal; every claim about the two scripts checked against them. Fixed, in both editions: the key-points clause read as if the script read the merge, now "reads them"; "an older copy never shows a line as earlier than it is" was false for a `[?]` reached after `[>]` or `[*]`, now "does not show a merged or in-flight line as free", the changelog's "does not show a merged line as free" with "or in-flight" added; "reads all of them at once" read as every folder's copy, now "every delivery's line"; "(chapter 14)" after "the branch is the claim" only repeated this chapter's own sentence, cut. Taken from its suggestions: the Portuguese "as palavras do script ficam em inglês", which the English lacked and chapter 14 already says, cut; "não é visto" agreed with two subjects, now "não são vistos". Kept: the plain "(chapter 14)" after the queue script, a pointer to where the script is taught, not a link. `make verify` green again, `make book` rebuilt.

```commit
docs(ch19-queue-branches): read every delivery's line from its branch

- chapter 19: queue.sh with the Git slot's word in a worktree layout
- the mark further along, the trunk word, what it does not see
- the claim the tree does not show, a branch with no mark pushed
- both editions; key point on the worktree bullet
- kit proposal 14: what queue.sh reads off trunk

work/done/ch19-queue-branches.md
```
