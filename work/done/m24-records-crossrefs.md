# m24-records-crossrefs

**Objective.** The author can read the record pages of M24 and of M23's fix round and find every cross-reference true: no slug or milestone that no committed queue line holds, the headings the chapters really have, the branch-claim line's six chapters, the right milestone and line cites, no chapter 8 edit credited to `ch07-09-manual-wording`, and the Environments pointer filed as a slot's shape, which step 4 checks.

**Behaviour.**

* Reading `work/done/ch12-14-17-20-branch-claim.md`, Contract, the author finds chapter 18's passage under "One delivery, one step to undo" and chapter 20's under "The pull request as the team's review", the headings those lines sit under in `book/en/18-git-essentials.md` and `book/en/20-team-tools.md` (m24-review P4).
* Reading the same page's Out of scope and Neighbouring lines, and `work/done/kit-2026-10-20.md`'s Out of scope, the author finds no slug or milestone number that `git show HEAD:docs/06-Queue.md` lacks; a later delivery is described by what it does, as `m23-records-crossrefs` did for R8 (P3).
* Reading `work/done/kit-2026-10-20.md` :3 and :40 and `work/done/ch08-update-2026-10-20.md` :59 and :67, the author finds the branch-claim line's chapters as its queue line has them: 12, 14, 17, 18, 19 and 20 (P5).
* Reading `work/done/ch13-23-merge-default.md` :36, the author finds `ch12-14-parallel-token` under M25, where docs/06 has it (S4), and with `ch17-23-git-slot-word.md` :37 no uncommitted slug and no `ch13-19-session-folder` placed in M25 (S10).
* Reading `work/done/ch08-next-free-line.md`, the author finds Step 5 cited at `kit-2026-10-19-2` :93, where it is (S6), and no sentence saying `ch07-09-manual-wording` edits chapter 8: that page's Contract :32 says "Chapter 8: no change" and commit `7660dfc` touches pt 07, en 07 and pt 09 only (S7).
* Reading `work/done/kit-2026-10-19-2.md`, the author finds the Environments pointer under a heading that does not say step 4 leaves it unchecked, and its item saying a slot's shape is what step 4 checks, though the report did not name this one; `work/done/kit-record-step4.md` says it filed the pointer wrongly and where it was corrected (S3).
* Edge: if, when /apply starts, `git show HEAD:docs/06-Queue.md` holds `ch13-19-session-folder` under M26, `ch12-14-18-several-slugs` under M27, `ch13-19-claim-script` under M28 and `ch14-after-over-token` under M29, the P3 and S10 parts shrink to the milestone fixes only (Contract, rule A).
* Fails: a replacement whose quoted text is not found; any other line of these pages changed; an em dash; a Done when item unticked; a chapter, docs/03, docs/05 or docs/06 touched.

**Contract.** Exact replacements in eight record pages, found by the quoted text, not by line number (line numbers are at `69d980b`); the rest of each page untouched. `m24-records-proof` edits Done when, Proof, Divergences and Delivery review of several of these pages before this line; no replacement below sits in those sections.

Rule A, checked first. At `69d980b`, HEAD's docs/06 holds M24 and M25 and no M26 to M29 heading; those lines are staged by the driver, uncommitted, so P3 and S10 hold in full. /apply runs `git show HEAD:docs/06-Queue.md`: if it holds all four lines named in the Edge above, under those milestones, replacements 3, 4, 5 and 8 are skipped, and 11 and 12 become only "M24's `ch12-14-parallel-token`" to "M25's `ch12-14-parallel-token`" (11) and "M25's `ch13-19-session-folder`" to "M26's `ch13-19-session-folder`" (11 and 12). Otherwise every replacement applies as written.

`work/done/ch12-14-17-20-branch-claim.md`

1. (P4, :38) `* Chapter 18, "Merges and the unit of work" (en and pt 25-33)` becomes `* Chapter 18, "One delivery, one step to undo" (en and pt 25-33)`.
2. (P4, :43) `* Chapter 20, "A pull request per delivery" (en and pt 22-26):` becomes `* Chapter 20, "The pull request as the team's review" (en and pt 22-26):`.
3. (P3, :61) "and `ch13-19-claim-script` (M28) touch chapter 13 next, the latter on the claim itself." becomes "and a later delivery of the queue's plan, on the kit's claim script, touch chapter 13 next, the latter on the claim itself."
4. (P3, :65) "* The claim script, its alias and Windows: `ch13-19-claim-script` (M28). Where each session opens: `ch13-19-session-folder` (M26)." becomes "* The claim script, its alias and Windows, and where each session opens: later deliveries of the queue's plan."
5. (P3, :68) "`ch12-14-parallel-token` (M25: chapters 12, 13, 14), `ch13-19-session-folder` (M26: chapter 19 "Worktrees in the kit", the sentence at :179 included), `ch12-14-18-several-slugs` (M27: 12, 13, 14, 18), `ch13-19-claim-script` (M28: 19), `ch14-after-over-token` (M29: 14)." becomes "`ch12-14-parallel-token` (M25: chapters 12, 13, 14), and later deliveries of the queue's plan: where each session opens (chapter 19 "Worktrees in the kit", the sentence at :179 included), a command typed with several slugs (12, 13, 14, 18), the claim script (19), and `after` over the parallel token (14)."

`work/done/kit-2026-10-20.md`

6. (P5, :3) "Chapters 8, 12, 14, 17 and 20 then teach the change" becomes "Chapters 8, 12, 14, 17, 18, 19 and 20 then teach the change".
7. (P5, :40) "**Out of scope.** Chapters 8, 12, 14, 17 and 20, each its M24 line;" becomes "**Out of scope.** Chapters 8, 12, 14, 17, 18, 19 and 20, each its M24 line;".
8. (P3, :40) "`work/ch13-apply-run-manual.md`, `work/ch13-19-session-folder.md` and every other hunk of docs/06" becomes "`work/ch13-apply-run-manual.md`, the draft page of a later delivery of the queue's plan and every other hunk of docs/06".

`work/done/ch08-update-2026-10-20.md`

9. (P5, :59) "touches chapters 12, 14, 17 and 20 only" becomes "touches chapters 12, 14, 17, 18, 19 and 20 only".
10. (P5, :67) "**Out of scope.** Chapters 12, 14, 17 and 20: `ch12-14-17-20-branch-claim`." becomes "**Out of scope.** Chapters 12, 14, 17, 18, 19 and 20: `ch12-14-17-20-branch-claim`."

`work/done/ch13-23-merge-default.md`

11. (S4, S10, :36) "M24's `ch12-14-parallel-token` (chapter 13); M25's `ch13-19-session-folder` (chapters 13 and 19); M27's `ch12-14-18-several-slugs` (chapters 13 and 18); M28's `ch13-19-claim-script` (chapters 13 and 19)." becomes "M25's `ch12-14-parallel-token` (chapter 13); and later deliveries of the queue's plan, on where each session opens (chapters 13 and 19), a command typed with several slugs (chapters 13 and 18) and the claim script (chapters 13 and 19)."

`work/done/ch17-23-git-slot-word.md`

12. (S10, :37) "M25's `ch13-19-session-folder` (chapter 19); M27's `ch12-14-18-several-slugs` (chapter 18); M28's `ch13-19-claim-script` (chapter 19)." becomes "and later deliveries of the queue's plan, on where each session opens (chapter 19), a command typed with several slugs (chapter 18) and the claim script (chapter 19)."

`work/done/ch08-next-free-line.md`

13. (S6, :23) "Step 5 (:89)" becomes "Step 5 (:93)".
14. (S7, :10) "inside the same block is `ch07-09-manual-wording`'s, not this delivery's." becomes "inside the same block stays: it is already the phrase `ch07-09-manual-wording` chose, and that line leaves chapter 8 unchanged."
15. (S7, :24) the whole item "* Neighbouring line on the same files: `ch07-09-manual-wording` (docs/06 :585) edits chapter 8 too, at pt :71 in the same block; this line comes first in queue order, and its change sits on other rows, so the two do not overlap." becomes "* Neighbouring line on the same files: none; `ch07-09-manual-wording` (docs/06 :585) leaves chapter 8 unchanged, its pt :71 ("devido pela") already the phrase it chose."
16. (S7, :58) "pt :71 ("devido pela") is untouched, `ch07-09-manual-wording`'s." becomes "pt :71 ("devido pela") is untouched."

`work/done/kit-2026-10-19-2.md`

17. (S3, :84) "**The project's other dispositions**, which step 4 does not check." becomes "**The project's other dispositions**, which the step 4 report did not name."
18. (S3, :87) "as the shape of a slot says; the step 4 report did not name it" becomes "as the shape of a slot says, which step 4 checks; the step 4 report did not name it".

`work/done/kit-record-step4.md`

19. (S3) After the last item of Decisions taken alone (the one opening "/apply, resumed in a fresh session"), a new item: "* Corrected later (m24-review S3): the Environments pointer is a slot's shape, which step 4 checks (:64), so this page filed it wrongly under what step 4 does not check (:8, :71); `m24-records-crossrefs` changed the record's second heading to what the step 4 report did not name, and its item to say step 4 checks a slot's shape." Lines :7, :64 and :73 stay: :7 lists what the report said, :64 is true, :73 names the heading's first words, which stay.

Terms: record, slot, migration, as docs/03 has them; no new row. No chapter, no case, no number, no code example.

**States.** Inapplicable: record pages, no screen.

**Visual reference.** Inapplicable: no screen, no chapter.

**Out of scope.**

* `work/done/kit-2026-10-20.md` :92, the same heading "which step 4 does not check": no reviewer saw a slot's shape under it; its items are that record's.
* The Contract quotes of the heading in `kit-record-step4.md` :32 and of the chapter lists in each page's Contract: the plan as written, kept as history.
* `ch12-14-17-20-branch-claim.md` :3: its Objective names 12, 14, 17 and 20 and then the sentences of 18 and 19, which is true.
* Done when, Proof, Divergences and Delivery review of these pages: `m24-records-proof`.
* P8, `work/kit-2026-10-20-1.md`: M25's in-flight page (m24-review).
* docs/06, docs/03, chapters, the kit repository.

**Decisions from the documents.**

* The candidates and their cites: `work/done/m24-review.md` :147 to :149, :156, :157, :159, :160, :163.
* The real headings: `book/en/18-git-essentials.md` :12 and `book/en/20-team-tools.md` :14, the sections holding the cited line ranges.
* A later delivery is described, not named, as `m23-records-crossrefs` :57 decided for R8: a description stays true wherever it lands.
* `ch07-09-manual-wording`'s Contract :32 ("Chapter 8: no change") and `git show --stat 7660dfc` (en 07, pt 07, pt 09, docs/06, the page).
* Step 4 checks "§5's slots and their shape" (`kit-record-step4.md` :64, from SETUP.md at `44132c4`); the record's :87 itself says "as the shape of a slot says".
* Record pages in `work/done/` are corrected by exact replacements (`kit-record-step4.md` :67; docs/05 via the batch rules).

**Decisions taken alone.**

* S3 is fixed by changing the record's second heading and one clause of its item, not by moving the item into the step 4 list: that list records what the report said, and the report did not name the pointer (:46).
* `kit-record-step4.md` gets one new item, not rewritten lines, so its history stays as it was decided, with the correction beside it; placed in Decisions taken alone because `m24-records-proof` owns its Done when, Divergences and Delivery review.
* Rule A: the M26 to M29 lines are staged, not committed, at `69d980b`, so P3 and S10 do not shrink now; /apply checks again, and shrinks them if the driver has committed the lines by then.
* The queue line keeps its wording.

**Done when.**

* [x] Rule A checked and its outcome recorded in the Proof; the replacements it leaves made word for word.
* [x] `git diff` of the eight pages shows only those replacements and the one new item.
* [x] A search of the eight pages finds no `ch13-19-session-folder`, `ch12-14-18-several-slugs`, `ch13-19-claim-script` or `ch14-after-over-token` (unless rule A kept them), no "M24's `ch12-14-parallel-token`", no "12, 14, 17 and 20" outside the Contracts and Objectives the Out of scope keeps, no "Merges and the unit of work" or "A pull request per delivery".
* [x] No em dash; no Done when item of a record unticked.
* [x] `make verify` green after the last edit, its result in this page's Proof.
* [x] The Delivery review as docs/05 §5 says, recorded with who read what and with the advisor.

**Proof.**

* Rule A: `git show HEAD:docs/06-Queue.md` at `730641f` has M24 at :597 and M25 at :615 as its last heading; `ch12-14-17-20-branch-claim` at :604 names chapters 12, 14, 17, 18, 19 and 20, `m24-records-crossrefs` is at :612 and `ch12-14-parallel-token` at :622 under M25; none of `ch13-19-session-folder`, `ch12-14-18-several-slugs`, `ch13-19-claim-script` or `ch14-after-over-token` is there. So every replacement applied as written, none skipped or shrunk.
* Each quoted text was counted in its page before editing: all 19 found exactly once, at the lines the Contract names (the new item's anchor at `kit-record-step4.md` :76).
* `git diff --numstat HEAD` of the eight pages: ch08-next-free-line 4/4, ch08-update-2026-10-20 2/2, ch12-14-17-20-branch-claim 5/5, ch13-23-merge-default 1/1, ch17-23-git-slot-word 1/1, kit-2026-10-19-2 2/2, kit-2026-10-20 2/2 (replacements 7 and 8 on one line), kit-record-step4 1/0.
* The search of the eight pages after the edits printed one line, `ch12-14-17-20-branch-claim.md:3`, its Objective's "12, 14, 17 and 20", which the Out of scope keeps. `grep -c` of the em dash: 0 in each page; of `* [ ]`: 0 in each page.
* The facts the new text states: `book/en/18-git-essentials.md` :12 "One delivery, one step to undo" and `book/en/20-team-tools.md` :14 "The pull request as the team's review"; `kit-2026-10-19-2.md` :93 is Step 5; `ch07-09-manual-wording.md` :32 "Chapter 8: no change"; `git show --stat 7660dfc`: en 07, pt 07, pt 09, docs/06 and the page.
* `make verify` green after the last edit, this page's included and the page moved to `work/done/`: build, parity, em dash, prose, width, examples, links and disclosure.
* `make book` exit 0 after that verify: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences.** The batch's lane rules leave docs/06, the staging and the commit to the driver: this session edited none of them. "With the advisor" is met by this session, which consulted its advisor before the edits and before reporting; the review agent had none. The review's note on `ch08-next-free-line.md` :24 is recorded below, left as the Contract wrote it and reported to the driver as a new line.

**Delivery review.** One read-only Opus agent this session launched, over `git diff HEAD` of the eight record pages, and this page as committed, before its Proof was written, checking rule A against HEAD's docs/06, the 19 replacements word for word, and each new sentence against the chapters, the queue, `7660dfc` and `kit-record-step4.md` :8, :64 and :71. It found nothing to fix, and two notes:

* `ch08-next-free-line.md` :24 cites `ch07-09-manual-wording` at docs/06 :585; HEAD has it at :586. The cite was true when the record was committed (:585 at `c42e106`) and is false at HEAD; replacement 15 kept it as the Contract wrote it, and it goes to the driver as a new line.
* `ch17-23-git-slot-word.md` :37 reads "(chapter 17); and later deliveries": the Contract's words, kept.

```commit
docs(m24-records-crossrefs): M24's records cite what exists

- no slug or milestone that no committed queue line holds
- the real chapter 18 and 20 headings; the branch-claim line's six chapters
- M25 for ch12-14-parallel-token; Step 5 at :93; no chapter 8 edit by
  ch07-09-manual-wording
- the Environments pointer as a slot's shape step 4 checks

work/done/ch12-14-17-20-branch-claim.md
work/done/kit-2026-10-20.md
work/done/ch08-update-2026-10-20.md
work/done/ch13-23-merge-default.md
work/done/ch17-23-git-slot-word.md
work/done/ch08-next-free-line.md
work/done/kit-2026-10-19-2.md
work/done/kit-record-step4.md
work/done/m24-records-crossrefs.md
```
