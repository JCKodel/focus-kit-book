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
* [x] Every Behaviour scenario is checked against the English and Brazilian Portuguese text; both editions are changed in the same delivery.
* [x] Each chapter opens with its reader value and retains its evidenced team gain; no filler and nothing useful cut; every number and quoted artifact remains sourced.
* [x] Terms follow docs/03, examples remain identified as written for the chapter, no em dash or private detail is introduced, and no run is narrated (docs/04).
* [x] `make verify` is green and `make book` builds both PDFs and EPUBs; the page records the results and gives the author both PDF paths for review (docs/05 §5).
* [x] All commands and existing sourced historical numbers retain their meaning; no private case passage is added or changed.

**Built.** Chapter 18, both editions: the opening offers the kit's three strategies and tells trunk-based development and git-flow apart as practices outside the kit; "One delivery, one step to undo" says `/propose` creates or reuses the branch named after the slug and the person merges page and build in one merge, here a merge commit undone with `git revert -m 1 <merge>`, with `lend-book` (pt `emprestar-livro`), written for the chapter, as three commands; the squash merge leaves one step with an ordinary revert but the kit asks only for one merge; the trunk section calls trunk-based development not a kit strategy; the git-flow section gives `develop`, `feature/`, `release/` and `hotfix/` to Driessen, not the kit; Choosing holds the slot's three strategies, the worktree bullet names `.focus-kit/worktrees/<slug>/` on `focus-kit/<slug>` unless the slot names another folder or prefix, a plain `<slug>` branch being someone else's, and git-flow moves outside the slot; the last key point follows. The four merge forms, their sections, the footnotes and every source are unchanged.

**Proof.** `make verify` green after the last edit. `make book` and the two PDF review paths are the batch driver's, which builds once at the end.

**Delivery review.** A read-only Opus agent read `git diff HEAD` of both chapter files, the page, docs/04, docs/03, AGENTS.md and the kit's Git choice, and confirmed every Behaviour case in both editions. Points and answers:
* "Not the one the kit names" and "in one merge commit" claimed the kit names a merge commit, where the source says one merge: now "in one merge, here a merge commit" and "the kit asks only that the delivery reach `main` in one merge, and this chapter uses a merge commit".
* "What `/propose` runs" named a command the source does not: now "what `/propose` does for you".
* "Or by hand" is not in the kit's text: kept, since chapter 19 merges by hand from `main/` and the chapter teaches the command.
* The worktree bullet made only the prefix configurable: now "unless the slot names another folder or prefix".
* PT "pela pull request dele" against the book's masculine use: now "pelo pull request do branch"; "o roda como o seu próprio fluxo" now "o adota como fluxo próprio".

**Decisions taken alone.** git-flow keeps its taught section and fit, outside the slot; trunk-based development is framed as external with its closest kit answer; the squash merge stays as one of git's four forms; the example's create and merge commands are separated by a blank line.

```commit
docs(ch18-kit-branches): tell git-flow and squash apart from the kit

- ch18: the kit's three strategies; git-flow and TBD outside the kit
- ch18: lend-book branch by slug, one merge, git revert -m 1
- ch18: squash is git's form, not what the kit asks for
- ch18: worktree bullet keeps the prefixed branch and folder
work/done/ch18-kit-branches.md
```
