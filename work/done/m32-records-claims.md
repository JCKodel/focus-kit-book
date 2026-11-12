# m32-records-claims

**Objective.** The author can read the records of `kit-2026-10-24`, `ch08-update-2026-10-24`, `ch11-14-queue-tree` and `ch19-queue-branches` and find each claim held by what happened: `queue.sh` reading docs/06 and not work/; the Portuguese line of the 2026.10.20.3 sentence; the six screenshots said to show chapter 14 before its review's two fixes; the fixture's token change named as a change to the Contract, not to decision 4; and the changelog's words quoted without "or in-flight". Findings R2-7, R3-1, R3-2, R3-3 and R3-4 of `work/done/m32-review.md`.

**Behaviour.**

* Reading `work/done/kit-2026-10-24.md`, the author finds at :30 and :88 that AGENTS.md's "Asked where things stand" bullet answers from docs/06 and work/, and that `queue.sh` reads docs/06, not work/; no longer "as `queue.sh` reads them" (R2-7).
* Reading `work/done/ch08-update-2026-10-24.md`, the author finds Proof (:121) saying `2026.10.20.3` is only at en 97 / pt 99, where both chapter 8 files had it at `7d8a0e7` (R3-1).
* Reading `work/done/ch11-14-queue-tree.md`, the author finds after "The glyph" (:154) that the six shots were taken before the Delivery review's two fixes to chapter 14 (Divergences, :159): all six show "the same alias" ("o mesmo alias"), now "the same alias trick" ("o mesmo truque de alias"), and the four site shots also show `m1-review`'s page "takes every delivery of the milestone" ("toma cada entrega do marco"), now taking the milestone's paragraph clause by clause; the glyph they prove is unchanged by those fixes (R3-2).
* Reading `work/done/ch19-queue-branches.md`, the author finds at :82 and :86 that option 1 changed the Contract's fixture, whose `m2-review` line carried `(--)`, and not decision 4, which is this line's own `(PA)` token and stays (R3-3); and at :101 the chapter's "does not show a merged or in-flight line as free" said to be the changelog's "does not show a merged line as free" with "or in-flight" added, the changelog's words quoted without it (R3-4).
* Edge: every other line of the four records reads as before: Done when items stay ticked, each `commit` block unchanged and last, the PNGs untouched.
* Edge, the shared tree: the three sibling lines under `m32-review` may run in the same tree on other files; their files in `git status` are theirs, and this delivery stages only its paths and its own line of docs/06.
* Fails: a quoted text not found exactly once in its file; a line of the records added or removed; a `commit` block changed; an em dash; a chapter, a screenshot, docs/03, docs/05 or an ADR touched; any line of docs/06 changed but this line's mark.

**Contract.** Exact replacements, each found by its quoted text, counted once in its file when this page was written; each stays on its line, the rest of each file untouched. Line numbers as the files are at HEAD `33432ee`, unchanged since their commits.

`work/done/kit-2026-10-24.md`

1. (R2-7, :30) "bullet answers from docs/06 and work/ as `queue.sh` reads them; none." becomes "bullet answers from docs/06 and work/, and `queue.sh` reads docs/06, not work/; none."
2. (R2-7, :88) "\"Asked where things stand\" answers from docs/06 and work/ as `queue.sh` reads them; none." becomes "\"Asked where things stand\" answers from docs/06 and work/, and `queue.sh` reads docs/06, not work/; none."

`work/done/ch08-update-2026-10-24.md`

3. (R3-1, :121) "`2026.10.20.3` only at en 97 / pt 101." becomes "`2026.10.20.3` only at en 97 / pt 99."

`work/done/ch11-14-queue-tree.md`

4. (R3-2, :154) "the PDF shots are English page 152 and Portuguese page 161." becomes "the PDF shots are English page 152 and Portuguese page 161. The six shots were taken before the Delivery review's two fixes to chapter 14 (Divergences): all six show \"the same alias\" (\"o mesmo alias\"), now \"the same alias trick\" (\"o mesmo truque de alias\"), and the four site shots also show `m1-review`'s page \"takes every delivery of the milestone\" (\"toma cada entrega do marco\"), now taking the milestone's paragraph clause by clause; the glyph they prove is unchanged by those fixes."

`work/done/ch19-queue-branches.md`

5. (R3-3, :82) "It reverses decision 4 for that line and the Contract's fourth line in both blocks." becomes "It changes the Contract's fixture, whose `m2-review` line carried `(--)`, and the Contract's fourth line in both blocks; decision 4 is this line's own `(PA)` token and stays."
6. (R3-3, :86) "reversing decision 4 for that line only," becomes "changing the Contract's fixture for that line only, not decision 4,".
7. (R3-4, :101) "now the changelog's \"does not show a merged or in-flight line as free\";" becomes "now \"does not show a merged or in-flight line as free\", the changelog's \"does not show a merged line as free\" with \"or in-flight\" added;".

Sources: the installed `queue.sh` at `914fc75`, whose only file read is `docs/06-*.md` (:23-28) and never work/; AGENTS.md at `914fc75` :37; both chapter 8 files at `7d8a0e7`, en :97 and pt :99; the six PNGs opened, the English and Portuguese PDF shots ending at the code block, the site shots reaching `m1-review`'s sentence; `work/done/ch11-14-queue-tree.md` :159; `git log --all -S'm2-review (--)'` finding the token only in `ef990c3`, the page's own text, and decision 4 at :75 being the line's `(PA)`; focus-kit `51ff062:CHANGELOG.md`, entry 2026.10.24, "so a worktree's older copy does not show a merged line as free"; chapter 19 at `ef990c3` en :199.

Terms: record, Delivery review, Done when, queue tree, as docs/03 and docs/05 have them; no row added. No chapter, no case, no number, no code example.

**States.** Inapplicable: record pages, no screen.

**Visual reference.** Inapplicable: no screen, no chapter.

**Out of scope.**

* `work/done/m32-review.md`: it quotes the old strings as its findings, and stays as written.
* The six PNGs: not retaken; the record says what they show.
* Chapters 8, 14 and 19: the records describe them, the chapters stay; `ch14-key-points-pointers` and `ch19-example-marks` own their next changes.
* docs/03's `queue tree` row and ADR-0018: `queue-tree-row-source`.
* The records' other claims and their `commit` blocks: history, no rewrite.

**Decisions from the documents.**

* The findings and their cites: `work/done/m32-review.md`, R2-7, R3-1 to R3-4, and the line's bullet "`m32-records-claims`: R2-7, R3-1, R3-2, R3-3, R3-4, four records' precision".
* The form of each replacement, in place on its line: `m31-records-claims`, after `m29-records-claims`.
* `make book` with HEAD and `git status --short book/` in Proof, as `m31-records-claims` did, because sibling lines may have chapters uncommitted in the same tree.

**Decisions taken alone.** The agent chose each of these; the author corrects them in the review. This page was written and built by the agent before the author read it, on the author's word to run the queue.

* R3-3: :82, option 1 as the record describes it, is replaced in place rather than kept with a sentence after it, since it is the record's own description of the choice and the person's answer quoted at :86 is "Tirar (--)", which stays.
* R3-2: the sentence goes after "The glyph", the paragraph that names the shots, not into Divergences, where the fixes are; it names what each kind of shot shows, from the shots themselves.
* R2-7: both lines say what `queue.sh` reads, rather than dropping the clause, since the reader of the record wants to know the script does not read work/.
* The queue line keeps its wording.

**Done when.**

* [x] Each quoted text counted once in its file before any edit; the seven replacements made word for word.
* [x] `git diff --numstat` of the four records shows only those lines changed, none added or removed: `kit-2026-10-24` :30, :88; `ch08-update-2026-10-24` :121; `ch11-14-queue-tree` :154; `ch19-queue-branches` :82, :86, :101; and docs/06's hunk this line's mark alone.
* [x] Each record's last fenced block is `commit`, unchanged, and nothing follows it; no em dash; no Done when item of a record unticked.
* [x] `make verify` green after the last edit, its time in Proof.
* [x] `make book` exit 0, Proof naming HEAD, `git status --short book/` and both PDF paths.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says, over `git diff HEAD` of the four records and this page, with this line's hunk of docs/06, against this page and docs/04; what it read and what it says of the advisor recorded.
* [x] Staged: this page moved to `work/done/`, the four records and this line's hunk of docs/06, nothing else.

## Outcome

**Built.** The seven replacements of the Contract, each old text counted once in its file, on the line the Contract names, before any edit, and replaced word for word by the Edit tool. docs/06: this line's mark alone.

**Divergences.** After the review, Behaviour's third bullet read "now taking the milestone's paragraph", the Contract's words, where it had paraphrased them; nothing in the records changed for it.

**Decisions taken by /apply.** The agent chose each of these.

* The review's note that the record quotes "takes every delivery of the milestone" while the site shots go on ", clause by clause" is left: the quote is what changed, and the shots hold the rest.
* `make book` ran once, after the first verify and before the review; the later edits touch only this page and docs/06's mark, nothing in `book/`.

**Delivery review.** One read-only Opus agent (an Explore agent with model opus), launched by this /apply, over `git diff HEAD` of the four records and this line's hunk of docs/06, both written to files, and this page, against this page and docs/04. It read this page whole, both diffs, docs/04 :12-115 and its headings, `work/done/m32-review.md` :177-181 and :191, the records' hunks and last 12 lines, `ch19-queue-branches` :70-78, `ch11-14-queue-tree` :156-166, `queue.sh` and AGENTS.md at `914fc75`, chapter 8 at `7d8a0e7` by grep, chapter 19 en :199 and the record's diff at `ef990c3`, the kit's `51ff062:CHANGELOG.md` :20-25, docs/06 :722 and the six PNGs as images. It found nothing blocking; its candidates: Behaviour's paraphrase (fixed, Divergences), the shorter quote of the site shots (Decisions taken by /apply), the fixture's `(--)` resting on the record's own :79 quote, which Sources names, and several sentences on one page line, as other records have. It says it did not consult an advisor tool, which docs/05 §5 asks it to keep.

**Proof.**

* Each of the seven old texts counted 1 in its file, at kit-2026-10-24 :30, :88; ch08-update-2026-10-24 :121; ch11-14-queue-tree :154; ch19-queue-branches :82, :86, :101 (a script over the four files).
* `git diff --numstat`: kit-2026-10-24 2 and 2, ch08-update-2026-10-24 1 and 1, ch11-14-queue-tree 1 and 1, ch19-queue-branches 3 and 3, hunks at those lines alone; docs/06 1 and 1, :722's mark.
* `make verify` exit 0 in 14 seconds after the seven replacements; `make book` exit 0 right after it, on HEAD `33432ee`, `git status --short book/` empty before and after: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* `make verify` exit 0 in 11 seconds after the review's fix, this page's move to `work/done/` and the line's `[x]`; and exit 0 once more after this bullet took that result, the last edit.

```commit
docs(m32-records-claims): make four M32 records hold what happened

- kit-2026-10-24: queue.sh reads docs/06, not work/
- ch08-update-2026-10-24: 2026.10.20.3 at pt 99
- ch11-14-queue-tree: the shots predate chapter 14's review fixes
- ch19-queue-branches: the fixture's token, the changelog's own words

work/done/m32-records-claims.md
```
