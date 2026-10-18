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

* [x] Both editions pass every Behaviour check against the completed kit migration and use docs/03's terms.
* [x] Every affected chapter keeps its opening value and evidenced team gain; no filler, no useful content cut, and every number and artifact has a checked source.
* [x] `make verify` is green after the last covered edit, `make book` builds both editions, and the author receives both PDF paths for review.
* [x] The independent delivery review, proof and decisions are recorded under docs/05; no private passage is added, so OD-3 approval is inapplicable.

**Contract check.** The local focus-kit SETUP.md matches the SHA-256 recorded by `kit-2026-10-18-1` (`6c8d8f40...6f17`); its docs/05 template §4 sentence on the next milestone and §8's finding rule equal this repository's docs/05 §4 and §8 word for word. No contradiction with the completed migration.

**Built.** Chapter 11, both editions: the opening adds placing a line in the milestone whose paragraph needs it or under the next; "Size and order" replaces "a later milestone, one of improvements" with the kit's rule, whoever adds the line, with `fix-overdue-return` (pt `corrigir-devolucao-atrasada`), written for the chapter, staying in milestone 1 because the paragraph promises to record the return, a review finding staying in its milestone, and a line entering the current milestone only through a clause the person widens first; the review section says findings stay even when the next milestone already holds lines; "Changing the queue" places the line by the paragraph; `due-date-format` (pt `formato-devolucao`) no longer goes above `m1-review`: with no next milestone the agent creates "Milestone 2: loan dates read at a glance", paragraph and `m2-review` last, written for the chapter, and milestone 1 keeps its lines, order and `after`; a move keeps its `after` and never changes what a milestone promises without a word; the third key point carries the rule. The page, the commit and the `[x]` line of the example are unchanged. Chapter 14, both editions: a paragraph in "The next line" says a milestone's end sets priority, not freedom: `due-date-format` is free and does not wait for `m1-review`, the next delivery reaches it only once milestone 1 holds no free line, and a new line is never placed higher because it is new. Chapter 15, both editions: the opening, "A line, and not a fix" and the fourth key point say a finding stays under `m1-review` even when milestone 2 already exists, with its own `/propose` and `/apply` and no review of its own.

**Proof.** `make verify` green after the last edit. `make book` and the two PDF review paths are the batch driver's, which builds once at the end.

**Delivery review.** A read-only Opus agent read `git diff HEAD` of the six chapter files, the page, docs/04, docs/03, docs/05 §§4 and 8 and AGENTS.md, and confirmed every Behaviour case in both editions. Points and answers:
* Chapter 14's "no clause of milestone 1's paragraph needs it" sat under its own milestone 1, which holds lines chapter 11's paragraph does not name: the reason removed there, chapter 11 gives it.
* Chapter 15 named chapter 11's milestone 2 under its own, different milestone 1, whose due-date clause could need the format: now "a milestone 2 already below it, holding its own lines and `m2-review`".
* "A milestone's end is an order too" mixed with `· after`: now "sets priority, not whether a line is free".
* "Takes the place its milestone's paragraph gives it": now "goes in the milestone whose paragraph needs it, never higher in the queue".
* "And say so" was unclear: now "and the line then answers the new clause".
* An awkward key point phrase and "no second milestone review" against `m2-review` reading the fix: reworded ("no review of its own").

**Decisions taken alone.** The fix example `fix-overdue-return` (an overdue loan whose copy cannot be taken back); milestone 2's title and paragraph; `due-date-format` carries no `· after lend-book`, since the example's `[x]` line would no longer fit the block width and its place below milestone 1 already puts it after every milestone 1 line in priority; chapter 14's own example milestone left as it is (out of this page's contract).

```commit
docs(ch11-next-milestone): place new lines by the milestone's paragraph

- ch11: a line no clause needs goes under the next milestone
- ch11: due-date-format opens milestone 2 with its review last
- ch14: a milestone's end sets priority, not whether a line is free
- ch15: a finding stays under its review when milestone 2 exists
work/done/ch11-next-milestone.md
```
