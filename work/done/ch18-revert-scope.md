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
* [x] The migration is `[x]` and its owning rule agrees before apply starts.
* [x] Both editions answer every Behaviour case and no affected one-step claim implies reversal of external effects.
* [x] Both chapters open with their value, retain evidenced gains, contain no filler or useful omissions, and every number/artifact remains sourced; no private-case change.
* [x] `make verify` is green and `make book` builds both editions; proof records both PDF paths for author review, followed by delivery review and archival per docs/05.

**Build.** Chapter 18, both editions: the opening adds saying on the page how what a delivery did outside git is undone, or that it is not; the line on page and build in one commit scopes "all of it" to what git holds; "Undoing a delivery" keeps `git revert <commit>` and `git revert -m 1 <merge>` with their explanation, says one step is not always a clean one beside the existing conflict warning, and adds one paragraph, after the merge revert so it covers both commands, on what either step does not undo, with two lending-library deliveries written for the chapter: `add-due-date` (`adicionar-data-de-devolucao`), whose database migration already ran, and `send-reminders` (`enviar-lembretes`), whose text messages went out; the gains and the first key point scope the one-command promise to what git holds. Chapter 19, both editions: the gains' "reverts alone" is scoped to git, pointing to chapter 18 for the rest; the full explanation is not repeated.

**Gate.** `kit-2026-10-18-1` is `[x]` in docs/06; docs/05 §5's Git slot and docs/03's unit of work already say that the step undoes what git holds and that a delivery acting outside git says in its Done when how that is undone, or that it is not. No shared file changes.

**Proof.** `make verify` green after the last chapter edit. A search of both editions of chapters 18 and 19 for one-step, one-command and revert claims leaves only git facts or claims now scoped. `make book` and the PDF paths are the batch driver's, run once at the end: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Review.** One read-only Opus agent over the four chapter files and this page. Applied: the paragraph moved after the merge revert so it scopes both commands; "Revert is the undo for anything already shared" became "for any commit already shared"; Portuguese wording fixed in the gains ("ou que não há como desfazê-lo"), the paragraph ("ao contrário") and chapter 19's gains, the English matched. Declined: "undoes a delivery whole" on trunk, and chapter 18 line 15 and chapter 19 line 17, stay as they are, since they are git facts the next paragraph or chapter 18 scopes; the page asks not to repeat the explanation. `make verify` green again after the fixes.

**Decisions taken alone.** "Database migration" in the prose, since docs/03's "migration" is the kit's term; new slugs rather than chapter 14's `due-reminder`, whose Portuguese line is not at the same place; the reminder is a text message, as the library's reminders are elsewhere in the book.
