# ch12-14-17-20-branch-claim

**Objective.** After chapters 12, 14, 17 and 20, and the sentences of 18 and 19 that describe the same step, the reader can say what claims a line with a branch or a worktree per delivery: `/propose` checks the remote for the delivery's branch, creates it and pushes it at once, before the page exists, and that branch is the claim of the line; after `git fetch`, a line whose branch exists is taken, not free, whatever the main branch's queue shows, so that queue changes only through merges; and a session asked where things stand reads the delivery branches after `git fetch`.

**Behaviour.** What the reader can do or explain after the chapters:

* On trunk, nothing changes: no branch is created, nothing is pushed, and a line is taken by its mark in the one working tree, which every session in that folder sees at once.
* With a branch per delivery, `/propose lend-book` first checks the remote for `lend-book`; there is none, so it creates the branch and pushes it at once, before the page exists, and only then marks `[~]` and writes the page on it.
* With a worktree per delivery, the same with the branch `<prefix>/<slug>`: the remote checked, the worktree created from the main branch's `HEAD`, its branch pushed at once.
* Say why the push comes first: the main branch's queue shows `lend-book` as `[ ]` until the merge, and a mark committed on the branch reaches a second clone only once pushed; the branch on the remote is what a second person sees after `git fetch` the moment the work starts, so nobody starts the same line again from main's queue.
* A session in another clone asked for the next delivery runs `git fetch`; `lend-book`'s branch exists, so `lend-book` is taken whatever main shows, even before any mark on it is pushed, and the answer is `search-catalog`.
* Edge: the remote already has the delivery's branch when `/propose` starts. The line is taken: `/propose` does not start it, unless the definition is being resumed on the person's word that its session ended, where it reuses the branch that exists (docs/05 §4).
* Edge: the main branch's docs/06 never carries a claim; marks reach it only with each delivery's merge, so claiming a line never conflicts there.
* Edge: a branch named only `<slug>` in a worktree project is someone else's, not the delivery's, and claims nothing (chapter 19, unchanged).
* Asked "where are we?" with a branch or a worktree per delivery, the session fetches and reads the delivery branches: a line in flight shows under "In flight" though main's copy reads `[ ]`.
* The agent's push rule, read in chapter 19: the agent never pushes on its own, except the new branch `/propose` pushes when it creates it, which is the claim; every later push stays the person's to ask for.
* A pull request: the branch is on the remote from `/propose`'s start; the pull request opens once the page's commit is pushed, so the page is reviewed before any code exists.
* Find it in the key points: chapter 12's `/propose` bullet, chapter 14's free-line and kanban bullets, chapter 17's manager bullet, chapter 19's worktree bullet, chapter 20's pull-request bullet.

**Contract.** Twelve files, `book/en/` and `book/pt/` of `12-propose.md`, `14-queue-states.md`, `17-project-as-assistant.md`, `18-git-essentials.md`, `19-worktrees.md`, `20-team-tools.md`, the same change in both editions, one sentence per line as the chapters are laid out. Line numbers are en's today; pt's are the same unless named.

* Chapter 12, "What `/propose` does" (en and pt 27-29):
  * :27, the sentence on reading marks off trunk: gains that, after `git fetch`, a line whose branch exists is taken, whatever the main branch's queue shows; the rest stays.
  * :28, "otherwise the branch or worktree named after the slug, created, or reused when the definition resumes": becomes the remote checked for that branch first, a branch already there meaning the line is taken; then the branch or worktree created and its branch pushed at once, before the page exists, so the line is taken in every clone; or reused when the definition resumes, with any draft page brought into it (chapters 18 and 19).
  * :29 stays: the mark and the page still go with the delivery's branch.
  * Key points, the `/propose` bullet (en 171, pt 180): "starts in the delivery's branch or worktree, where the project's Git slot puts one" gains "pushing its branch the moment it creates it, the line's claim".
* Chapter 14, "At the moment the work changes" (en 60-64, pt 61-65):
  * :60 gains "pushed when `/propose` creates it" after "the mark lives on the delivery's branch".
  * One sentence after :60: after `git fetch`, a line whose branch exists is taken, whatever the main branch shows: the branch is the claim of the line, on the remote from the moment the work starts, before any mark on it is pushed, so the main branch's queue changes only through merges.
  * :61-64 stay; :63's "a remote branch once that commit is pushed" stays true for marks.
* Chapter 14, "The next line, and which run together" (en 70-72, pt 71-73): :71 gains that the session runs `git fetch` first and a line whose branch exists is taken; :72 gains that `lend-book`'s branch on the remote says taken even before any of its marks is pushed. Portuguese slugs as the chapter has them.
* Chapter 14, "Key points": the free-line bullet (en 184, pt 185) gains "with a branch or a worktree per delivery, a line whose branch exists after `git fetch` is taken, whatever the main branch shows", docs/03's `free line`; the kanban bullet (en 187, pt 188) "from each slug's own worktree or branch" becomes "from each slug's own branch, local or remote, pushed when `/propose` creates it", docs/03's `kanban board`.
* Chapter 17, "The manager's session" (en 119, 132, 151):
  * :119, the rules-file line: "answers from the queue and `work/`" gains ", and with a branch or a worktree per delivery from the delivery branches after `git fetch`", the installed AGENTS.md template's line.
  * :132: "so the session takes each slug's line" becomes "so the session runs `git fetch` and takes each slug's line"; the rest stays.
  * Key points, the manager bullet (:151): "from each slug's worktree or branch" becomes "from the delivery branches after `git fetch`".
  * The example answer stays: it is on the lending library, whose answer the next sentence already reads off trunk.
* Chapter 18, "Merges and the unit of work" (en and pt 25-33), widened as a sibling: :25 "creates the branch named after the slug, or reuses it when it exists" becomes "checks the remote for it, creates it and pushes it at once, so the line is taken in every clone, or reuses it when the definition resumes"; :27 "the first line is what `/propose` does for you" becomes "the first two lines"; the code block gains `git push -u origin lend-book` (pt `emprestar-livro`) right under `git switch -c lend-book`, in the same group, the blank line and the two merge lines unchanged.
* Chapter 19, "Worktrees in the kit", widened as siblings:
  * :179 "`/propose <slug>` creates the worktree ... or reuses the one that exists" becomes: checks the remote for `<prefix>/<slug>`, creates the worktree at `<hidden>/worktrees/<slug>/` on that branch from the main branch's `HEAD` and pushes the branch at once, so the line is taken in every clone, or reuses the one that exists, and writes the page there.
  * :194 "The agent never commits, merges, pushes, resolves a conflict or removes a worktree on its own" gains "apart from the branch `/propose` pushes when it creates it, the line's claim"; "the push, the conflict and the worktree stay yours to ask for" becomes "every later push, the conflict and the worktree stay yours to ask for".
  * Key points, the worktree bullet (:350): "and the line's marks live on its branch until the merge" becomes "`/propose` pushes the branch when it creates it, the line's claim, and the line's marks live on it until the merge".
* Chapter 20, "A pull request per delivery" (en and pt 22-26):
  * Step 1 gains: `/propose` pushes the branch the moment it creates it, so the line is taken for everyone who fetches.
  * Step 2's "Open the pull request as soon as it is pushed" becomes "as soon as the page's commit is pushed": two pushes, the branch's by `/propose` and the page's by the person or at their asking.
  * Step 4: "so the queue on the main branch holds what has landed" becomes "so the queue on the main branch changes only through merges and holds what has landed"; the rest stays.
  * Key points, the pull-request bullet (en 86): "a branch named by the slug" gains ", pushed when `/propose` creates it".
  * :61 and the board bullet (:88) stay true: they read marks, not the claim.
* Portuguese: "claim" is "reivindicação" (docs/03), taken is "ocupada", "remoto" and "`git fetch`" as chapter 18 and docs/03 write them; "push" as each chapter already writes it, "enviado/envio" in 14 and 20, "push" in 18 and 19.
* Terms of docs/03: claim, free line, kanban board, remote, branch, worktree, trunk. Rows already exist since kit-2026-10-20; none to add.
* Sources: docs/05 §§2 and 4 and the installed `references/documents.md` at 2026.10.20 (the Git slot options: "pushes it", "`git ls-remote --exit-code --heads origin <prefix>/<slug>`", "pushes its branch at once, so the line is taken in every clone"); the AGENTS.md template's "where things stand" line; docs/03 `claim` and `free line`. No footnote: the reader gains nothing to open.
* Cases: none. No number, version, date or commit.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 8: `ch08-update-2026-10-20`, in parallel.
* Chapter 13 :28, how `/apply` weighs the next free line off trunk: true but silent on the claim; `ch12-14-parallel-token` (M25) and `ch13-19-claim-script` (M28) touch chapter 13 next, the latter on the claim itself. Reported to the driver.
* Chapter 23 :66 (the manager reads each slug's line from its worktree or branch), chapter 7 :80-84 (the three git strategies, quoting no slot option), chapter 10 :34-36, and the free-line definitions in trunk contexts (chapter 7 :80, 18 :184, 19 :24): true as they stand.
* The sentence "Without a board the marks cost nothing", which the kit removed: no chapter holds it (chapter 18 :76's "costs nothing" is about branches).
* The kit's reason as a story, the near miss its changelog tells: the book teaches the kit as it is today, with no version or before and after; the reason enters only as the second reader of main's queue who would start the line again.
* The claim script, its alias and Windows: `ch13-19-claim-script` (M28). Where each session opens: `ch13-19-session-folder` (M26).
* This repository's own git: it stays on trunk and the agent never pushes (docs/05 §5).

**Neighbouring lines on the same files**, applied after this one in queue order: `ch12-14-parallel-token` (M25: chapters 12, 13, 14), `ch13-19-session-folder` (M26: chapter 19 "Worktrees in the kit", the sentence at :179 included), `ch12-14-18-several-slugs` (M27: 12, 13, 14, 18), `ch13-19-claim-script` (M28: 19), `ch14-after-over-token` (M29: 14). This Contract is written against the files as they are today.

**Decisions from the documents.**

* `/propose` checks the remote, creates and pushes the branch at once, before the page exists, then marks `[~]`: docs/05 §2 and the installed template's Git slot options at 2026.10.20.
* After `git fetch`, a line whose branch exists is taken, whatever main shows, and main's queue changes only through merges: docs/05 §4, docs/03 `free line` and `claim`.
* An existing branch is reused only on resumption, on the person's word that its session ended: docs/05 §4 and the propose skill.
* "Where are we" reads the delivery branches after `git fetch`: AGENTS.md's line as the template now writes it (`work/done/kit-2026-10-20.md`).
* Taught as the kit is today, no version or number: AGENTS.md, the author's rule.
* Both editions in the same delivery: ADR-0004.

**Decisions taken alone.**

* Widened to chapters 18 :25-33 and 19 :179, :194, :350: each describes `/propose` creating the branch, or the agent never pushing, and goes stale without the push; no other line before M26 owns them. The queue line should name them: "chapters 12, 14, 17, 18, 19 and 20".
* Chapter 13 :28 is not widened: true as written, and two later lines touch chapter 13, one on the claim itself.
* Chapter 18's block shows the push as `git push -u origin lend-book`, plain git that chapter 18 :70 already teaches; the remote check stays in prose, since it changes nothing the reader sees.
* "Taken" in Portuguese is "ocupada", clearer than "pega"; "reivindicação" only where the text names the claim, as docs/03 does.
* No new gain sentence: the kit's evidence is a near miss in a project the book does not name, and the chapters' gain sections already cover a board and a manager reading the queue.
* Chapter 17's example answer stays as written: it reads the same with branches once the session has fetched, and the sentence after it says how.

**Done when.**

* [x] Each passage of the Contract changed, both editions written; no other sentence changed.
* [x] Each chapter still opens with its value; no filler and nothing useful cut.
* [x] No number added; no em dash, version, date or commit hash in a chapter; no private case used, so no approval owed.
* [x] `make verify` green.
* [x] `make book` built both editions: the batch's driver ran it after this lane, at `2b66f27`, this delivery's commit (exit 0), and `work/done/m24-review.md` records the build at `2fccad2`, the same `book/`, with both PDF paths.

**Built.** Every Contract passage in both editions: chapter 12 :27, :28 and the `/propose` key point; chapter 14 :60, the new sentence after it on the branch as the claim, :71-72 and the free-line and kanban key points; chapter 17 :119, :132 and the manager key point; chapter 18 :25, :27 and `git push -u origin lend-book` (pt `emprestar-livro`) in the block; chapter 19 :179, :194 and the worktree key point; chapter 20 steps 1, 2 and 4 and the pull-request key point. Chapter 14's new sentence makes pt's later line numbers one more than before.

**Checked.** Each change against the installed kit's `references/documents.md` at 2026.10.20 (the Git slot options, the queue paragraph, the AGENTS.md "where things stand" line) and docs/03 `claim`, `free line`, `kanban board`.

**Divergences.** None from the Contract.

**Decisions taken alone in /apply.**

* Chapter 12's Portuguese, which had no word for push, uses "enviado/enviando", as chapters 14 and 20.
* Chapter 18's Portuguese :25 says "dá push nele", the verb chapter 18 already uses.
* Chapter 20 step 2 says which push opens the pull request as "the second push, yours or asked of the agent".
* Chapter 19 :179 keeps "or reuses the one that exists" as the Contract fixes it; chapter 12 :28 and 18 :25 already say the reuse is for a definition that resumes.
* For the driver: the queue line should name "chapters 12, 14, 17, 18, 19 and 20" (Decisions taken alone above).

**Delivery review.** A read-only general-purpose agent on Opus, launched by this lane, read `git diff HEAD` of the twelve chapters against this page, docs/03, docs/04 and the kit source; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded. Nothing broke the page or docs/04; six wording preferences:

* en 14:72 "takes a line ... as taken": fixed, "counts a line whose branch exists as taken".
* en and pt 19:350 "on it" / "nele" ambiguous: fixed, "on the branch" / "no branch".
* en and pt 12:171/180, the pushing phrase before "or on trunk": kept, the Contract places it there.
* en and pt 19:179, reuse without "when the definition resumes": kept, the Contract keeps the clause.
* en and pt 12:28, dense participle chain: kept, the Contract's structure; accurate.
* pt 12 "enviado/enviando": kept, decided above.

**Proof.** `make verify` passed whole (build, parity, em dash, prose, width, examples, links, disclosure) after the last edit, the page's move included. The batch's driver ran `make book` at `2b66f27`, this delivery's commit (exit 0); `work/done/m24-review.md` records the build at `2fccad2`, the same `book/`, with both PDF paths.

```commit
docs(ch12-14-17-20-branch-claim): teach the pushed branch as claim

- /propose checks the remote, creates and pushes the branch at once
- after git fetch a line whose branch exists is taken (ch 12, 14)
- where things stand reads the delivery branches after fetch (ch 17)
- ch 18 block gains git push -u; ch 19 and 20 name the first push

work/done/ch12-14-17-20-branch-claim.md
```
