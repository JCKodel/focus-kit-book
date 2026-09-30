# Worktrees and parallel agents

After this chapter you can build two deliveries at the same time in two worktrees, merge them with `--no-ff`, resolve the conflict where they meet, and catch a conflict marker before it is committed.
You can also say where parallel agents stop paying: shared files, shared resources, disk, and the one person who reviews and merges.

## What a worktree is

Every git command in this chapter is one you run: the agent runs none of them but `git worktree add`, which the clinic's `/propose` runs, and `git add`, `git status` and `git diff`, as in [chapter 17](17-git-essentials.md#commits-and-the-history).
Every excerpt comes from the guided project at its chapter tag [`book-v1/worktrees`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/worktrees), commit `699ab40`, or from the record of the run that built it.[^clinic-worktrees-run]

Your clone is at `book-v1/four-pieces`.
Between it and `book-v1/worktrees` are the kit update, the seven clinic fixes that this book's reviews queued in the clinic's milestone 1.1 (the tag's [docs/06](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/worktrees/docs/06-Queue.md) lists them), then three deliveries, `git-worktrees`, `route-errors` and `minutes-of`, and two merges.
For this chapter, run `git fetch --tags` and then `git switch -c mine18 book-v1/worktrees`, a branch of your own at the tag.
Building those lines yourself with `/propose` and `/apply` is optional; the tag is what to compare against, as in [chapter 15](15-four-pieces.md#the-four-pieces).

A worktree is an extra working folder of the same git repository, on its own branch.
The git documentation puts it this way: "*A git repository can support multiple working trees, allowing you to check out more than one branch at a time.*"[^git-worktree]
The folder you cloned is the main worktree; each one you add is linked to it and shares everything but its own checked-out files, its `HEAD` and its staging area.[^git-worktree]

Four commands cover its life:

```
git worktree add ../<folder> -b <branch> main
git worktree list
git worktree remove ../<folder>
git branch -d <branch>
```

`add` creates the folder, creates the branch at `main` and checks it out there; `list` prints each worktree with its commit and branch; `remove` deletes the folder, and refuses one with files changed or not tracked, which is how git keeps work you have not committed.[^git-worktree]
The branch outlives the folder: `git branch -d` deletes it, and only once it is merged.
Git also refuses to check out one branch in two worktrees, so two agents never write on one branch.[^git-worktree]

Against a second clone, a worktree shares one history: a commit made in the worktree is in the main folder at once, so you merge it from there with no push and no fetch.
A clone has its own copy of the history, and the two meet only through a remote.
Against switching branches in one folder, each agent has its own folder: one folder holds one branch at a time, two agents writing in it write over each other, and switching with uncommitted work needs `git stash` first.

The clinic chose this form in its delivery `git-worktrees`, which amended its [ADR-0003](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/worktrees/docs/adr/ADR-0003-git-strategy.md): the decision of trunk stays above as history, and the amendment's Decision reads:

```markdown
A worktree per delivery. `/propose <slug>` creates it from the main folder
with `git worktree add ../focus-kit-clinic-<slug> -b <slug> main`, and
writes the page and the docs/06 mark there. `/apply <slug>` runs in a fresh
session opened in that folder. The person commits the delivery on branch
`<slug>`, then from the main folder runs `git merge --no-ff <slug>` into
`main`: one merge per delivery. The person resolves any conflict, then runs
`git worktree remove ../focus-kit-clinic-<slug>` and `git branch -d <slug>`.

The agent stages and suggests the commit message. It never commits, merges,
resolves a merge conflict or removes a worktree. docs/05 §5 holds the
commands.
```

One folder per delivery, beside the clinic's own, on a branch named after the slug; one `--no-ff` merge per delivery, so it reverts in one step, as [chapter 17](17-git-essentials.md#the-four-side-by-side) showed.
Every step that changes the history is the person's: the agent never commits, merges, resolves a conflict or removes a worktree.

## Two deliveries at once

Two lines of the clinic's milestone 1.1 went first.
`route-errors` asked for one shared copy of each error answer the server's routes repeat; its `/propose` found five such answers where the line named two, and widened the line.
`minutes-of` asked for one shared parser of "HH:MM" times, whose two copies were in `weeklyHours/rules.ts` and `appointments/rules.ts`.

I started the two `/propose` sessions in the same second, both from the clinic's root, headless, with `Your call. Say what you chose and why.` as the answer to their questions, the brief of [chapter 10](10-propose.md).
Each ran `git worktree add ../focus-kit-clinic-<slug> -b <slug> main` and wrote its page and its queue mark in its worktree.
Headless, a session cannot write in an `--add-dir` folder (a second folder the session may work in) that did not exist when it started, so I made the two empty folders before starting the sessions, and `git worktree add` accepts an empty folder.
Then two `/apply` sessions, again in the same second, each started from its own worktree's root.
A worktree has no `node_modules`, since git does not track it, so each `/apply` ran `npm ci` first.
I reviewed both pages and both staged changes and sent no request, then committed each delivery on its branch, in its worktree: [`af3269a`](https://github.com/JCKodel/focus-kit-clinic/commit/af3269aecc1d2408012ad0d5c839f49decd5d8e9) with 12 files and [`948b94d`](https://github.com/JCKodel/focus-kit-clinic/commit/948b94de50e941f6f3b816889bcd604319834e4e) with 7.[^clinic-worktrees-run]

The agents' time overlapped.
The two `/propose` sessions took 128 seconds from the first start to the last end, against 177.8 seconds for their four turns added; the two `/apply` sessions took 155 seconds, against 277.2 seconds added.[^clinic-worktrees-run]

In an interactive session, open one terminal per session: one in the clinic's root for each `/propose`, one in each worktree for its `/apply`.
`/propose` writes in the sibling folder, outside the one its session started in, so the host asks you to approve that write, as [chapter 8](08-analyze.md#check-it-against-the-code) says of a permission the mode does not grant.
That last part follows from the permission mode; the run was headless and did not show it.

## Merging, and the conflict

The merge outputs in this chapter come from the run's record: `git worktree list`, the first merge and `bdb0609` below are copied from my terminal, the rest byte for byte, with paths relative to the clinic's root.[^clinic-worktrees-run]
From the clinic's root, on `main`, the two worktrees beside the main folder:

```
git worktree list
```

```text
.                               0993b68 [main]
../focus-kit-clinic-minutes-of   948b94d [minutes-of]
../focus-kit-clinic-route-errors af3269a [route-errors]
```

The first merge found nothing in its way (the lines for each file changed are left out here):

```
git merge --no-ff route-errors
```

```text
Merge made by the 'ort' strategy.
 12 files changed, 304 insertions(+), 67 deletions(-)
```

The second stopped:

```
git merge --no-ff minutes-of
```

```text
Auto-merging docs/01-Architecture.md
Auto-merging docs/06-Queue.md
CONFLICT (content): Merge conflict in docs/06-Queue.md
Automatic merge failed; fix conflicts and then commit the result.
```

A conflict is what git reports when both branches changed the same lines, or lines next to each other: git merges every other change, stops before the merge commit, and leaves the file for you.[^git-merge]
In the file, git writes both versions between conflict markers: `<<<<<<<` opens the version of the branch you are on, `=======` separates it from the merged branch's, and `>>>>>>>` closes that one.[^git-merge]
`git diff` shows them; during a merge it prints a combined diff, with two columns of `+` and `-`, the first against the branch you are on and the second against the merged branch:

```
git diff
```

```text
diff --cc docs/06-Queue.md
index ac17a76,60ea2d3..0000000
--- a/docs/06-Queue.md
+++ b/docs/06-Queue.md
@@@ -40,8 -40,8 +40,13 @@@ git-worktrees is built in its own workt
  [ ] time-zone-names      setup accepts every IANA name the runtime knows, such as US/Eastern and Etc/UTC, as docs/03 says
  [ ] slot-taken-retry     after a refused booking whose slot reload fails, "Try again" keeps the "no longer free" message and the chosen date
  [ ] routes-table         the Routes table of docs/02 renders whole, with the slots and appointments routes as rows
++<<<<<<< HEAD
 +[x] route-errors         one shared copy of each error answer routes repeat (DatabaseFailed, BadRequest, NotSignedIn, ProfessionalNotFound, ClinicNotSetUp 500); the first copies are in session.server.ts and weeklyHours/route.server.ts
 +[ ] minutes-of           one shared "HH:MM" parser; the first copy is in weeklyHours/rules.ts, the second in appointments/rules.ts
++=======
+ [ ] route-errors         one shared databaseFailed and one shared notFound answer; the first copies are in session.server.ts and weeklyHours/route.server.ts
+ [x] minutes-of           one shared "HH:MM" parser; the first copy is in weeklyHours/rules.ts, the second in appointments/rules.ts
++>>>>>>> minutes-of
  [x] booking-submit       useBooking's submit publishes its in-flight state as an update and books with the state the hook read, not a ref written during render
  [x] hours-save           useWeeklyHours' save publishes its in-flight state as an update, so a time typed just before Save survives
  [x] hours-report         the hours editor's reports reach the professionals section as one WeeklyHoursReport and one tested event; finishes what orchestrator-tests left
```

Above `=======` is `main`, which already holds `route-errors`: its line marked `[x]` with the wider text, and `minutes-of` still `[ ]`.
Below is `minutes-of`: its own line `[x]`, and `route-errors` with the text it had before.
Each branch marked its own line in the queue, and the two lines are next to each other, so git could not keep one change without the other side's version of the neighbouring line.
docs/01 changed on both branches too, `route-errors` in its `server/` listing and `minutes-of` in its `lib/` listing, lines apart: git printed "Auto-merging" and merged it alone.

The resolution keeps what both sides did: both lines, both `[x]`, and `route-errors` with its new text; the markers go.
With the file edited to that, `git diff` shows the resolution against each side:

```
git diff
```

```text
diff --cc docs/06-Queue.md
index ac17a76,60ea2d3..0000000
--- a/docs/06-Queue.md
+++ b/docs/06-Queue.md
@@@ -40,8 -40,8 +40,8 @@@ git-worktrees is built in its own workt
  [ ] time-zone-names      setup accepts every IANA name the runtime knows, such as US/Eastern and Etc/UTC, as docs/03 says
  [ ] slot-taken-retry     after a refused booking whose slot reload fails, "Try again" keeps the "no longer free" message and the chosen date
  [ ] routes-table         the Routes table of docs/02 renders whole, with the slots and appointments routes as rows
 -[ ] route-errors         one shared databaseFailed and one shared notFound answer; the first copies are in session.server.ts and weeklyHours/route.server.ts
 +[x] route-errors         one shared copy of each error answer routes repeat (DatabaseFailed, BadRequest, NotSignedIn, ProfessionalNotFound, ClinicNotSetUp 500); the first copies are in session.server.ts and weeklyHours/route.server.ts
- [ ] minutes-of           one shared "HH:MM" parser; the first copy is in weeklyHours/rules.ts, the second in appointments/rules.ts
+ [x] minutes-of           one shared "HH:MM" parser; the first copy is in weeklyHours/rules.ts, the second in appointments/rules.ts
  [x] booking-submit       useBooking's submit publishes its in-flight state as an update and books with the state the hook read, not a ref written during render
  [x] hours-save           useWeeklyHours' save publishes its in-flight state as an update, so a time typed just before Save survives
  [x] hours-report         the hours editor's reports reach the professionals section as one WeeklyHoursReport and one tested event; finishes what orchestrator-tests left
```

No marker is left: in the second column the `route-errors` line is as `main` had it, in the first the `minutes-of` line is as its branch had it.
`git add` marks the file resolved, and `git commit --no-edit` makes the merge commit with the message git prepared:

```
git add docs/06-Queue.md
git commit --no-edit
```

```text
[main 699ab40] Merge branch 'minutes-of'
```

```
git log --oneline --graph -5
```

```text
*   699ab40 Merge branch 'minutes-of'
|\  
| * 948b94d Declare minutesOf once in lib/time.ts (minutes-of)
* |   045c744 Merge branch 'route-errors'
|\ \  
| |/  
|/|   
| * af3269a Share the error answers routes repeat (route-errors)
|/  
* 0993b68 Build every delivery in its own worktree (git-worktrees)
```

Both branches start at `0993b68`, `git-worktrees`.
[`045c744`](https://github.com/JCKodel/focus-kit-clinic/commit/045c744d27acdbaee7e269e848c5de6ee696d21d) joins `route-errors`' one commit to `main`, and [`699ab40`](https://github.com/JCKodel/focus-kit-clinic/commit/699ab4008f78853810c28561110666abd2d0b823) joins `minutes-of`'s; the crossed lines in the middle are only how `--graph` draws `af3269a` and `0993b68` on separate lines.
Each delivery is one merge commit, reverted with `git revert -m 1 <merge>`.
`npm run verify` on `699ab40` passed its 336 Vitest and 144 Playwright tests.[^clinic-worktrees-run]

When you would rather not resolve now, `git merge --abort` leaves the merge and puts the branch back as it was before it.[^git-merge]

## When git commits the markers

The first time, I pasted the commands of the whole merge as one block, so these two ran right after the conflict, before I had touched the file:

```
git add docs/06-Queue.md
git commit --no-edit
```

```text
[main bdb0609] Merge branch 'minutes-of'
```

Git made the merge commit `bdb0609` with the markers in docs/06, lines 43 to 49, and said nothing.[^clinic-worktrees-run]
To git, a marker is text like any other: `git add` is how you tell it a file is resolved, and it takes your word.

The guard is one command before the merge's commit:

```
git diff --cached --check
```

It reads what is staged and reports each conflict marker as `<file>:<line>: leftover conflict marker`, and exits non-zero when it finds one.[^git-diff]
The run did not use it; exercise 18.2 has you run it.

`bdb0609` was never pushed, so the undo was to move `main` back to the commit before it, and throw it away:

```
git reset --hard 045c744
```

```text
HEAD is now at 045c744 Merge branch 'route-errors'
```

Then the same merge again, the same conflict, and the resolution of the previous section.
`bdb0609` is on no branch now, and the clinic's history does not hold it.
Reset rewrites history, so it is for commits nobody else has; once a commit is pushed, undo it with `git revert`, which is [chapter 17's rule for rebase](17-git-essentials.md#fast-forward-and-rebase).
In the record, I asked the book's agent to run that second part, against the rule that the person merges; the chapter shows git's output, and the rule stands (chapter 19).

## Where parallelism stops

Two agents in two worktrees made two deliveries in less time than one after the other; the run also showed where that stops.[^clinic-worktrees-run]

**The queue.** Every delivery marks its line in docs/06, so two deliveries in flight always touch that file, and their lines are often neighbours.
The clinic's ADR-0003 says so in its consequences: "*`docs/06` is edited by every delivery, so two deliveries in flight can conflict on neighbouring queue lines. The person resolves it by keeping both marks.*"
It is the conflict of the run, and it is always resolvable the same way.

**The same files.** `route-errors` changed 12 files and `minutes-of` 7; only docs/01 and docs/06 were in both, and docs/01 merged alone because the changes were lines apart.
Two deliveries that change the same lines of a code file conflict there, and that resolution is a decision about the code, no longer a matter of keeping both marks.
ADR-0003: "*Before building two deliveries at once, the person checks that they do not touch the same files.*"

**Shared resources.** Worktrees share the machine: the clinic's end-to-end tests start a server on port 3100 in every worktree.
`route-errors`' first `npm run verify` stopped before Playwright with `Error: http://localhost:3100/api/health is already used`, since the other worktree's run held the port; run again with no change, it passed.
ADR-0003: "*The e2e ports (3100 and 5174, in `playwright.config.ts`) and the e2e database (`e2eDatabasePath`, in the system temp folder) are shared by every worktree today.*"
The database did nothing visible in this run.
A port or a database per worktree is a project's choice, with its own delivery; the clinic has not made it.

**Disk.** Each worktree needs its own dependencies: `node_modules` took 155M in each, as much as the clinic's main folder.
ADR-0003: "*Each worktree costs a folder and its own `node_modules`.*"

**The person.** The agents' time overlapped: 155 seconds of clock for 277.2 seconds of `/apply` work.
The review did not: one person reads each page, each staged change, commits and merges, one at a time.
The run did not measure that time, so this chapter gives no number for it.

This book is on trunk for the last two reasons, shared files and one reviewer, as its ADR-0010 in [chapter 6](06-the-documents.md#adrs) says.

So you decide which deliveries run in parallel before starting them, by the files each will touch: read the line, docs/01 and the code it names, and pair deliveries whose files do not meet, except the queue.
After the clinic's run, milestone 1.1 still has three open lines to build, and exercise 18.3 has you pair two.

## Key points

* A worktree is an extra working folder of the same repository on its own branch: `git worktree add ../<folder> -b <branch> main`, `list`, `remove`, then `git branch -d`; it shares one history, and each agent writes in its own folder.
* Two agents in two worktrees overlap their time; the person merges each delivery with `--no-ff`, one merge commit each, reverted with `git revert -m 1`.
* A conflict is two branches changing the same or neighbouring lines: git stops, merges the rest, and leaves both versions between markers; keep what both did, `git add`, then commit, or leave with `git merge --abort`.
* Git commits markers without a word if you stage the file unresolved; run `git diff --cached --check` before committing a merge, and undo an unpushed bad merge with `git reset --hard`, a pushed one with `git revert`.
* Parallelism stops at the queue (always conflicts, keep both marks), files both deliveries change, shared ports and databases, a `node_modules` per worktree, and the one person who reviews and merges.

## Exercises

These exercises use your clone of the clinic at `book-v1/worktrees`, on your branch `mine18`.
They are git commands you run yourself; nothing here changes the clinic.

### Exercise 18.1

Create two worktrees from your branch, `../try-a` on `try-a` and `../try-b` on `try-b`.
In each, mark a different one of the adjacent `[ ]` lines `time-zone-names` and `slot-taken-retry` of docs/06 as `[x]`, and commit.
Merge both into `mine18` with `--no-ff`, resolve the conflict, and read `git log --oneline --graph`.

### Exercise 18.2

Go back to before the second merge with `git reset --hard`, repeat it, stage the file with its markers, run `git diff --cached --check`, and say what it prints and why nothing is committed yet.
Then run `git merge --abort`, remove both worktrees and delete both branches: say why `git branch -d` refuses one of them, and what deletes it.

### Exercise 18.3

From the tag's docs/06, pick two open lines of milestone 1.1 that two agents could build at the same time, name the files each would touch, from docs/01 and the code, and say which conflicts you would still expect.

[^git-worktree]: Git, "git-worktree", the documentation, accessed 2026-09-30. <https://git-scm.com/docs/git-worktree>
[^clinic-worktrees-run]: This book's run of the guided project's parallel deliveries, 2026-09-30, with Claude Code 2.1.286 and the model `claude-opus-5-5`: every turn of `git-worktrees`, `route-errors` and `minutes-of`, the times, the merges in `merges.txt`, and the `npm run verify` output on the clinic's commit `699ab40` in `verify.txt`. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/clinic-worktrees-run/README.md>
[^git-merge]: Git, "git-merge", the documentation, section "How conflicts are presented" and option `--abort`, accessed 2026-09-30. <https://git-scm.com/docs/git-merge>
[^git-diff]: Git, "git-diff", the documentation, option `--check`, accessed 2026-09-30. <https://git-scm.com/docs/git-diff>
