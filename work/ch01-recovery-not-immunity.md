# ch01-recovery-not-immunity

**Objective.** A reader can recover a recorded decision after compaction or resumption by reopening its page and project documents.

**Behaviour.**
* After compaction omits a decision, the reader asks the agent to reopen the delivery page and relevant project documents and can recover the written decision.
* In a resumed or fresh session, the reader has the current files read before work continues instead of relying on a summary's completeness.
* A decision never written into a file has no guaranteed recovery path; a saved file itself does not mean its full text remains in every later model call.
* As the conversation grows, a document loaded near its start is still subject to context limits and loss of attention; the team gain is a source it can reread.

**Contract.** `book/en/01-how-agents-see.md` and `book/pt/01-how-agents-see.md`, chiefly When the window fills, Documents as memory, What the team gains and matching key points.
Use docs/03's context window, compaction, page and fresh session; add no terminology.
Keep the chapter's existing explanation and diagram unless their wording makes the same immunity claim.
Primary source already cited: Anthropic, Effective context engineering for AI agents, Compaction and Structured note-taking (<https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>).
Decision from docs/06: durable files preserve a recoverable record, not permanent inclusion or perfect recall.
No new case passage or number.

**States.** Inapplicable: chapter prose, no new screen.

**Visual reference.** Inapplicable: the existing book layout.

**Out of scope.** Host configuration, automatic rereading hooks and new diagrams: the reader needs an instruction, not a new tool.

**Done when.**
* [ ] Both editions instruct rereading after compaction/resumption and no sentence promises documents cannot leave the active context or lose attention.

* [ ] Both editions say the same thing, using docs/03's terms and Portuguese example names.
* [ ] The opening states the reader's value and the gain is supported; no filler added or useful explanation cut; every number and quoted artifact has its source (docs/00 and docs/04).
* [ ] `make verify` and `make book` pass; the author receives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the passage checks (docs/05 §5).
