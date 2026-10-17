# docs03-finding-and-gain

**Objective.** Whoever reads docs/03 finds the `finding` and `team gain` rows saying what docs/05 §8 and docs/04 say: a finding includes a code review candidate the person confirms, and a gain with no number gets no sentence about the missing number.

**Decided without the author.**

1. Whose word confirms a code review finding: the person's, "a candidate the person confirms", as docs/05 §8 says ("A candidate the person confirms is a finding like the others") and as docs/03's own `milestone review` row already says. The queue line's "a finding the code review confirms" is chapter 15's wording, and in docs/05 the checker only marks candidates (seen, latent or weak) and the person decides. docs/05 is the process document that owns the rule, so it wins.
2. The `team gain` row copies docs/04's wording (§Chapter shape, **A gain per chapter**: "with its number or a sourced claim where the book has one, and otherwise the gain alone, with no sentence on the missing number"), so the two documents cannot drift apart again. Source: `m15-review` finding doc-1, which names docs/04:48 as the rule.
3. Scope is the two rows. ADR-0017's Decision (doc-2) is its own line, `adr17-gain-amendment`, already in docs/06, and is not touched here.
4. No chapter changes, so no edition changes. Chapter 15 says "A finding the code review confirms is a finding like the others ... one it does not confirm is not a finding" (en lines 57 and 110, and the same passages in pt). That can be read as saying the review confirms its own candidates, where docs/05 has the person confirm them. This page only notes it, and it stays outside this delivery: `m15-review` did not raise it, so it gets no queue line here (docs/05 §8, a finding comes from the review). The reply to the author names it as an observation.
5. No new docs/03 term and no new queue line: both rows exist, and the delivery rewrites them.

**Behaviour.**

* After the delivery, reading docs/03's `finding` row, the reader learns that a milestone review's code reading also produces findings: a candidate the person confirms becomes a `[ ]` line under the review line, like a clause that failed.
* After the delivery, reading docs/03's `team gain` row, the reader finds no permission for "one sentence saying it has none". A chapter whose gain has no number states the gain and nothing about the missing number, as docs/04 says.
* `grep -n "saying it has none" docs/03-Domain.md` finds nothing.
* Edge: a candidate the checker marked seen but the person did not confirm is not a finding. The row says "the person confirms", not "the checker marks".
* Edge: the other rows of docs/03 (`milestone review`, `chapter shape`, `key points`, `source note`) stay byte for byte, and so do docs/04, docs/05, ADR-0017 and both editions.
* Fails: a row that loses its other clauses ("becomes a `[ ]` line in the same milestone, under the review line, never a fix in the middle of the next milestone, and gets no second review"; "the section before the key points") is not this delivery. Only the clauses the Contract names change.

**Contract.** docs/03, two rows replaced, every other column kept:

```
| finding | achado | none | A clause of a milestone's paragraph that no delivery answers, or that fails in the person's hands, or a candidate of the milestone review that the person confirms; it becomes a `[ ]` line in the same milestone, under the review line, never a fix in the middle of the next milestone, and gets no second review. |
```

```
| team gain | ganho do time | `## What the team gains` / `## O que o time ganha` | The section before the key points that says what a team or a project gains from the chapter, with a number or a sourced claim where the book has one, and otherwise the gain alone, with no sentence on the missing number. |
```

No new term; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* ADR-0017:18's "one sentence saying the gain has no number": its own line, `adr17-gain-amendment` (doc-2).
* Chapter 15's "a finding the code review confirms": the chapter's wording, noted in decision 4, with no line from this page.
* docs/05 §8 and docs/04: they already say what the rows now copy.
* Any chapter: no reader-facing text changes, so the both-editions rule does not apply.

**Done when.**

* [x] docs/03's `finding` and `team gain` rows equal the Contract's two lines, byte for byte, and this delivery stages no other line of docs/03 (`git diff --cached docs/03-Domain.md` shows two removed and two added lines).
* [x] `grep -n "saying it has none" docs/03-Domain.md` finds nothing.
* [x] `make verify` green; no em dash on this page or in the rows.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06 (docs/05 §6), the other session's changes left unstaged; commit message in a `commit` block.

**Proof.** `make verify` green. The two rows in docs/03 match the Contract's lines byte for byte (checked against the page's code blocks); `grep -n "saying it has none" docs/03-Domain.md` finds nothing; `git diff --cached docs/03-Domain.md` shows two removed and two added lines.

**Divergences.** None.

**Review.** Delivery review (docs/05 §5), read-only agent on Opus: no findings that break the page, docs/04 or this delivery. It noted that the queue line's text says "a finding the code review confirms" where the row says "the person confirms"; decision 1 covers it, and the queue line's text stays as its definition. No new queue line.

```commit
docs(docs03-finding-and-gain): align finding and team gain rows

- finding row includes a review candidate the person confirms
- team gain row copies docs/04: no sentence on a missing number
work/done/docs03-finding-and-gain.md
```
