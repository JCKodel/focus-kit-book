# clinic-worktrees

**Objective.** The guided project works on a worktree per delivery from now on, and chapter 18 has a real parallel run to quote: two clinic deliveries proposed and built by two agents at the same time in two worktrees, merged by the author with `--no-ff`, conflict included, all recorded. No chapter.

**Behaviour.**

* The clinic's ADR-0003 and the Git slot of its docs/05 say a worktree per delivery, for good, in a clinic delivery `git-worktrees` built on trunk by a recorded run, so the kit makes the switch and nothing in the clinic is edited by hand.
* Two recorded `/propose` sessions, for the clinic's M1.1 lines `route-errors` and `minutes-of`, run at the same time from the clinic's root; each creates its worktree, `../focus-kit-clinic-<slug>` on a branch named after the slug, and writes its page there; the record shows the two sessions' times overlap.
* Two recorded `/apply` sessions run at the same time, each from its worktree's root, with the e2e ports (3100, 5174) and the e2e database in `tmpdir()` shared as the clinic has them today; whatever that sharing does (a port in use, a database removed by the other run, nothing) is recorded as it happened, not prevented.
* The author commits each delivery on its branch, in its worktree, then merges `route-errors` and then `minutes-of` into `main` with `git merge --no-ff` from the clinic's root, and resolves any conflict by hand; the two lines are adjacent in the clinic's docs/06, so a conflict on the queue is expected, and whatever happens is recorded byte for byte.
* After the merges, `npm run verify` is green on the clinic's `main`, the two worktrees are removed and their branches deleted, and `main` is pushed.

**Contract.**

Run from the clinic, `../focus-kit-clinic`, kit `bff8414` (installed at `a3e2470`). Recipe: docs/05 §5 "A recorded clinic run", with the changes below. Common flags as docs/05.

1. Before the run: the book's `main` with only this page's `/propose` changes uncommitted (chapter 17 committed first); `make verify` green. The clinic on `main`, clean, equal to `origin/main`. A throwaway check, in a scratchpad repository and never in the clinic, with step 3's exact flags: does `claude -p` accept `--add-dir` naming a directory that does not exist yet, can the session run `git worktree add -b t ../t` there (the host's Bash sandbox may refuse a sibling folder), and does `acceptEdits` then let it write in `../t`? The answer goes in the README; if either is no, the run stops and the author decides.
2. `git-worktrees`, on trunk, the five steps of docs/05 as they are, `/propose` with this brief as its first answer, word for word:
   > The clinic's git strategy becomes a worktree per delivery, for good: amend ADR-0003 and the Git slot of docs/05. Each delivery's worktree is the sibling folder ../focus-kit-clinic-<slug>, on a branch named after the slug. The owner commits the delivery on its branch and merges it into main with git merge --no-ff, one merge per delivery, and resolves any conflict; the agent never commits or merges.
   Every further round of questions: `Your call. Say what you chose and why.` The author commits on `main` and pushes before step 3.
3. Before it, the author creates the two empty folders `../focus-kit-clinic-<slug>` by hand, recorded, since step 1's check found that `--add-dir` naming a folder that does not exist yet lets the worktree be created but not written (decided by the author at `/apply`). `/propose route-errors` and `/propose minutes-of`, fresh, headless, detached (`nohup`), started together from the clinic's root, flags as step 1 of docs/05 plus `--add-dir ../focus-kit-clinic-<slug>` and `--allowedTools "Bash(git worktree *)" "Bash(git branch *)" "Bash(git log *)" "Bash(git rev-parse *)" "Bash(git add *)" "Bash(git status *)" "Bash(git diff *)"`: the kit names no command for creating the worktree, so the list covers the forms an agent may use and the read-only calls it orients with, since one denied call can leave the page in the main checkout and cost a run. Answers: `Your call. Say what you chose and why.` Page review as step 2 of docs/05, one session per page.
4. `/apply route-errors` and `/apply minutes-of`, fresh, headless, detached, started together, each from its worktree's root, flags and allowlist as step 3 of docs/05. Staged review as step 4.
5. Every later turn of a session goes by `--resume <its session id>`, never `--continue`: the two `/propose` sessions share a directory (m3-review's lesson).
6. The author, by hand, commands recorded: `git commit` in each worktree with the kit's message; from the clinic's root `git worktree list`, `git merge --no-ff route-errors`, `git merge --no-ff minutes-of`; on a conflict, `git status`, the conflicted hunk of each file, the resolution, `git add` and `git commit`; `git log --oneline --graph` of the merged range; `git worktree remove` for each; `git branch -d` for each; `git push`. No tag: not a chapter (docs/05 §5); chapter 18's `/propose` decides its tag.
7. Exits as docs/05, plus: a run whose worktree `/propose` did not create (with `git worktree add` in the empty folder of step 3) stops the delivery; the author decides a second run.

The record, `work/done/clinic-worktrees-run/`, as docs/05 §5, plus:

* README: the `--add-dir` check; per session its start and end time and the `duration_ms` and usage of its stream-json `result` line, so the overlap and the wall time against the sum can be read; what the shared e2e ports and database did; the time and disk size of each worktree's `npm ci`, the cost behind the kit's "a directory per delivery".
* `git-worktrees/`, `route-errors/`, `minutes-of/`: `turn-N.txt` per turn, as docs/05.
* `merges.txt`: every command of step 6 and its output byte for byte, run in a terminal as the author runs it; conflicted hunks with their markers as git wrote them.
* `verify.txt`: `npm run verify` on the clinic's `main` after the merges.

Documents of the book: docs/05 §5 "Guided project" says the clinic is on a worktree per delivery since this delivery, the author commits on the branch and merges `--no-ff`, and a recorded run's `/apply` starts from the worktree's root with later turns by `--resume`. docs/06: a new line `clinic-worktrees` in M5 before `worktrees` (this `/propose`), `[x]` by `/apply`. No docs/03 term: "conflict" enters with chapter 18's `/propose`. No ADR in the book (ADR-0010, trunk, stays).

**Out of scope.**

* Chapter 18: its own `/propose` after this run, from the record.
* Chapter 17's "The clinic and this book, one person each, are on trunk", true at `book-v1/four-pieces` and false on the clinic's `main` after step 2: chapter 18's delivery amends it in both editions.
* Making the e2e ports or database per worktree: the sharing is what the run observes; a fix is a clinic delivery after it, if the author wants one.
* The clinic's other M1.1 lines and `m1.1-review`: not part of the pair.
* A squash merge, a rebase or a pull request: `--no-ff` from the local clinic, so the graph shows two lines joining (chapter 17's table); pull requests are chapter 20.
* The host's own worktree flag, if any: the kit creates the worktree with git on any host; chapter 18 may cite host docs.
* The book's git strategy: trunk (ADR-0010).

**Done when.**

* [x] The `--add-dir` check answered and recorded.
* [x] `git-worktrees` committed and pushed on the clinic's `main`; ADR-0003 and docs/05's Git slot say a worktree per delivery.
* [x] Both `/propose` sessions created their worktrees and pages, with overlapping times; pages reviewed.
* [x] Both `/apply` sessions ran with overlapping times; staged changes reviewed; each committed on its branch.
* [x] Both branches merged with `--no-ff`, conflicts resolved by the author, all in `merges.txt` (the redone merge's resolution by the book's session, at the author's request).
* [x] `npm run verify` green on the clinic's `main` (`verify.txt`); worktrees removed, branches deleted, pushed.
* [x] Record complete, no session id, no absolute path; host notes outside the repositories deleted.
* [x] Book docs/05 updated; `make verify` green; docs/06 `[x]`, page in `work/done/`, staged, commit message suggested.

**What happened.**

* The `--add-dir` check answered no on its third question: `claude -p` starts with a folder that does not exist yet and `git worktree add` creates it, but a Write there is denied. An explicit `Write(...)` rule does not help; an empty folder made before the session does, and so does `--resume` once the folder exists. The author chose the empty folders, made by hand before step 3; Contract steps 3 and 7 say so. docs/05 §5 now carries it as a rule of the recipe.
* Chapter 17 was committed by the author before the run (`2625c6f`); the book's `make verify` was green.
* `git-worktrees`: `/propose` first added a line `parallel-verify` and a rule of one worktree at a time for verify and dev; the page review dropped both, since they would have prevented what this run records, and kept the shared ports and database as a fact in ADR-0003's amendment. A second request put back a newline the first edit had lost. `/apply` renamed ADR-0003 to `ADR-0003-git-strategy.md` with an amendment and rewrote the Git slot of docs/05. Committed and pushed by the author, `0993b68`.
* Both `/propose` sessions started in the same second, each created its worktree with `git worktree add` in its empty folder and wrote its page there. `route-errors` widened its line from two error answers to five. Both `/apply` sessions started in the same second, from their worktrees; each ran `npm ci` (766 ms and 155M for `minutes-of`; the same 155M for `route-errors`, whose time the agent cut from its output). Wall time 155 s against 277 s of `duration_ms` added.
* The shared e2e ports did something: `route-errors`' first verify stopped before Playwright on port 3100 in use, held by the other run, and passed when run again. The shared e2e database did nothing visible.
* The merges: `route-errors` clean; `minutes-of` conflicted on the two adjacent queue lines, as expected, while docs/01, changed in both, merged alone. The author pasted the commands as one block, so the merge was committed with the conflict markers (`bdb0609`, never pushed). The author decided to undo and redo it and delegated the rest of step 6 to the book's session, bending, at the author's explicit request, docs/05 §5's "never commits, tags or pushes" and the clinic's new rule that the agent never commits, merges, resolves a conflict or removes a worktree: `git reset --hard 045c744`, the merge again, the resolution before `git add`, `699ab40`. For chapter 18: git commits the markers without a word.
* The `script` recording lost the echo of the commands; `merges.txt` part 1 is the terminal's text the author copied, prompts written `$ ` and paths made relative.
* `npm run verify` green on the clinic's `main` at `699ab40`: 336 Vitest (328, plus 5 and 3), 144 Playwright. Worktrees removed, both branches deleted by `-d`, pushed `0993b68..699ab40`.
* Host: no note appeared; each worktree got a host folder of its own holding only its transcript, which outlives the worktree. The throwaway check's host folder was deleted.
* Dropped: nothing. No docs/03 term, no ADR in the book.

