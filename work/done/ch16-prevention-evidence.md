# ch16-prevention-evidence

**Objective.** A reader can justify proportionate prevention with a documented error from another project without waiting for the same error to recur locally.

**Behaviour.**
* A proposed check names a documented failure in another project, shows the same conditions are possible here and explains what the check catches; the governor can admit it before this project suffers that failure.
* A speculative risk with no documented occurrence still fails the governor, and a real incident irrelevant to this project's conditions does not justify a permanent check.
* A relevant error does not justify any cost: the reader compares the check's repeated execution and maintenance with the concrete harm it prevents and selects a proportionate check.
* The existing Case A mark and public book-review examples remain evidence of local errors; their origin is an example, not a rule that every adopting team must repeat the error.

**Contract.** `book/en/16-the-governor.md` and `book/pt/16-the-governor.md`: opening, The question, The error that earned a mark, gain and final key point where necessary.
Keep docs/03's governor and docs/05 §7's requirement for an error that happened: neither requires that it happened in this repository.
Use this book's already public `work/done/m14-review.md` (the existing `m14-review` source note) as the documented outside-project evidence a reader's team can inspect; explain relevance and ongoing cost without inventing an incident or effectiveness measurement.
The existing Ninjobs numbers and private Case A facts stay unchanged; only the conclusion drawn from the Case A passage changes.
Decision from docs/06: evidence can travel across projects; its applicability and cost must be argued for this one.

**States.** Inapplicable: chapter prose, no new screen.

**Visual reference.** Inapplicable: the existing book layout.

**Out of scope.** Adding a mandatory check or changing kit policy: this delivery clarifies the current governor, not a new process gate; new incidents or private details: existing evidence suffices.

**Done when.**
* [x] Both editions distinguish relevant documented external evidence, speculative risk and disproportionate prevention; no sentence requires the local team to suffer the same error first.
* [x] List the revised Case A paragraph and obtain the author's approval of its anonymized wording before completion (docs/00 OD-3); `make scan` passes.

* [x] Both editions say the same thing, using docs/03's terms and Portuguese example names.
* [x] The opening states the reader's value and the gain is supported; no filler added or useful explanation cut; every number and quoted artifact has its source (docs/00 and docs/04).
* [x] `make verify` and `make book` pass; the author receives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the passage checks (docs/05 §5).

## Delivery

**Built.** Both editions of chapter 16: the opening accepts an error from another project whose record opens and whose conditions the reader's shares, at a cost the error justifies; The question says when another project's error counts, that an unrecorded risk and an irrelevant real error still fail, and that a relevant error buys the smallest check that catches it; The error that earned a mark keeps Case A's facts, says the mark's origin is an example, not a toll, and works the readers' first error (the public `work/done/m14-review.md`, B1) as outside evidence: relevant where checks list files without `-z` and names can be non-ASCII, irrelevant otherwise, and still out at a cost paid by hand; the gain and the last key point follow. Line 78 (the six rules) is left to ch16-six-rules-timeline.

**Revised Case A paragraph, for the author's approval (docs/00 OD-3).** EN: "The question is asked in each project, and the governor decides there; the error it accepts may come from that project or from another one's record. [Case A facts unchanged.] That error happened on Case A, and that is where the mark came from, not a toll every team pays: a team whose lines also wait on someone outside it has the error documented in chapter 14 and can add `[?]` before its own board misleads it." PT carries the same sentences. Under this batch the approval is asked in the lane report; `make scan` passes inside `make verify`.

**Proof.** `make verify` green after the last edit; both editions read side by side; the B1 mechanism checked against `work/done/m14-review.md` and `scripts/repo_files.py`. `make book` is the batch driver's.

**Divergences and omissions.** No second `[^m14-review]` reference: the passage points to the record the readers' entry cites, so the note prints once. No shared document changes: docs/03 and docs/05 §7 already allow an error from elsewhere.

**Review.** One read-only Opus agent, no must-fix, five optional points, all taken: "matched no file" became "was skipped", which is what B1 says; "keep one test" became "prove once", as this book's own fix kept its proof on the page; "will" became "may" for Portuguese file names; Case A's error is "documented in chapter 14", not "here"; two Portuguese wordings ("podem ter", "ficaria de fora").

**Decisions taken alone.** The outside example is the readers' first error, worked as reasoning for the reader's team, not as a report of this repository; no cost number, only the comparison of a one-time check with one paid by hand in every delivery.
