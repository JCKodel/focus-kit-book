# docs03-finding-slow-test

**Objective.** A person reading docs/03's `finding` term learns that a slow test the milestone review runs and that fails is a finding, as the `milestone review` term and docs/05 §8 already say.

**Behaviour.**

* Reading docs/03's `finding` row, a person finds four kinds of finding: a clause no delivery answers, a clause that fails in the person's hands, a failing slow test the milestone review runs, and a candidate the person confirms.
* The row and the `milestone review` row agree: both say a failing slow test is a finding.
* A project whose Verify slot names no slow tests has no such finding; the row says the test is one the review runs, so it implies no slow suite here.
* The rest of the row (a `[ ]` line in the same milestone, under the review line, never a fix in the middle of the next milestone, no second review) is unchanged.

**Contract.** docs/03, row `finding`, Meaning, exact new text:

"A clause of a milestone's paragraph that no delivery answers, or that fails in the person's hands, a slow test of the Verify slot that the milestone review runs and that fails, or a candidate of the milestone review that the person confirms; it becomes a `[ ]` line in the same milestone, under the review line, never a fix in the middle of the next milestone, and gets no second review."

Term, Portuguese and Identifier columns unchanged. Sources: docs/05 §8 ("It runs §5's slow tests, when the slot names them; a failing one is a finding") and docs/03's `milestone review` row. No data, schema or API change; no new term.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.** Chapter 15: its review section already says a failing slow test is a finding (`ch05-13-slow-tests`); its short definition, "A clause no delivery answers, or one that fails in the person's hands, is a finding.", is a chapter and not this line's file; if wanted, it is a new `[ ]` line. docs/05: already says it.

**Done when.**

* [x] The row reads word for word as the Contract; each Behaviour line reads true against docs/03 and docs/05 §8.
* [x] `make verify` green after the last edit. `make book`: inapplicable, no chapter changes. Both editions: inapplicable, docs/03 is one table and only its Meaning column changes.
* [x] Only docs/03's row, this line's mark of docs/06 and this page are staged.
* [x] Delivery review by a read-only Opus agent per docs/05 §5, its candidates answered on this page; page archived and commit message suggested.

**Built.** docs/03's `finding` row now names four kinds of finding: a clause no delivery answers, a clause that fails in the person's hands, a slow test of the Verify slot that the milestone review runs and that fails, and a candidate the person confirms. It agrees with the `milestone review` row and docs/05 §8.

**Divergences.** None.

**Decisions.** The row takes the Contract's text word for word; no question was left open. Under the batch, the driver sets this line's mark and stages docs/03's row with the mark and this page.

**Proof.** `git diff` of docs/03 shows only the `finding` row's Meaning changed. `make verify` green after the last edit. `make book`: inapplicable, no chapter changes.

**Delivery review.** A read-only agent on Opus read this delivery's hunk of docs/03 against this page, docs/05 §8 and docs/04. The text matches the Contract word for word, the other columns and the rest of the row are unchanged, and every Behaviour line reads true. Points: (1) the list reads a little hard, with the first "or" before the slow test: it is the Contract's wording, kept as defined. (2) The row does not repeat "when the slot names any": "that the milestone review runs" already implies it, and the `milestone review` row says it. (3) Other sessions' files are changed in the tree: under this batch, the driver stages by path.

```commit
docs(docs03-finding-slow-test): count a failing slow test as a finding

- docs/03's finding row names a slow test the milestone review runs
- it agrees with the milestone review row and docs/05 §8

work/done/docs03-finding-slow-test.md
```
