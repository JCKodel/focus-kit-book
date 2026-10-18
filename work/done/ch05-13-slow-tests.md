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

* [x] Both editions pass every Behaviour check against the completed kit migration and use docs/03's terms.
* [x] Every affected chapter keeps its opening value and evidenced team gain; no filler, no useful content cut, and every number and artifact has a checked source.
* [x] `make verify` is green after the last covered edit, `make book` builds both editions, and the author receives both PDF paths for review.
* [x] The independent delivery review, proof and decisions are recorded under docs/05; no private passage is added, so OD-3 approval is inapplicable.

**Contract check.** The completed migration agrees with this page: docs/05 §5 Verify names `make verify` and `Slow tests: none`, §8 runs the slot's slow tests when it names any and a failing one is a finding, docs/04 Tests says there is no slow suite. No contradiction; no shared file changed.

**What was built.** Chapter 5: a slow test that proves what fast ones cannot may stay out of verify and is kept, with its command and purpose written next to the verify command, or none; the review that closes a milestone runs them and a failure keeps the milestone open until its fix is done. Chapter 7: the Verify slot holds the command of any slow tests kept out of verify for the milestone review. Chapter 13: /apply writes docs/04's tests, puts one too slow for verify with the slow tests and says so, deletes no test, waives no proof, changes neither the pure use case nor the level of test; then runs verify; the person's checklist asks about it. Chapter 15: the opening, the review section and two key points say the review runs the slow tests and a failing one is a finding. Both editions.

**Divergences and omissions.** None. Chapter 5 describes the place in plain words, without naming docs/05 or the slot, since the documents arrive in chapter 7 and the page forbids an early link.

**Proof.** Prose: each Behaviour bullet reread against both editions; chapter 5's table and the pure-use-case sentence unchanged; `make verify` green after the last edit. `make book` and the PDF paths are the batch driver's, run once at the end.

**Delivery review.** One read-only Opus agent over `git diff HEAD` of the eight chapter paths, against this page, docs/03, docs/04 and docs/05. Candidates and answers: chapter 5 "until it passes" disagreed with chapter 15's close condition, fixed to "until its fix is done"; "stays out of it" made exclusion mandatory, fixed to "may stay out"; chapter 7's slot clause was hard to count and lacked the command, reworded; chapter 13 ran verify before writing the tests, reordered; it did not say the slot names the command, fixed there and in the checklist; chapter 15 said "a finding like the others" before findings are defined, dropped; pt "a própria prova" restored for parity; whether the moved test runs once in the delivery, left, since the kit says nothing of it. docs/03's finding definition omits a failing slow test, outside this page: a new queue line.

**Decisions.** Recommended answers taken under the batch: plain words in chapter 5; no mention of this repository's own slot; no change to What the team gains, whose evidence is unchanged.
