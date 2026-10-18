# ch05-13-slow-tests

**Objective.** The reader can keep delivery verification fast while retaining named slow tests that the milestone review runs.

**Behaviour.**

* Given a slow end-to-end check that proves something fast tests cannot, the reader keeps it, records its command and purpose in docs/05’s Verify slot, and knows the milestone review runs it.
* Given no separate slow suite, the slot says “none”; no extra runner or invented timing threshold is required.
* During apply, a test too slow for verify is named among that slot’s slow tests and the agent tells the person; moving it does not silently delete coverage or waive the delivery’s own proof.
* The milestone review runs the named slow suite; a failure becomes a finding under that review, and the milestone cannot close while that finding remains unfinished.
* Ordinary deliveries still finish with verify green; slow-suite placement changes neither the pure-use-case rule nor which level proves a scenario.

**Contract.** Edit both editions of `05-testing-each-piece.md` (test-speed explanation), `07-the-documents.md` (Verify slot description), `13-apply.md` (tests, verification and finish), and `15-closing-a-milestone.md` (review duties and findings).
Source: SETUP.md apply instructions, docs/05 template §§5 and 8, and the completed migration's docs/04 Tests and docs/05 Verify slot.
Use docs/03's verify, slot, proof, milestone review and finding terms.
Chapter 5 explains the rule briefly where it names a milestone, without adding an early forward link.
The book repository's existing checks remain in make verify and its new slot says no separate slow suite; describe software-project behavior without claiming this repository already has one.
No code, test, command, dependency or schema is added by this chapter delivery.

**States.** Inapplicable: prose, no new screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** Changing this repository’s test pipeline belongs to a separate delivery; no benchmarks, new timings, additional test taxonomy or redesign of the chapter examples.

**Definition decision.** The author authorized defining this page before its dependency completes, using `work/kit-2026-10-18-1.md` as the contract.
The queue retains `after kit-2026-10-18-1` as an implementation gate; apply first checks the completed migration against this contract and reports any contradiction.
Source is the local working copy of focus-kit SETUP.md 2026.10.18.1, not its older HEAD; the installation page owns its fingerprint.
No implementation or staging occurs during this proposal.

**Done when.**

* [ ] Both editions pass every Behaviour check against the completed kit migration and use docs/03's terms.
* [ ] Every affected chapter keeps its opening value and evidenced team gain; no filler, no useful content cut, and every number and artifact has a checked source.
* [ ] `make verify` is green after the last covered edit, `make book` builds both editions, and the author receives both PDF paths for review.
* [ ] The independent delivery review, proof and decisions are recorded under docs/05; no private passage is added, so OD-3 approval is inapplicable.
