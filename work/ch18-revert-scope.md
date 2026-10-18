# ch18-revert-scope

**Objective.** After chapters 18 and 19 the reader can distinguish reverting a delivery's tracked changes from undoing effects it already caused outside Git.

**Behaviour.**
* Given one delivery committed on trunk, or integrated as one merge, the reader knows which tracked change the existing revert command reverses; the one-change promise is preserved with its scope stated.
* Given a migration already run, reverting its migration file does not undo the database change; the delivery's Done when must say how the effect is undone, or that it is not.
* Given a reminder already sent, reverting its sending code does not recall the message; the page explicitly records the irreversible effect instead of promising a universal rollback.
* Given later work touching the reverted lines, the existing conflict warning still applies; one unit of work does not guarantee a conflict-free revert.

**Contract.** Files: both editions of `18-git-essentials.md` and `19-worktrees.md`; opening/value wording where needed, unit-of-work and revert explanations, gains and key points wherever they promise one-step undo. Terms: unit of work, delivery, page and revert from docs/03. Source: focus-kit SETUP.md 2026.10.18.1 Git slot, pinned in `work/kit-2026-10-18-1.md`, and chapter 18's existing Git revert reference. The migration owns docs/05's Git slot and docs/03. Preserve `git revert <commit>` and `git revert -m 1 <merge>` with their existing explanation. Use hypothetical lending-library migration and reminder examples, identified as written for the chapter; no actual external operation or API change.

**States.** Inapplicable: no new screen.

**Visual reference.** Inapplicable: existing layout.

**Out of scope.** No rollback tool, database-specific migration recipe or actual message; branching strategy corrections belong to `ch18-kit-branches`, and commit authority to `agent-commits-asked`.

**Decisions.** The user approved defining against the migration's contract while keeping its `after` gate for apply. docs/00's beginner audience needs two concrete external effects, not a new disaster-recovery chapter. Existing examples and evidence remain; qualify broad promises consistently without repeating the full explanation in both chapters.

**Done when.**
* [ ] The migration is `[x]` and its owning rule agrees before apply starts.
* [ ] Both editions answer every Behaviour case and no affected one-step claim implies reversal of external effects.
* [ ] Both chapters open with their value, retain evidenced gains, contain no filler or useful omissions, and every number/artifact remains sourced; no private-case change.
* [ ] `make verify` is green and `make book` builds both editions; proof records both PDF paths for author review, followed by delivery review and archival per docs/05.
