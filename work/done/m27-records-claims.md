# m27-records-claims

**Objective.** The author can read the records of M27's three deliveries and of M26's fix round, with the two earlier pages that fix round edited, and find each claim held by what happened: every Delivery review tick saying who read, against what, and whether the agent kept the session's advisor as its paragraph records it; every `make book` line saying the tree, the commit it came before and when in the run it ran; and each count, chapter list and queue mark as it was. Findings C6, C8, C9, C10, C11, C13 and C19 to C27 of `work/done/m27-review.md`.

**Behaviour.**

* Reading the Delivery review item of `ch08-update-2026-10-20-3` or `m26-records-claims`, the author finds the reader, what it was given and that it did not open docs/04 (nor docs/03, for the first), so it was narrower than docs/05 §5, and the advisor as the paragraph has it; the Divergences say the review ran narrower than the item asked (C6, C24).
* Reading the Delivery review item of `ch12-14-18-several-slugs`, `ch12-propose-worktree-path` or `ch08-worktree-slot-manual`, the author finds one read-only Opus agent launched by the lane, what it read, and that whether it kept the session's advisor, as docs/05 §5 asks, is not recorded; the paragraphs say the same; no item ticks "as docs/05 §5 says" (C8, C20, C22).
* Reading `kit-2026-10-20-3`'s Divergences, the author finds that the review tick stands only on the item /apply reworded, the advisor docs/05 §5 asks staying unproven (C9); reading its Proof, that both builds ran on HEAD `c137b00`, `m26-records-claims`' commit 7 seconds after the definition `662dadd`, which touches no `book/` file (C10); reading its Behaviour, that apply's `SKILL.md` changes its last two paragraphs (C11).
* Reading `ch08-update-2026-10-20-3`'s neighbouring-lines bullet, the author finds what `ch12-14-18-several-slugs` touched when this page was defined and what its line named at this /apply's HEAD, neither of them chapter 8 (C13).
* Reading `ch12-propose-worktree-path`, the author finds a `make book` item saying the lane ran it after the second of three verifies, its Divergences in the past ("as defined"), and its Proof naming the commit the build came before and that the tree's HEAD is not recorded (C19, C21); reading `ch08-worktree-slot-manual`'s Proof, that its build came before its commit `c90ef6b` in the tree it shared with `ch12-propose-worktree-path`, what of that lane's files the tree held not recorded (C23); reading `ch13-19-session-folder`'s Divergences, "after the second of its three verifies" (C25).
* Reading `ch08-update-2026-10-20-2`'s Divergences, the author finds both rewordings of its review item, "with the advisor" cut and "(Delivery review)" added, and the paragraph's "is not recorded"; reading `m26-records-claims`' Decisions taken alone in /apply, that the report to the driver added no line under M26 (C26).
* Reading `m26-records-claims`' Neighbouring lines, the author finds `ch08-worktree-slot-manual` `[x]` and `ch12-propose-worktree-path` `[>]` as docs/06 at its define commit `af2bc0a` has them, and only the second's chapter able to sit uncommitted in the tree (C27).
* Fails: a replacement whose quoted text is not found exactly once; any other line of these pages changed; an em dash; a Done when item of a record unticked; a chapter, docs/03, docs/05 or docs/06 touched.

**Contract.** Exact replacements in eight record pages, found by the quoted text, not by line number (line numbers as the files are now, unchanged since `93e458c`); each replacement stays on its line, so no line moves, and the rest of each page is untouched. Each Delivery review item follows the form of `m26-records-claims` replacements 1, 13 and 22 (`m24-records-proof` items 23 and 54); "narrower than docs/05 §5" only where the paragraph says docs/04 was not opened (`m24-records-proof` :186); a time-bound claim true when written is put in the past where it stands, a count false when written is corrected in place, as `m26-records-claims` corrected `ch09-14-token-wording`'s Neighbours cite (its replacement 15).

`work/done/ch08-update-2026-10-20-3.md`

1. (C6, :126) "* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says, over `git diff HEAD` of both chapter files against this page, docs/04, docs/03, the record and SETUP.md at `69a19c0`; its advisor recorded as known or not. No private case, so OD-3 approval is inapplicable." becomes "* [x] Delivery review by one read-only Opus agent, launched by this /apply, over `git diff HEAD` of both chapter 8 files and this page, against this page, `AGENTS.md`, the record's lines 94 to 126 and SETUP.md at `69a19c0` (Delivery review): narrower than docs/05 §5, which has it read against docs/04, here not opened directly, nor docs/03; whether it kept the session's advisor is not known. No private case, so OD-3 approval is inapplicable."
2. (C13, :75) "(`ch12-14-18-several-slugs` touches chapters 12, 13, 14 and 18 only)" becomes "(`ch12-14-18-several-slugs` touched chapters 12, 13, 14 and 18 only as its line read at this page's define commit `9b37854`; at `61433bb`, this /apply's HEAD, the line named chapters 12, 13, 14, 16, 18 and 19 and docs/03, none of them chapter 8)".
3. (C6, C13, :106) "**Divergences.** None. Both excerpts went in as the Contract drafts them" becomes "**Divergences.** None from the Contract. Both excerpts went in as the Contract drafts them".
4. (C6, C13, :106) "the manual sentence en 100 / pt 101." becomes "the manual sentence en 100 / pt 101. The Delivery review ran narrower than its Done when item, as defined, asked: docs/03 and docs/04 were not opened (Delivery review); `m27-records-claims` gave the item the paragraph's words. The neighbouring line widened at `61433bb`, before this page's commit, and still shared no file; `m27-records-claims` put the Contract's bullet in the past."

`work/done/ch12-14-18-several-slugs.md`

5. (C8, :137) "* [x] Delivery review by a read-only agent over this page and `git diff HEAD` of the twelve chapter files and docs/03, against docs/04 and AGENTS.md." becomes "* [x] Delivery review by one read-only Opus agent, launched by this lane, over this page and `git diff HEAD` of the twelve chapter files and docs/03, given docs/04 and AGENTS.md (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
6. (C8, :152) "given docs/04 and AGENTS.md. Its reply, as returned:" becomes "given docs/04 and AGENTS.md; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded, its reply naming none. Its reply, as returned:".

`work/done/kit-2026-10-20-3.md`

7. (C11, :10) "and its last three paragraphs, shortened with no rule changed;" becomes "and its last two paragraphs, shortened with no rule changed;".
8. (C9, :135) "and gained "(the staging and the `[x]` by the batch's driver)"." becomes "and gained "(the staging and the `[x]` by the batch's driver)". The tick stands on that reworded item alone: whether the agent kept the session's advisor, as docs/05 §5 asks, stays unproven (Delivery review)."
9. (C10, :151) "on the tree at `662dadd` with this delivery's changes:" becomes "on HEAD `c137b00`, `m26-records-claims`' commit, made 7 seconds after this page's define commit `662dadd` and touching no `book/` file (`git diff --stat 662dadd c137b00 -- book/` is empty), with this delivery's changes:".

`work/done/ch12-propose-worktree-path.md`

10. (C19, :72) "* [x] `make book`: left to the driver after the batch; the milestone review records the build." becomes "* [x] `make book` exit 0, run by this lane after the second of its three verifies, with both PDF paths (Proof); the definition left it to the driver (Divergences)."
11. (C20, :73) "* [x] Delivery review by one read-only Opus agent over this page and `git diff HEAD` of the two chapter files, against docs/04 and AGENTS.md." becomes "* [x] Delivery review by one read-only Opus agent, launched by this lane, over this page and `git diff HEAD` of the two chapter files, given docs/04 and AGENTS.md, which its reply does not name among what it read (Divergences); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
12. (C19, C21, :78) "* `make book`: the Done when item leaves it to the driver; the batch's rules had this lane run it after the last verify, and the Proof records it." becomes "* `make book`: the Done when item, as defined, left it to the driver; the batch's rules had this lane run it after the second of its three verifies, and the Proof records it. `m27-records-claims` gave the item the Proof's words."
13. (C20, :79) "though its prompt gave both and it checked docs/04's prose rules." becomes "though its prompt gave both and it checked docs/04's prose rules; nor does it say whether the agent kept the session's advisor. `m27-records-claims` gave the item these words."
14. (C20, :88) "and `book/pt/12-propose.md` and this page. Its reply, as returned:" becomes "and `book/pt/12-propose.md` and this page; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded. Its reply, as returned:".
15. (C21, :123) "This lane ran `make book` after the second verify, exit 0, both editions:" becomes "This lane ran `make book` after the second verify, before its commit `818011e`; the tree's HEAD and what it held of the other lanes' files are not recorded. Exit 0, both editions:".

`work/done/ch08-worktree-slot-manual.md`

16. (C22, :53) "* [x] Delivery review as docs/05 §5 says; only this delivery's paths" becomes "* [x] Delivery review by one read-only Opus agent, launched by this lane, over this page and `git diff HEAD` of both chapter 8 files, with `work/done/kit-2026-10-20-2.md` :18 and :76 and SETUP.md at `da29c25` (Delivery review), the paragraph naming no docs/04, against which docs/05 §5 has it read; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded; only this delivery's paths".
17. (C22, :72) "and `SETUP.md` at `da29c25` of `~/Projects/focus-kit`. Its reply: "No findings."" becomes "and `SETUP.md` at `da29c25` of `~/Projects/focus-kit`; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded. Its reply: "No findings."".
18. (C23, :74) "This lane ran `make book` on the tree at HEAD `460add8` with this delivery's edits unstaged, exit 0, both editions:" becomes "This lane ran `make book` on the tree at HEAD `460add8` with this delivery's edits unstaged, before its commit `c90ef6b`, in the one tree it shared with `ch12-propose-worktree-path`, defined at `460add8` and running beside it; what of that lane's uncommitted chapter 12 the tree held is not recorded. Exit 0, both editions:".

`work/done/m26-records-claims.md`

19. (C27, :104) "both under M26's review and `[~]`," becomes "both under M26's review, `[x]` and `[>]` in docs/06 at this page's define commit `af2bc0a`,".
20. (C27, sibling, :104) "Their uncommitted chapters may sit in the tree when this line runs `make book`; the Proof names them." becomes "The second's uncommitted chapter 12 may sit in the tree when this line runs `make book`; the Proof names what the tree held."
21. (C24, :116) "* [x] Delivery review by one read-only Opus agent this lane launches, over `git diff HEAD` of the seven pages and this page, against this page and docs/04; whether it keeps the session's advisor recorded as it is." becomes "* [x] Delivery review by one read-only Opus agent, launched by this lane, over `git diff HEAD` of the seven pages and this page (Delivery review): narrower than docs/05 §5, which has it read against docs/04, here taken from the brief it was given and not opened as a file; its report says it consulted an advisor once, of which this session has no other record."
22. (C24, :122) "**Divergences.** None from the Contract." becomes "**Divergences.** None from the Contract. The Delivery review ran narrower than its Done when item, as defined, asked: docs/04 was taken from the brief and not opened (Delivery review); `m27-records-claims` gave the item the paragraph's words."
23. (C26, :126) "that the item also gained "(Delivery review)" is reported to the driver as a possible line under M26." becomes "that the item also gained "(Delivery review)" was reported to the driver as a possible line under M26; no line was added, and `m27-records-claims` has that Divergences sentence name both rewordings and the paragraph's "is not recorded"."

`work/done/ch13-19-session-folder.md`

24. (C25, :113) "the batch's rules had this lane run it after the last verify, and the Proof records it." becomes "the batch's rules had this lane run it after the second of its three verifies, and the Proof records it."

`work/done/ch08-update-2026-10-20-2.md`

25. (C26, :98) ""with the advisor" was cut, the Delivery review paragraph recording that whether the agent kept it is not known, and" becomes ""with the advisor" was cut and "(Delivery review)" added, the Delivery review paragraph recording that whether the agent kept it is not recorded, and".

Terms: record, Delivery review, queue line, as docs/03 and docs/05 have them; no new row. No chapter, no case, no number, no code example.

**States.** Inapplicable: record pages, no screen.

**Visual reference.** Inapplicable: no screen, no chapter.

**Out of scope.**

* `ch08-update-2026-10-20-3` :13 and :83, which say chapters 12, 13, 14 and 18 teach several slugs: the plan's account of where the subject is taught, not of the neighbouring line's files, kept as written.
* `ch08-update-2026-10-20-3` :113 and `ch12-14-18-several-slugs` :203, their `make book` lines: no candidate of the review names them.
* `m26-records-claims`' Contract replacement 10 and its Built and Proof, which quote `ch13-19-session-folder` :113 as m26 left it: history of that delivery.
* The `make book` of `work/done/m27-review.md` at `93e458c`: its `book/` holds later commits to chapters 8 and 12 (`87d6be7`, `6e37777`), so it is not the build of `ch08-worktree-slot-manual` or `ch12-propose-worktree-path` and no line here cites it.
* Dropped by `work/done/m27-review.md`: C12 and C29, seen, as line-number drifts; the weak C14, C18 and C28. C7 is fixed on that page. C1 to C5 and C15 to C17 are the chapter lines'.
* docs/06, docs/03, docs/05, chapters, the kit repository, `work/done/m27-review.md`.

**Decisions from the documents.**

* The candidates and their cites: `work/done/m27-review.md` :148 to :178 and its Findings (:185).
* The Delivery review slot: docs/05 §5 (:261 to :268), a read-only agent on Opus that keeps the session's advisor, against the page and docs/04.
* The item form, "narrower" and the "not recorded" wording: `work/done/m26-records-claims.md` replacements 1, 13, 17 and 22, after `work/done/m24-records-proof.md` items 23 and 54 and its :186.
* The reworded items: `git show <define>:work/<slug>.md` against `git show <apply>:work/done/<slug>.md` over the Done when items, ticks set aside, for the six pages defined in the range (`9b37854`/`87d6be7`, `61433bb`/`6e37777`, `662dadd`/`2096a5f`, `460add8`/`818011e`, `010bc8b`/`c90ef6b`, `af2bc0a`/`c137b00`): only `kit-2026-10-20-3`'s review item changed, listed in its Divergences (:135). `ch08-update-2026-10-20-2`'s item at `d738fe5` read "one read-only Opus agent with the advisor", at `e85f8ac` "one read-only Opus agent (Delivery review)".
* C10: `git log` gives `662dadd` (11:37:51), `c137b00` (11:37:58), then `2096a5f` with parent `c137b00`; `git diff --stat 662dadd c137b00 -- book/` is empty.
* C11: `git diff c137b00 2096a5f -- .claude/skills/apply/SKILL.md` changes its first paragraph, the worktree sentence and the last two paragraphs ("Run verify until green" and "End the page"); the paragraph before them is unchanged.
* C13: `git show 9b37854:docs/06-Queue.md` :650 reads "chapters 12, 13, 14 and 18"; `61433bb`, the parent of `87d6be7`, reads "chapters 12, 13, 14, 16, 18 and 19 and docs/03".
* C19, C21, C23: `818011e`'s parent is `af2bc0a`, `c90ef6b`'s is `460add8`; `ch12-propose-worktree-path` was defined at `460add8` and committed at 11:29:26, after `c90ef6b` (11:22:15), so the two lanes ran in one tree; no page records the HEAD at `818011e`'s build.
* C26: `git show HEAD:docs/06-Queue.md` holds no M26 line on the "(Delivery review)" gain.
* C27: `git show af2bc0a:docs/06-Queue.md` :638 and :639.

**Decisions taken alone.** The agent chose each of these.

* C13 is put in the past in the Contract bullet itself and noted in Divergences, since the bullet was true at `9b37854` and the page's Divergences said "None"; C11 is corrected in place, false when written, as `m26-records-claims` corrected a cite it did not keep as history.
* "Narrower than docs/05 §5" for C6 and C24 only, whose paragraphs say docs/04 was not opened; C8 and C20, where docs/04 was given and the reply does not name it, and C22, where the paragraph lists what was read without it, say just that.
* `ch08-update-2026-10-20-3`'s item keeps its paragraph's "is not known", so item and paragraph say the same, the mismatch C26 found elsewhere not repeated.
* C9 changes the Divergences, not the item: the item already says "is not recorded"; what the record lacked was that the tick holds only on that rewording.
* C27 widens to the next sentence of the same bullet, which said both lines' chapters could sit uncommitted while `ch08-worktree-slot-manual` was committed at `c90ef6b`, before `af2bc0a`; it belongs to no other line.
* Divergences sentences that name `m27-records-claims` are added only where a Divergences already spoke of the item (`ch12-propose-worktree-path` :78 and :79) or said "None" against the finding (C6, C24); elsewhere the commit carries the change, as `m26-records-claims` did for `kit-2026-10-20-1`.
* The queue line keeps its wording.

**Neighbouring lines.** `ch08-update-other-edits` (chapter 8, being applied), `ch12-13-19-several-slugs-paths` (chapters 12, 13 and 19) and `ch16-subagent-account` (chapter 16) touch no page of this line. `ch08-update-other-edits` reads `kit-2026-10-20-3.md`'s §7 disposition and Migration report, which no replacement here changes, and no replacement moves a line. Their uncommitted chapters may sit in the tree when this line runs `make book`; the Proof names HEAD and `git status --short book/`.

**The token of this line.** `(PA)` holds: the definition takes nothing from the three lines' pages, and the build touches none of their files. No correction.

**Done when.**

* [x] Each quoted text counted once in its page before any edit; the 25 replacements made word for word.
* [x] `git diff` of the eight pages shows only those replacements, no line added or removed.
* [x] A search of the eight pages finds no ticked "as docs/05 §5 says" on a review item but in quotes of old text; no `make book` item ticked as left to the driver whose Proof says the lane ran it; and no build said to run "after the last verify" that its Proof places after an earlier one (`kit-2026-10-20-3` :86 and `m26-records-claims` :115 match their Proof, :151 and :140); each hit recorded in the Proof, as a quote or as true.
* [x] Each of the eight pages' last fenced block is `commit`, and nothing follows it; no em dash; no Done when item of a record unticked.
* [x] `make verify` green after the last edit, its result in this page's Proof; a link that fails on a refused host is named with its link, not counted green.
* [x] `make book` exit 0 after the last verify, the Proof naming HEAD, `git status --short book/` and both PDF paths.
* [x] Delivery review by one read-only Opus agent this lane launches, told to open docs/04 as a file and to list what it read, over `git diff HEAD` of the eight pages and this page, against this page and docs/04; ticked on what its paragraph records, the advisor recorded as it is.

**Built.** The 25 replacements of the Contract in the eight record pages, each made with its quoted text as the anchor and its new text word for word; replacements 3 and 4 change `ch08-update-2026-10-20-3` :106 in two places, and 19 and 20 change `m26-records-claims` :104 in two places. Before the edits, the facts the new texts assert were read again from git: `662dadd` at 11:37:51 and `c137b00` at 11:37:58 with parent `662dadd`, `2096a5f` with parent `c137b00`, `git diff --stat 662dadd c137b00 -- book/` empty; `818011e` (11:29:26) with parent `af2bc0a`, `c90ef6b` (11:22:15) with parent `460add8`; `9b37854:docs/06-Queue.md` :650 naming chapters 12, 13, 14 and 18, `61433bb`'s naming chapters 12, 13, 14, 16, 18 and 19 and docs/03; `af2bc0a:docs/06-Queue.md` :638 `[x] ch08-worktree-slot-manual` and :639 `[>] ch12-propose-worktree-path`.

**Checked.** Over the eight pages: no em dash, no unticked Done when item, each page's last fenced block `commit` with nothing after it; the search hits are listed in the Proof.

**Divergences.** None from the Contract. `make book` ran after the second of three verifies; the third, after the Proof recorded the build and the `commit` block was written, covers those last edits to this page, which no build reads.

**Delivery review.** One read-only Opus agent, launched by this lane, told to open docs/04 as a file and to list what it read, over `git diff HEAD` of the eight pages and this page, against this page and docs/04. Its reply says it opened docs/04, `AGENTS.md` and this page whole, read excerpts of the eight pages, re-applied the 25 replacements to the HEAD text by script and found the eight files identical to the result, and checked the commits, times, parents and queue lines the new texts cite with `git log` and `git show`; to the question whether it consulted an advisor, it answered "No, I did not consult any advisor." Its one finding, as returned:

> 1. `work/done/m27-records-claims.md:131`: the Proof calls "`m26-records-claims` :38, a quote of old text". But :38 holds "after the last verify" twice. One is the old text. The other is m26's own new text for `ch13-19-session-folder` :113, which this delivery's replacement 24 has just corrected, and which the Out of scope bullet at :77 keeps as history. Change it to: "`m26-records-claims` :38, its Contract's replacement 10, old and new text, kept as history (Out of scope)".

Fixed as it says, at what is now :137, after this paragraph was added above it. Its two notes, on the verify line to rerun after the last edit and on the `make book` Proof and `commit` block still to come, were the page's remaining steps, done below.

**Proof.**

* Each of the 25 anchors counted 1 in its page and sat on the line the Contract names, before any edit; after them, each new text counted 1 on that same line.
* `git diff --numstat HEAD` of the eight pages: 23 insertions and 23 deletions, the 23 changed lines; each page has as many lines as at HEAD.
* Search of the eight pages for "as docs/05 §5 says": `m26-records-claims` :8 (Behaviour), :23, :44, :55 and :62 (its Contract's quotes), :72 (Out of scope), :112 (its search item) and :137 (its Proof), all quotes of old text or of the search; no review item ticks it.
* Search for a `make book` left to the driver: `ch12-propose-worktree-path` :72 now says the lane ran it, and :78 says the definition left it; `ch13-19-session-folder` :106 and :113 say the same; `m26-records-claims` :36 and :38 are its Contract's quotes.
* Search for "after the last verify": `kit-2026-10-20-3` :86, true by its Proof :151 (a build after the first verify and again after the last); `m26-records-claims` :115, true by its Proof :140; `m26-records-claims` :38, its Contract's replacement 10, old and new text, kept as history (Out of scope).
* No em dash in the eight pages or this page; no unticked Done when item in the eight; each one's last fenced block is `commit`, nothing after it.
* `make verify` passed whole, links included, after the 25 replacements, again after the review's fix, and a third time after the ticks and this page's last edit.
* `make book` exit 0 after the second verify, on HEAD `d87f649` (`ch12-13-19-several-slugs-paths`' commit, made while this lane ran) with `git status --short book/` empty, so no other lane's uncommitted chapter was in the tree. PDFs: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

```commit
docs(m27-records-claims): make M27's records hold only what happened

- review items say who read, against what; the advisor as recorded
- make book lines name the tree and the commit the build came before
- counts, chapter lists and queue marks corrected as they were
- reworded Done when items named in Divergences

work/done/m27-records-claims.md
```
