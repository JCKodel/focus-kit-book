# 19. Worktrees and parallel agents

After this chapter you can run two agents at once in one folder, on trunk, on free lines whose files do not meet, tell what is and is not a conflict there, and commit each delivery alone.
You can also say when it still pays to give each delivery a worktree, a second working folder of the same repository on its own branch, lay it out as the kit shapes it, a container folder with `main/` and a hidden folder, build in worktrees, resolve the conflict when two branches touched the same lines, catch a conflict marker before it is committed, and say when working in parallel stops paying.
And you can run several `/propose` at once on the agent's recommended answers, read on each page what it decided without you before any `/apply`, and say why every commit stays your decision.

## The problem: one folder, two jobs

An agent takes minutes to build a delivery, and while it works you wait.
The natural move is to start a second agent on the next delivery, in a second session, in the same folder.
Often that works: the two agents write different files, and each delivery still lands as its own commit.
It goes wrong in two cases.

If both deliveries change the same lines of a file, or one needs a file the other is changing, each agent builds on top of the other's half-done work, and neither delivery can be reviewed or reverted alone.

If one commit takes both deliveries, one of them perhaps half done, no single `git revert` can undo them apart.
The unit of work of [chapter 18](18-git-essentials.md), one delivery that reverts in one step, is gone, and separating the two afterwards means picking changes file by file, line by line, by hand.

The first case is avoided by choosing which deliveries run together; the second, by how you commit.

## Two sessions in one folder

Two sessions can share one folder when they build free lines that touch different files.
A free line is a line of the queue that is not done, not waiting, and needs no other line done first ([chapter 14](14-queue-states.md) teaches the queue's marks).

Say the lending library has two free lines: `return-book`, which touches `src/features/loans/`, and `overdue-list`, which touches `src/features/reports/`; the slugs and paths are an illustration, written for this chapter.
Their code files do not meet.
Both mark docs/06, the queue, but each marks only its own line.
`git add -p` offers a file to stage in hunks, separate pieces of a change: two lines far apart are two hunks, two neighbouring lines are one, and each session still stages its own line alone (the section on the batch shows how).
So the two can run in one folder at once.

Each session keeps to its delivery:

* it changes the mark of its own line in the queue, and no other;
* it stages only its own paths, and only its own line of docs/06;
* it leaves alone whatever the other session changed or staged.

The commit stays your decision, one delivery at a time, after you have used it and read what it staged.
Before committing `return-book`, look at what is staged:

```
git diff --cached --stat
```

It lists each staged file and how many of its lines change: it names files, and says nothing of whose lines a shared file holds.
So a list of only `src/features/loans/`, the page of `return-book` and docs/06 does not settle docs/06, which both sessions change; `git diff --cached docs/06-Queue.md` does, and when it shows `return-book`'s line alone, a plain `git commit` takes that delivery and nothing else.
If the list also holds `src/features/reports/` or the page of `overdue-list`, or the queue's staged diff holds `overdue-list`'s line, the other session has staged its work too, and a plain commit takes both.

Then do not commit yet: the commit waits until the index holds only the delivery you reviewed.
The session that found the other's entries already staged told you so and left them as they were; neither session removes the other's entries.
The usual way to an index of one delivery is order: commit each delivery as its session ends, before the other stages anything.
If both are staged already, sorting the index is yours: `git restore --staged <its paths>` takes the other's files out of the index and leaves them in the folder.
The queue cannot be split with `s` when the two lines are neighbours, since `git restore --staged -p` divides a hunk as `git add -p` does;[^git-restore] so `git restore --staged docs/06-Queue.md` takes the whole file out, you ask this delivery's session to stage its own line again, and you commit.
Then the other session stages its entries again, when you ask it.

The trap is naming paths.
`git commit -- docs/06-Queue.md src/features/loans/` looks like the way to commit one delivery, and it is never a way to choose one.
A plain `git commit` takes the index: a line the other session changed and did not stage is in the folder, not in the index, so it stays out of the commit.
A commit with paths takes the folder instead: the git documentation says it is made "*by taking the updated working tree contents of the paths specified on the command line, disregarding any contents that have been staged for other paths.*"[^git-commit]
So git takes docs/06 whole from the folder, the other line's mark included, staged or not, and that mark rides into this commit.
You choose a delivery with the index and check it with `git diff --cached`, never with paths on `git commit`.

## What is and is not a conflict there

In one folder, each session sees the other's work as it happens, and most of it is no reason to stop:

* another line's mark changes in docs/06, `[~]` to `[*]`, say;
* another delivery's page appears in `work/`, or its files in the tree;
* another delivery's entries are already staged;
* two neighbouring lines of docs/06, one per delivery, which git puts in one hunk: each session stages its own line, and sharing a hunk is sharing no line.

Each is the other session's work: the session goes on, and touches none of it.
This is written down because, without it, a second session on another module stops when the first changes docs/06, though it has everything it needs to go on.

Two things are a conflict:

* both deliveries edit the same line, of `src/features/loans/rules.ts`, say, or of the queue;
* this page needs a file the other delivery is changing, as when `return-book` needs `src/features/loans/` while another delivery reshapes it.

Then the session stops and reports, and the decision is yours: order the two lines, by writing `· after <slug>` on the one that must wait for the other, or give one of them a worktree.

## What a worktree is and when it pays

A worktree is an extra working folder of the same git repository, checked out on its own branch.
In the words of the git documentation: "*A git repository can support multiple working trees, allowing you to check out more than one branch at a time.*"[^git-worktree]
The folder you cloned is the main worktree, the one whose `.git` folder holds the history: the commits, the branches and the tags.
`git worktree add` creates another folder, checks a branch out in it, and leaves there a small `.git` file that points back to where the history lives.
All worktrees share the history; each has its own files, its own `HEAD` (the commit it is on) and its own staging area.[^git-worktree]
So a commit made in one worktree is visible at once from every other, with no push and no pull, while what you change or stage in one never appears in another.
Git also refuses to check out one branch in two worktrees, so two folders never write to the same branch.[^git-worktree]

A worktree per delivery pays in two cases: several people working at once, since one commit on a shared branch would carry another person's half-done work; and one person whose deliveries touch the same files, so each is built apart and their changes meet only at the merge.
A branch per delivery in one folder does not do it: the folder holds one branch at a time, and switching while an agent has work not yet committed carries that work along or stops until `git stash` puts it aside.
A second clone gives each agent its own folder, but with its own copy of the whole history on disk, which meets the other only through a push and a pull.

Say `return-book` and `overdue-list` both need `src/features/loans/`, in the lending library's folder `library/`, whose `main/` holds the branch `main` (the next section sets it up):

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

Copies the remote's history into `.focus-kit/repo.git`, a bare repository: one with no files of its own, only the history.[^git-clone]
No working folder then holds the history, and every working folder, `main/` included, is a worktree of the bare repository.

```
cd .focus-kit/repo.git
git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'
```

Writes the fetch line a bare clone leaves out: without it, `git fetch` in `main/` brings no `origin/main`, git's record of where the remote's `main` is.

```
git worktree add ../../main main
```

Run inside `.focus-kit/repo.git`, creates `library/main/` on the branch `main`: the checkout, a worktree like the others, whose `.git` is a file that points to `.focus-kit/repo.git`.
`git worktree list` now prints two lines, one ending in `library/.focus-kit/repo.git` marked `(bare)`, one ending in `library/main` on `[main]`.

A project that chooses this writes these steps in a manual of `docs/manuals/` ([chapter 7](07-the-documents.md)), so whoever clones it next makes the same container.

Then six steps, run from `main/` except where the text says otherwise.
A path given to `git worktree add` is relative to the folder you stand in, so the same command run elsewhere puts the folder elsewhere; from `main/`, `../.focus-kit/worktrees/<slug>` lands inside the container.

```
git worktree add ../.focus-kit/worktrees/return-book \
  -b focus-kit/return-book main
```

Creates the folder `library/.focus-kit/worktrees/return-book`, creates the branch `focus-kit/return-book` at `main`, and checks it out in the folder.
The folder sits in the hidden folder, beside `main/`, so none of `main/`'s files show it.

Then you work inside the folder as in any other: the agent builds, you use what it built, review and commit there.
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
You use the delivery, review and commit on the branch, merge into `main` with `--no-ff`, remove the worktree and delete the branch.

The agent never commits, merges, pushes, resolves a conflict or removes a worktree on its own: every step that changes the history is yours to decide, as in every git strategy.
Ask, and it takes any of them for you: it writes the commit message, resolves the conflict, commits, merges, pushes or removes the worktree, and knows the commands that undo a step, such as `git merge --abort` for a merge stopped by a conflict or `git revert` for a delivery to take back.
Each step comes after your reading: ask for the commit once you have used the delivery and the staged diff holds only it, for the merge commit once the resolved file has no conflict marker left, and for the push once `git log` shows what will leave.
After a merge it made, `git log --oneline --graph -3` in `main/` shows the merge commit and the branch it brought in.
To run two deliveries at once in worktrees, open one session per folder: one in `main/` for each `/propose`, one in each worktree for its `/apply`.

The kit gives every tool and every person this one shape because of an error: a `/propose` running in a worktree another tool made, in a folder of its own, writes the page where the next `/apply` does not look.

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
Pushed: `git revert`, since a reset rewrites history that others already have, which is the rebase rule of chapter 18.

## Proposing in a batch

Everything above runs `/apply` in parallel.
A `/propose` feels slower, and the time goes to you, answering its questions, the hours of a person that, as [chapter 22](22-cost-and-where.md) shows, no token count sees.
When you could answer each of those questions yourself, you can move that time to one reading instead of spending it in every conversation.

That is a batch: one session per line, each running `/propose <slug>`, and each told, in the conversation, to take its own recommendation wherever it would ask.
The kit has no command for it and needs none.
`/propose` already asks with its recommendation first, and writes on the page each decision it takes with the document it came from (chapter 12); the kit's process asks that every choice made on your behalf be explicit on the page.
The batch only answers its questions in advance.

Each page then lists the questions it answered alone: the question, the answer chosen and why, and the document that left it open.
Here is that list on the page of `overdue-list`, written for this chapter:

```
**Decided without you.**

1. Order of the list: most days overdue first. docs/00 does not
   say; recommended, since the librarian calls the oldest loan
   first.
2. A copy returned today leaves the list at once. docs/00 does not
   say; recommended, so the list never shows a book already back.
```

Each item gives the question, the answer and its reason, and names docs/00 as the document that left it open; the heading is the project's to name, since the kit fixes the page's sections and not this one.
A page that answered nothing alone says so, or carries no list.

The batch moves your decisions to the reading and removes none of them.
Before the first `/apply`, read every page, this list first, and correct each one in its own conversation.

The recommendation covers only a question the documents leave open and you could answer.
A question that belongs to someone else, a client or the library's director, is never answered on a recommendation: the page goes as far as it can, and the line waits as `[?]` with `· resume: propose`, as `due-reminder` waits on `· blocked: what provider?` in chapter 14.
Case A gave such a question a line of its own, a question delivery, whose only output is a written answer; it is Case A's own customization, not a step of the kit (chapter 20).

Pages written at once do not read each other.
`/propose` reads the deliveries in flight in `work/` when it starts, and a page being written at the same time is not there yet: two pages may settle the same question two ways, or each ask docs/03 for the same new term.
You find it by reading the pages side by side, and you correct one of them in its conversation.

Each `/propose` writes its page and its line's mark and stages nothing: the proposal stays in the folder, uncommitted, and whatever the index already held stays as it was.
No commit hands a page on, either: the `/apply` that builds it, in the same folder, reads the page and the mark from the folder as they are.
The lines of one batch sit side by side in the queue, so git puts their marks in one hunk of docs/06.
That hunk holds no conflict: no line in it is changed by two sessions, and each session's change is its own line's mark, which the list of what is not a conflict names.
Nor is it a reason to stage anything while the pages are being written.

The applies that follow add no rule of their own: they run at once only on free lines whose files do not meet, and each commit is your decision, one delivery at a time.
Each `/apply` stages its delivery when it completes: its page, what it built and its line of the queue, and the other proposals stay unstaged in the folder.
That is where the shared hunk counts, and the session that owns a line stages its mark, never you.
`git add -p` cannot do it here: it splits a hunk with `s` only where an unchanged line separates two changes, and its `e` opens the hunk in an editor, which a session does not drive.[^git-add]
So the session writes a patch, the text `git diff` prints for a change, holding only its own line's `-` and `+`, next to each other, with the other lines as they stand in the index (the staged copy a commit is made from), unchanged, around them.
It gives that patch to `git apply --cached`, which applies it to the index alone and leaves the files in the folder as they are.[^git-apply]
Before each commit, `git diff --cached docs/06-Queue.md` shows this delivery's changes alone, its line's `-` and `+` side by side, and no change of another session.
If the index already held another session's entries, the session tells you and leaves them as they were, and the commit waits until the index holds only this delivery, as earlier in this chapter.

Asking for a step is not handing over the batch.
Once you have used and reviewed one delivery, and the index holds only it, its files in `git diff --cached --stat` and its line alone in `git diff --cached docs/06-Queue.md`, you may ask its session to commit it; the next delivery waits for its own use, its own review and its own index.
Letting the agents commit a batch of applies on their own, before you have read them, leaves the method, and it costs four things.
A commit stops saying that a person read the change, which is what it says in [chapter 13](13-apply.md).
In one folder, an agent's commit takes what another session staged, or, with paths, the shared docs/06 whole: the trap of naming paths, earlier in this chapter.
Reading many changes after they are committed is the condition of automation bias (chapters 13 and 24).
And a wrong delivery that later ones built on reverts with a conflict wherever they changed its lines (chapter 18).

## When parallel stops paying

In one folder or in worktrees, two deliveries at once still share whatever is not in their own files.
Before starting two, check five things.

**The queue.** In one folder it does not conflict: each session marks its own line, and each `/apply` stages that line alone, whether or not it shares a hunk with the other's.
Across worktrees it always conflicts at the merge, since every delivery marks its line, and it resolves the same way every time: keep both marks.

**Files both change.** A code file that two deliveries both change is different.
In one folder the session stops when it meets the other's change; across worktrees the merge does, and its resolution is a decision about the code: the person who makes it must understand both changes.
So list the files each delivery will touch, from its queue line, docs/01 and the code it names: deliveries whose files do not meet can share one folder; deliveries whose files meet run at once only in worktrees, and only when you can make the merge's decision; otherwise, order them with `· after <slug>`.

**Shared ports and databases.** Two sessions share the machine in either form: its ports, a test database in a common folder.
In one folder they also share the folder itself, its test database and its build output.
Two test runs that start a server on the same port, or write the same database, collide, and one fails for a reason that has nothing to do with its code.
A port or a database per session is a choice the project can make, in a delivery of its own.

**Dependencies.** One folder installs them once.
Each worktree installs its own, so each costs as much disk as the main folder, and the install takes its time again.

**You.** The agents work in parallel; your review does not.
You read each page, use each delivery, read its staged change and decide each commit and merge, one delivery at a time, so run at once only as many deliveries as you can review; a batch of proposes moves that reading to one sitting and does not shorten it.
This book, written and reviewed by one person in shared files, stays on trunk for those reasons, and its docs/05 lets two sessions work in one folder on free lines that touch different files.

## What the team gains

Two agents build at once, and each delivery still lands as one change that reverts alone in git, and what it did outside git is left to its page (chapter 18): one commit in one folder, one merge from a worktree.
I measured it once, in worktrees on a small TypeScript project of mine: two deliveries built at the same time took 155 seconds from the first start to the last end, against 277.2 seconds of the agents' work added up, at the cost of a `node_modules` folder in each worktree, two test runs that collided once on a shared port, and the queue's conflict at the merge.[^parallel-run]
The measurement is of two deliveries whose code files did not meet; the gain ends at the speed of the person who reviews them and decides their commits and merges.
Proposes in a batch carry the parallel into definition: the agents write the pages while you are away, and each page brings the decisions it took alone, listed for your one reading.

## Key points

* Two sessions share one folder on trunk when their lines are free and their files do not meet: each marks only its line, stages only its paths and its line of the queue, and you decide each commit, one delivery at a time.
* Another line's mark, another delivery's page or files and another session's staged entries are not a conflict; neither are two neighbouring lines of the queue in one hunk; a line edited by both, or a file one page needs that the other is changing, is: stop, then order the lines or give one a worktree.
* Commit from the index once it holds only that delivery: `git diff --cached --stat` names files, so read the staged diff of a shared file for its lines too; with another delivery staged, wait; and never select a delivery with `git commit -- <paths>`, which takes each named file whole from the folder, the other delivery's lines in a shared file included, staged or not.
* A worktree per delivery pays for several people, or for deliveries that touch the same files: a container folder whose `main/` is the checkout keeps each delivery's worktree in `<hidden>/worktrees/<slug>/` on `<prefix>/<slug>`, `.focus-kit/` and `focus-kit/` by default; `git worktree add`, work there, `git merge --no-ff` from `main/`, `git worktree remove`, `git branch -d`; a conflict leaves both versions between markers, and `git diff --cached --check` catches any left before the commit.
* Parallel pays while the deliveries' files do not meet, or meet only across worktrees whose merge you can decide, the machine's ports and databases do not collide, the disk holds each worktree's dependencies, and one person can still review each delivery; proposes can run in a batch on the recommended answers, staging nothing, each page listing what it decided alone for you to read before any `/apply`, each `/apply` staging its own delivery, and every commit stays your decision, made by you or asked of the agent after your review.

[^git-commit]: Git, "git-commit", the documentation, option `--only`, accessed 2026-10-13. <https://git-scm.com/docs/git-commit>
[^git-clone]: Git, "git-clone", the documentation, option `--bare`, accessed 2026-10-16. <https://git-scm.com/docs/git-clone>
[^git-worktree]: Git, "git-worktree", the documentation, accessed 2026-09-30. <https://git-scm.com/docs/git-worktree>
[^git-merge]: Git, "git-merge", the documentation, section "How conflicts are presented" and option `--abort`, accessed 2026-09-30. <https://git-scm.com/docs/git-merge>
[^git-diff]: Git, "git-diff", the documentation, option `--check`, accessed 2026-09-30. <https://git-scm.com/docs/git-diff>
[^git-add]: Git, "git-add", the documentation, section "Interactive mode", accessed 2026-10-18. <https://git-scm.com/docs/git-add>
[^git-restore]: Git, "git-restore", the documentation, option `--patch`, accessed 2026-10-18. <https://git-scm.com/docs/git-restore>
[^git-apply]: Git, "git-apply", the documentation, option `--cached`, accessed 2026-10-18. <https://git-scm.com/docs/git-apply>
[^parallel-run]: J.C. Ködel, "One Page at a Time", the record of two deliveries built in parallel in two worktrees, 2026-09-30, in the book's repository. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/clinic-worktrees-run>
