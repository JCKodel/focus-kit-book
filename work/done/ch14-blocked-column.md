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
* [x] `ch14-back-to-open` is `[x]` and its rule matches the page before apply starts.
* [x] Both editions answer every Behaviour case, the board and key points agree, and no passage promises preservation of the previous column.
* [x] The chapter opens with its value, retains its evidenced gain, contains no filler or useful omissions, and every number/artifact remains sourced; historical private-case passages remain unchanged.
* [x] `make verify` is green and `make book` builds both editions; proof records both PDF paths for author review, followed by delivery review and archival per docs/05.

**Delivery.** Chapter 14's board section, both editions: a six-column board puts a `[?]` card in Waiting and moves it to `[ ]` or `[>]` on resolution; the chapter's three-column board, said to be an illustration and not a kit rule nor a feature of any board, places a `[?]` card by its resume phase, To Do for `propose`, Doing for `apply`, so the board keeps no memory of a column. `due-reminder`'s place on the drawn board is tied to its `resume: propose`; `reservations` blocked in definition and `my-loans` waiting on `fix-due-date` (PT `corrigir-devolucao`) show cases 3 and 4; resolution removes both suffixes and the tag. Key point rewritten. The board block, the Waiting section and every Case A passage are unchanged.

**Proof.** `ch14-back-to-open` is `[x]` (docs/06) and the chapter's Waiting section matches docs/05 §4. `make verify` green after the last edit. `make book` is run once by the batch driver; the PDFs to review are `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Review.** One read-only Opus reader over both chapter diffs against this page and docs/04: all Behaviour cases answered, no column memory left, editions agree. Points answered: "on three columns" read as all three columns, reworded to a three-column board; the illustration disclaimer merged into the placement sentence; `my-loans` waiting on the fix is no longer a hypothetical, since the Waiting section narrates it; the `reservations` Case A sentence moved above the blocked hypotheticals so it no longer follows a move out of Doing. No finding left for the queue.

**Decisions.** The six-column waiting column is named Waiting (PT Esperando); the drawn board is kept as it is, already consistent with the rule.
