# ch15-review-range-order

**Objective.** A reader of chapters 15 and 8 knows which commits a milestone review's range holds: every commit after the previous review's commit, so all the fixes of that review's findings and those of the next milestone's deliveries that landed after it, not every one of them; both editions. Finding R2-1 of `m17-review` (work/done/m17-review.md).

**Decided without the author.** A batch /propose with no question asked; each choice below is the recommended one and names its source.

1. The fault is the quantifier, not the rule. Chapter 15 says "The previous review's commit sits before every commit of the next milestone", and chapter 8 says the range holds "the next milestone's deliveries in whatever order they landed". Neither holds: a free line does not wait for the milestone before it (chapter 14, §The next line; docs/05 §4, free line), so a delivery of the next milestone can be committed while the previous review is still `[*]`, before the review's commit. The rule itself, docs/05 §8, is right and unchanged.
2. The new text keeps the sentence's reason: the fixes of a review's findings are always committed after that review, since they are lines it writes, so the range always holds them; of the next milestone's deliveries, it holds those that landed after the review's commit.
3. The text says that a delivery committed before the review's commit is outside the range, and does not say where it was read. A delivery committed before the previous review's code reading is in that reading's range, but one committed between that reading and the review's commit is in neither, so a blanket claim would be false; and the finding stops at "not every one of them" (docs/05 §8: no widening of a finding). Whether the process should close that gap is not this line's.
4. The pointer "(chapter 14)" stays in the new sentence: it leans on a specific term, the free line, that chapter 14 teaches (docs/04, Chapter pointers).
5. Files other slugs touch, and the order (the batch's order; docs/05 §4 and §6 as they read when /apply runs, since `conflict-same-lines`, applied first, may change how a shared hunk is treated):
   * `book/en/15-closing-a-milestone.md` and `book/pt/15-closing-a-milestone.md`: this slug edits the sentence after "Its page names as the base" (line 21); `ch15-first-commit-base`, applied next, edits the sentence "The first commit, the base of a first milestone" (line 23). Two lines apart, so one hunk: `ch15-first-commit-base` starts its /apply only after this delivery's commit. In pt, `docs03-checker-pt` (another agent's, applied later) may edit line 22 ("A leitura custa"), in the same hunk; it too follows this commit.
   * `book/en/08-install-and-hosts.md` and `book/pt/08-install-and-hosts.md`: this slug edits the sentence that starts "Item 3 names as the base" (pt "O item 3 cita como base", line 81); `untracked-diff-wording` edits the sentence before it, "Item 2 has the delivery review" (line 80), in the same hunk, and applies after this commit. `ch08-report-item-one` (report block, item 1) and `pt-ch08-migration-label` (pt key point) touch other hunks of the same files: stage by hunk if they are in the tree. Line numbers shift as these land; /apply finds each passage by its text.
6. No new docs/03 term, no queue line, no change to docs/05: the chapters are brought to what docs/05 §8 already says. No `kit:` note: the kit's changelog says only "The range then holds the fixes of the previous review's findings", which is true.

**Behaviour.**

* A reader of chapter 15, §The review is a delivery, can say that the range from the previous review's commit holds every fix of that review's findings, and only those of the next milestone's deliveries committed after that commit.
* The same reader can say why one delivery of the next milestone may be outside the range: its line was free while the review was still open, and it was committed first.
* A reader of chapter 8, §What an update reports, reads the same thing in the sentence on item 3.
* Fails: `grep -n "sits before every commit\|in whatever order they landed" book/en/15-closing-a-milestone.md book/en/08-install-and-hosts.md` finds a line; `grep -n "fica antes de todo commit\|em qualquer ordem em que entraram" book/pt/15-closing-a-milestone.md book/pt/08-install-and-hosts.md` finds a line.
* Edge: chapter 15's key point ("its page names as the base the commit of the previous milestone's review") and §No second review ("`m2-review`'s range starts at `m1-review`'s commit and holds `returned-loan`'s fix") stay as they are: both are true.

**Contract.** The sentences, as /apply writes them (one sentence per line, docs/04).

`book/en/15-closing-a-milestone.md`, replacing the line "The previous review's commit sits before every commit of the next milestone, whose deliveries can land before the previous one's findings close, so the range from it holds all of them, the fixes of those findings included.":

```
The range from the previous review's commit holds every commit made after it: all the fixes of that review's findings, which close after it, and the next milestone's deliveries that landed after it.
A free line of the next milestone does not wait for the review (chapter 14), so a delivery committed before the review's commit is outside the range from it.
```

`book/pt/15-closing-a-milestone.md`, replacing the line "O commit da revisão anterior fica antes de todo commit do marco seguinte, ...":

```
O intervalo a partir do commit da revisão anterior guarda todo commit feito depois dele: todas as correções dos achados dessa revisão, que fecham depois dele, e as entregas do marco seguinte que entraram depois dele.
Uma linha livre do marco seguinte não espera a revisão (capítulo 14), então uma entrega cujo commit veio antes do commit da revisão fica fora do intervalo a partir dele.
```

`book/en/08-install-and-hosts.md`, in the sentence on item 3, "so the range holds every commit after that review, the fixes of its findings and the next milestone's deliveries in whatever order they landed" becomes:

```
so the range holds every commit after that review: the fixes of its findings, and the next milestone's deliveries that landed after it
```

`book/pt/08-install-and-hosts.md`, in the sentence on item 3, "para que o intervalo guarde todo commit depois dessa revisão, as correções dos seus achados e as entregas do marco seguinte em qualquer ordem em que entraram" becomes:

```
para que o intervalo guarde todo commit depois dessa revisão: as correções dos seus achados e as entregas do marco seguinte que entraram depois dela
```

The rest of each sentence, its link to chapter 15 included, stays. Terms: free line (linha livre), milestone review (revisão de marco), finding (achado), docs/03; no new term.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Where a delivery committed before the review's commit is read, and any rule to close the gap between a review's reading and its commit: decision 3; a process question, not this finding.
* docs/05 §8 and docs/03's milestone review row: already right.
* Chapter 15's key points and §No second review: true as written (Behaviour, edge).
* Line 23 of chapter 15 ("the whole project"): `ch15-first-commit-base`.

**Done when.**

* [x] Chapter 15 and chapter 8 carry the Contract's text, in both editions.
* [x] The Behaviour's greps find nothing.
* [x] No number, no private case, no em dash, no narrated run in the new text.
* [x] `make verify` green.
* [x] The delivery review run as docs/05 §5 says, on this delivery's hunks of the four files and this page.
* [x] `make book`, and the paths of both PDFs given to the author (docs/05 §5, Proof of a screen).
* [x] Page in `work/done/`, line `[x]`, staged by hunk where the files hold other deliveries' changes (decision 5), commit message in a `commit` block.

Queue line, as it stands in docs/06:

```
[~] ch15-review-range-order  chapters 15 and 8 say the review's range holds the next milestone's deliveries that landed after the review's commit, not every one of them; both editions
```

**Built.** Chapter 15, §The review is a delivery, both editions: the sentence after "Its page names as the base" is replaced by the Contract's two sentences. Chapter 8, §What an update reports, both editions: the sentence on item 3 carries the Contract's clause; its link to chapter 15 and the rest of the sentence stay. The Behaviour's greps find nothing.

**Decisions at apply time.** `make book` is run once by the batch driver at the end of the parallel run, not by this /apply; the driver gives the author the PDF paths. Staging is the driver's, from the paths this delivery reports, in this parallel run. No Case A or Case B passage.

**Divergences and omissions.** None.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure).

**Delivery review.** One read-only agent on Opus read this delivery's hunks of the four chapter files against this page and docs/04. No findings: the text matches the Contract in all four places, the Portuguese mirrors the English, the pointer to chapter 14 leans on the free line, and both claims hold against chapter 14 and docs/05 §8.

```commit
docs(ch15-review-range-order): say which commits a review's range holds

- Chapter 15: the range holds every fix and the deliveries after the review's commit
- Chapter 15: a free line's delivery committed before that commit is outside it
- Chapter 8's item 3 sentence says the same
- Both editions

work/done/ch15-review-range-order.md
```
