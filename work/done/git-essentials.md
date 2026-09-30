# git-essentials

**Objective.** After chapter 17 the reader can say what version control keeps and why git was made, read a project's history as commits, branches and merges, merge a branch in each of the four ways git offers and say which of them keeps a delivery undoable in one step, undo a delivery with `git revert`, and say when trunk, a branch per delivery or git-flow fits a project.

**Behaviour.**

* The reader can say what version control keeps (every version of any kind of file, with who, when and why), why folders of `final`, `final final` files are not it, what git cannot merge (a binary file), that git is distributed, and who made git, when and why (amendment, below).
* The reader can say what a commit is (a snapshot with author, message and parents, named by a hash), what a branch is (a name that moves with each commit on it) and what a tag is (a name that never moves), and read `git log --oneline --graph` of a real history with them.
* The reader can say what each merge form leaves on the receiving branch, fast-forward, merge commit, squash merge and rebase followed by a fast-forward, and point to the first three in a real history (the clinic and CLAHub).
* The reader can say, for each form, how many commits `git revert` needs to undo a delivery whose branch held several commits, and so which forms keep chapter 6's unit of work (one merge, one revert): a merge commit (`git revert -m 1`) and a squash merge (`git revert`); a fast-forward and a rebase only when the branch held one commit.
* The reader can undo one delivery on trunk and one that landed in a merge commit, and check that the files are back.
* The reader can say that the kit's trunk is not trunk-based development, and what the latter is.
* The reader can say what git-flow's four kinds of branch are for, when its author says it fits and when it does not, and how a project on git-flow records it in the Git slot.

**Contract.**

Chapter 17, `book/en/17-git-essentials.md` and `book/pt/17-git-essentials.md`, new:

* Title: "Git essentials: trunk, branches, git-flow" / "O essencial de git: trunk, branches, git-flow" (docs/00 §Contents). No part heading, as chapter 14 opens Part III with none.
* Voice: instruction to the reader as "you" (docs/04 §Voice). Every git command in the chapter is one the person runs; the agent runs none of them but `git add`, `git status` and `git diff` (chapter 11).
* Tags and commits quoted, frozen: the clinic at `book-v1/four-pieces` (`e6653b5`); CLAHub at `book-v1`, the fork `JCKodel/clahub` (chapter 8). No clinic or fork changes, no run, no new tag.
* Sections, in order (headings may be reworded; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. Version control, and why git (amendment, below): version control and what it keeps, the designer's folder of `final` files, binary files and merge, centralized and distributed, git's history from *Pro Git* (1991 to 2002 patches, 2002 BitKeeper, 2005 its free status revoked, Linus Torvalds and the community, the five goals).
  3. Commits and the history. Commit, hash, parent, history; `git log --oneline` of the clinic, the output of `git log --oneline book-v1/four-pieces` whole (13 lines, one per commit), said: one commit per delivery, the page and its build in it (chapter 11's `git commit`, pointed to), and `git log --merges` prints nothing. `git show --stat f16f83b`, the stat lines only: the delivery `cancel-appointment` in one commit, `work/done/cancel-appointment.md` beside its code. This is trunk (chapter 6, pointed to; not repeated).
  4. Branches and tags. A branch as a moving name (`git switch -c <name>`, `git branch`), a tag as a fixed one, with the chapter tags the reader has checked out since chapter 5 as the example; `HEAD` in one sentence.
  5. Four ways to merge. For each: what the receiving branch holds afterwards, the command, and the history it leaves.
     * Fast-forward (`git merge --ff-only`) and rebase (`git rebase main`, then a fast-forward): no merge commit, the history a line; the clinic's line is what a fast-forward would leave. The rule of Pro Git: never rebase commits someone else already has.
     * Merge commit (`git merge --no-ff`): CLAHub, `git log --oneline --graph book-v1`, its first 20 lines, which hold both a merge commit and squash merges; then `git log --oneline 846e337^1..846e337^2`, the 7 commits of pull request #246 (`feat/214-structured-error-handling`), and `git show --no-patch --format='%h %p %s' 846e337`, its two parents. Pull requests are named as how CLAHub merges and pointed to chapter 20.
     * Squash merge (`git merge --squash`, then a commit): CLAHub's `9d1e666` (#308), one parent, the pull request number in its subject; the branch's commits are not in `book-v1`'s history.
     * Then one table, "Form | Lands on the receiving branch | Undo a delivery of several commits": fast-forward, the commits as they were, one revert per commit; merge commit, the commits and one commit with two parents, `git revert -m 1 <merge>`; squash merge, one new commit, `git revert <commit>`; rebase then fast-forward, the commits rewritten, one revert per commit. Said after it: with a branch per delivery, merge by merge commit or squash, so the delivery stays one unit of work (chapter 6's rule and chapter 9's `[>]`, pointed to).
     A conflict is named in one sentence and pointed to chapter 18.
  6. Undoing a delivery. `git revert <commit>` makes a new commit and keeps the history; on trunk, right after it, `git revert f16f83b` would undo `cancel-appointment`, page included (later commits that change the same lines make a revert conflict: named, pointed to chapter 18); on a merge commit, `git revert -m 1 846e337` undoes #246's 7 commits, `-m 1` naming the parent to keep, and `git diff --stat 846e337^1 846e337` is what it would undo, its last line quoted. Nothing is run in the clinic or the fork for this section: the reader runs it in exercise 17.2.
  7. Trunk, and trunk-based development. At most two sentences: the kit's trunk is one person on `main`; trunk-based development is a team merging small changes into `main` at least daily, often through branches that live a day or less, which in the kit's terms is a branch per delivery with small deliveries.
  8. git-flow. Its four kinds of branch from Driessen's post: `main` holds released versions, `develop` the next one, `feature/*` from `develop` and back with `--no-ff` (quoted: his reason, that it groups a feature's commits so the whole feature can be reverted, the same reason as section 4's table), `release/*` and `hotfix/*`. His 2020 note, paraphrased: for software delivered continuously, such as a web app, a simpler flow; git-flow for software that ships explicit versions or keeps several in use. In the kit: a branch per delivery whose branch starts from `develop` and is named `feature/<slug>`, recorded so in the Git slot; release and hotfix branches are the team's release work, which the kit does not model. The clinic and this book, one person each, are on trunk; CLAHub, a team merging pull requests into `main`, is a branch per delivery.
  9. Key points, at most five, one of them: with a branch per delivery, merge by merge commit or squash, so one revert undoes the delivery.
  10. Exercises (below).
* Excerpts: command output byte for byte, identical in both editions, fence `text`, each preceded by the command that printed it; commit hashes linked to the repository's commit page where the text names them.
* Numbers, and only these: the clinic's 13 commits and no merge at `book-v1/four-pieces`; #246's 7 commits; the parents' count of each form; the figures of the quoted `--stat` lines; the pull request numbers the subjects print; "at least once a day" from the TBD source; 1991, 2002 and 2005 and "thousands of parallel branches" from *Pro Git* (amendment).
* docs/03 terms: introduced (entered by this /propose): version control (amendment), commit, branch, tag, merge, fast-forward, merge commit, squash merge, rebase, revert, trunk-based development. Used: trunk, git-flow, pull request, stage, unit of work, delivery, page, chapter tag, guided project, brownfield project, slot. Portuguese: "commit de merge" for merge commit, "desfazer" for revert in prose; commit, branch, merge, fast-forward, squash merge, rebase, tag, as chapters 6, 9 and 11 already use them.
* Sources (`[^key]`, same keys in both editions):
  * `[^pro-git-about]`: *Pro Git*, "About Version Control" (amendment).
  * `[^pro-git-history]`: *Pro Git*, "A Short History of Git" (amendment).
  * `[^gitattributes]`: git documentation, `gitattributes`, the attribute `merge` (amendment).
  * `[^pro-git-branching]`: Scott Chacon and Ben Straub, *Pro Git*, 2nd ed., "Basic Branching and Merging", <https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging>.
  * `[^pro-git-rebasing]`: *Pro Git*, "Rebasing", "The Perils of Rebasing", <https://git-scm.com/book/en/v2/Git-Branching-Rebasing>.
  * `[^git-revert]`: git documentation, `git-revert`, the `-m` option, <https://git-scm.com/docs/git-revert>.
  * `[^tbd]`: Paul Hammant, trunkbaseddevelopment.com, <https://trunkbaseddevelopment.com/>.
  * `[^git-flow]`: Vincent Driessen, "A successful Git branching model", 2010, with its note of reflection of 2020, <https://nvie.com/posts/a-successful-git-branching-model/>.
  * The clinic's and CLAHub's commits are linked in the text, with no note (docs/04).
* Exercises, in your clone of the clinic at `book-v1/four-pieces`, on a branch of your own; these are git commands you run yourself, since the agent never commits or merges:
  * 17.1 Make a branch `try-merge`, commit two small changes on it, and bring them into your branch four times, from the same starting point each time (`git reset --hard` back to it between tries): `--ff-only`, `--no-ff`, `--squash` and a commit, `git rebase` then `--ff-only`. After each, read `git log --oneline --graph` and write how many reverts undo both changes.
  * 17.2 After the `--no-ff` try, run `git revert -m 1 HEAD`, then `git diff book-v1/four-pieces` and say why it prints nothing. Then `git switch -c undo-cancel f16f83b`, `git revert HEAD`, and say why `git diff 442f88a` prints nothing.
  * 17.3 In the fork at `book-v1`, find one pull request that landed as a merge commit and one that landed squashed, and write the command that undoes each. Nothing is run.
  Their answers are derived at the tags and recorded in What happened for the `exercise-answers` appendix.
* Documents: docs/03 gains the ten terms above (this /propose). docs/06: `git-essentials` `[>]` (this /propose), `[x]` by /apply. docs/00 §Contents already names chapter 17. No ADR.

**Out of scope.**

* Merge conflicts, their markers and who resolves them: chapter 18, where parallel deliveries meet.
* Worktrees and parallel agents: chapter 18.
* Why the person commits and the agent stages, and reviewing a staged change: chapter 19.
* Pull requests, their reviews, GitHub's merge buttons and branch protection: chapter 20.
* Switching the clinic off trunk, a run, a new tag: its history already shows trunk and CLAHub's shows branches.
* A run of git-flow: no repository of the book uses it; its source is the post.
* `git cherry-pick`, `git stash`, `git reset` beyond exercise 17.1's reset, interactive rebase, submodules, hooks, remotes and `push`/`pull` beyond what chapters 5 and 11 already use: not what a delivery needs (docs/00, not a git manual).
* GitHub flow by name: the kit's branch per delivery is its shape; chapter 20 has GitHub.
* Ninjobs: its trunk is chapter 6's and 4's story, not repeated.

**Done when.**

* [x] Both editions written, same file name and heading structure, opening with the Objective in at most three sentences; no draft marker.
* [x] Every command output shown matches a run of the same command at `book-v1/four-pieces` or at the fork's `book-v1`, byte for byte, checked by script, in both editions: `14 matched, 0 failed`.
* [x] Exercise answers and the table's revert counts derived from the histories and the git documentation, not run: the agent commits and merges nowhere, a throwaway clone included; in What happened.
* [x] No filler and nothing useful cut; every number cites its source.
* [x] `make verify` green, the link check and the disclosure scan included.
* [x] `make book` builds; both PDF paths given to the author.
* [x] docs/06 line `[x]`, page in `work/done/`, staged, commit message suggested.

**What happened.**

* Written as the Contract says, sections in its order; section 4 has an H3 per form and a fourth, "The four side by side", for the table. Headings: "Commits and the history", "Branches and tags", "Four ways to merge", "Undoing a delivery", "Trunk, and trunk-based development", "git-flow".
* Diverged from the page, each to match the source or the run:
  * git-flow has five branches, not "four kinds": Driessen's two main branches (`master`, `develop`) and three kinds of supporting branch (feature, release, hotfix). The chapter says "two branches that live forever and three kinds that come and go".
  * Driessen's post names `master`; the chapter says "`master` (`main` today)" once.
  * The TBD source says "at least once every 24 hours", not "at least once a day"; the chapter quotes it. "Branches that live a day or less" is not on the cited page, and its short-lived branches page says "a couple of days"; the chapter says "short-lived branches", with no duration and no second note.
  * `git show --stat f16f83b`, "the stat lines only", is shown as `git show --stat --format= f16f83b`, which prints only those lines, so the output under the command is whole.
  * The graph is shown as `git log --oneline --graph book-v1 | head -20` (`-20` would limit commits, not lines), and the `--stat` of `846e337` as `git diff --stat 846e337^1 846e337 | tail -1`, so each fence is the whole output of the command above it.
  * The merge subject prints `from clahub/feat/214-structured-error-handling`, quoted as printed.
  * The `--no-ff` quotation is Driessen's sentence "Reverting a whole feature (i.e. a group of commits), is a true headache...": its neighbour carries an em dash.
  * Added, from the `-m` option of `git-revert`: once a merge is reverted, a later merge of the same branch brings only the commits made after it; one sentence, as a reader who reverts a merge meets it next.
  * The graph's commits above the merges are called squash merges by what the reader can see (one parent, a pull request number in the subject), with no count.
* Chapters 18 and 20 do not exist yet: named in plain text, not linked.
* Excerpt check, a one-off Python script, not kept (each `text` fence against the command fence before it, run in the clinic or the fork, non-tty): `14 matched, 0 failed` (7 per edition); `git log --merges book-v1/four-pieces` printed 0 bytes. The third one-off excerpt check after chapters 15 and 16: a candidate line for a kept check, not this delivery.
* Exercise answers and the table's counts, derived from the histories and the git documentation, nothing run, no throwaway clone:
  * Table: a fast-forward and a rebase land the branch's commits on the receiving branch with no commit of their own, so undoing N commits takes N reverts; a merge commit is one commit whose `-m 1` revert returns the tree to parent 1; a squash merge is one commit with one parent, one `git revert`.
  * 17.1. `mine` has no commit of its own after the tag, so: `--ff-only` moves `mine` to `try-merge`, a line of two commits, 2 reverts; `--no-ff` makes a merge commit though a fast-forward was possible, the graph shows two lines joining, 1 revert (`git revert -m 1 HEAD`); `--squash` and a commit, one commit with one parent, 1 revert; `git rebase mine` on `try-merge` has nothing to rewrite (it already starts at `mine`) and `--ff-only` then gives the same line as the first try, 2 reverts.
  * 17.2. The merge's parent 1 is `book-v1/four-pieces` (`e6653b5`), so `git revert -m 1 HEAD` makes a commit whose tree equals the tag's, and `git diff book-v1/four-pieces` prints nothing. `f16f83b`'s one parent is `442f88a` (`git show --no-patch --format='%h %p %s' f16f83b`), so reverting it at its own branch tip gives the tree of `442f88a`, and `git diff 442f88a` prints nothing.
  * 17.3. Merge commit: #246, `git revert -m 1 846e337` (or #291, #297, #298, #299 of the graph); squashed: #308, `git revert 9d1e666` (or #300 to #307).
* Proof: no screenshot (docs/05, a chapter delivery with no new kind of content). `make verify` green, the link check and the disclosure scan included. `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` (and both EPUBs), with the known `user-select` warnings only.
* Documents: docs/03 gained the ten terms at /propose; /apply corrected the trunk-based development row to the source ("at least once every 24 hours", short-lived branches, no duration). docs/06 `[x]`. No ADR.
* Amendment, after the first /apply, before any commit, at the author's request: the chapter did not say what version control is. Developers often know git as the place the code lives, not as every version it has had; designers keep versions as `final`, `final final` files in folders and gain from it too; and the chapter said nothing of why git exists or who made it. Added in the same delivery, as the page was not committed: the section "Version control, and why git" before "Commits and the history", the Objective and opening widened, a Behaviour line, three notes (`[^pro-git-about]`, `[^pro-git-history]`, `[^gitattributes]`), the term version control in docs/03, and a key point (the old points on merging by delivery and on `git revert` joined, to stay at five).
  * The `logo final.psd` file names are an illustration of the practice *Pro Git* describes ("copy files into another directory"), not an artifact of a run; the Portuguese uses the names a Brazilian team writes (`logo versão final mesmo.psd`).
  * "repository" is not entered in docs/03: that term is the FOCUS piece; the text says "the git repository" once, in its everyday sense, as earlier chapters do.
  * The binary merge sentence follows `gitattributes`: an unset `merge` takes the current branch's version and declares a conflict, "suitable for binary files".
  * *Pro Git*'s "incredibly error prone" is paraphrased, not quoted: the prose rule `intensifier` finds "incredibly" in a quotation too (verify red once, on both editions' line 14).
  * `make verify` green again, the excerpt check again `14 matched, 0 failed`, `make book` rebuilt both editions.
