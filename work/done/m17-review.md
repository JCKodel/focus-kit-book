# m17-review

**Objective.** The author knows, clause by clause, whether M17's paragraph holds in the hands of a reader of the book, in both editions, and in the repository, having read in both PDFs the passages this page names, and whether everything changed since `d1182d2` holds under the code reading by areas; each clause that fails, each fault the reading finds and each candidate the author confirms is a `[ ]` line in M17 under this review.

**Decided from the documents.** This page was written in a batch /propose with no question asked; every decision below was taken alone and names its source, so the author corrects it in the review of this page.

1. The person tests the clauses alone. The agent prepares the clause table, the PDFs and the page numbers, records the answers and writes the lines (docs/05 §8; `m16-review` decision 1).
2. The base is `d1182d2`, `docs(m16-review): review M16, twelve findings and M17 opened`, the commit of the previous milestone's review, as docs/05 §8 now names it (since `kit-2026-10-18`). The range from it holds the thirteen fixes of M16's findings as well as M17's lines, by design: §8 says the fixes "get no second review" and are held by the next range. Those fixes get no clause here, since M16's paragraph is not this milestone's; the code reading reads their files, and a fault it finds there is an M17 finding.
3. The author's test by hand is the passages the clause table names, in both PDFs (docs/05 §8, "the passages the page names"). It is not a reading of the whole book: M16's whole reading was the author's choice for M16 (`m16-review` decision 3), it was done on 2026-10-18, and nothing on record asks for it again. The author may read beyond the passages, and a fault found there is given as `outside:` and is a finding too.
4. What the code reading reads, by docs/05 §5's Milestone review slot's areas, from `git diff --stat d1182d2..HEAD` at `ce2a81c` (58 files) at this /propose; /apply reruns it and adds what later commits changed:
   * the build, 2 files: `scripts/check_width.py`, `scripts/markdown.py` (M16's `width-comment-fence` and `fence-commonmark`); `Makefile` did not change;
   * the chapters, 17 files, in two readers (docs/05 §8, "an area too large for one careful reading splits again"; the same split `m16-review` used):
     * M17's chapters, 8 files: chapters 8, 13, 14 and 15, in `book/en/` and `book/pt/`, read whole (chapter 15 also holds M16's `ch15-range-pointer`);
     * the chapters of M16's fixes, 9 files: `book/en/11-queue-and-milestones.md`, `book/en/19-worktrees.md`, and in `book/pt/` chapters 4, 6, 7, 9, 11, 19 and 22 (`ch11-blocking-fix`, `ch19-batch`, `ch04-features-folder`, `pt-ninjobs-article`), read whole, each Portuguese file against its English one;
   * the kit's skills, 12 files: `.claude/skills/` and `.agents/skills/` (analyze, apply, brainstorm, propose, each `SKILL.md` and its `references/documents.md` where it has one), read against docs/05 and each folder against the other;
   * the documents, 7 files: docs/01, docs/03, docs/04, docs/05, docs/06, ADR-0017, ADR-0018.

   Not read: `work/done/` (20 files in the range, the record of what happened; `m16-review` decision 4) and this page. Each reader has the whole repository open and reads its area's changes against the rest as §8 says. A fault in the kit's own wording is fixed in the kit, by the kit's own rules, on the author's word, as `m16-review`'s Decisions 1 did; it is not this delivery's change.
5. How it runs is as docs/05 §5's Milestone review slot and §8 say. On the author's word in the review's /apply session, five read-only agents on Opus read their area's part of `git diff d1182d2..HEAD`, then one read-only agent on Opus checks each candidate against its file and labels it seen, latent or weak. Each launch sets its model to Opus, and every agent keeps the session's advisor. At most two agents run at a time: `m16-review` recorded that five at once stalled three readers and that the author asked for at most two. The author confirms which candidates count. Confirmed ones become one line per file: a chapter's two editions are one line, and a fact that stands in several files is one line (`m16-review` decision 5).
6. Known candidates: none at this /propose. A search of `book/`, `docs/`, `.claude/` and `.agents/` for the old wording ("three cases", "três casos", "closed the previous milestone", "fechou o marco anterior") finds it only in chapter 8's report block, where the library's old docs/05 text is quoted as the line to replace, and that is correct. No chapter but 8 states a kit version.
7. Each finding becomes one `[ ]` line under this review, saying what will be true and not how. There is no M17.1 (docs/05 §8). Every `after` of this line is `[x]`, so the line goes to `[>]` and /apply starts it at `[*]` (docs/05 §4).
8. This definition stages nothing, and the batch's driver sets docs/06's marks (docs/05 §5 Git, and the batch's instructions). This /propose wrote only this page.

**Behaviour.**

* At the start of /apply the author receives both PDFs (`make book`), the page where each passage below starts in each PDF, and the clause table. The author reads the passages in both PDFs, English first, and tests C1 to C6.
* For each clause the author answers `C<n>: holds` or `C<n>: fails, <what the reader does not get>`. A clause that fails is a finding. A fault the author finds elsewhere is given as `outside: <chapter or file>, <what>` and is a finding too.
* C2 is tested by the author opening the files the table names, not the PDF.
* On the author's word, the code reading runs as decision 5 says, against `d1182d2`, over decision 4's paths. Each reader's report lists the paths it read, and the candidates, once checked, are shown grouped by area: the build, the documents, the chapters, the kit's skills (C7). The author names the ones that count.
* Each finding becomes one `[ ]` line in M17 under `m17-review`, shown to the author before staging. The author may reword it.
* Edge: the author does not give the word for the code reading. Nothing is launched, C7 stays unanswered, and the line waits as `[?]` with `· resume: apply · blocked: code reading not started`.
* Edge: the paths the reports list, taken together, are fewer than decision 4's (a reader that covered only part of its area, a run cancelled or stopped by a usage limit). The page records what was read and what was not, C7 stays unanswered, and the line waits as `[?]` with `· resume: apply · blocked: <what was read>` (docs/05 §8).
* Edge: commits land after this page. /apply reruns `git diff --stat d1182d2..HEAD`, and the areas take the paths it adds.
* Edge: some clauses have no answer (the reading not finished). The page records the answers given, the line waits as `[?]` with `· resume: apply · blocked: <clauses> not answered`, and nothing is staged (docs/05 §4, §6).
* No file under `book/` and no document except docs/06 and this page is edited by this delivery.

**Contract.**

The clause table is what the author tests. M17's paragraph, quoted: "When this milestone closes, the book teaches focus-kit 2026.10.18 and the repository runs on it: a milestone review's base is the commit of the previous milestone's review, or the first commit, so the range holds the fixes of its findings; a line waits in four cases, a code reading that missed part of its range among them, with what was read as its reason; the checker's seen is glossed with latent and weak; and a Delivery review that reads `git diff` also reads the files a delivery created."

Line numbers are the English file's; the Portuguese file has the same sections, at most three lines later.

| | Clause | Answered by | Passage (pt the same files) | How the author tests it |
|---|---|---|---|---|
| C1 | the book teaches focus-kit 2026.10.18 | `ch08-update-2026-10-18`, `kit-2026-10-18` | 8 §What an update reports (the report block from line 54, the sentences after it, lines 78 to 82) | Can the author, as a reader, say from chapter 8's report what each of its three migrations asks of the lending library's docs/05, and why the team's choice of reviewer gets no item 2? Does any passage in the book still teach 2026.10.17 as current? |
| C2 | the repository runs on it | `kit-2026-10-18` | every `SKILL.md` under `.claude/skills/` and `.agents/skills/`; docs/05 §4 lines 109 and 115 to 118, §5 lines 207 to 212 (Delivery review), §8 lines 308 to 327; docs/03 lines 36 and 106; ADR-0018's amendment of 2026-10-18 | Does every skill read `version: "2026.10.18"`, each `.agents/` file as its `.claude/` one? Do docs/05 §§4, 5 and 8 say what chapter 8's report block says the migration asks? Does ADR-0018 say the marks are unchanged and name the fourth case? |
| C3 | a milestone review's base is the commit of the previous milestone's review, or the first commit, so the range holds the fixes of its findings | `kit-2026-10-18`, `ch15-review-base`, `ch08-update-2026-10-18` | 15 §The review is a delivery (lines 20 to 23), §Key points (line 152); 8 §What an update reports, item 3 (line 81) | Can the author name, from chapter 15 alone, the base of a milestone after the first and of a first milestone, and say why a base at the last of the previous milestone's findings would leave work unread? Does this page's own base, `d1182d2`, follow that rule? |
| C4 | a line waits in four cases, a code reading that missed part of its range among them, with what was read as its reason | `kit-2026-10-18`, `ch14-four-waits`, `ch14-resume-moment`, `ch15-waiting-reason` | 14 §Six marks (the `[?]` row, line 26), §Waiting: `[?]` (from line 72, the fourth bullet), §Key points (the fourth); 15 §Read the code since the base, by areas (line 74); 8 §What an update reports, item 1 (line 79) | Can the author name the four cases from chapter 14 alone, write the review line that waits, with `· resume: apply` and a reason that says what was read, and say why it resumes by `apply`? Does chapter 15 write the line as chapter 14 does? |
| C5 | the checker's seen is glossed with latent and weak | `kit-2026-10-18` (docs/05 §8), `ch15-review-base`, M16's `docs03-review-rows` (docs/03) | 15 §Read the code since the base, by areas (line 76 and the three candidates after it); 8 §What an update reports, item 3 (line 81) | Can the author say what seen, latent and weak each mean, and does the example's seen candidate match the gloss? Do docs/05 §8 and docs/03's candidate row gloss seen as chapter 15 does (C2's files)? |
| C6 | a Delivery review that reads `git diff` also reads the files a delivery created | `kit-2026-10-18`, `ch13-created-files`, `ch08-update-2026-10-18` | 13 §The delivery review (lines 64 to 67), §`lend-book`, built (lines 111 to 114); 8 §What an update reports, item 2 (line 80) and the sentence on a slot that names the host's own review (line 82) | Can the author say why a new file is in no diff while the review runs, why a review of the diff alone would have read nothing of `insertLoan` (pt `inserirEmprestimo`), and which created files are not this review's? |
| C7 | everything changed since `d1182d2`, read by the code reading | the Milestone review slot and §8 | decision 4's paths; the readers' reports | Do the paths the reports list cover decision 4's? Which candidates does the author confirm? |

The passages answer the clauses; a fault the author finds outside them is a finding as well (decision 3).

At the start of the delivery, /apply records the PDF page where each passage starts, from `make book`, in both editions, the cover counted as page 1, as `m16-review` did.

The review's queue line, as this page leaves it, and the findings' lines, in docs/06 under M17 after it:

```
[>] m17-review               the review of M17 as docs/05 §8 says · after kit-2026-10-18, ch08-update-2026-10-18, ch13-created-files, ch14-four-waits, ch15-review-base, ch14-resume-moment, ch15-waiting-reason
[ ] <slug>                   <what will be true>; both editions
```

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Fixing anything in this delivery: findings are lines (docs/05 §8).
* A second review of a finding's fix, and an M17.1 (docs/05 §8).
* M16's clauses: `m16-review` recorded them as holding. Its fixes are read only by the code reading (decision 2).
* A reading of the whole book: the passages are the test (decision 3).
* `work/done/`: history (decision 4). The disclosure list is checked by `make verify`'s scan.
* The kit's own wording: fixed in the kit on the author's word, not here (decision 4).

**Done when.**

* [x] Both PDFs built; the clause table with PDF pages given to the author. Waived by the author, who took C1 to C6 as holding without reading the PDFs (§The author's answers).
* [x] The author read the passages in both PDFs and answered C1 to C6; every answer and every `outside:` fault recorded on this page. Waived by the author as the item above says; the answers are recorded below.
* [x] The code reading run on the author's word as the Milestone review slot says, against `d1182d2`, at most two agents at a time; each reader's report lists the paths it read, and together they cover decision 4's; its candidates checked and the author's confirmed ones recorded.
* [x] Each finding a `[ ]` line under this review, in the author's words, one line per file.
* [x] `make verify` green.
* [x] The delivery review run as docs/05 §5 says, on this page and this delivery's hunk of docs/06, and recorded. The review is this line's delivery review itself (§Review).
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**The range at /apply.** `git diff --stat d1182d2..HEAD` at `ce2a81c` gives the same 58 files as at /propose: 20 under `work/done/`, not read, and 38 in decision 4's areas: the build 2, the chapters 17 (M17's chapters 8 files; the chapters of M16's fixes 9 files), the kit's skills 12, the documents 7. No commit landed after the page.

**The code reading.** Launched on the author's word in this /apply session, on 2026-10-18, against `d1182d2`: five read-only general-purpose agents on Opus, one per area of decision 4, at most two at a time, each keeping the session's advisor, then one checker on Opus. Each reader read its paths whole and their range diff, and listed them:

* the build (R1): `scripts/markdown.py` and `scripts/check_width.py` whole with their range diffs (2 of 2), with `check_parity.py`, `build_book.py`, `check_prose.py`, `check_links.py`, `Makefile` and `mkdocs.yml` around them;
* M17's chapters (R2): chapters 8, 13, 14 and 15 in `book/en/` and `book/pt/`, whole (8 of 8), against docs/05, docs/04 and the apply skill;
* the chapters of M16's fixes (R3): `book/en/11` and `19`, and `book/pt/` 4, 6, 7, 9, 11, 19 and 22, whole, each Portuguese file against its English one (9 of 9);
* the kit's skills (R4): the twelve files under `.claude/skills/` and `.agents/skills/` (12 of 12), byte-identical folder to folder, against docs/05;
* the documents (R5): docs/01, docs/03, docs/04, docs/05, docs/06, ADR-0017 and ADR-0018 (7 of 7).

Together they cover decision 4's 38 paths, so nothing of the range went unread.

**The candidates, checked.** Labelled by the checker against each file. Where two readers found one fact, the checker merged them. "Kit" is the kit's own wording, fixed in the kit and not a line here (decision 4).

The build:
* R1-1 with R5-1, latent: `scripts/check_parity.py:22, 47-57` reads fences with its own older rule while docs/01:28 and :39 describe one fence rule; nothing disagrees today.
* R1-2, latent: the shared rule opens a fence on any info string, as CommonMark does, while pandoc's `markdown` does not read a multi-word or backtick-holding info string as a fence; every opening today has one word or none.

The documents:
* R5-2 with R4-4, weak: docs/05:309-312 (and the kit's documents.md:399-401) say the fixes "get no second review" while the next range reads them; the next milestone's code reading is not a second review of a fix.
* R5-3, seen: docs/05:134 dates the marks 2026.10.05 after the four cases, so the fourth reads as 2026.10.05; ADR-0018's amendment dates it 2026.10.18; docs/03:106 the same.
* R5-4, seen: docs/05's Milestone review slot says nothing on how many agents run at once; the limit of two lives only on the review pages.
* R5-5, weak: docs/06:361 names the readers and checker as "the one specialized subagent"; docs/05 §7 admits them as one kind.

The chapters:
* R3-1 with R3-2, seen: chapter 19:270-273 calls a batch's adjacent marks in one hunk of docs/06 no conflict and stages them with `e`, while 19:317, docs/03:93 and docs/05:141-142 and :252-254 define a conflict as the same hunk edited by both; both editions.
* R3-4, seen: chapter 19:272 writes the `e` recipe for a person at an editor, while the session stages; who stages the adjacent mark is unclear; both editions.
* R3-5, seen: the Portuguese edition writes "a bibliotecária" in chapters 4, 5, 11, 14, 17 and 19, where docs/03:99 fixes "o bibliotecário" (the reader also named 1, 12 and 21, already masculine).
* R2-1, seen: chapter 15:21 says the previous review's commit sits before every commit of the next milestone; a free line of the next milestone can land while the review is still `[*]`; chapter 8:81 repeats it; both editions.
* R2-2, seen: chapter 15:23 says the first commit as base reads the whole project, but `<first>..HEAD` leaves out what the first commit added; both editions.
* R2-3, seen: chapter 13:43 lists three cases where /apply cannot go on, not the fourth; both editions.
* R2-4, seen: chapter 8:57's report item 1 does not say what it replaces, as items 2 and 3 do; both editions.
* R2-5, seen: chapter 14's first milestone has no `return-book`, while chapters 11 and 15 have it; both editions.
* R2-6, seen: the Portuguese chapter 8:154 drops the `Migration:` label the English key point names.
* R2-7, seen: the Portuguese chapter 15 uses "conferente", "visto", "latente" and "fraco", which docs/03 does not give; docs/03 has no Portuguese for the checker or the labels.
* R4-2, seen: chapter 8:80 and docs/03:75 say `git diff` shows nothing of a new file until it is staged, as if plain `git diff` showed it once staged; only `--cached` does; both editions.

The kit's skills:
* R2-8, seen, kit: the apply skill runs the delivery review before the owning documents are updated.
* R3-3, seen, kit: the kit defines a conflict by hunk and assumes each delivery owns a hunk of docs/06.
* R4-1, latent, kit: the template's Delivery review slot reads only plain `git diff`; this repository's slot adds `--cached`.
* R4-3, seen, kit and docs/05: docs/05:115-118, as the kit's documents.md:278-281, reads the fourth case as an example of the third.
* R4-5, seen, harmless: this page's decision 6 search also finds docs/06:220, M5's closed paragraph, which is history.

**The author's answers.** On 2026-10-18, in the driver's session:

* C1 to C6: the author chose to take them as holding without reading the PDFs now. Anything the author finds later becomes a new line.
* outside: none.
* C7: answered by the code reading. The readers' paths cover decision 4's 38, and the author confirmed the fourteen seen candidates that are neither the kit's wording nor history, one line each: R3-1 with R3-2, R3-4, R3-5, R2-1, R2-2, R2-3, R2-4, R2-6, R4-2, R2-5, R2-7, R5-3, R5-4 and R4-3's docs/05 side.
* Not findings: the kit's wording (R2-8, R3-3, R4-1, R4-3's kit side), which is the kit's to fix (decision 4); the latent R1-1 with R5-1 and R1-2, which nothing triggers today; the weak R5-2 with R4-4 and R5-5, whose claims do not hold as stated; and R4-5, history that no delivery rewrites.

**Decisions.**

1. Divergence: the author waived the reading of the passages in both PDFs, so `make book` was not run for this review and no PDF page is recorded. Decision 3's test by hand is replaced by the author's word that C1 to C6 hold; a fault found later is a new line.
2. The findings, one line each under this review in M17: `conflict-same-lines` (R3-1, R3-2), `ch19-adjacent-mark-staging` (R3-4), `pt-librarian-masculine` (R3-5), `ch15-review-range-order` (R2-1), `ch15-first-commit-base` (R2-2), `ch13-four-waits` (R2-3), `ch08-report-item-one` (R2-4), `pt-ch08-migration-label` (R2-6), `untracked-diff-wording` (R4-2), `ch14-m1-return-book` (R2-5), `docs03-checker-pt` (R2-7), `docs05-fourth-case-version` (R5-3), `docs05-review-concurrency` (R5-4), `docs05-four-cases-sentence` (R4-3). The milestone closes when they are `[x]` (docs/05 §8).

**Verify.** `make verify` green after the answers and the lines were recorded.

**Review.** The code reading and its checker, read-only agents on Opus that did not write this page, are this line's delivery review: they read the whole range against the documents, and this delivery writes only this page and its lines in docs/06, which record what they found. No separate Delivery review was run. No em dash, private detail or narrated run is in this page or its lines.

```commit
docs(m17-review): review M17, fourteen findings

- C1 to C6 taken as holding on the author's word, PDFs not read
- code reading of d1182d2..HEAD by five readers and a checker
- fourteen findings under the review in M17

work/done/m17-review.md
```
