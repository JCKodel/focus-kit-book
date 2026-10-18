# ch18-kit-branches

**Objective.** After chapter 18 the reader can distinguish the kit's delivery branches from other Git strategies while understanding how each integration is undone.

**Behaviour.**
* Given the kit's branch-per-delivery choice for `lend-book`, the reader creates or reuses the branch named for the slug and integrates the completed page and build in one merge, reversible with the merge revert already taught.
* Given squash merge, the reader can explain its single resulting commit and ordinary revert, but does not infer that the kit prescribes squash as its branch integration strategy.
* Given git-flow, the reader identifies `develop`, feature, release and hotfix branches as that external workflow, not as names or a fourth strategy installed by focus-kit.
* Given a worktree strategy, the chapter preserves the documented prefixed branch and directory convention through its chapter 19 pointer rather than confusing it with the plain slug branch.
* The Choosing list, trunk-based-development explanation and opening no longer promise that every strategy they teach is a kit choice; the four Git integration forms remain taught.

**Contract.** Files: `book/en/18-git-essentials.md` and `book/pt/18-git-essentials.md`. Sections: opening, One delivery/undo explanation, Four ways to merge where attribution needs it, trunk comparison, git-flow, Choosing and affected key points. Sources: installed `brainstorm/references/documents.md` Choices; focus-kit SETUP.md 2026.10.18.1 Choices (local uncommitted source read 2026-10-18); docs/03 (unit of work), docs/05 §5 Git. Keep existing primary Git/Pro Git, trunk-based-development and Driessen notes for the external practices; no new factual claim about those tools is needed. Decision: retain useful Git instruction and correct attribution, with no change to this book's trunk choice.

**States.** Inapplicable: chapter prose, no new screen.

**Visual reference.** Inapplicable: existing book layout, no new visual content.


**Out of scope.** Changing repository Git strategy, implementing a merge, external side-effect undo (`ch18-revert-scope`), agent commit authorization and chapter 19 worktree layout.

**Done when.**
* [ ] Every Behaviour scenario is checked against the English and Brazilian Portuguese text; both editions are changed in the same delivery.
* [ ] Each chapter opens with its reader value and retains its evidenced team gain; no filler and nothing useful cut; every number and quoted artifact remains sourced.
* [ ] Terms follow docs/03, examples remain identified as written for the chapter, no em dash or private detail is introduced, and no run is narrated (docs/04).
* [ ] `make verify` is green and `make book` builds both PDFs and EPUBs; the page records the results and gives the author both PDF paths for review (docs/05 §5).
* [ ] All commands and existing sourced historical numbers retain their meaning; no private case passage is added or changed.
