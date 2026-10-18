# ch13-refuse-incomplete

**Objective.** The reader can tell whether a page is ready for `/apply` and return an incomplete definition to `/propose` before building begins.

**Behaviour.**

* Given `work/lend-book.md` with an unanswered Contract question, the reader sees `/apply` refuse to build and point to `/propose lend-book`, even though the file exists.
* Given a fully defined page whose line is `[>]` and whose `after` lines are `[x]`, the reader sees the first build edit change that line to `[*]`.
* Given the same page with an unfinished `after`, or a draft whose line is `[ ]` or `[~]`, the reader does not infer permission to start from the file's existence or change the mark straight to `[*]`.
* Given a `[?]` line, the reader first resolves the recorded reason and returns through its recorded resume phase; a `resume: propose` draft is not ready to build merely because the reason was removed.

**Contract.** Edit `book/en/13-apply.md` and `book/pt/13-apply.md`, "What `/apply` does" and "It reads before it builds", before the first-edit sentence, plus any directly contradicting statement nearby.
Sources: installed `.agents/skills/apply/SKILL.md`, its refusal and first-edit paragraph; docs/05 §§2 to 4; docs/03's page, draft page and mark.
State refusal and the pointer explicitly, then qualify the existing first-edit sentence with complete `[>]` and satisfied `after`; preserve the distinction between refusing an incomplete proposal and recording an interruption after building began.
Follow the existing resumption explanation and chapter 14 pointer, without creating a new transition or another approval step.
Use the lending-library slug of each edition when illustrating a command; this is an example written for the chapter, not a captured command output.
These choices implement docs/05 §3's completeness rule, not a new gate.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** Delivery review bases, verify scheduling and later `/apply` steps belong to their M19 lines; no skill or process-file changes, and no new state machine.

**Done when.**

* [ ] Both editions let a reader answer every Behaviour scenario and never equate an existing page with a complete definition.
* [ ] The chapter keeps its opening value and evidenced team gain; no filler or useful content is cut, and all numbers and artifacts keep their provenance.
* [ ] No Case A or Case B passage is changed or introduced, so OD-3 approval is inapplicable.
* [ ] `make verify` and `make book` pass, and both PDFs are given to the author to review.
