# docs06-m16-paragraph

**Objective.** Whoever reads M16's paragraph in docs/06 reads that the reviews' readers and their checker are the one specialized subagent the governor admits, as docs/05 and chapter 16 say, and M15's `pt-free-line-done` line reads in the same column as its neighbours. Found by `m16-review` (work/done/m16-review.md, doc-4 seen: "docs/06:361, the M16 paragraph says "the reviews' readers" where docs/05:291, docs/06:368 and chapter 16 say readers and checker"; doc-8 seen, cosmetic: "docs/06:336, `pt-free-line-done`'s sentence starts one column left of its neighbours").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The words are those of docs/05 §7 ("no specialized subagent beyond the reviews' readers and checker") and chapter 16's key point ("the reviews' readers and checker are the one specialized subagent it admits"), so the paragraph only gains "and checker", and its singular "the one specialized subagent" stays, as in chapter 16. Source: docs/05:293; book/en/16-the-governor.md:87; docs/06:368.
2. Only `pt-free-line-done` moves. In M15's block every other line's sentence starts at column 30 (a prefix of 29 characters); this one's prefix is 28, so its slug gets one more space. Other milestones use their own column, and a few lines whose slug is longer than the column are not this finding. Source: a measurement of docs/06 when this page was written (lines 330 to 339 at 29, line 336 at 28).
3. The milestone is closed, its review done, and the paragraph still owns what M16 promised, so it is fixed in place; `m16-review`'s page, which quotes the old paragraph, is history and stays. Source: docs/05 §4 (the queue is edited by conversation in any session); work/done/m16-review.md:36.
4. No docs/03 term, no new queue line, no split. Source: docs/03; docs/05 §1.

**Behaviour.**

* After the delivery, M16's paragraph ends its list of what the review does with "and the reviews' readers and checker as the one specialized subagent the governor admits".
* M15's line `pt-free-line-done` has its sentence start in the column of the lines above and below it; its mark, slug and words are unchanged.
* Edge: no other line of docs/06 changes beyond this delivery's own mark, which /apply sets; the driver's marks on the batch's other lines are another session's hunks and are not staged here.
* Fails: a paragraph that drops the checker from any other clause, or a line whose words change.

**Contract.** docs/06, two edits:

* M16's paragraph (line 361): "and the reviews' readers as the one specialized subagent the governor admits;" becomes "and the reviews' readers and checker as the one specialized subagent the governor admits;". The rest of the paragraph stays.
* M15's line (336): `[x] pt-free-line-done` followed by eight spaces instead of seven, so its sentence starts at column 30, as on lines 330 to 339.

No new term; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* work/done/m16-review.md's quote of the paragraph: history.
* The columns of other milestones' blocks (decision 2).
* Any other wording of M16's paragraph: no finding names it.

**Order with the other slugs of this batch.** Sixth; it touches only docs/06, whose other hunks (the marks) the driver sets. Its two edits are in M15's block and in M16's paragraph, apart from the M16 lines whose marks change, so they are this delivery's own hunks, staged with its own mark line (docs/05 §4).

**Done when.**

* [x] docs/06:361 and :336 read as the Contract says, and nothing else in docs/06 changes but this delivery's mark.
* [x] The column of line 336's sentence measured again and recorded on this page.
* [x] `make verify` green; no em dash.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its own hunks of docs/06 (docs/05 §6), other sessions' changes left unstaged; commit message in a `commit` block.

**Proof.** `git diff` of docs/06, this delivery's hunks only: line 361 gains "and checker" and nothing else in the paragraph changes; line 336 gains one space after its slug; line 378 is this delivery's mark. The column measured again: lines 330 to 339 all have a prefix of 29 characters, so every sentence of M15's block, line 336's included, starts at column 30. `make verify` green: build, parity, em dash, prose, width, links, disclosure.

**Divergences.** None.

**Omissions.** None.

**Decisions taken in /apply.** None beyond the page's.

**Review.** Delivery review by a read-only Opus agent on this delivery's hunks of docs/06 and this page, against the page, docs/04, docs/05 §7 and chapter 16. No findings: line 361 reads as the Contract says, matching docs/05:293 and book/en/16-the-governor.md:87; line 336's sentence starts at column 30 with mark, slug and words unchanged; no em dash; the width rule does not measure docs/06.

```commit
docs(docs06-m16-paragraph): name the checker in M16's paragraph

- docs/06: M16's paragraph names the reviews' readers and checker
- docs/06: M15's `pt-free-line-done` sentence starts in its neighbours' column

work/done/docs06-m16-paragraph.md
```
