# apply-use-first

**Objective.** The reader can use the delivered result as its user before reviewing the staged change and deciding its commit.

**Behaviour.**

* After apply finishes lend-book, the person first uses the lending behavior and refusal cases the page promises, then reviews the staged change against that page, then decides the commit.
* A visible defect within the page is reported in that apply conversation and corrected with renewed verification and proof; a new capability becomes a queue line instead of enlarging the delivery.
* For this book or another document delivery, using the result means opening and reading its rendered deliverable; it does not require inventing a software screen.
* Passing verify does not substitute for using the result, and using it does not substitute for reviewing the index; automatic publication and commit are not implied.
* In a parallel batch, each delivery receives that use and review before its own commit, rather than treating the batch as one approval.

**Contract.** Edit both editions of `10-quick-guide.md` (step 7, handoff and key point), `13-apply.md` (finish and human review), and the passages describing personal review in `18-git-essentials.md`, `19-worktrees.md`, `22-cost-and-where.md` and `23-adoption.md`.
Source: SETUP.md apply next steps and docs/05 template §2, together with chapter 13’s existing use-before-commit explanation in “Review the staged change” and docs/05 Proof.
Keep that existing explanation as the main teaching passage, align abbreviated sequences elsewhere, and preserve chapter 22’s measurements untouched.
Examples use the lending library's existing scenarios, not a new historical claim about either private case.
No new terms, data contract or manual procedure beyond the chapter's existing steps.

**States.** Inapplicable: prose, no new screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** Cost accounting belongs to `ch22-cost-method`; commit authority belongs to `agent-commits-asked`; staging and shared-index mechanics belong to their queue lines. No changes to private-case passages.

**Definition decision.** The author authorized defining this page before its dependency completes, using `work/kit-2026-10-18-1.md` as the contract.
The queue retains `after kit-2026-10-18-1` as an implementation gate; apply first checks the completed migration against this contract and reports any contradiction.
Source is the local working copy of focus-kit SETUP.md 2026.10.18.1, not its older HEAD; the installation page owns its fingerprint.
No implementation or staging occurs during this proposal.

**Done when.**

* [ ] Both editions pass every Behaviour check against the completed kit migration and use docs/03's terms.
* [ ] Every affected chapter keeps its opening value and evidenced team gain; no filler, no useful content cut, and every number and artifact has a checked source.
* [ ] `make verify` is green after the last covered edit, `make book` builds both editions, and the author receives both PDF paths for review.
* [ ] The independent delivery review, proof and decisions are recorded under docs/05; no private passage is added, so OD-3 approval is inapplicable.
