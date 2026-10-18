# ch07-ninjobs-focus

**Objective.** A reader can distinguish the Ninjobs architecture decision before simplification from the two principles retained afterwards, without mistaking either phase for the whole history.

**Behaviour.**

* Reading chapter 7, the reader understands that after simplification Ninjobs retained vertical slices and exceptions as values, without requiring the four pieces for every feature.
* Reading chapter 4 and chapter 6 with chapter 7, the reader places the earlier requirement for all four pieces in the earlier phase; the later simplification does not erase that recorded experience.
* Reading ADR-0016, the reader finds a dated amendment qualifying its historical context without rewriting the original decision or redefining FOCUS.
* Neither the book nor the delivery claims a full compliance audit of the earlier implementation: the preserved process decision describes the earlier choice, while the available source supports the later arrangement.
* The book removes chapter 7's unnecessary infrastructure characterization and paraphrases only the allowed process decision; no private code, structure, path or configuration is published.

**Contract.** `book/en/07-the-documents.md` and its Portuguese counterpart, The two choices; narrowly qualify the relevant historical sentences in `book/en/04-focus.md`, `book/en/06-birth-of-focus-kit.md` and their Portuguese counterparts only where needed to distinguish the two phases.
Append an amendment to `docs/adr/ADR-0016-the-books-definition-of-focus.md` identifying the original account as the earlier requirement and the later decision as simplification retaining the two principles.
The architecture definition itself remains unchanged.
Evidence: the author's authorized read-only inspection on 2026-10-18 of Ninjobs' preserved process decisions and current source, cross-checked against ADR-0016 and the book's existing historical account.
The available local history does not hold the earlier implementation, so it proves the recorded earlier choice, not perfect implementation compliance.
Per docs/03 and docs/04, publish only the paraphrased process conclusion, with no private source note or source-code example.

**States.** Inapplicable: chapter prose.

**Visual reference.** Inapplicable: existing layout.

**Out of scope.** Changing FOCUS's definition, evaluating commercial code quality, publishing an architecture inventory, editing the sibling kit repository or revising unrelated historical numbers.

**Decisions.** The author's request was to establish what happened from evidence rather than prefer whole FOCUS.
The evidence supports a temporal correction rather than changing chapter 7 to an unqualified whole-FOCUS claim.
The kit's bare Ninjobs example under whole FOCUS needs the same qualification; report the concrete correction to the author for the kit repository, without making an external edit here.
The author authorized definition before prerequisites finish; `after kit-2026-10-18-1` still gates implementation.

**Done when.**

* [ ] Both editions and the ADR agree on the two phases; only the bounded historical sentences change, with no unsupported conformity claim.
* [ ] The author reviews the paraphrased historical wording; no private detail, source path or new measurement appears, and `make scan` passes.
* [ ] Each chapter keeps its reader-value opening and evidenced gain, with no filler or useful explanation cut; retained numbers preserve their provenance.
* [ ] `make verify` and `make book` pass; both PDFs are given to the author, and the pending kit wording correction is explicitly reported.
