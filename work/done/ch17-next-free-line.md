# ch17-next-free-line

**Objective.** After chapter 17 the reader can check the manager's sample answer against the queue chapters 11 and 14 teach: with `return-book` being built, the next free line is `m1-review`, which names no `after` and sits above milestone 2's `due-date-format`, and the milestone's count is the six lines chapter 11 shows; both editions. This answers m23-review's D7 (`work/done/m23-review.md`, Findings).

**Behaviour.** What the reader can do or explain after the chapter:

* Read the sample answer and find its "Next free line" by chapter 14's rule: the first line counting down the queue that is not `[x]` and not `[?]` and whose `after` lines are all `[x]`; that is `m1-review`, not `due-date-format`.
* Read its "Run" line and see the command for the line it names, on both hosts, as chapter 8's table writes it.
* Count the milestone's lines in chapter 11's queue (skeleton, catalog, members, lend-book, return-book, m1-review) and get the answer's "4 of 6": four `[x]`, `return-book` in flight, `m1-review` free.
* Edge: no seventh line is left for the reader to imagine; any seventh line would be either waiting (against "Waiting: none") or free above `m1-review` (then it would be the next free line), and `fix-overdue-return` comes only once `return-book` is built (chapter 11 :79).
* Edge: `due-date-format` stays free and is not named: chapter 14 :77 to :78 says it does not wait for `m1-review` but is reached only once milestone 1 holds no free line.

**Contract.** Chapter 17, both editions, the sample answer's code block (:124 to :128), against the files as they are today (en and pt line numbers match). One line per line, as the block is laid out; nothing else in the chapter changes.

* `book/en/17-project-as-assistant.md`:
  * :124 "Milestone 1, a librarian lends and takes back: 4 of 7 lines done." becomes "Milestone 1, a librarian lends and takes back: 4 of 6 lines done."
  * :127 "Next free line: due-date-format [ ], no page yet." becomes "Next free line: m1-review [ ], no page yet."
  * :128 "Run: /propose due-date-format (Codex: $propose due-date-format)" becomes "Run: /propose m1-review (Codex: $propose m1-review)"
* `book/pt/17-project-as-assistant.md`:
  * :124 "Marco 1, um bibliotecário empresta e recebe de volta: 4 de 7 feitas." becomes "Marco 1, um bibliotecário empresta e recebe de volta: 4 de 6 feitas."
  * :127 "Próxima linha livre: formato-devolucao [ ], ainda sem página." becomes "Próxima linha livre: m1-review [ ], ainda sem página."
  * :128 "Rode: /propose formato-devolucao (Codex: $propose formato-devolucao)" becomes "Rode: /propose m1-review (Codex: $propose m1-review)"
* `m1-review` stays in English in the Portuguese edition, as the kit writes it (chapter 11 pt :96).
* :125, :126 and :131 to :134 stay: "the first free line" at :131 still describes the answer, and :132's `return-book` example is unaffected.
* Terms of docs/03: free line, milestone review, queue. No new term; no docs/03 row.
* Sources: chapter 11 :49 to :55 (the queue, `m1-review` with no `after`) and :79; chapter 14 :68 and :76 to :78 (free line, the first counting down the queue); docs/03's `free line` row. No footnote: the reader gains nothing to open.
* Cases: none. Example: the lending library, written for the chapter, as the text before the block already says.
* Neighbouring lines on the same file: `ch17-23-git-slot-word` (M23, applied before this one) edits chapter 17 :137 only, below this block, so these line numbers hold after it; M24's `ch12-14-17-20-branch-claim` edits chapter 17 later and finds this block as this delivery leaves it.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 17 :131 to :134 and :137 (the last is `ch17-23-git-slot-word`'s).
* Chapters 11 and 14: the source of the queue, not targets.
* D3 and D5, summaries pointing to chapters 14 and 17: dropped weak by the review.
* Any version, date or history of the kit's rule.

**Decisions from the documents.**

* The next delivery is the first free line counting down the queue, and a milestone's end sets priority, not whether a line is free: docs/05 §4, docs/03's `free line` row, chapter 14 :76 to :78.
* `m1-review` names no `after` in chapter 11's queue, so it is free while `return-book` is `[*]`: chapter 11 :54, docs/03's `free line` row.
* Finding D7, seen, medium: `work/done/m23-review.md`.
* Taught as the kit is today (2026.10.19.2), with no version or "now": AGENTS.md.

**Decisions taken alone.**

* The answer names `m1-review`; the queue line's other branch, "or the queue it reads says otherwise", is not taken: giving `m1-review` an `after` or showing a different queue would contradict chapter 11 :54 and chapter 14 :77 to :78.
* "4 of 7" becomes "4 of 6", a sibling in the same block that goes stale once `m1-review` is named and that no other line owns: chapter 11's milestone 1 has six lines, and a seventh would be waiting, or free above `m1-review`, or `fix-overdue-return`, which comes only after `return-book` is built.
* :131 gains no clause on why the review comes before `due-date-format`: chapter 14 :77 to :78 teaches it, and "the first free line" already holds.
* The queue line keeps its wording.

**Done when.**

* [x] Both editions changed in the three block lines the Contract names, and nowhere else in chapter 17.
* [x] `grep -n "due-date-format\|4 of 7" book/en/17-project-as-assistant.md` and `grep -n "formato-devolucao\|4 de 7" book/pt/17-project-as-assistant.md` find nothing.
* [x] The chapter still opens with its value; no filler, nothing useful cut; one sentence per line kept.
* [x] No version, date, before/after or narration of a run in the text; no em dash; no private case used.
* [x] `make verify` green after the last edit, its result recorded in this page's Proof.
* [x] `make book` built both PDFs: the batch's driver ran it after the last M23 fix lane, at `16fdca6` (exit 0), whose chapter 17 is as this delivery left it, and `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths, after M24 changed chapter 17 (Proof).
* [x] Delivery review by one read-only Opus agent this lane launched, over chapter 17 and this page (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded.

**Proof.**

`git diff HEAD -- book/` shows chapter 17 only, 6 insertions and 6 deletions: lines :124, :127 and :128 in each edition, with the strings the Contract names; no line moved.
Both Done-when greps find nothing; no chapter still says "4 of 7" or "4 de 7".

`make verify` green after the last edit. The batch's driver ran `make book` after the last M23 fix lane, at `16fdca6` (exit 0), whose chapter 17 is as this delivery left it; `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths, after M24 changed chapter 17.

**Divergences.** None.

**Decisions.**

* The open branch of the queue line is taken with the recommended option, as the page's Decisions taken alone already say: the answer names `m1-review`.

**Delivery review.** One read-only Opus agent, launched by this lane, over this delivery's paths (`git diff HEAD` of chapter 17 en and pt) and this page, against the page, docs/04 and AGENTS.md; it read chapter 11 en and pt :45 to :100, chapter 14 en and pt :64 to :80, docs/03's `free line` row, chapter 17 en and pt :110 to :140 and chapter 15 en by search. Verdict: passes, no findings; the Contract strings are in place in both editions and nothing else changed, `m1-review` is the first free line by chapter 14's rule, "4 of 6" matches chapter 11's six lines, :131 to :134 still hold, and `m1-review` stays in English in the pt edition as chapter 11 pt :57 and :96 write it.
It noted, not as a finding, that the answer starts the milestone's review while `return-book` is still being built, which chapter 15 :25 and :128 allow.

**Noted, not fixed.** Nothing.

**Dropped.** Nothing.

```commit
docs(ch17-next-free-line): name m1-review as ch17's next free line

- ch17's sample answer names m1-review, the first free line
- the milestone's count reads 4 of 6, chapter 11's six lines
- both editions

work/done/ch17-next-free-line.md
```
