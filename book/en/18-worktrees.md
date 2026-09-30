# Worktrees and parallel agents

After this chapter you can have two agents build two deliveries at the same time, each in its own folder, so that each commit holds one delivery and nothing else.
You can also merge both back, resolve the conflict when they touched the same lines, catch a conflict marker before it is committed, and say when working in parallel stops paying.

## The problem: one folder, two jobs

An agent takes minutes to build a delivery, and while it works you wait.
The natural move is to start a second agent on the next delivery, and in one folder that goes wrong in one of two ways.

If both agents work on the same branch, their changes land in the same folder.
`git status` shows the two deliveries mixed, and a commit takes both: one commit with two deliveries, one of them perhaps half done, which no single `git revert` can undo apart.
The unit of work of [chapter 17](17-git-essentials.md#the-four-side-by-side), one delivery that reverts in one step, is gone, and separating the two afterwards means picking changes file by file, line by line, by hand.

If you give each delivery its own branch, the folder still holds only one branch at a time.
Switching branches while an agent has work not yet committed either carries that work to the other branch or makes git refuse until you put it aside with `git stash`; and two agents cannot be on two branches of one folder at the same moment.

A second clone of the repository gives each agent its own folder, but each clone has its own copy of the history: the two meet only by pushing to a remote and fetching from it, and every clone repeats the whole history on disk.

What you want is several folders, each on its own branch, sharing one history.
That is a worktree.

## What a worktree is

A worktree is an extra working folder of the same git repository, checked out on its own branch.
In the words of the git documentation: "*A git repository can support multiple working trees, allowing you to check out more than one branch at a time.*"[^git-worktree]

The folder you cloned is the main worktree.
It holds the `.git` folder, where the history lives: the commits, the branches and the tags.
`git worktree add` creates another folder, checks a branch out in it, and leaves there a small `.git` file that points back to the main one.
All worktrees share the history; each has its own files, its own `HEAD` (the commit it is on) and its own staging area.[^git-worktree]
So a commit made in one worktree is visible at once from every other, with no push and no fetch, while what you change or stage in one never appears in another.
Git also refuses to check out one branch in two worktrees, so two folders never write to the same branch.[^git-worktree]

This is the guided project with two deliveries in progress, `route-errors` and `minutes-of`, as `git worktree list` printed it from the main folder:[^clinic-worktrees-run]

```text
.                               0993b68 [main]
../focus-kit-clinic-minutes-of   948b94d [minutes-of]
../focus-kit-clinic-route-errors af3269a [route-errors]
```

Three folders, one repository: the main folder on `main`, and beside it one folder per delivery, each on a branch named after the delivery, each line with the commit its branch is on.

## How it solves the problem

Give each delivery its own worktree, and each agent its own folder:

* The agent building `route-errors` works in `../focus-kit-clinic-route-errors`, on the branch `route-errors`; its `git status` shows only that delivery's changes, and the commit you make there holds that delivery and nothing else.
* The agent building `minutes-of` does the same in its own folder, at the same time.
* Nobody switches branches, so nothing needs a stash, and neither agent ever sees the other's half-done files.

When a delivery is done, you bring it into `main` from the main folder with a merge commit, `git merge --no-ff`, so it stays one unit of work, reverted in one step with `git revert -m 1 <merge>` ([chapter 17](17-git-essentials.md#merge-commit)).

It also saves time: in the guided project, the two agents that built those two deliveries at once took 155 seconds from the first start to the last end, for 277.2 seconds of work added up.[^clinic-worktrees-run]

## The life of a worktree

Five commands, run from the main folder except where the text says otherwise.

```
git worktree add ../app-x -b x main
```

Creates the folder `../app-x`, creates the branch `x` at `main`, and checks it out in the folder.
You then build and commit inside `../app-x` as in any folder.
Only what git tracks is there: dependencies such as `node_modules` are not, so you install them in each worktree (`npm ci` in the guided project).

```
git worktree list
```

Prints every worktree, its commit and its branch, as above.

```
git merge --no-ff x
```

On `main`, in the main folder, brings the delivery in as one merge commit; the branch's commit is already visible there, since the history is shared.

```
git worktree remove ../app-x
```

Deletes the folder.
It refuses a folder with files changed or not tracked, so work you have not committed is never lost by accident.[^git-worktree]

```
git branch -d x
```

Deletes the branch, which outlives its folder.
`-d` deletes only a branch that is merged; `-D` deletes it anyway.

## Worktrees in the kit

A worktree per delivery is one of the three git strategies of [chapter 6](06-the-documents.md#the-two-choices), and in the kit it is these five commands with `/propose` and `/apply` in between.
`/propose <slug>` runs `git worktree add ../<project>-<slug> -b <slug> main` and writes the page in the new folder; `/apply <slug>` runs in a fresh session opened in that folder; you review, commit on the branch, merge with `--no-ff`, remove the worktree and delete the branch.
The agent never commits, merges, resolves a conflict or removes a worktree: every step that changes the history is yours, as in every git strategy.
The guided project took this strategy in its [ADR-0003](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/worktrees/docs/adr/ADR-0003-git-strategy.md), which records the same steps.

To run two deliveries at once in an interactive session, open one terminal per session: one in the main folder for each `/propose`, one in each worktree for its `/apply`.
`/propose` writes in a folder outside the one its session started in, so the host asks you to approve that write, as [chapter 8](08-analyze.md#check-it-against-the-code) says of a permission the mode does not grant.
Headless, a session can write only in an `--add-dir` folder (a second folder it may work in) that existed when it started, so create the empty folder first; `git worktree add` accepts an empty folder.[^clinic-worktrees-run]

## When the branches meet: the conflict

Worktrees keep deliveries apart while they are built; the merge brings them together, and git combines the two sides line by line.
If both branches changed the same lines, or lines next to each other, git cannot know which to keep: it merges every other change, stops before the merge commit, and leaves the file to you.
That is a conflict.[^git-merge]

In the guided project, each delivery marked its own line in docs/06, the queue, and the two lines are neighbours.
The first merge, `route-errors`, went in clean; the second stopped:

```
git merge --no-ff minutes-of
```

```text
Auto-merging docs/01-Architecture.md
Auto-merging docs/06-Queue.md
CONFLICT (content): Merge conflict in docs/06-Queue.md
Automatic merge failed; fix conflicts and then commit the result.
```

docs/01 had changed on both branches too, but in lines far apart, so git merged it alone ("Auto-merging"): a conflict is about lines, not files.

In the conflicted file, git writes both versions between conflict markers: `<<<<<<<` opens the version of the branch you are on, `=======` separates it from the version of the branch coming in, and `>>>>>>>` closes that one.[^git-merge]
`git diff` shows them.
During a merge it prints two columns of `+` and `-` before each line, the first comparing with the branch you are on and the second with the branch coming in; what matters here is the lines between the markers:

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

Above `=======` is `main`, which already holds `route-errors`: its line `[x]`, with the text that delivery rewrote, and `minutes-of` still `[ ]`.
Below is `minutes-of`: its own line `[x]`, and `route-errors` as it was before.
Neither side is right alone; the right version keeps what both did: both lines `[x]`, and `route-errors` with its new text.

To resolve, edit the file to that version and delete the three marker lines; then `git add` tells git the file is resolved, and `git commit --no-edit` makes the merge commit with the message git prepared:

```
git add docs/06-Queue.md
git commit --no-edit
```

If you would rather not resolve it now, `git merge --abort` leaves the merge and puts the branch back as it was before.[^git-merge]

The history afterwards, in the graph of [chapter 17](17-git-essentials.md#merge-commit):

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

Both branches start at `0993b68`, each holds one commit, and each comes into `main` through its own merge commit, `045c744` and `699ab40`: two deliveries, each reverted alone.

## The trap: committing the markers

`git add` is how you tell git a conflict is resolved, and git takes your word.
Stage the file with its markers still inside, commit, and the merge commit holds the markers, with no warning.
It happened in the guided project, when the merge's commands were pasted as one block and the add and the commit ran before anyone touched the file.[^clinic-worktrees-run]

The guard is one command, before the merge's commit:

```
git diff --cached --check
```

It reads what is staged and reports each conflict marker as `<file>:<line>: leftover conflict marker`, and it exits non-zero when it finds one, so a script can stop on it.[^git-diff]

If the markers were committed anyway, the undo depends on whether anyone else has the commit.
Not pushed: `git reset --hard <the commit before the merge>` throws the merge away, and you merge again.
Pushed: `git revert`, since reset rewrites history that others already have, which is [chapter 17's rule for rebase](17-git-essentials.md#fast-forward-and-rebase).

## When parallel stops paying

Worktrees remove the mixing; they do not remove everything two deliveries share.
Before starting two at once, check four things.

**Files.** Two deliveries that change the same lines conflict at the merge.
The queue is always one of them, since every delivery marks its line, and it resolves the same way every time: keep both marks.
A code file both change is different: its resolution is a decision about the code.
So pair deliveries whose files do not meet: read each queue line, docs/01 and the code it names, and list the files each will touch.

**Shared resources.** Worktrees share the machine: its ports, a test database in a common folder.
In the guided project, both deliveries ran their end-to-end tests at once, both on port 3100, and one stopped with `Error: http://localhost:3100/api/health is already used`; run again, it passed.[^clinic-worktrees-run]
A port or a database per worktree is a choice the project can make, in a delivery of its own.

**Disk.** Each worktree has its own dependencies: in the guided project, 155M of `node_modules` per worktree, as much as the main folder.[^clinic-worktrees-run]

**You.** The agents work in parallel; your review does not.
You read each page and each staged change, commit and merge, one delivery at a time, so run at once only as many deliveries as you can review.
This book, written and reviewed by one person in shared files, stays on trunk for those two reasons, as its ADR-0010 in [chapter 6](06-the-documents.md#adrs) says.

## Key points

* Two agents in one folder mix their deliveries in one commit, or fight over the one branch the folder holds; a worktree gives each delivery its own folder and branch, sharing one history.
* `git worktree add ../<folder> -b <branch> main`, work and commit there, `git merge --no-ff <branch>` from the main folder, then `git worktree remove` and `git branch -d`; each delivery stays one merge commit, reverted alone.
* A conflict is two branches changing the same or neighbouring lines: git merges the rest and leaves both versions between markers; keep what both did, `git add`, commit, or leave with `git merge --abort`.
* Git commits markers without a word if you stage the file unresolved: run `git diff --cached --check` before committing a merge.
* Parallel pays while the deliveries' files do not meet, the machine's shared resources do not collide, the disk holds a copy of the dependencies per worktree, and you can still review each delivery.

## Exercises

These exercises use the guided project at its chapter tag [`book-v1/worktrees`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/worktrees), which holds the two deliveries above and their merges.
Your clone is at `book-v1/four-pieces`: run `git fetch --tags`, then `git switch -c mine18 book-v1/worktrees`.
Between the two tags are the kit update, seven fixes that this book's reviews queued in the clinic's milestone 1.1, the switch to worktrees and the two deliveries; building them yourself with `/propose` and `/apply` is optional, and the tag is what to compare against.
The commands are git commands you run yourself.

### Exercise 18.1

Create two worktrees from your branch, `../try-a` on `try-a` and `../try-b` on `try-b`.
In each, mark a different one of the adjacent `[ ]` lines `time-zone-names` and `slot-taken-retry` of docs/06 as `[x]`, and commit.
Merge both into `mine18` with `--no-ff`, resolve the conflict, and read `git log --oneline --graph`.

### Exercise 18.2

Go back to before the second merge with `git reset --hard`, repeat it, stage the file with its markers, run `git diff --cached --check`, and say what it prints and why nothing is committed yet.
Then run `git merge --abort`, remove both worktrees and delete both branches: say why `git branch -d` refuses one of them, and what deletes it.

### Exercise 18.3

From the tag's [docs/06](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/worktrees/docs/06-Queue.md), pick two open lines of milestone 1.1 that two agents could build at the same time, name the files each would touch, from docs/01 and the code, and say which conflicts you would still expect.

[^git-worktree]: Git, "git-worktree", the documentation, accessed 2026-09-30. <https://git-scm.com/docs/git-worktree>
[^clinic-worktrees-run]: This book's run of two deliveries of the guided project in parallel, 2026-09-30, with Claude Code 2.1.286 and the model `claude-opus-5-5`: every turn, the times, the merges in `merges.txt` (the `git worktree list` output copied from the terminal, the rest byte for byte, paths relative to the clinic's root), and the tests on the clinic's commit `699ab40` in `verify.txt`. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/clinic-worktrees-run/README.md>
[^git-merge]: Git, "git-merge", the documentation, section "How conflicts are presented" and option `--abort`, accessed 2026-09-30. <https://git-scm.com/docs/git-merge>
[^git-diff]: Git, "git-diff", the documentation, option `--check`, accessed 2026-09-30. <https://git-scm.com/docs/git-diff>
