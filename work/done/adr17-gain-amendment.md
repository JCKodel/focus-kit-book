# adr17-gain-amendment

**Objective.** Whoever reads ADR-0017 learns that a chapter whose gain has no number states the gain alone, with no sentence about the missing number, as docs/04 and docs/03 already say.

**Decided without the author.**

1. Amend, do not rewrite. The Decision's bullet **A gain per chapter** (ADR-0017:18) stays byte for byte, and a new amendment at the end of the ADR says it is read through the amendment. Source: the queue line ("carries an amendment"), ADR-0016's amendment `ch15-injection-rule` ("is read through this one and are not rewritten") and ADR-0017's own three amendments, which never edit the Decision.
2. The heading names this delivery and the day /apply runs: `## Amendment, 2026-10-17 (adr17-gain-amendment)`, and the text credits the rule to `one-gain-section` and the author's review of 2026-10-16. Source: ADR-0005's amendment (`od4-kit-pointer`), which names the delivery that writes it and the one that made the change; dating it 2026-10-16 under `one-gain-section` would say that delivery wrote it, and it did not (m15-review, doc-2: "with no amendment for `one-gain-section`"). If /apply runs on another day, it uses that day and records it under Divergences.
3. The wording copies docs/04 §Chapter shape (**A gain per chapter**: "with its number or a sourced claim where the book has one, and otherwise the gain alone, with no sentence on the missing number") and adds the prologue's sentence on the baseline from docs/04 **One gain**, so ADR, docs/03 and docs/04 cannot drift apart again. Same choice as decision 2 of `docs03-finding-and-gain`.
4. Scope is ADR-0017 alone: docs/04 (`one-gain-section`) and docs/03 (`docs03-finding-and-gain`) already say it, and no chapter changes, so the both-editions rule does not apply. Source: m15-review's table, `adr17-gain-amendment` | ADR-0017 | doc-2.
5. No new docs/03 term and no new queue line: `team gain` exists, and the change fits one page.

**Behaviour.**

* After the delivery, reading ADR-0017 to the end, the reader finds an amendment that says a gain with no number is stated alone, with no sentence about the missing number, and that the lack of a baseline is said once, in the prologue.
* The amendment says the Decision's "or one sentence saying the gain has no number" is read through it, so a reader of line 18 is not left with the old allowance as the rule.
* The amendment names where the rule came from (`one-gain-section`, the author's review of 2026-10-16) and where it lives now (docs/04 §Chapter shape).
* Edge: line 18 and every other line already in ADR-0017 stay byte for byte; the diff only adds lines at the end of the file.
* Edge: docs/03, docs/04, docs/05, the other ADRs and both editions do not change.
* Fails: an amendment that rewrites or deletes the Decision's bullet; an amendment that says a gain may carry "no number" in any form a chapter could copy as its sentence.

**Contract.** ADR-0017, appended after the last line of the amendment `renumber-chapters`, with one blank line before the heading and one after it, one sentence per line:

```
## Amendment, 2026-10-17 (adr17-gain-amendment)

A chapter's gain section holds a number or a sourced claim where the book has one, and otherwise the gain alone, with no sentence on the missing number; that no study in the book measures a team with the method against the same team without it is said once, in the prologue.
The author decided it in the review of 2026-10-16 and `one-gain-section` applied it to every chapter and to docs/04 §Chapter shape; the Decision's "or one sentence saying the gain has no number" is read through this amendment and is not rewritten.
```

No new term; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* ADR-0017:18 itself: amended, not rewritten (decision 1).
* docs/03's `team gain` row: done by `docs03-finding-and-gain`.
* docs/04: already says it since `one-gain-section`.
* Any chapter, either edition: no reader-facing text changes.
* doc-3 to doc-8 of m15-review: their own lines or weak.

**Done when.**

* [x] ADR-0017 ends with the Contract's block, byte for byte, and `git diff --cached docs/adr/ADR-0017-the-rewrite.md` shows only added lines, at the end of the file.
* [x] `grep -n "one sentence saying the gain has no number" docs/adr/ADR-0017-the-rewrite.md` finds line 18 and the amendment's quote, and nothing else.
* [x] `make verify` green; no em dash on this page or in the amendment.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06 (docs/05 §6), other sessions' changes left unstaged; commit message in a `commit` block.

**Divergences.** None: /apply ran on 2026-10-17, the day the Contract's heading names.

**Decisions taken in /apply.**

1. The prologue sentence in the amendment follows docs/00 product question 7 ("no study in the book measures a team with the method against the same team without it") and docs/04 **One gain**, which both say it is the prologue's alone; the English prologue says it at line 105. Recommended option, no question asked (batch run).

**Proof.**

* `git diff --cached docs/adr/ADR-0017-the-rewrite.md`: five added lines after the `renumber-chapters` amendment, none removed.
* `grep -n "one sentence saying the gain has no number" docs/adr/ADR-0017-the-rewrite.md`: line 18 and line 46, the amendment's quote.
* `make verify`: green (build, parity, em dash, prose, links, disclosure).
* No file under `book/` changed, so no `make book`.

**Review.** A read-only Opus agent read this delivery's diffs against the page and docs/04 (docs/05 §5). Nothing breaks the page or docs/04: the Contract matches byte for byte, line 18 is unchanged, and the wording matches docs/04, docs/03 and docs/00 product question 7. Two nits, both fixed: the Proof cited `git diff` for a staged change, now `git diff --cached`; the docs/06 hunk is staged after the line becomes `[x]`. No new queue line.

```commit
docs(adr17-gain-amendment): amend ADR-0017 on a gain with no number

- ADR-0017 ends with an amendment: a gain with no number is stated alone
- the baseline is said once, in the prologue, as docs/00 and docs/04 say
- the Decision's bullet stays as written and is read through the amendment
work/done/adr17-gain-amendment.md
```
