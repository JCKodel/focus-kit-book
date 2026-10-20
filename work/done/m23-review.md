# m23-review

**Objective.** The author can see whether each promise of M23 holds in both editions and in the installed process, answered by the review's own reading of the passages, with every checker-confirmed failure recorded as a new line under this review.

**Behaviour.**

* With every line in this review's `after` `[x]`, /apply builds both PDFs at the end commit, reads in both the passages the clause table below names, at their start pages, and answers each clause's question itself: holds, or fails with what the passage says. These answers are the review's reading, not the author's: the author does not read the PDFs in this run and tests no clause.
* The review compares the installed commands and the active documents with focus-kit 2026.10.19.2 as `work/done/kit-2026-10-19-2.md` records it (SETUP.md at the kit's `44132c4`), then checks the book's explanations against those rules.
* The author's word that starts the readers is already given, for this batch: "review and fixes directly" (Decisions). /apply records the end commit, then launches read-only area readers over one fixed range, `git diff <base>..<end>`; one checker tests each candidate against that same snapshot and labels it seen, latent or weak.
* Each candidate the checker marks seen, low ones included, becomes a `[ ]` line under this review in docs/06, candidates sharing a file or a cause sharing a line; every latent and weak candidate is dropped and listed on this page with its mark. No fix is made here.
* A clause with no answer, a required reader that cannot run, or paths of the range no reader read leave this review waiting as `[?]` with `· resume: apply` and the reason (docs/05 §§4, 8); a partial reading that found nothing never closes it.
* A commit made during the reading does not move the end commit; what it changed is named as outside this reading.
* Edge, the parallel sessions: `kit-2026-10-20` (M24) is `[~]` in another session and `ch13-19-session-folder` (M25) has a draft page. A commit of theirs that lands before the reading starts is inside the range: its paths are read by their area's reader and named as M24's or M25's, with no clause here. If the reinstall at 2026.10.20 is in the range, the skills are checked against 2026.10.19.2 as M23's last commit left them, `git show 31f510e:<path>`, and the later version is named, not counted as an M23 failure.
* Edge, the shared tree: readers and the checker read the end commit (`git diff <base>..<end>`, `git show <end>:<path>`), never the working tree, which may hold the other sessions' uncommitted edits. The driver's uncommitted docs/06 marks, `work/ch13-19-session-folder.md` and `work/kit-2026-10-20.md` are not this review's.

**Contract.** Clause checks from docs/06's M23 paragraph, each against the named deliveries' pages in `work/done/` and the cited chapter sections in both PDFs (`output/one-page-at-a-time.pdf`, `output/uma-pagina-de-cada-vez.pdf`). Lines are en / pt; where one number is given it is the same in both.

| Clause | Deliveries and passages | The review's question |
|---|---|---|
| The book teaches focus-kit 2026.10.19.2 and the repository runs on it | `kit-2026-10-19-2`: installed skills (`metadata.version` 2026.10.19.2), docs/05 §5's Manuals slot and the Environments local item's pointer, AGENTS.md's manuals line, docs/03's `manual` row, ADR-0018's amendment `kit-2026-10-19-2`, `docs/manuals/build-the-book-from-a-clone.md`; `readme-run-manual`: README.md "Build locally", README.pt.md "Gerar localmente", `docs/manuals/release-the-book.md`:18; `ch08-update-2026-10-19-2`: chapter 8, "What the install never touches, and how to update" / "O que a instalação nunca toca, e como atualizar" (:46, the refusal check), "What an update reports" / "O que uma atualização relata" (:56 to :84 / :56 to :85) | Does chapter 8's update example match what this repository's update to 2026.10.19.2 did: the report as a list by document and section, its migrations under docs/05 §5's Manuals slot and AGENTS.md's manuals line proposed, never applied, the other items matching or a recorded choice, the refusal check on a copy outside the repository, and the next command named from the queue? And does the repository hold what the kit asks: the slot naming the manual of running it, the manual itself, and the READMEs pointing to it instead of holding its steps? |
| Running the product from a fresh clone is a manual always owed, named in the Manuals slot from `/brainstorm` | `ch10-12-run-manual`: chapter 7, "One place per fact" / "Um lugar para cada fato" (:15), "Manuals" / "Manuais" (:97 to :99 / :98 to :100, :108 / :109), "Where a new fact goes" / "Para onde vai um fato novo" question 7 (:139 / :140), "What the team gains" / "O que o time ganha" (:172 / :173), "Key points" / "Pontos-chave" (:180 / :181); chapter 9, `/brainstorm`'s fifth subject (:22), "What it writes, and where it stops" / "O que ele escreve, e onde para" (:62), "Review before you commit" / "Revise antes do commit" (:122) | Asked which manual every project owes, and what `/brainstorm`'s Manuals slot says on a new project, does each edition answer: the manual of running the product from a fresh clone, from installing what it needs to the first screen or call, named as owed and by which delivery, never "none yet" alone, with no folder created yet? |
| Written first by `/analyze` on an existing repository | `ch10-12-run-manual`: chapter 7, "Manuals" (:108 / :109); chapter 9, `/analyze`'s "What it asks" / "O que ele pergunta" (:91), "Review before you commit" (:122), "Key points" (:141); chapter 10, "An existing project" / "Um projeto existente", step 3's "You see" (:87) | On a repository with code, does each edition say `/analyze` writes the manual of running the product first, then one for each thing a person already does by hand, and what the review checks in it? |
| Written by the first delivery after which a person can run it and updated by every delivery that changes a step | `ch10-12-run-manual`: chapter 7, "Manuals" (:99 / :100, the library's `skeleton` / `esqueleto` and `docs/manuals/run-the-app-from-a-clone.md` / `rodar-o-app-de-um-clone.md`), "Key points" (:180 / :181); chapter 10, "A new project" / "Um projeto novo", step 6's "You see" (:66); `ch13-apply-run-manual`: chapter 13, "Green is not done" / "Verde não é pronto" (:101, :108), "`lend-book`, built" / "`emprestar-livro`, construída" (:163 to :165), "Review the staged change" / "Revise a mudança em stage" (:191), "Key points" (:275) | Does each edition say the first delivery after which the product runs writes the manual and each delivery that changes a step updates it, that `lend-book` / `emprestar-livro` leaves it as it is, that `/apply`'s next steps are the conversation's and the manual is what lasts, never that the manual replaces them, and do chapters 7, 10 and 13 name the same file and the same delivery? |

**Base.** `838f737027a393cfe5fc92372846e95b50cbd363` (`docs(m22-review): review M22, nine findings`), the commit of m22-review, the previous milestone's review (docs/05 §8, docs/03's `milestone review` row). The range therefore also holds the fixes of M22's nine findings (`ch08-13-17-next-line`, `ch20-merge-and-marks`, `ch08-13-20-default-review`, `ch14-face-retired`, `docs05-dependency-merged`, `kit-note-work-in-flight`, `m22-batch-proof`, `readme-make-list`, `docs06-m21-opening`), which get no second review (docs/05 §8), the release commit of v1.2.6 (`695d69f`, `VERSION`) and the queue's plan of M23 to M25 (`fa671ad`): the clause checks above are M23's alone, while the readers read the whole range, as m22-review did with M21's fixes.

**End.** The commit HEAD is when the reading starts; /apply records it before launching any reader, and nothing it records later moves it. Planned: `31f510e` (`docs(ch13-apply-run-manual): name the manual of running it in ch 13`), HEAD when this page was written; the driver's `[~]` and `[>]` marks and this page's define commit come after it, and a commit of M24 or M25 may too (Behaviour), so /apply records the actual end and recomputes the inventory there.

**Areas.** The paths `git diff --stat 838f737..HEAD` shows today, at `31f510e` (58 paths, 1722 insertions, 267 deletions), by the areas of docs/05 §5's Milestone review slot. /apply recomputes them at its end commit, places any new path in its area, and splits an area too large for one careful reading:

* **Build:** `README.md`, `README.pt.md`, `VERSION`, `docs/manuals/build-the-book-from-a-clone.md`, `docs/manuals/release-the-book.md` (5 files), read beside the `Makefile` and the `scripts/` the manual quotes, which the range does not change.
* **Chapters**, split in two:
  * M23's chapters, both editions: `book/{en,pt}/07-the-documents.md`, `08-install-and-hosts.md`, `09-starting-a-project.md`, `10-quick-guide.md`, `13-apply.md` (10 files);
  * the fixes' other chapters, both editions: `book/{en,pt}/14-queue-states.md`, `17-project-as-assistant.md`, `20-team-tools.md`, `23-adoption.md` (8 files).
* **The kit's skills:** `.claude/skills/{analyze,apply,brainstorm,propose}/SKILL.md`, `.claude/skills/{analyze,brainstorm}/references/documents.md`, and the same six under `.agents/skills/` (12 files), each also compared byte for byte with SETUP.md §3 of 2026.10.19.2 at the kit's `44132c4`.
* **The documents:** `AGENTS.md`, `docs/03-Domain.md`, `docs/05-Process.md`, `docs/06-Queue.md`, `docs/adr/ADR-0018-six-marks.md`, `work/kit-proposals.md` (6 files), and this page, `work/m23-review.md`, which the define commit adds.
* **Delivery records**, the 17 paths under `work/done/` (1341 insertions, 9 deletions), split in two for one careful reading each:
  * records 1, M23's five pages: `kit-2026-10-19-2`, `ch08-update-2026-10-19-2`, `ch10-12-run-manual`, `ch13-apply-run-manual`, `readme-run-manual` (528 lines);
  * records 2, M22's nine finding pages: `ch08-13-17-next-line`, `ch08-13-20-default-review`, `ch14-face-retired`, `ch20-merge-and-marks`, `docs05-dependency-merged`, `docs06-m21-opening`, `kit-note-work-in-flight`, `m22-batch-proof`, `readme-make-list` (804 lines), and the three pages `m22-batch-proof` edited, `ch08-update-2026-10-19-1`, `ch12-free-lines-branches`, `ch14-20-read-branches`.

Count: 5 + 18 + 12 + 6 + 17 = 58.

**Readers.** Seven read-only readers on Opus, one per area above, each keeping the session's advisor, Fable, at most two at a time, then one read-only checker on Opus; no other model runs the review (docs/05 §5, Milestone review). Planned pairs: the two chapter readers; the skills with the documents; records 1 with records 2; the build alone. Each reader lists the paths it read.

**Slow tests.** The Verify slot names none (docs/05 §5); none is invented for this review.

**Known candidates for the checker**, raised by M23's proposes and applies without a line of their own; leads to check, not findings. Lines are both editions unless the pt line is given. Some sit outside the range's hunks; each names the reader that reads it beside its area:

* L1, `work/done/ch08-update-2026-10-19-2.md`, Delivery review, the four candidates it kept: the excerpt's "other items" line leaves out docs/01 and the docs/manuals/ echo; "recorded on 2026-10-17" is not in this version's record; chapter 8 :53 lists "a rule, a queue line or a slot", not a line of `AGENTS.md`; "never one version of the kit with another" beside the refusal's "the kit's own change to that file since then". Chapter 8 by the M23 chapters reader, the record by records 1.
* L2, chapter 8 :84 / :85: the excerpt's `Next:` names `ch08-update-2026-10-19-2`, the delivery that writes the excerpt, which its page left to the person's review. M23 chapters reader.
* L3, chapter 11's `skeleton` / `esqueleto` line, unchanged by `ch10-12-run-manual`, while chapters 7 and 13 say that delivery writes the manual of running it. M23 chapters reader, outside the range.
* L4, chapter 15's hand test and chapter 19 :132's container manual, declared true as they are by `ch13-apply-run-manual`'s Out of scope, against chapter 7's three kinds of manual. M23 chapters reader, outside the range.
* L5, the `(see README)` in the messages of `scripts/check_examples.py` and `scripts/build_book.py`, kept by `readme-run-manual`, which now land on a README that names the tool and links the manual but holds no install command. Build reader, outside the range.
* L6, `docs/03-Domain.md`'s `manual` row against chapter 7's three kinds and docs/05 §5's Manuals slot. Documents reader.
* L7, the slug `ch10-12-run-manual` against its queue line's "chapters 7, 9 and 10", decided alone on its page (the chapter numbers before the 2026-10-16 renumbering). Documents reader.
* L8, M23's four chapter and README pages leave `make book` to the batch's driver, run once for the batch, as M22's did before `m22-batch-proof`: this review's `make book` at the end commit is that run, and this page records it (Mechanical checks). Records 1 reader.

**Mechanical checks**, run by /apply at the end commit:

* Every installed skill, `.claude/skills/*/SKILL.md` and `.agents/skills/*/SKILL.md`, carries `metadata.version` `2026.10.19.2` at the end commit (or, if 2026.10.20 is in the range, at `31f510e`, Behaviour); the 12 skill files are byte-equal to SETUP.md §3 of `git -C ~/Projects/focus-kit show 44132c4:SETUP.md`, read from the kit's history since its checkout is at a later version.
* `docs/manuals/build-the-book-from-a-clone.md` exists with the six headings of `set-up-the-disclosure-list.md`; the README link in both editions resolves to it from the repository root; `make` with no target prints the eight lines the manual's step 2 and the README's first bullet promise.
* `git status --short book/` is empty before `make book`, so the PDFs hold the end commit's `book/`; both PDFs contain the text of `31f510e`, the last commit under `book/` at define time (chapter 13's `run-the-app-from-a-clone.md` / `rodar-o-app-de-um-clone.md` sentence), and /apply records each chapter's start page in both editions and the start page of each section the clause table names.
* `make verify` and `make book` are rerun by /apply after its last edit; their results here are /apply's, not this page's. A failure caused by another session's uncommitted file is named as that session's.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs, `make book` at the end commit; /apply records the start page of every chapter in both editions.

**Out of scope.**

* Fixing any finding: each becomes its own line (docs/05 §8).
* Re-testing M22's clauses: its review answered them; its fixes are read by the area readers, not tested by clause.
* Rerunning the fresh-clone proof: `kit-2026-10-19-2` holds it, and no delivery since changed a build step (`readme-run-manual` changed text only); the build reader reads the manual against the `Makefile` and `scripts/` instead.
* M24 and M25: their lines, pages and commits are theirs; any in the range is read, not reviewed by clause (Behaviour).
* Changing the readers' model or the slot: docs/05 §5 owns it.
* The author's reading of the PDFs, the author's answer to any clause and the author's confirmation of candidates: not part of this run, by the author's choice (Decisions).

**Decisions from the documents.**

* The base is m22-review's commit, the previous milestone's review, the first of docs/05 §8's cases.
* The range's M22 finding fixes, the v1.2.6 release commit and the plan of M23 to M25 are read by the area readers but have no clause here (docs/05 §8: findings get no second review).
* The kit's version and its source are `kit-2026-10-19-2`'s: 2026.10.19.2 at `44132c4`, read from the kit's history.
* The end commit and the final path inventory are inputs /apply fixes before reading, not open scope (docs/05 §8).

**Decisions taken alone** (the batch's driver asked for recommended answers; correct them in the review).

* The author's choice for this batch, as the driver relays it, is "review and fixes directly": the driver runs the readers and the checker in this review's /apply, with no further word asked; checker-confirmed seen candidates become `[ ]` lines under m23-review; latent and weak candidates are dropped and listed here. This replaces docs/05 §8's "a candidate the person confirms" for this run.
* The author does not read the PDFs in this run, so the clause tests are answered by the review's own reading of the passages, in both PDFs, and the page says so; it never records an answer as the author's. This departs from docs/05 §8's "the person tests each clause by hand" for this run, at the author's word.
* "Seen" includes "seen, low": every seen candidate becomes a line, as the author's rule reads literally; candidates that share a file or a cause share one line, as m22-review grouped them.
* M23's paragraph is taken as four clauses: the opener (the book teaches 2026.10.19.2 and the repository runs on it), then the manual sentence in three, by who owes or writes the manual: owed and named from `/brainstorm`; written first by `/analyze`; written by the first runnable delivery and updated by each step change. Different passages answer each.
* `readme-run-manual` answers the opener's "the repository runs on it": it is the project following the Manuals slot's rule that a place naming a command with steps points to its manual. So every delivery of M23 answers a clause, and no row is needed for an unnamed one.
* The two docs/manuals/ files go to the build reader, not the documents reader: the build manual's commands and messages are checked against the `Makefile` and `scripts/`, which only that reader opens.
* The chapters split as M23's own chapters (7, 8, 9, 10, 13) and the M22 fixes' other chapters (14, 17, 20, 23), so one reader holds every passage the clause table names; the records split as M23's pages and M22's finding pages, with the three pages `m22-batch-proof` edited in the second.
* The leads above go to the checker through the reader of the area holding them; L3, L4 and L5 lie outside the range's hunks and are read beside their area.
* No fresh-clone rerun (Out of scope); the mechanical checks read the manual's existence, headings and links and `make`'s eight lines instead.
* A confirmed candidate becomes a `[ ]` line under this review whether or not it answers a clause of M23: docs/05 §8 puts each finding in the same milestone.
* (apply) P6, seen in `work/kit-2026-10-20.md`, M24's page in flight in another session, is named for that delivery and opens no line here: Out of scope gives M24 its own pages, and its /apply recomputes the next command it names.
* (apply) The review's Delivery review is one read-only Opus agent over this page, as the batch's lane rules ask, though m22-review had none.

**End commit.** `8a87b0c9a322114419e1ab0a17c4306c3b2a5d92` (`docs(queue): define m23-review`), HEAD when the reading started, recorded before any reader ran. Nothing was committed during the reading. The range holds two commits after the planned `31f510e`: `5698c3b` (`docs(queue): define kit-2026-10-20`, M24's, adding `work/kit-2026-10-20.md` and its docs/06 lines) and `8a87b0c` (this page's define). The reinstall at 2026.10.20 is not in the range: every skill is at 2026.10.19.2 at the end commit.

**Inventory at the end commit.** `git diff --stat 838f737..8a87b0c`: 60 paths, 1890 insertions, 267 deletions. The two paths beyond the planned 58 go to the documents: `work/m23-review.md` (this page) and `work/kit-2026-10-20.md` (M24's, read and named as M24's, no clause). Build 5, chapters 18 (M23's 10, the fixes' 8), skills 12, documents 8, records 17 (records 1: 5, records 2: 12): 60.

**Reading.** Seven read-only readers on Opus with the session's advisor, two at a time (the two chapter readers; the skills with the documents, then records 1 beside the documents; records 2 with the build), then one checker on Opus, all on `git show 8a87b0c:<path>` and the range diff, never the working tree. Paths read against the range: all 60. M23's chapters read its 10 whole and through the range diff, with chapters 11, 12, 15 and 19 for L3 and L4; the fixes' chapters read its 8 whole, with chapters 7, 10, 11, 12, 15, 18 and 19 by grep; the skills read the `.claude/` six whole and through the diff, and the `.agents/` six through the stat, whose bytes this session compared with SETUP §3 (below); the documents read its 8, this page and M24's included; records 1 read its 5 pages whole; records 2 read its 9 pages whole and the 3 pages `m22-batch-proof` edited through its hunks; the build read its 5 with the `Makefile`, `scripts/`, `.githooks/pre-commit` and the other manuals. No path missed.

**Mechanical checks**, run by /apply at `8a87b0c`:

* The eight installed `SKILL.md`, under `.claude/skills/` and `.agents/skills/`, carry `metadata.version` `2026.10.19.2`. `git -C ~/Projects/focus-kit show 44132c4:SETUP.md` has SHA-256 `fb0509f13564f64807e14a3becde92c0a4807cde18cb8ad311f80fb1315fe55d`, the one `kit-2026-10-19-2` recorded; the twelve skill files equal SETUP §3.1 to §3.5 of it byte for byte.
* `docs/manuals/build-the-book-from-a-clone.md` exists with the six headings of `set-up-the-disclosure-list.md`, in order; README.md:26 and README.pt.md:26 link `docs/manuals/build-the-book-from-a-clone.md`, which resolves from the root; `make` with no target prints the eight lines (`help`, `serve`, `build`, `verify`, `scan`, `hooks`, `book`, `release`).
* `git status --short book/` was empty before `make book`, so both PDFs hold the end commit's `book/`; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` with their EPUBs. The en PDF holds `run-the-app-from-a-clone.md` twice and the pt PDF `rodar-o-app-de-um-clone.md` twice (chapters 7 and 13), the text of `31f510e`.
* `make verify`: green at `8a87b0c` plus this page, after its last edit, with the other sessions' uncommitted docs/06 hunks and `work/ch13-19-session-folder.md` in the tree.

**Start pages** in the PDFs (en / pt): prologue 5 / 5, 1: 11 / 11, 2: 19 / 19, 3: 24 / 24, 4: 40 / 41, 5: 54 / 56, 6: 63 / 65, 7: 68 / 70, 8: 79 / 82, 9: 89 / 93, 10: 97 / 102, 11: 104 / 109, 12: 114 / 120, 13: 124 / 130, 14: 140 / 147, 15: 150 / 158, 16: 159 / 167, 17: 167 / 175, 18: 175 / 183, 19: 186 / 195, 20: 203 / 213, 21: 209 / 219, 22: 214 / 225, 23: 220 / 232, 24: 226 / 238. The clauses' sections (en / pt): chapter 7, "One place per fact" 69 / 71, "Manuals" 73 / 76, "Where a new fact goes" 75 / 78, "What the team gains" and key points 77 / 80; chapter 8, "What the install never touches, and how to update" 80 / 83, "What an update reports" 81 / 84; chapter 9, "What it writes, and where it stops" 92 / 96, `/analyze`'s "What it asks" 93 / 97, "Review before you commit" 95 / 99, key points 96 / 100; chapter 10, "A new project" 98 / 103, "An existing project" 100 / 106; chapter 13, "Green is not done" 129 / 135, "`lend-book`, built" 130 / 137, "Review the staged change" 133 / 140, key points 138 / 145.

**Clause answers**, the review's own reading of the passages at the end commit in both editions, the PDFs built from it; not the author's, who read nothing in this run.

* The book teaches focus-kit 2026.10.19.2 and the repository runs on it: holds, with one failure in the excerpt's last line. Chapter 8 (en/pt :56 to :84 / :85) shows the report as a list by document and section; the Manuals slot and AGENTS.md's manuals line as "Proposed", and :57 says the setup file does not write what the project's documents should hold; section numbers "None", the Milestone review a recorded choice, the rest as "other items"; :46 the refusal on a copy outside the repository, as the record's Refusal case. The next command, `/propose ch08-update-2026-10-19-2`, is the record's, but the excerpt drops the record's "once this line is `[x]`" and calls it "the queue's first free line" while its `after` was in flight (C2, a finding). The repository holds what the kit asks: docs/05 §5's Manuals slot names `build-the-book-from-a-clone.md`, owed and written by `kit-2026-10-19-2`, and its Environments local item points to it; AGENTS.md:9 says "running it"; the manual exists; README.md and README.pt.md "Build locally" name the commands and point to it for the steps, and `release-the-book.md`:18 points to it. The record behind the excerpt has its own faults (R1, K3, R2, findings).
* Owed, named in the Manuals slot from `/brainstorm`: holds. Chapter 7 :97 / :98 says every project owes the manual of running the product from a fresh clone, from installing what it needs to the first screen or call; :98 / :99 that the slot names it from the start and the first delivery after which a person can run it writes it; :108 / :109 and :180 / :181 that `/brainstorm` writes none and names it as owed; question 7 at :139 / :140 and the gain at :172 / :173 agree. Chapter 9 :22 and :62 give the slot as owed by the first delivery after which a person can run it, the others "none yet", never "none yet" alone; :61 says it writes no manual and `docs/manuals/` is created with the first one; :122 the review checks it.
* Written first by `/analyze` on an existing repository: holds. Chapter 9 :91 says `/analyze` writes, in `docs/manuals/`, the manual of running the product from a fresh clone first, then one for each thing a person already does by hand; :141 repeats it; :122 and :124 say what the review checks (written on an existing project; a person who read nothing else can follow every manual, and every command exists); chapter 7 :108 / :109 and chapter 10 step 3's "You see" :87 agree.
* Written by the first runnable delivery and updated by every step change: holds. Chapter 7 :99 / :100 has `skeleton` / `esqueleto` writing `docs/manuals/run-the-app-from-a-clone.md` / `rodar-o-app-de-um-clone.md`, a later database delivery updating it and a refusal to `lend-book` leaving it as it is; chapter 13 :101 says the first delivery after which the product runs writes it and every later step change updates it; :163 to :165 name the same file and the same `skeleton`, and `lend-book` / `emprestar-livro` leaves it as it is; :108 and :275 say the next steps are the conversation's and end with it, the manual is what lasts, never that it replaces them; :191 the review asks it. Chapter 10 step 6 :66 names the skeleton and `docs/manuals/` but not the file; the checker marked that weak (X1): a quick guide naming the folder misstates nothing.

**Candidates**, marked by the checker at `8a87b0c` (seen: true in the file today; latent: nothing triggers it today; weak: the claim does not hold as stated). Ids are the readers': C M23's chapters, D the fixes' chapters, K skills, P documents, R records 1, S records 2, B build; L the leads above; X1 the review's own, from its clause reading. Lines are both editions unless the pt line is given. 53 ids in 48 rows: 32 seen (10 medium, 22 low, none high), 3 latent, 18 weak.

| id | file:line | mark | claim |
|---|---|---|---|
| C1, K4 (L1) | en 08:82-83, pt :83-84 | weak | "other items" leaves out docs/01 and docs/manuals/; SETUP's step 4 checks neither, so the excerpt is right (cause: R1) |
| C2 (L2) | en 08:84, pt :85-86 | seen, low | `Next:` calls ch08-update "the queue's first free line" though its `after` was in flight; the record's "once this line is `[x]`" dropped |
| C3 (L1) | 08:52-53 | weak | "a rule" covers AGENTS.md's lines, and :52 says "the line" |
| C4 | 09:122 | weak | "by which delivery" is answered by the condition at :62 |
| C5 | pt 09:22, :62; pt 08:71; pt 07:99, :181 | seen, low | one kit term as "a cargo da", "devido pela" and "devido" |
| C6 | 08:104; 13:28 | latent | the chapters follow docs/05 §4, which the skills read |
| L1b | 08:78 | weak | "recorded on 2026-10-17" is the real date of `review-slot-models`; the excerpt says it paraphrases |
| L1d | 08:45, :96 | weak | step 3's file check and step 4's report are different steps |
| L3 | en 11:49, pt :52 | weak | a queue line is one sentence; nothing contradicts `skeleton` writing the manual |
| L4 | ch 15:31-53; ch 19:132 | weak | the hand test is no manual; the container setup is a by-hand action, one of chapter 7's kinds |
| X1 | 10:66 | weak | names the delivery and the folder, not the file; misstates nothing |
| D1, S3 | en 14:64, pt :65 | seen, low | "every delivery's latest mark" against :63's limits and chapter 20 :61's "as far as it can see it" |
| D2 | 17:137; 18:25; 19:145 | seen, low | "a person reviews and commits" with no "by default" or the Git slot's word |
| D3 | 17:132; 20:61; en 14:171 | weak | summaries pointing to chapter 14, which teaches "the lines only a branch has" |
| D4 | en 14:171, pt :172 | seen, low | the board "moves its cards as the marks change" while a branch's mark shows only once committed or pushed |
| D5 | 23:66 | weak | a role summary pointing to chapter 17 |
| D6 | 23:63-64, :112 | seen, low | the Git slot's alternative names commits only; chapter 20 :35, :86 let the slot give the merge too |
| D7 | 17:124-128 | seen, medium | "Next free line: due-date-format" while `m1-review` (chapter 11 :54, no `after`) is free and above it by chapter 14 :78 |
| K1, P2 | en 07:102, pt :103, pt :17 | seen, low | manuals "named in the documentation language", which the kit and docs/05 dropped |
| K2 | 09:22 | seen, low | `/brainstorm`'s slots leave out the slow tests the skill and chapter 7 :45 name |
| K3 | work/done/kit-2026-10-19-2.md:46, :80 | seen, medium | :46 says the step 4 report does not name the Environments pointer; :80 lists it under step 4 |
| P1 (L7) | docs/06-Queue.md:576 | weak | the slug kept with a recorded reason; no rule ties slugs to chapter numbers |
| L6 | docs/03-Domain.md:116 | weak | the `manual` row matches the slot and chapter 7 |
| P3 | docs/06-Queue.md:571 | weak | the `/analyze` clause is answered by ch10-12-run-manual's page |
| P4 | work/m23-review.md:87-88 | seen, medium | this page sets aside docs/05 §8's person testing and confirming on the driver's relayed word, which no document provides for |
| P5 | work/m23-review.md:13-14 | weak | working-tree claims the end commit cannot check; the M25 slug part is R8 |
| P6 | work/kit-2026-10-20.md:9, :40 | seen, low | M24's: :9 expects `/propose m23-review`, stale now; :40 names `work/ch13-apply-run-manual.md`, now in `work/done/` (Decisions taken alone) |
| R1 | work/done/kit-2026-10-19-2.md:76-87 | seen, medium | "Migration report (step 4)" lists Environments, docs/manuals/, docs/01, docs/03 and ADR-0018, which step 4 never checks |
| R2 | work/done/kit-2026-10-19-2.md:9 | seen, low | credits the docs/manuals/ echo to the kit's changelog, which names only the AGENTS.md template |
| R3, S6 (L8) | ch08-update-2026-10-19-2.md:59, :79; ch10-12-run-manual.md:55, :87; ch13-apply-run-manual.md:70; ch20-merge-and-marks.md:47, :71 | seen, medium | Done when ticks `make book` and the PDF paths on a driver's run no page records, the pattern m22-batch-proof fixed |
| R4 | work/done/readme-run-manual.md:84, :109 | seen, low | ticks the `[x]` and the staging, then says this session did neither |
| R5 | work/done/kit-2026-10-19-2.md:3, :37; ch08-update-2026-10-19-2.md:34 | seen, low | name chapter 12 as taught by ch10-12-run-manual, which left it untouched |
| R6 | work/done/ch10-12-run-manual.md:8, :52, :85, :89 | seen, low | Behaviour expects chapter 9 to name the file; it does not, its review noted it, Divergences says none |
| R7 | work/done/ch13-apply-run-manual.md:18, :56; ch10-12-run-manual.md:76 | seen, low | contradict each other on who fixed the Portuguese phrase |
| R8 | work/done/ch13-apply-run-manual.md:41 | seen, low | names `ch13-19-session-folder` (M25), which no committed line holds |
| R9, S2 | ch13-apply-run-manual.md:69, :79; ch08-update-2026-10-19-2.md:72; ch10-12-run-manual.md:89; readme-run-manual.md:115; docs05-dependency-merged.md:57, :69, :71; ch20-merge-and-marks.md:71-78 | seen, medium | delivery reviews narrower than docs/05 §5 (only the chapter files, or the advisor in place of a read-only Opus agent, or no advisor) while Done when ticks "as docs/05 §5 says" |
| R10 | work/done/ch08-update-2026-10-19-2.md:39 | seen, low | cites docs/05 §5 lines 250 to 253; the sentence ends on 254 |
| S1 | d740cbb, 9c2e490, 53a82de; ch08-13-17-next-line.md:78, :82; ch20-merge-and-marks.md:67; ch08-13-20-default-review.md:66, :70 | seen, medium | ch08-13-20-default-review's sentences landed in the two other deliveries' commits, whose pages say "1 insertion", "nothing else", "three hunks" |
| S4 | ch08-13-17-next-line.md:12, :71; ch12-free-lines-branches.md:12; docs05-dependency-merged.md:7 | latent | true when written, before `6f28cb2`; chapter 14 agrees with docs/05 §4 today |
| S5 | en 14:171 | weak | a team's own board may read pages; nothing says the kit does |
| S7 | work/done/ch08-13-20-default-review.md:16 | seen, low | puts chapter 8 :30 under "What the install never touches"; it is under "Install" (the docs05-dependency-merged half weak) |
| B1 | docs/manuals/build-the-book-from-a-clone.md:13, :21; scripts/check_links.py:40-45 | seen, low | the manual's URLs are outside the link check; the nodejs.org URL was checked in the README |
| B2 | README.md:22, :26 | weak | the examples fact has its owner in docs/01 |
| B3 | docs/manuals/build-the-book-from-a-clone.md:15; Makefile:36 | seen, medium | `pip install pypdf` is refused (PEP 668) for the Homebrew `python3` that `make book` runs |
| B4 | build manual :7, :12; README.md:18 | latent | `str.removesuffix` needs Python 3.9; every current one is newer |
| B5 | README.md:20 | weak | leaving `make build` out was a recorded choice |
| B6 | docs/manuals/release-the-book.md:9, :18, :19 | seen, low | one manual named by its path, the others by bare names, in one list |
| B7 (L5) | scripts/check_examples.py:221, :225; scripts/build_book.py:468, :473; build manual :42-44 | seen, low | "(see README)" lands on a README with no install command, loops back inside the manual, and sends pt readers to the English README |

Dropped, latent: C6, S4, B4. Dropped, weak: C1, K4, C3, C4, L1b, L1d, L3, L4, X1, D3, D5, P1, L6, P3, P5, S5, B2, B5. P6 is M24's (Decisions taken alone).

**Findings.** The seen candidates, grouped by file or cause, opened under this review in docs/06 by the driver (this session does not edit docs/06):

```
[ ] kit-record-step4         the page of kit-2026-10-19-2: its "Migration report (step 4)" holds only what SETUP's step 4 checks, the project's other dispositions apart, agreeing with its Decisions on the Environments pointer, and the docs/manuals/ echo is not credited to the kit's changelog · after m23-review
[ ] ch08-next-free-line      chapter 8: the update excerpt's `Next:` keeps the record's condition, once kit-2026-10-19-2 is `[x]`, or stops calling ch08-update-2026-10-19-2 the queue's first free line; both editions · after m23-review
[ ] ch14-board-visibility    chapter 14: each refresh carries every delivery's mark as far as it can see it, and the board's cards move as each mark becomes visible, as :63 says; both editions · after m23-review
[ ] ch17-23-git-slot-word    chapters 17, 18, 19 and 23: a person reviews and commits or merges by default, and the Git slot's word may let the agent commit and merge, as chapter 20 says; both editions · after m23-review
[ ] ch17-next-free-line      chapter 17: the manager's sample answer names as next free line the one chapters 11 and 14 make next, `m1-review` while it has no `after`, or the queue it reads says otherwise; both editions · after m23-review
[ ] ch07-09-manual-wording   chapters 7, 8 and 9: manuals named after what they do, without "in the documentation language", and one Portuguese phrase for the manual owed by the first runnable delivery; both editions · after m23-review
[ ] ch09-slow-tests          chapter 9: /brainstorm's process slots name the slow tests kept out of verify, as its skill and chapter 7 do; both editions · after m23-review
[ ] docs05-author-word       docs/05 §8 and docs/03's `milestone review` row: what holds when the author's word gives the clause tests and the candidates' confirmation to the review's own session · after m23-review
[ ] m23-records-proof        the pages of ch08-update-2026-10-19-2, ch10-12-run-manual, ch13-apply-run-manual, readme-run-manual, ch20-merge-and-marks and docs05-dependency-merged: Done when ticks only what their Proof records, the `make book` run and PDF paths, the Delivery review as docs/05 §5 says, the `[x]` and the staging · after m23-review
[ ] m23-records-crossrefs    the pages of kit-2026-10-19-2, ch08-update-2026-10-19-2, ch10-12-run-manual and ch13-apply-run-manual say that ch10-12-run-manual left chapter 12 untouched and chapter 9 names no file, agree on who set the Portuguese phrase, name no slug that no committed line holds and cite docs/05 §5's lines 250 to 254 · after m23-review
[ ] m22-records-commits      the pages of ch08-13-17-next-line, ch20-merge-and-marks and ch08-13-20-default-review: each Proof says which commit holds default-review's chapter sentences, and chapter 8 :30's section is "Install" · after m23-review
[ ] manual-link-pointers     docs/manuals/build-the-book-from-a-clone.md and release-the-book.md, scripts/check_links.py, check_examples.py and build_book.py: the link check reads the manuals' URLs, "(see README)" points where the install steps are, and the manuals are named one way · after m23-review
[ ] manual-pypdf-install     docs/manuals/build-the-book-from-a-clone.md: pypdf installed for the `python3` that `make book` runs, which refuses a bare `pip install` on Homebrew · after m23-review
```

**Done when.**

* [x] Every line in this review's `after` is `[x]`, and every clause above has the review's answer from its reading of the passages in both PDFs, recorded as the review's, not the author's.
* [x] Base, end commit, the inventory of paths by area, the slow tests (none), each reader's paths read and every checked candidate with its mark are recorded on this page.
* [x] Every seen candidate but P6 (Decisions taken alone) is its own `[ ]` line under this review, shared causes sharing a line, thirteen lines, handed to the driver to add to docs/06; every latent and weak candidate is listed as dropped; nothing is fixed here.
* [x] The mechanical checks above are recorded with their results; `make verify` is green after the last edit and `make book` built both PDFs at the end commit, both run by this /apply; the staging is the driver's at its word: this session staged nothing.

**Divergences.** The finding lines are not in docs/06: the batch's lane rules leave docs/06 to the driver, who adds the thirteen lines above under m23-review and marks it `[x]`. The staging and the commit are the driver's. P6 is seen but opens no line here, being M24's page (Decisions taken alone). The readers ran in other pairs than Readers planned: records 1 beside the documents, records 2 beside the build, as each slot freed, never more than two at a time.

**Proof.** The skills' versions and their byte comparison with SETUP.md at `44132c4`, the manual's headings and link, `make`'s eight lines and the PDFs' text and start pages, all above; `make verify` green after the last edit of this page.

**Delivery review.** One read-only Opus agent with the advisor read this page against its define version at `8a87b0c`, docs/04, docs/05 §§3 to 5 and 8, docs/06's line format and the cited files at the end commit. It found five: the candidate counts (now 53 ids: 32 seen, 3 latent, 18 weak), no `commit` block, `make verify` ticked but not recorded, chapter 9 :128 for :124, and "every seen candidate" with P6 aside; two lines with no verb; the readers' pairs unrecorded. All fixed here. It confirmed the thirteen lines' format, slugs and coverage, the numbers, the start pages and a dozen citations.

```commit
docs(m23-review): review M23, thirteen findings

- seven readers and a checker over 838f737..8a87b0c, 60 paths read
- the four clauses hold by the review's reading, but chapter 8's Next
- 53 candidates: 32 seen, 3 latent, 18 weak; P6 left to M24
- thirteen finding lines under m23-review for docs/06
- skills byte-equal to SETUP.md at 44132c4; make book at the end

work/done/m23-review.md
```
