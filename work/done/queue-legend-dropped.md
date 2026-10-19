# queue-legend-dropped

**Objective.** A person reading docs/06's legend or docs/03's glossary learns what focus-kit 2026.10.18.1 says: a cancelled line is `[x]` with `· dropped: <reason>`, and a conflict between two sessions is a line both edited, not two neighbouring lines in one hunk.

**Behaviour.**

* Reading docs/06's legend, a person finds `· dropped: <reason>` named as the suffix of an `[x]` line the person cancelled, with docs/05 §4 as its rule, in the same words as SETUP.md's docs/06 template.
* Reading docs/03's `mark` row, a person still counts six marks: `· dropped:` is a suffix on `[x]`, not a seventh mark, and the row says what a dropped line's page holds.
* Reading docs/03's `conflict` row, a person learns that two sessions conflict on a line both edited, or on a file one page needs that the other delivery is changing; two deliveries' edits in one hunk, each on its own line, are no conflict.
* No other sentence of the legend changes; docs/05 §4, which already holds both rules, does not change.

**Contract.** Three exact edits, in English (the process documents' language).

1. docs/06, legend, first line. The clause
   `` `[?]` waiting, with `· resume: propose` or `· resume: apply` before `· blocked: <reason>` or `· blocked: after <slug>, <slug>` at the end of the line. ``
   becomes
   `` `[?]` waiting, with `· resume: propose` or `· resume: apply` before `· blocked: <reason>` or `· blocked: after <slug>, <slug>` at the end of the line, and `· dropped: <reason>` on an `[x]` line the person cancelled (docs/05 §4). ``
   Source: focus-kit SETUP.md 2026.10.18.1, its docs/06 template legend.
2. docs/03, row `mark`, Meaning: after "set at the moment the work changes, not when a command ends, so the queue shows work while it happens;" insert "an `[x]` line ending `· dropped: <reason>` is a delivery the person cancelled, a suffix and not a seventh mark, its page in `work/done/` saying what was built and undone;" before "a line never leaves the queue." Source: docs/05 §4.
3. docs/03, row `conflict`, Meaning: the sentence "Between two sessions in one folder, the same lines edited by both, or a file one page needs that the other delivery is changing: the session stops and reports; two lines next to each other, one changed by each, are no conflict, though git shows them in one hunk." becomes "Between two sessions in one folder, a line both sessions edited, or a file one page needs that the other delivery is changing: the session stops and reports; two deliveries' edits in one hunk, each on its own line, as two neighbouring queue lines are, are no conflict." Source: docs/05 §4 and SETUP.md 2026.10.18.1's docs/05 template §4.

The docs/06 legend edit is part of this delivery. It sits in the file's first lines, a hunk apart from the queue lines whose marks other sessions change; /apply stages that hunk and this line's own mark only, as docs/05 §4 and §6 say, and leaves every other line's hunk unstaged. No data, schema or API change. No new docs/03 term.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.** Chapters: chapter 14 already teaches dropped lines (`ch14-ended-and-dropped`) and chapter 19 the conflict by line. docs/05 and ADR-0018: they already hold both rules (`kit-2026-10-18-1`). The kit repository: unchanged.

**Decisions from the documents.** The legend takes SETUP.md's clause word for word, so the project's legend and the kit's template do not drift (docs/05 §5's slots, kit-2026-10-18-1). The conflict row takes docs/05 §4's wording rather than a paraphrase, since docs/03 follows docs/05's definitions (kit-2026-10-18-1's Contract).

**Done when.**

* [x] The three edits are in place word for word; every Behaviour line reads true against docs/06, docs/03 and docs/05 §4.
* [x] Only the legend hunk and this line's mark of docs/06 are staged, with docs/03 and this page; other lines' hunks stay as other sessions left them.
* [x] `make verify` green after the last edit. `make book`: inapplicable, no chapter changes. Both editions: inapplicable, the process documents are English only.
* [x] Delivery review by a read-only Opus agent per docs/05 §5, its candidates answered on this page; the page moves to `work/done/` and the commit message is suggested.

**Built.** docs/06's legend now names `· dropped: <reason>` as the suffix of an `[x]` line the person cancelled, citing docs/05 §4, in the clause SETUP.md 2026.10.18.1's docs/06 template gives. docs/03's `mark` row says a dropped line is a suffix on `[x]`, not a seventh mark, its page in `work/done/` saying what was built and undone. docs/03's `conflict` row now says a conflict between sessions is a line both edited, and two deliveries' edits in one hunk, each on its own line, are none.

**Divergences.** None.

**Decisions.** The three edits are the Contract's text word for word; no question was left open. Under the batch, the driver sets this line's mark and stages the docs/06 legend hunk with the mark, docs/03 and this page.

**Proof.** `git diff` of docs/06 and docs/03 shows only the legend line and the two rows changed; docs/05 is unchanged. `make verify` green after the last edit. `make book`: inapplicable, no chapter changes.

**Delivery review.** A read-only agent on Opus read this delivery's hunks of docs/06 and docs/03 against this page, docs/05 §4 and docs/04. The three edits match the Contract word for word, and every Behaviour line reads true. Points: (1) the queue line was still `[>]`: under this batch, the driver sets the mark and stages it. (2) It could not open SETUP.md to compare the legend: the clause is the Contract's, which cites SETUP.md. (3) The new clause follows the `[?]` item and reads a little oddly: it is SETUP.md's wording, kept so the legend and the template do not drift.

```commit
docs(queue-legend-dropped): name the dropped suffix and line conflicts

- docs/06's legend names `· dropped: <reason>` on a cancelled `[x]` line
- docs/03's mark row: dropped is a suffix, not a seventh mark
- docs/03's conflict row: a line both sessions edited, not one hunk

work/done/queue-legend-dropped.md
```
