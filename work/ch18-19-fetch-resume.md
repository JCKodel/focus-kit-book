# ch18-19-fetch-resume

**Objective.** After chapters 18 and 19 the reader, a non-developer too, can say what a remote is where chapter 18 first names it, what `git fetch` and the `-u` of `git push -u` do, and that `/propose` reuses a delivery's existing worktree and branch only when its definition resumes.

**Behaviour.** What the reader can do or explain after the two chapters:

* Read chapter 18's "One delivery, one step to undo" and know what "the remote" means at its first use (:25), before the section on commits defines it in full.
* Read chapter 18's `lend-book` example and say what `git push -u origin lend-book` does: it sends the new branch to the remote named `origin`, and `-u` links the local branch to it, so a later plain `git push` or `git pull` on that branch needs no names.
* Read chapter 18's remote paragraph (:71) and tell `git fetch` from `git pull`: fetch brings the remote's branches into your clone without changing yours, so you see the branches others pushed, which a session does before it reads the queue (chapter 14); pull brings the remote's new commits into your branch.
* Read chapter 18's key point on the remote and find fetch beside clone, push and pull.
* Read chapter 19 :179 and say that `/propose` creates and pushes `<prefix>/<slug>`, or, when the definition resumes, reuses the worktree and branch that exist, as chapter 12 :28 and chapter 18 :25 say.
* Edge: docs/03's `remote` row, which defines `git fetch` and cites chapter 18, now cites a chapter that says the same thing.
* Edge: no passage of the two chapters reads as if an existing branch were reused whatever the line's state; no chapter text names a version, a date or a run.

**Contract.** Two chapters, same changes in both editions, against the files as they are today (en and pt line numbers match). One sentence per line, as the chapters are laid out. Chapter 18 gains one line after its first code block, so its lines from :37 on move down by one; the cites below are the lines as they are now.

* `book/en/18-git-essentials.md` and `book/pt/18-git-essentials.md`:
  * :25, en: "`/propose` checks the remote for the branch named after the slug," becomes "`/propose` checks the remote, the copy of the repository the team shares on a server, for the branch named after the slug,". The rest stays.
  * :25, pt: "o `/propose` consulta o remoto pelo branch com o nome do slug," becomes "o `/propose` consulta o remoto, a cópia do repositório que o time compartilha em um servidor, pelo branch com o nome do slug,". The rest stays.
  * New line after the code block (:29 to :35), before "A squash merge also leaves one step":
    * en: "`git push -u origin lend-book` sends the new branch to the remote named `origin`, and `-u` links your branch to it, so a later `git push` or `git pull` on that branch needs no names."
    * pt: "`git push -u origin emprestar-livro` envia o branch novo para o remoto chamado `origin`, e o `-u` liga o seu branch a ele, então um `git push` ou `git pull` seguinte nesse branch não precisa de nomes."
  * :71, en: "`git push` sends your branch's new commits to it, and `git pull` brings its new commits into your branch." becomes "`git push` sends your branch's new commits to it, `git fetch` brings its branches into your clone without changing yours, so you see the branches others pushed, as a session does before it reads the queue ([chapter 14](14-queue-states.md)), and `git pull` brings its new commits into your branch."
  * :71, pt: "`git push` envia para ele os commits novos do seu branch, e `git pull` traz os commits novos dele para o seu branch." becomes "`git push` envia para ele os commits novos do seu branch, `git fetch` traz os branches dele para o seu clone sem mudar os seus, então você vê os branches que outros enviaram, como uma sessão faz antes de ler a fila ([capítulo 14](14-queue-states.md)), e `git pull` traz os commits novos dele para o seu branch."
  * :203 (key point), en: "a remote is another copy you clone, push to and pull from;" becomes "a remote is another copy you clone, push to, fetch from and pull from;".
  * :203, pt: "um remoto é outra cópia que você clona, para a qual dá push e da qual dá pull;" becomes "um remoto é outra cópia que você clona, para a qual dá push e da qual dá fetch e pull;".
* `book/en/19-worktrees.md` and `book/pt/19-worktrees.md`, :179:
  * en: "so the line is taken in every clone, or reuses the one that exists, and writes the page there." becomes "so the line is taken in every clone, or, when the definition resumes, reuses the worktree and branch that exist, and writes the page there."
  * pt: "então a linha fica ocupada em todo clone, ou reaproveita o que existe, e escreve a página ali." becomes "então a linha fica ocupada em todo clone, ou, quando a definição é retomada, reaproveita o worktree e o branch que existem, e escreve a página ali."
* Terms of docs/03: remote, branch, worktree, claim, trunk. No new term; no docs/03 row changes: the `remote` row (:82) already says "`git fetch` brings its branches into your clone without changing yours", and chapter 18 :71 now says it in the same words.
* Sources: the finding `work/done/m24-review.md` (C1, C4, P1); chapter 12 :27 and :28 and chapter 14 :61 and :72 (fetch before reading the queue, the branch as claim, reuse on resume); chapter 18 :25 (the resume condition's wording); docs/03 :82. No footnote: the reader gains nothing to open.
* Cases: none. No number.
* Neighbouring lines on the same files, all later in queue order, which find these sentences as this delivery leaves them: M26's `ch13-19-session-folder` (chapter 19), M27's `ch12-14-18-several-slugs` (chapter 18), M28's `ch13-19-claim-script` (chapter 19). M24's parallel lines `ch08-23-fetch-taken` (chapters 8, 13, 14, 17, 23), `ch07-review-merge` (chapter 7) and `docs03-free-line-held` (docs/03's `free line` row) touch neither chapter 18 nor 19 nor the `remote` row.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* docs/03's `remote` row: true once chapter 18 :71 says what fetch does.
* Chapter 18 :27, "`git switch lend-book` instead when the branch exists": :25, two lines above, already gives the resume condition, and the review did not flag it.
* Chapters 8, 12, 14 and 17, which use `git fetch` before chapter 18: chapter 18 is where the book's git terms are defined, and `ch08-23-fetch-taken` owns those chapters' fetch sentences.
* Chapter 19 :120 to :123, the bare clone's fetch line: comes after chapter 18 and already says what it fixes.
* `git switch` and the other commands of :27, defined at :78 in the same chapter: not in the finding.

**Done when.**

* [ ] Both editions changed as the Contract says, and nothing else in the two chapters.
* [ ] `grep -n "git fetch" book/en/18-git-essentials.md book/pt/18-git-essentials.md` prints :71 (and nothing claims fetch elsewhere in the chapter).
* [ ] `grep -n "reuses the one that exists\|reaproveita o que existe" book/*/19-worktrees.md` prints nothing.
* [ ] Each chapter still opens with its value, no filler and nothing useful cut, no number added, no em dash, no run narration.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given for review.

**Decisions from the documents.**

* The remote is explained briefly at first use and in full where it is now: the author's brief for this line ("plainly, briefly, where first used") and docs/04's one sentence per line.
* Fetch is worded as docs/03's `remote` row words it, so P1 closes without editing docs/03.
* The resume condition in chapter 19 :179 uses chapter 18 :25's words ("when the definition resumes", "quando a definição é retomada") and chapter 12 :28's sense: a branch already there means the line is taken unless the definition resumes.
* Taught as the kit is at 2026.10.20, with no version or "now": AGENTS.md and the M21 rule.

**Decisions taken alone.**

* :25 glosses only the remote, not `git fetch`: the chapters say a session fetches before it reads the queue (12 :27, 14 :72), and :25 is about the check for one branch, so saying "/propose runs `git fetch`" there would claim a step the chapters do not state; fetch is defined at :71, its first use in chapter 18.
* `-u` is explained without the word "upstream", a term the book defines nowhere; "links your branch to it" says what it does for a non-developer.
* The `-u` sentence is a new line after the code block, not a clause in :27, which is already long; chapter 18's lines from :37 on shift by one.
* The key point :203 gains fetch: a sibling sentence that would go stale and belongs to no other line.
* Chapter 19 :179 names "the worktree and branch" instead of "the one", since the sentence creates both.
