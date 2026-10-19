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
* [x] Both editions instruct rereading after compaction/resumption and no sentence promises documents cannot leave the active context or lose attention.

* [x] Both editions say the same thing, using docs/03's terms and Portuguese example names.
* [x] The opening states the reader's value and the gain is supported; no filler added or useful explanation cut; every number and quoted artifact has its source (docs/00 and docs/04).
* [x] `make verify` and `make book` pass; the author receives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the passage checks (docs/05 §5).

**Built.** Both editions of chapter 1. The opening adds what to have the agent read again after a compaction or when a session is resumed. The context window: what the agent reads stays in the window until the session ends or a compaction summarizes it. The first practice of What this changes in your project (the passage the contract calls Documents as memory): the host loads the rules file at the start of every session; a decision in a file can be read again at any point; a file does not stay whole in the window, a document read early ends up in the middle and a compaction summarizes it; Anthropic's structured note-taking quoted from the cited source; after a compaction, a resumed session or work that drifts from a decision, ask the agent to reopen the delivery's page and the documents; a decision never written has nothing to reopen. What the team gains: the person has the agent read the decision again instead of trusting what it remembers; the evidence is the measured loss and the practice Anthropic recommends. Key points: the reread instruction gets its own bullet.

**Divergences.** None. No Case A or Case B passage or number was used or changed.

**Decisions.** The chapter has no section named Documents as memory; the matching text is the first practice under What this changes in your project, and no heading was added. The sentence in The context window that said files stay in the window for the rest of the session made the same immunity claim and was changed. The source's "five most recently accessed files" detail is Claude Code behaviour, outside this page, and was left out. "Structured note-taking" is quoted, not adopted as a term.

**Proof.** `grep` for "cannot fall", "loaded whole", "não pode cair", "carregada inteira" and "carrega inteiros" in both chapter files finds nothing. The two quotes match the Structured note-taking section of the cited Anthropic article, read on 2026-10-18. `make verify` green after the last edit; `make book` is run once by the batch driver for `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, for the author's passage checks.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of both chapter files against this page, docs/03 and docs/04. Points: (1) "stays there for the rest of the session" still promised files stay in the window: now "until the session ends or a compaction summarizes it". (2) The gain said the agent rereads by itself and covered a buried decision the instruction did not: the person has the agent read it again, and the instruction adds work that drifts from a decision. (3) "the remedy" overstated the source: "recommends the same practice for agents". (4) A recommendation is not measured evidence: the evidence sentence separates the measured loss from the recommended practice. (5) "not text the window keeps" was absolute and repeated the earlier sentence: folded into "a file does not stay whole in the window", and the key point says "is sure to keep". (6) "page" before its introduction: kept, the word is plain and practice two explains it right after. (7) Loss of attention only implied: "in the middle, where the model uses it worst". (8) pt "soterra": replaced by "se afasta dela". (9) The opening named only compaction: it names resuming too. Verify ran again after the fixes.

```commit
docs(ch01-recovery-not-immunity): reread decisions after compaction

- A file is a record to read again, not text the window keeps whole
- After a compaction or a resumed session, reopen the page and documents
- What the agent reads stays until the session ends or a compaction
- The gain: the person has the agent read the decision again

work/done/ch01-recovery-not-immunity.md
```
