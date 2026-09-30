# clinic worktrees run

The guided project switched from trunk to a worktree per delivery, then two of its deliveries, `route-errors` and `minutes-of`, were proposed and built by two agents at the same time in two worktrees and merged into `main` with `--no-ff`, conflict included. The delivery that planned and recorded it is `../clinic-worktrees.md`; the format is docs/05 §5, "A recorded clinic run", with the changes that page lists.

* Host: Claude Code, `claude --version` printed `2.1.286 (Claude Code)`; macOS 26 (Darwin 25.6.0), arm64.
* Model: `claude-opus-5-5`, given with `--model` on every turn.
* Kit: focus-kit `bff8414`, as installed; not updated. The clinic's `.claude/` has not changed since `a3e2470`, "Update focus-kit to bff8414".
* The clinic's first commit: `36d7ad930d5c96bd6dbc87924384ebaed42bc7e1`, "Leave "saving" out of the weekly hours answer's report type (hours-answer)"; the clinic was on `main`, clean, equal to `origin/main`.
* The clinic's last commit: `699ab40`, "Merge branch 'minutes-of'", pushed; no tag.
* Date: 2026-09-30.

## The `--add-dir` check

Run before anything else, in a throwaway repository in the host's scratch folder with one commit on `main`, never in the clinic, with step 3's flags: the common flags, `--add-dir ../t` and the seven `--allowedTools` patterns. The prompt asked the session to run `git worktree add -b t ../t` and then write `../t/hello.txt` with the Write tool.

* `claude -p` accepts `--add-dir` naming a folder that does not exist yet: yes, it starts and runs.
* `git worktree add -b t ../t` from the session: yes, the host's sandbox let it create the sibling folder.
* A Write in `../t` under `acceptEdits`: no. It was denied, "It requires approval, and this session has no approval surface".

Three more tries, to find the cause for the author:

* The same Write, with `../t` already there when the session started: written.
* `../t` absent at the start, with `"Write(../t/**)" "Edit(../t/**)"` added to `--allowedTools`: denied again.
* `--resume` of the session that created the worktree, `../t` now there: written.
* An empty `../t` made before the session, which then ran `git worktree add -b t ../t` in it (git accepts an empty folder) and wrote: written, nothing denied.

So a session cannot write in an `--add-dir` folder that did not exist when it started. A first try had a stray ` .` in the prompt, and git answered `fatal: invalid reference: .`; it was the prompt's fault and was run again. A detached `nohup` session outlived the shell that started it and wrote its whole stream. The host's folder for the throwaway repository was deleted afterwards.

The author decided: before the two `/propose` sessions, the author creates the two empty folders by hand, and `/propose` still creates the worktree in its folder with git. The book's page, Contract steps 3 and 7, says so.

## The commands

Common flags, on every turn:

```
--model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose
```

Every turn was started by the book's `/apply` session through its shell: `nohup` with standard input from `/dev/null`, output to a file, the start and end times written in UTC around the `claude` process. Every later turn of a session went by `--resume <its session id>`; `--continue` was never used.

* `git-worktrees`: `/propose` from the clinic's root with the common flags; `/apply` from the clinic's root with the common flags and the allowlist of docs/05 §5 step 3.
* `/propose route-errors` and `/propose minutes-of`, started together from the clinic's root, each with the common flags plus:

  ```
  --add-dir ../focus-kit-clinic-<slug> --allowedTools "Bash(git worktree *)" "Bash(git branch *)" "Bash(git log *)" "Bash(git rev-parse *)" "Bash(git add *)" "Bash(git status *)" "Bash(git diff *)"
  ```

* `/apply route-errors` and `/apply minutes-of`, started together, each from its worktree's root, with the common flags plus:

  ```
  --disallowedTools "Bash(npm run dev*)" --allowedTools "Bash(npm *)" "Bash(npx *)" "Bash(node *)" "Bash(mkdir *)" "Bash(cp *)" "Bash(git add *)" "Bash(git status *)" "Bash(git diff *)"
  ```

* The author decided before the run: page reviews and staged reviews send a request only for a real hole against the book's page, otherwise "none", as in the M4.2 loop; the commits, merges and the rest of step 6 are the author's, recorded with `script` in a terminal.
* After the merge committed with its markers, the author asked the book's session to run the rest of step 6, so it ran in the clinic `git reset --hard`, the merge, the conflict resolution with the editor, `git commit`, `git worktree remove` twice, `git branch -d` twice and `git push` (see Merges). That bends docs/05 §5 "Guided project", which says the agent never commits or pushes in the guided project, and the clinic's new docs/05, which says the agent never commits, merges, resolves a conflict or removes a worktree; it was the author's explicit request. Nothing else in the clinic was edited by hand.
* Every turn ended with a result of `success`, and every `claude` process exited with code 0; standard error held only `stty: stdin isn't a terminal`.

## Sessions and times

UTC. `duration_ms` and usage come from each turn's stream-json `result` line; usage is input, cache creation, cache read and output tokens.

| Turn | Start | End | `duration_ms` | Input | Cache creation | Cache read | Output |
|---|---|---|---|---|---|---|---|
| git-worktrees 1, `/propose` | 20:04:14 | 20:04:57 | 42052 | 12 | 20821 | 128877 | 3764 |
| git-worktrees 2, brief | 20:05:04 | 20:05:14 | 9255 | 2 | 2607 | 31162 | 785 |
| git-worktrees 3, `Your call` | 20:05:21 | 20:06:13 | 50676 | 10 | 6877 | 181676 | 5179 |
| git-worktrees 4, page review | 20:06:28 | 20:06:45 | 16226 | 6 | 2969 | 125642 | 1915 |
| git-worktrees 5, correction | 20:06:51 | 20:07:02 | 9369 | 8 | 1678 | 176771 | 663 |
| git-worktrees 6, `/apply` | 20:07:07 | 20:08:43 | 95961 | 34 | 23537 | 480802 | 7769 |
| route-errors 1, `/propose` | 20:14:56 | 20:15:50 | 53000 | 14 | 41962 | 217205 | 5006 |
| minutes-of 1, `/propose` | 20:14:56 | 20:15:29 | 32255 | 14 | 27690 | 164797 | 2812 |
| route-errors 2, `Your call` | 20:16:00 | 20:17:04 | 63384 | 12 | 12863 | 353218 | 6552 |
| minutes-of 2, `Your call` | 20:16:00 | 20:16:30 | 29191 | 6 | 3728 | 121161 | 3211 |
| route-errors 3, `/apply` | 20:17:26 | 20:20:01 | 154110 | 46 | 44197 | 946008 | 14513 |
| minutes-of 3, `/apply` | 20:17:26 | 20:19:30 | 123086 | 32 | 25984 | 462361 | 7452 |

* The two `/propose` sessions overlap on both turns: each pair started in the same second. From the first start to the last end, 20:14:56 to 20:17:04, is 128 seconds; their four `duration_ms` add up to 177.8 seconds.
* The two `/apply` sessions overlap: started in the same second, 155 seconds from start to the last end, against 277.2 seconds for the two `duration_ms` added.

## What the shared e2e ports and database did

* `route-errors`' first `npm run verify` passed typecheck, lint and 333 Vitest tests, then stopped before Playwright: `Error: http://localhost:3100/api/health is already used, make sure that nothing is running on the port/url or set reuseExistingServer:true in config.webServer.` The other worktree's e2e run held the port. Its `lsof` to see what held port 3100 was denied. It ran verify again with no change, and it passed: 333 Vitest, 144 Playwright.
* `minutes-of`'s verify passed on its first run: 331 Vitest, 144 Playwright.
* The shared e2e database in the system temp folder did nothing visible: no test failed on it.

## `npm ci` in each worktree

Each worktree starts with no `node_modules`, and each `/apply` ran `npm ci` itself, as the clinic's new docs/05 says.

* `minutes-of`: npm printed `added 54 packages, and audited 55 packages in 766ms`.
* `route-errors`: the agent kept only the last five lines of the output, and the time was not among them.
* Disk: `du -sh node_modules` gave 155M in each worktree, the same as the clinic's main folder. That is the cost behind "each worktree costs a folder and its own `node_modules`", now in the clinic's ADR-0003.

## git-worktrees

On trunk, the five steps of docs/05 §5, with `--resume` for every later turn.

* `/propose`: turn 1 (`/propose git-worktrees`) read the documents and `playwright.config.ts` and asked one round of five questions: scope (the documents only, or ports per worktree too), how a worktree gets its ports, where worktrees live, how a delivery reaches `main`, and where the line goes. Turn 2 was the brief, word for word:

  ```
  The clinic's git strategy becomes a worktree per delivery, for good: amend ADR-0003 and the Git slot of docs/05. Each delivery's worktree is the sibling folder ../focus-kit-clinic-<slug>, on a branch named after the slug. The owner commits the delivery on its branch and merges it into main with git merge --no-ff, one merge per delivery, and resolves any conflict; the agent never commits or merges.
  ```

  It asked a second round (ports in or out; where the line goes). Turn 3 was `Your call. Say what you chose and why.`; it wrote the page and put two lines in milestone 1.1: `git-worktrees` `[>]` and a new `parallel-verify` `[ ]` for ports and database per worktree, with the rule "only one worktree at a time runs verify or dev" in docs/05.
* Page review: turn 4, one request, since the new line and the rule would have kept the two `/apply` sessions from running verify at the same time, which the book's page records and does not prevent, word for word:

  ```
  Drop parallel-verify: remove its line from docs/06, its clause from the milestone paragraph, its Out of scope entry and the rule that only one worktree at a time runs verify or dev. Whether the shared ports and e2e database need a fix is decided after worktrees have been used in parallel, not now. Keep only the fact, as a consequence in ADR-0003's amendment: the e2e ports and the e2e database are shared by every worktree today.
  ```

  It did, and its edit that removed the line also removed the newline after `git-worktrees`, joining it to `time-zone-names`. Turn 5, word for word:

  ```
  In docs/06 the git-worktrees line and the time-zone-names line are now one line: the newline between them was lost. Put each on its own line again.
  ```

* `/apply`: turn 6. It renamed ADR-0003 to `ADR-0003-git-strategy.md` with an amendment (the trunk decision kept as history; a worktree per delivery, `git worktree add ../focus-kit-clinic-<slug> -b <slug> main` from the main folder; the person commits, merges `--no-ff`, removes the worktree, deletes the branch), rewrote docs/05 §2, §5 Git, §5 local and §6, marked the line, ran `npm run verify` green (328 Vitest, 144 Playwright), moved the page and staged.
* Staged review: none.
* Denied calls, two: a chain ending in `git mv` of the ADR, which it did with Write and `rm`; a chain with `sed -i` that marked the queue, which it did with Edit.
* Diverged: git stages the ADR as a delete and an add, not a rename, because the amendment more than doubles the file; the page says so. The suggested message carried a `Co-Authored-By` trailer, the first run to print one; the author committed it as printed.
* Commit: `0993b68`, "Build every delivery in its own worktree (git-worktrees)", by the author on `main`, pushed before the next step.

## route-errors

* `/propose`: turn 1 read the documents and the five route files, found five error answers repeated, not two, and asked one round of five questions (every repeated answer or only the two of the queue line; inline copies; where the shared file goes; the name; a test). Turn 2, `Your call`: it chose all five recommendations, created the worktree with `git worktree add ../focus-kit-clinic-route-errors -b route-errors main` in the empty folder, wrote the page there and widened its queue line to the five answers.
* Page review: none.
* `/apply`: turn 3, from the worktree's root. It found no `node_modules`, ran `npm ci`, wrote `src/server/answers.server.ts` with five functions and its test, changed the six route and session files, updated docs/01, docs/02 and docs/06, ran verify twice (above), moved the page and staged.
* Staged review: none. Twelve files, as its page's table says.
* Denied calls, five: two shell loops with a brace or `$` expansion that printed the route files, which it read with Read; `npm run verify` into a log file with `$?`; `lsof` on the e2e ports; a chain of `mkdir` and `git mv` to move the page, which it did with a plain `mv`.
* Commit: `af3269a`, "Share the error answers routes repeat (route-errors)", by the author on the branch, in its worktree.

## minutes-of

* `/propose`: turn 1 found the two identical copies of `minutesOf` and asked two questions (the file name; what moves). Turn 2, `Your call`: `src/lib/time.ts`, only `minutesOf`, a plain number; it created the worktree the same way and wrote the page there.
* Page review: none.
* `/apply`: turn 3, from the worktree's root. It ran `npm ci`, wrote `src/lib/time.ts` and three tests, removed the two copies, updated docs/01's `lib/` listing, ran verify green on the first run, moved the page and staged.
* Staged review: none. Seven files.
* Denied calls, two: `npm ci` chained with `$?` and Vitest, which it ran as a plain `npm ci`; a Python heredoc chained with `sed -i` that wrote "What happened", which it did with Edit and a plain `mv`.
* Commit: `948b94d`, "Declare minutesOf once in lib/time.ts (minutes-of)", by the author on the branch, in its worktree.
* Both clinic pages leave "Manual check by the person" unticked; this run has no manual check.

## Merges

`merges.txt`, in two parts.

* Part 1, the author, in a terminal under `script`: the two commits, `git worktree list`, `git merge --no-ff route-errors` (clean) and `git merge --no-ff minutes-of`, which stopped on a conflict in `docs/06-Queue.md`, the two adjacent lines as expected: each branch had marked its own line `[x]` and left the other `[ ]`, and `route-errors` had also rewritten its line's text. The commands were pasted as one block, so `git add` and `git commit --no-edit` ran before the conflict was resolved: git made the merge `bdb0609` with the markers in docs/06, lines 43 to 49, and said nothing. Nothing was pushed.
* The author decided to undo that merge and redo it, and asked the book's session to run the rest.
* Part 2, the book's session: `git reset --hard 045c744`, the merge again, the same conflict, the resolution with the editor (both lines kept, both `[x]`, `route-errors` with its new text), `git diff` of the resolution, `git add`, `git commit --no-edit` (`699ab40`), the graph, then `npm run verify`, `git worktree remove` for each, `git branch -d` for each (both deleted, since `--no-ff` left them merged) and `git push` (`0993b68..699ab40`).
* `docs/01-Architecture.md` changed in both branches, in the `server/` and `lib/` listings, and git merged it alone.
* The `script` recording lost the echo of the commands, which the shell redraws; part 1 is the terminal's text as the author copied it, with the prompt written `$ `, paths made relative to the clinic's root and the columns of `git worktree list` realigned after that; part 2 is byte for byte, with the same paths made relative. `bdb0609` is on no branch.

## Host notes

The host's auto-memory folder for the clinic was empty before and after. Its folder for the clinic gained only the transcripts of the three sessions started there; each worktree got a folder of its own, keyed by its path, holding only its `/apply` transcript, and those folders outlive `git worktree remove`. Nothing was deleted, since none is a note.

## Files

```
README.md                 this file
git-worktrees/turn-N.txt  every turn, in order
route-errors/turn-N.txt   turns 1 and 2 /propose, turn 3 /apply
minutes-of/turn-N.txt     the same
merges.txt                step 6, commands and output
verify.txt                npm run verify on the clinic's main after the merges, 699ab40
```

The turn files are derived from each turn's stream: text blocks byte for byte, tool calls as `[tool <name>] <path or command>`. Absolute paths are removed, so paths are relative to the root the session started in (the clinic's root, or the worktree's root for `/apply`). Session ids are left out. In `verify.txt` the terminal colours are removed and the clinic's folder became `.`.
