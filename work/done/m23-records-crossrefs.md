# m23-records-crossrefs

**Objective.** A reader of the records of `kit-2026-10-19-2`, `ch08-update-2026-10-19-2`, `ch10-12-run-manual` and `ch13-apply-run-manual` finds them agreeing with each other and with the repository: `ch10-12-run-manual` left chapter 12 untouched and chapter 9 names no file, the Portuguese phrase has one story, no slug is named that no committed queue line holds, and docs/05 §5's Manuals sentence is cited as lines 250 to 254.

**Behaviour.**

* A reader asked "which chapters did M23 teach the kit change in?" answers from `work/done/kit-2026-10-19-2.md`'s Objective and Out of scope: chapters 7, 8, 9, 10 and 13, each by its M23 line, with no chapter 12 (m23-review R5).
* A reader of `work/done/ch08-update-2026-10-19-2.md`'s Out of scope and `work/done/ch13-apply-run-manual.md`'s Out of scope finds `ch10-12-run-manual` owning chapters 7, 9 and 10, never chapter 12, as that page's Built says ("chapters 11 and 12 untouched") (R5).
* A reader of `work/done/ch10-12-run-manual.md` who compares its Behaviour's second scenario (the slot naming `docs/manuals/run-the-app-from-a-clone.md`, chapter 9) with chapter 9 finds the gap stated in Divergences: chapter 9 names the manual of running it, not the library's file, which chapter 7 carries (R6).
* A reader asked "who set the Portuguese phrase 'o manual de rodá-lo' / 'o manual de rodar o produto'?" gets one answer from both pages: `ch13-apply-run-manual`'s /propose picked it, from the kit's README.pt.md, and the batch's driver passed it to `ch10-12-run-manual`'s /apply (R7).
* A reader of `work/done/ch13-apply-run-manual.md`'s Out of scope meets no slug that no committed line of docs/06 holds; the later change to where `/apply`'s fresh session opens is described, not named (R8).
* A reader who opens docs/05 at lines 250 to 254 from `work/done/ch08-update-2026-10-19-2.md`'s Decisions finds the whole Manuals sentence, which ends on 254 (R10).
* Edge: the history stays honest. Each edit corrects what the record states about a fact; no Behaviour, Contract or Done when of the four pages is rewritten as if it had been defined otherwise, and this page names every sentence changed.
* Edge: `ch10-12-run-manual`'s Done when "chapter 12 untouched" and "Chapters 7, 9 and 10 changed ... as the Contract says" stand: the Contract's chapter 9 items never asked for the file name, only Behaviour's second scenario did.
* Edge: `kit-record-step4` and `m23-records-proof` edit the same pages earlier in queue order; the sentences here are none of theirs, and each edit below is found by its section and quoted text, the line numbers being today's.

**Contract.** Record pages under `work/done/`, edited in place with no marker in them, as `m22-batch-proof` did. Line numbers are today's, at `7e7fcae`, and only a guide; /apply finds each sentence by section and quoted text. `kit-2026-10-19-2.md` carries no line numbers here: `kit-record-step4` edits it first and splits its step 4 list.

* **`work/done/kit-2026-10-19-2.md`**
  1. Objective, last sentence: "Chapters 8, 10, 12 and 13 then teach the change (their own M23 lines)." becomes "Chapters 7, 8, 9, 10 and 13 then teach the change (their own M23 lines)."
  2. Out of scope, first clause: "Chapters 8, 10, 12 and 13, each its M23 line;" becomes "Chapters 7, 8, 9, 10 and 13, each its M23 line;". The rest of the paragraph stays.
* **`work/done/ch08-update-2026-10-19-2.md`**
  1. Out of scope (:34), first sentence: "Chapters 7, 9 and 10, their manual sentences included (...), and chapter 12: `ch10-12-run-manual`." becomes "Chapters 7, 9 and 10, their manual sentences included (...): `ch10-12-run-manual`." The parenthesis stays word for word.
  2. Decisions from the documents (:39), the Manuals item: "docs/05 §5 at HEAD (lines 250 to 253)" becomes "docs/05 §5 at HEAD (lines 250 to 254)". Nothing else in the item changes.
* **`work/done/ch10-12-run-manual.md`**
  1. Decisions taken alone in /apply (:76), the phrase item's opening: "The phrase, set by the batch's driver so the book says it one way, here and in `ch13-apply-run-manual`:" becomes "The phrase, picked by `ch13-apply-run-manual`'s /propose and passed by the batch's driver to this /apply so the book says it one way, here and in that delivery:". The rest of the item stays.
  2. Divergences (:85): "None beyond the forward pointer above." becomes "Beyond the forward pointer above, one: Behaviour's second scenario expects chapter 9 to name `docs/manuals/run-the-app-from-a-clone.md` (pt `rodar-o-app-de-um-clone.md`); chapter 9 names the manual of running it and no file, which chapter 7 carries, as the Delivery review noted and left."
* **`work/done/ch13-apply-run-manual.md`**
  1. Out of scope (:39): "Chapters 7, 9, 10 and 12, and the kinds of manual, the Manuals slot and `/analyze`: `ch10-12-run-manual`," becomes "Chapters 7, 9 and 10, and the kinds of manual, the Manuals slot and `/analyze`: `ch10-12-run-manual`,". The rest stays. (Not in m23-review's R5 row, which cites three places; it is the same cause on a page this line names and would go stale.)
  2. Out of scope (:41): "Where `/apply`'s fresh session opens with a worktree per delivery: `ch13-19-session-folder` (M25), which also edits chapter 13; this page leaves line 21 and the \"fresh session\" of line 108 as they are, but adds a sentence to line 108, which that delivery edits on top of." becomes "Where `/apply`'s fresh session opens with a worktree per delivery: a later delivery of the queue's plan, which also edits chapter 13; this page leaves line 21 and the \"fresh session\" of line 108 as they are, but adds a sentence to line 108, which that delivery edits on top of."
  3. Contract :18 and Decisions taken alone :56 stay: "this page fixes it, for the driver to pass on" and "since `ch10-12-run-manual` fixes none" already tell the story above, `ch10-12-run-manual`'s page having fixed no Portuguese phrase when this one was defined.
* **Terms:** delivery, record, slot, as docs/03 has them; no new term, no docs/03 row.
* **Sources:** m23-review's candidates R5, R6, R7, R8, R10 (`work/done/m23-review.md`); docs/06 at `7e7fcae` for the committed lines; docs/05 at `7e7fcae`, lines 250 to 254, unchanged since `3cc90a8`; the commit order `7a0c04f` (define `ch13-apply-run-manual`) before `2911ef6` (apply `ch10-12-run-manual`) for R7.
* **Cases, code examples:** none. No chapter changes.

**States.** Inapplicable: record pages, no screen.

**Visual reference.** Inapplicable: no screen, no chapter.

**Out of scope.**

* The step 4 report, its Decisions on the Environments pointer and the changelog credit on `kit-2026-10-19-2`'s page: `kit-record-step4`, which edits the same page first.
* Done when, Proof and Delivery review of the M23 pages: `m23-records-proof`, which edits three of these pages first.
* The slug `ch10-12-run-manual` against its chapters: kept with a recorded reason (m23-review P1, weak).
* `ch13-apply-run-manual`'s :18 and :56: true as they are (Contract).
* Any chapter, docs/03, docs/05, docs/06: the line fixes records only.

**Decisions from the documents.**

* The records are edited in place, with the change named on this page, not in them: the precedent of `m22-batch-proof` (`97ff7e2`) and the batch rule that a delivery naming a record may edit it.
* The fix of R6 goes in Divergences, not Behaviour: docs/05 §3 has the page record "what diverged" after /apply, and Behaviour is what was defined.
* No chapter is touched, so the book's Done when items (both editions, opens with its value, PDFs) are inapplicable (docs/05 §3 reads them for a chapter page).

**Decisions taken alone** (the batch's driver asked for recommended answers; correct them in the review).

* R7's account, `ch13-apply-run-manual`'s /propose picking the phrase and the driver passing it to `ch10-12-run-manual`'s /apply, is the driver's word relayed to this /propose, matching the commit order; only `ch10-12-run-manual`'s sentence is wrong, so only it changes.
* R8 is fixed by describing the later delivery, not naming it: docs/06's committed lines hold no `ch13-19-session-folder` at `7e7fcae`, the driver's uncommitted queue puts it under M26, not M25, and a description stays true wherever it lands.
* R10 changes only the number; "at HEAD" stays, being true when the page was written (docs/05 unchanged since `3cc90a8`).
* `ch13-apply-run-manual`'s :39 joins R5 as a sibling sentence of the same cause on a page this line names.
* The queue line's wording needs no change.

**Done when.**

* [x] The eight edits of the Contract are in the four pages, each found by its section and text after `kit-record-step4` and `m23-records-proof` have applied, and nothing else in those pages changed.
* [x] A search of the four pages finds no "12 and 13", "and 12," or "and chapter 12" naming `ch10-12-run-manual`'s or M23's chapters, no `ch13-19-session-folder`, no "lines 250 to 253", and one account of who picked the Portuguese phrase.
* [x] No em dash in the edited sentences.
* [x] `make verify` green after the last edit.
* [x] Delivery review by a read-only Opus agent this lane launched, over the diff against this page; its findings fixed or recorded (Delivery review). Whether it kept the session's advisor, as docs/05 §5 asks, is not recorded.
* [x] Page in `work/done/`, the commit suggested in a `commit` block; the line's `[x]` and the staging are the batch driver's steps. No chapter changes, so `make book` is the driver's, once for the batch.

**Built.** The eight replacements, word for word, each found by its section and quoted text after `kit-record-step4` (`9bd46a2`) and `m23-records-proof` (`8eb5748`); the line numbers at `7e7fcae` still held. `git diff HEAD` of the four pages shows 8 lines out and 8 in, two per page, nothing else.

**Checked.** docs/05's Manuals item opens on line 250 and its first sentence ends on 254. `ch10-12-run-manual`'s Built says "chapters 11 and 12 untouched". Chapter 9, both editions, names the `docs/manuals/` folder and no file. `ch08-update-2026-10-19-2` :69 says only that chapter 8 took chapter 7's words, so the phrase keeps one account. The page's search finds nothing in the four pages.

**Divergences.** None.

**Decisions taken alone in /apply.** None beyond the page's.

**Delivery review.** A read-only Opus agent, launched by this lane, read `git diff HEAD` of the four pages against this page, docs/04 and AGENTS.md, and checked the facts the edits state. No finding. Its one optional wording note, on `ch10-12-run-manual`'s Divergences writing the short Portuguese file name, needs no change: that page uses the short form already at :68.

**Proof.** `make verify` exited 0 after the eight replacements (build, parity, em dash, prose, width, examples, links, disclosure), and again after this page's last edit and its move.

```commit
docs(m23-records-crossrefs): four M23 records agree on chapters

- kit-2026-10-19-2, ch08, ch13 pages: M23 taught chapters 7, 8, 9, 10
  and 13; ch10-12-run-manual never owned chapter 12
- ch08 page: docs/05's Manuals sentence is lines 250 to 254
- ch10-12 page: the phrase came from ch13-apply-run-manual's /propose;
  Divergences names chapter 9's missing file
- ch13 page: the later worktree delivery is described, not named

work/done/m23-records-crossrefs.md
```
