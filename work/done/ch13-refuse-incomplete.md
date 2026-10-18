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

* [x] Both editions let a reader answer every Behaviour scenario and never equate an existing page with a complete definition.
* [x] The chapter keeps its opening value and evidenced team gain; no filler or useful content is cut, and all numbers and artifacts keep their provenance.
* [x] No Case A or Case B passage is changed or introduced, so OD-3 approval is inapplicable.
* [x] `make verify` and `make book` pass, and both PDFs are given to the author to review.

**Divergences and omissions.** None against the Contract. The old `[?]` clause, "goes on only when you say it is resolved", was the directly contradicting statement nearby: it read as if a resolved line always builds, so it now returns by its resume phase, and a `resume: propose` line goes to `/propose` first. The Key points line on `[*]` lies outside the Contract's sections and is left as it is. The opening, the problem, the evidence and the team gain are untouched.

**Case A and Case B.** No passage changed or introduced; OD-3 approval is inapplicable.

**Delivery review.** A read-only agent on Opus read `git diff HEAD` of both chapter files against this page, docs/04, docs/05 §§2 to 4 and the installed skill. All four scenarios answerable in both editions; five points, answered: the "(chapter 12)" pointer cited a rule chapter 12 does not state, now docs/05 §3, and chapter 12's "`[>]` when the page is written" became a new `[ ]` line, outside this Contract; "goes on only once the reason is resolved" restored before the resume phase; "with its draft" became "with any draft kept", as docs/05 §4 says; the unfinished `after` sentence now says an `after` is an order, not a wait; "So on a page" lost its connective and the Portuguese says "pergunta de escopo". The optional Key points qualifier was declined, being outside the Contract.

**Proof.** `make verify` green after the last edit. `make book` is run once by the batch driver at the end, which records `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for review.

**Decisions taken alone.** The lending-library example names "a Contract question still unanswered" in general rather than inventing a specific question for `lend-book`.

```commit
docs(ch13-refuse-incomplete): refuse an incomplete page in chapter 13

- /apply refuses a page that is not [>] and points to /propose
- [*] only on a complete [>] line whose after lines are [x]
- a refusal is not a [?] stop; an unfinished after is an order
- a resolved [?] returns by its resume phase; both editions

work/done/ch13-refuse-incomplete.md
```
