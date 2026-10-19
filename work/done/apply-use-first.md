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

* [x] Both editions pass every Behaviour check against the completed kit migration and use docs/03's terms.
* [x] Every affected chapter keeps its opening value and evidenced team gain; no filler, no useful content cut, and every number and artifact has a checked source.
* [x] `make verify` is green after the last covered edit, `make book` builds both editions, and the author receives both PDF paths for review.
* [x] The independent delivery review, proof and decisions are recorded under docs/05; no private passage is added, so OD-3 approval is inapplicable.

**Build.** Chapter 13, both editions: "Review the staged change" now opens with the use paragraph, moved from after the checklist and kept as the main teaching passage, saying to begin with the delivery, not the diff, adding that a document is used by opening what it renders and reading it, that using it does not replace reading the diff and that neither step publishes or commits, and that a correction runs verify and the proof again; the Ninjobs sentence moved with it; the checklist follows as "Then read the staged change against the page". `/apply`'s last words, the `lend-book` next steps (a new first step: in the development environment, lend a copy, see the 21-day due date, try the three refusals of chapter 12's page), the delivery review's "comes after", the commit section's lead, the request to commit and the key point now put use first. Chapter 10, both editions: step 6's handoff names the next steps starting with use; step 7 is use, with `lend-book` and the document case, then the staged diff; the key point adds "use what it built". Chapters 18, 19, 22 and 23, both editions: each abbreviated review sequence names the use before the diff and the commit; chapter 19's batch passage already said "used and reviewed" and stays; chapter 22's sentence on where the person's time goes gains the use, its measurements untouched.

**Gate.** `kit-2026-10-18-1` is `[x]`; focus-kit SETUP.md 2026.10.18.1, the installed `.claude/skills/apply/SKILL.md` and docs/05 §2 ("a person uses it, reviews and commits") already say use first. No contradiction, no shared file changes.

**Proof.** `make verify` green after the last chapter edit. `make book` and the PDF paths are the batch driver's, run once at the end: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Review.** One read-only Opus agent over the twelve chapter files and this page. Applied: chapter 23's key point "after using the delivery and reviewing it", since a commit is not used; the Portuguese chapter 18 pronoun matched to the agent; the document case added to chapter 13's main passage too; "Once you have used the delivery, read the staged diff, then commit"; "neither ... nor"; the first next step reordered to name the environment first, with chapter 12's "a member with an overdue book". Became a queue line: chapters 15 and 20 still say review then commit without the use, outside this Contract. Not this delivery's: the uncommitted chapter 21 edit belongs to another session. `make verify` green again after the fixes.

**Decisions taken alone.** The use paragraph moved to open the section rather than reworded in place, so the section's order is the order the person follows; the document case stated in chapters 10 and 13, with no new example; no new term.

```commit
docs(apply-use-first): use the delivery before reviewing its diff

- Chapter 13 opens the person's review with using the delivery
- /apply's next steps start with use, lend-book's refusals tried
- Chapter 10 step 7 uses the delivery, a document by reading it
- Chapters 18, 19, 22 and 23 name the use before diff and commit

work/done/apply-use-first.md
```
