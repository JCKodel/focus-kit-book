# m26-records-claims

**Objective.** The author can read the records of M26's three deliveries, of M25's fix round and of `kit-2026-10-20-1` and find each claim held by what happened: every Done when tick saying what its Proof and Delivery review record, the advisor as the page records it, every item /apply reworded listed in Divergences, each `make book` with its tree and commit and the build that holds both lanes' chapters, cites and quotes matching what they cite, and no queue line claimed that the committed docs/06 lacks.

**Behaviour.**

* Reading `kit-2026-10-20-2`'s Divergences, the author finds that /apply reworded two Done when items from their `52fe5f9` text, the verify item gaining its exception for one external link, which the Proof records failing, and the review item its parenthesis on the driver (C4).
* Reading the Delivery review item of `kit-2026-10-20-2`, `ch08-update-2026-10-20-2`, `ch13-19-session-folder` or `kit-2026-10-20-1`, and `kit-2026-10-20-2`'s Delivery review paragraph, the author finds who read and that whether the agent kept the session's advisor, as docs/05 §5 asks, is not recorded, or, for `ch13-19-session-folder`, that nothing shows it; no item ticks "as docs/05 §5 says" or "with the advisor" (C5, C6, C7, C23).
* Reading `ch08-update-2026-10-20-2`'s Divergences, the author finds the cut "with the advisor" listed (C6).
* Reading `ch13-19-session-folder`'s Done when, the author finds a `make book` item saying this lane ran it, as the Proof records, and its two Divergences on those items written as of the definition (C8).
* Reading the `make book` line of `ch08-update-2026-10-20-2` or `ch13-19-session-folder`, the author finds that it ran before the lane's commit (`e85f8ac`, `51334ce`) in the one tree the two lanes shared, what the tree held of the other lane not recorded, and `work/done/m26-review.md`'s build at `cfcfc9d`, whose `book/` is as `51334ce` left it, with both PDF paths (C9).
* Reading `ch08-update-2026-10-20-2`'s Sources, the author finds SETUP.md step 5 at `da29c25` cited as lines 105 to 111 (C13).
* Reading the Delivery review item of `ch08-23-branch-read` or `ch09-14-token-wording`, the author finds it narrower than docs/05 §5, docs/04 not opened or not reread, and the advisor known only from the agent's own report (C22, C26).
* Reading `ch09-14-token-wording`'s `make book` item, the author finds the tree it built from, not a commit, under "Verify and book after the last edit" (C26); reading its Neighbours, that `ch08-23-branch-read` changes chapter 14 :64 and :193, not :62 (C27).
* Reading `ch08-23-branch-read`'s Divergences, the author finds that its Contract and a Decision quote chapter 14 :62 as "and the lines only a branch has", which read "adds the lines only a branch has" (C28).
* Reading `m25-records-claims`, the author finds its search item saying what the search hit, a `make book` item in its Done when, its `make book` line saying it ran before its commit `6daa835` with the tree's HEAD not recorded and no `book/` file of its own, and its Divergences saying no line was added under M25 for `kit-2026-10-20-1` :65, which this line corrects (C23, C24, C25).
* Fails: a replacement whose quoted text is not found exactly once; any other line of these pages changed; an em dash; a Done when item of a record unticked; a chapter, docs/03, docs/05 or docs/06 touched.

**Contract.** Exact replacements in seven record pages, found by the quoted text, not by line number (line numbers are at `dd0d75a`); the rest of each page untouched. Each Delivery review item follows the form of `m24-records-proof` items 23 and 54; "launched by this lane" only where the page's paragraph already says so; "narrower than docs/05 §5" only where the paragraph says docs/04 was not read (`m24-records-proof` :186).

`work/done/kit-2026-10-20-2.md`

1. (C5, :56) "* [x] Delivery review as docs/05 §5 says;" becomes "* [x] Delivery review by one read-only Opus agent, launched by this lane, over `git diff HEAD` of the twelve skill files and ADR-0018 and this page (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded;".
2. (C4) After the Divergences bullet ending "and matches word for word.", a new bullet: "* Two Done when items were reworded in /apply from their `52fe5f9` text: the verify item, which read "`make verify` green after the last covered edit;", gained "but for one external link this delivery does not touch, whose host refused every connection (Proof)", the Proof recording `scripts/check_links.py` failing, so `make verify` did not pass whole; the review item gained "(the staging and the `[x]` by the batch's driver)"."
3. (C5, :104) "cutting sections 3.1 to 3.11 itself." becomes "cutting sections 3.1 to 3.11 itself; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."

`work/done/ch08-update-2026-10-20-2.md`

4. (C13, :65) "step 5 at 105 to 110;" becomes "step 5 at 105 to 111;".
5. (C6, :98) "**Divergences.** None from the Contract; the wording departs from its drafts only as the three /apply decisions above say." becomes "**Divergences.** None from the Contract; the wording departs from its drafts only as the three /apply decisions above say. One Done when item was reworded in /apply: the Delivery review item read "one read-only Opus agent with the advisor" in the definition (`d738fe5`); "with the advisor" was cut, the Delivery review paragraph recording that whether the agent kept it is not known, and `m26-records-claims` gave the item the paragraph's words."
6. (C9, :103) "* `make book` exit 0, run after that verify, in the tree this lane shares with `ch13-19-session-folder`, whose files were then uncommitted. PDFs: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`." becomes "* `make book` exit 0, run after that verify by this lane before its commit `e85f8ac`, in the one tree it shared with `ch13-19-session-folder`, whose files were then uncommitted; what of them the tree held is not recorded. PDFs: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. `work/done/m26-review.md` records the build at `cfcfc9d`, whose `book/` is as `51334ce` left it, both lines' chapters included, with both paths."
7. (C6, :115) "and SETUP.md at `da29c25`. No private case, so OD-3 approval is inapplicable." becomes "and SETUP.md at `da29c25`; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded. No private case, so OD-3 approval is inapplicable."

`work/done/ch13-19-session-folder.md`

8. (C8, :106) "* [x] `make book`: left to the driver after the batch; the milestone review records the build." becomes "* [x] `make book` exit 0, run by this lane after the second verify, with both PDF paths (Proof); the definition left it to the driver (Divergences)."
9. (C7, :107) "* [x] Delivery review by one read-only Opus agent, with the advisor, over this page and `git diff HEAD` of the four chapter files, against docs/04 and AGENTS.md." becomes "* [x] Delivery review by one read-only Opus agent, launched by this lane, over this page and `git diff HEAD` of the four chapter files, against docs/04 and AGENTS.md (Delivery review); nothing shows it kept the session's advisor, as docs/05 §5 asks (Divergences)."
10. (C8, :113) "* `make book`: the Done when item leaves it to the driver; the batch's rules had this lane run it after the last verify, and the Proof records it." becomes "* `make book`: the Done when item, as defined, left it to the driver; the batch's rules had this lane run it after the last verify, and the Proof records it. `m26-records-claims` gave the item the Proof's words."
11. (C7, :114) "* The delivery review: the Done when item says "with the advisor";" becomes "* The delivery review: the Done when item, as defined, said "with the advisor";", and after that bullet's last words, "nothing shows it kept the session's advisor.", is added " `m26-records-claims` gave the item these words."
12. (C9, sibling, :130) "This lane ran `make book` after the second verify, exit 0, both editions: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`." becomes "This lane ran `make book` after the second verify, before its commit `51334ce`, in the one tree it shared with `ch08-update-2026-10-20-2`, committed at `e85f8ac`; whether that commit came before the build is not recorded. Exit 0, both editions: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. `work/done/m26-review.md` records the build at `cfcfc9d`, whose `book/` is as `51334ce` left it, both lines' chapters included, with both paths."

`work/done/ch08-23-branch-read.md`

13. (C22, :93) "* [x] Delivery review as docs/05 §5 says." becomes "* [x] Delivery review by one read-only Opus agent, over this page and `git diff HEAD` of the eighteen chapter files (Delivery review): narrower than docs/05 §5, which has it read against docs/04, here, with AGENTS.md, taken from the context it was given and not opened as files; its report says it consulted an advisor once, of which this session has no other record."
14. (C28, :111) "**Divergences.** One, from the Delivery review:" becomes "**Divergences.** Two, both from the Delivery review:", and after that paragraph's last words, "whose "ela" can only be the mark.", is added " And the Contract (:15) and the second Decision taken alone quote chapter 14 en :62 / pt :63 as "and the lines only a branch has" / "e as linhas que só um branch tem", which at `7664d02` read "adds the lines only a branch has" / "acrescenta as linhas que só um branch tem"; the edits carry the Contract's phrase, and the quotes stay as the plan wrote them."

`work/done/ch09-14-token-wording.md`

15. (C27, :52) "and chapter 14 :62, :64 and :193" becomes "and chapter 14 :64 and :193".
16. (C26, :86) "* [x] `make book` run after the last edit, with its commit and both PDF paths recorded in the Proof:" becomes "* [x] `make book` run after the last edit, with the tree it built from and both PDF paths recorded under Verify and book after the last edit: HEAD `5a40864` with this delivery's unstaged edits in `book/`, before this lane's commit `414a0a4`;".
17. (C26, :87) "* [x] The Delivery review (docs/05 §5) read the changes against this page and docs/04, its reader and whether it kept the session's advisor recorded." becomes "* [x] Delivery review by one read-only Opus agent, over the nine files' `git diff HEAD` and this page (Delivery review): narrower than docs/05 §5, which has it read against docs/04, here not reread, nor AGENTS.md; its report says it consulted an advisor once, of which this session has no other record."

`work/done/m25-records-claims.md`

18. (C24, :120) ""Ten files" only in `ch12-14-parallel-token`'s Divergences." becomes ""Ten files" only in `ch12-14-parallel-token`'s Divergences. Run, the search also hit `m24-records-crossrefs`' own plan and quotes, kept, and `kit-2026-10-20-1` :65's ticked "Delivery review as docs/05 §5 says" (Divergences)."
19. (C25) After the Done when item "* [x] `make verify` green after the last edit, its result in this page's Proof.", a new item: "* [x] `make book` exit 0, run after that verify, with both PDF paths (Proof)."
20. (C23, :133) "so it stays; reported to the driver as a new line under M25." becomes "so it stays; reported to the driver, and no line was added under M25; `m26-records-claims` rewords the item."
21. (C25, :153) "* `make book` exit 0, run after that verify; PDFs:" becomes "* `make book` exit 0, run after that verify, before this lane's commit `6daa835`; the tree's HEAD and what it held of the other lanes' files are not recorded, and this delivery changes no file under `book/`. PDFs:".

`work/done/kit-2026-10-20-1.md`

22. (C23, :65) "* [x] Delivery review as docs/05 §5 says;" becomes "* [x] Delivery review by one read-only Opus agent, launched by this lane, over `git diff HEAD` of the twelve skill files, docs/05, docs/03, ADR-0018, docs/06's header hunk and this page (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded;".

Terms: record, Delivery review, queue line, as docs/03 and docs/05 have them; no new row. No chapter, no case, no number, no code example.

**States.** Inapplicable: record pages, no screen.

**Visual reference.** Inapplicable: no screen, no chapter.

**Out of scope.**

* `m25-records-claims` Behaviour :9, which promised no item ticked "as docs/05 §5 says": plan text; replacement 22 makes it true of `kit-2026-10-20-1` :65.
* `m25-records-claims` :143, the review finding on "NEWLINE": what that review saw, which :133 now completes.
* `kit-2026-10-20-2` :112 and `ch08-23-branch-read` :117 already name the tree each `make book` ran on, and their commits follow them in `git log`; `kit-2026-10-20-2`'s link failure stays as its Proof records it.
* `ch08-update-2026-10-20-2` :104, which the review also cites under C13: its cites of the record (44, 65, 71 to 82, 92) and of SETUP.md (72 to 77) hold at `c43f362` and `da29c25`.
* The Contract and Decision quotes of `ch08-23-branch-read` (:15, :100) and `ch08-update-2026-10-20-2`'s Contract drafts: the plan as written, kept as history; the Divergences now say what was there and what shipped.
* `ch08-23-branch-read` :115's last finding, which already records C28 as the page's history; the Divergences now list it.
* Dropped by `work/done/m26-review.md`: C12, seen, as line-number drift; the latent C18; the weak C10, C11, C15, C19, C20, C21, C29 and C30. C14 is fixed on that page. C1 to C3, C16 and C17 are the chapter lines'.
* docs/06, docs/03, docs/05, chapters, the kit repository, `work/done/m26-review.md`.

**Decisions from the documents.**

* The candidates and their cites: `work/done/m26-review.md` :147 to :152, :156, :165 to :171, and its line 3's list (:179).
* The Delivery review slot: docs/05 §5 (:244 to :245), a read-only Opus agent that keeps the session's advisor, against the page and docs/04.
* The item form and the "not recorded" wording: `work/done/m24-records-proof.md` items 23 and 54, and its :186 on where "narrower" belongs; the build lines: `work/done/m25-records-claims.md` replacements 7 and 13.
* The reworded items: `git show <define>:work/<slug>.md` against `git show <apply>:work/done/<slug>.md` over the Done when items, for the seven pages (`52fe5f9`/`c43f362`, `d738fe5`/`e85f8ac`, `9a635ba`/`51334ce`, `7780762`/`d8b2df0`, `59e39f2`/`414a0a4`, `5a40864`/`6daa835`, `2fccad2`/`dd3cb78`): only `kit-2026-10-20-2`'s two and `ch08-update-2026-10-20-2`'s one are not in their Divergences; `kit-2026-10-20-1`'s one is (:107).
* The builds: `git log` gives `e85f8ac` then `51334ce`; `git diff --stat 51334ce cfcfc9d -- book/` is empty; `work/done/m26-review.md` :210 records `make book` exit 0 at `cfcfc9d` with `git status --short book/` empty and both paths.
* C27: `git diff -U0 6daa835 d8b2df0 -- book/en/14-queue-states.md book/en/13-apply.md` shows hunks at 13 :28 and 14 :64 and :193 only.
* C28: `git show 7664d02:book/en/14-queue-states.md` :62 and the pt :63.
* C13: `git -C ~/Projects/focus-kit show da29c25:SETUP.md`, step 5 at lines 105 to 111.
* C23: `git show HEAD:docs/06-Queue.md` holds no M25 line for `kit-2026-10-20-1` :65 and holds `m26-records-claims` (:640), so this page may name it.

**Decisions taken alone.** The agent chose each of these.

* C4: the verify tick stands, since the item already names the link exception and the Proof; the rewording goes to Divergences, with no driver's rule cited, since no document names one for that lane.
* The second rewording on `kit-2026-10-20-2` :56, "(the staging and the `[x]` by the batch's driver)", joins C4's bullet: the same cause, no other line holds it.
* C8 and C7: `ch13-19-session-folder`'s two Divergences are put in the past ("as defined") and say the item was corrected, so they do not go stale after replacements 8 and 9.
* C9 widens to `ch13-19-session-folder` :130, the sibling build in the same shared tree, which belongs to no other line.
* C25: `m25-records-claims` gets a ticked `make book` item, since its Proof records the run, as that page added items to others (its replacements 15 and 20).
* C28 goes to Divergences, not into the Contract's quote, as `m25-records-claims` kept plan quotes as history.
* C22 and C26: "narrower than docs/05 §5", since both paragraphs say docs/04 was not opened or not reread.
* The queue line keeps its wording.

**Neighbouring lines.** `ch08-worktree-slot-manual` and `ch12-propose-worktree-path`, both under M26's review and `[~]`, touch chapters 8 and 12 only; this line touches seven pages in `work/done/` and this page, so none shares a file. Their uncommitted chapters may sit in the tree when this line runs `make book`; the Proof names them.

**The token of this line.** `(PA)` holds: the definition takes nothing from the two lines' pages, and the build touches none of their files. No correction.

**Done when.**

* [ ] Each quoted text counted once in its page before any edit; the 22 replacements made word for word.
* [ ] `git diff` of the seven pages shows only those replacements and the two new items.
* [ ] A search of the seven pages finds no ticked "Delivery review as docs/05 §5 says" and no "with the advisor" on a review item, but in quotes of the old text (`ch13-19-session-folder` :114, `m25-records-claims`' Contract, :120 and :133), each hit recorded in the Proof.
* [ ] Each of the seven pages' last fenced block is `commit`, and nothing follows it; no em dash; no Done when item of a record unticked.
* [ ] `make verify` green after the last edit, its result in this page's Proof; a link that fails on a refused host is named with its link, not counted green.
* [ ] `make book` exit 0 after the last verify, the Proof naming HEAD, `git status --short book/` and both PDF paths.
* [ ] Delivery review by one read-only Opus agent this lane launches, over `git diff HEAD` of the seven pages and this page, against this page and docs/04; whether it keeps the session's advisor recorded as it is.
