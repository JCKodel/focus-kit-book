# ch21-hidden-folder

**Objective.** After chapter 21 a reader who chooses a worktree per delivery builds the container with the hidden folder `.focus-kit/` and the branch prefix `focus-kit/`, the names the kit gives when the Git slot names none, knows the two names say what made them, and reads no name of any tool that plants the kit anywhere in the book.

**Behaviour.**

* A reader following "The life of a worktree" on the lending library runs `git clone --bare <url> .focus-kit/repo.git`, creates `library/main/` from it, and adds `return-book`'s worktree at `library/.focus-kit/worktrees/return-book` on the branch `focus-kit/return-book`; `git worktree list` prints paths with `.focus-kit/`.
* A reader whose docs/05 Git slot names `.wt/` and `wt/` gets `.wt/worktrees/return-book/` on `wt/return-book`, as the chapter already says; a slot that names neither means `.focus-kit/` and `focus-kit/`.
* A reader who finds a folder `.focus-kit/` in a colleague's project knows from its name what made it; that is the reason chapter 21 gives for the default, in the present.
* Failure: a reader searching the book for `.face/` or `face/` finds nothing in either edition, including the conflict markers block, the key points and docs/03.
* The conflict example still ends on `>>>>>>> focus-kit/overdue-list`, and the trap section's commands still name the delivery branch with the new prefix.
* A reader of chapter 21's gain still reads the two errors the one shape prevents, now without a tool's folder as the example: a page written in a worktree made somewhere the kit did not say, and copied to the main branch by hand.

**Contract.**

* **Chapter 21, both editions, file name, title and headings kept.** Every `.face/` becomes `.focus-kit/` and every `face/` prefix becomes `focus-kit/`: the two bullets of "How it solves the problem"; "The life of a worktree" (the container paragraph, `git clone --bare`, `cd`, the `(bare)` line, the `git worktree add` block and its explanation, `git merge --no-ff`, `git worktree remove`, `git branch -d`); "Worktrees in the kit" (the slot sentence, which keeps the `.wt/` example); the conflict block's `>>>>>>>` line; the key point. Fourteen occurrences per edition today; the delivery counts them again before and after.
* **Chapter 21, "Worktrees in the kit"**, the slot sentence gains the reason, in the present: the two names say what made the folder and the branch, so a person who finds them in a project knows where they came from. One sentence.
* **Chapter 21, "Worktrees in the kit"**, the last paragraph ("One shape for every tool and every person prevents an error: when nothing says where a delivery's worktree belongs, a `/propose` running in the background enters a worktree its host made on its own, in the host's folder, and the person copies the page to the main branch by hand.") is rewritten to say the same without "its host made on its own, in the host's folder": when nothing says where a delivery's worktree belongs, a session makes one wherever it stands, and the page it writes there is copied to the main branch by hand. "What the team gains" keeps its matching sentence with the same wording change.
* **Width:** every block stays within 74 columns after the rename (`.focus-kit/worktrees/return-book` is longer than `.face/worktrees/return-book`); a line that would exceed it is wrapped with `\` as the `git worktree add` block already does.
* **Portuguese:** `biblioteca/.focus-kit/worktrees/devolver-livro` and `focus-kit/devolver-livro`; `.focus-kit/` and `focus-kit/` are not translated (a folder and a branch name the kit fixes).
* **Terms:** docs/03's `container folder` row names `.face/`, `face/` as its example; `kit-2026-10-16-2` changes it to `.focus-kit/`, `focus-kit/`. If that line is not `[x]` first, this delivery changes the row.
* **Sources:** SETUP.md's docs/05 §5 Git slot and §5's worktree strategy (the names and "a slot that names neither"); the kit's changelog paraphrased with no note, present tense, no version, for the reason the names carry.
* **Cases:** none; the `[^parallel-run]` run and its numbers are unchanged, since the run's record keeps its own paths.
* **Code examples:** the existing command blocks, renamed.

**Out of scope.**

* The book's repository adopting a worktree per delivery: trunk (docs/05 §5).
* The recorded run `work/done/*-run/` behind `[^parallel-run]`: a record, not the book; its paths stay as they were run.
* Chapter 20's git strategies and chapter 10's Git slot: they name no folder.
* Chapter 11's migration of a Git slot that names no folder: `ch11-update-2026-10-16-2`.
* Any cut of chapter 21's length: `ch20-21-git-cut`.

**Done when.**

* [x] Chapter 21 changed in both editions, same headings; it still opens with its value; no filler and nothing useful cut.
* [x] `grep -rn "\.face/\|\bface/" book/ docs/03-Domain.md` finds nothing; `grep -c "focus-kit/" book/en/21-worktrees.md` equals the count of `.face/` plus `face/` before the change, recorded on this page.
* [x] Every code block of chapter 21 fits 74 columns in both editions.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* Trunk, no branch: docs/05 §5 Git.
* The two names and "a slot that names neither": SETUP.md's Git slot and worktree strategy.
* No tool that plants the kit named anywhere, and the host-made-worktree sentence rewritten rather than cut: the kit names none (changelog), and docs/04 asks that a rule's reason be the error it prevents, said in the present; the error stays, the tool goes.
* The reason the names carry said in one sentence where the default is introduced: docs/04, say it where the doubt is born.
* docs/03's row left to `kit-2026-10-16-2`, with this delivery as fallback: the row is a process document's and that delivery migrates them all.

**Decisions in the review.**

* None.

**What happened.**

* Built: chapter 21 in both editions, headings unchanged; every `.face/` became `.focus-kit/` and every `face/` prefix `focus-kit/` (the two bullets of "How it solves the problem", "The life of a worktree", the slot sentence, the conflict block's `>>>>>>>` line, the key point); "Worktrees in the kit" gains one sentence after the slot sentence, "The kit's two names say what made the folder and the branch, so a person who finds them in a project knows where they came from."; its last paragraph and the matching sentence of "What the team gains" no longer name a host's folder: a session makes a worktree wherever it stands, and the page written there is copied to the main branch by hand.
* Counted before, per edition: 15 `.face/` and 9 `face/` prefixes, 24 occurrences on 18 lines. After: `grep -o "focus-kit/" book/en/21-worktrees.md | wc -l` is 24 and `grep -c "focus-kit/"` is 18 lines, the same in Portuguese; the reason sentence names no folder, so the counts match.
* docs/03: the `container folder` row already names `.focus-kit/`, `focus-kit/`, as `kit-2026-10-16-2` left it; unchanged.
* Width: `awk` over every code block of both chapters 21 prints no line over 74 columns; the longest, `git worktree add ../.focus-kit/worktrees/devolver-livro \`, is 56.

**Divergences.**

* The Contract says fourteen occurrences per edition; the count is 24 on 18 lines, as the Contract asked to recount. Done when's `grep -c` counts lines, so both counts are recorded above.
* The reason sentence opens with "The kit's two names" (pt: "Os dois nomes do kit") rather than "the two names", since the sentence before it names `.wt/` and `wt/` too.

**Proof.** `grep -rn "\.face/\|\bface/" book/ docs/03-Domain.md` finds nothing; `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the author's review of chapter 21.

```commit
docs(ch21-hidden-folder): the kit's hidden folder and branch prefix

- chapter 21: .focus-kit/ and focus-kit/ in every command and example
- chapter 21: the two names say what made them
- chapter 21: the one-shape error said without a host's folder
work/done/ch21-hidden-folder.md
```
