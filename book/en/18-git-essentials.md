# 18. Git essentials

After this chapter you can keep every delivery one step to undo, one commit on trunk or one merge otherwise, and take it back with `git revert`.
You can also say what version control keeps and who made git, read a history of commits, branches and merges, merge a branch in each of the four ways git offers, and choose between trunk, a branch per delivery, a worktree per delivery and git-flow for a project.

## The problem

A project changes every day, and sooner or later someone asks what it looked like last week, who changed a line, or how to take back yesterday's change without losing today's.
Without a record of every version, the answer is somebody's memory.
With agents writing much of the change, the record matters more: each delivery must be one piece you can read, and one piece you can take back.

## One delivery, one step to undo

The kit asks one thing of git: one delivery, one step to undo.
On trunk a delivery is one commit, and `git revert <commit>` takes it back; on a branch, the delivery may hold several commits, and how it is merged decides whether one step still takes it back.
Git merges a branch in four ways, and this is what each leaves and what undoing a delivery of several commits then takes:

| Form | Lands on the receiving branch | Undo a delivery of several commits |
|---|---|---|
| Fast-forward | The commits, as they were | One revert per commit |
| Merge commit | The commits, and one commit with two parents | `git revert -m 1 <merge>` |
| Squash merge | One new commit | `git revert <commit>` |
| Rebase, then fast-forward | The commits, rewritten | One revert per commit |

With a branch per delivery, merge by merge commit or by squash, so the delivery stays one unit of work that one revert takes back.
A fast-forward or a rebase keeps that only when the branch held one commit.
The sections below define each term of the table: the four forms, then `git revert`.

## Commits and the history

Version control is a system that records the changes to a set of files over time, so that you can bring back any earlier version.[^pro-git-about]
It keeps every version, each with who changed it, when and why, so you can compare two versions, find who introduced a problem and when, and put one file or the whole project back as it was.[^pro-git-about]
Where the first systems kept the history on one server, git is distributed: every copy of the project holds the whole history, and any copy can restore the server if it is lost.[^pro-git-about]
Linus Torvalds, who created Linux, and the kernel's community wrote git in 2005 to keep the kernel's history, when the tool they had used stopped being free of charge for them, and they wrote it for speed and for many lines of work at once.[^pro-git-history]

A repository is a project under git: its files and, in a hidden `.git` folder, its whole history.
A commit is a saved snapshot of the whole project, with its author, its message and the commit or commits it came from, its parents.
It is named by a hash, a long hexadecimal string computed from all of that, which git prints shortened to its first characters.
The history is the chain of parents, from the last commit back to the first.

`git log --oneline` prints it one commit per line, the newest first.
For the lending library of Part I it could read like this; the output is an illustration, written for this chapter:

```text
a41c9e2 Let a member return a copy (return-book)
7d03b18 Lend a copy, and refuse when the rules say no (lend-book)
2f6e5a1 Start: documents and first milestone
```

Each line is one delivery, and its message says what a user can now do, with the delivery's slug at the end.
`git show <hash>` opens one of them: the message, and every line it added and removed.

A delivery's page and its build are one change.
The code, the tests, the documents the delivery updated and its page in `work/done/` go into the same commit, so the history holds the decision and the change it made side by side, and taking the delivery back takes all of it at once.
The agent stages that change and suggests the message; you read it and commit it, and that commit is your review.

A remote is another copy of the repository that yours knows by name, usually on a server such as GitHub, named `origin` by convention: `git clone <url>` copies it to your machine with its whole history, `git push` sends your branch's new commits to it, and `git pull` brings its new commits into your branch.
A team shares its work this way, and chapter 20's pull request, which asks for a pushed branch to be reviewed and merged, builds on it.

## Branches and tags

A branch is a name that points to one commit and moves to each new commit made on it.
Git was built for "*thousands of parallel branches*", and a branch is only a name, which is why it costs nothing.[^pro-git-history]
`main` is a branch; `git switch -c <name>` creates another at the commit you are on and switches to it, and `git branch` lists the branches, with a `*` before yours.
Two branches that start at the same commit and each gain commits have two histories that share their start: a merge brings them back together.

A tag is a name fixed on one commit, which never moves.
A project tags its releases, `v1.0`, `v1.1`, so that "what did we ship in v1.0" is one command away, while `main` moves on.

`HEAD` is the commit you are on: usually the last commit of your branch, which moves with it.

## Four ways to merge

A merge brings one branch's commits into another.
Say you made a branch `try` from `main`, committed on it, and now bring it into `main`, the receiving branch.
Git offers four ways, and each leaves a different history.[^pro-git-branching]

### Fast-forward

If `main` has no commit of its own since `try` left it, git can simply move the name `main` forward to `try`'s last commit.
That is a fast-forward, and it makes no commit:

```
git switch main
git merge --ff-only try
```

`--ff-only` refuses to merge when a fast-forward is not possible, so you know which form you got.
The history stays one line, and `main` now holds `try`'s commits exactly as they were.

### Rebase, then fast-forward

If `main` has moved on, a fast-forward is impossible.
A rebase rewrites `try`'s commits on top of `main`'s last commit, as new commits with new hashes, and then a fast-forward is possible again:

```
git switch try
git rebase main
git switch main
git merge --ff-only try
```

The history is again one line.
Rebase has one rule, from *Pro Git*: "*Do not rebase commits that exist outside your repository and that people may have based work on.*"[^pro-git-rebasing]
A rebase abandons the old commits, so anyone who built on them must merge their work again.
Rebase only commits nobody else has.

### Merge commit

A merge commit is a commit with two parents, the receiving branch's last commit and the merged branch's, that brings the whole branch in:

```
git switch main
git merge --no-ff try
```

`--no-ff` makes the merge commit even when a fast-forward was possible.
The branch's own commits stay in the history, readable one by one, and the merge commit marks where the whole branch came in.
`git log --oneline --graph` draws the parents as lines, and a merge commit is where two lines join.

### Squash merge

A squash merge writes the branch's whole change as one new commit with one parent:

```
git switch main
git merge --squash try
git commit
```

`--squash` stages the change and makes no commit; your `git commit` makes it.
The branch's own commits do not reach `main`: only this one commit does.

When both branches changed the same lines, git cannot choose and stops with a conflict, which you resolve before the merge completes; [chapter 19](19-worktrees.md) teaches it, where parallel deliveries meet.

## Undoing a delivery

`git revert <commit>` makes a new commit that undoes an earlier one, and keeps the history: the delivery and its undoing are both there to read.[^git-revert]
On trunk it undoes a delivery whole, its page included.
Later commits that changed the same lines make the revert stop with a conflict, resolved the same way as a merge's.

A merge commit has two parents, so git must be told which side to keep.
`git revert -m 1 <merge>` keeps parent 1, the receiving branch as it was, and undoes everything the second parent brought, every commit of the branch, in one new commit.[^git-revert]
The git documentation adds one caution: once a merge is reverted, a later merge of the same branch brings only the commits made on it after that merge.[^git-revert]

Revert is the undo for anything already shared.
`git reset --hard <commit>` also goes back, by moving the branch and dropping the commits after it; that rewrites history, so it is the rebase rule again: only on commits nobody else has.

## Trunk

The kit's trunk is one person committing on `main`, one commit per delivery, alone or with several agents open at once on deliveries that touch different files (chapter 19): a line, where each commit is a delivery and each revert takes one back.
Trunk-based development is a team practice of the same name, described by Paul Hammant: everyone merges small changes into the main branch "*at least once every 24 hours*", often through short-lived branches reviewed as pull requests.[^tbd]
In the kit's terms that is a branch per delivery with small deliveries, each merged by a merge commit or a squash.

## git-flow

git-flow is the branching model Vincent Driessen published in 2010: two branches that live forever, `master` (`main` today) for released versions and `develop` for the next one, and three kinds that come and go, `feature/` branches that go back into `develop` by merge commit, so a whole feature is easy to revert, and `release/` and `hotfix/` branches that prepare and fix a release.[^git-flow]
In 2020 he added a note at the top of the post: for software delivered continuously, such as a web app, which is not rolled back and does not keep several versions in use, a simpler flow fits better; git-flow still fits software that ships explicit versions or keeps several in use.[^git-flow]
In the kit, git-flow is a branch per delivery whose branch starts from `develop` and is named `feature/<slug>`, and its release and hotfix branches are the team's release work, which the kit does not model.

## Choosing

A project writes its choice once, in the Git slot of its docs/05, and every command reads it.

* **Trunk** fits one person, alone or with several sessions open on free lines (queue lines not done, not waiting and needing no other line done first, defined yet or not; [chapter 14](14-queue-states.md)) that touch different files: one commit per delivery on `main`, each session staging only its delivery, and the person committing one delivery at a time.
  It does not fit two people: their deliveries share one branch, and one commit carries the other's half-done work.
* **A branch per delivery** fits sequential work reviewed by pull request (chapter 20): each delivery merged by merge commit or squash.
* **A worktree per delivery** fits several people working at once, or one person whose deliveries touch the same files ([chapter 19](19-worktrees.md)): each delivery on its own branch in its own folder, merged the same way.
* **git-flow** fits software that ships numbered versions and keeps several in use.

Whichever it is, the rule is the same: one delivery, one step to undo, and the person commits and merges, never the agent.
This book, written and reviewed by one person, is on trunk.

## What the team gains

Every delivery lands as one commit on trunk or one merge otherwise, with its page beside its code, so taking a delivery back is one command, and reading why a line changed is one commit that holds both the change and the decision.
The evidence is the history itself: the lending library's log, shown earlier in this chapter, reads as the list of what users can do, one line per delivery and one revert per line, and a person who never opens the code can follow it.

## Key points

* One delivery, one step to undo: a delivery's page and build are one change, one commit on trunk or one merge otherwise, undone with `git revert <commit>` or `git revert -m 1 <merge>`.
* Version control keeps every version of a project's files with who changed what and when; git, written in 2005 by Linus Torvalds and the Linux kernel's community, is distributed, so every copy holds the whole history.
* A commit is a snapshot with its author, message and parents, named by a hash; a branch is a name that moves with each commit on it; a tag never moves; a remote is another copy you clone, push to and pull from.
* A fast-forward and a rebase leave a line of the branch's commits; a merge commit adds a commit with two parents; a squash merge leaves one new commit; never rebase commits someone else has.
* Trunk fits one person, alone or with several sessions on free lines that touch different files; a branch per delivery fits sequential work reviewed by pull request; a worktree per delivery fits several people, or deliveries that touch the same files; git-flow fits software that ships versions; the agent stages, the person commits and merges.

[^pro-git-about]: Scott Chacon and Ben Straub, "About Version Control", *Pro Git*, 2nd ed., accessed 2026-09-30. <https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control>
[^pro-git-history]: Scott Chacon and Ben Straub, "A Short History of Git", *Pro Git*, 2nd ed., accessed 2026-09-30. <https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git>
[^pro-git-branching]: Scott Chacon and Ben Straub, "Basic Branching and Merging", *Pro Git*, 2nd ed., accessed 2026-09-30. <https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging>
[^pro-git-rebasing]: Scott Chacon and Ben Straub, "Rebasing", section "The Perils of Rebasing", *Pro Git*, 2nd ed., accessed 2026-09-30. <https://git-scm.com/book/en/v2/Git-Branching-Rebasing>
[^git-revert]: Git, "git-revert", the documentation, option `-m`, accessed 2026-09-30. <https://git-scm.com/docs/git-revert>
[^tbd]: Paul Hammant, "Trunk Based Development", section "Elaboration, Claims and Caveats", accessed 2026-09-30. <https://trunkbaseddevelopment.com/>
[^git-flow]: Vincent Driessen, "A successful Git branching model", 2010, with its "Note of reflection" of 2020. <https://nvie.com/posts/a-successful-git-branching-model/>
