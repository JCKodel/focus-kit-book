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

**Done when.**

* [ ] Every line in this review's `after` is `[x]`, and every clause above has the review's answer from its reading of the passages in both PDFs, recorded as the review's, not the author's.
* [ ] Base, end commit, the inventory of paths by area, the slow tests (none), each reader's paths read and every checked candidate with its mark are recorded on this page.
* [ ] Every seen candidate is its own `[ ]` line under this review, shared causes sharing a line; every latent and weak candidate is listed as dropped; nothing is fixed here.
* [ ] The mechanical checks above are recorded with their results; `make verify` is green after the last edit and `make book` built both PDFs at the end commit, both rerun by /apply; only this review's changes are staged, with its suggested commit message, or the staging is the driver's at its word.
