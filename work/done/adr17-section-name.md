# adr17-section-name

**Objective.** Whoever reads ADR-0017's amendment of 2026-10-17 is sent to the docs/04 section `one-gain-section` actually changed, §Writing the book, and finds the rule there. Found by `m16-review` (work/done/m16-review.md, doc-3 seen: "ADR-0017:46 names docs/04 §Chapter shape where `one-gain-section` changed §Writing the book").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The section is §Writing the book, its bullets **A gain per chapter** and **One gain**: `one-gain-section`'s commit changed those two bullets and no line of §Chapter shape, and its own page records that "§Chapter shape's block never held it". The amendment's rule is in **A gain per chapter** (the gain alone, with no sentence on the missing number) and in **One gain** (the baseline said once, in the prologue), so the reference names both. Source: work/done/one-gain-section.md, Divergences; `git show` of that delivery's commit on docs/04; docs/04:35-36 and :49.
2. Fixed in place, not by a new amendment. The fault is a wrong reference inside a two-day-old amendment; its decision does not change, and a third amendment that only corrects a section name would make the ADR longer to read for no new rule. ADR-0017's own precedent (`adr17-gain-amendment` decision 1) is about not rewriting the Decision, which this fix does not touch. Source: docs/adr/ADR-0017-the-rewrite.md; work/done/adr17-gain-amendment.md decision 1.
3. No docs/03 term, no new queue line, no split. Source: docs/03; docs/05 §1.

**Behaviour.**

* After the delivery, the last sentence of ADR-0017's amendment `adr17-gain-amendment` says `one-gain-section` applied the rule to docs/04 §Writing the book, its **A gain per chapter** and **One gain**, and a reader who opens that section finds both bullets.
* `grep -n "Chapter shape" docs/adr/ADR-0017-the-rewrite.md` finds nothing.
* Edge: the amendment's first sentence, its heading, the Decision and every other line of the ADR stay byte for byte; the diff changes one line.
* Edge: work/done/adr17-gain-amendment.md, which quotes the old words, stays as it is: it is the history of that delivery.
* Fails: a new amendment heading; any change to the Decision.

**Contract.** ADR-0017, line 46, in the amendment `## Amendment, 2026-10-17 (adr17-gain-amendment)`: "applied it to every chapter and to docs/04 §Chapter shape;" becomes "applied it to every chapter and to docs/04 §Writing the book, its **A gain per chapter** and **One gain**;". The rest of the line stays.

No new term; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* work/done/adr17-gain-amendment.md and work/done/one-gain-section.md: done pages are history.
* docs/04: it already holds the rule where this fix points.
* Both editions: no reader-facing text changes, so ADR-0004's both-editions rule does not apply.

**Order with the other slugs of this batch.** Fifth; it touches only ADR-0017, which no other slug of the batch touches, so it runs in any order.

**Done when.**

* [x] ADR-0017:46 reads as the Contract says, and `git diff` of the ADR shows that one line changed.
* [x] `grep -n "Chapter shape" docs/adr/ADR-0017-the-rewrite.md` prints nothing.
* [x] `make verify` green; no em dash.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its own hunk of docs/06 (docs/05 §6), other sessions' changes left unstaged; commit message in a `commit` block.

**Proof.** `git diff --numstat docs/adr/ADR-0017-the-rewrite.md`: 1 insertion, 1 deletion, line 46, which now reads as the Contract says. `grep -n "Chapter shape" docs/adr/ADR-0017-the-rewrite.md` prints nothing. docs/04 §Writing the book (:12) holds **One gain** (:35-36) and **A gain per chapter** (:49), the amendment's two rules. `make verify` green: build, parity, em dash, prose, width, links, disclosure.

**Divergences.** None.

**Omissions.** None.

**Decisions taken in /apply.** None beyond the page's.

**Review.** Delivery review by a read-only Opus agent on the diff of ADR-0017, this delivery's line of docs/06 and this page, against the page and docs/04. No findings: the line matches the Contract and is the only one changed, the grep is empty, both bullets are under §Writing the book with the amendment's rule, and `one-gain-section`'s commit touched no line of §Chapter shape.

```commit
docs(adr17-section-name): point ADR-0017's amendment to docs/04's section

- ADR-0017: the 2026-10-17 amendment names docs/04 §Writing the book and its two bullets

work/done/adr17-section-name.md
```
