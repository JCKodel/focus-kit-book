# 19. Git essentials

After this chapter you can say what version control keeps and why git was made, read a history of commits, branches and merges, and merge a branch in each of the four ways git offers.
You can also undo a delivery in one step with `git revert`, and choose between trunk, a branch per delivery and git-flow for a project.

## The problem

A project changes every day, and sooner or later someone asks what it looked like last week, who changed a line, or how to take back yesterday's change without losing today's.
Without a record of every version, the answer is somebody's memory.
With agents writing much of the change, the record matters more: each delivery must be one piece you can read, and one piece you can take back.

## Version control, and why git

Version control is a system that records the changes to a set of files over time, so that you can bring back any earlier version.[^pro-git-about]
It keeps every version, each with who changed it, when and why, so you can compare two versions, find who introduced a problem and when, and put one file or the whole project back as it was.[^pro-git-about]

It works on any kind of file, and *Pro Git* names the designer who wants to keep every version of an image or a layout among the first to gain from it.[^pro-git-about]
Without it, the versions live in file names, `logo final.psd`, `logo final final.psd`, `logo final really.psd`, where only the person who named them knows which is the last and nothing says what changed from one to the next.
*Pro Git* calls copying files into another folder the most common way to keep versions, because it is simple, and one that invites mistakes: it is easy to forget which folder you are in, write to the wrong file or copy over one you meant to keep.[^pro-git-about]
With version control there is one `logo.psd`, and its earlier versions are in the history, each with its author, its date and its message.
One limit for images: git merges text line by line, but two versions of a binary file, such as a `.psd`, it cannot combine, so it keeps yours and marks the file as a conflict, and the two people who edited it choose which version stays.[^gitattributes]

The first systems kept the history on one server, from which each person checked out the files.
Git is distributed: every copy of the project holds the whole history, and any copy can restore the server if it is lost.[^pro-git-about]

Git was made for the Linux kernel.
From 1991 to 2002, changes to the kernel passed between its developers as patches and archived files; from 2002 the project used BitKeeper, a proprietary distributed system.[^pro-git-history]
In 2005 the relationship between the kernel's community and the company behind BitKeeper broke down, and the tool stopped being free of charge for them.[^pro-git-history]
That led the community, and in particular Linus Torvalds, who created Linux, to write their own tool, with what they had learned using BitKeeper and with these goals: speed, a simple design, strong support for non-linear development, "*thousands of parallel branches*", fully distributed, and able to handle a project the size of the kernel.[^pro-git-history]
Those goals are why a branch costs almost nothing in git: it is only a name, as the sections below show.

## Commits and the history

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

The kit keeps one rule here: a delivery's page and its build are one change.
The code, the tests, the documents the delivery updated and its page in `work/done/` go into the same commit, so the history holds the decision and the change it made side by side, and taking the delivery back takes all of it at once.
The agent stages that change and suggests the message; you read it and commit it, and that commit is your review.

## Branches and tags

A branch is a name that points to one commit and moves to each new commit made on it.
`main` is a branch; `git switch -c <name>` creates another at the commit you are on and switches to it, and `git branch` lists the branches, with a `*` before yours.
Two branches that start at the same commit and each gain commits have two histories that share their start: a merge brings them back together.

A tag is a name fixed on one commit, which never moves.
A project tags its releases, `v1.0`, `v1.1`, so that "what did we ship in v1.0" is one command away, while `main` moves on.

`HEAD` is the commit you are on: usually the last commit of your branch, which moves with it.

## Remotes: clone, push and pull

A remote is another copy of the repository that yours knows by name, usually a server such as GitHub, and by convention named `origin`.
`git clone <url>` copies a remote to your machine, with its whole history, and remembers it as `origin`.
`git push` sends your branch's new commits to the remote; `git pull` brings the remote's new commits into your branch.
A team shares its work this way: each person commits on their own copy and pushes, and the others pull.
Chapter 21 builds on this, with the pull request that asks for a pushed branch to be reviewed and merged.

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

### The four side by side

A delivery of several commits, merged in each form, and what undoing it takes, with `git revert` from the next section:

| Form | Lands on the receiving branch | Undo a delivery of several commits |
|---|---|---|
| Fast-forward | The commits, as they were | One revert per commit |
| Merge commit | The commits, and one commit with two parents | `git revert -m 1 <merge>` |
| Squash merge | One new commit | `git revert <commit>` |
| Rebase, then fast-forward | The commits, rewritten | One revert per commit |

With a branch per delivery, merge by merge commit or by squash, so the delivery stays one unit of work that one revert takes back.
A fast-forward or a rebase keeps that only when the branch held one commit.

When both branches changed the same lines, git cannot choose and stops with a conflict, which you resolve before the merge completes; [chapter 20](20-worktrees.md) teaches it, where parallel deliveries meet.

## Undoing a delivery

`git revert <commit>` makes a new commit that undoes an earlier one, and keeps the history: the delivery and its undoing are both there to read.[^git-revert]
On trunk, one delivery is one commit, so `git revert <commit>` undoes the delivery whole, its page included.
Later commits that changed the same lines make the revert stop with a conflict, resolved the same way as a merge's.

A merge commit has two parents, so git must be told which side to keep.
`git revert -m 1 <merge>` keeps parent 1, the receiving branch as it was, and undoes everything the second parent brought, every commit of the branch, in one new commit.[^git-revert]
The git documentation adds one caution: once a merge is reverted, a later merge of the same branch brings only the commits made on it after that merge.[^git-revert]

Revert is the undo for anything already shared.
`git reset --hard <commit>` also goes back, by moving the branch and dropping the commits after it; that rewrites history, so it is the rebase rule again: only on commits nobody else has.

## Trunk, and trunk-based development

The kit's trunk is one person committing on `main`, one delivery at a time, one commit per delivery.
It is the simplest history there is: a line, where each commit is a delivery and each revert takes one back.

Trunk-based development is a team practice of the same name, described by Paul Hammant: everyone merges small changes into the main branch "*at least once every 24 hours*", often through short-lived branches reviewed as pull requests.[^tbd]
In the kit's terms that is a branch per delivery with small deliveries, each merged by a merge commit or a squash.

## git-flow

git-flow is the branching model Vincent Driessen published in 2010.[^git-flow]
It has two branches that live forever and three kinds that come and go:

* `master` (`main` today) holds only released versions, each merge into it a release, tagged.
* `develop` holds the next version as it is built.
* `feature/<name>` starts from `develop` and goes back into it with `--no-ff`, for his reason: "*Reverting a whole feature (i.e. a group of commits), is a true headache in the latter situation, whereas it is easily done if the `--no-ff` flag was used.*"[^git-flow] It is the table's reason: one merge commit, one revert.
* `release/<version>` starts from `develop` to prepare a release and merges into both `master` and `develop`.
* `hotfix/<version>` starts from `master` to fix a released version and merges into both.

In 2020 he added a note at the top of the post: for software delivered continuously, such as a web app, which is not rolled back and does not keep several versions in use, a simpler flow fits better; git-flow still fits software that ships explicit versions or keeps several in use.[^git-flow]

In the kit, git-flow is a branch per delivery whose branch starts from `develop` and is named `feature/<slug>`.
Release and hotfix branches are the team's release work, which the kit does not model.

## Choosing

A project writes its choice once, in the Git slot of its docs/05, and every command reads it.

* **Trunk** fits one person, or one person at a time: one commit per delivery on `main`.
* **A branch per delivery** fits a team, or one person running agents in parallel ([chapter 20](20-worktrees.md)): each delivery merged by merge commit or squash, usually through a pull request (chapter 21).
* **git-flow** fits software that ships numbered versions and keeps several in use.

Whichever it is, the rule is the same: one delivery, one step to undo, and the person commits and merges, never the agent.
This book, written and reviewed by one person, is on trunk.

## What the team gains

Every delivery lands as one commit on trunk or one merge otherwise, with its page beside its code, so taking a delivery back is one command, and reading why a line changed is one commit that holds both the change and the decision.
The history reads as the list of what users can do, one line per delivery, and a person who never opens the code can follow it.
There is no number for this gain: it is a property of the history's shape, and no measurement was made.

## Key points

* Version control keeps every version of a project's files, of any kind, with who changed what and when; git, made in 2005 for the Linux kernel, is distributed, so every copy holds the whole history.
* A commit is a snapshot with its author, message and parents, named by a hash; a branch is a name that moves with each commit on it; a tag never moves; a remote is another copy you clone, push to and pull from.
* A fast-forward and a rebase leave a line of the branch's commits; a merge commit adds a commit with two parents; a squash merge leaves one new commit; never rebase commits someone else has.
* A delivery's page and build are one change: one commit on trunk, one merge otherwise, undone with `git revert <commit>` or `git revert -m 1 <merge>`.
* Trunk fits one person; a branch per delivery fits a team or parallel agents; git-flow fits software that ships versions; the agent stages, the person commits and merges.

[^pro-git-about]: Scott Chacon and Ben Straub, "About Version Control", *Pro Git*, 2nd ed., accessed 2026-09-30. <https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control>
[^pro-git-history]: Scott Chacon and Ben Straub, "A Short History of Git", *Pro Git*, 2nd ed., accessed 2026-09-30. <https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git>
[^gitattributes]: Git, "gitattributes", the documentation, the attribute `merge`, accessed 2026-09-30. <https://git-scm.com/docs/gitattributes>
[^pro-git-branching]: Scott Chacon and Ben Straub, "Basic Branching and Merging", *Pro Git*, 2nd ed., accessed 2026-09-30. <https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging>
[^pro-git-rebasing]: Scott Chacon and Ben Straub, "Rebasing", section "The Perils of Rebasing", *Pro Git*, 2nd ed., accessed 2026-09-30. <https://git-scm.com/book/en/v2/Git-Branching-Rebasing>
[^git-revert]: Git, "git-revert", the documentation, option `-m`, accessed 2026-09-30. <https://git-scm.com/docs/git-revert>
[^tbd]: Paul Hammant, "Trunk Based Development", section "Elaboration, Claims and Caveats", accessed 2026-09-30. <https://trunkbaseddevelopment.com/>
[^git-flow]: Vincent Driessen, "A successful Git branching model", 2010, with its "Note of reflection" of 2020. <https://nvie.com/posts/a-successful-git-branching-model/>
