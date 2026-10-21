# m29-records-claims

**Objective.** The author can read the records of M29's three deliveries and of M28's fix round and find each claim held by what happened: every `make verify` and `make book` item saying the order the Proof records; every Delivery review saying what its agent read and what its report says of the advisor, and, where the Done when held no review item, Divergences saying so; every Done when item reworded in /apply, or given the record's words later, named in Divergences; every list of choices made alone saying the agent chose; each mark, date and section name as it was; and `m28-records-claims`' dropped review finding given its real disposition. docs/03's `migration` row and `kit-2026-10-20-5` agree that a migration can be a rule's sentence the newer version writes out with the rule unchanged. Findings C7, C8, C10 to C14 and C18 to C25 of `work/done/m29-review.md`.

**Behaviour.**

* Reading `ch14-after-over-token`, the author finds its `make book` item saying the book ran after the verify that followed the chapters' last edit, with one more verify after it (C7); the review paragraph saying whether the agent kept the session's advisor is not recorded; and a Divergences bullet saying the Done when held no Delivery review item and naming the `make book` item's new words (C8, C7). Its "Decisions at build" say the agent chose them (C11).
* Reading `ch08-update-2026-10-20-5`, the author finds its verify item saying green after the last edit to the chapters, as the Proof records, none recorded after the page's later records, and Divergences naming that change (C10); its "Decisions taken by /apply" saying the agent chose (C11).
* Reading `kit-2026-10-20-5`, the author finds the queue line's sentence dated as it was: written at `6278488` on 2026-10-21, after `870bb13` had corrected the changelog on 2026-10-20 (C12); the opening sentence on the session's repository placed in SETUP's opening lines, above §1 (C14); and the Objective and the Contract's rule calling the `after` sentence a rule unchanged that the version writes out, as :51 and the changelog say (C13).
* Reading docs/03's `migration` row, the author finds a migration to be a rule a newer kit version changes in a project file, or a rule's sentence it writes out there with the rule unchanged, never one it only splits or rewraps (C13).
* Reading `m28-records-claims`, the author finds `ch13-16-several-slugs-sessions` `[x]` at this page's define commit `4ea1f17` (16:01), its commit `f71ac44` at 15:55 (C20); the `make book` item opening with "after the second of three verifies, not the last", and Divergences naming what /apply added to it (C19); and its review's finding 3 dropped by the batch's driver so the fix round would not loop, no queue line holding it, in Divergences and in the paragraph after the reply (C18).
* Reading `ch10-12-no-implicit-hosts`, the author finds Divergences "None from the Contract" with a sentence saying the Done when held no Delivery review item; the review paragraph saying the advisor is not recorded; and `make book` naming the commit it came before, its parent and the `[>]` line beside it there, the tree's HEAD and contents not recorded (C21).
* Reading `ch08-update-choice-outcome`, the author finds the review item saying who read, against what, and the advisor not recorded, as the paragraph now says, and Divergences naming the item's new words (C22).
* Reading `m28-claim-wording` and `ch13-16-several-slugs-sessions`, the author finds each review item saying what the agent read, narrower than docs/05 §5, and that it consulted no advisor; each Divergences saying the review ran without the session's advisor and naming the item's new words (C23); each "Decisions taken by /apply" saying the agent chose (sibling of C11). In `m28-claim-wording`, the Objective naming docs/03's container folder row beside the claim row, the queue line decision saying the line names only the claim row, and Divergences saying the commit message's docs/03 bullet claims a checked ref for both rows, though only the claim row names one (C25). In `ch13-16-several-slugs-sessions`, `m28-claim-wording` `[x]` at this page's define commit `dd570a4` (15:49), its commit `cbab6db` at 15:45, at :15, :28 and :49 (C24).
* Fails: a replacement whose quoted text is not found exactly once; any other line of these pages changed; a line added or removed but replacement 2's one new bullet; a `commit` block changed; an em dash; a Done when item of a record unticked; a chapter, docs/05 or docs/06 touched.

**Contract.** Exact replacements in eight record pages and docs/03, found by the quoted text, not by line number (line numbers as the files are now, each unchanged since its own commit: `ch14-after-over-token` `66344a9`, `ch08-update-2026-10-20-5` `3c26b8a`, `kit-2026-10-20-5` `6c8d56b`, `m28-records-claims` `db59ecf`, `ch10-12-no-implicit-hosts` `f628338`, `ch08-update-choice-outcome` `f0b1ced`, `m28-claim-wording` `cbab6db`, `ch13-16-several-slugs-sessions` `f71ac44`, docs/03 `cbab6db`; none has an uncommitted edit). Each quoted text was counted once in its page when this page was written. Each replacement stays on its line but replacement 2, which adds one bullet after its line; the rest of each file is untouched. The forms are `m28-records-claims`': a review item says who read, against what, and the advisor as the paragraph has it; "narrower than docs/05 §5" only where docs/04 was not opened or was read by grep only; a claim false when written is corrected in place (C12, C13, C14, C20, C24, C25 :3 and :67); a Done when item given the record's words is named in Divergences with "`m29-records-claims` gave the item ..."; a Done when that held no review item is said so in Divergences, never given a new ticked item; a `commit` block stays as the commit carries it.

`work/done/ch14-after-over-token.md`

1. (C7, :83) "* [x] `make book` builds both editions after the last verify, both PDF paths recorded." becomes "* [x] `make book` builds both editions after the verify that followed the chapters' last edit, one more verify following it (Divergences), both PDF paths recorded."
2. (C7, C8, :106) "as the delivery review suggested, matching pt :93 and :105." becomes "as the delivery review suggested, matching pt :93 and :105." followed by a new line, "* The Done when, as defined at `2faeb03`, held no Delivery review item, which docs/05 §5 asks before /apply ends; the review ran as its paragraph records, whether it kept the session's advisor not recorded (Delivery review). Its `make book` item said "after the last verify", while the Proof records the book after the verify that followed the review's fix and one more verify after it; `m29-records-claims` gave the item the Proof's words."
3. (C8, :117) "and `work/done/kit-2026-10-20-5.md`. Its reply, as returned:" becomes "and `work/done/kit-2026-10-20-5.md`; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded, its reply naming none. Its reply, as returned:".
4. (C11, :156) "Taken alone, by the batch rule" becomes "The agent chose these alone, by the batch rule".

`work/done/ch08-update-2026-10-20-5.md`

5. (C10, :131) "the key point en 183 / pt 184." becomes "the key point en 183 / pt 184. The Done when's verify item, as defined at `3c2a050`, said green "after the last covered edit"; the Proof records `make verify` after the last edit to the chapters and none after this page's Divergences and Delivery review records, which `make verify` also reads; `m29-records-claims` gave the item the Proof's words."
6. (C11, :133) "**Decisions taken by /apply.** The Contract's one open case" becomes "**Decisions taken by /apply.** The agent chose this one alone. The Contract's one open case".
7. (C10, :150) "* [x] `make verify` green after the last covered edit; `make book` builds both editions, with both PDF paths." becomes "* [x] `make verify` green after the last edit to the chapters, none recorded after this page's later records (Divergences); `make book` builds both editions, with both PDF paths."

`work/done/kit-2026-10-20-5.md`

8. (C13, :3) "holds the two rules the version adds to it, `after` holding /propose and /apply until every line it names is `[x]` whatever the `(PA)` token says, and" becomes "holds the two sentences the version's template adds to it, `after` holding /propose and /apply until every line it names is `[x]` whatever the `(PA)` token says, a rule unchanged that the version writes out, and".
9. (C14, :12) "SETUP's §1, which installs nowhere, gains the opening sentence on the session's repository, step 3's sentence" becomes "SETUP's opening lines, above §1, gain the sentence on the session's repository; §1, which installs nowhere, gains step 3's sentence".
10. (C13, :23) "where 2026.10.20.5 changes a rule step 4 checks, here two of §4's" becomes "where 2026.10.20.5 changes a rule step 4 checks or writes out its sentence with the rule unchanged, here two of §4's".
11. (C12, :48) "the line was written against `cc16f4e`'s changelog, which said no migration, before `870bb13` corrected it," becomes "the line, written at `6278488` on 2026-10-21, said the report names no migration, as `cc16f4e`'s changelog did, though `870bb13` had corrected that changelog on 2026-10-20,".

`work/done/m28-records-claims.md`

12. (C20, :125) "(`[~]`, chapters 13 and 16 and its page) touches no page of this line; its chapter edits are uncommitted in the tree now, so this line's" becomes "(`[x]` in docs/06 at this page's define commit `4ea1f17`, its commit `f71ac44` at 15:55, before that commit's 16:01, chapters 13 and 16 and its page) touched no page of this line; its chapter edits were committed there, and this line's".
13. (C19, :136) "* [x] `make book` exit 0 after the last verify, the Proof naming HEAD" becomes "* [x] `make book` exit 0 after the second of three verifies, not the last (Divergences), the Proof naming HEAD".
14. (C18, :143) "it is a new queue line, not this one." becomes "it was left to a new queue line, not this one, which the batch's driver did not write: by its word to `m29-records-claims`' /propose, it dropped the finding so the fix round would not loop, docs/05 §8 giving a review's finding lines no second review, and no line of docs/06 holds it."
15. (C19, :143) "`make book` ran after the second of three verifies; the third, after the Proof recorded the build" becomes "`make book` ran after the second of three verifies, and /apply added to its Done when item, from its `4ea1f17` text, ": it ran after the second of three verifies (Divergences)"; `m29-records-claims` gave the item's opening the Proof's words. The third, after the Proof recorded the build".
16. (C18, :157) "finding 3 in Divergences and as a new queue line;" becomes "finding 3 in Divergences, dropped with no queue line, as they say;".

`work/done/ch10-12-no-implicit-hosts.md`

17. (C21, :72) "**Divergences.** None: the eight sentences" becomes "**Divergences.** None from the Contract: the eight sentences".
18. (C21, :72) "the claims are still at en 08 :132-135 and pt 08 :134-137." becomes "the claims are still at en 08 :132-135 and pt 08 :134-137. The Done when, as defined at `0ada2f1`, held no Delivery review item, which docs/05 §5 asks before /apply ends; the review ran as its paragraph records (Delivery review)."
19. (C21, :79) "* `make book`: run after the verify that followed the records, exit 0;" becomes "* `make book`: run after the verify that followed the records, before this delivery's commit `f628338`, whose parent is `12d5b84`, where docs/06 holds `m28-claim-wording` `[>]` beside it, the batch's lanes sharing one tree; the tree's HEAD and which lanes' uncommitted edits it held are not recorded; exit 0;".
20. (C21, :81) "It ran neither verify nor the book, being read-only." becomes "It ran neither verify nor the book, being read-only. Whether it kept the session's advisor, as docs/05 §5 asks, is not recorded, its reply naming none."

`work/done/ch08-update-choice-outcome.md`

21. (C22, :49) "**Divergences.** None: both sentences" becomes "**Divergences.** None from the Contract: both sentences".
22. (C22, :49) "no other line of chapter 8 moved." becomes "no other line of chapter 8 moved. The Delivery review item, as defined at `a6686b3`, ticked a review "as docs/05 §5 says" recording "whether it consulted the advisor", which its paragraph does not say (Delivery review); `m29-records-claims` gave the item the paragraph's words."
23. (C22, :58) "Its prompt asked for no advisor, and its reply names none." becomes "Its prompt asked for no advisor, and its reply names none, so whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."
24. (C22, :66) "* [x] Delivery review as docs/05 §5 says, its record saying what the agent read and whether it consulted the advisor." becomes "* [x] Delivery review by one read-only Opus agent, launched by this /apply, over `git diff HEAD` of both editions of chapter 8, against this page, docs/04 and `AGENTS.md` (Delivery review), its record saying what the agent read; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded."

`work/done/m28-claim-wording.md`

25. (C25, :3) "docs/03's claim row and ADR-0018's `kit-2026-10-20-4` amendment, the reader" becomes "docs/03's claim and container folder rows and ADR-0018's `kit-2026-10-20-4` amendment, the reader".
26. (C25, :67) "* Queue line: no wording change; it names what the page changes." becomes "* Queue line: no wording change; it names docs/03's claim row, not the container folder row this page widens as a sibling (above)."
27. (C23, C25, :70) "the chapters keep 291/291 and 393/393 lines." becomes "the chapters keep 291/291 and 393/393 lines. The Delivery review ran without the session's advisor, which docs/05 §5 asks it to keep: it consulted none; and it did not reread docs/04, docs/05 or AGENTS.md beyond what was in its context, while its Done when item, as defined, ticked it as read against them (Delivery review); `m29-records-claims` gave the item the paragraph's words. The commit message below, as `cbab6db` carries it, says docs/03's container folder and claim rows name the ref each strategy checks; only the claim row names the refs checked, the container folder row the branch a worktree is on, `<prefix><slug>`."
28. (C11 sibling, :72) "**Decisions taken by /apply.** The Portuguese fix above" becomes "**Decisions taken by /apply.** The agent chose this one alone: the Portuguese fix above".
29. (C23, :93) "* [x] Delivery review by one read-only Opus agent over this page and `git diff HEAD` of the six files, against docs/04, docs/05 §§2 and 3, AGENTS.md and `claim.sh`; what it read and whether an advisor was consulted recorded as they were." becomes "* [x] Delivery review by one read-only Opus agent, launched by this /apply, over this page and `git diff HEAD` of the six files (Delivery review): narrower than docs/05 §5, which has it read against docs/04, here not reread beyond what was in its context, nor docs/05 or AGENTS.md; it read the page, the diff, `claim.sh` and grep output over `book/` and `docs/`, and consulted no advisor, which docs/05 §5 asks it to keep."

`work/done/ch13-16-several-slugs-sessions.md`

30. (C24, :15) "(the line above, `[*]`, applied before this one;" becomes "(the line above, `[x]` in docs/06 at this page's define commit `dd570a4`, its commit `cbab6db` at 15:45, before that commit's 15:49, so applied before this one;".
31. (C24, :28) "`m28-claim-wording` (`[*]`, above) touches chapter 13 :28 and chapter 19, docs/03, ADR-0018, and is applied first;" becomes "`m28-claim-wording` (above, `[x]` at `dd570a4`) touched chapter 13 :28 and chapter 19, docs/03, ADR-0018, and was applied first;".
32. (C24, :49) "chapter 13 is shared with `m28-claim-wording`, `[*]` above, so /apply waits for every line above to be `[x]`;" becomes "chapter 13 is shared with `m28-claim-wording`, above, `[x]` at `dd570a4`, so /apply's wait for every line above to be `[x]` was already met;".
33. (C23, :51) "the chapters keep 291/291 and 117/118 lines." becomes "the chapters keep 291/291 and 117/118 lines. The Delivery review ran without the session's advisor, which docs/05 §5 asks it to keep: it consulted none; and it read docs/04 by grep for two rules only and AGENTS.md only from its context, while its Done when item, as defined, ticked it as read against them (Delivery review); `m29-records-claims` gave the item the paragraph's words."
34. (C11 sibling, :53) "**Decisions taken by /apply.** The three review findings fixed now" becomes "**Decisions taken by /apply.** The agent chose this one alone: the three review findings fixed now".
35. (C23, :75) "* [x] Delivery review by one read-only Opus agent over this page and `git diff HEAD` of the four files, against docs/04, docs/05 §§2 and 3, AGENTS.md and `.claude/skills/apply/SKILL.md`; what it read and whether an advisor was consulted recorded as they were." becomes "* [x] Delivery review by one read-only Opus agent, launched by this /apply, over this page and `git diff HEAD` of the four files (Delivery review): narrower than docs/05 §5, which has it read against docs/04, here read by grep for the em dash and run-narration rules only; it read docs/05 at :188-206 with grep hits in §2 and :370, AGENTS.md only from its context and `.claude/skills/apply/SKILL.md` at :1-30, and consulted no advisor, which docs/05 §5 asks it to keep."

`docs/03-Domain.md`

36. (C13, :17, the `migration` row's definition) "A rule a newer kit version changes in a file that belongs to the project (docs/04, docs/05, `AGENTS.md`): the setup file reports it" becomes "A rule a newer kit version changes in a file that belongs to the project (docs/04, docs/05, `AGENTS.md`), or a rule's sentence it writes out there with the rule unchanged, never one it only splits or rewraps: the setup file reports it". The row then reads, whole:

```
| migration | migração | none | A rule a newer kit version changes in a file that belongs to the project (docs/04, docs/05, `AGENTS.md`), or a rule's sentence it writes out there with the rule unchanged, never one it only splits or rewraps: the setup file reports it, with the path, the section and the proposed wording, and writes nothing there; the project applies it as a delivery. |
```

Terms: record, Delivery review, queue line, mark, migration, as docs/03 and docs/05 have them; the `migration` row is widened, no row added. No chapter, no case, no number, no code example.

**States.** Inapplicable: record pages and a domain row, no screen.

**Visual reference.** Inapplicable: no screen, no chapter.

**Out of scope.**

* C9 and C16, weak, and C15 and C17, line-number drift in a record, dropped by `work/done/m29-review.md` :193; C26, weak, on chapter 16.
* C1 to C6: `ch08-other-items-claude-md`' and `ch14-renewal-example`'s, chapters 8 and 14.
* `work/done/ch12-13-19-several-slugs-paths.md` :102, the `make book` line `m28-records-claims`' review finding 3 named: dropped by the batch's driver, as replacement 14 records; this line gives the finding its disposition and leaves the line.
* `ch08-update-2026-10-20-5`'s review paragraph (:143), which says its agent did not call any advisor tool, and its Divergences, which do not say the review ran without the advisor: no candidate names it.
* `m28-claim-wording`'s `commit` block (:96 to :109): the message `cbab6db` carries, byte for byte; replacement 27 records its docs/03 bullet's overstatement in Divergences instead.
* `kit-2026-10-20-5`'s other Done when items and its review, which hold against its Proof and paragraph; `ch08-update-2026-10-20-5`'s `make book`, whose order beside the alignment edit the Proof does not record and its item does not claim.
* `ch10-12-no-implicit-hosts`' and `ch08-update-choice-outcome`'s "Decisions taken by /apply", which say nothing was open: no choice to attribute.
* Chapter 8 en :55 / pt :55, which defines a migration as "a change your documents still need": true of the widened row, and `ch08-other-items-claude-md`'s file.
* docs/05, docs/06, chapters, the kit repository, `work/done/m29-review.md`.

**Decisions from the documents.**

* The candidates and their cites: `work/done/m29-review.md`, its candidate table (:156 to :183) and Findings (:187 to :193).
* The Delivery review slot: docs/05 §5 (:265 to :272), a read-only agent on Opus that keeps the session's advisor, against the page and docs/04.
* The forms: `work/done/m28-records-claims.md` replacements 12, 23, 24, 27, 30 and 32, after `m27-records-claims`.
* The reworded items: `git show <define>:work/<slug>.md` against `work/done/<slug>.md` over the Done when items, ticks set aside, for the six pages not yet compared (`2faeb03`, `3c2a050`, `0ada2f1`, `a6686b3`, `12d5b84`, `dd570a4`): only `ch13-16-several-slugs-sessions`' fourth item changed, its grep, which its Divergences :51 already name; `m28-records-claims`' `make book` item gained ": it ran after the second of three verifies (Divergences)" from `4ea1f17`; `kit-2026-10-20-5`'s review item is named in its Divergences :115.
* C7: Proof :114 and :115, `make book` and then `make verify` once more. C10: Proof :137, the verify after the last edit to the chapters; `make verify`'s disclosure scan reads `work/done/` (`kit-2026-10-20-5.md` :156, its hit at :150).
* C12: `6278488` 2026-10-21 09:56, its docs/06 :668 "the report names no migration"; `870bb13` 2026-10-20 19:07 in the sibling checkout.
* C13: SETUP §1 step 4 at `cc16f4e` (:44 to :46), "compare its rules with the current templates and report every migration still needed"; the changelog at `870bb13`, "The rule is unchanged; a rerun reports the sentence as a migration to docs/05 §4"; the kit page :23 and the changelog's "wording only" for splits.
* C14: `git show cc16f4e:SETUP.md`, the opening sentence at :5 to :7, `## 1. What to do` at :12, step 3's templates sentence at :40 to :42, `## 2.` at :176.
* C18: docs/05 §8 :394 to :395 and :435 to :437, a review's finding lines getting no second review; docs/06 holds no line on `ch12-13-19-several-slugs-paths` :102; the disposition on the batch's driver's word to this /propose.
* C20: docs/06 at `4ea1f17` :670 holds `[x] ch13-16-several-slugs-sessions`, committed at `f71ac44` (15:55:01), `4ea1f17` at 16:01:38. C24: docs/06 at `dd570a4` :669 holds `[x] m28-claim-wording`, committed at `cbab6db` (15:45:15), `dd570a4` at 15:49:04.
* C21: `f628338`'s parent is `12d5b84`, whose docs/06 holds `m28-claim-wording` and `ch10-12-no-implicit-hosts` `[>]`, `ch08-update-choice-outcome` committed at `f0b1ced` before it.
* C25: `git show cbab6db -- docs/03-Domain.md`, the container folder row gaining `<prefix><slug>` and no ref, the claim row the refs checked; `git log -1 --format=%B cbab6db` equal to the page's `commit` block.

**Decisions taken alone.** The agent chose each of these.

* C13 widens docs/03's row rather than narrowing the kit page to it: the changelog and the kit page :51 record the `after` rule unchanged and its sentence reported, SETUP step 4 compares the project's text with the templates, and chapter 8 en :55 already reads a migration as a change the documents still need; the kit page's :3 and :23, which said the version adds or changes the rule, are corrected in place, as its own Contract read `870bb13`.
* C25's Objective (:3) and queue line reason (:67) are corrected in place, false when written, the page's own :62 widening the container folder row at define; the commit message's bullet is named in Divergences, the `commit` block left as the commit carries it.
* C18's disposition is written as the batch's driver's word, the one source for it, with docs/05 §8 as its reason; `ch12-13-19-several-slugs-paths` :102 stays.
* C19 gives the item's opening the Proof's words, as `m28-records-claims` did for `m27-records-claims` (replacement 23), and names in Divergences what /apply added.
* C7's Divergences sentence is a new bullet, the only line this delivery adds, since `ch14-after-over-token`'s Divergences are a list of separate points.
* "Narrower than docs/05 §5" for both C23 pages: `m28-claim-wording`'s agent did not reread docs/04 beyond its context, `ch13-16-several-slugs-sessions`' read it by grep for two rules.
* The "Decisions taken by /apply" of `m28-claim-wording` and `ch13-16-several-slugs-sessions` gain "The agent chose this one alone" beside C11's two: the queue line asks it of every list of choices made alone in these pages, and no other line owns them.
* C21's `make book` names no lane's edits as present, only the `[>]` line at the parent: the build's time is not recorded, and `ch08-update-choice-outcome`'s edits may still have been uncommitted when it ran.
* The queue line keeps its wording.

**Neighbouring lines.** `ch08-other-items-claude-md` (chapter 8) and `ch14-renewal-example` (chapter 14), `[~]` in the working tree's docs/06 when this page was written and `[ ]` in the committed queue at `ea83160`, beside this line under M29, touch no file of this line; their chapter edits may be uncommitted in the tree when this line runs `make book`, so its Proof names HEAD and `git status --short book/`.

**The token of this line.** `(PA)`: the definition takes nothing from the two chapter lines' pages, and the build touches none of their files; `after` names `m29-review`, `[x]`.

**Done when.**

* [x] Each quoted text counted once in its file before any edit; the 36 replacements made word for word.
* [x] `git diff` of the nine files shows only those replacements: 32 lines changed and one added, `ch14-after-over-token`'s new bullet, replacement 2 leaving its own line as it was (Divergences); `ch10-12-no-implicit-hosts` :72, `ch08-update-choice-outcome` :49 and `m28-records-claims` :143 take two replacements each.
* [x] A search of the eight pages finds no ticked review item reading "as docs/05 §5 says", no ticked `make book` item saying "after the last verify" that its Proof places before a later verify, no "Decisions taken by /apply" or "Decisions at build" holding a choice without saying the agent chose, and no `[*]` or `[~]` for `m28-claim-wording` or `ch13-16-several-slugs-sessions`; each hit recorded in the Proof, as a quote or as true.
* [x] Each of the eight pages' last fenced block is `commit`, unchanged, and nothing follows it; no em dash; no Done when item of a record unticked.
* [x] `make verify` green after the last edit, its result in this page's Proof; a link that fails on a refused host is named with its link, not counted green.
* [x] `make book` exit 0 after the verify that followed the records, one more verify following it (Divergences), the Proof naming HEAD, `git status --short book/` and both PDF paths; if `make book` runs before a later verify, the item and Divergences say so.
* [x] Delivery review by one read-only Opus agent this lane launches, told to open docs/04 as a file, to list what it read and to say whether it consulted an advisor, over `git diff HEAD` of the nine files and this page, against this page and docs/04; the tick and the paragraph record its reading and its answer on the advisor as given, and Divergences say so if it ran without the advisor docs/05 §5 asks.

**Built.** The 36 replacements of the Contract in the eight record pages and docs/03's `migration` row, applied by a script that read each old and new text from this page's Contract, counted each old text once in its file before any edit and again just before its own replacement, and wrote the new text word for word; replacement 2 keeps its line and adds `ch14-after-over-token`'s one new Divergences bullet after it. docs/03's row now reads as the Contract prints it, whole.

**Checked.** Over the eight pages: no em dash, no unticked Done when item, each page's last fenced block `commit`, unchanged, with nothing after it; over the nine files and this page, no em dash; the search hits are listed in the Proof.

**Divergences.** Two. The `make book` item, as defined at `54c819f`, said "after the last verify"; the book ran after the verify that followed the records and the page's move to `work/done/`, and one more verify followed the Proof and the `commit` block, as the Proof records; /apply gave the item those words. The other from the Delivery review's finding 1: the second Done when item, as defined at `54c819f`, said "33 lines changed and one added"; replacement 2's new text keeps its old line whole and adds the bullet after it, so `git diff --numstat` of the nine files shows 33 insertions and 32 deletions, 32 lines changed and one added. /apply gave the item those words. The Delivery review ran without the session's advisor, which docs/05 §5 asks it to keep: its reply says it consulted none (Delivery review).

**Decisions taken by /apply.** The agent chose these alone, by the batch rule to take the recommended option: finding 1 fixed in this page's Done when item, the text this delivery wrote; findings 6 and 8 kept as the reply gives them, 6 resting on the source this page's Decisions name and 8 on records not yet written when it ran. No queue line comes of the review. The queue line keeps its wording.

**Delivery review.** One read-only Opus agent (an Explore agent with model opus), launched by this lane, told to open docs/04 as a file, to list what it read and to say whether it consulted an advisor, over `git diff HEAD` of the nine files and this page, against this page and docs/04. It ran after the 36 replacements and this page's Built and Checked, before these records. Its reply says it read this page and docs/04 whole with the Read tool, the diff of the nine files, scripts that rebuilt each file from HEAD and the Contract, and the commits, queue lines and record lines it lists; and that it consulted no advisor. Its reply, as returned:

> ## Delivery review of `m29-records-claims`
>
> The build itself has no blocking finding: all 36 replacements went in word for word and nothing else changed. The one problem is in the page's own Done when, which miscounts the diff (finding 1).
>
> ### Findings
>
> 1. **The page's line count is wrong, and so is the expected 34/33. This breaks the page's Done when, not the build.** `/Volumes/Data/Projects/focus-kit-book/work/m29-records-claims.md:138` says "33 lines changed and one added". The actual diff is 33 insertions and 32 deletions: 32 lines changed and one added. Replacement 2 (page :22) keeps its old text unchanged, so `work/done/ch14-after-over-token.md:106` is not changed; the diff only adds :107 after it (`@@ -106,0 +107 @@`). So `ch14-after-over-token` shows 4 insertions and 3 deletions, not 5 and 4. Every other file matches the expected count. The build is right and the page's arithmetic is wrong. Ticking :138 as written would record a false count, so the tick or Divergences must say 32 changed and one added.
>
> 2. **All 36 replacements are exact and nothing else changed. No break.** A script parsed the 36 replacements from the committed page (`git show HEAD:work/m29-records-claims.md`) and checked each old text against HEAD of its file. Each old text occurs exactly once and on its cited line (:83 … :17, all 36). Applying the replacements to HEAD gives files byte-identical to the working tree for all nine files.
>
> 3. **Records hold their form. No break.** In each of the eight pages:
>    - the last fenced block is ```` ```commit ````, identical to HEAD, with nothing after it;
>    - no Done when item is unticked;
>    - there is no em dash, in the nine files or in the page.
>
> 4. **The docs/03 row is correct. No break.** `/Volumes/Data/Projects/focus-kit-book/docs/03-Domain.md:17` equals the row printed at page :83, byte for byte.
>
> 5. **The cited history is true. No break.** I spot-checked these:
>    - **Times:** `4ea1f17` 16:01:38 with parent `f71ac44` 15:55:01; `dd570a4` 15:49:04 with parent `cbab6db` 15:45:15. This supports replacements 12, 30, 31 and 32.
>    - **Queue marks:** docs/06 at `4ea1f17`:670 holds `[x] ch13-16-several-slugs-sessions`, and at `dd570a4`:669 holds `[x] m28-claim-wording`.
>    - **Replacement 19:** the parent of `f628338` is `12d5b84`, whose docs/06 holds `m28-claim-wording` `[&gt;]` (:669) and `ch08-update-choice-outcome` `[x]` (:672); `f0b1ced` is an ancestor of it.
>    - **Replacement 11:** `6278488` is dated 2026-10-21 09:56, and its docs/06:668 says "the report names no migration". In `/Volumes/Data/Projects/focus-kit`, `870bb13` is dated 2026-10-20 19:07 and changes "is unchanged, so a rerun reports no migration" to "a rerun reports the sentence as a migration".
>    - **Replacement 9:** in `cc16f4e:SETUP.md`, the opening sentence is at :5-7, `## 1.` at :12 and step 4 at :44-46.
>    - **Replacement 27:** `cbab6db`'s docs/03 diff gives the claim row the refs and the container folder row `&lt;prefix&gt;&lt;slug&gt;` with no ref. Its message, line 7, says both rows "name the ref each strategy checks".
>    - **Proofs and reviews behind the new text:**
>      - The ch14 Proof (:114-115) records `make book` and then one more verify.
>      - The ch08-2026 Proof (:137) records no verify after the records.
>      - The review paragraphs at m28-claim-wording :82, ch13-16 :63, ch08-choice :58 and ch10-12 :81 say what replacements 20, 23, 27, 29, 33 and 35 now state, including docs/05 :188-206, SKILL.md :1-30, "docs/04 by grep" and "consulted no advisor".
>    - **Define commits:** `2faeb03` and `0ada2f1` hold no Delivery review item, `a6686b3` holds "as docs/05 §5 says", `3c2a050` holds "after the last covered edit", and `db59ecf`'s `make book` item carries the suffix that `4ea1f17` lacks. This supports replacements 2, 5, 15, 18 and 22.
>    - **Replacement 14:** docs/05 :394-395 and :435-437 say a review's finding lines get no second review, and docs/06 holds no line for the `ch12-13-19-several-slugs-paths` :102 finding.
>
> 6. **One claim cannot be checked against the repository. No break.** Replacement 14 at `work/done/m28-records-claims.md:143` says the batch's driver dropped the finding "by its word". Nothing in the repository records that word; the page names it as the only source (:123).
>
> 7. **docs/04 holds. No break.** Its record-relevant rules are the em dash rule and that a run's record stays in `work/done/`, and both hold. Its "One sentence per line" rule is for the book's Markdown source, not records. No chapter, docs/05 or docs/06 file is in this delivery's diff.
>
> 8. **The page is not finished yet. Not a break.** `/apply` has so far appended only **Built** and **Checked** (4 insertions). All seven Done when items (:137-143) are unticked, and there is no Proof, Divergences, Delivery review paragraph or `commit` block yet. Those need to be written before close, with finding 1 recorded.
>
> ### What I read
> - `work/m29-records-claims.md`, whole, with the Read tool.
> - `docs/04-Conventions.md`, whole, with the Read tool.
> - `git status --short`, `git log --oneline -5`, and `git diff HEAD --stat/--numstat/-U0` over the nine files. The full `-U0` output went to a saved file I did not open.
> - Python scripts that ran `git show HEAD:` of the page and the nine files and read the working copies. They checked counts, line numbers, the reconstruction, the commit blocks, unticked items and em dashes.
> - `git diff HEAD -- work/m29-records-claims.md`.
> - In this repository:
>   - `git log -1` for 18 commits;
>   - `git show` of docs/06 at `4ea1f17`:670, `dd570a4`:669, `12d5b84` (grep) and `6278488` (grep);
>   - `git show cbab6db -- docs/03-Domain.md`, and its message (grep);
>   - the define-commit pages at `4ea1f17`, `db59ecf`, `2faeb03`, `0ada2f1`, `a6686b3` and `3c2a050` (grep).
> - In `/Volumes/Data/Projects/focus-kit`: `git log` and `show` for `870bb13`, plus `cc16f4e:SETUP.md` headings and :5-7, :40-46.
> - Line ranges:
>   - `ch14-after-over-token.md` :108-122 and :118-135 (grep "advisor");
>   - `ch08-update-2026-10-20-5.md` :135-146;
>   - `kit-2026-10-20-5.md` :51, :150 and :156;
>   - `m28-claim-wording.md` :82 plus a grep;
>   - `ch13-16-several-slugs-sessions.md` :63 plus a grep;
>   - `ch08-update-choice-outcome.md` :58;
>   - `ch10-12-no-implicit-hosts.md` :81;
>   - `m28-records-claims.md` :143 and :157;
>   - `docs/05-Process.md` :394-395 and :435-437;
>   - `docs/06-Queue.md` (grep for `ch12-13-19-several-slugs-paths`).
>
> I did not consult any advisor tool during this review.

Finding 1 is fixed as Divergences say; findings 2 to 5 and 7 hold; 6 and 8 kept, as Decisions say. Its line numbers for this page are as the page was when it ran.

**Proof.**

* Each of the 36 old texts counted 1 in its file before any edit and again just before its own replacement; each new text counted 1 after it.
* `git diff --numstat HEAD` of the nine files: 33 insertions and 32 deletions, the 32 changed lines and `ch14-after-over-token`'s one new bullet; no fence line in the diff; docs/03's `migration` row equal to the Contract's printed row.
* Search of the eight pages for a ticked item reading "as docs/05 §5 says": `m28-records-claims` :133, its own search item quoting the phrase, true as a quote; no review item ticks it.
* Search for a ticked `make book` item saying "after the last verify": `kit-2026-10-20-5` :68, true by its Proof :156 (the book after the last verify); `m28-records-claims` :133, its search item's quote.
* "Decisions taken by /apply" and "Decisions at build": `ch14-after-over-token` :157, `ch08-update-2026-10-20-5` :133, `m28-claim-wording` :72 and `ch13-16-several-slugs-sessions` :53 say the agent chose; `ch10-12-no-implicit-hosts` :74 and `ch08-update-choice-outcome` :51 say nothing was open, true.
* No `[*]` or `[~]` beside `m28-claim-wording` or `ch13-16-several-slugs-sessions` in the eight pages.
* No em dash in the nine files or this page; no unticked Done when item in the eight pages; each one's last fenced block is `commit`, as HEAD has it, nothing after it.
* `make verify` passed whole, `scripts/check_links.py` included, after these records and the page's move to `work/done/`, and again after this Proof and the `commit` block, the last edit.
* `make book` exit 0 after the first of those verifies, on HEAD `54c819f` (this line's define commit) with `git status --short book/` empty. PDFs: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

```commit
docs(m29-records-claims): make M29's records hold only what happened

- review items say who read, against what; the advisor as recorded
- reworded Done when items and absent review items named in Divergences
- marks, dates, sections and m28's dropped finding as they were
- docs/03: a migration may be a rule's sentence written out unchanged

work/done/m29-records-claims.md
```
