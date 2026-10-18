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
* [ ] Both editions distinguish relevant documented external evidence, speculative risk and disproportionate prevention; no sentence requires the local team to suffer the same error first.
* [ ] List the revised Case A paragraph and obtain the author's approval of its anonymized wording before completion (docs/00 OD-3); `make scan` passes.

* [ ] Both editions say the same thing, using docs/03's terms and Portuguese example names.
* [ ] The opening states the reader's value and the gain is supported; no filler added or useful explanation cut; every number and quoted artifact has its source (docs/00 and docs/04).
* [ ] `make verify` and `make book` pass; the author receives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the passage checks (docs/05 §5).
