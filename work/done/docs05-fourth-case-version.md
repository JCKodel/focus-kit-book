# docs05-fourth-case-version

**Objective.** A session or a person reading docs/05 §4 or docs/03's waiting mark row can tell that the six marks are those of focus-kit 2026.10.05 and that the fourth case a line waits in, a code reading that missed part of its range, came with focus-kit 2026.10.18.

**Decided without the author.** This page was written in a batch /propose with no question asked (the author's instruction for this run); each decision names its source, so the author corrects it in the review of this page.

1. The dates: the marks are 2026.10.05's (ADR-0018, its decision); the fourth case is 2026.10.18's (ADR-0018's amendment of 2026-10-18, from `kit-2026-10-18`). docs/03:30's mark row ("one of focus-kit's six (since 2026.10.05)") is already right and does not change.
2. docs/04 §Writing the book, The kit as it is, forbids naming a version as a date in the book's chapters; docs/05 and docs/03 are process documents, and both already date the marks, so the rule does not apply here (docs/04 §Languages lists `docs/` as process documents).
3. Kit: `kit:` none; the dating sentence is this project's (it cites this repository's ADR-0018), and the kit's text has its own.

**Behaviour.**

* A reader of docs/05 §4's paragraph that closes the marks reads that the marks are focus-kit 2026.10.05's and the fourth waiting case 2026.10.18's, both with ADR-0018.
* A reader of docs/03's waiting mark row reads that the kit took the mark in 2026.10.05, and this book with it, and that the fourth case came with 2026.10.18, with ADR-0018's amendment named.
* Edge: nothing else in either sentence changes; the four cases themselves are not reworded here (`docs05-four-cases-sentence` does docs/05's sentence of cases).
* Fails, and is fixed before done: a sentence that still reads as if all four cases were 2026.10.05's.

**Contract.**

Exact; /apply rewraps docs/05's paragraph to the file's width and changes no other sentence.

* docs/05 §4, line 134: "These are the marks of focus-kit 2026.10.05 (ADR-0018)." becomes "These are the marks of focus-kit 2026.10.05, and the fourth case a line waits in is that of 2026.10.18 (ADR-0018 and its amendment of 2026-10-18)."
* docs/03, row `waiting mark`, line 106, its last sentence: "Case A made it by hand for lines waiting on a person; the kit took it in 2026.10.05, and this book with it (ADR-0018, superseding ADR-0013)." becomes "Case A made it by hand for lines waiting on a person; the kit took it in 2026.10.05, and this book with it (ADR-0018, superseding ADR-0013); the fourth case came with 2026.10.18 (ADR-0018's amendment of 2026-10-18)."
* No new term.

Shared files and order: this applies after `conflict-same-lines` (docs/05:142-143, :252-254; docs/03:93) and before `docs05-review-concurrency` (docs/05:232-238) and `docs05-four-cases-sentence` (docs/05:115-118); other agents' `untracked-diff-wording` (docs/03:75) and `docs03-checker-pt` (docs/03:33, :36) touch docs/03 too. Each is another hunk, at least seven unchanged lines from this one; an earlier delivery's hunks may still be staged and not committed when this one runs, so /apply stages only this delivery's hunks of docs/05 and docs/03 with `git add -p`, and its own line of docs/06.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* docs/03:30's mark row: already dated right (decision 1).
* The wording of the four cases: `docs05-four-cases-sentence`.
* ADR-0018: its amendment already dates the fourth case.
* The chapters: they name no version as a date (docs/04, The kit as it is).

**Done when.**

* [x] docs/05:134 and docs/03:106 hold the Contract's exact text.
* [x] `make verify` green.
* [x] The delivery review run as docs/05 §5 says, and recorded.
* [x] Page in `work/done/`, line `[x]`, staged by hunk as the Contract says, commit message in a `commit` block.

**Built.** docs/05 §4's closing sentence on the marks and docs/03's waiting mark row hold the Contract's exact text; the docs/05 sentence is rewrapped onto three lines within the paragraph's width, and no other sentence changed.

**Decisions at apply time.** None beyond the page's. No Case A or Case B passage.

**Divergences and omissions.** None.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure).

**Delivery review.** One read-only agent on Opus read this delivery's hunks of docs/05 and docs/03 and its line of docs/06 against this page, docs/04 and ADR-0018 with its amendment. No finding: both texts match the Contract, the rewrapped lines keep to the paragraph's width, no em dash, and "its amendment of 2026-10-18" names ADR-0018's only amendment of that date.

```commit
docs(docs05-fourth-case-version): date the fourth waiting case 2026.10.18

- docs/05 §4 says the marks are 2026.10.05's and the fourth case 2026.10.18's
- docs/03's waiting mark row names ADR-0018's amendment for the fourth case

work/done/docs05-fourth-case-version.md
```
