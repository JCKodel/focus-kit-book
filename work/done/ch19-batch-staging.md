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
* [x] Every Behaviour scenario is checked against the English and Brazilian Portuguese text; both editions are changed in the same delivery.
* [x] Each chapter opens with its reader value and retains its evidenced team gain; no filler and nothing useful cut; every number and quoted artifact remains sourced.
* [x] Terms follow docs/03, examples remain identified as written for the chapter, no em dash or private detail is introduced, and no run is narrated (docs/04).
* [x] `make verify` is green and `make book` builds both PDFs and EPUBs; the page records the results and gives the author both PDF paths for review (docs/05 §5).
* [x] The Case A question-delivery passage and published parallel-work measurement retain their evidence; any changed private passage is listed and author-approved (docs/00 OD-3).

**Built.** In both editions of chapter 19, "Proposing in a batch" now says each `/propose` writes its page and mark and stages nothing, leaving the index as it was, and that `/apply` reads an uncommitted proposal from the folder, so no commit hands a page on. The shared queue hunk is no conflict and no reason to stage during definition. The `git add -p` and `git apply --cached` technique moved to the applies that follow, where each `/apply` stages its page, build and queue line and leaves the other proposals unstaged; already staged entries of another session are reported and left as they were. "The queue" in "When parallel stops paying" and the last key point now give staging to `/apply`.

**Decisions.** No question was left open by the page; the Case A question-delivery passage and the parallel-work measurement are unchanged, so no private passage needs approval.

**Review.** One read-only Opus review over both chapter files found no blocking point and four minor ones, all fixed: "add no rule" became "add no rule of their own" before the staging sentence; the Portuguese "Nenhum commit passa a página adiante, também" became "Nem é preciso um commit para passar a página adiante"; "The queue" gave staging to every session and now gives it to each `/apply`; the staged queue diff now reads "this delivery's changes alone", since an `/apply` may also add lines to docs/06.

**Proof.** `make verify` green after the last edit. `make book` runs once at the end of the batch, by the driver; the PDFs for review are `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

```commit
docs(ch19-batch-staging): stage batch deliveries in /apply, not /propose

- /propose in a batch writes page and mark and stages nothing
- /apply reads the uncommitted proposal from the folder
- selective patch staging of the queue line moved to /apply
- another session's staged entries are reported, left as they were
- both editions

work/done/ch19-batch-staging.md
```
