# m23-records-proof

**Objective.** The author can read on the pages of `ch08-update-2026-10-19-2`, `ch10-12-run-manual`, `ch13-apply-run-manual`, `readme-run-manual`, `ch20-merge-and-marks` and `docs05-dependency-merged` a Done when that ticks only what the page records: which `make book` run built their chapters and where its PDF paths are, which delivery review ran and how it falls short of docs/05 §5, and who marked the line `[x]` and staged it.

**Behaviour.**

* Reading the `make book` item of `work/done/ch08-update-2026-10-19-2.md`, `ch10-12-run-manual.md` or `ch13-apply-run-manual.md`, the author finds who ran it, the batch's driver, after the last M23 build lane at `31f510e`, exit 0, and the record that gives both PDF paths, `work/done/m23-review.md`, whose build at `8a87b0c` has the same `book/`; each page's Proof says the same (m23-review R3, L8).
* Reading `work/done/ch20-merge-and-marks.md`, the author finds the `make book` item, the Proof and the Divergence pointing to the build `work/done/m23-review.md` records at `8a87b0c`, which holds chapter 20 as this delivery left it, and no claim that the author read those PDFs (R3, S6).
* Reading the Delivery review item of `ch08-update-2026-10-19-2` or `ch13-apply-run-manual`, the author finds what ran, a read-only Opus agent launched by the lane, what it read, and that the page does not record the session's advisor docs/05 §5 has it keep; for `ch13-apply-run-manual`, that it read the two chapter files only (R9).
* Reading the Delivery review paragraphs of the four M23 pages, the author finds the agent launched by the lane (the driver's word, below).
* Reading `docs05-dependency-merged`'s Done when, the author finds its review done by the session's advisor, not by docs/05 §5's agent, as its Divergences already say; that page and `ch20-merge-and-marks` say no second review is recorded, instead of "the driver may run it again" (S2).
* Reading the staging items of `readme-run-manual`, `ch10-12-run-manual` and `ch13-apply-run-manual`, the author finds the `[x]` and the staging done by the batch's driver from a temporary index at commit time; on `ch20-merge-and-marks` and `docs05-dependency-merged`, by the driver from its own index, as their Divergences say (R4).
* Edges: no item is unticked; each ticked item states only what ran and where it is recorded. Nothing claims a session ran what it did not, nor that any agent kept the advisor. No Behaviour, Contract, Objective or commit block of the six pages changes, nor any sentence `m23-records-crossrefs` or `m22-records-commits` edits.

**Contract.** The records the pages point to, checked at define time:

* `work/done/m23-review.md`, Mechanical checks: at the end commit `8a87b0c`, `git status --short book/` empty, then `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* `git diff --stat 31f510e 8a87b0c -- book/` is empty. Chapter 8 last changed at `29670c7`, chapters 7, 9 and 10 at `2911ef6`, chapter 13 at `31f510e`: `git diff --stat` from each to `31f510e` on its chapter files is empty. Chapter 20 last changed at `9c2e490`; `git diff 9c2e490 8a87b0c` on both chapter 20 files is empty.
* The driver's build at `31f510e`: no page records it; the driver's word relayed to this /propose (Decisions taken alone) is the source, and this page records it.

Exact replacements, each found by its section and quoted text (line numbers are today's, at `61d00b2`, and only a guide); the rest of each page untouched:

1. `work/done/ch08-update-2026-10-19-2.md`, Done when, :59, the item starting "`make verify` green after the last covered edit; `make book` builds both editions", to:

   > * [x] `make verify` green after the last covered edit; `make book` built both editions: the batch's driver ran it after the last M23 build lane, at `31f510e` (exit 0), and `work/done/m23-review.md` records the build at `8a87b0c`, whose `book/` is the same and holds this chapter as this delivery left it, with both PDF paths.

2. Same page, Done when, :60, "Delivery review as docs/05 §5 says; no private case, so OD-3 approval is inapplicable.", to:

   > * [x] Delivery review by a read-only Opus agent this lane launched, over what the Delivery review below names; this page does not record that it kept the session's advisor, as docs/05 §5 asks. No private case, so OD-3 approval is inapplicable.

3. Same page, Delivery review, :72: "A read-only Explore agent on Opus read" becomes "A read-only Explore agent on Opus, launched by this lane, read". Nothing else in the paragraph changes.

4. Same page, Proof, :79: its last sentence, "`make book` is the driver's, run once for the batch.", becomes:

   > The batch's driver ran `make book` at `31f510e` (exit 0); `work/done/m23-review.md` records the build at `8a87b0c`, the same `book/`, with both PDF paths.

5. `work/done/ch10-12-run-manual.md`, Done when, :55, "`make verify` green; `make book` is run once for the batch by its driver, who gives the author both PDF paths.", to:

   > * [x] `make verify` green; `make book` built both editions: the batch's driver ran it after the last M23 build lane, at `31f510e` (exit 0), and `work/done/m23-review.md` records the build at `8a87b0c`, whose `book/` is the same and holds chapters 7, 9 and 10 as this delivery left them, with both PDF paths.

6. Same page, Done when, :56, to:

   > * [x] Page in `work/done/`, the commit suggested in a `commit` block; the line's `[x]` and the staging by paths and hunk were the batch driver's, from a temporary index at commit time.

7. Same page, Proof, :87: its last clause, "; `make book` is run by the batch's driver.", becomes:

   > ; the batch's driver ran `make book` at `31f510e` (exit 0), and `work/done/m23-review.md` records the build at `8a87b0c`, the same `book/`, with both PDF paths.

8. Same page, Delivery review, :89: "A read-only agent on Opus read" becomes "A read-only agent on Opus, launched by this lane, read". Nothing else in the paragraph changes.

9. `work/done/ch13-apply-run-manual.md`, Done when, :69, "Delivery review as docs/05 §5 says.", to:

   > * [x] Delivery review by one read-only Opus agent this lane launched, over the two chapter files (Delivery review): narrower than docs/05 §5, which also has it read this page, against the page and docs/04, and keep the session's advisor, which this page does not record.

10. Same page, Done when, :70, to:

    > * [x] `make verify` green after the last edit; `make book` built both editions: the batch's driver ran it after this lane, at `31f510e`, this delivery's commit (exit 0), and `work/done/m23-review.md` records the build at `8a87b0c`, the same `book/`, with both PDF paths.

11. Same page, Done when, :71, to:

    > * [x] Only this delivery's paths and its hunk of docs/06 staged, by the batch's driver from a temporary index at commit time; the page moved to `work/done/` and its commit message suggested.

12. Same page, Delivery review, :79: "One read-only Opus agent over the two chapter files." becomes "One read-only Opus agent, launched by this lane, over the two chapter files." Nothing else in the paragraph changes.

13. `work/done/readme-run-manual.md`, Done when, :84, to:

    > * [x] `make verify` green; page in `work/done/`, the commit suggested in a `commit` block; the line's `[x]` and the staging by its paths and its hunk of docs/06 were the batch driver's, from a temporary index at commit time.

14. Same page, Delivery review, :115: "A read-only agent on Opus read" becomes "A read-only agent on Opus, launched by this lane, read". Nothing else in the paragraph changes.

15. `work/done/ch20-merge-and-marks.md`, Done when, :47, to:

    > * [x] `make book` built both editions: `work/done/m23-review.md` records the build at `8a87b0c`, whose chapter 20 is as this delivery left it, with both PDF paths (`output/one-page-at-a-time.pdf`, `output/uma-pagina-de-cada-vez.pdf`).

16. Same page, Done when, :48, to:

    > * [x] Only this delivery's files staged, by the batch's driver from its own index (Divergences), with the suggested commit message; no commit by this lane.

17. Same page, Proof, :71, the bullet "`make book` is run once by the driver for the batch, so this lane reports no PDF paths; staging and the commit are the driver's in this batch.", to:

    > * This lane did not run `make book`; `work/done/m23-review.md` records the build at `8a87b0c`, which holds chapter 20 as this delivery left it, with both PDF paths. Staging and the commit are the driver's in this batch.

18. Same page, Divergences, :75, to:

    > * Done when's `make book` and staging items are not this lane's: the build is the one `work/done/m23-review.md` records, and the driver commits each delivery from its own index.

19. Same page, Divergences, :76: its last clause, "; the driver may run it again as docs/05 §5 says.", becomes "; no review by a read-only agent, as docs/05 §5 says, is recorded for it."

20. Same page, Decisions taken alone in /apply, :83, to:

    > * `make book` and staging are left to the driver, as the batch's rule says; their Done when items name the build `work/done/m23-review.md` records and the driver's index.

21. `work/done/docs05-dependency-merged.md`, Done when, :57, to:

    > * [x] Delivery review by the session's advisor, not by the read-only Opus agent docs/05 §5 asks (Divergences); only this delivery's paths and its hunk of docs/06 staged, by the batch's driver from its own index; the page moved to `work/done/` and its commit message suggested.

22. Same page, Divergences, :69: its last clause, "; the driver may run it again as docs/05 §5 says.", becomes "; no review by a read-only agent, as docs/05 §5 says, is recorded for it."

* **Terms:** delivery, record, Delivery review, as docs/03 has them; no new term, no docs/03 row.
* **Sources:** m23-review's candidates R3, R4, R9, S2, S6 and lead L8 (`work/done/m23-review.md`, Findings table); docs/05 §5's Delivery review slot; the driver's word on the batch (Decisions taken alone).
* **Cases, code examples:** none. No chapter changes.

**States.** Inapplicable: record pages, no screen.

**Visual reference.** Inapplicable: no screen, no chapter.

**Out of scope.**

* `work/done/m23-review.md`, whose L8 calls its own build at `8a87b0c` the batch's one run: a lead's wording, which the pages now complete with the driver's earlier build, and no candidate names it.
* `ch08-update-2026-10-19-2` :34, :39; `ch10-12-run-manual` :76 and :85 (Divergences); `ch13-apply-run-manual` :39, :41: `m23-records-crossrefs`, which edits the same pages after this line, by quoted text.
* `ch20-merge-and-marks` :67, the Proof's first bullet, and the commit sentences: `m22-records-commits`, `[~]` in another session, which edits the same page after this line.
* `readme-run-manual` :109 and :113 on `make book`: true as written, the delivery changes no chapter, and R3 does not cite them.
* The Delivery review paragraphs' content, beyond "launched by this lane": each says what its agent or the advisor read; the gap is stated on the Done when items.
* A new `make verify`, `make book` or delivery review run for the six deliveries: the build recorded holds their chapters.
* Any chapter, docs/03, docs/05, docs/06: the line fixes records only.

**Decisions from the documents.**

* The pages point to `work/done/m23-review.md` for the PDF paths: the one committed record of a build holding all six deliveries' chapters (Contract's git checks); `work/done/m22-review.md`'s build at `abb988a` predates `9c2e490`, so not for chapter 20.
* Items stay ticked and are reworded to what ran, rather than unticked: the precedent of `m22-batch-proof` (`97ff7e2`), Decisions taken alone.
* Records edited in place, the change named here, not in them: `m22-batch-proof` and the batch rule that a delivery naming a record may edit it.
* No chapter is touched, so the book's Done when items (both editions, opens with its value, PDFs) are inapplicable (docs/05 §3).

**Decisions taken alone** (the batch's driver asked for recommended answers; correct them in the review).

* The driver's word relayed to this /propose is the source of three facts no page held: in M23's batch the driver ran `make book` once after the last build lane (both PDFs at `31f510e`, exit 0) and again inside m23-review; each delivery's review was a read-only Opus agent launched by its lane; the staging and the `[x]` were the driver's, from a temporary index at commit time. They go on the four M23 pages only; the two M22 pages keep what their Divergences record ("its own index", the advisor).
* No page claims the advisor: nothing records whether the M23 agents kept it, so the items say the page does not record it.
* `ch10-12-run-manual` and `readme-run-manual` have no Delivery review item in Done when, so R9 needs no tick changed there; they only gain "launched by this lane". `ch20-merge-and-marks` has none either; its R9 part is the Divergence's "may run it again", reworded to what is recorded.
* `ch20-merge-and-marks` :47 drops "for the author's reading": m23-review says the author read no PDF in that run.
* Siblings included, the same deferral on the same pages: the Proof sentences (items 4, 7, 17), ch20's Divergence and Decision (items 18, 20), docs05's Divergence (item 22).
* The queue line's wording needs no change.

**Done when.**

* [x] The 22 replacements above made word for word, each found by its section and quoted text, and nothing else in the six pages changed (`git diff` of each shows only those lines).
* [x] The Contract's git checks rechecked at /apply: `git diff --stat 31f510e 8a87b0c -- book/` empty, chapter 20 unchanged from `9c2e490` to `8a87b0c`.
* [x] A search of the six pages finds no "run once for the batch", "the driver may run it again" or "for the author's reading", "is run by the batch's driver" only in `readme-run-manual`'s Proof (Out of scope), and no "Delivery review as docs/05 §5 says" ticked.
* [x] No em dash; no private case, so OD-3 approval is inapplicable.
* [x] `make verify` green after the last edit.
* [x] Delivery review by a read-only Opus agent this lane launched, over the diff of the six pages, against this page and docs/04; its findings recorded (Delivery review). This page does not record whether it kept the session's advisor, as docs/05 §5 asks it to.
* [x] Page in `work/done/`, the commit suggested in a `commit` block; the line's `[x]` and the staging are the batch driver's steps. No chapter changes, so `make book` is the driver's, once for the batch.

**Built.** The 22 replacements, word for word, matched by their quoted text; the line numbers at `61d00b2` still held. `git diff HEAD` of the six pages shows 22 lines out and 22 in (ch08 4, ch10-12 4, ch13 4, readme 2, ch20 6, docs05 2), nothing else; no item unticked.

**Checked.** At /apply, `git diff --stat 31f510e 8a87b0c -- book/` is empty, and so is chapter 20's diff from `9c2e490` to `8a87b0c`, chapter 8's from `29670c7` to `31f510e` and chapters 7, 9 and 10's from `2911ef6` to `31f510e`. The page's search finds "is run by the batch's driver" only at `readme-run-manual` :113, its Proof. No em dash in the six pages.

**Divergences.** None.

**Decisions taken alone in /apply.**

* The replacements were applied by one script that asserts each quoted text occurs exactly once on its page, so no edit could land on a second match.

**Delivery review.** A read-only Opus agent, launched by this lane, read `git diff HEAD` of the six pages against this page, docs/04 and docs/05 §5, reran the Contract's git checks and the search, and read `work/done/m23-review.md`'s Mechanical checks. No finding breaks the page, docs/04 or the text this delivery wrote. It noted that `readme-run-manual` :109 still says the driver runs `make book` once for the batch: kept by Out of scope, true for a delivery that changed no chapter, so no queue line. Its three wording notes (ch08 :60 and ch13 :69, ch20 :76 and docs05 :69, on how "as docs/05 §5 says" attaches) are on this page's quoted text, applied as written. Whether it kept the session's advisor is not recorded.

**Proof.** `make verify` exited 0 after the 22 replacements (build, parity, em dash, prose, width, examples, links, disclosure), and again after this page's last edit and its move.

```commit
docs(m23-records-proof): six pages tick only what their records hold

- ch08, ch10-12, ch13, readme pages: make book, review and staging items
  say what ran, the driver's build at 31f510e and m23-review's at 8a87b0c
- ch20, docs05 pages: build, review and staging items point to records
- Delivery review paragraphs say the agent was launched by the lane

work/done/m23-records-proof.md
```
