# conflict-same-lines

**Objective.** A reader of chapter 19, and a session reading docs/05 §§4 and 6 or docs/03, finds one definition of a conflict between two sessions in one folder, the same lines edited by both, so two marks side by side in one hunk of docs/06, one changed by each session, are staged and never stopped for.

**Decided without the author.** This page was written in a batch /propose with no question asked (the author's instruction for this run); each decision names its source, so the author corrects it in the review of this page.

1. The unit of a conflict is the line, not the hunk. The documents leave two readings: keep "the same hunk" and have adjacent marks stop the session, or say "the same lines" and have them staged. Taken: the lines. Sources: git's own conflict, in docs/03:93's first sentence and chapters 18:134 and 19:14, is "the same lines"; chapter 19:271 already argues that a batch's shared hunk holds no conflict; the next line of M17, `ch19-adjacent-mark-staging`, presupposes adjacent marks are staged; this line's slug. Stopping for them would stop every batch at its first staged mark.
2. "Hunk" stays wherever it names what is staged or read, not what conflicts: docs/05 §4:140-141 ("paths and hunks, including its own hunk of docs/06"), §5:208-209 (Delivery review), §6:250, :257 and :266, chapter 13:64, 89, 91 and 118, chapter 19:28, 34, 288 and 316. Each is true for lines far apart, the common case, and the adjacent case is said once where the definition is (Contract) and taught by `ch19-adjacent-mark-staging`.
3. The definition says the adjacent case in one clause, in docs/05 §4 and docs/03, since a session reading only those (the apply skill sends it to docs/05 §§4 and 6, `.claude/skills/apply/SKILL.md:25`) would otherwise read one hunk as one change. docs/05 §6 only drops its "same hunk".
4. Kit: the kit's process text defines the conflict by hunk and assumes each delivery owns a hunk of docs/06 (`m17-review` candidate R3-3, kit side). `kit:` the author tells the kit that its §4 and §6 should say "the same lines" and name adjacent marks as no conflict; this repository's docs/05 changes here as the project's text and the kit is not edited (batch instruction; `m17-review` decision 4).

**Behaviour.**

* A reader of chapter 19 §What is and is not a conflict there finds the first conflict as both deliveries editing the same lines of a file (`src/features/loans/rules.ts`, pt `src/features/emprestimos/regras.ts`), with no "hunk" in that bullet.
* A reader of §Proposing in a batch reads that the lines of a batch sit side by side, git puts their marks in one hunk, and that hunk holds no conflict because no line in it is changed by two sessions; the sentence no longer has to explain that "the same hunk" means "the same lines".
* The second key point says the same lines edited by both, or a file one page needs that the other is changing, is a conflict.
* A session that reads docs/05 §4 finds: a conflict is the same lines edited by both, or a file this page needs that the other delivery is changing; two lines next to each other, one edited by each, are not a conflict, though git shows them in one hunk. docs/05 §6 stops it when this delivery and another changed the same lines, and for no "same hunk".
* docs/03's conflict row, between two sessions in one folder, says the same lines and the adjacent case, as docs/05 §4.
* Edge: a search of `book/`, `docs/`, `AGENTS.md` and `README*.md` for "same hunk" and "mesmo hunk" finds nothing after this delivery.
* Edge: the Portuguese edition says "as mesmas linhas" in each place the English says "the same lines", and keeps "hunk" where the English keeps it (docs/04 §Languages).
* Fails, and is fixed before done: any place that still makes the hunk the unit of a conflict, in either edition or in docs/03 or docs/05.

**Contract.**

Chapter 19, `book/en/19-worktrees.md` and `book/pt/19-worktrees.md`, same lines in both:
* §What is and is not a conflict there, line 70: the bullet says the two deliveries edit the same lines of the file, and drops "the same hunk".
* §Proposing in a batch, line 271: the sentence keeps that the hunk holds no conflict, that no line in it is changed by two sessions, and that each session's change is its own line's mark, which the list of what is not a conflict names first; it drops "which is what the conflict above means by the same hunk, the same lines".
* §Key points, the second bullet, line 317: "the same lines edited by both" in place of "the same hunk edited by both" (pt "as mesmas linhas editadas pelas duas").
* No new term, source note or case. docs/03's terms: conflict, stage, queue, mark.

docs/05, exact (the file wraps at about 72 columns; /apply rewraps the paragraph and changes no other sentence):
* §4, lines 142 to 143, the sentence "A conflict is the same hunk edited by both, or a file this page needs that the other delivery is changing; then stop and report." becomes: "A conflict is the same lines edited by both, or a file this page needs that the other delivery is changing; then stop and report. Two lines next to each other, one edited by each, are not a conflict, though git shows them in one hunk: each session stages only its own line."
* §6, lines 252 to 254: "or changes overlap in the same hunk," becomes "or this delivery and another changed the same lines,".

docs/03, row `conflict`, line 93, exact, its second part: "Between two sessions in one folder, the same lines edited by both, or a file one page needs that the other delivery is changing: the session stops and reports; two lines next to each other, one changed by each, are no conflict, though git shows them in one hunk." The Portuguese column and the first sentence do not change.

Shared files and order: `ch19-adjacent-mark-staging` edits chapter 19's next line, 272 to 273, in both editions, and applies after this page: it keeps line 271 as this page leaves it. `pt-librarian-masculine` (another agent) edits `book/pt/19-worktrees.md` after both; `docs05-fourth-case-version` edits docs/05:134 and docs/03:106; `docs05-four-cases-sentence` docs/05:115-118; `untracked-diff-wording` docs/03:75; `docs03-checker-pt` docs/03:33 and :36. All are other hunks: /apply stages this delivery's hunks of `book/en/19-worktrees.md`, `book/pt/19-worktrees.md`, docs/03 and docs/05 with `git add -p`, and its own line of docs/06.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* "Hunk" where it names what is staged or read (decision 2): true for lines far apart.
* How a session stages one line of a shared hunk: `ch19-adjacent-mark-staging`, the next line.
* Chapter 18's merge conflict and chapter 19's §When the branches meet: already "the same lines".
* The kit's text: the kit's own, on the author's word (decision 4).

**Done when.**

* [x] Chapter 19 lines 70, 271 and 317 changed in both editions as the Contract says.
* [x] docs/05 §4 and §6 and docs/03's conflict row hold the Contract's exact text.
* [x] `grep -rn "same hunk\|mesmo hunk" book docs AGENTS.md README*.md` finds nothing outside `work/` and docs/06's history.
* [x] `make verify` green.
* [x] `make book`, and the paths of both PDFs given to the author.
* [x] The delivery review run as docs/05 §5 says, and recorded.
* [x] Page in `work/done/`, line `[x]`, staged by hunk as the Contract says, commit message in a `commit` block, `kit:` note for the author in the final report.

**Built.** Chapter 19, both editions, lines 70, 271 and 317 as the Contract says, English first; docs/05 §4 and §6 and docs/03's conflict row with the Contract's exact text. A search of `book`, `docs` (docs/06's history aside), `AGENTS.md` and `README*.md` for "same hunk" and "mesmo hunk" finds nothing.

**Decisions at apply time.** docs/05's §4 paragraph is rewrapped from the edited sentence to its end, to stay within the file's width; no other sentence changed. docs/06's hunk holds other sessions' `[>]` marks set by the driver, next to this line's: this delivery stages only its own line, from an index copy built on HEAD with that one line changed, which is the case this page defines as no conflict. Chapter 19 line 185 ("or lines next to each other") is git's merge between branches, not two sessions in one folder, and stays. No Case A or Case B passage.

**Divergences and omissions.** None.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure); `make book` builds `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review.** One read-only agent on Opus read this delivery's diff of both chapter files, docs/03 and docs/05 and its line of docs/06 against this page and docs/04. One finding, fixed: two lines of docs/05 (§4 and §6) ran past the file's width after the edit, so both paragraphs were rewrapped and verify run again, green. Everything else held: the exact texts, the Portuguese mirroring the English, no em dash, every remaining "hunk" near "conflict" naming what is staged (decision 2).

**Kit note for the author.** `kit:` the kit's §4 and §6 should define a conflict between two sessions as the same lines edited by both, and name two adjacent lines, one changed by each, as no conflict though git shows them in one hunk (decision 4).

```commit
docs(conflict-same-lines): define a session conflict by lines, not hunks

- Chapter 19's conflict bullet, batch hunk sentence and key point say the same lines
- docs/05 §4 names adjacent lines in one hunk as no conflict; §6 drops "same hunk"
- docs/03's conflict row says the same lines and the adjacent case
- Both editions

work/done/conflict-same-lines.md
```
