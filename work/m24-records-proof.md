# m24-records-proof

**Objective.** The author can read on the pages of M24's `kit-2026-10-20`, `ch08-update-2026-10-20` and `ch12-14-17-20-branch-claim` and of M23's fix round a Done when that ticks only what the page records: which `make book` run built their chapters, where its PDF paths are and what that build holds of them, which delivery review ran, what it read and that its advisor is not recorded, and what `manual-link-pointers`' grep printed.

**Behaviour.**

* Reading the `make book` item and the Proof of `kit-2026-10-20`, `ch08-update-2026-10-20` or `ch12-14-17-20-branch-claim`, the author finds who ran it, the batch's driver, after `ch12-14-17-20-branch-claim`, at `2b66f27`, exit 0, and the record that gives both PDF paths, `work/done/m24-review.md`, whose build at `2fccad2` has the same `book/` (m24-review P2).
* Reading the `make book` item and the Proof of `ch08-next-free-line`, `ch14-board-visibility`, `ch17-23-git-slot-word`, `ch13-23-merge-default`, `ch17-next-free-line`, `ch07-09-manual-wording`, `ch09-slow-tests` or `manual-pypdf-install`, the author finds the driver's run after the last M23 fix lane, at `16fdca6`, exit 0, which holds the round's chapters as it left them, and `work/done/m24-review.md`'s build at `2fccad2` with both PDF paths: the same chapters for 7, 9, 13 and 23, and for 8, 14, 17, 18 and 19 the text after M24 changed them, said on the page (S1).
* Fails if: an item or Proof says a person read a PDF or was given its paths, says /apply ran a build it did not, or points to `2fccad2` as holding a chapter M24 changed since (m24-review :127: the author read nothing in that run).
* Reading the Delivery review item of any page below, the author finds what ran, a read-only Opus agent launched by the lane, what it read, and that whether it kept the session's advisor docs/05 §5 asks is not recorded; where it read the chapter files or the hunks only, that this is narrower than docs/05 §5, which also has it read the page (P7, S2). Each Delivery review paragraph says the agent was launched by the lane; none says it kept the advisor.
* Reading `work/done/manual-link-pointers.md`'s Done when, the author finds the grep ticked with what it printed, the build manual's :42-44 and no cross-reference between manuals, and its Divergence speaking of the item as defined (S8).
* Edges: no item is unticked; each ticked item states only what ran and where it is recorded. No Behaviour, Contract, Objective or commit block of the eighteen pages changes, nor any sentence `m24-records-crossrefs` edits. M25's in-flight `work/kit-2026-10-20-1.md` is not touched.

**Contract.** The records the pages point to, checked at define time (HEAD `f63276d`; the eighteen pages unchanged since `1c96493`):

* `work/done/m24-review.md`, Mechanical checks (:122): at the end commit `2fccad2`, `git status --short book/` empty, then `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* `git diff --stat 2b66f27 2fccad2 -- book/` is empty; chapter 8 is unchanged from `f969c48` to `2b66f27`.
* `git log 16fdca6..2fccad2 -- book/` lists `f969c48` and `2b66f27` only; `git diff --name-only 16fdca6 2fccad2 -- book/` lists chapters 8, 12, 14, 17, 18, 19 and 20, both editions; chapters 7, 9, 13 and 23 are the same.
* From each fix-round chapter commit to `16fdca6`, its chapter files are unchanged (`c42e106` ch 8, `f8ec9c7` ch 14, `4c52280` ch 17, `db68417` ch 9), or changed only by later fix-round lanes: `0b6105a`'s by `4c52280` and `16fdca6`, `7660dfc`'s pt 9 by `db68417`.
* The driver's runs at `16fdca6` and `2b66f27` and how each lane's review ran: no page records them; the driver's word relayed to this /propose (Decisions taken alone) is the source, and this page records it.

Exact replacements, each found by its page and quoted text, which occurs once on its page (line numbers are today's and only a guide); the rest of each page untouched. "Opening" means the quoted words gain ", launched by this lane," before the verb or "over", nothing else in that paragraph changing.

`work/done/kit-2026-10-20.md`

1. Done when :64, "`make book` builds both editions (run by the batch's driver, once per batch)." becomes "`make book` built both editions: the batch's driver ran it after ch12-14-17-20-branch-claim, at `2b66f27` (exit 0), and `work/done/m24-review.md` records the build at `2fccad2`, whose `book/` is the same, with both PDF paths."
2. Done when :65, "Delivery review as docs/05 §5 says; only this delivery's paths" becomes "Delivery review by a read-only Opus agent this lane launched (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded; only this delivery's paths".
3. Delivery review :113, "A read-only agent on Opus, with the advisor, read" becomes "A read-only agent on Opus, launched by this lane, read".
4. Proof :120, "`make book` is run by the batch's driver." becomes "The batch's driver ran `make book` at `2b66f27` (exit 0); `work/done/m24-review.md` records the build at `2fccad2`, the same `book/`, with both PDF paths."

`work/done/ch08-update-2026-10-20.md`

5. Done when :94, "`make book` is run once for the batch by its driver, who reads the excerpt in both PDFs, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`." becomes "`make book` built both editions: the batch's driver ran it after ch12-14-17-20-branch-claim, at `2b66f27` (exit 0), and `work/done/m24-review.md` records the build at `2fccad2`, whose `book/` is the same and holds chapter 8 as this delivery left it, with both PDF paths."
6. Done when :95, "Delivery review as docs/05 §5 says. No private case" becomes "Delivery review by a read-only Opus agent this lane launched, over what the Delivery review below names; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded. No private case".
7. Delivery review :111, opening of "A read-only Explore agent on Opus read".
8. Proof :118, "after the last covered edit, the page's move included." becomes "after the last covered edit, the page's move included. The batch's driver ran `make book` at `2b66f27` (exit 0); `work/done/m24-review.md` records the build at `2fccad2`, the same `book/`, with both PDF paths."

`work/done/ch12-14-17-20-branch-claim.md`

9. Done when :94, "`make book`, with both PDF paths given to the person: run by the batch's driver, once per batch." becomes "`make book` built both editions: the batch's driver ran it after this lane, at `2b66f27`, this delivery's commit (exit 0), and `work/done/m24-review.md` records the build at `2fccad2`, the same `book/`, with both PDF paths."
10. Delivery review :110, "A read-only general-purpose agent on Opus read `git diff HEAD` of the twelve chapters against this page, docs/03, docs/04 and the kit source." becomes "A read-only general-purpose agent on Opus, launched by this lane, read `git diff HEAD` of the twelve chapters against this page, docs/03, docs/04 and the kit source; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
11. Proof :119, "`make book` is run by the driver once per batch." becomes "The batch's driver ran `make book` at `2b66f27`, this delivery's commit (exit 0); `work/done/m24-review.md` records the build at `2fccad2`, the same `book/`, with both PDF paths."

`work/done/ch08-next-free-line.md`

12. Done when :53, "`make book` run, both PDF paths given, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, with the excerpt's last line read in each." becomes "`make book` built both PDFs: the batch's driver ran it after the last M23 fix lane, at `16fdca6` (exit 0), whose chapter 8 is as this delivery left it, and `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths, after M24 changed chapter 8 (Proof)."
13. Done when :54, "The Delivery review as docs/05 §5 says." becomes "Delivery review by one read-only Opus agent this lane launched, over both chapter files (Delivery review): narrower than docs/05 §5, which also has it read this page, and keep the session's advisor, which this page does not record."
14. Divergences :56, "who runs it once for the batch and gives the author both PDF paths, `output/` English and Portuguese; the Done when item on it is ticked on that word." becomes "who ran it after the last M23 fix lane, at `16fdca6`; the Done when item on it names that run and the build `work/done/m24-review.md` records."
15. Proof :58, "`make verify` green after the last edit: build, parity, em dash, prose, width, examples, links and disclosure." gains after it " The batch's driver ran `make book` at `16fdca6` (exit 0), whose chapter 8 is as this delivery left it; `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths, after M24 changed chapter 8."
16. Delivery review :60, opening of "One read-only Opus agent read".

`work/done/ch14-board-visibility.md`

17. Done when :57, "and `make book` built both PDFs, its run and both PDF paths recorded in this page's Proof by /apply." becomes "and `make book` built both PDFs: the batch's driver ran it after the last M23 fix lane, at `16fdca6` (exit 0), whose chapter 14 is as this delivery left it, and `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths, after M24 changed chapter 14 (Proof)."
18. Done when :58, "The Delivery review as docs/05 §5 says, recorded on this page." becomes "Delivery review by one read-only Opus agent this lane launched, over both chapter files and this page (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
19. Divergences :60, the same quoted text and replacement as item 14.
20. Proof :62, the same quoted text as item 15, gaining " The batch's driver ran `make book` at `16fdca6` (exit 0), whose chapter 14 is as this delivery left it; `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths, after M24 changed chapter 14."
21. Delivery review :64, opening of "One read-only Opus agent read".

`work/done/ch17-23-git-slot-word.md`

22. Done when :74, "`make book` built both PDFs, its run and both PDF paths recorded in this page's Proof; when a batch's driver runs it instead, this item is ticked only on that run as the Proof records it." becomes "`make book` built both PDFs: the batch's driver ran it after the last M23 fix lane, at `16fdca6` (exit 0), whose chapters 17, 18, 19 and 23 are as M23's fix round left them, and `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths, after M24 changed chapters 17, 18 and 19 (Proof)."
23. Done when :75, "The Delivery review as docs/05 §5 says, recorded on this page with who read what." becomes "Delivery review by one read-only Opus agent this lane launched, over this delivery's paths (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
24. Proof :82, "`make book` is run by the driver once for the batch." becomes "The batch's driver ran `make book` after the last M23 fix lane, at `16fdca6` (exit 0); `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths, after M24 changed chapters 17, 18 and 19."
25. Delivery review :92, opening of "One read-only Opus agent over this delivery's paths".

`work/done/ch13-23-merge-default.md`

26. Done when :73, the same quoted text as item 22, becomes "`make book` built both PDFs: the batch's driver ran it after this lane, at `16fdca6`, this delivery's commit (exit 0), and `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths, after M24 changed chapters 18 and 19 (Proof)."
27. Done when :74, the same quoted text and replacement as item 23.
28. Proof :80, "`make book` is run by the driver once for the batch." becomes "The batch's driver ran `make book` at `16fdca6`, this delivery's commit (exit 0); `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths, after M24 changed chapters 18 and 19."
29. Delivery review :84, opening of "One read-only Opus agent over this delivery's paths".

`work/done/ch17-next-free-line.md`

30. Done when :62, the same quoted text as item 22, becomes "`make book` built both PDFs: the batch's driver ran it after the last M23 fix lane, at `16fdca6` (exit 0), whose chapter 17 is as this delivery left it, and `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths, after M24 changed chapter 17 (Proof)."
31. Done when :63, the same quoted text as item 23, becomes "Delivery review by one read-only Opus agent this lane launched, over chapter 17 and this page (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
32. Proof :70, "`make book` is run by the driver once for the batch." becomes "The batch's driver ran `make book` after the last M23 fix lane, at `16fdca6` (exit 0), whose chapter 17 is as this delivery left it; `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths, after M24 changed chapter 17."
33. Delivery review :78, opening of "One read-only Opus agent over this delivery's paths".

`work/done/ch07-09-manual-wording.md`

34. Done when :56, "`make book` built both PDFs, their paths given to the author (`make book` run by the batch driver)." becomes "`make book` built both PDFs: the batch's driver ran it after the last M23 fix lane, at `16fdca6` (exit 0), and `work/done/m24-review.md` records the build at `2fccad2`, whose chapters 7 and 9 are the same, with both PDF paths."
35. Done when :57, "Delivery review as docs/05 §5 says." becomes "Delivery review by one read-only Opus agent this lane launched, over the three chapter files (Delivery review): narrower than docs/05 §5, which also has it read this page, and keep the session's advisor, which this page does not record."
36. Proof :73, "`make book` run by the batch driver." becomes "`make book` run by the batch's driver at `16fdca6` (exit 0), and `work/done/m24-review.md` records the build at `2fccad2`, the same chapters 7 and 9, with both PDF paths."
37. Delivery review :75, opening of "a read-only Opus agent over the three chapter files".

`work/done/ch09-slow-tests.md`

38. Done when :37, the same quoted text as item 34, becomes "`make book` built both PDFs: the batch's driver ran it after the last M23 fix lane, at `16fdca6` (exit 0), and `work/done/m24-review.md` records the build at `2fccad2`, whose chapter 9 is the same, with both PDF paths."
39. Proof :53, "`make book` run by the batch driver." becomes "`make book` run by the batch's driver at `16fdca6` (exit 0), and `work/done/m24-review.md` records the build at `2fccad2`, the same chapter 9, with both PDF paths."
40. Delivery review :55, "a read-only Opus agent over the two chapter files against this page and docs/04: no findings." becomes "a read-only Opus agent, launched by this lane, over the two chapter files against this page and docs/04, narrower than docs/05 §5, which also has it read this page; whether it kept the session's advisor is not recorded. No findings."

`work/done/manual-pypdf-install.md`

41. Done when :44, "`make book` prints both PDF paths, recorded (run by the driver once for the batch)." becomes "`make book` built both PDFs: the batch's driver ran it after the last M23 fix lane, at `16fdca6` (exit 0), and `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths."
42. Done when :46, "The Delivery review as docs/05 §5 says." becomes "Delivery review by one read-only Opus agent this lane launched, over the manual and this page (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
43. Proof :76, "`make book` is run by the driver once for the batch." becomes "The batch's driver ran `make book` after the last M23 fix lane, at `16fdca6` (exit 0); `work/done/m24-review.md` records the build at `2fccad2`, with both PDF paths."
44. Delivery review :86, opening of "One read-only Opus agent over this delivery's paths".

`work/done/manual-pip-floor.md`

45. Done when :43, the same quoted text and replacement as item 42.
46. Delivery review :88, opening of "One read-only Opus agent over this delivery's paths".

`work/done/docs05-author-word.md`

47. Done when :54, "Delivery review as docs/05 §5 says;" becomes "Delivery review by one read-only Opus agent this lane launched, over the two files' hunks (Delivery review): narrower than docs/05 §5, which also has it read this page, and keep the session's advisor, which this page does not record;".
48. Delivery review :76, opening of "a read-only Opus agent over the two files' hunks".

`work/done/kit-record-step4.md`

49. Done when :84, "Delivery review as docs/05 §5 says: one read-only agent on Opus with the session's advisor reads `git diff HEAD` of the record and this page against this page and docs/04." becomes "Delivery review by one read-only Opus agent this lane launched, over `git diff HEAD` of the record and this page against this page and docs/04 (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
50. Delivery review :91, opening of "One read-only Opus agent read".

`work/done/m22-records-commits.md`

51. Done when :89, "Delivery review as docs/05 §5 says: a read-only Opus agent with the session's advisor reads the diff of the three pages and this page against this page, docs/04 and the three commits; its findings fixed or recorded." becomes "Delivery review by a read-only Opus agent this lane launched, over the diff of the three pages and this page against this page, docs/04 and the three commits; its findings fixed or recorded (Delivery review). Whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."

`work/done/m23-records-crossrefs.md`

52. Done when :68, "Delivery review as docs/05 §5 says: a read-only Opus agent with the advisor reads the diff against this page; its findings fixed or recorded (Delivery review). Whether it kept the advisor is not recorded." becomes "Delivery review by a read-only Opus agent this lane launched, over the diff against this page; its findings fixed or recorded (Delivery review). Whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."

`work/done/manual-link-pointers.md`

53. Done when :59, "`grep -n "docs/manuals/" docs/manuals/*.md` prints nothing (prints only the three quoted messages at :42-44; see Divergences)." becomes "`grep -n "docs/manuals/" docs/manuals/*.md` prints only the build manual's :42-44, the three quoted messages, and no cross-reference between manuals (Proof; Divergences)."
54. Done when :62, "The Delivery review as docs/05 §5 says." becomes "Delivery review by one read-only Opus agent this lane launched, over the seven files and this page (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
55. Divergences :124, "Done when says `grep -n "docs/manuals/" docs/manuals/*.md` prints nothing, but" becomes "Done when, as defined, said `grep -n "docs/manuals/" docs/manuals/*.md` prints nothing, but".
56. Delivery review :132, opening of "One read-only Opus agent over this delivery's paths".

* **Terms:** delivery, record, Delivery review, as docs/03 has them; no new term, no docs/03 row.
* **Sources:** m24-review's candidates P2, P7, S1, S2, S8 (`work/done/m24-review.md`, Candidates table, :146 to :161), its Mechanical checks :122 and clause note :127; docs/05 §5's Delivery review slot (:239 to :246); the driver's word on the batch (Decisions taken alone); the form of `work/done/m23-records-proof.md`.
* **Cases, code examples:** none. No chapter changes.
* **Neighbouring line:** `m24-records-crossrefs`, after this one in queue order, edits `kit-2026-10-20` (:3, :40), `ch08-update-2026-10-20` (:59, :67), `ch12-14-17-20-branch-claim` (:38, :43, :61, :65, :68), `ch13-23-merge-default` (:36), `ch17-23-git-slot-word` (:37), `ch08-next-free-line` (:10, :23, :24, :58) and `kit-record-step4` (:7, :64, :73), by quoted text. Only `ch08-next-free-line` :58 is touched by both: item 15 appends after that Proof's last sentence, a clause S7 does not cite.

**States.** Inapplicable: record pages, no screen.

**Visual reference.** Inapplicable: no screen, no chapter.

**Out of scope.**

* `work/kit-2026-10-20-1.md` :64 (P2's fourth cite): M25's page in flight, which m24-review handed to the driver for that page's own /apply (`work/done/m24-review.md` :103).
* `kit-2026-10-20` :65's staging part: weak in P2, its Divergences record it.
* `kit-2026-10-20` :34, "the kit's readers on Opus with the advisor": a project choice the kit keeps, not a claim about a review.
* `manual-link-pointers` :61 and :120, `manual-pip-floor` :78, `kit-record-step4` :87, `docs05-author-word` :54's `make book` clause and the records pages' "`make book` is the driver's, once for the batch": deliveries that changed no chapter, true as written, and S1 cites none of them.
* `manual-pypdf-install` :86's note that the item was ticked before the driver's run: history, true.
* The Delivery review paragraphs' content beyond the opening: each says what its agent read; the gap is stated on the Done when items, or on the paragraph where the page has no item (`ch12-14-17-20-branch-claim`, `ch09-slow-tests`).
* `work/done/m23-records-proof.md`: its review item already says the advisor is not recorded.
* A new `make verify`, `make book` or delivery review run for these deliveries: the builds named hold their chapters.
* Any sentence `m24-records-crossrefs` edits; any chapter, docs/03, docs/05, docs/06.

**Decisions from the documents.**

* Items stay ticked and are reworded to what ran, records edited in place, the change named here and not in them: the precedent of `m23-records-proof` and `m22-batch-proof`, and the batch rule that a delivery naming a record may edit it.
* No chapter is touched, so the book's Done when items (both editions, opens with its value, PDFs) are inapplicable (docs/05 §3).
* "The person read" and "paths given to the author" leave every item: m24-review :127 records that the author read nothing in that run.

**Decisions taken alone** (the batch's driver asked for recommended answers; correct them in the review).

* The driver's word relayed to this /propose is the source of facts no page held: it ran `make book` after M23's last fix, `16fdca6` (ch13-23-merge-default's commit), and after `2b66f27`, both exit 0; each lane's review was one read-only Opus agent the lane launched; whether it kept the session's advisor is recorded nowhere.
* The queue line's "pointing to m24-review's at `2fccad2`" holds for M24's three pages and for chapters 7, 9, 13 and 23; for chapters 8, 14, 17, 18 and 19 `2fccad2` holds M24's later text (Contract's git checks), so those pages name the driver's run at `16fdca6` first and m24-review's build for the PDF paths, saying M24 changed the chapter since.
* "With the advisor" leaves `kit-2026-10-20` :113, `kit-record-step4` :84, `m22-records-commits` :89 and `m23-records-crossrefs` :68, though those lanes wrote it: the driver says nothing records it, and `m23-records-crossrefs` :68 itself says so. If the author holds the lanes' words as the record, those four keep them and say "as the paragraph records".
* S2's "the other fix-round pages' review items" is read as every fix-round page ticking "Delivery review as docs/05 §5 says": `ch08-next-free-line`, `ch14-board-visibility`, `ch17-23-git-slot-word`, `ch13-23-merge-default`, `ch17-next-free-line`, `manual-link-pointers`, `manual-pypdf-install` and `manual-pip-floor`, the last cited by no row.
* "Narrower than docs/05 §5" only where the paragraph says the agent read the chapter files or hunks and not the page (`ch08-next-free-line`, `ch07-09-manual-wording`, `ch09-slow-tests`, `docs05-author-word`); `ch12-14-17-20-branch-claim` reads "against this page" and keeps no such clause.
* `ch12-14-17-20-branch-claim` and `ch09-slow-tests` have no Delivery review item, so the advisor sentence goes on their paragraph.
* Siblings included, going stale with the cited items: the Proof sentences of every page whose item changes, the Divergences of `ch08-next-free-line` and `ch14-board-visibility` ("ticked on that word"), and `manual-link-pointers` :124.
* The queue line's wording: "the Delivery review with the advisor and what it read" becomes "the Delivery review as it ran, its advisor not recorded, and what it read", proposed to the driver, who owns docs/06.

**Done when.**

* [ ] The 56 replacements above made word for word, each quoted text found exactly once on its page, and nothing else in the eighteen pages changed (`git diff` of each shows only those lines).
* [ ] The Contract's git checks rechecked at /apply: `2b66f27` to `2fccad2` empty on `book/`, `16fdca6` to `2fccad2` only chapters 8, 12, 14, 17, 18, 19 and 20.
* [ ] A search of the eighteen pages finds no ticked "Delivery review as docs/05 §5 says", no "with the advisor" or "with the session's advisor" on a review, no "paths given to the author", "who reads the excerpt", "last line read in each" or "ticked on that word", and "once for the batch" only in the Out of scope places.
* [ ] No em dash; no private case, so OD-3 approval is inapplicable.
* [ ] `make verify` green after the last edit.
* [ ] Delivery review by a read-only Opus agent this lane launched, over the diff of the eighteen pages and this page, against this page and docs/04; its findings recorded (Delivery review), and whether it kept the session's advisor recorded as it was.
* [ ] Page in `work/done/`, the commit suggested in a `commit` block; the line's `[x]` and the staging are the batch driver's steps. No chapter changes, so `make book` is not this delivery's.
