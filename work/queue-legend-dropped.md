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

* [ ] The three edits are in place word for word; every Behaviour line reads true against docs/06, docs/03 and docs/05 §4.
* [ ] Only the legend hunk and this line's mark of docs/06 are staged, with docs/03 and this page; other lines' hunks stay as other sessions left them.
* [ ] `make verify` green after the last edit. `make book`: inapplicable, no chapter changes. Both editions: inapplicable, the process documents are English only.
* [ ] Delivery review by a read-only Opus agent per docs/05 §5, its candidates answered on this page; the page moves to `work/done/` and the commit message is suggested.
