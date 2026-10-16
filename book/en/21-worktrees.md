# 21. Worktrees and parallel agents

After this chapter you can run two agents at once in one folder, on trunk, on free lines whose files do not meet, tell what is and is not a conflict there, and commit each delivery alone.
You can also say when it still pays to give each delivery a worktree, a second working folder of the same repository on its own branch, lay it out as the kit shapes it, a container folder with `main/` and a hidden folder, build in worktrees, resolve the conflict when two branches touched the same lines, catch a conflict marker before it is committed, and say when working in parallel stops paying.

## The problem: one folder, two jobs

An agent takes minutes to build a delivery, and while it works you wait.
The natural move is to start a second agent on the next delivery, in a second session, in the same folder.
Often that works: the two agents write different files, and each delivery still lands as its own commit.
It goes wrong in two cases.

If both deliveries change the same lines of a file, or one needs a file the other is changing, each agent builds on top of the other's half-done work, and neither delivery can be reviewed or reverted alone.

If one commit takes both deliveries, one of them perhaps half done, no single `git revert` can undo them apart.
The unit of work of [chapter 20](20-git-essentials.md), one delivery that reverts in one step, is gone, and separating the two afterwards means picking changes file by file, line by line, by hand.

The first case is avoided by choosing which deliveries run together; the second, by how you commit.

## Two sessions in one folder

Two sessions can share one folder when they build free lines that touch different files.
A free line is a line of the queue that is not done, not waiting, and needs no other line done first ([chapter 16](16-queue-states.md) teaches the queue's marks).

Say the lending library has two free lines: `return-book`, which touches `src/loans/`, and `overdue-list`, which touches `src/reports/`; the slugs and paths are an illustration, written for this chapter.
Their code files do not meet.
Both mark docs/06, the queue, but each marks its own line, and two lines far apart in one file are two hunks, separate pieces of a change that git stages apart.
So the two can run in one folder at once.

Each session keeps to its delivery:

* it changes the mark of its own line in the queue, and no other;
* it stages only its own paths, and only its own hunk of docs/06 (`git add -p` stages a file hunk by hunk);
* it leaves alone whatever the other session changed or staged.

The commit stays yours, one delivery at a time.
Before committing `return-book`, look at what is staged:

```
git diff --cached --stat
```

It lists each staged file and how many of its lines change.
If the list holds only `src/loans/`, the page of `return-book` and docs/06, and `git diff --cached docs/06-Queue.md` shows only that line's hunk, a plain `git commit` takes that delivery and nothing else.
If it also holds `src/reports/` or the page of `overdue-list`, the other session has staged its work too, and a plain commit takes both.

The trap is naming paths.
`git commit -- docs/06-Queue.md src/loans/` looks like the safe way to commit one delivery, and for files only that delivery changed, it is.
For a file both changed, it takes too much: the git documentation says a commit with paths is made "*by taking the updated working tree contents of the paths specified on the command line, disregarding any contents that have been staged for other paths.*"[^git-commit]
So git takes docs/06 whole from the folder, the other line's mark included, staged or not, and that mark rides into this commit.

The way out is order.
Commit each delivery as its session ends, before the other stages anything.
If the other has staged already, unstage its entries yourself, `git restore --staged <its paths>` and `git restore --staged -p docs/06-Queue.md` for its hunk of the queue, commit, and let its session stage them again; a session never touches the other's entries.

## What is and is not a conflict there

In one folder, each session sees the other's work as it happens, and most of it is no reason to stop:

* another line's mark changes in docs/06, `[~]` to `[*]`, say;
* another delivery's page appears in `work/`, or its files in the tree;
* another delivery's entries are already staged.

Each is the other session's work: the session goes on, and touches none of it.
This is written down because, without it, a second session on another module stops when the first changes docs/06, though it has everything it needs to go on.

Two things are a conflict:

* both deliveries edit the same hunk, the same lines of `src/loans/loan.ts`, say;
* this page needs a file the other delivery is changing, as when `return-book` needs `src/loans/` while another delivery reshapes it.

Then the session stops and reports, and the decision is yours: order the two lines, by writing `· after <slug>` on the one that must wait for the other, or give one of them a worktree.

## What a worktree is

A worktree is an extra working folder of the same git repository, checked out on its own branch.
In the words of the git documentation: "*A git repository can support multiple working trees, allowing you to check out more than one branch at a time.*"[^git-worktree]

The folder you cloned is the main worktree.
It holds the `.git` folder, where the history lives: the commits, the branches and the tags.
That is the common case.
A repository can also be bare: a repository with no files of its own, only the history, made by `git clone --bare`.[^git-clone]
Then no working folder holds the history, and every working folder, `main/` included, is a worktree of the bare repository.
`git worktree add` creates another folder, checks a branch out in it, and leaves there a small `.git` file that points back to where the history lives.
All worktrees share the history; each has its own files, its own `HEAD` (the commit it is on) and its own staging area.[^git-worktree]
So a commit made in one worktree is visible at once from every other, with no push and no pull, while what you change or stage in one never appears in another.
Git also refuses to check out one branch in two worktrees, so two folders never write to the same branch.[^git-worktree]

## When a worktree still pays

One folder holds one branch at a time, and everyone working in it shares its files.
So a worktree per delivery pays in two cases: several people working at once, since one commit on a shared branch would carry another person's half-done work; and one person whose deliveries touch the same files, so each is built apart and their changes meet only at the merge.

Branches alone do not do it.
If you give each delivery its own branch in one folder, the folder still holds only one branch at a time.
Switching branches while an agent has work not yet committed either carries that work to the other branch or makes git refuse until you put it aside with `git stash`; and two agents cannot be on two branches of one folder at the same moment.

A second clone of the repository gives each agent its own folder, but each clone has its own copy of the history: the two meet only by pushing to a remote and pulling from it, and every clone repeats the whole history on disk.

A worktree per delivery gives exactly that: several folders, each on its own branch, sharing one history.

## How it solves the problem

Give each delivery its own worktree, and each agent its own folder.
Say `return-book` and `overdue-list` both need `src/loans/`, in the lending library's folder `library/`, whose `main/` holds the branch `main` (the next section sets it up):

* The agent building `return-book` works in `library/.focus-kit/worktrees/return-book`, on the branch `focus-kit/return-book`; it sees only that delivery's changes, and the commit you make there holds that delivery and nothing else.
* The agent building `overdue-list` does the same in `library/.focus-kit/worktrees/overdue-list`, on `focus-kit/overdue-list`, at the same time.
* Nobody switches branches, so nothing needs a stash, and neither agent ever sees the other's half-done files.

When a delivery is done, you bring it into `main` from `main/` with a merge commit, `git merge --no-ff`, so it stays one unit of work, reverted in one step with `git revert -m 1 <merge>`.

## The life of a worktree

First, once per clone, the container: a folder that holds the checkout, `main/`, and a hidden folder, `.focus-kit/`, with the history and every delivery's worktree.
The commands, the folder and the slugs are written for this chapter, on the lending library.
From an empty folder `library/`:

```
git clone --bare <url> .focus-kit/repo.git
```

Copies the remote's history into `.focus-kit/repo.git`, a bare repository.

```
cd .focus-kit/repo.git
git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'
```

Tells `git fetch` to keep a copy of every remote branch as `origin/<branch>`, the remote-tracking branch: git's local record of where the remote's branch is.
A bare clone writes no such line; the git documentation says that with `--bare` "*neither remote-tracking branches nor the related configuration variables are created.*"[^git-clone]
Skip it, and `git fetch` in `main/` brings no `origin/main`.

```
git worktree add ../../main main
```

Run inside `.focus-kit/repo.git`, creates `library/main/` on the branch `main`: the checkout, a worktree like the others, whose `.git` is a file that points to `.focus-kit/repo.git`.
`git worktree list` now prints two lines, one ending in `library/.focus-kit/repo.git` marked `(bare)`, one ending in `library/main` on `[main]`.

A project that chooses this writes these steps in a manual of `docs/manuals/` ([chapter 10](10-the-documents.md)), so whoever clones it next makes the same container.

Then six steps, run from `main/` except where the text says otherwise.
A path given to `git worktree add` is relative to the folder you stand in, so the same command run elsewhere puts the folder elsewhere; from `main/`, `../.focus-kit/worktrees/<slug>` lands inside the container.

```
git worktree add ../.focus-kit/worktrees/return-book \
  -b focus-kit/return-book main
```

Creates the folder `library/.focus-kit/worktrees/return-book`, creates the branch `focus-kit/return-book` at `main`, and checks it out in the folder.
The folder sits in the hidden folder, beside `main/`, so none of `main/`'s files show it.

Then you work inside the folder as in any other: the agent builds, you review and commit there.
Only what git tracks is in the new folder: dependencies such as `node_modules` are not, so you install them in each worktree (`npm ci` in a Node project).

```
git worktree list
```

Prints every worktree, the commit it is on and its branch.

```
git merge --no-ff focus-kit/return-book
```

On `main`, in `main/`, brings the delivery in as one merge commit; the branch's commits are already visible there, since the history is shared.

```
git worktree remove ../.focus-kit/worktrees/return-book
```

Deletes the folder.
It refuses a folder with files changed or not tracked, so work you have not committed is never lost by accident.[^git-worktree]

```
git branch -d focus-kit/return-book
```

Deletes the branch, which outlives its folder.
`-d` deletes only a branch that is merged; `-D` deletes it anyway.

## Worktrees in the kit

A worktree per delivery is one of the git strategies a project can write in the Git slot of its docs/05, and in the kit it is the steps above with `/propose` and `/apply` in between.
The slot may name the hidden folder and the branch prefix, and one that names neither means `.focus-kit/` and `focus-kit/`, the ones above; a slot that names `.wt/` and `wt/` puts `return-book` in `.wt/worktrees/return-book/` on `wt/return-book`.
The kit's two names say what made the folder and the branch, so a person who finds them in a project knows where they came from.
`/propose <slug>` creates the worktree at `<hidden>/worktrees/<slug>/` on the branch `<prefix>/<slug>`, from the main branch's `HEAD`, or reuses the one that exists, and writes the page there.
A branch `<slug>` without the prefix is not the delivery's: it is someone else's.
You make the container once; the kit makes each worktree.
`/apply <slug>` runs in a fresh session opened in that folder, builds the page, and stages the change.
You review and commit on the branch, merge into `main` with `--no-ff`, remove the worktree and delete the branch.

The agent never commits, merges, resolves a conflict or removes a worktree: every step that changes the history is yours, as in every git strategy.
To run two deliveries at once in worktrees, open one session per folder: one in `main/` for each `/propose`, one in each worktree for its `/apply`.

One shape for every tool and every person prevents an error: when nothing says where a delivery's worktree belongs, a session makes one wherever it stands, and the page it writes there is copied to the main branch by hand.

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
>>>>>>> focus-kit/overdue-list
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

In one folder or in worktrees, two deliveries at once still share whatever is not in their own files.
Before starting two, check five things.

**The queue.** In one folder it does not conflict: each session marks its own line and stages its own hunk.
Across worktrees it always conflicts at the merge, since every delivery marks its line, and it resolves the same way every time: keep both marks.

**Files both change.** A code file that two deliveries both change is different.
In one folder the session stops when it meets the other's change; across worktrees the merge does, and its resolution is a decision about the code: the person who makes it must understand both changes.
So pair deliveries whose files do not meet: read each queue line, docs/01 and the code it names, and list the files each will touch.

**Shared ports and databases.** Two sessions share the machine in either form: its ports, a test database in a common folder.
In one folder they also share the folder itself, its test database and its build output.
Two test runs that start a server on the same port, or write the same database, collide, and one fails for a reason that has nothing to do with its code.
A port or a database per session is a choice the project can make, in a delivery of its own.

**Dependencies.** One folder installs them once.
Each worktree installs its own, so each costs as much disk as the main folder, and the install takes its time again.

**You.** The agents work in parallel; your review does not.
You read each page and each staged change, commit and merge, one delivery at a time, so run at once only as many deliveries as you can review.
This book, written and reviewed by one person in shared files, stays on trunk for those reasons, and its docs/05 lets two sessions work in one folder on free lines that touch different files.

## What the team gains

Two agents build at once, and each delivery still lands as one change that reverts alone: one commit in one folder, one merge from a worktree.
I measured it once, on a small TypeScript project of mine: two deliveries built at the same time by two agents took 155 seconds from the first start to the last end, against 277.2 seconds of the agents' work added up, a little over half the waiting.[^parallel-run]
The same run paid the costs of the section above: each worktree's `node_modules` took 155 MB of disk, and the two test runs collided once on a shared port and passed when run again; the queue conflicted, as it always does.[^parallel-run]
That run was in worktrees.
One folder removes the second folder, the second install of 155 MB, the merge and the queue's conflict; no run measured two sessions in one folder, so that gain has no number of its own.
The rule of what is not a conflict removes an error: a second session that stops on a changed queue when it has everything it needs to go on.
The one shape of a worktree per delivery removes another: a page written in a worktree made somewhere the kit did not say, and copied to the main branch by hand.
One run is a sign, not a rate: the gain holds while the deliveries' files do not meet, and it ends at the speed of the person who reviews and commits them.

## Key points

* Two sessions share one folder on trunk when their lines are free and their files do not meet: each marks only its line, stages only its paths and its hunk of the queue, and you commit one delivery at a time.
* Another line's mark, another delivery's page or files and another session's staged entries are not a conflict; the same hunk edited by both, or a file one page needs that the other is changing, is: stop, then order the lines or give one a worktree.
* Commit from the index once `git diff --cached --stat` holds only that delivery; `git commit -- <paths>` takes each named file whole from the folder, the other delivery's hunk of a shared file included.
* A worktree per delivery pays for several people, or for deliveries that touch the same files: a container folder whose `main/` is the checkout keeps each delivery's worktree in `<hidden>/worktrees/<slug>/` on `<prefix>/<slug>`, `.focus-kit/` and `focus-kit/` by default; `git worktree add`, work there, `git merge --no-ff` from `main/`, `git worktree remove`, `git branch -d`; a conflict leaves both versions between markers, and `git diff --cached --check` catches any left before the commit.
* Parallel pays while the deliveries' files do not meet, the machine's ports and databases do not collide, the disk holds each worktree's dependencies, and one person can still review each delivery.

[^git-commit]: Git, "git-commit", the documentation, option `--only`, accessed 2026-10-13. <https://git-scm.com/docs/git-commit>
[^git-clone]: Git, "git-clone", the documentation, option `--bare`, accessed 2026-10-16. <https://git-scm.com/docs/git-clone>
[^git-worktree]: Git, "git-worktree", the documentation, accessed 2026-09-30. <https://git-scm.com/docs/git-worktree>
[^git-merge]: Git, "git-merge", the documentation, section "How conflicts are presented" and option `--abort`, accessed 2026-09-30. <https://git-scm.com/docs/git-merge>
[^git-diff]: Git, "git-diff", the documentation, option `--check`, accessed 2026-09-30. <https://git-scm.com/docs/git-diff>
[^parallel-run]: J.C. Ködel, "One Page at a Time", the record of two deliveries built in parallel in two worktrees, 2026-09-30, in the book's repository. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/clinic-worktrees-run>
