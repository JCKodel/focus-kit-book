# m28-records-claims

**Objective.** The author can read the records of M28's five deliveries and of M27's fix round and find each claim held by what happened: every Delivery review tick saying who read, against what, and what its report says of the advisor, no ticked item reading "as docs/05 §5 says" where the review ran narrower; every Done when item reworded in /apply named in Divergences, and a Done when that held no review item said so; every `make book` line naming the commit it came before and the tree it ran in; and each line number, mark and neighbouring line as it was. Findings C12 to C21 and C26 to C33 of `work/done/m28-review.md`.

**Behaviour.**

* Reading `kit-2026-10-20-4`'s Delivery review item, the author finds the paragraph's account of the report, an advisor tool consulted once and not confirmed as the session's, and not just "is not recorded"; its Divergences, which already say the tick stands on the reworded item alone, name this line (C12).
* Reading `ch08-update-2026-10-20-4`'s review item, the author finds no "as docs/05 §5 says", but what the agent read, that it was narrower than docs/05 §5 (docs/04, `AGENTS.md` and docs/03 not opened) and that it did not call the advisor; the Divergences say /apply added the item's parenthesis (C13).
* Reading `ch13-19-claim-script`'s review item and paragraph, the author finds what the reply shows was read, that it does not say whether `AGENTS.md` or docs/05 was opened, and that the advisor is not recorded; the Divergences name the first Done when item's rewording in /apply (C14). Its Neighbouring lines bullet and its token reason say `ch08-copilot-cli` touched chapter 8 only at the define commit `ed47eda`, and that at `f84d8d9`, this /apply's HEAD, the line named chapters 8 and 10 with `(P-)` and its page edits docs/03's host row (C19).
* Reading `ch08-copilot-cli`, the author finds `ch13-19-claim-script` `[>]` as docs/06 at `f84d8d9` has it, not `[*]` (C20); the review paragraph saying neither docs/04 nor `AGENTS.md` was given or opened, so narrower than docs/05 §5, and the advisor not recorded; the Divergences saying the Done when held no Delivery review item (C15); and chapter 10's sentence at :33, the line the review read (C18).
* Reading `ch10-copilot-cli-invocation`, the author finds chapter 12's phrase cited at en :159 / pt :168 (C21); the queue line's "(en :32)" in the past and the driver's wording already written at the define commit `9efd4a9` (C17); and the Proof's `make book` on HEAD `9efd4a9`, with no other line in flight, and the review paragraph's advisor not recorded (C16).
* Reading `m27-records-claims`, the author finds `ch08-update-other-edits` `[x]` at the define commit `6777047` and only the other two lines' chapters able to sit in the tree (C26); its `make book` item saying after the second of three verifies (C27); and Divergences saying the review ran without the advisor docs/05 §5 asks (C28).
* Reading `ch08-update-other-edits`, `ch16-subagent-account` and `ch12-13-19-several-slugs-paths`, the author finds no review item ticking "as docs/05 §5 says" or "did not keep the session's advisor" on a reason no record shows (C29, C33); each `make book` naming the commit it came before and the lines `[>]` beside it, the tree's HEAD and contents not recorded (C30, C31); `ch16-subagent-account`'s review paragraph saying its reply's reading list names neither docs/04 nor `AGENTS.md` and its Divergences saying the Done when held no review item (C31); and `ch12-13-19-several-slugs-paths`' Divergences naming its two Done when items reworded in /apply and its review item saying docs/04 was read by grep only (C32).
* Fails: a replacement whose quoted text is not found exactly once; any other line of these pages changed; a line added or removed; an em dash; a Done when item of a record unticked; a chapter, docs/03, docs/05 or docs/06 touched.

**Contract.** Exact replacements in nine record pages, found by the quoted text, not by line number (line numbers as the files are now, each unchanged since its own commit: `kit-2026-10-20-4` `3037952`, `ch08-update-2026-10-20-4` `b595ca0`, `ch13-19-claim-script` `bba2d20`, `ch08-copilot-cli` `c75deb0`, `ch10-copilot-cli-invocation` `484035c`, `m27-records-claims` `5698ac3`, `ch08-update-other-edits` `1c943dd`, `ch16-subagent-account` `d554b12`, `ch12-13-19-several-slugs-paths` `d87f649`; none has an uncommitted edit). Each replacement stays on its line, so no line moves, and the rest of each page is untouched. The forms are `m27-records-claims`': a review item says who read, against what, and the advisor as the paragraph has it ("whether it kept the session's advisor, as docs/05 §5 asks, is not recorded"); "narrower than docs/05 §5" only where docs/04 was not opened or was read by grep only; a claim true when written and stale at /apply is put in the past where it stands and noted in Divergences; a claim false when written is corrected in place; a reworded or missing Done when item is named in Divergences, never added as a new ticked item.

`work/done/kit-2026-10-20-4.md`

1. (C12, :64) "its reader recorded; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded;" becomes "its reader recorded; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded, its report saying it consulted an advisor tool once and cannot confirm it was the session's;".
2. (C12, :113) "stays unproven (Delivery review)." becomes "stays unproven (Delivery review). `m28-records-claims` gave the item the paragraph's account of the report."

`work/done/ch08-update-2026-10-20-4.md`

3. (C13, :129) "* [x] Delivery review as docs/05 §5 says, by one read-only Opus agent over `git diff HEAD` of both chapter 8 files and this page, against this page, docs/04, `AGENTS.md`, the record, the README and SETUP.md at `ffbec72`, recording what its agent read and whether it kept the session's advisor (it did not call it; narrower than asked: `AGENTS.md`, docs/03 and docs/04 not opened)." becomes "* [x] Delivery review by one read-only Opus agent, launched by this /apply, over `git diff HEAD` of both chapter 8 files and this page, against this page, the record's lines 70 to 101, the README and SETUP.md at `ffbec72` (Delivery review): narrower than docs/05 §5, which has it read against docs/04, here not opened, nor `AGENTS.md` or docs/03; it said it did not call the session's advisor, which docs/05 §5 asks it to keep."
4. (C13, :109) "it did not open `AGENTS.md`, docs/03 or docs/04 (Delivery review)." becomes "it did not open `AGENTS.md`, docs/03 or docs/04, and did not call the session's advisor (Delivery review). /apply added to the item, which ticked "as docs/05 §5 says", the parenthesis "(it did not call it; narrower than asked: `AGENTS.md`, docs/03 and docs/04 not opened)"; `m28-records-claims` gave the item the paragraph's words."

`work/done/ch13-19-claim-script.md`

5. (C19, :82) "`ch08-copilot-cli` touches chapter 8 only. No line in flight touches chapters 13 or 19 or docs/03." becomes "`ch08-copilot-cli` touched chapter 8 only as its line read at this page's define commit `ed47eda`; at `f84d8d9`, this /apply's HEAD, the line named chapters 8 and 10 with `(P-)`, and its page edits docs/03's host row, another row of a file this page edits, its `(P-)` keeping its /apply until this line is `[x]`. No line in flight at `ed47eda` touched chapters 13 or 19 or docs/03."
6. (C19, :112) "touch chapter 8 only, none of this page's files," becomes "touched chapter 8 only at `ed47eda`, none of this page's files (`ch08-copilot-cli`, widened at `f84d8d9`, also edits docs/03's host row, its `(P-)` keeping its /apply until this line is `[x]`),".
7. (C14, :124) "* [x] Delivery review by one read-only Opus agent over this page and `git diff HEAD` of the five files, against docs/04, docs/05 §§2 and 3, the propose skill and `claim.sh`." becomes "* [x] Delivery review by one read-only Opus agent (Explore type), launched by this /apply, over this page and `git diff HEAD` of the five files, asked to read them against docs/04, docs/05 §§2 and 3, `AGENTS.md`, the propose skill and `claim.sh` (Delivery review): its reply shows docs/04's width rule, the propose skill and `claim.sh` read, and does not say whether it opened `AGENTS.md` or docs/05; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
8. (C14, :145) "it did not say whether it opened `AGENTS.md` or docs/05." becomes "it did not say whether it opened `AGENTS.md` or docs/05; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded, its reply naming none."
9. (C14, C19, :127) "the rest of the Contract is as written." becomes "the rest of the Contract is as written. One Done when item was reworded in /apply from its `ed47eda` text: the first gained "with the four wordings of Divergences". `m28-records-claims` gave the review item the paragraph's words. The neighbouring line `ch08-copilot-cli` widened at `f84d8d9`, before this page's commit, to chapter 10, its page editing docs/03's host row, its `(P-)` keeping its build after this line; `m28-records-claims` put the Contract's bullet and the token's reason in the past."

`work/done/ch08-copilot-cli.md`

10. (C20, :54) "`ch13-19-claim-script` (M28, `[*]`)" becomes "`ch13-19-claim-script` (M28, `[>]` in docs/06 at this page's define commit `f84d8d9`)".
11. (C20, :77) "`ch13-19-claim-script`, `[*]` above it," becomes "`ch13-19-claim-script`, `[>]` above it at `f84d8d9`,".
12. (C15, :79) "**Divergences.** None from the Contract: every edit went in word for word in both editions." becomes "**Divergences.** None from the Contract: every edit went in word for word in both editions. The Done when, as defined at `f84d8d9`, held no Delivery review item, which docs/05 §5 asks before /apply ends; the review ran as its paragraph records, narrower than docs/05 §5 (Delivery review)."
13. (C15, :91) "it did not list docs/04 or `AGENTS.md` among what it opened." becomes "it did not list docs/04 or `AGENTS.md` among what it opened, and neither is among what it was given: narrower than docs/05 §5, which has it read against docs/04; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded, its reply naming none."
14. (C18, :91) "(1) en 10 :32 and its Portuguese," becomes "(1) en 10 :33 (:32 before this delivery's new row) and its Portuguese,".

`work/done/ch10-copilot-cli-invocation.md`

15. (C21, :11) "chapter 12 :159 and :192," becomes "chapter 12 en :159 / pt :168,".
16. (C21, :37) "* Chapter 12 :159 and :192:" becomes "* Chapter 12 en :159 / pt :168:".
17. (C17, :45) "Queue line wording: the line cites "(en :32)"; the sentence is at :33 since ch08-copilot-cli added the CLI's row." becomes "Queue line wording: the line cited "(en :32)" when this page was written, as docs/06 at `c75deb0` has it; the sentence is at :33 since ch08-copilot-cli added the CLI's row."
18. (C17, :50) "the suggested wording above stands for it." becomes "the driver had already written the suggested wording at this page's define commit `9efd4a9`, whose line reads "(en :33)", so nothing stood open for it."
19. (C16, :55) "* `make book`: run after the last verify, exit 0;" becomes "* `make book`: run after the last verify, on HEAD `9efd4a9`, this page's define commit, which the Proof did not name: the parent of its commit `484035c`, with no commit between them, and no other line `[~]`, `[>]` or `[*]` in docs/06 there; exit 0;".
20. (C16, :57) "It ran neither verify nor the book, being read-only." becomes "It ran neither verify nor the book, being read-only. Whether it kept the session's advisor, as docs/05 §5 asks, is not recorded, its reply naming none."

`work/done/m27-records-claims.md`

21. (C26, :105) "`ch08-update-other-edits` (chapter 8, being applied)" becomes "`ch08-update-other-edits` (chapter 8, `[x]` in docs/06 at this page's define commit `6777047`, its commit `1c943dd` three minutes before)".
22. (C26, sibling, :105) "Their uncommitted chapters may sit in the tree when this line runs `make book`; the Proof names HEAD" becomes "The other two's uncommitted chapters may sit in the tree when this line runs `make book`; the Proof names HEAD".
23. (C27, :116) "* [x] `make book` exit 0 after the last verify," becomes "* [x] `make book` exit 0 after the second of three verifies (Divergences),".
24. (C27, C28, :123) "**Divergences.** None from the Contract. `make book` ran after the second of three verifies; the third," becomes "**Divergences.** None from the Contract. The Delivery review ran without the session's advisor, which docs/05 §5 asks it to keep: its agent answered that it consulted none (Delivery review). `make book` ran after the second of three verifies, not after the last as its Done when item, as defined, said; `m28-records-claims` gave the item the Proof's words. The third verify,".

`work/done/ch08-update-other-edits.md`

25. (C29, :55) "* [x] Delivery review as docs/05 §5 says, recording what its agent read and whether it kept the session's advisor." becomes "* [x] Delivery review by one read-only Opus agent, launched by this lane, over `git diff HEAD` of the two chapter files and this page, against docs/04, AGENTS.md, the record and docs/05 §7 (Delivery review), recording what its agent read; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
26. (C29, :59) "re-checked before the edit." becomes "re-checked before the edit. The Delivery review item, as defined, ticked "as docs/05 §5 says", while whether its agent kept the session's advisor, which §5 asks, is not recorded (Delivery review); `m28-records-claims` gave the item the paragraph's words."
27. (C30, :67) "* `make book`: exit 0, after the last verify;" becomes "* `make book`: exit 0, after the last verify, before this delivery's commit `1c943dd`, whose parent is `506f8d7`, in the one tree it shared with `ch16-subagent-account` and `ch12-13-19-several-slugs-paths`, `[>]` beside it in docs/06 there; the tree's HEAD and what it held of their uncommitted chapters 16, 12, 13 and 19 are not recorded;".
28. (C33, :69) "it did not keep the session's advisor, since a subagent opened this way has none." becomes "whether it kept the session's advisor, as docs/05 §5 asks, is not recorded, its reply naming none: the page said it did not, since a subagent opened this way has none, which no record shows, agents launched by this batch's sessions as general-purpose agents on Opus having each called an advisor tool once (`work/done/m27-review.md` :128), and none saying whether an Explore agent has one."

`work/done/ch16-subagent-account.md`

29. (C31, :76) "given docs/04, AGENTS.md, docs/05 §4 and §7 and docs/03's `subagent` row. Its reply, as returned:" becomes "given docs/04, AGENTS.md, docs/05 §4 and §7 and docs/03's `subagent` row; its reply's "What I read" names neither docs/04 nor AGENTS.md, which only its "Rules" heading names, and whether it kept the session's advisor, as docs/05 §5 asks, is not recorded, its reply naming none. Its reply, as returned:".
30. (C31, :67) "**Divergences.** None: every change is in both editions with the wording the Contract gives." becomes "**Divergences.** None from the Contract: every change is in both editions with the wording the Contract gives. The Done when, as defined at `a9b8f8c`, held no Delivery review item, which docs/05 §5 asks before /apply ends; the review ran as its paragraph records (Delivery review)."
31. (C31, :119) "This lane ran `make book` after the second verify, exit 0, both editions:" becomes "This lane ran `make book` after the second verify, before its commit `d554b12`, whose parent is `6777047`, in the one tree it shared with `ch12-13-19-several-slugs-paths` and `m27-records-claims`, `[>]` beside it in docs/06 there; the tree's HEAD and what it held of the first's uncommitted chapters 12, 13 and 19 are not recorded. Exit 0, both editions:".

`work/done/ch12-13-19-several-slugs-paths.md`

32. (C32, :84) "* [x] Delivery review by one read-only Opus agent over this page and `git diff HEAD` of the six chapter files, against docs/04, docs/05 §§3 and 4 and the kit skills, as its reply lists, which does not name AGENTS.md; it did not keep the session's advisor." becomes "* [x] Delivery review by one read-only Opus agent, launched by this lane, over this page and `git diff HEAD` of the six chapter files (Delivery review): narrower than docs/05 §5, which has it read against docs/04, here read by grep hits only; its reply lists docs/05 §4, the apply skill and grep hits in docs/05 §3, the propose skill and docs/04, and does not name AGENTS.md; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
33. (C32, :89) "**Divergences.** The delivery review's five findings," becomes "**Divergences.** Two Done when items were reworded in /apply from their `506f8d7` text: the first gained "with the review's wording fixes in Divergences", and the review item, which asked for one "against docs/04 and AGENTS.md" and that "the record names the agent's model and whether it kept the session's advisor, and the tick says the same", named what its reply lists and the advisor as not kept; `m28-records-claims` gave the review item the paragraph's words. The delivery review's five findings,".
34. (C33, :104) "it did not keep the session's advisor, since a subagent opened this way has none." becomes "whether it kept the session's advisor, as docs/05 §5 asks, is not recorded, its reply naming none: the page said it did not, since a subagent opened this way has none, which `work/done/m27-review.md` :128 contradicts, its general-purpose agents on Opus each having called an advisor tool once."

Terms: record, Delivery review, queue line, mark, as docs/03 and docs/05 have them; no new row. No chapter, no case, no number, no code example.

**States.** Inapplicable: record pages, no screen.

**Visual reference.** Inapplicable: no screen, no chapter.

**Out of scope.**

* C24 (`ch08-update-2026-10-20-4` :116, "on HEAD `4254cfc`"), weak: `ed47eda` landed 56 seconds before the commit and changed only docs/06 and a page. C25, fixed on `work/done/m28-review.md`. C1, C2 and C7 latent; C3, C4 and C10 weak.
* C5, C6, C22 and C23: `m28-claim-wording`'s, `[x]`. C8 and C9: `ch10-12-no-implicit-hosts`'. C11: `ch08-update-choice-outcome`'. C34 and C35: `ch13-16-several-slugs-sessions`'.
* `kit-2026-10-20-4` :30 and :53, which call `m27-records-claims` `[*]`: its Divergences :112 already say the committed queue held it `[x]`.
* `ch08-copilot-cli` :48's "en 32", the Contract's cite of chapter 10's slug sentence after the new row: true in the tree the review read; no candidate names it.
* `ch10-copilot-cli-invocation`'s Done when, which holds no Delivery review item: no candidate names it, so this line leaves it, as M28's review saw it.
* `ch10-copilot-cli-invocation` :11 and :37's "stay" on chapter 12, which `ch10-12-no-implicit-hosts` later widened: what the page decided when it ran, kept as history.
* `ch08-update-choice-outcome` :66 and the other M28 fix-round pages: M29's review's range, not this line's.
* The eight earlier pages `m27-records-claims` edited, read by M28's records 2 reader, which found the twenty-five replacements reproduced: no candidate names them.
* docs/06, docs/03, docs/05, chapters, the kit repository, `work/done/m28-review.md`.

**Decisions from the documents.**

* The candidates and their cites: `work/done/m28-review.md`, its candidate table (:164 to :185) and Findings (:197); the readers' fuller wording in the review's working notes, kept out of the repository.
* The Delivery review slot: docs/05 §5 (:261 to :268), a read-only agent on Opus that keeps the session's advisor, against the page and docs/04.
* The item form, "narrower" and the "not recorded" wording: `work/done/m27-records-claims.md` replacements 1, 5, 11 and 21, after `m26-records-claims` and `m24-records-proof`.
* The reworded items: `git show <define>:work/<slug>.md` against `git show <apply>:work/done/<slug>.md` over the Done when items, ticks set aside, for the nine pages (`953b4ec`/`1c943dd`, `a9b8f8c`/`d554b12`, `506f8d7`/`d87f649`, `6777047`/`5698ac3`, `e8e37c5`/`3037952`, `4254cfc`/`b595ca0`, `ed47eda`/`bba2d20`, `f84d8d9`/`c75deb0`, `9efd4a9`/`484035c`): changed are `kit-2026-10-20-4`'s review item (in its Divergences :113), `ch08-update-2026-10-20-4`'s review item (the parenthesis), `ch13-19-claim-script`'s first item, and `ch12-13-19-several-slugs-paths`' first and review items; `ch08-copilot-cli`'s items were plain bullets at `f84d8d9`, ticked in /apply, with no review item; `ch16-subagent-account` and `ch10-copilot-cli-invocation` held none at either commit.
* C19: `git show ed47eda:docs/06-Queue.md` :666 reads "chapter 8: the GitHub Copilot CLI ..." with no token; `f84d8d9`'s reads "[>] ch08-copilot-cli (P-)  chapters 8 and 10"; `git show f84d8d9:work/ch08-copilot-cli.md` :50 edits docs/03's host row; `bba2d20`'s parent is `f84d8d9`.
* C20: docs/06 at `f84d8d9` :665 holds `[>] ch13-19-claim-script`; at `c75deb0`, `[x]`; no commit holds it `[*]`.
* C18: chapter 10's "In Claude Code a command runs only when you name it" is en :32 / pt :32 at `f84d8d9` and en :33 / pt :33 at `c75deb0`.
* C21: at `c75deb0`, "stops Claude Code from running a skill on its own" is en `12-propose.md` :159 and its Portuguese pt :168; en :192 is the key point on `/propose a b`.
* C17: docs/06 at `c75deb0` :667 reads "(en :32)"; at `9efd4a9` :667, "(en :33)", the page's suggested wording with the token.
* C16: `484035c`'s parent is `9efd4a9` (14:36:56, 14:40:56), no commit between; docs/06 at `9efd4a9` holds no `[~]`, `[>]` or `[*]` but :667.
* C26: docs/06 at `6777047` :652 holds `[x] ch08-update-other-edits`, committed at `1c943dd` (13:30:22), `6777047` at 13:33:24.
* C30, C31: `1c943dd`'s parent is `506f8d7`, whose docs/06 holds :653 and :654 `[>]`; `d554b12`'s parent is `6777047`, whose docs/06 holds :653 and :655 `[>]`.
* C33: `work/done/m27-review.md` :128, its readers and checker launched "as a general-purpose agent with its model set to Opus", each calling the advisor tool once; `kit-2026-10-20-4` :122, its agent reporting an advisor tool.

**Decisions taken alone.** The agent chose each of these.

* No Delivery review item is added to `ch08-copilot-cli`'s or `ch16-subagent-account`'s Done when: a ticked item written after the run would rewrite the definition and add a line; the Divergences say the Done when held none, which docs/05 §5 asks.
* C33 turns "it did not keep the session's advisor" into "is not recorded" in both pages and in their review items: the replies name no advisor, and the page's reason is the only ground for "did not"; for `ch08-update-other-edits`' Explore agent the text says no record shows whether one has an advisor, rather than claiming it had one.
* `m27-records-claims`' review item stays: "the advisor recorded as it is" holds; the fix is its Divergences, which said "None" against a review run without the advisor docs/05 §5 asks.
* `kit-2026-10-20-4`'s item gains the report's words rather than a new Divergences sentence: its Divergences already have m27's form; the item said less than the paragraph.
* `ch10-copilot-cli-invocation`'s `make book` names HEAD `9efd4a9` as fact, not "not recorded": no commit lies between the define commit and the delivery's, and no other line was in flight, so the tree held only this delivery's changes.
* "Narrower than docs/05 §5" for `ch08-copilot-cli` (replacements 12 and 13), whose paragraph names docs/04 neither among what the agent was given nor among what it opened: read as not opened, stricter than `m27-records-claims`' C22, which in the same case said just that; for `ch16-subagent-account`, given docs/04, the paragraph says just what its reply lists.
* C18 is corrected in the review paragraph, which paraphrases the reply and quotes none of it, with the old line number in parentheses.
* C19 and C17 are put in the past, true when written; C21, C20 and C26 are corrected in place, false when written; C26 widens to the next sentence of the same bullet, which belongs to no other line.
* The queue line keeps its wording.

**Neighbouring lines.** `ch13-16-several-slugs-sessions` (`[~]`, chapters 13 and 16 and its page) touches no page of this line; its chapter edits are uncommitted in the tree now, so this line's `make book` Proof names HEAD and `git status --short book/`. `m28-claim-wording`, `ch10-12-no-implicit-hosts` and `ch08-update-choice-outcome` are `[x]` and touched none of the nine pages.

**The token of this line.** `(PA)`: the definition takes nothing from `ch13-16-several-slugs-sessions`' page, and the build touches none of its files.

**Done when.**

* [ ] Each quoted text counted once in its page before any edit; the 34 replacements made word for word.
* [ ] `git diff` of the nine pages shows only those replacements, no line added or removed (32 lines changed: `ch08-copilot-cli` :91 and `m27-records-claims` :105 take two each).
* [ ] A search of the nine pages finds no ticked review item reading "as docs/05 §5 says" and no "a subagent opened this way has none" but in the replaced texts' own quotes; no `make book` said to run "after the last verify" that its Proof places after an earlier one; each hit recorded in the Proof, as a quote or as true.
* [ ] Each of the nine pages' last fenced block is `commit`, and nothing follows it; no em dash; no Done when item of a record unticked.
* [ ] `make verify` green after the last edit, its result in this page's Proof; a link that fails on a refused host is named with its link, not counted green.
* [ ] `make book` exit 0 after the last verify, the Proof naming HEAD, `git status --short book/` and both PDF paths; if `make book` runs before a later verify, the item and Divergences say so.
* [ ] Delivery review by one read-only Opus agent this lane launches, told to open docs/04 as a file, to list what it read and to say whether it consulted an advisor, over `git diff HEAD` of the nine pages and this page, against this page and docs/04; the tick and the paragraph record its reading and its answer on the advisor as given, and Divergences say so if it ran without the advisor docs/05 §5 asks.
