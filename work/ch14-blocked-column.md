# ch14-blocked-column

**Objective.** After chapter 14 the reader can place a waiting line and its resolved state on a board using the queue's recorded phase, without needing a remembered previous column.

**Behaviour.**
* Given a six-column board, a `[?]` line appears in Waiting with its reason; after resolution, `resume: propose` yields `[ ]` and `resume: apply` yields `[>]`, each in its own column.
* Given the chapter's three-column projection, a waiting line with `resume: propose` appears in To Do tagged blocked, and one with `resume: apply` in Doing tagged blocked; its queue suffix, not a saved column, determines placement.
* Given a line blocked during definition after it had appeared in Doing as `[~]`, its `resume: propose` means the three-column projection now places it in To Do tagged blocked. On resolution it stays in To Do as `[ ]`, without the tag, retaining its draft.
* Given a line blocked while building, its `resume: apply` means Doing tagged blocked, then Doing as `[>]` on resolution, without falsely showing an active `[*]` build.
* Given an ordinary `after` dependency on an unstarted line, its card has no blocked tag; resolving a waiting reason removes both waiting suffixes and the tag.

**Contract.** Files: `book/en/14-queue-states.md` and `book/pt/14-queue-states.md`, board explanation, illustrated board and affected key points. Sources: docs/05 §4 as migrated by `kit-2026-10-18-1`, and the explicit resumption contract of `work/ch14-back-to-open.md`; retain existing kanban references. Terms: kanban board, mark and draft page from docs/03. The six-column board maps each mark directly; the three-column board is the chapter's illustrative projection, whose waiting placement is derived from `resume`. State this as the illustration's mapping, not a mandatory kit rule or an asserted feature of FACE or Azure DevOps. No hidden state or board API is introduced.

**States.** Inapplicable: an existing textual board illustration, no implemented screen.

**Visual reference.** Existing three-column text board in both editions, kept within docs/04's block width; no new diagram type.

**Out of scope.** No board software or integration changes, no new claim about Case A's historical board, no change to the waiting transition itself (`ch14-back-to-open` owns it), no recovery rule for malformed legacy lines.

**Decisions.** The user authorized definition before `after ch14-back-to-open` completes; that dependency still gates apply. Mapping a blocked card by its recorded resume phase is the minimal stateless projection consistent with that contract, replaces the unsupported remembered-column promise, and is explicit for the person's review.

**Done when.**
* [ ] `ch14-back-to-open` is `[x]` and its rule matches the page before apply starts.
* [ ] Both editions answer every Behaviour case, the board and key points agree, and no passage promises preservation of the previous column.
* [ ] The chapter opens with its value, retains its evidenced gain, contains no filler or useful omissions, and every number/artifact remains sourced; historical private-case passages remain unchanged.
* [ ] `make verify` is green and `make book` builds both editions; proof records both PDF paths for author review, followed by delivery review and archival per docs/05.
