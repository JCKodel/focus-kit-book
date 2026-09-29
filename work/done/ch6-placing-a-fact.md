# ch6-placing-a-fact

**Objective.** A reader of chapter 6 decides which document a new fact belongs in, because the chapter gives one question per document, works one real fact through them, and has an exercise with answers the reader can check, as its opening promises.

**Behaviour.**

* A new section, between "AGENTS.md" and "Living documents", gives the questions that place a fact, in the order of the Contract, and says what `AGENTS.md` is for in that decision.
* The section works one real fact of the clinic through the questions: "every appointment lasts the same length", which lands in three places, each holding a different fact: the term and the rule in docs/03, the choice and why the alternatives lost in ADR-0005, the question nobody closes alone in docs/00.
* The reader sees that one sentence of a brief can hold several facts, and that "one place per fact" means each of them has one owner, not that the sentence lands whole in one document.
* The reader can follow the example without chapter 7: the text first says what the clinic is and where the documents come from (tag `book-v1/brainstorm`, written in chapter 7).
* Exercise 6.5 lists five other clinic facts; the reader places each one and checks the answer against the clinic's documents at `book-v1/brainstorm`.
* Key points say how a fact is placed.
* The opening is unchanged: the chapter now keeps it.
* Finding F6 of the M3 review is settled.

**Contract.**

* Files: `book/en/06-the-documents.md` and `book/pt/06-the-documents.md`.
* New section: `## Where a new fact goes` / `## Onde entra um fato novo`, after `## AGENTS.md`, before `## Living documents`.
* The questions, in this order, each answered by the first one that fits:
  1. Is it a choice between alternatives, with a reason someone may want to revisit? An ADR holds the choice and the reason; the document it governs holds the result (docs/01 for the architecture, docs/05 for the git strategy), as "The two choices" already says.
  2. Is it what the product is, for whom, what it is not, a value, or something nobody closes alone? docs/00.
  3. Is it a word, an entity, or a rule that always holds for the data? docs/03.
  4. Is it how the thing is built: stack, where code goes, data access, errors, environments? docs/01, or docs/02 when a server holds the rule.
  5. Is it how code or text is written: naming, style, tests, commits? docs/04.
  6. Is it a fact of this project that the commands read: verify, environments, git? docs/05 §5, a slot.
  7. Is it work to do? docs/06 holds the line; the page in `work/` holds the delivery.
  `AGENTS.md` is never the answer: a line there only points at the owner, when every session must keep the fact in mind.
* Worked example, real, from `JCKodel/focus-kit-clinic` at tag `book-v1/brainstorm`, excerpts as whole units (docs/04, "Context before an excerpt"):
  * docs/03, the row `| Appointment length | `slotMinutes` | The fixed length of every appointment in the clinic; 30 by default. |` and invariant 2 (an appointment starts on the grid of `slotMinutes`).
  * `docs/adr/ADR-0005-fixed-appointment-length.md`: one length for the whole clinic, against a length per clinic, per professional or per service; said in prose or quoted from its Decision.
  * docs/00, Open decisions: "What happens to future appointments when the owner changes the appointment length."
* Exercise 6.5, the five facts, and where each lives at `book-v1/brainstorm` (for /apply to check, not printed in the chapter):
  1. Each test file sits next to the file it tests: docs/04, Tests.
  2. `SlotTaken` is the refusal when a booking asks for a time that is not free: docs/03, the table.
  3. A client has no account and proves who they are with a booking code: ADR-0004 for the why, docs/00 "No client accounts", docs/03 the Client row, and a line of `AGENTS.md` that points.
  4. Biome formats and lints: docs/01, the stack table (the choice); docs/04, Style (the rule that formatting is never discussed).
  5. The project works on trunk: docs/05, the Git slot, and ADR-0003.
  The exercise links the tag's tree on GitHub.
* Terms of docs/03: none new; uses project documents, ADR, rules file, open decision, slot, delivery, page, guided project, chapter tag.
* Sources: the clinic's documents at `book-v1/brainstorm`, already cited by chapter 7; no new source note unless the tag's tree is not linked in the text.
* Cases: none; the guided project only.

**Out of scope.**

* A new term "fact" in docs/03: the chapter uses the word in its plain sense.
* Chapter 7 or its exercises: the new exercise checks against the tag, not against chapter 7.
* A borderline example from this book (the `useful-notes` delivery): the clinic's example is closer to the reader's project.
* The docs/04 description's "section 6": that is `ch6-section-reference`.

**Done when.**

* [x] Both editions written; the section opens with its value, no filler and nothing useful cut.
* [x] Every excerpt and every place named in the example and in exercise 6.5 matches the clinic at `book-v1/brainstorm`.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* The fact is not in the clinic's brief: in chapter 7's run the agent asked how long an appointment is and proposed one fixed length, and the answer was "your call" (`work/done/brainstorm-run/questions.md`, round 2). The chapter says so, and says "one sentence of a brief or of a conversation can hold several facts", so nothing shown claims the brief said it.
* The three excerpts are quoted whole at the tag: docs/03's header with the Appointment length row, invariant 2, ADR-0005's Decision, and the Open decisions line of docs/00. ADR-0005's Context (per clinic, per professional or per service; simplicity) is said in prose. Each excerpt is linked to its file at the tag, so no new source note; the exercise links the tag's tree.
* The Portuguese edition translates the clinic's excerpts and says before them that the originals are in English (docs/04, Evidence); the clinic's Slot is "horário livre" there, since "slot" in this book's docs/03 is the process slot.
* Key points stay at five (docs/04, Chapter shape): the `AGENTS.md` bullet became the bullet on placing a fact, which keeps that `AGENTS.md` only points; "the commands hold no fact of the project" moved into the docs/05 part of the second bullet, as "where the commands read every fact of the project".
* The new section is the sixth H2, so the docs/04 description's "section 6" now points at it and not at "Living documents". Left as is, out of scope by name: `ch6-section-reference`, the next line of the queue, fixes it.
* The exercise asks also whether each fact holds more than one, since facts 3 and 4 land in several places; the answers are not printed, as planned.
* Proof: `make verify` green; `make book` built both PDFs, and the new section appears in each.
* No new term, rule or ADR: the delivery changes no document other than the chapter and the queue.
