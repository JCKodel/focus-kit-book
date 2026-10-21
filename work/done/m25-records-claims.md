# m25-records-claims

**Objective.** The author can read the records of M25's three deliveries, of M24's fix round and of `m24-records-crossrefs` and find each claim held by what happened: which tree and commit each `make book` ran at and which build holds both lanes' chapters, every Delivery review as it ran, against docs/04 or narrower, its advisor as the page records it, no slug or milestone that no committed queue line holds, counts, Contract quotes and Divergences that match, and every page ending with its `commit` block.

**Behaviour.**

* Reading the `make book` line of the Proof of `ch08-update-2026-10-20-1` or `ch12-14-parallel-token`, the author finds the exit 0 the lane recorded, that it ran before the lane's commit (`5a478e6`, `395975a`) in the one tree the two `(PA)` lanes shared, that what the tree held of the other lane is not recorded, and `work/done/m25-review.md`'s build at `dae2358`, whose `book/` is as `395975a` left it, with both PDF paths (C11).
* Reading `ch12-14-parallel-token`'s Done when, the author finds a Delivery review item that says what its paragraph records: docs/04 taken from the brief and the page, narrower than docs/05 §5 (C12).
* Reading the Delivery review paragraph of `kit-2026-10-20-1`, `ch08-update-2026-10-20-1` or `ch12-14-parallel-token`, or the Delivery review item of `ch08-update-2026-10-20-1`, `ch07-review-merge`, `ch08-23-fetch-taken`, `ch18-switch-resume`, `docs03-free-line-held` or `ch18-19-fetch-resume`, the author finds that whether the agent kept the session's advisor, as docs/05 §5 asks, is not recorded, and no item ticked "as docs/05 §5 says" (C13, C29).
* Reading `m24-records-crossrefs`' Done when, the author finds its review item saying what its Divergences records: the review agent had no advisor (C28).
* Reading the nine pages, the author finds no slug or milestone that `git show HEAD:docs/06-Queue.md` lacks; a later delivery is described by what it does, as `m24-records-crossrefs` did (C14, C31).
* Reading `ch12-14-parallel-token`, the author finds the Contract counting eight files and its Divergences naming the one shift, "and so on" shipped as "and likewise" (C15, C16); reading `kit-2026-10-20-1` :62, a tick that says the `free line` row kept "that no session holds", as its Divergences records (C19).
* Reading `m24-records-crossrefs` :16, the author finds that replacement 16 is the one that sits in a section `m24-records-proof` also edits (C32).
* Reading `ch18-19-fetch-resume`, the author finds a Delivery review item and a page-move item in its Done when, and the page ending with its `commit` block, its two Decisions sections moved before Done when (C34).
* Edge: if, when /apply starts, `git show HEAD:docs/06-Queue.md` holds every slug these pages name under the milestone they name (Contract, rule A), the C14 and C31 replacements are skipped.
* Fails: a replacement whose quoted text is not found exactly once; any other line of these pages changed; an em dash; a Done when item of a record unticked; a chapter, docs/03, docs/05 or docs/06 touched.

**Contract.** Exact replacements in nine record pages, found by the quoted text, not by line number (line numbers are at `7664d02`); the rest of each page untouched. Each Delivery review item follows the form of `m24-records-proof` items 23 and 54; none says "launched by this lane" unless its page already does, and none says "narrower than docs/05 §5" where the paragraph read against the page and docs/04 (`m24-records-proof` :186).

Rule A, checked first. At `7664d02`, HEAD's docs/06 ends at M25; M26 to M29 are a staged, uncommitted hunk. /apply runs `git show HEAD:docs/06-Queue.md`: if it holds `ch08-update-2026-10-20-2` and `ch13-19-session-folder` under M26, `ch08-update-2026-10-20-3` and `ch12-14-18-several-slugs` under M27, `ch08-update-2026-10-20-4`, `ch13-19-claim-script` and `ch08-copilot-cli` under M28, and `ch08-update-2026-10-20-5` and `ch14-after-over-token` under M29, replacements 1, 4, 5, 6, 11, 17, 19 and 22 are skipped. Otherwise every replacement applies as written.

`work/done/kit-2026-10-20-1.md`

1. (C14, :40) "`work/ch13-19-session-folder.md` and the later milestones' hunk of docs/06" becomes "the draft page of a later delivery of the queue's plan and the later milestones' hunk of docs/06".
2. (C19, :62) "and ADR-0018 say what the Contract says;" becomes "and ADR-0018 say what the Contract says, `free line` keeping "that no session holds" as Divergences records;".
3. (C13, :116) "cutting sections 3.1 to 3.5 itself." becomes "cutting sections 3.1 to 3.5 itself; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."

`work/done/ch08-update-2026-10-20-1.md`

4. (C14, :13) "(M26's worktree session folder included)" becomes "(the worktree session folder of a later kit version included)".
5. (C14, :68) "M26's `ch08-update-2026-10-20-2` rewrites this excerpt later, after this line; `ch13-19-session-folder` does not touch chapter 8." becomes "A later delivery of the queue's plan rewrites this excerpt for the next kit version, after this line; the one on where each session opens does not touch chapter 8."
6. (C14, :76) "anything later than `9be385a` (M26 and after)." becomes "anything later than `9be385a`."
7. (C11, :107) "* `make book` exit 0; PDFs: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`." becomes "* `make book` exit 0, run by this lane before its commit `5a478e6`, in the one tree it shared with `ch12-14-parallel-token`, whose chapters were then uncommitted; what of them the tree held is not recorded. PDFs: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. `work/done/m25-review.md` records the build at `dae2358`, whose `book/` is as `395975a` left it, both lines' chapters included, with both paths."
8. (C13, :111) "(the Contract's draft, kept). No new queue line." becomes "(the Contract's draft, kept). No new queue line. Whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
9. (C13, sibling, :119) "* [x] Delivery review as docs/05 §5 says, over `git diff HEAD` of both chapter files against this page, docs/04, docs/03 and the record." becomes "* [x] Delivery review by one read-only Opus agent, over `git diff HEAD` of both chapter files against this page, docs/04, docs/03 and the record (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."

`work/done/ch12-14-parallel-token.md`

10. (C15, :18) "**Contract.** Ten files," becomes "**Contract.** Eight files,".
11. (C14, :90) "`ch13-19-session-folder` (M26, chapter 13), `ch12-14-18-several-slugs` (M27, chapters 12, 13, 14), `ch14-after-over-token` (M29, chapter 14)." becomes "later deliveries of the queue's plan, on where each session opens (chapter 13), a command typed with several slugs (chapters 12, 13, 14) and `after` over the parallel token (chapter 14)."
12. (C15, C16, :116) "**Divergences.** None from the Contract. The Contract's "Ten files" counts eight: chapters 11 to 14 in two editions, as the queue line names them." becomes "**Divergences.** One from the Contract: chapter 12 :26's "and so on" shipped as "and likewise", a Delivery review note taken (Delivery review). The Contract said "Ten files" for the eight it names, chapters 11 to 14 in two editions, as the queue line names them; `m25-records-claims` corrected the count."
13. (C11, :123) "* `make book` exit 0; PDFs: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`." becomes "* `make book` exit 0, run by this lane before its commit `395975a`, in the one tree it shared with `ch08-update-2026-10-20-1`, committed at `5a478e6`; whether that commit came before the build is not recorded. PDFs: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. `work/done/m25-review.md` records the build at `dae2358`, whose `book/` is as `395975a` left it, both lines' chapters included, with both paths."
14. (C13, :126) "which this page's Out of scope already holds as silent, not false; no new queue line." becomes "which this page's Out of scope already holds as silent, not false; no new queue line. Whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
15. (C12) After the Done when item "* [x] `make book` built both editions, with both PDF paths.", a new item: "* [x] Delivery review by one read-only Opus agent, over `git diff HEAD` of the eight chapter files and this page (Delivery review): narrower than docs/05 §5, which has it read against docs/04, here taken from the brief and this page; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."

`work/done/ch07-review-merge.md`

16. (C29, :52) "* [x] The Delivery review as docs/05 §5 says, recorded on this page with who read what." becomes "* [x] Delivery review by one read-only Opus agent, over both chapter 7 files and this page, against docs/04 and AGENTS.md (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."

`work/done/ch08-23-fetch-taken.md`

17. (C31, :47) "`ch08-update-2026-10-20-1`, `-2`, `-3`, `-4`, `-5` and `ch08-copilot-cli` (chapter 8; the first rewrites the excerpt that holds pt :71 and :77); `ch12-14-parallel-token`, `ch12-14-18-several-slugs`, `ch13-19-session-folder` and `ch13-19-claim-script` (chapters 13 and 14); `ch14-after-over-token` (chapter 14)." becomes "`ch08-update-2026-10-20-1` (chapter 8; it rewrites the excerpt that holds pt :71 and :77) and later deliveries of the queue's plan on chapter 8, the update example at later kit versions and the Copilot CLI as a host; `ch12-14-parallel-token` and later deliveries on a command typed with several slugs, where each session opens and the claim script (chapters 13 and 14); a later delivery on `after` over the parallel token (chapter 14)."
18. (C29, :84) "* [x] The Delivery review as docs/05 §5 says, the Proof or the review paragraph naming who read (agent or advisor), what it read and what it found." becomes "* [x] Delivery review by one read-only Opus agent, over this page and `git diff -U0 HEAD` of the ten chapter files, with docs/04's em dash and width rules (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."

`work/done/ch18-19-fetch-resume.md`

19. (C31, :33) "M26's `ch13-19-session-folder` (chapter 19), M27's `ch12-14-18-several-slugs` (chapter 18), M28's `ch13-19-claim-script` (chapter 19)." becomes "later deliveries of the queue's plan, on where each session opens (chapter 19), a command typed with several slugs (chapter 18) and the claim script (chapter 19)."
20. (C34) After the Done when item "* [x] `make book`: not run by this lane; the driver runs it after the batch and the milestone review records the build.", two new items: "* [x] Delivery review by one read-only Opus agent, over this page and `git diff HEAD` of the four chapter files, against docs/04 and AGENTS.md (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded." and "* [x] Page moved to `work/done/`, covered by the last verify (Proof)."
21. (C34, :94 to :107) The block from "**Decisions from the documents.**" through "* Chapter 19 :179 names "the worktree and branch" instead of "the one", since the sentence creates both." moves, unchanged, to after the Out of scope's last item (:45, "* `git switch` and the other commands of :27, ...") and before "**Done when.**", one blank line on each side; the page then ends with its `commit` block.

`work/done/ch18-switch-resume.md`

22. (C31, :20) "M27's `ch12-14-18-several-slugs` (chapters 12, 13, 14 and 18), later in queue order, finds :27" becomes "a later delivery of the queue's plan, on a command typed with several slugs (chapters 12, 13, 14 and 18), finds :27".
23. (C29, :54) "* [x] The Delivery review as docs/05 §5 says, recorded on this page with who read what." becomes "* [x] Delivery review by one read-only Opus agent, over both chapter 18 files and this page, against docs/04 and AGENTS.md (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."

`work/done/docs03-free-line-held.md`

24. (C29, :51) "* [x] The Delivery review as docs/05 §5 says, recorded on this page with who read what." becomes "* [x] Delivery review by one read-only Opus agent, over `git diff HEAD -- docs/03-Domain.md` against this page, docs/04 and chapter 14 (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."

`work/done/m24-records-crossrefs.md`

25. (C32, :16) "no replacement below sits in those sections." becomes "only replacement 16 sits in one, `ch08-next-free-line`'s Proof, on a clause `m24-records-proof` leaves as it is (its :134)."
26. (C28, :101) "* [x] The Delivery review as docs/05 §5 says, recorded with who read what and with the advisor." becomes "* [x] Delivery review by one read-only Opus agent this session launched, recorded with who read what (Delivery review); the review agent had no advisor, which docs/05 §5 asks it to keep (Divergences)."

Terms: record, Delivery review, queue line, parallel token, as docs/03 and docs/05 have them; no new row. No chapter, no case, no number, no code example.

**States.** Inapplicable: record pages, no screen.

**Visual reference.** Inapplicable: no screen, no chapter.

**Out of scope.**

* The Contract quotes the review saw against what shipped: `kit-2026-10-20-1` :29 (the `free line` row as planned, its composition at :105) and `ch12-14-parallel-token` :56 ("and so on"): the plan as written, kept as history; the tick and the Divergences now say what shipped.
* `kit-2026-10-20-1` :118, which quotes "M26 to M29" as the text its review fixed: a quote of what was removed.
* `kit-2026-10-20-1` has no Delivery review item in its Done when: no candidate saw it; C13 is its paragraph's advisor.
* The Delivery review paragraphs of the four C29 pages: they say what the agent read; the item now carries the advisor.
* `m24-records-crossrefs` :113, "the review agent had none": its own record, which item 26 now matches; its quote of the old item's "With the advisor" stays as the record of how the lane justified that tick.
* C33, dropped as line-number drift; the latent C30 (`make book` items pointing to the milestone review) and the weak part of C34 (`ch18-19-fetch-resume` :63 against :50) and of C16 (the pt wording), as `work/done/m25-review.md` lists them.
* docs/06, docs/03, chapters, the kit repository, `work/ch13-19-session-folder.md`.

**Decisions from the documents.**

* The candidates and their cites: `work/done/m25-review.md` :150 to :155, :158, :167, :168, :170 to :173 (C33 dropped there).
* The Delivery review slot: docs/05 §5 (:244), a read-only Opus agent that keeps the session's advisor, against the page and docs/04.
* The item form and the "not recorded" wording: `work/done/m24-records-proof.md` items 23 and 54, and its :186 on where "narrower" belongs.
* A later delivery is described, not named: `m24-records-crossrefs` :82, with its item 8's "the draft page of a later delivery of the queue's plan".
* A page ends with its `commit` block: docs/05 §3 (:69 to :71).
* The builds: `git log` gives `5a478e6` (parent `8da0912`) and `395975a` (parent `5a478e6`); `git diff --stat 395975a dae2358 -- book/` is empty; `work/done/m25-review.md` Proof records `make book` exit 0 at `dae2358` with both paths.
* Rule A's list: the staged hunk of docs/06 at `7664d02`, M26 to M29.

**Decisions taken alone.**

* C15: the Contract's "Ten files" is corrected to "Eight files", a miscount of the list it gives, not a choice of the plan, and the Divergences says it was corrected, so the history stays on the page.
* C16 and C15 share one replacement of the Divergences, since both sit in its one paragraph.
* C28: `m24-records-crossrefs` :113 records that the review agent had no advisor, so its item says that, not "not recorded"; the driver's "recorded nowhere" holds for the pages that say nothing.
* No item says "launched by this lane" where its page does not already say who launched the agent.
* C13 on `ch08-update-2026-10-20-1` widens to its Done when item :119, a sibling that ticks "as docs/05 §5 says" and belongs to no other line.
* C34's two Decisions sections move whole to before Done when, as in `ch07-review-merge`; their text is unchanged.
* The page-move item is added, ticked, since the page's Proof (:81) records the move.
* The queue line keeps its wording.

**Neighbouring lines.** `ch09-14-token-wording` and `ch08-23-branch-read`, both under M25 and `[~]`, touch chapters and docs/03 only; this line touches nine pages in `work/done/` and this page, so none shares a file. Only replacement 21 moves lines, inside `ch18-19-fetch-resume`.

**The token of this line.** `(PA)` holds: the definition takes nothing from the pages of the two lines above in flight, and the build touches none of their files. No correction.

**Done when.**

* [x] Rule A checked and its outcome recorded in the Proof; the replacements it leaves made word for word, each quoted text counted once in its page first.
* [x] `git diff` of the nine pages shows only those replacements, the three new items and the one moved block.
* [x] A search of the nine pages finds no `ch13-19-session-folder`, `ch12-14-18-several-slugs`, `ch13-19-claim-script`, `ch14-after-over-token`, `ch08-copilot-cli`, `2026-10-20-2` to `-5` or M26 to M29, but at `kit-2026-10-20-1` :118 (unless rule A kept them); no ticked "Delivery review as docs/05 §5 says"; no "with the advisor" on a review; "Ten files" only in `ch12-14-parallel-token`'s Divergences.
* [x] Each of the nine pages' last fenced block is `commit`, and nothing follows it.
* [x] No em dash; no Done when item of a record unticked.
* [x] `make verify` green after the last edit, its result in this page's Proof.
* [x] Delivery review by one read-only Opus agent this session launches, over `git diff HEAD` of the nine pages and this page, against this page and docs/04; whether it keeps the session's advisor recorded as it is.

**Built.** The 26 replacements of the Contract in the nine record pages, each quoted text counted once in its page before any was made; replacement 21 moved `ch18-19-fetch-resume`'s two Decisions sections, unchanged, to before its Done when, so the page ends with its `commit` block.

**Checked.** The Done when searches over the nine pages: no em dash, no unticked item, each page's last fenced block `commit` with nothing after it; "Ten files" only in `ch12-14-parallel-token`'s Divergences; the "with the advisor" left are `kit-2026-10-20-1` :34, the kit's readers in its kept choices, not a review, and `m24-records-crossrefs` :113's "With the advisor", its quote of the old item, which the Out of scope keeps. The slug search and the "as docs/05 §5 says" search hit what Divergences records.

**Divergences.**

* Done when's slug search exempts only `kit-2026-10-20-1` :118, but `m24-records-crossrefs` names the M26 to M29 slugs and milestones in its own Behaviour, rule A, Contract replacements (the text it removed), Done when search and Proof (:10, :13, :18, :24 to :45, :91, :98, :105). They are that page's plan and its quotes of what it removed, the category the Out of scope gives :118, and the Contract leaves them untouched; kept.
* The Out of scope says `kit-2026-10-20-1` has no Delivery review item in its Done when; it has one, :65, ticked "Delivery review as docs/05 §5 says". The Contract does not touch it and changes no other line, so it stays; reported to the driver as a new line under M25. Behaviour's C13 and C14 bullets and the Out of scope carried these two facts wrong from the definition.

**Decisions taken alone in /apply.**

* The two hits above are left and recorded, not fixed: the Contract's "the rest of each page untouched" and Fails rule out a line it does not quote.

**Delivery review.** One read-only Opus agent this session launched read AGENTS.md, docs/04, docs/05 §5, this page and `git diff HEAD` of the nine pages and this page, re-applied the 26 replacements to HEAD's copies and got the working-tree files byte for byte; it said it had the advisor tool and consulted it once. Findings:

* Done when's slug and "as docs/05 §5 says" search does not hold as written (`m24-records-crossrefs`' own quotes, `kit-2026-10-20-1` :65): already in Divergences.
* No `make verify` result in Proof yet: added below.
* Divergences named a "NEWLINE" no queue line holds: rewritten as reported to the driver.
* Checked missed `m24-records-crossrefs` :113's "With the advisor": added.
* `ch08-23-fetch-taken`'s item does not say "narrower than docs/05 §5": the Contract allows it; no change.

**Proof.**

* Rule A: `git show HEAD:docs/06-Queue.md` at `5a40864` ends at :627, M25 at :615 its last heading, this line at :626; none of `ch08-update-2026-10-20-2` to `-5`, `ch13-19-session-folder`, `ch12-14-18-several-slugs`, `ch13-19-claim-script`, `ch08-copilot-cli` or `ch14-after-over-token` is there. So every replacement applied as written, none skipped.
* Each of the 25 quoted texts counted 1 in its page, and replacement 21's two ends and its anchor counted 1, before the edits.
* `git diff --stat HEAD -- work/done/`: the nine pages, 41 insertions and 38 deletions; `ch18-19-fetch-resume`'s diff is replacement 19, the block moved whole and the two new items.
* `make verify` passed whole (build, parity, em dash, prose, width, examples, links, disclosure) after the Contract's edits, and again after the last edit, the records and the page's move included.
* `make book` exit 0, run after that verify; PDFs: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

```commit
docs(m25-records-claims): make M25's records hold only what happened

- make book lines name the tree and commit, and the build at dae2358
- review items say what ran; the advisor recorded as it is
- no slug or milestone the committed queue lacks; counts match
- ch18-19-fetch-resume ends with its commit block

work/done/m25-records-claims.md
```
