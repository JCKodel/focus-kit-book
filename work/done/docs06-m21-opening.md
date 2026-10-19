# docs06-m21-opening

**Objective.** Whoever reads M21's paragraph in docs/06 reads that the kit was planted in Ninjobs after the opening, in chapter 6's words. Found by `m22-review` (work/done/m22-review.md, finding 25, P3, seen, low: "`docs/06-Queue.md`:517 (from `docs-m21-tidy`:22): M21's paragraph says the kit was planted "after the beta"; chapter 6:50 says "after the opening" on purpose (`ch06-kit-after-ninjobs`:53, 62; `m21-review`:27)").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The word is chapter 6's: "after the opening". `ch06-kit-after-ninjobs` chose it on purpose, since the chapter calls 2026-09-10 the public opening and never says beta, and `m21-review` already asked its question in those words. Source: book/en/06-birth-of-focus-kit.md:50; work/done/ch06-kit-after-ninjobs.md:53; work/done/m21-review.md:27.
2. Only the paragraph changes. M21's line `ch06-kit-after-ninjobs` (docs/06:530) also says "after the beta", but it is a done line that records what was asked, and the finding names the paragraph alone; it stays. Source: work/done/m22-review.md:90; docs/05 §1 (least change).
3. The milestone is closed, its review done, and the paragraph still owns what M21 promised, so it is fixed in place; `docs-m21-tidy`'s and `m21-review`'s pages are history and stay. Source: docs/05 §4; precedent work/done/docs06-m16-paragraph.md, decision 3.
4. No chapter changes: chapter 6 already says "after the opening" in both editions (book/en and book/pt, line 50). docs/06 is a process document, in English only, so there is no Portuguese wording. Source: AGENTS.md; docs/05.
5. No docs/03 term, no new queue line, no split. Source: docs/03; docs/05 §1.
6. Last of M22's finding lines, as m22-review orders, since it edits the queue itself. Source: work/done/m22-review.md:109.

**Behaviour.**

* After the delivery, M21's paragraph says "the kit planted there after the opening".
* `grep -n "after the beta" docs/06-Queue.md` finds only line 530, the done line of decision 2.
* Edge: no other word of M21's paragraph changes, and no other line of docs/06 changes beyond this delivery's own mark, which /apply sets; the driver's marks on the batch's other lines are another session's hunks and are not staged here.
* Fails: a paragraph that still says "beta", or any chapter touched.

**Contract.** docs/06, one edit, in M21's paragraph (line 517):

* "the kit planted there after the beta," becomes "the kit planted there after the opening,". The rest of the paragraph stays.

No Portuguese wording (docs/06 is English only). No new term; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* docs/06:530, `ch06-kit-after-ninjobs`'s done line: the record of what was asked (decision 2).
* work/done/docs-m21-tidy.md and work/done/m21-review.md: history.
* Chapter 6: already right in both editions.

**Done when.**

* [x] docs/06:517 reads as the Contract says, and nothing else in docs/06 changes but this delivery's mark.
* [x] `make verify` green; no em dash.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its own hunks of docs/06 (docs/05 §6), other sessions' changes left unstaged; commit message in a `commit` block.

**Built.** docs/06, M21's paragraph: "the kit planted there after the beta," now reads "the kit planted there after the opening,". No other word of the paragraph changed; of docs/06, besides that, only this line's mark.

**Diverged from the contract.** Nothing.

**Proof.** `git diff HEAD -- docs/06-Queue.md` shows, of this delivery, the paragraph's one word and this line's mark. `grep -n "after the beta" docs/06-Queue.md` finds only the done line of `ch06-kit-after-ninjobs`, as decision 2 keeps it. Chapter 6 says "after the opening" at line 50 in book/en and "depois da abertura" in book/pt; no chapter touched. `make verify` green.

**Review.** A read-only agent on Opus read this delivery's hunks of `git diff HEAD -- docs/06-Queue.md`, this page, docs/04 and chapter 6's line 50 in both editions. It confirmed the Contract word for word, nothing else in the paragraph changed, line 530 kept, no em dash, verify clean. Its two findings were about timing, not the text: the line was still `[*]` while the Done when said `[x]`, and nothing was staged yet. The first is closed by this delivery's last edit, the `[x]`; the second by the driver, which stages and commits this delivery from its own index.

**Decisions.**

* No ADR, no manual and no other document: nothing a person does by hand changes.
* The page's "Decided without the author" stand as written: the driver ran this /apply with recommended answers, so no question was asked.
* Staging: the driver of this batch stages and commits each delivery from a temporary index, so this session staged nothing; the Done when's staging item is the driver's step.
* Other lanes' marks in docs/06 were not touched: of docs/06 only this delivery's paragraph edit and its own mark changed.

```commit
docs(docs06-m21-opening): M21 plants the kit after the opening

- docs/06: M21's paragraph says "after the opening", as chapter 6

work/done/docs06-m21-opening.md
```
