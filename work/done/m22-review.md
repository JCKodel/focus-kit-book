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

**Actual end.** `c3ec277` (`docs(queue): define m22-review`), HEAD when the reading started, recorded before any reader ran. `git diff --stat 4e283ec..c3ec277`: 54 paths, 1483 insertions, 158 deletions; the 53 paths of the planned inventory and this page, `work/m22-review.md`, which `c3ec277` adds (78 lines). The paths by area are those below, unchanged; this page joins the documents reader.

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

**Reading.** At `c3ec277`, seven read-only readers on Opus, two at a time (chapters 06 to 13 with chapters 14 to 23; the skills with the documents; records 1 with records 2; the build alone), then one checker on Opus. Paths read against the range: all 54. Chapters 06 to 13 read its 8 (the four en files whole, the four pt files through the range diff and the passages around each hunk), with chapter 7's Board slot for L4; chapters 14 to 23 read its 10 whole, with chapters 12 and 17 in both editions for L1 and L6; the skills read its 12 (the diff whole, the `.claude` copies whole, the `.agents` copies by `cmp`); the documents read its 7, this page at `c3ec277` included; records 1 read its 7 pages whole; records 2 read its 5 pages and `work/done/m21-review.md` whole; the build read its 4 (`VERSION` through the range diff and the release commit). No path missed.

**Mechanical checks**, run by /apply at `c3ec277`:

* `make` with no target prints exactly the eight lines of `make-help`'s Contract, `make help     this list` first and `make release  publish the next version, author only (BUMP=minor|major)` last, nothing else, and exits 0.
* Every installed skill, `.claude/skills/*/SKILL.md` and `.agents/skills/*/SKILL.md`, carries `metadata.version` `2026.10.19.1`; the 12 skill files are byte-equal to SETUP.md §3.1 to §3.5 at the kit's `35bdc9a`.
* The PDFs at `output/one-page-at-a-time.pdf` (17:06) and `output/uma-pagina-de-cada-vez.pdf` (17:07) contain the text of `abb988a`, the last commit under `book/` in the range: chapter 14's and chapter 20's sentences it added are in both; `c3ec277` changes no file under `book/`.

**Start pages** in the PDFs (en / pt): prologue 5 / 5, 1: 11 / 11, 2: 19 / 19, 3: 24 / 24, 4: 40 / 41, 5: 54 / 56, 6: 63 / 65, 7: 68 / 70, 8: 78 / 81, 9: 88 / 92, 10: 96 / 101, 11: 103 / 108, 12: 113 / 119, 13: 123 / 129, 14: 138 / 145, 15: 149 / 156, 16: 158 / 165, 17: 166 / 173, 18: 173 / 181, 19: 184 / 193, 20: 201 / 211, 21: 207 / 217, 22: 212 / 223, 23: 218 / 230, 24: 224 / 236. The clauses' sections (en / pt): chapter 8, "What the install never touches, and how to update" 79 / 82, "What an update reports" 80 / 83, key points 87 / 90; chapter 12, "What `/propose` does" 114 / 120, key points 121 / 127; chapter 14, "At the moment the work changes" 140 / 147, "The next line, and which run together" 141 / 148, "The queue as a kanban board" / "A fila como quadro kanban" 145 / 152, key points 147 / 154; chapter 17, "The manager's session" 171 / 178; chapter 20, "The pull request as the team's review" 202 / 212, "Boards" 204 / 214, key points 205 / 215.

**Candidates**, marked by the checker at `c3ec277` (seen: true in the file today; latent: nothing triggers it today; weak: the claim does not hold as stated). Lines are both editions unless the pt line is given. Ids are the readers': C chapters 06 to 13, D chapters 14 to 23, S skills, E documents, R records 1, P records 2, B build; L the leads above. The proposed line was the session's; the author's decision on each is under Findings below.

| # | Ids | File and lines | Claim | Mark | Proposed line |
|---|---|---|---|---|---|
| 1 | C1, L2 | `book/{en,pt}/13-apply.md`:26, 31 to 32, 103, 107 | `/apply` checks its `after` lines done and names the next free line from docs/06, with no word on reading each slug's line off trunk (ch14 en :60 to 62, :70 to 73; docs/05:119 to 125); ch12:27 says it for `/propose` only | seen | `ch08-13-17-next-line` (with 7, 8): chapters 8, 13 and 17 say that off trunk the next free line and an `after` are read by slug, as chapter 14 teaches |
| 2 | C2, D9, L3 | `book/{en,pt}/12-propose.md`:25, `19-worktrees.md`:288 | "`work/` for the deliveries in flight", while off trunk their pages sit on their branches (ch12:29); the kit's propose skill has the same words | seen, low | `kit-note-work-in-flight` (with 18): the kit-proposals note `ch12-free-lines-branches` promised; the chapters keep the kit's words |
| 3 | C3, D8, L4 | `book/en/07-the-documents.md`:56 (pt :57) | The library's Board slot "`npm run board` pushes docs/06" against the per-slug reading of ch14:64 and ch20:60 | weak, low (a slot names the command; the library's Git strategy is not stated) | none |
| 4 | C4 | `book/{en,pt}/13-apply.md`:259 | "a person reads the diff before it exists in the history" with no "by default", against :210 and :213 | seen, low | `ch08-13-20-default-review` (with 14, 15, 16): the review-before-commit and merge sentences say "by default", or name who decides |
| 5 | C5, D3, E1, E2, S1, L6 | `docs/05-Process.md`:176 to 177 | The project's "keep a dependency blocked until its completed changes are available in the branch that needs them" contradicts :97 to 98, :119 to 125 and ch14 en :71 to 73; not in SETUP.md at `35bdc9a`; passed on by `kit-2026-10-19-1`:17, `ch12-free-lines-branches`:12, 32 and `ch14-20-read-branches`:42 | latent (this repository is on trunk, :274) | with 6 |
| 6 | E3 | `docs/05-Process.md`:176 | "blocked" said of a dependency, which docs/03:110 to 113 and docs/05:134 to 135 call an order, not a blocked reason | seen, low | `docs05-dependency-merged` (with 5): say which rule holds off trunk, in docs/03's words, or drop the project's sentence |
| 7 | C6, R1 | `book/en/08-install-and-hosts.md`:100 (pt :102) | The update names "the command docs/06's first free line wants", with no off-trunk word; `ch08-update-2026-10-19-1`:42 handed it to a page that covers only `/propose` | seen, low | with 1 |
| 8 | D1, L1 | `book/{en,pt}/17-project-as-assistant.md`:24 to 25, 119, 127, 131, 150; `23-adoption.md`:66 | The manager's "where are we" read from docs/06 alone, "Next free line" included; scoped out by `ch14-20-read-branches`:44 with no line | seen | with 1 |
| 9 | D2, L4 | `book/en/14-queue-states.md`:171 (pt :172) | FACE "reads docs/06 and the pages in `work/`", against the same chapter's :61 to 62 and key point :187; what FACE does is the author's fact | seen, low | `ch14-face-reading`: say whether FACE reads one file, on trunk, or each slug's line (the author chose `ch14-face-retired`) |
| 10 | D4 | `book/{en,pt}/20-team-tools.md`:60, 87 | "with a branch per delivery" and "the other deliveries' latest marks", against ch14 en :63 (a worktree's mark at once, a branch's once committed) | seen, low | `ch20-merge-and-marks` (with 13): "branch or worktree", and the marks as far as the push can see |
| 11 | R2, E4, D7, L5 | `docs/03-Domain.md`:108; `work/done/ch14-20-read-branches.md`:60 vs `ch14-20-board-branch.md`:10, 36 | (a) `board mirror` has no per-slug reading while `kanban board` (:31) does; (b) one record reversing another's "no rule" | (a) latent, low; (b) weak (2026.10.19.1's docs/05:117 to 124 now gives the rule) | none |
| 12 | E5, S3 | `docs/03-Domain.md`:113 to 114 | `dependency` and `free line` silent on where the `[x]` is read off trunk | latent, low | none |
| 13 | D5 | `book/{en,pt}/20-team-tools.md`:8 | Two sentences on one source line, against docs/04:18 | seen, low | with 10 |
| 14 | D6 | `book/{en,pt}/20-team-tools.md`:10, 33 | :10 "a second person who reviews before the merge" unqualified against :34; :33 "approves the merge" | :10 seen, low; :33 weak | with 4 |
| 15 | P1 | `book/{en,pt}/20-team-tools.md`:34, 85 | "By default whoever merges is the reviewer", while by default the person may ask the agent to merge (ch23 en :64, ch19 en :194 to 196, ch13:4); `ch20-roles-and-points`:64, 87 left it to the author | seen, low | with 4 |
| 16 | P2 | `book/{en,pt}/08-install-and-hosts.md`:30 | "commit it yourself, as by default with every change the agent makes", while the default is commit it or ask the agent (ch13:4, ch18 en :65, ch23 en :64) | seen, low | with 4 |
| 17 | C aside | `book/{en,pt}/13-apply.md`:4 | "by default" placed on using rather than on reviewing | weak | none |
| 18 | E6 | `work/done/ch12-free-lines-branches.md`:37 | Sends ch12:25 to "a note for `work/kit-proposals.md`"; no such note exists | seen, low | with 2 |
| 19 | E7 | this page :69 (at `c3ec277`) | Lists the leads outside the range's hunks as "L1, L2, L4, L6's chapters"; L3, L5 and L6's docs/05:176 to 177 are outside them too | seen, low | none: this page, corrected in this review if the author confirms |
| 20 | E | `docs/adr/ADR-0018-six-marks.md`:52, 56 | The `kit-2026-10-19` amendment's "when that branch is merged" not said to be replaced | weak (dated amendments supersede by order) | none |
| 21 | S2 | `work/done/kit-2026-10-19-1.md`:19, 67 | The Git slot's "never commits or merges on its own" listed as a recorded choice though it is the template's default | latent, low | none |
| 22 | R3 | `work/done/ch08-update-2026-10-19-1.md`:51 vs :74; `ch12-free-lines-branches.md`:65 vs :73; `ch14-20-read-branches.md`:76 vs :85, 92 | "`make verify` green" ticked over a Proof recording a failing link check; `make book` ticked unhedged while deferred to the driver, whose run no record holds (the other four pages' Done when say the driver may run it: weak) | seen | `m22-batch-proof`: record the batch's verify rerun and `make book` run where the pages point, or say in docs/05 where a batch driver records them |
| 23 | R4 | `book/en/12-propose.md`:25, `13-apply.md`:115 | docs/03 "for the words" and "for the names" while the loan period's value is cited to it | weak, low | none |
| 24 | R5 | commit subjects `1a83924`, `9ee7baf`, `b0aaf2b`, `ceca01e`, `fac1518` (also `0824987`, `c0046bc`, `67fee58`, `1e0159b`, `d1eb372`) | Declarative subjects against docs/05:315's "Imperative subject" | seen, low | `docs05-commit-subject`: either the subjects follow §6 or §6 says what the practice is |
| 25 | P3 | `docs/06-Queue.md`:517 (from `docs-m21-tidy`:22) | M21's paragraph says the kit was planted "after the beta"; chapter 6:50 says "after the opening" on purpose (`ch06-kit-after-ninjobs`:53, 62; `m21-review`:27) | seen, low | `docs06-m21-opening`: M21's paragraph says "after the opening" |
| 26 | P4, B1 | `README.md`:20, `README.pt.md`:20 | "`make` lists these commands" above five of the eight targets `make` prints (help, build and scan absent); "target" against "command" (`make-help`:59): weak | seen, low | `readme-make-list`: the bullet says `make` lists its commands, or the list gains build and scan |
| 27 | B2 | `docs/01-Architecture.md`:65; `Makefile`:7 | "each target whose rule line ends in `## `" while the pattern `^[a-z]+:` skips a name with a hyphen or digit; recorded only in `make-help`:13, 136 | latent, low (no such target) | none |
| 28 | P5 | `work/done/kit-2026-10-19-1.md`:14 | Names the kit's checkout path on the author's machine, where earlier kit pages say "the sibling checkout" | weak, low (the public kit's checkout, not a private case) | none |

**Clause answers.** The author answered all four clauses as holds, by their word in the /apply session, without reading the PDFs at this time: chapter 8's update example matches this repository's update to 2026.10.19.1; with a branch per delivery a board reads a `[~]` line from that delivery's branch and the main branch's copy shows it as it was until the merge; `/propose` reads its own line and its `after` lines by slug, from each one's branch or worktree off trunk; `make` with no target prints the eight lines and runs nothing else.

**Findings.** The author confirmed, and the session opened under this review in docs/06:

| Line | Candidates | Files |
|---|---|---|
| `ch08-13-17-next-line` | 1, 7, 8 | chapters 8, 13, 17 and 23, both editions |
| `ch20-merge-and-marks` | 10, 13 | chapter 20, both editions |
| `ch08-13-20-default-review` | 4, 14, 15, 16 | chapters 8, 13 and 20, both editions; after the two lines above, which share its files |
| `ch14-face-retired` | 9 | chapter 14, both editions |
| `docs05-dependency-merged` | 5, 6 | docs/05 §4 |
| `kit-note-work-in-flight` | 2, 18 | `work/kit-proposals.md` |
| `m22-batch-proof` | 22 | the pages of `ch08-update-2026-10-19-1`, `ch12-free-lines-branches` and `ch14-20-read-branches`: records only |
| `readme-make-list` | 26 | `README.md`, `README.pt.md` |
| `docs06-m21-opening` | 25 | docs/06; last, after every other finding, since it edits the queue itself |

Candidate 9 is answered by the author: FACE is being retired, so chapter 14 drops FACE and its note `[^face]` in both editions and keeps a board that reads the queue itself, with nothing to mirror, named after no tool, reading docs/06 and `work/` by slug as the chapter teaches for branches. For `m22-batch-proof`, the three pages' Proof and Done when must agree, and the driver runs `make verify` again before the release. Rejected: 24 (past commits cannot change) and every latent or weak candidate (3, 11, 12, 17, 20, 21, 23, 27, 28). Candidate 19 is corrected on this page, in its Decisions, with no line. No other pair of lines shares a file: `docs05-dependency-merged` stays in docs/05, and chapter 14 is `ch14-face-retired`'s alone.

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
* The leads above go to the checker through the reader of the area holding them; all six lie outside the range's hunks (L3's ch12:25, L5's docs/03:108 and L6's docs/05:176 to 177 as well as L1, L2, L4 and L6's chapters), so each is read by that reader beside its area (corrected by this review, candidate 19).
* A confirmed candidate becomes a `[ ]` line under this review, whether or not it answers a clause of M22: docs/05 §8 puts each finding in the same milestone, as m21-review's Divergence found.
* The end commit and the final path inventory are inputs /apply fixes before reading, not open scope (docs/05 §8).

**Done when.**

* [x] Every line in this review's `after` is `[x]`, and every clause above has the author's answer.
* [x] Base, end commit, the inventory of paths by area, the slow tests (none), each reader's paths read and every checked candidate are recorded on this page.
* [x] Every candidate the author confirms is its own `[ ]` line under this review; nothing is fixed here. Confirmed candidates that share a cause share a line, nine lines in all.
* [x] `make verify` is green after the last edit, both PDFs were built at the end commit for the author's reading, and only this review's changes are staged, with its suggested commit message. The driver stages: this session stages nothing, at the driver's word.

**Divergences.** The Done when's staging is the driver's, who commits this review beside its lanes; this session staged nothing. The review has no Delivery review of its own: docs/05 §7 has no review of a review. The PDFs are those `make book` built with `abb988a`, whose `book/` equals the end commit's.

**Proof.** `make` with no target, the skills' versions and their byte comparison with SETUP.md at `35bdc9a`, and the PDFs' text and start pages, all above; `make verify` green after the last edit of this page.

```commit
docs(m22-review): review M22, nine findings

- seven readers and a checker over 4e283ec..c3ec277, 54 paths read
- the four clauses hold, by the author's word
- 28 candidates: 18 seen, 4 latent, 6 weak; candidate 19 corrected here
- nine finding lines under m22-review, ch14-face-retired among them
- make output and the skills checked against SETUP.md at 35bdc9a

work/done/m22-review.md
```
