# the-governor

**Objective.** After chapter 13 the reader can ask the governor question of anything that wants to enter their process and of every step already in it, accept only an answer that names an error that happened, and say what the process does not have and what does each of those jobs instead.

**Behaviour.**

* The reader can state the question (which concrete error would it have caught?) and say why the answer must name an error that happened, not one that could: every step is paid by every delivery from then on, and a possible error justifies anything.
* The reader can tell a "no" from a "yes": the check the agent added to the clinic's `skeleton` page (chapter 10) named no error and left; the parity check of this book's note keys and the database lint of Ninjobs each named one and entered.
* The reader asks the same question of what is already there, and removes a step that names no error; the Ninjobs story shows the rule that keeps a list of exceptions honest (an entry with no live warning fails too).
* The reader can list the seven things the process does not have and, for each, say what does its job: formal spec → the page; spec delta → the documents changed in the same delivery; change folder → `work/<slug>.md`, then `work/done/`; numbered tasks → the Behaviour lines; gate before implementation → the person reading the page; specialized subagent → one agent that reads the documents; a tool the deliveries did not ask for → the governor itself.
* The reader can say why reading the page before `/apply` (chapter 10) is not a gate (a person decides; the process runs no check) and why the second agent that read the `skeleton` page (chapter 10) is not a specialized subagent (the author chose a reader once; no step of the process calls one).
* The reader applies the same question to code: an abstraction is written on the second concrete occurrence and the delivery names the first, as the clinic's lines `route-errors` and `minutes-of` do (chapter 12).

**Contract.**

Chapter 13, `book/en/13-the-governor.md` and `book/pt/13-the-governor.md`:

* Title: "The governor, and what the process does not have" / "O regulador, e o que o processo não tem".
* Voice: instruction to the reader as "you"; Ninjobs and this book told in the first person (docs/04 §Voice).
* Sections, in order (headings may be reworded; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. The question. The kit's rule, paraphrased and named in plain words (`SETUP.md`, the docs/05 template, §7 "What this process does not have"), no note. Why an error that happened: a step costs every delivery that follows; chapter 4 already showed checks that never failed on an error in the product, pointed to in one sentence, its numbers not repeated.
  3. A "no" and a "yes". The "no": chapter 10's import check, one sentence and an internal link, not quoted again. The "yes" in this book: `make verify` gained the parity check of note keys because chapter 8 cited `[^analyze-run]` 13 times in English and 14 in Portuguese; the page names the error, the check came after it.
  4. Asking it again of what is there (Ninjobs). One story, how it was, what went wrong, where it went: on the restart a homegrown check on the code's form stayed out, since no error in the product had ever failed it; a warning of the database vendor's own lint sat in a report nobody opened while an index identical to another was written twice on every write, and no test saw it; on 2026-09-02 the vendor's lint entered `verify`, naming that index as its error; a new warning fails `verify`, and an allowlist entry with no live warning fails too, because a list with dead entries stops being read. Paraphrased from Ninjobs' ADR-0022, amendment of 2026-09-02. No vendor name, no name of the lint, of the homegrown check, of the index or of any table; no other check of that ADR; nothing that makes the architecture the cause (the cause is the tooling). The author approves the passage before the chapter is done.
  5. What the process does not have. The seven items of §7, each with what does its job (Behaviour, fourth line), one line each; then the two objections of the fifth Behaviour line, a sentence each.
  6. The same question in code. The rule "abstraction on the second concrete occurrence, and the delivery says which was the first" (as `SETUP.md` writes it in the text of `/apply` and in the AGENTS.md template), named in plain words, no note, shown on the clinic's milestone 2 lines `route-errors` and `minutes-of`, quoted from chapter 12's `queue.diff` (the first and the second copy they name). Short.
  7. Key points, at most five, one of them: the answer names an error that happened.
  8. Exercises (below).
* The guided project does not change: no run, no tag. The chapter links chapter 12's tag `book-v1/closing-a-milestone` where it quotes the lines.
* Excerpts, byte for byte in English, translated in Portuguese with the note of chapter 10: the two lines `route-errors` and `minutes-of` from `work/done/closing-a-milestone-run/queue.diff`; the kit's §7 only if quoted, from `SETUP.md` at the commit the clinic installed (`e7607c5`).
* Numbers, and only these: 13 and 14 (chapter 8's citations, from `work/done/useful-notes.md`), the date 2026-09-02.
* docs/03 terms: governor, its meaning widened to both directions (done by this /propose). Used: page, delivery, documents, queue, verify, fresh session, guided project, chapter tag, finding, case. No new term.
* Sources (`[^key]`, same keys in both editions):
  * `[^ninjobs]` (new in this chapter): Ninjobs, a private repository: its ADR-0022, amendment of 2026-09-02, and the page of that delivery, paraphrased; the date from the amendment.
  * `[^useful-notes]` (new): `work/done/useful-notes.md` on `main`, where the error that justified the parity check is written.
  * `[^closing-a-milestone-run]` (as chapter 12): `work/done/closing-a-milestone-run/README.md` on `main`, for the two lines.
* Exercises, on the clinic, by conversation with the agent, never by hand:
  * 13.1 Ask the agent which are the first and the second copy behind your milestone 2 lines that make a shared copy; for a repetition in your code with one copy only, say why it waits.
  * 13.2 Ask the agent to propose one check your `npm run verify` lacks, then ask it the governor question; keep the check only if the answer names an error from your project's history (`git log`, `work/done/`).
  * 13.3 For each of the seven items of your clinic's docs/05 §7, say what in your project does its job.
* Documents: docs/03 governor widened (this /propose). docs/06: `the-governor` `[>]`, and the new line `m3-review` at the end of M3 (this /propose); `the-governor` to `[x]` by /apply. docs/00 §Contents already names chapter 13. docs/05 §7 unchanged. The page's What happened records the exercise answers for the `exercise-answers` appendix.

**Out of scope.**

* Running a proposal in the clinic to refuse it: the real ones exist; a staged one would be fabricated.
* The growth of focus-kit itself and the commit that cut it back: a pivot of the kit, left out of chapter 4 for the same reason.
* Chapter 4's numbers (29 checks, four screens): told there, pointed to.
* The other checks of Ninjobs' ADR-0022, its vendor and its infrastructure: not needed by the story, and docs/03 forbids them.
* FOCUS and YAGNI as architecture: Part III; here only the rule of the second occurrence.
* Building the clinic's `route-errors` and `minutes-of`: they wait in its queue.
* The review of this book's M3: its own line, `m3-review`.
* Customizing the process (extra marks, proof files): chapter 21.

**Done when.**

* [x] Both editions written, same file name and heading structure, opening with the Objective in at most three sentences; no draft marker.
* [x] No filler and nothing useful cut; every number cites its source.
* [x] Every English excerpt matches its source byte for byte, checked by script; Portuguese translated with the note.
* [x] The author approved the Ninjobs passage.
* [ ] `make verify` green, the disclosure scan and the link check included. The link to the clinic's tag `book-v1/closing-a-milestone` answers only after the author pushes it (pending from chapter 12); every other source is already on `main`.
* [x] `make book` builds; both PDF paths given to the author.
* [x] docs/06 line `[x]`, page in `work/done/`, staged, commit message suggested.

## What happened

* Both editions written with the Contract's eight sections, in its order; no draft marker. The Portuguese edition uses chapter 4's "teria pegado" and chapter 10's "checagem", "Behaviour" and "Out of scope" for the clinic's page, and translates the two queue lines in their diff fence with the note of chapter 10.
* The Ninjobs passage: approved by the author, who asked to name the database vendor. The Contract and Out of scope said no vendor name, because docs/03 forbade Ninjobs' infrastructure; asked, the author chose to name it. So both editions say "Supabase, the database vendor", and docs/03 (and the line of AGENTS.md that points to it) gains the one exception: the vendor's name where a story needs it, never its servers, projects, schema or configuration. The lint, the homegrown check, the index and the table stay unnamed, and so does the date the index entered, since the page allows only 2026-09-02.
* The `[^closing-a-milestone-run]` note is shorter than chapter 12's: it leaves out the run's dates, versions and range, since the page allows only its three numbers and this chapter quotes only the queue's diff.
* §7 of the kit is paraphrased, not quoted, so it has no excerpt to check; `SETUP.md` is named in plain words, with no note.
* Proof: the two English lines compared by script with `work/done/closing-a-milestone-run/queue.diff`: identical. `make verify`: build, parity, em dash and prose green; links fails only on the tag `book-v1/closing-a-milestone`, in chapters 12 and 13 of both editions, which the author has not pushed yet (pending from chapter 12); `make scan`, the disclosure scan, green on its own. `make book` builds both editions, with the known warning `Ignored user-select: none`.
* Documents: docs/03 governor widened (by /propose) and the Ninjobs exception (this /apply); AGENTS.md points to it; docs/06 line `[x]`. docs/05 §7 unchanged. No ADR.

Exercise answers, for the `exercise-answers` appendix:

* 13.1: in the clinic, `route-errors` names the first copies, `session.server.ts` and `weeklyHours/route.server.ts`, and the review found the others (`professionals/route.server.ts` and the appointments route); `minutes-of` names both, `weeklyHours/rules.ts` first and `appointments/rules.ts` second. A repetition with one copy waits because nothing yet shows what the shared version must serve.
* 13.2: the answer depends on the reader's project; a check whose answer names no error from `git log` or `work/done/` stays out, as the clinic's import check did in chapter 10.
* 13.3: formal spec, the page; spec delta, the documents changed in the same delivery; change folder, `work/<slug>.md` then `work/done/`; numbered tasks, the Behaviour lines; gate, the reader of the page before `/apply`; specialized subagent, one agent that reads the documents; a tool nobody asked for, the governor.

