# ch11-next-milestone

**Objective.** The reader can place a new queue line by the current milestone’s paragraph and keep its review findings in that milestone.

**Behaviour.**

* For the existing first lending milestone, a required return-book fix stays in that milestone because it is needed to satisfy recording returns.
* A due-date-format request that no clause requires goes under the next milestone, keeping its slug and draft; it is not inserted before m1-review merely because it arrived now.
* With no next milestone, the agent creates one with a paragraph that the new line answers and a review planned last; existing dependencies and priority remain visible.
* A finding confirmed by m1-review stays under that review in milestone 1 even when milestone 2 already exists; it gets its own propose/apply and no second milestone review.
* The same placement rule applies whoever adds the line; moving it does not silently redefine the current milestone or discard a dependency.

**Contract.** Edit both editions of `11-queue-and-milestones.md` (milestone membership, changing the queue, due-date-format introduction and key point), `14-queue-states.md` (adding lines and priority), and `15-closing-a-milestone.md` (findings and closing).
Source: SETUP.md docs/05 template §§4 and 8 and the completed migration's matching rules.
Keep chapter 11’s due-date-format page and its behavior intact, but place its line in a minimal next-milestone example whose paragraph promises readable loan dates and whose review is last.
Label examples written for the chapter, with Portuguese slugs in that edition; preserve return-book and existing first-milestone clauses.
No new domain term or data/API contract.

**States.** Inapplicable: prose, no new screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** Changing the real queue’s milestone membership, altering marks or resetting a wait; those are separate process or chapter-state deliveries. Session wording in the same chapter belongs to `propose-same-session`.

**Definition decision.** The author authorized defining this page before its dependency completes, using `work/kit-2026-10-18-1.md` as the contract.
The queue retains `after kit-2026-10-18-1` as an implementation gate; apply first checks the completed migration against this contract and reports any contradiction.
Source is the local working copy of focus-kit SETUP.md 2026.10.18.1, not its older HEAD; the installation page owns its fingerprint.
No implementation or staging occurs during this proposal.

**Done when.**

* [ ] Both editions pass every Behaviour check against the completed kit migration and use docs/03's terms.
* [ ] Every affected chapter keeps its opening value and evidenced team gain; no filler, no useful content cut, and every number and artifact has a checked source.
* [ ] `make verify` is green after the last covered edit, `make book` builds both editions, and the author receives both PDF paths for review.
* [ ] The independent delivery review, proof and decisions are recorded under docs/05; no private passage is added, so OD-3 approval is inapplicable.
