# ch19-batch-staging

**Objective.** After chapter 19 the reader can run a batch of proposals without staging their definitions and stage each complete delivery during its later `/apply`.

**Behaviour.**
* Given two free lines defined together, each `/propose` writes its page and mark without staging; existing index entries remain untouched.
* Given adjacent queue marks in one diff hunk, the reader does not mistake them for a conflict or stage a batch during definition.
* When `/apply` completes one of those deliveries, its session stages its own page, build and queue line, leaving the other proposal unstaged; the chapter places selective-patch instructions at this phase.
* Before the person commits, the index must hold only the delivery being committed; pre-existing entries from another session are reported rather than silently unstaged.
* A new `/apply` session can read an uncommitted proposal from the working tree, so no proposal commit is required to transfer it.

**Contract.** Files: `book/en/19-worktrees.md` and `book/pt/19-worktrees.md`. Section: the batch of proposes, its transition to applies and any summary that incorrectly assigns staging to `/propose`. Sources: installed propose skill (writes page; no staging step), installed apply skill (stages completed delivery), docs/05 §§2, 5 Git and 6; existing Git notes for `git add -p` and `git apply --cached` stay with the retained explanation. Decision: preserve the useful patch technique while making `/apply` its actor; no general ban on the person explicitly committing a branch is invented.

**States.** Inapplicable: chapter prose, no new screen.

**Visual reference.** Inapplicable: existing book layout, no new visual content.


**Out of scope.** The separate `ch19-commit-by-index` correction, agent commit authorization, conflict definition changes, worktree layout and real execution of a batch of applies.

**Done when.**
* [ ] Every Behaviour scenario is checked against the English and Brazilian Portuguese text; both editions are changed in the same delivery.
* [ ] Each chapter opens with its reader value and retains its evidenced team gain; no filler and nothing useful cut; every number and quoted artifact remains sourced.
* [ ] Terms follow docs/03, examples remain identified as written for the chapter, no em dash or private detail is introduced, and no run is narrated (docs/04).
* [ ] `make verify` is green and `make book` builds both PDFs and EPUBs; the page records the results and gives the author both PDF paths for review (docs/05 §5).
* [ ] The Case A question-delivery passage and published parallel-work measurement retain their evidence; any changed private passage is listed and author-approved (docs/00 OD-3).
