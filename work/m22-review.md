# m22-review

**Objective.** The author can decide whether each promise of M22 holds in both editions, in the installed process and at the command line, with every confirmed failure recorded as a new finding under this review.

**Behaviour.**

* With every line M22's review names `[x]`, the author receives both PDFs built at the end commit and the clause checks below, each with its chapter sections and their start pages in both editions, and runs `make` with no target; each answer is recorded as holds, or fails with what the author saw.
* The review compares the installed commands and the active documents with focus-kit 2026.10.19.1 as `work/done/kit-2026-10-19-1.md` records it (SETUP.md at the kit's `35bdc9a`), then checks the book's explanations against those rules.
* On the author's word, read-only area readers read one fixed range, `git diff <base>..<end>`; one checker tests each candidate against that same snapshot and labels it seen, latent or weak before the author decides which become findings.
* A clause with no answer, a required reader that cannot run, or paths of the range no reader read leave this review waiting as `[?]` with `· resume: apply` and the reason (docs/05 §§4, 8); a partial reading that found nothing never closes it.
* A commit made during the reading does not move the end commit; what it changed is named as outside this reading. Each confirmed candidate becomes a `[ ]` line under this review, with no fix made here.

**Contract.** Clause checks from docs/06's M22 paragraph, each against the named deliveries' pages in `work/done/` and the cited chapter sections in both PDFs (`output/one-page-at-a-time.pdf`, `output/uma-pagina-de-cada-vez.pdf`); for the last clause, the author's terminal:

| Clause | Deliveries and passages | Author's question |
|---|---|---|
| The book teaches focus-kit 2026.10.19.1 and the repository runs on it | `kit-2026-10-19-1`: installed skills (`metadata.version` 2026.10.19.1), docs/05 §4's board paragraph and provenance sentence, ADR-0018's amendment, docs/03's `kanban board` row; `ch08-update-2026-10-19-1`: chapter 8, "What the install never touches, and how to update" / "O que a instalação nunca toca, e como atualizar", "What an update reports" / "O que uma atualização relata" | Does chapter 8's update example match what this repository's update to 2026.10.19.1 did: the report as a list by document and section, its one migration under docs/05 §4 (how the queue is read with a branch or a worktree per delivery) proposed, never applied, the other items matching or a recorded choice, and the next command named from the queue? |
| With a branch or a worktree per delivery the main branch shows each line as it was until the merge, so a board takes each slug's line from its worktree or branch and reconciles by slug | `ch14-20-read-branches` (with `kit-2026-10-19-1`'s docs/05 §4 and docs/03 text); chapter 14, "At the moment the work changes" / "No momento em que o trabalho muda", "Key points" / "Pontos-chave" (the kanban bullet); chapter 20, "The pull request as the team's review" / "O pull request como a revisão do time" (step 4), "Boards" / "Quadros", "Key points" / "Pontos-chave" | With a branch per delivery, where does a board read a line marked `[~]` on another delivery's branch, what does the main branch's copy show until the merge, and does one delivery's push carry the other deliveries' latest marks? |
| A session picking free lines or resolving an `after` reads each slug's line the same way | `ch14-20-read-branches`, chapter 14, "The next line, and which run together" / "A próxima linha, e quais rodam juntas"; `ch12-free-lines-branches`, chapter 12, "What `/propose` does" / "O que o `/propose` faz", "Key points" / "Pontos-chave" | On trunk and with a worktree per delivery, where does `/propose` read its own line and the lines its `after` names, and why would the main branch's copy alone name a delivery another session is building (`lend-book` / `emprestar-livro`)? |
| `make` with no target shows the commands, one line each saying what it does | `make-help`: `Makefile`, docs/01, `README.md`, `README.pt.md` | Run `make` in the repository with no target: do exactly the eight `make <target> <what it does>` lines of `make-help`'s Contract print, `help` first and `release` last with its `BUMP` parenthesis, and does nothing else run? |

**Base.** `4e283ec18190b2b88af0624858c98414d953734f`, the commit of m21-review, the previous milestone's review (docs/05 §8, docs/03's `milestone review` row). The range therefore also holds the fixes of M21's seven findings (`m21-git-slot-default`, `ch20-roles-and-points`, `ch14-20-board-branch`, `ch12-refuse-first`, `ch08-step4-outcomes`, `ch07-12-loan-days`, `docs-m21-tidy`), which get no second review (docs/05 §8), and the release commit of v1.2.5 (`VERSION`): the clause checks above are M22's alone, while the readers read the whole range, as m21-review did with M19's fixes.

**End.** The commit HEAD is when the reading starts; /apply records it before launching any reader, and nothing it records later moves it. Planned: `abb988a` (`docs(ch14-20-read-branches): read each slug's line from its branch`), HEAD when this page was written; the driver's `[~]` and `[>]` marks and this page's define commit come after it, so /apply records the actual end and recomputes the inventory there.

**Areas.** The paths `git diff --stat 4e283ec..HEAD` shows today, at `abb988a` (53 paths, 1405 insertions, 158 deletions), by the areas of docs/05 §5's Milestone review slot. /apply recomputes them at its end commit and splits an area too large for one careful reading:

* **Build:** `Makefile`, `README.md`, `README.pt.md`, `VERSION` (4 files).
* **Chapters**, split in two:
  * chapters 06 to 13, both editions: `book/{en,pt}/06-birth-of-focus-kit.md`, `08-install-and-hosts.md`, `12-propose.md`, `13-apply.md` (8 files);
  * chapters 14 to 23, both editions: `book/{en,pt}/14-queue-states.md`, `18-git-essentials.md`, `19-worktrees.md`, `20-team-tools.md`, `23-adoption.md` (10 files).
* **The kit's skills:** `.claude/skills/{analyze,apply,brainstorm,propose}/SKILL.md`, `.claude/skills/{analyze,brainstorm}/references/documents.md`, and the same six under `.agents/skills/` (12 files), each also compared byte for byte with SETUP.md §3 of 2026.10.19.1 at the kit's `35bdc9a`.
* **The documents**, split in two:
  * documents: `docs/01-Architecture.md`, `docs/03-Domain.md`, `docs/05-Process.md`, `docs/06-Queue.md`, `docs/adr/ADR-0018-six-marks.md`, `work/kit-proposals.md` (6 files), and this page, `work/m22-review.md`, which the end commit adds;
  * delivery records, the 12 pages added to `work/done/` (1190 lines) and the two lines `docs-m21-tidy` added to `work/done/m21-review.md`, split in two for one careful reading each: records 1, `ch07-12-loan-days`, `ch08-step4-outcomes`, `ch08-update-2026-10-19-1`, `ch12-free-lines-branches`, `ch12-refuse-first`, `ch14-20-board-branch`, `ch14-20-read-branches` (609 lines); records 2, `ch20-roles-and-points`, `docs-m21-tidy`, `kit-2026-10-19-1`, `m21-git-slot-default`, `make-help` (581 lines) and the edit to `m21-review`.

**Readers.** Seven read-only readers on Opus, one per area above, each keeping the session's advisor, Fable, at most two at a time, then one read-only checker on Opus; no other model runs the review (docs/05 §5, Milestone review). Each reader lists the paths it read.

**Slow tests.** The Verify slot names none (docs/05 §5); none is invented for this review.

**Known candidates for the checker**, raised by M22's proposes and applies without a line of their own; leads to check, not findings. Lines are both editions unless the pt line is given. Some sit outside the range's hunks; each names the reader that reads it beside its area, so the paths read and the leads agree:

* L1, chapter 17, "The manager's session" / "A sessão do gerente", en ~112 to 135, :131 (pt :131): the manager's session answers "where are we" from docs/06 alone; with a branch or a worktree per delivery the main branch's copy shows each line as it was until the merge. Read by the chapters 14 to 23 reader.
* L2, chapter 13, "What `/apply` does" / "O que o `/apply` faz", :26: `/apply` sees its `after` lines done and names the next free line from docs/06, with no word on reading each slug's line by branch. Read by the chapters 06 to 13 reader.
* L3, chapter 12, "What `/propose` does", :25: `work/` for the deliveries in flight, whose pages sit on their branches with a branch or worktree per delivery. Read by the chapters 06 to 13 reader.
* L4, chapter 7, "The seven documents" / "Os sete documentos", the lending library's Board slot, en :56 (pt :57, `npm run board` / `npm run quadro`), and chapter 14, "The queue as a kanban board", FACE reading docs/06 as one file, en :171 (pt :172): a board or tool reading one file against the reading by slug that chapter 14 now teaches. Chapter 7 by the chapters 06 to 13 reader, chapter 14 by the chapters 14 to 23 reader.
* L5, `docs/03-Domain.md`:108, the `board mirror` row says nothing about reading each slug's line by branch, while the `kanban board` row (:31) does. Read by the documents reader.
* L6, `docs/05-Process.md`:176 to 177, the project's rule that a dependency stays blocked until its completed changes reach the branch that needs them, which no chapter teaches; judged the project's, not the kit's, by the delivery that raised it. Read by the documents reader, checked against chapters 12 and 14.

Only this page, its move to `work/done/` and its findings' lines change; no chapter, document or build change.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs, `make book` at the end commit; /apply records the start page of every chapter in both editions.

**Out of scope.**

* Fixing any finding: each becomes its own line (docs/05 §8).
* Re-testing M21's clauses: its review answered them; its fixes are read by the area readers, not tested by clause.
* Changing the readers' model or the slot: docs/05 §5 owns it.
* Taking the approval of this page as the author's PDF reading or as the word that starts the readers: each is asked in the /apply session.

**Decisions.**

* The base is m21-review's commit, the previous milestone's review, the first of docs/05 §8's cases.
* The range's M21 finding fixes and the v1.2.5 release commit are read by the area readers but have no clause here (docs/05 §8: findings get no second review).
* M22's paragraph's middle sentence is taken as two clauses, the board and the session picking free lines or resolving an `after`, since different deliveries and passages answer each; every delivery of M22 answers a clause, so no row for an unnamed delivery.
* Areas as m21-review split them: two chapter readers, the documents and the records apart, the records split in two at the order above, the build and the skills one each; seven readers.
* The leads above go to the checker through the reader of the area holding them; the ones outside the range's hunks (L1, L2, L4, L6's chapters) are read by that reader beside its area.
* A confirmed candidate becomes a `[ ]` line under this review, whether or not it answers a clause of M22: docs/05 §8 puts each finding in the same milestone, as m21-review's Divergence found.
* The end commit and the final path inventory are inputs /apply fixes before reading, not open scope (docs/05 §8).

**Done when.**

* [ ] Every line in this review's `after` is `[x]`, and every clause above has the author's answer.
* [ ] Base, end commit, the inventory of paths by area, the slow tests (none), each reader's paths read and every checked candidate are recorded on this page.
* [ ] Every candidate the author confirms is its own `[ ]` line under this review; nothing is fixed here.
* [ ] `make verify` is green after the last edit, both PDFs were built at the end commit for the author's reading, and only this review's changes are staged, with its suggested commit message.
