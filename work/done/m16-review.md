# m16-review

**Objective.** The author knows, clause by clause, whether M16's paragraph holds in the hands of a reader of the book, in both editions, and in the repository, having read the whole book in both PDFs, and whether everything changed since `3b728ae` holds under the code reading by areas; each clause that fails, each fault the whole reading finds and each candidate the author confirms is a `[ ]` line in M16 under this review.

**Decided from the documents.**

1. The person tests the clauses alone. The agent prepares the clause table, the PDFs and the page numbers, records the answers and writes the lines (docs/05 §8; `m15-review` decision 1).
2. The base is `3b728ae`, the commit of `m15-review`, which is the parent of M16's first commit, `3bcef84` (`kit-2026-10-17`). The author chose it in this /propose. M16's commits are interleaved with the fixes of M15's 24 findings, which ran until `f0187aa`. The range `f0187aa..HEAD` would leave out the kit's reinstall, the delivery M16 stands on: its migration of docs/03, docs/05 and the skills, and the removal of `.windsurf/skills/`. The range from `3b728ae` holds everything no review has read since M15's review read the whole repository from `3ca06b1`, M15's fixes included. That is where docs/05 §8 says what a fix missed is found: "They get no second review", and the next milestone's review reads the whole. docs/05 §8 names "the commit that closed the previous milestone, or the first commit", and neither name fits a milestone whose first line started before the previous one's findings closed. That gap is the first known candidate for the documents' reader (decision 6).
3. The author's test by hand is a reading of the whole book, both PDFs entire, as the author said at M15's close ("they will read the whole book, both editions, at the end of M16", `m15-review` §The author's answers). The author chose it in this /propose. The clause table names the passages that answer each clause. A fault the reading finds outside them is a finding of M16 as well. M15's C1 count, five chapters against nine with or without the prologue, which M15 left to this reading, is clause C8 here.
4. What the code reading reads, by docs/05 §5's Milestone review slot's areas, from `git diff --stat 3b728ae..HEAD` (111 files) at this /propose; /apply reruns it and adds what later commits changed:
   * the build: `Makefile`, `scripts/check_disclosure.py`, `scripts/check_width.py`, `scripts/markdown.py`;
   * the chapters, in two readers because 46 files are too many for one careful reading (docs/05 §8, "an area too large for one careful reading splits again"; M15 recorded the same split as a divergence because its page had said one reader): chapters 1 and 3 to 11, and chapters 12 to 24, each in `book/en/` and `book/pt/`, read whole;
   * the kit's skills: `.claude/skills/` and `.agents/skills/` (analyze, apply, brainstorm, propose, each `SKILL.md` and its `references/documents.md` where it has one), and the deletion of `.windsurf/skills/`, read against docs/05 and against each other;
   * the documents: docs/01, docs/03, docs/04, docs/05, docs/06, ADR-0017, ADR-0018.

   Not read: `work/done/` (36 files in the range, the record of what happened, which a later delivery does not rewrite; `m15-review` decision 3) and this page. Each reader has the whole repository open and reads its area's changes against the rest as §8 says: one delivery's work against another's, a document against another, the whole against docs/01. A fault in the kit's own wording is a note for the kit, not a line (`m15-review` decision 3).
5. How it runs is as docs/05 §5's Milestone review slot and §8 say. On the author's word in the review's /apply session, five read-only agents on Opus read their area's part of `git diff 3b728ae..HEAD`. One more read-only agent on Opus checks each candidate against its file and labels it "seen", "latent" (nothing triggers it today) or "weak" (the claim does not hold as stated), and "covered by M16" when an open M16 line plans it, as `m15-review` did. Each launch sets its model to Opus, and every agent keeps the session's advisor. The author confirms which candidates count. Confirmed ones become one line per file: a chapter's two editions are one line, and a fact that stands in several files is one line (`m15-review` decision 5).
6. Known candidates, which open the list before the review runs: docs/05 §8's base names no commit for a milestone that started before the previous one's findings closed (decision 2); and chapter 15 §The review is a delivery, line 20, teaches the same two names.
7. Each finding becomes one `[ ]` line under this review, saying what will be true and not how. There is no M16.1 (docs/05 §8). Every `after` of this line is `[x]`, so the line goes to `[>]` and /apply starts it at `[*]` (docs/05 §4).

**Behaviour.**

* At the start of /apply the author receives both PDFs (`make book`), the page where each passage below starts in each PDF, and the clause table. The author reads both PDFs entire, English first, and tests C1 to C8.
* For each clause the author answers `C<n>: holds` or `C<n>: fails, <what the reader does not get>`. A clause that fails is a finding. A fault the author finds elsewhere in the reading is given as `outside: <chapter>, <what>` and is a finding too.
* C7 is tested by the author opening the files the table names, not the PDF.
* On the author's word, the code reading runs as decision 5 says, against `3b728ae`, over decision 4's paths. Each reader's report lists the paths it read, and the candidates, once checked, are shown grouped by area: the build, the documents, the chapters, the kit's skills (C9). The author names the ones that count.
* Each finding becomes one `[ ]` line in M16 under `m16-review`, shown to the author before staging. The author may reword it.
* Edge: the author does not give the word for the code reading. Nothing is launched, C9 stays unanswered, and the line waits as `[?]` with `· resume: apply · blocked: code reading not started`.
* Edge: the paths the reports list, taken together, are fewer than decision 4's (a reader that covered only part of its area, a run cancelled or stopped by a usage limit). The page records what was read and what was not, C9 stays unanswered, and the line waits as `[?]` with `· resume: apply · blocked: code reading read <what it read>, not the range` (docs/05 §8).
* Edge: commits land after this page. /apply reruns `git diff --stat 3b728ae..HEAD`, and the areas take the paths it adds.
* Edge: some clauses have no answer (the reading not finished). The page records the answers given, the line waits as `[?]` with `· resume: apply · blocked: <clauses> not answered`, and nothing is staged (docs/05 §4, §6).
* No file under `book/` and no document except docs/06 and this page is edited by this delivery.

**Contract.**

The clause table is what the author tests. M16's paragraph, quoted: "When this milestone closes, the book teaches focus-kit 2026.10.17 and the repository runs on it: `/apply` having each delivery's own changes reviewed by a context that did not write them, with the host's own review where the agent can run it and keep it to the delivery's paths, else a read-only agent, fixing what breaks the page before it ends; a milestone review whose code reading is the kit's own and runs in any host that runs agents, over `git diff <base>..HEAD` and never a bare commit, split into the Milestone review slot's areas with one read-only agent each, every reader listing the paths it read and the line waiting as `[?]` when they miss part of the range, a checker marking every candidate seen, latent or weak before the person sees it, the review started on the person's word because it costs, and the reviews' readers as the one specialized subagent the governor admits; Devin Desktop, formerly Windsurf, reading the commands from `.agents/skills/` and invoking them as `/<name>`; and a reader who runs `/propose` in a batch knows what each page must say about the answers chosen without them, and why the commit stays theirs when applies run in parallel."

| | Clause | Answered by | Passage (pt the same files) | How the author tests it |
|---|---|---|---|---|
| C1 | the book teaches focus-kit 2026.10.17 | `ch08-09-review-slot`, `kit-2026-10-17` | 8 §What an update reports; 9 §`/brainstorm`: a new project (lines 27 and 28) and §`/analyze`: an existing project (questions 5 and 6) | Can the author, as a reader, say from chapter 8's report what each of its four migrations asks of docs/05, and answer chapter 9's two questions on review for a new project? Does any passage in the book still teach 2026.10.16.2 as current? |
| C2 | `/apply` has each delivery's own changes reviewed by a context that did not write them, the host's own review where it can be kept to the paths, else a read-only agent, and fixes what breaks the page before it ends | `ch13-delivery-review`, `ch07-11-23-review-words` | 13 §What `/apply` does (from "With verify green and the proof done"), §`lend-book`, built, §What the team gains; 7 §The seven documents (the ten slots) | Can the author say why the session that built a change does not review it, which reviewer is used when, what it fixes and what becomes a `[ ]` line? Does chapter 7 count ten slots, the Delivery review among them? |
| C3 | the milestone review's code reading, the kit's own, in any host that runs agents, over `git diff <base>..HEAD` and never a bare commit, by the slot's areas with one read-only agent each, the paths read and `[?]` when they miss part of the range, a checker labelling every candidate seen, latent or weak, started on the person's word | `ch15-review-by-areas`, `ch07-11-23-review-words` | 15 §The review is a delivery, §Read the code since the base, by areas, §Key points; 11 §Milestones (line 85); 23 §Roles in a team (line 64) | Can the author run the reading from chapter 15 alone, in a host with agents and in one without, and say why a bare commit reads too little? Do chapters 7, 11 and 23 say it as chapter 15 does, with no review launched by hand? |
| C4 | the reviews' readers are the one specialized subagent the governor admits | `ch16-review-agents` | 16 §What the process does not have, §The subagent it admits, §The error that earned a mark | Can the author say what a specialized subagent is, why the readers and the checker are admitted and nothing else, and which error stands behind them? |
| C5 | Devin Desktop, formerly Windsurf, reads the commands from `.agents/skills/` and invokes them as `/<name>` | `ch08-10-devin-desktop`, `kit-2026-10-17` | 8 §How each host finds the commands; 10 §Before you start (the hosts table); docs/03's `host` row | Can a Devin Desktop user find in chapter 8 where the commands live, how to invoke one and why `.windsurf/skills/` holds none, and in chapter 10 the command to type? |
| C6 | a reader who runs `/propose` in a batch knows what each page must say about the answers chosen without them, and why the commit stays theirs when applies run in parallel | `batch-propose` | 19 §Proposing in a batch, §When parallel stops paying | Can the author run a batch from chapter 19 alone, say where on each page the questions answered alone are, which question stays waiting, and why applies stay parallel only on free lines and each commit stays the person's? |
| C7 | the repository runs on 2026.10.17 | `kit-2026-10-17`, `docs05-review-checker` | every `SKILL.md` under `.claude/skills/` and `.agents/skills/`; `.windsurf/`; docs/05 §5's Delivery review and Milestone review slots, §7 and §8; the Review records of M16's pages in `work/done/` | Does every skill read `version: "2026.10.17"`? Is `.windsurf/` absent? Do docs/05's two slots, §7 and §8 say what chapter 8's report block says the migration asks? Does every M16 page after `kit-2026-10-17` record its delivery review? |
| C8 | M15's C1, left to this reading: a reader reaches the method in five chapters instead of nine | `m15-review` (C1, its answer deferred) | the contents page of each PDF; the prologue §What the team gains (the five parts); 6, How focus-kit was born; 7, The documents (Part II begins) | Which count does the author take, with or without the prologue, and does it give five against nine (`m15-review` C1's test, both counts)? |
| C9 | everything changed since `3b728ae`, read by the code reading | the Milestone review slot and §8 | decision 4's paths; the readers' reports | Do the paths the reports list cover decision 4's? Which candidates does the author confirm? |

The whole reading of both PDFs (decision 3) covers every chapter, and a fault it finds outside these passages is a finding.

At the start of the delivery, /apply records the PDF page where each passage starts, from `make book`, in both editions, the cover counted as page 1, as `m15-review` did.

The review's queue line, as this page leaves it, and the findings' lines, in docs/06 under M16 after it:

```
[>] m16-review               the review of M16 as docs/05 §8 says · after ch13-delivery-review, ch15-review-by-areas, batch-propose, ch08-10-devin-desktop, ch08-09-review-slot, ch07-11-23-review-words
[ ] <slug>                   <what will be true>; both editions
```

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Fixing anything in this delivery: findings are lines (docs/05 §8).
* A second review of a finding's fix, and an M16.1 (docs/05 §8).
* M15's clauses other than C1's deferred count: `m15-review` recorded them as holding.
* `work/done/`: history (decision 4). The disclosure list is checked by `make verify`'s scan.
* Changing docs/05 §8's base wording here: decision 6 makes it a candidate, and confirmed, a line.

**Done when.**

* [x] Both PDFs built; the clause table with PDF pages given to the author.
* [x] The author read both PDFs entire and answered C1 to C8; every answer and every `outside:` fault recorded on this page.
* [x] The code reading run on the author's word as the Milestone review slot says, against `3b728ae`; each reader's report lists the paths it read, and together they cover decision 4's; its candidates checked and the author's confirmed ones recorded.
* [x] Each finding a `[ ]` line under this review, in the author's words, one line per file; three answered in M17 instead (decision 2's divergence).
* [x] `make verify` green.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Where each passage starts.** From `make book` at the start of the delivery, on 2026-10-18: `output/one-page-at-a-time.pdf` (en, 195 pages) and `output/uma-pagina-de-cada-vez.pdf` (pt, 204 pages), PDF page numbers, the cover counted as page 1, which is the folio the contents page prints.

| Clause | Passage | en | pt |
|---|---|---|---|
| C1 | 8 §What an update reports | 69 | 72 |
| C1 | 9 §`/brainstorm`: a new project, lines 27 and 28 | 77 | 81 |
| C1 | 9 §`/analyze`: an existing project | 79 | 83 |
| C1 | 9, questions 5 and 6 | 80 | 84 |
| C2 | 13 §What `/apply` does | 107 | 112 |
| C2 | 13, "With verify green and the proof done" | 108 | 114 |
| C2 | 13 §`lend-book`, built | 110 | 116 |
| C2 | 13 §What the team gains | 115 | 121 |
| C2 | 7 §The seven documents | 60 | 62 |
| C3 | 15 §The review is a delivery (line 20 there too) | 125 | 131 |
| C3 | 15 §Read the code since the base, by areas | 126 | 132 |
| C3 | 15 §Key points | 130 | 136 |
| C3 | 11 §The review, and its findings (line 85) | 93 | 99 |
| C3 | 23 §Roles in a team (line 64) | 185 | 194 |
| C4 | 16 §What the process does not have | 133 | 140 |
| C4 | 16 §The subagent it admits | 134 | 141 |
| C4 | 16 §The error that earned a mark | 135 | 142 |
| C5 | 8 §How each host finds the commands | 72 | 75 |
| C5 | 10 §Before you start (the hosts table) | 84 | 89 |
| C6 | 19 §Proposing in a batch | 162 | 171 |
| C6 | 19 §When parallel stops paying | 164 | 173 |
| C8 | the contents page | 4 | 4 |
| C8 | the prologue | 5 | 5 |
| C8 | the prologue §What the team gains | 9 | 9 |
| C8 | 1, How an agent sees your project | 11 | 11 |
| C8 | 6, How focus-kit was born | 55 | 57 |
| C8 | 7, The documents (Part II begins) | 59 | 61 |

**What C7 opens.** Every `SKILL.md` under `.claude/skills/` and `.agents/skills/` (four each: analyze, apply, brainstorm, propose); `.windsurf/`; docs/05 lines 206 to 211 (Delivery review), 230 to 236 (Milestone review), §7 from line 287 and §8 from line 296; chapter 8 §What an update reports for the report block; and the Review records of `ch13-delivery-review`, `ch15-review-by-areas`, `ch07-11-23-review-words`, `ch16-review-agents`, `batch-propose`, `ch08-10-devin-desktop` and `ch08-09-review-slot` in `work/done/`.

**The range at /apply.** `git diff --stat 3b728ae..HEAD` at `b5939e4` gives the same 111 files as at /propose: 36 under `work/done/`, not read, and 75 in decision 4's areas: the build 4, the chapters 46 (chapters 1 and 3 to 11, 20 files; chapters 12 to 24, 26 files), the kit's skills 18 (12 modified, 6 deleted under `.windsurf/skills/`), the documents 7. No commit landed after the page.

**The code reading.** Launched on the author's word in this session, on 2026-10-18, against `3b728ae`: five read-only general-purpose agents on Opus, one per area of decision 4, each keeping the session's advisor, then one checker on Opus. Each reader read its paths whole and their range diff, and listed them:

* the build: `Makefile`, `scripts/check_disclosure.py`, `scripts/check_width.py`, `scripts/markdown.py` (4 of 4);
* chapters 1 and 3 to 11, both editions (20 of 20);
* chapters 12 to 24, both editions (26 of 26);
* the kit's skills: the twelve current files under `.claude/skills/` and `.agents/skills/`, and the six deleted under `.windsurf/skills/` through `git show 3b728ae:` (18 of 18);
* the documents: docs/01, docs/03, docs/04, docs/05, docs/06, ADR-0017, ADR-0018 (7 of 7).

Together they cover decision 4's 75 paths.

Divergence: the first launch ran the five readers at once. The build and chapters 1 to 11 reported. The other three stalled with no report after 600 seconds, and their relaunches were stopped by the author, who asked for at most two agents at a time. Those three areas then ran again, two at a time, and reported in full, so nothing of the range went unread.

**The candidates, checked.** Labelled by the checker against each file; "kit wording" is the kit's own text, a note for the kit and not a line (decision 4).

The build:
* build-1 seen: docs/04:165, the Tests list leaves out the width check that `Makefile:20`, docs/01:66 and docs/05:165 name.
* build-2 latent: docs/04:45 says every block but `ts` is measured; `scripts/check_width.py:20` also skips `typescript`, which no block uses.
* build-3 latent: `scripts/check_width.py:35` measures a fence inside an HTML comment, which `mask` skips; none exists.
* build-4 latent: `scripts/markdown.py:35-36`, `closes` takes a closing fence with text after the run; none exists.
* build-5 latent: `scripts/markdown.py:11` opens a fence on a backtick info string with a backtick, or on four spaces of indent; none exists.

The documents:
* known-1 seen, kit wording: docs/05:307-309, the base names no commit for a milestone that started before the previous one's findings closed (decision 6); one fact with chB-1.
* doc-1 latent: docs/05:206-210, `git diff` and `git diff --cached` show no untracked file, so a delivery's new file escapes its review; nothing was missed so far.
* doc-2 seen: docs/01:31 and :39, `mask` is said shared by the prose and link checks; `check_parity.py` and `build_book.py` use it too, `target_end` is not named, nor `check_width.py`'s use of `language_of`.
* doc-3 seen: ADR-0017:46 names docs/04 §Chapter shape where `one-gain-section` changed §Writing the book.
* doc-4 seen: docs/06:361, the M16 paragraph says "the reviews' readers" where docs/05:291, docs/06:368 and chapter 16 say readers and checker.
* doc-5 weak: the slot's read-only agent instead of the host's review is the author's recorded choice (`kit-2026-10-17`).
* doc-6 weak: §8's wait takes §4's format through its "(§4)"; the same fact as kit-3.
* doc-7 seen: docs/03:36 glosses latent and weak but not seen (docs/05:320 is kit wording; chapter 15:83 glosses it).
* doc-8 seen, cosmetic: docs/06:336, `pt-free-line-done`'s sentence starts one column left of its neighbours.

The chapters:
* chB-1 seen: 15:20 and :150 (pt :20, :153) teach the same two names as known-1; line 22's extension does not fit this case.
* chB-2 seen: 15:50 (pt :51) says chapter 18 teaches `<base>..HEAD`; chapter 18 has no `git diff` and no range.
* chB-3 seen: 19:270, a batch's adjacent marks in one hunk of docs/06 are called no conflict, against 19:70 and docs/05 §4, and `git add -p` cannot split adjacent lines (the tension starts in the kit's wording of docs/05 §4).
* chB-4 seen: 19:265 points question deliveries to chapter 23 and offers them as method; chapter 20:60-62 and :84 define them as Case A's customization.
* chA-1 seen: pt 04:56 says the kit writes `features/`; the kit writes no such folder.
* chA-3 seen: 11:151 (pt :156) says every fix found outside the page is a line above that the delivery waits for; chapter 13:71 and the apply skill block only on a prerequisite.
* chA-7 seen: pt, the article before Ninjobs is feminine in chapters 0, 2, 3, 4, 11, 12, 13, 15, 16, 21 and masculine in 6, 7, 9, 22; the range moved 9:49 to the masculine.
* chA-8 seen: pt 11:55, 56, 101 drop "exemplar", the librarian and "de empréstimo" from the en queue, a cut the 74-column width forced.
* weak: chB-5 (16:55 names one case of 13's condition and links it), chA-2 (10's step 6 lists what one sees, pointing to 13), chA-4 (chapter 3 does show `lend`), chA-5 (8:103 and :142 give the rule), chA-6 (the reasons agree), chA-9 (the pt separates view and screen), chA-10 (a summary; 15 has the alternative).

The kit's skills:
* kit-1 seen: docs/03:34, the delivery review row fixes "what breaks the page and docs/04"; the apply skill and chapter 13:70 add this delivery's own lines. The row is this repository's text.
* kit-2 latent, kit wording: the apply skill's "this delivery's own lines" can be read as queue lines.
* kit-3 latent, kit wording: docs/05 §4 says `[?]` has three cases, §8 adds a fourth; docs/03:105 and chapter 14:26 repeat "three".
* kit-4 seen, kit wording: the analyze skill:46 cites docs/05 §8 for the slot that is in §5.

**The author's confirmations.** On 2026-10-18 the author confirmed every candidate this page suggested: build-1, known-1 with chB-1, doc-1, doc-2, doc-3, doc-4, doc-7, chB-2, chB-3, chB-4, chA-1, chA-3, kit-1 and kit-3; and of those left to the author's choice, build-2 to build-5, doc-8, chA-7 and chA-8. The weak ones are not findings.

**Decisions.**

1. The kit's own wording is fixed in the kit, on the author's word ("I need you to fix the kit with what you have, not notes"), which goes beyond decision 4's note for the kit and this page's Out of scope. It is not this delivery's change: it was made in the kit's repository, by the kit's own rules, as focus-kit 2026.10.18, staged there and not committed. It changes `SETUP.md` §3: the milestone review's base is the commit of the previous milestone's review, or the first commit (known-1); a line waits in four cases, the code reading that missed part of its range the fourth, with what was read as its reason (kit-3, doc-6); seen is glossed (doc-7); a Delivery review that reads `git diff` also reads the files the delivery created (doc-1); `/apply` fixes the text the delivery wrote (kit-2); `/analyze`'s question on the milestone review points to docs/05 §5 (kit-4). §1 step 4's migration list names them, and both changelogs carry the entry. chB-3 is chapter 19's fault alone: the kit has no batch text.
2. By the kit's rule, its bump opens M17, focus-kit 2026.10.18, in docs/06, with `kit-2026-10-18`, one line per chapter that teaches what changed (8, 13, 14 and 15) and `m17-review`. The author chose to answer there the three findings the kit answers: known-1 with chB-1 (docs/05 §8, chapter 15 lines 20 and 150), doc-1 (the Delivery review slot) and kit-3 (docs/05 §4, docs/03 line 105, chapter 14). M16 keeps the book's own faults and closes without waiting for M17. Divergence: this goes against decision 7, this page's Out of scope ("confirmed, a line") and docs/05 §8, which keep every finding under the review in the same milestone. It is the author's choice, because the kit's 2026.10.18 answers those three in the kit's own words, and a line under M16 would teach a version the repository does not run yet. The M17 lines answer them: known-1 with chB-1 by `kit-2026-10-18`, `ch08-update-2026-10-18` and `ch15-review-base`; doc-1 by `kit-2026-10-18` and `ch13-created-files`; kit-3 by `kit-2026-10-18` and `ch14-four-waits`. doc-7 is split. Its docs/05 half, the kit's gloss of seen, comes with `kit-2026-10-18`, which is the M17 paragraph's clause on seen. Its docs/03 half is M16's `docs03-review-rows`. Chapter 15:83 already glosses seen, so no chapter line carries it.
3. The findings, one line per file, under this review in M16: `docs04-width-rule` (build-1, build-2), `width-comment-fence` (build-3), `fence-commonmark` (build-4, build-5), `docs01-helpers` (doc-2), `adr17-section-name` (doc-3), `docs06-m16-paragraph` (doc-4, doc-8), `docs03-review-rows` (kit-1, doc-7), `ch15-range-pointer` (chB-2), `ch19-batch` (chB-3, chB-4), `ch04-features-folder` (chA-1), `ch11-blocking-fix` (chA-3, chA-8), `pt-ninjobs-article` (chA-7).

**The author's answers.** The line waited as `[?]` with `· resume: apply · blocked: C1 to C8 not answered` until the author answered, on 2026-10-18, in a fresh /apply session. HEAD was still `b5939e4`, the range the same 111 files, and both PDFs had been built after it, so the pages above stand. The author read both PDFs entire, English first.

* C1: holds.
* C2: holds.
* C3: holds.
* C4: holds.
* C5: holds.
* C6: holds.
* C7: holds.
* C8: holds, counted without the prologue: chapters 1 to 5 against M15's nine.
* outside: none.
* C9: answered by the code reading. The readers' paths cover decision 4's 75, and the author confirmed the candidates above.

No clause fails, so the findings are the code reading's twelve lines (decision 3) and the three M17 answers (decision 2). M15's C1, deferred to this reading, now holds.

**Verify.** `make verify` green after the answers were recorded, and again after the review's fixes.

**Review.** The delivery review was a read-only general-purpose agent on Opus that kept the session's advisor. It read this page whole, since the page is untracked and `git diff` does not show it, and this delivery's hunk of docs/06, against the page, docs/04 and docs/05 §§4 to 8. It found seven things, all fixed:

* the line still waited as `[?]` after the answers. It went to `[*]` (docs/05 §4).
* decision 2 sent three findings to M17 without recording that this departs from docs/05 §8. The divergence is recorded now, with the M17 lines that answer each finding.
* the M17 paragraph and `ch15-review-base` carried doc-7 as well, which decision 2 did not count, and chapter 15:83 already glosses seen. Decision 2 now splits doc-7, and `ch15-review-base` no longer asks for the gloss.
* `docs01-helpers` left out doc-2's `target_end`. It is named now.
* `docs06-m16-paragraph` did not say that doc-8's misaligned line is M15's `pt-free-line-done`. It does now.
* verify was not recorded on the page. It is now.
* C9 had no answer entry. It has one now.

No em dash, private detail or narrated run was found.

```commit
docs(m16-review): review M16, twelve findings and M17 opened

- C1 to C8 hold on the author's reading of both PDFs
- code reading of 3b728ae..HEAD by five readers and a checker
- twelve findings under the review, three more answered by M17
- M17 opened for focus-kit 2026.10.18

work/done/m16-review.md
```
