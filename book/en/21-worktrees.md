# 21. Worktrees and parallel agents

After this chapter you can have two agents build two deliveries at the same time, each in its own folder, so that each merge holds one delivery and nothing else.
You can also resolve the conflict when both touched the same lines, catch a conflict marker before it is committed, and say when working in parallel stops paying.

## The problem: one folder, two jobs

An agent takes minutes to build a delivery, and while it works you wait.
The natural move is to start a second agent on the next delivery, and in one folder that goes wrong in one of two ways.

If both agents work on the same branch, their changes land in the same folder, mixed.
A commit takes both: one commit with two deliveries, one of them perhaps half done, which no single `git revert` can undo apart.
The unit of work of [chapter 20](20-git-essentials.md), one delivery that reverts in one step, is gone, and separating the two afterwards means picking changes file by file, line by line, by hand.

If you give each delivery its own branch, the folder still holds only one branch at a time.
Switching branches while an agent has work not yet committed either carries that work to the other branch or makes git refuse until you put it aside with `git stash`; and two agents cannot be on two branches of one folder at the same moment.

A second clone of the repository gives each agent its own folder, but each clone has its own copy of the history: the two meet only by pushing to a remote and pulling from it, and every clone repeats the whole history on disk.

What you want is several folders, each on its own branch, sharing one history.
That is a worktree.

## What a worktree is

A worktree is an extra working folder of the same git repository, checked out on its own branch.
In the words of the git documentation: "*A git repository can support multiple working trees, allowing you to check out more than one branch at a time.*"[^git-worktree]

The folder you cloned is the main worktree.
It holds the `.git` folder, where the history lives: the commits, the branches and the tags.
`git worktree add` creates another folder, checks a branch out in it, and leaves there a small `.git` file that points back to the main one.
All worktrees share the history; each has its own files, its own `HEAD` (the commit it is on) and its own staging area.[^git-worktree]
So a commit made in one worktree is visible at once from every other, with no push and no pull, while what you change or stage in one never appears in another.
Git also refuses to check out one branch in two worktrees, so two folders never write to the same branch.[^git-worktree]

## How it solves the problem

Give each delivery its own worktree, and each agent its own folder.
Say the lending library has two deliveries ready to build, `return-book` and `overdue-list`:

* The agent building `return-book` works in `../library-return-book`, on the branch `return-book`; it sees only that delivery's changes, and the commit you make there holds that delivery and nothing else.
* The agent building `overdue-list` does the same in `../library-overdue-list`, at the same time.
* Nobody switches branches, so nothing needs a stash, and neither agent ever sees the other's half-done files.

When a delivery is done, you bring it into `main` from the main folder with a merge commit, `git merge --no-ff`, so it stays one unit of work, reverted in one step with `git revert -m 1 <merge>`.

## The life of a worktree

Six steps, run from the main folder except where the text says otherwise.

```
git worktree add ../library-return-book -b return-book main
```

Creates the folder `../library-return-book`, creates the branch `return-book` at `main`, and checks it out in the folder.

Then you work inside the folder as in any other: the agent builds, you review and commit there.
Only what git tracks is in the new folder: dependencies such as `node_modules` are not, so you install them in each worktree (`npm ci` in a Node project).

```
git worktree list
```

Prints every worktree, the commit it is on and its branch.

```
git merge --no-ff return-book
```

On `main`, in the main folder, brings the delivery in as one merge commit; the branch's commits are already visible there, since the history is shared.

```
git worktree remove ../library-return-book
```

Deletes the folder.
It refuses a folder with files changed or not tracked, so work you have not committed is never lost by accident.[^git-worktree]

```
git branch -d return-book
```

Deletes the branch, which outlives its folder.
`-d` deletes only a branch that is merged; `-D` deletes it anyway.

## Worktrees in the kit

A worktree per delivery is one of the git strategies a project can write in the Git slot of its docs/05, and in the kit it is the steps above with `/propose` and `/apply` in between.
`/propose <slug>` creates the worktree named after the slug, `../<project>-<slug>` on a branch `<slug>` from `main`, and writes the page there.
`/apply <slug>` runs in a fresh session opened in that folder, builds the page, and stages the change.
You review and commit on the branch, merge into `main` with `--no-ff`, remove the worktree and delete the branch.

The agent never commits, merges, resolves a conflict or removes a worktree: every step that changes the history is yours, as in every git strategy.
To run two deliveries at once, open one session per folder: one in the main folder for each `/propose`, one in each worktree for its `/apply`.

## When the branches meet: the conflict

Worktrees keep deliveries apart while they are built; the merge brings them together, and git combines the two sides line by line.
If both branches changed the same lines, or lines next to each other, git cannot know which to keep: it merges every other change, stops before the merge commit, and leaves the file to you.
That is a conflict.[^git-merge]
A conflict is about lines, not files: two branches that change the same file far apart merge on their own.

In the conflicted file, git writes both versions between conflict markers: `<<<<<<<` opens the version of the branch you are on, `=======` separates it from the version of the branch coming in, and `>>>>>>>` closes that one.[^git-merge]
Every delivery marks its own line in the queue, so two deliveries whose lines are neighbours always meet there.
Here `return-book` was merged first, and `overdue-list` comes in second; the block is an illustration, written for this chapter:

```text
<<<<<<< HEAD
[x] return-book     a librarian records that a copy came back
[ ] overdue-list    a librarian sees every loan past its due date
=======
[ ] return-book     a librarian records that a copy came back
[x] overdue-list    a librarian sees every loan past its due date
>>>>>>> overdue-list
```

Above `=======` is `main`, where `return-book` is done; below is `overdue-list`, where its own line is done.
Neither side is right alone; the right version keeps what both did, both lines `[x]`.

To resolve, edit the file to that version and delete the three marker lines; then `git add` tells git the file is resolved, and `git commit --no-edit` makes the merge commit with the message git prepared:

```
git add docs/06-Queue.md
git commit --no-edit
```

If you would rather not resolve it now, `git merge --abort` leaves the merge and puts the branch back as it was before.[^git-merge]

## The trap: committing the markers

`git add` is how you tell git a conflict is resolved, and git takes your word.
Stage the file with its markers still inside, commit, and the merge commit holds the markers, with no warning.
It happens most easily when the merge's commands are run as one block, and the add and the commit run before anyone has touched the file.

The guard is one command, before the merge's commit:

```
git diff --cached --check
```

It reads what is staged and reports each conflict marker as `<file>:<line>: leftover conflict marker`, and it exits non-zero when it finds one, so a script can stop on it.[^git-diff]

If the markers were committed anyway, the undo depends on whether anyone else has the commit.
Not pushed: `git reset --hard <the commit before the merge>` throws the merge away, and you merge again.
Pushed: `git revert`, since a reset rewrites history that others already have, which is the rebase rule of chapter 20.

## When parallel stops paying

Worktrees remove the mixing; they leave in place everything two deliveries share.
Before starting two at once, check five things.

**The queue.** It always conflicts, since every delivery marks its line, and it resolves the same way every time: keep both marks.

**Files both change.** A code file that two deliveries both change is different: its resolution is a decision about the code, and the person who makes it must understand both changes.
So pair deliveries whose files do not meet: read each queue line, docs/01 and the code it names, and list the files each will touch.

**Shared ports and databases.** Worktrees share the machine: its ports, a test database in a common folder.
Two test runs that start a server on the same port collide, and one fails for a reason that has nothing to do with its code.
A port or a database per worktree is a choice the project can make, in a delivery of its own.

**Dependencies.** Each worktree installs its own, so each costs as much disk as the main folder, and the install takes its time again.

**You.** The agents work in parallel; your review does not.
You read each page and each staged change, commit and merge, one delivery at a time, so run at once only as many deliveries as you can review.
This book, written and reviewed by one person in shared files, stays on trunk for those two reasons.

## What the team gains

Two agents build at once, and each delivery still lands as one merge that reverts alone.
I measured it once, on a small TypeScript project of mine: two deliveries built at the same time by two agents took 155 seconds from the first start to the last end, against 277.2 seconds of the agents' work added up, a little over half the waiting.[^parallel-run]
The same run paid the costs of the section above: each worktree's `node_modules` took 155 MB of disk, and the two test runs collided once on a shared port and passed when run again; the queue conflicted, as it always does.[^parallel-run]
One run is a sign, not a rate: the gain holds while the deliveries' files do not meet, and it ends at the speed of the person who reviews and merges them.

## Key points

* Two agents in one folder mix their deliveries in one commit, or fight over the one branch the folder holds; a worktree gives each delivery its own folder and branch, sharing one history.
* `git worktree add ../<folder> -b <branch> main`, work and commit there, `git merge --no-ff <branch>` from the main folder, then `git worktree remove` and `git branch -d`; in the kit, `/propose` creates the worktree and `/apply` builds in it, and the person merges.
* A conflict is two branches changing the same or neighbouring lines: git merges the rest and leaves both versions between markers; keep what both did, `git add`, commit, or leave with `git merge --abort`.
* Git commits markers without a word if you stage the file unresolved: run `git diff --cached --check` before committing a merge.
* Parallel pays while the deliveries' files do not meet, the machine's ports and databases do not collide, the disk holds each worktree's dependencies, and one person can still review each delivery.

[^git-worktree]: Git, "git-worktree", the documentation, accessed 2026-09-30. <https://git-scm.com/docs/git-worktree>
[^git-merge]: Git, "git-merge", the documentation, section "How conflicts are presented" and option `--abort`, accessed 2026-09-30. <https://git-scm.com/docs/git-merge>
[^git-diff]: Git, "git-diff", the documentation, option `--check`, accessed 2026-09-30. <https://git-scm.com/docs/git-diff>
[^parallel-run]: J.C. Ködel, "One Page at a Time", the record of two deliveries built in parallel in two worktrees, 2026-09-30, in the book's repository. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/clinic-worktrees-run>
