# Git essentials: trunk, branches, git-flow

After this chapter you can say what version control keeps and why git was made, read a project's history as commits, branches and merges, merge a branch in each of the four ways git offers, and say which of them keeps a delivery undoable in one step.
You can also undo a delivery with `git revert`, and say when trunk, a branch per delivery or git-flow fits a project.

## Version control, and why git

Version control is a system that records the changes to a set of files over time, so that you can bring back any earlier version.[^pro-git-about]
It keeps every version, not only the last, each with who changed it, when and why, so you can compare two versions, find who introduced a problem and when, and put one file or the whole project back as it was.[^pro-git-about]
A developer often knows the git repository as the place where the code lives; it is also every state the code has had, and the clinic's history below is 13 of them, any of which you can open.

It works on any kind of file, and *Pro Git* names the designer who wants to keep every version of an image or a layout among the first to gain from it.[^pro-git-about]
Without it, the versions live in file names, `logo final.psd`, `logo final final.psd`, `logo final really.psd`, where only the person who named them knows which is the last and nothing says what changed from one to the next.
*Pro Git* calls copying files into another folder the most common way to keep versions, because it is simple, and one that invites mistakes: it is easy to forget which folder you are in, write to the wrong file or copy over one you meant to keep.[^pro-git-about]
With version control there is one `logo.psd`, and its earlier versions are in the history, each with its author, its date and its message.
One limit for images: git merges text line by line, but two versions of a binary file, such as a `.psd`, it cannot combine, so it keeps yours and marks the file as a conflict, and the two people who edited it choose which version stays.[^gitattributes]

The first systems kept the history on one server, from which each person checked out the files; git is distributed: every clone holds the whole history, so your clone of the clinic has all its commits, and any clone can restore the server if it is lost.[^pro-git-about]

Git was made for the Linux kernel.
From 1991 to 2002, changes to the kernel passed between its developers as patches and archived files; from 2002 the project used BitKeeper, a proprietary distributed system.[^pro-git-history]
In 2005 the relationship between the kernel's community and the company behind BitKeeper broke down, and the tool stopped being free of charge for them.[^pro-git-history]
That led the community, and in particular Linus Torvalds, who created Linux, to write their own tool, with what they had learned using BitKeeper and with these goals: speed, a simple design, strong support for non-linear development, "*thousands of parallel branches*", fully distributed, and able to handle a project the size of the kernel.[^pro-git-history]
Those goals are why a branch costs almost nothing in git: it is only a name, as the next sections show.

## Commits and the history

Every git command in this chapter is one you run: the agent runs none of them but `git add`, `git status` and `git diff`, as in [chapter 11](11-apply.md#review-before-you-commit).
The histories shown are the guided project at its chapter tag [`book-v1/four-pieces`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/four-pieces), commit `e6653b5`, and CLAHub, chapter 8's brownfield project, in the fork `JCKodel/clahub` at the tag [`book-v1`](https://github.com/JCKodel/clahub/tree/book-v1); each output is quoted as it ran.

A commit is a saved snapshot of the whole project, with its author, its message and the commit or commits it came from, its parents.
It is named by a hash, a long hexadecimal string computed from all of that, which git prints shortened to its first characters.
The history is the chain of parents, from the last commit back to the first.
`git log --oneline` prints it one commit per line, the newest first:

```
git log --oneline book-v1/four-pieces
```

```text
e6653b5 Move each client hook's events into tested plain functions
c54d011 Queue the confirmed findings of the milestone 1 review (docs/06)
f16f83b Let a client cancel an appointment up to 24 hours before it starts
442f88a Let a client book a free slot and keep the booking code
afc833a Wait for SQLite locks instead of failing with SQLITE_BUSY
064d7a9 Let the owner set each professional's weekly hours
4cceb3a Let the owner add, rename and remove professionals
75a8a25 Set up the clinic and let the owner sign in and out
d5b5c03 Build the skeleton: health page, Hono server, migrations, verify
3f0b47c Update focus-kit to e7607c5
23f67bb Brainstorm: documents and first milestone
a5ac6fd Install focus-kit
31d9503 Start: README and licenses
```

These are the clinic's 13 commits: one per delivery, each with the page and its build, made by the `git commit` of [chapter 11](11-apply.md#review-before-you-commit).
`git log --merges book-v1/four-pieces` lists only the commits with two parents, and it prints nothing: there is no merge in this history.

One commit holds one delivery.
This is [`f16f83b`](https://github.com/JCKodel/focus-kit-clinic/commit/f16f83bdfadf7bf5919545aa390c92e6c01d5e3c), the delivery `cancel-appointment`, with the files it changed and how many lines each gained and lost (`--format=` leaves out the author and the message):

```
git show --stat --format= f16f83b
```

```text
 docs/01-Architecture.md                            |   4 +-
 docs/02-Backend.md                                 |  15 +
 docs/03-Domain.md                                  |   4 +-
 docs/06-Queue.md                                   |   2 +-
 src/app/main.tsx                                   |   2 +
 src/features/appointments/BookingView.e2e.ts       |  99 +----
 src/features/appointments/BookingView.tsx          |  14 +-
 src/features/appointments/CancelView.e2e.ts        | 432 +++++++++++++++++++++
 src/features/appointments/CancelView.tsx           |  99 +++++
 src/features/appointments/RememberedView.tsx       | 118 +++++-
 src/features/appointments/api.ts                   |  67 +++-
 src/features/appointments/e2e.server.ts            |  92 +++++
 src/features/appointments/remembered.test.ts       |  36 ++
 src/features/appointments/remembered.ts            |  32 +-
 .../appointments/repository.server.test.ts         |  69 +++-
 src/features/appointments/repository.server.ts     |  45 +++
 src/features/appointments/route.server.test.ts     | 212 ++++++++++
 src/features/appointments/route.server.ts          |  63 ++-
 src/features/appointments/rules.test.ts            |  64 +++
 src/features/appointments/rules.ts                 |  23 ++
 src/features/appointments/strings.ts               |  23 ++
 src/features/appointments/styles.ts                |  16 +
 src/features/appointments/useCancel.ts             |  60 +++
 src/features/appointments/useRemembered.ts         |  82 +++-
 work/done/cancel-appointment-cancelled-390x844.png | Bin 0 -> 32270 bytes
 work/done/cancel-appointment-confirm-390x844.png   | Bin 0 -> 36094 bytes
 work/done/cancel-appointment-form-390x844.png      | Bin 0 -> 41477 bytes
 work/done/cancel-appointment-list-390x844.png      | Bin 0 -> 32483 bytes
 work/done/cancel-appointment-no-match-390x844.png  | Bin 0 -> 45783 bytes
 .../cancel-appointment-typed-cancelled-390x844.png | Bin 0 -> 39982 bytes
 work/done/cancel-appointment.md                    | 316 +++++++++++++++
 31 files changed, 1854 insertions(+), 135 deletions(-)
```

The page, `work/done/cancel-appointment.md`, is in the same commit as the code, the tests, the documents and the screenshots it proved: 31 files, one unit of work.
That is trunk, the kit's first answer to the git choice of [chapter 6](06-the-documents.md#the-two-choices): one person on `main`, one commit per delivery.

## Branches and tags

A branch is a name that points to one commit and moves to each new commit made on it.
`main` is a branch; `git switch -c <name>` creates another at the commit you are on and switches to it, and `git branch` lists the branches, with a `*` before yours.
Two branches that start at the same commit and each gain commits have two histories that share their start: that is what a merge brings back together.

A tag is a name fixed on one commit, which never moves.
The chapter tags you have checked out since [chapter 5](05-install-and-hosts.md#exercises), `book-v1/start` to `book-v1/four-pieces`, are tags: `book-v1/four-pieces` names `e6653b5` today and always will, while the clinic's `main` moves on.

`HEAD` is the commit you are on: usually the last commit of your branch, which moves with it.

## Four ways to merge

A merge brings one branch's commits into another.
Say you made a branch `try` from `main`, committed on it, and now bring it into `main`, the receiving branch.
Git offers four ways, and each leaves a different history.[^pro-git-branching]

### Fast-forward and rebase

If `main` has no commit of its own since `try` left it, git can simply move the name `main` forward to `try`'s last commit.
That is a fast-forward, and it makes no commit:

```
git switch main
git merge --ff-only try
```

`--ff-only` refuses to merge when a fast-forward is not possible, so you know which form you got.
The history stays one line, and `main` now holds `try`'s commits exactly as they were.
The clinic's history above is what a line of fast-forwards would leave: no merge commit anywhere.

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

### Merge commit

A merge commit is a commit with two parents, the receiving branch's last commit and the merged branch's, that brings the whole branch in:

```
git switch main
git merge --no-ff try
```

`--no-ff` makes the merge commit even when a fast-forward was possible.
CLAHub merges this way, through pull requests: a pull request, which [chapter 6](06-the-documents.md#the-two-choices) defined and chapter 20 teaches, asks for a branch to be merged after someone reviews it.
`--graph` draws the parents as lines, a merge commit where two lines join:

```
git log --oneline --graph book-v1 | head -20
```

```text
* 9d1e666 chore(deps): bump hono to 4.12.12 and prisma to 7.7.0 (#308)
* 7681b69 chore(deps): bump next from 16.1.7 to 16.2.3 (#307)
* 67c7328 chore(deps): bump vite from 7.3.1 to 7.3.2 (#304)
* e610454 chore(deps): bump defu from 6.1.4 to 6.1.6 (#303)
* d416f52 chore(deps): bump brace-expansion (#302)
* 47d957f chore(deps): bump picomatch (#301)
* 0876294 chore(deps-dev): bump flatted from 3.3.3 to 3.4.2 (#300)
*   9e9bdfe Merge pull request #291 from DamageLabs/dependabot/npm_and_yarn/multi-0d13b2d87f
|\  
| * f359190 chore(deps): bump serialize-javascript and terser-webpack-plugin
* |   59dbf66 Merge pull request #299 from DamageLabs/feat/about-page
|\ \  
| * | c849395 feat: add About page with project history and DamageLabs links
|/ /  
* |   26c9049 Merge pull request #298 from DamageLabs/feat/umami-analytics
|\ \  
| * | a3683be feat: add Umami analytics tracking
|/ /  
* |   cde3de9 Merge pull request #297 from DamageLabs/fix/docs-styling
|\ \  
```

`9e9bdfe`, `59dbf66`, `26c9049` and `cde3de9` are merge commits, one per pull request, each with the branch's commits on the line to its right.
The commits above them each have one parent and a pull request number in their subject: squash merges, the next form.

A merge commit keeps the branch's commits in the history.
Pull request #246, [`846e337`](https://github.com/JCKodel/clahub/commit/846e337fab0c7c89f42101de0ab42241c2f0fa57), brought in a branch of seven commits.
`<commit>^1` is a commit's first parent and `<commit>^2` its second, so this lists what the second parent's side had that the first did not:

```
git log --oneline 846e337^1..846e337^2
```

```text
42ccb59 fix(test): update webhook E2E test for structured error response
2efdc4e test(lib): add tests for result, logger, and api-error utilities
5f3d099 feat(exclusions): add toast notifications for error feedback
acee866 feat(ui): add error boundaries and not-found page
99c45a2 refactor: replace console.* with structured logger
a10bfdb refactor(actions): use shared result utilities and add error codes
bae1f35 feat(lib): add shared action result, logger, and API error helpers
```

The branch's work stays readable, commit by commit, in the history.
And the merge commit itself, with its hash, its two parents and its subject:

```
git show --no-patch --format='%h %p %s' 846e337
```

```text
846e337 2779b05 42ccb59 Merge pull request #246 from clahub/feat/214-structured-error-handling
```

`2779b05` is where `main` was; `42ccb59` is the branch's last commit, the first line of the list above.

### Squash merge

A squash merge writes the branch's whole change as one new commit with one parent:

```
git switch main
git merge --squash try
git commit
```

`--squash` stages the change and makes no commit; your `git commit` makes it.
CLAHub's [`9d1e666`](https://github.com/JCKodel/clahub/commit/9d1e666e1d30f271aea9640393229a7cbfbd1b62), the top line of the graph, is one:

```
git show --no-patch --format='%h %p %s' 9d1e666
```

```text
9d1e666 7681b69 chore(deps): bump hono to 4.12.12 and prisma to 7.7.0 (#308)
```

One parent, and the pull request's number, #308, in the subject, which is how a squash merge made on GitHub names what it came from.
The branch's own commits are not in `book-v1`'s history: only this one commit is.

### The four side by side

A delivery of several commits, merged in each form, and what undoing it takes, with `git revert` from the next section:

| Form | Lands on the receiving branch | Undo a delivery of several commits |
|---|---|---|
| Fast-forward | The commits, as they were | One revert per commit |
| Merge commit | The commits, and one commit with two parents | `git revert -m 1 <merge>` |
| Squash merge | One new commit | `git revert <commit>` |
| Rebase, then fast-forward | The commits, rewritten | One revert per commit |

With a branch per delivery, merge by merge commit or by squash, so the delivery stays one unit of work: the rule of [chapter 6](06-the-documents.md#the-two-choices), one merge of the branch, which [chapter 9's `[>]`](09-queue-and-milestones.md#the-marks) already assumes.
A fast-forward or a rebase keeps that only when the branch held one commit.

When both branches changed the same lines, git cannot choose and stops with a conflict, which you resolve before the merge completes; [chapter 18](18-worktrees.md#when-the-branches-meet-the-conflict) teaches it, where parallel deliveries meet.

## Undoing a delivery

`git revert <commit>` makes a new commit that undoes an earlier one, and keeps the history: the delivery and its undoing are both there to read.[^git-revert]

On trunk, right after `f16f83b`, `git revert f16f83b` would undo `cancel-appointment` whole, its page included, since they are one commit.
Later commits that change the same lines make the revert stop with a conflict, the same as a merge's ([chapter 18](18-worktrees.md#when-the-branches-meet-the-conflict)).

A merge commit has two parents, so git must be told which side to keep.
`git revert -m 1 846e337` keeps parent 1, `main` as it was, and undoes everything the second parent brought: #246's seven commits, in one new commit.
What it would undo is the difference between parent 1 and the merge:

```
git diff --stat 846e337^1 846e337 | tail -1
```

```text
 19 files changed, 533 insertions(+), 94 deletions(-)
```

The git documentation adds one caution: once a merge is reverted, a later merge of the same branch brings only the commits made on it after that merge.[^git-revert]

Nothing here was run in the clinic or the fork: you run it yourself in exercise 17.2.

## Trunk, and trunk-based development

The kit's trunk is one person committing on `main`, one delivery at a time.
Trunk-based development is a team practice of the same name: everyone merges small changes into the main branch "*at least once every 24 hours*", often through short-lived branches reviewed as pull requests,[^tbd] which in the kit's terms is a branch per delivery with small deliveries.

## git-flow

git-flow is the branching model Vincent Driessen published in 2010.[^git-flow]
It has two branches that live forever and three kinds that come and go:

* `master` (`main` today) holds only released versions, each merge into it a release, tagged.
* `develop` holds the next version as it is built.
* `feature/<name>` starts from `develop` and goes back into it with `--no-ff`, for his reason: "*Reverting a whole feature (i.e. a group of commits), is a true headache in the latter situation, whereas it is easily done if the `--no-ff` flag was used.*"[^git-flow] It is the table's reason: one merge commit, one revert.
* `release/<version>` starts from `develop` to prepare a release and merges into both `master` and `develop`.
* `hotfix/<version>` starts from `master` to fix a released version and merges into both.

In 2020 he added a note at the top of the post: for software delivered continuously, such as a web app, which is not rolled back and does not keep several versions in use, a simpler flow fits better; git-flow still fits software that ships explicit versions or keeps several in use.[^git-flow]

In the kit, git-flow is a branch per delivery whose branch starts from `develop` and is named `feature/<slug>`, and the Git slot of docs/05 says so.
Release and hotfix branches are the team's release work, which the kit does not model.
This book, one person, is on trunk; so was the clinic up to `book-v1/four-pieces`, and since its delivery `git-worktrees` it builds a worktree per delivery ([chapter 18](18-worktrees.md)); CLAHub, a team merging pull requests into `main`, is a branch per delivery.

## Key points

* Version control keeps every version of a project's files, of any kind, with who changed what and when; git, made in 2005 for the Linux kernel, is distributed, so every clone holds the whole history.
* A commit is a snapshot with its author, message and parents, named by a hash; a branch is a name that moves with each commit on it; a tag is a name that never moves.
* A fast-forward and a rebase leave a line of the branch's commits; a merge commit adds a commit with two parents; a squash merge leaves one new commit with one parent.
* `git revert` undoes a commit with a new commit and keeps the history; with a branch per delivery, merge by merge commit or squash, so one revert undoes the delivery (`git revert -m 1 <merge>` or `git revert <commit>`), as one commit does on trunk.
* The kit's trunk is one person on `main`; trunk-based development is a team merging small changes daily; git-flow fits software that ships explicit versions, and in the kit it is a branch per delivery from `develop`.

## Exercises

These exercises use your clone of the clinic at `book-v1/four-pieces`, on a branch of your own (`git switch -c mine book-v1/four-pieces`).
They are git commands you run yourself, since the agent never commits or merges.

### Exercise 17.1

Make a branch `try-merge` from `mine`, commit two small changes on it, and switch back to `mine`.
Bring `try-merge` into `mine` four times, going back with `git reset --hard book-v1/four-pieces` between tries: `git merge --ff-only`, `git merge --no-ff`, `git merge --squash` and a `git commit`, and `git rebase mine` on `try-merge` followed by `git merge --ff-only` on `mine`.
After each, read `git log --oneline --graph` and write how many reverts undo both changes.

### Exercise 17.2

Do the `--no-ff` try again, run `git revert -m 1 HEAD`, then `git diff book-v1/four-pieces`, and say why it prints nothing.
Then `git switch -c undo-cancel f16f83b`, `git revert HEAD`, and say why `git diff 442f88a` prints nothing.

### Exercise 17.3

In the fork at `book-v1`, find one pull request that landed as a merge commit and one that landed squashed, and write the command that undoes each.
Nothing is run.

[^pro-git-about]: Scott Chacon and Ben Straub, "About Version Control", *Pro Git*, 2nd ed., accessed 2026-09-30. <https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control>
[^pro-git-history]: Scott Chacon and Ben Straub, "A Short History of Git", *Pro Git*, 2nd ed., accessed 2026-09-30. <https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git>
[^gitattributes]: Git, "gitattributes", the documentation, the attribute `merge`, accessed 2026-09-30. <https://git-scm.com/docs/gitattributes>
[^pro-git-branching]: Scott Chacon and Ben Straub, "Basic Branching and Merging", *Pro Git*, 2nd ed., accessed 2026-09-30. <https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging>
[^pro-git-rebasing]: Scott Chacon and Ben Straub, "Rebasing", section "The Perils of Rebasing", *Pro Git*, 2nd ed., accessed 2026-09-30. <https://git-scm.com/book/en/v2/Git-Branching-Rebasing>
[^git-revert]: Git, "git-revert", the documentation, option `-m`, accessed 2026-09-30. <https://git-scm.com/docs/git-revert>
[^tbd]: Paul Hammant, "Trunk Based Development", section "Elaboration, Claims and Caveats", accessed 2026-09-30. <https://trunkbaseddevelopment.com/>
[^git-flow]: Vincent Driessen, "A successful Git branching model", 2010, with its "Note of reflection" of 2020. <https://nvie.com/posts/a-successful-git-branching-model/>
