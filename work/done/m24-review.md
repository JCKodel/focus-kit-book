# m24-review

**Objective.** The author can see whether each promise of M24 holds in both editions and in the installed process, answered by the review's own reading of the passages on the author's word, with every checker-seen candidate recorded as a new line under this review.

**Behaviour.**

* With every line in this review's `after` `[x]`, /apply builds both PDFs at the end commit, reads in both the passages the clause table below names, at their start pages, and answers each clause's question itself: holds, or fails with what the passage says. The page records these answers as the review's, never the author's: the author reads no PDF in this run and tests no clause (docs/05 §8, the paragraph on the person's word).
* The review compares the installed commands and the active documents with focus-kit 2026.10.20 as `work/done/kit-2026-10-20.md` records it (SETUP.md at the kit's `0223e14`), then checks the book's explanations against those rules.
* The author's word that starts the readers and hands the review its tests is already given, relayed by the batch's driver and quoted under Decisions. /apply records the end commit, then launches read-only area readers over one fixed range, `git diff <base>..<end>`; one checker tests each candidate against that same snapshot and labels it seen, latent or weak.
* Each candidate the checker marks seen, low ones included, becomes a `[ ]` line under this review in docs/06, candidates sharing a file or a cause sharing a line; every latent and weak candidate is dropped and listed on this page with its mark. No fix is made here.
* A clause with no answer, a required reader that cannot run, or paths of the range no reader read leave this review waiting as `[?]` with `· resume: apply` and the reason (docs/05 §§4, 8); a partial reading that found nothing never closes it.
* A commit made during the reading does not move the end commit; what it changed is named as outside this reading.
* Edge, the parallel session: `kit-2026-10-20-1` (M25) is `[~]` in another session. A commit of M25 that lands before the reading starts is inside the range: its paths are read by their area's reader and named as M25's, with no clause here. If the reinstall at 2026.10.20.1 is in the range, the skills are checked against 2026.10.20 as M24 left them, `git show 2b66f27:<path>`, and the later version is named, not counted as an M24 failure.
* Edge, the shared tree: readers and the checker read the end commit (`git diff <base>..<end>`, `git show <end>:<path>`), never the working tree, which may hold other sessions' uncommitted edits. The driver's uncommitted docs/06 marks and `work/ch13-19-session-folder.md` are not this review's.

**Contract.** Clause checks from docs/06's M24 paragraph, each against the named deliveries' pages in `work/done/` and the cited chapter sections in both PDFs (`output/one-page-at-a-time.pdf`, `output/uma-pagina-de-cada-vez.pdf`). Lines are en / pt at `2b66f27`; where one number is given it is the same in both.

| Clause | Deliveries and passages | The review's question |
|---|---|---|
| The book teaches focus-kit 2026.10.20 and the repository runs on it | `kit-2026-10-20`: installed skills (`metadata.version` 2026.10.20), docs/05 §2 (:33), §4's board paragraph (:121) and its provenance sentence, §5's Git slot and Publish policy unchanged, AGENTS.md's where-things-stand line (:37), docs/03's `free line`, `kanban board`, `claim` and `remote` rows, ADR-0018's amendment `kit-2026-10-20`; `ch08-update-2026-10-20`: chapter 8, "What the install never touches, and how to update" / "O que a instalação nunca toca, e como atualizar" (:46, the refusal check), "What an update reports" / "O que uma atualização relata" (:56 to :90 / :56 to :94), and the explanation after the excerpt | Does chapter 8's update example match what this repository's update to 2026.10.20 did: the report as a list by document and section, docs/05 §2, §4 and AGENTS.md's line each lacking something with the template's wording proposed, the trunk Git slot with the Publish policy a recorded choice, the refusal check on a copy outside the repository, and the next command with its condition? And does the repository hold what the kit asks, staying on trunk with no delivery branch and nothing pushed? |
| With a branch or a worktree per delivery the branch is the claim of the line, pushed by /propose the moment it is created | `ch12-14-17-20-branch-claim`: chapter 12, "What `/propose` does" / "O que o `/propose` faz" (:27, :28), key points (:171 / :180); chapter 18, "One delivery, one step to undo" / "Uma entrega, um passo para desfazer" (:25, :27, the block's `git push -u origin lend-book` / `emprestar-livro` at :31); chapter 19, "Worktrees in the kit" / "Worktrees no kit" (:179, :194), key points (:350); chapter 20, "The pull request as the team's review" / "O pull request como a revisão do time" (steps 1 and 2, :22 to :26), key points (:87) | Does each edition say that `/propose` checks the remote for the delivery's branch, creates it and pushes it at once, before the page exists, that this branch is the line's claim, that a branch already on the remote means the line is taken unless the definition resumes, that on trunk nothing is created or pushed, and that every later push stays the person's, the pull request opening once the page's commit is pushed? |
| A line whose branch exists on the remote is taken whatever the main branch's queue shows | `ch12-14-17-20-branch-claim`: chapter 14, "At the moment the work changes" / "No momento em que o trabalho muda" (:60, :61 / :61, :62), "The next line, and which run together" / "A próxima linha, e quais rodam juntas" (:72, :73 / :73, :74), key points (free line :185 / :186, kanban :188 / :189); chapter 17, "The manager's session" / "A sessão do gerente" (:119, :132), key points (:151); docs/03 `free line` and `claim` | Asked for the next delivery or where things stand with a branch or a worktree per delivery, does each edition have the session run `git fetch` first, count a line whose branch exists as taken even before any of its marks is pushed, and read the delivery branches, in the words docs/03's `free line` and `claim` rows use? |
| The main branch's queue changes only through merges | `ch12-14-17-20-branch-claim`: chapter 14 :61 / :62; chapter 20 step 4 (:27); `kit-2026-10-20`: docs/05 §4's board paragraph, docs/03 `claim` | Does each edition say that the main branch's docs/06 never carries a claim and its marks arrive only with each delivery's merge, and do chapters 14 and 20 agree with docs/05 §4 and docs/03 on it? |

**Base.** `ac44bea934303f88c3a0aa59f9a386892259dc50` (`docs(m23-review): review M23, thirteen findings`), the commit of m23-review, the previous milestone's review (docs/05 §8, docs/03's `milestone review` row). The range therefore also holds M23's fix round, the thirteen finding lines and the two they led to (`kit-record-step4`, `ch08-next-free-line`, `ch14-board-visibility`, `ch17-23-git-slot-word`, `ch13-23-merge-default`, `ch17-next-free-line`, `ch07-09-manual-wording`, `ch09-slow-tests`, `docs05-author-word`, `m23-records-proof`, `m23-records-crossrefs`, `m22-records-commits`, `manual-link-pointers`, `manual-pypdf-install`, `manual-pip-floor`), which gets no second review (docs/05 §8): the clause checks above are M24's alone, while the readers read the whole range.

**End.** The commit HEAD is when the reading starts; /apply records it before launching any reader, and nothing it records later moves it. Planned: `2b66f27` (`docs(ch12-14-17-20-branch-claim): teach the pushed branch as claim`), HEAD when this page was written; the driver's marks and this page's define commit come after it, and a commit of M25 may too (Behaviour), so /apply records the actual end and recomputes the inventory there.

**Areas.** The paths `git diff --stat -M ac44bea..HEAD` shows today, at `2b66f27` (73 paths, 2259 insertions, 353 deletions), by the areas of docs/05 §5's Milestone review slot. /apply recomputes them at its end commit and places any new path in its area:

* **Build:** `docs/manuals/build-the-book-from-a-clone.md`, `docs/manuals/release-the-book.md`, `scripts/build_book.py`, `scripts/check_examples.py`, `scripts/check_links.py` (5 files), read beside the `Makefile` and README.md / README.pt.md, which the range does not change.
* **Chapters** (22 files), split in two:
  * M24's chapters, both editions: `book/{en,pt}/08-install-and-hosts.md`, `12-propose.md`, `14-queue-states.md`, `17-project-as-assistant.md`, `18-git-essentials.md`, `19-worktrees.md`, `20-team-tools.md` (14 files), every passage the clause table names;
  * the fix round's other chapters, both editions: `book/{en,pt}/07-the-documents.md`, `09-starting-a-project.md`, `13-apply.md`, `23-adoption.md` (8 files).
* **The kit's skills:** `.claude/skills/{analyze,apply,brainstorm,propose}/SKILL.md`, `.claude/skills/{analyze,brainstorm}/references/documents.md`, and the same six under `.agents/skills/` (12 files), each also compared byte for byte with SETUP.md §3 of 2026.10.20 at the kit's `0223e14`.
* **The documents:** `AGENTS.md`, `docs/01-Architecture.md`, `docs/03-Domain.md`, `docs/04-Conventions.md`, `docs/05-Process.md`, `docs/06-Queue.md`, `docs/adr/ADR-0018-six-marks.md` (7 files), and this page, `work/m24-review.md`, which the define commit adds.
* **Delivery records**, the 27 paths under `work/done/` (1941 insertions, 41 deletions), split in two:
  * records 1, M24's three pages: `kit-2026-10-20` (moved from `work/` in the range), `ch08-update-2026-10-20`, `ch12-14-17-20-branch-claim` (389 lines);
  * records 2, M23's fix round: the fifteen finding pages above and the nine earlier pages they edited, `ch08-13-17-next-line`, `ch08-13-20-default-review`, `ch08-update-2026-10-19-2`, `ch10-12-run-manual`, `ch13-apply-run-manual`, `ch20-merge-and-marks`, `docs05-dependency-merged`, `kit-2026-10-19-2`, `readme-run-manual` (24 files).

Count: 5 + 22 + 12 + 7 + 27 = 73.

**Readers.** Four read-only readers on Opus, each keeping the session's advisor, Fable, then one read-only checker on Opus; no other model runs the review (docs/05 §5, Milestone review). At most two of the review's agents run at a time, two readers or the last reader beside the checker, so with the batch's other agents no more than three run at once. Planned, lean, by joining areas a careful reading can hold:

* pair 1: **M24's chapters** (14 files), with chapters 13 and 23 for L1 and L2 and chapter 8 :110 for L5; and **skills, documents and records 1** (12 + 8 + 3 files), the installed kit, the migrated documents and the pages that did it, read together;
* pair 2: **the fix round's chapters and the build** (8 + 5 files); and **records 2** (24 files).

Each reader lists the paths it read.

**Slow tests.** The Verify slot names none (docs/05 §5); none is invented for this review.

**Known candidates for the checker**, raised by M24's proposes and applies without a line of their own; leads to check, not findings. Each names the reader that reads it:

* L1, chapter 13 :28, how `/apply` weighs the next free line off trunk, silent on the claim, left by `ch12-14-17-20-branch-claim`'s Out of scope and reported to the driver. M24 chapters reader, outside the range's M24 hunks.
* L2, chapter 23 :66, the manager reading "each slug's line from its worktree or branch", beside chapter 17's new "from the delivery branches after `git fetch`". M24 chapters reader.
* L3, docs/03's `remote` row cites chapter 18, which teaches push and pull, while `git fetch` is first used in chapter 19; kept by `kit-2026-10-20`'s Delivery review. Skills, documents and records 1 reader.
* L4, `ch08-update-2026-10-20`'s Contract says "reivindicação" is not needed, and its Divergences that the pt excerpt uses it: check both editions' §4 item agree with docs/03. M24 chapters reader.
* L5, chapter 8 :110 / :114, how the update reads each slug's line "from its worktree or branch, local or remote", kept by `ch08-update-2026-10-20`'s Out of scope, while `kit-2026-10-20` dropped "or worktree" from docs/03's `kanban board` and `ch12-14-17-20-branch-claim` did the same in chapter 14's kanban bullet. M24 chapters reader.
* L6, M24's three pages leave `make book` to the batch's driver: this review's `make book` at the end commit is that run, and this page records it (Mechanical checks). Skills, documents and records 1 reader.

**Mechanical checks**, run by /apply at the end commit:

* Every installed skill, `.claude/skills/*/SKILL.md` and `.agents/skills/*/SKILL.md`, carries `metadata.version` `2026.10.20` (or, if 2026.10.20.1 is in the range, at `2b66f27`, Behaviour); the 12 skill files are byte-equal to SETUP.md §3 of `git -C ~/Projects/focus-kit show 0223e14:SETUP.md`, SHA-256 `0b2873c7ee9ee239fffa0184f315e877968931c0350cdbc43f54390cea03a80a`, the record's.
* docs/05 §2's first sentence, §4's board paragraph from "On trunk the board sees it at once." and AGENTS.md's where-things-stand line equal the 2026.10.20 `references/documents.md` word for word; `git branch --list` shows `main` alone and the range pushes nothing (trunk).
* `git status --short book/` is empty before `make book`, so the PDFs hold the end commit's `book/`; both PDFs contain the text of `2b66f27` (`git push -u origin lend-book` / `emprestar-livro`, chapter 18), and /apply records each chapter's start page in both editions and the start page of each section the clause table names.
* `make verify` and `make book` are rerun by /apply after its last edit; their results here are /apply's, not this page's. A failure caused by another session's uncommitted file is named as that session's.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs, `make book` at the end commit; /apply records the start page of every chapter in both editions.

**Out of scope.**

* Fixing any finding: each becomes its own line (docs/05 §8).
* Re-testing M23's clauses or its findings: m23-review answered the clauses, and the fix round is read by the area readers, not tested by clause.
* M25 and later: their lines, pages and commits are theirs; any in the range is read, not reviewed by clause (Behaviour).
* A fresh-clone rerun: no delivery of M24 changed a build step; the fix round's manual changes are read by the build reader against the `Makefile` and `scripts/`.
* Changing the readers' model or the slot: docs/05 §5 owns it.
* The author's reading of the PDFs, the author's answer to any clause and the author's confirmation of candidates: not part of this run, by the author's word (Decisions taken alone).

**Decisions from the documents.**

* The base is m23-review's commit, the previous milestone's review, the first of docs/05 §8's cases.
* The fix round is read by the area readers but has no clause here (docs/05 §8: findings get no second review).
* The kit's version and its source are `kit-2026-10-20`'s: 2026.10.20 at `0223e14`, read from the kit's history.
* The review's session takes the clause tests and the confirmation of seen candidates because the author's word, quoted below, gives them to it (docs/05 §8, the paragraph on the person's word, added by `docs05-author-word`); the checker, the range and the `[?]` for paths not read stay as §8 says.
* The end commit and the final path inventory are inputs /apply fixes before reading, not open scope (docs/05 §8).

**Decisions taken alone** (the batch's driver asked for recommended answers; correct them in the review).

* The author's word for this run, relayed by the driver and quoted as docs/05 §8 asks: "review and fixes directly": the review's own session answers the clause tests by reading the passages, and checker-seen candidates become `[ ]` lines under m24-review; latent and weak ones are dropped and listed. The author reads no PDF in this run.
* "Seen" includes "seen, low": every seen candidate becomes a line; candidates sharing a file or a cause share one line, as m23-review grouped them.
* M24's paragraph is taken as four clauses: the opener (the book teaches 2026.10.20 and the repository runs on it), then the claim sentence in three, by what a reader must say: the branch pushed by /propose as the claim; a line with a remote branch taken whatever main shows; main's queue changing only through merges. Different passages answer each.
* `kit-2026-10-20` answers the opener with `ch08-update-2026-10-20`, and `ch12-14-17-20-branch-claim` the other three, now over chapters 12, 14, 17, 18, 19 and 20, as its queue line reads; every delivery of M24 answers a clause.
* Lean readers: four, not seven. The skills, the documents and M24's three records join, since each record is read against the installed files and documents it changed; the fix round's chapters join the build, both small; the chapters split as M24's (every clause passage in one reader) and the fix round's; the records as M24's and the fix round's.
* "At most three agents in total" is read as at most two of the review's agents at a time, the checker allowed to start beside the last reader on the candidates already in, so the batch's other agent keeps its slot.
* The leads above go to the checker through the reader of the area holding them; L1 lies outside the range's M24 hunks and is read beside its area.
* A seen candidate becomes a `[ ]` line under this review whether or not it answers a clause of M24: docs/05 §8 puts each finding in the same milestone.

**Decisions taken alone in /apply** (recommended answers, the batch's rule).

* The readers ran as planned, two at a time: M24's chapters beside the skills, documents and records 1; then, as each slot freed, the fix round's chapters with the build, records 2, and the checker beside records 2, the records 2 candidates sent to it when they came in. Never more than two of this review's agents at once.
* P8 is seen but lies on M25's in-flight page, `work/kit-2026-10-20-1.md`, as does P2's item at its :64: no line here; they are handed to the driver for that page's own /apply, as m23-review left its P6 to M24.
* Chapter 13 :28 (L1, inside C2) goes into this review's line although `ch12-14-17-20-branch-claim` set it aside: the later line `ch13-19-claim-script`, in the driver's uncommitted queue, teaches the claim script, not how `/apply` weighs the next free line.
* Lines are grouped wide, as the driver asked: chapters by cause (reading lines off trunk; `git fetch` and the branch reused; chapter 7 alone; docs/03's `free line` alone), records in two lines, one for what a Done when ticks, one for what a page cites.

**End commit.** `2fccad2dd42d422ac7431880c4c2c69e1ac3e7b8` (`docs(queue): define kit-2026-10-20-1`), HEAD when the reading started, recorded before any reader ran. Nothing was committed during the reading. The range holds two commits after the planned `2b66f27`: `8183fa5` (this page's define) and `2fccad2` (M25's define, adding `work/kit-2026-10-20-1.md` and its docs/06 lines). The reinstall at 2026.10.20.1 is not in the range: every skill is at 2026.10.20 at the end commit.

**Inventory at the end commit.** `git diff --stat -M ac44bea..2fccad2`: 75 paths, 2442 insertions, 355 deletions. The two paths beyond the planned 73 go to the documents: `work/m24-review.md` (this page) and `work/kit-2026-10-20-1.md` (M25's, read and named as M25's, no clause). Build 5, chapters 22 (M24's 14, the fix round's 8), skills 12, documents 9, records 27 (records 1: 3, records 2: 24): 75.

**Reading.** Four read-only readers on Opus with the session's advisor, then one checker on Opus, all on `git show 2fccad2:<path>` and the range diff, never the working tree. Paths read against the range: all 75.

* M24's chapters (C): the 14 chapter files whole and through the range diff, chapters 13 and 23 in both editions for L1 and L2, the three M24 pages, the propose and apply skills, docs/03, docs/05 §§2, 4, 5, AGENTS.md :37 and SETUP.md at `0223e14`.
* Skills, documents and records 1 (P): the 12 skill files, AGENTS.md, docs/01, docs/03, docs/04, docs/05, docs/06 (committed), ADR-0018, this page, `work/kit-2026-10-20-1.md`, the three M24 pages; chapters 8, 18 and 19 by grep for L3; SETUP.md at `0223e14` and `9be385a`.
* The fix round's chapters and the build (D): chapters 7, 9, 13 and 23 in English whole, chapters 7 and 9 in Portuguese whole, pt chapter 13 in parts and pt chapter 23 without its lines 56 to 70, each also through the range diff; the range's pt 23 hunk (:64) was read in the diff, and reader C read pt 13 and pt 23 whole. The two manuals and three scripts, beside the `Makefile` and README.md / README.pt.md :15 to :30; the link check's file and URL functions run on the end commit's tree.
* Records 2 (S): the 24 pages whole and through the range diff, with the commits each delivery made, docs/06's M22 to M25, docs/05 §§5, 8 and SETUP.md at `44132c4`.

**Mechanical checks**, run by /apply at `2fccad2`:

* The eight installed `SKILL.md`, under `.claude/skills/` and `.agents/skills/`, carry `metadata.version` `2026.10.20`. `git -C ~/Projects/focus-kit show 0223e14:SETUP.md` has SHA-256 `0b2873c7ee9ee239fffa0184f315e877968931c0350cdbc43f54390cea03a80a`, the record's; the twelve skill files equal SETUP §3.1 to §3.5 of it byte for byte (`cmp` of `git show 2fccad2:<path>` against each cut section).
* docs/05 §2's first sentence of the paragraph "Before /propose changes the queue or the page" (:32 to :35), §4's board paragraph from "On trunk the board sees it at once." (:119 to :126) and AGENTS.md :37 equal the 2026.10.20 `references/documents.md` word for word, compared with whitespace normalized (the project keeps its wrapping). `git branch --list` shows `main` alone; `origin/main` is `695d69f` (`chore(release): v1.2.6`), an ancestor of the base, so nothing in the range was pushed (trunk).
* `git status --short book/` was empty before `make book`, so both PDFs hold the end commit's `book/`; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` with their EPUBs. The en PDF holds `git push -u origin lend-book` (page 180) and the pt PDF `git push -u origin emprestar-livro` (page 186), the text of `2b66f27`.
* `make verify`: green after the last edit of this page (Proof).

**Start pages** in the PDFs (en / pt): prologue 5 / 5, 1: 11 / 11, 2: 19 / 19, 3: 24 / 24, 4: 40 / 41, 5: 54 / 56, 6: 63 / 65, 7: 68 / 70, 8: 79 / 82, 9: 90 / 94, 10: 99 / 103, 11: 106 / 110, 12: 116 / 121, 13: 126 / 131, 14: 142 / 148, 15: 153 / 159, 16: 162 / 168, 17: 170 / 176, 18: 178 / 184, 19: 189 / 196, 20: 206 / 214, 21: 212 / 220, 22: 217 / 226, 23: 223 / 233, 24: 229 / 239. The clauses' sections (en / pt): chapter 8, "What the install never touches, and how to update" 80 / 83, "What an update reports" 81 / 84, key points 88 / 92; chapter 12, "What `/propose` does" 117 / 122, key points 124 / 129; chapter 14, "At the moment the work changes" 144 / 150, "The next line, and which run together" 145 / 151, key points 151 / 157; chapter 17, "The manager's session" 175 / 181, key points 176 / 183; chapter 18, "One delivery, one step to undo" 179 / 185, key points 187 / 194; chapter 19, "Worktrees in the kit" 196 / 204, key points 204 / 212; chapter 20, "The pull request as the team's review" 207 / 215, key points 210 / 219.

**Clause answers**, the review's own reading of the passages at the end commit in both editions, the PDFs built from it; not the author's, who read nothing in this run.

* The book teaches focus-kit 2026.10.20 and the repository runs on it: holds. Chapter 8 (en/pt :56 to :90 / :94) shows the report as a list by document and section; docs/05 §2, §4 and AGENTS.md's line each lack something, with the template's wording proposed, word for word docs/05 :33, :121 and AGENTS.md :37 (backticks dropped); the Git slot is trunk, a recorded choice, with the Publish policy; :46 the refusal on a copy outside the repository, as the record's Refusal case; `Next: /propose ch08-update-2026-10-20, once kit-2026-10-20 is [x].`, the record's Step 5 with its condition. The repository holds what the kit asks (Mechanical checks): skills at 2026.10.20, the migrated passages, trunk with `main` alone and nothing pushed.
* With a branch or a worktree per delivery the branch is the claim, pushed by /propose the moment it is created: fails at chapter 19 :179 alone. Chapter 12 :28 says `/propose` checks the remote, creates the branch and pushes it at once, before the page exists, that a branch already there means the line is taken unless the definition resumes, and that on trunk nothing is created; :171 / :180 call it the line's claim; 18 :25 and :31 and 20 step 1 (:22, :23) say the same push; 19 :194 keeps every later push the person's; 20 step 2 (:24, :25) opens the pull request once the page's commit is pushed, the second push. But 19 :179 has `/propose` reuse "the one that exists" with no resume condition (C1).
* A line whose branch exists on the remote is taken whatever the main branch's queue shows: fails in chapter 17; chapter 14 holds. Chapter 14 :72 / :73 has the session run `git fetch` first and count a line whose branch exists as taken, :73 / :74 even before any of its marks is pushed, in docs/03's `free line` and `claim` words, :185 / :186 the same. Chapter 17 :132 and :151 run `git fetch` and read the delivery branches, but nowhere say that a line whose branch exists is taken or in flight before its marks are pushed (C3).
* The main branch's queue changes only through merges: holds. Chapter 14 :61 / :62 says the branch is the claim, on the remote before any mark is pushed, "so the main branch's queue changes only through merges"; 20 step 4 (:27) that it "changes only through merges and holds what has landed", a `[~]` or `[*]` set on a branch being on that branch only; docs/05 §4's board paragraph and docs/03's `claim` say the same.

**Candidates**, marked by the checker at `2fccad2` (seen: true in the file today; latent: nothing triggers it today; weak: the claim does not hold as stated). Ids are the readers': C M24's chapters, P skills, documents and records 1, D the fix round's chapters and the build, S records 2. Lines are both editions unless the pt line is given; record pages are under `work/done/`. 26 ids: 23 seen (5 medium, 18 low, none high), no latent, 3 weak. The leads: L1, L2 and L5 are in C2; L3 is C4 and P1; L4 is no candidate (chapter 8 en :69 / pt :69 to :70 agree with docs/03's `claim | reivindicação`, :116); L6 is P2.

| id | file:line | mark | claim |
|---|---|---|---|
| C1 | 19-worktrees :179 | seen, medium | `/propose` "reuses the one that exists" with no resume condition, against 12 :28 and 18 :25; the kit's own words |
| C2 | 08 :110 / pt :114; 13 :28; 23 :66 | seen, low | lines read "from its worktree or branch" with no `git fetch` and no rule that an existing branch means taken |
| C3 | 17 :132, :151 | seen, low | fetches, but never says a line whose branch exists is taken before its marks are pushed (clause 3) |
| C4 | 18 :71 (fetch used at 08 :76, 12 :27, 14 :61, :72, :185, 17 :119, :132) | seen, medium | no chapter says what `git fetch` does; 18 :25 uses "remote" before :71 defines it; `-u` (:31) explained nowhere |
| C5 | pt 08 :71, :77 | seen, low | "tomada" where pt 12, 14, 18, 19 and 20 say "ocupada" |
| C6 | 14 :62, :172 / pt :63, :173 vs :188 / pt :189 | seen, low | body "from its worktree, or from its branch", key point "from each slug's own branch" |
| C7 | 18 :27 | weak | :25 two lines above already says "reuses it when the definition resumes" |
| P1 | docs/03-Domain.md :82 | seen, low | `remote` defines `git fetch` and cites chapter 18, which never mentions fetch |
| P2 | kit-2026-10-20 :64; ch08-update-2026-10-20 :94; ch12-14-17-20-branch-claim :94; `work/kit-2026-10-20-1.md` :64 (M25's) | seen, medium | `make book` ticked with no run and no PDF paths in the Proof; kit :65's staging part weak (its Divergences records it) |
| P3 | ch12-14-17-20-branch-claim :61, :65, :68; kit-2026-10-20 :40 | seen, low | name slugs and milestones M26 to M29 that no committed line holds |
| P4 | ch12-14-17-20-branch-claim :38, :43 | seen, low | headings "Merges and the unit of work" and "A pull request per delivery" exist nowhere |
| P5 | kit-2026-10-20 :3, :40; ch08-update-2026-10-20 :59, :67 | seen, low | the sibling line's chapters as "12, 14, 17 and 20", widened to 18 and 19 |
| P6 | docs/03-Domain.md :115 | seen, low | "the first one ... is the next delivery" also counts a free line another session holds; 14 :185 says "no session holds" |
| P7 | ch08-update-2026-10-20 :95, :111; ch12-14-17-20-branch-claim :110 | seen, low | Delivery review ticked "as docs/05 §5 says", the advisor unrecorded |
| P8 | `work/kit-2026-10-20-1.md` :9, :42 | seen, low | M25's page calls m24-review `[~]`; committed docs/06 :605 has `[>]` (Decisions taken alone in /apply) |
| D1 | 07 :82 / pt :83 | seen, low | the person "reviews the commit" after the slot lets the agent merge; 13 :169, citing chapter 7, says "the commit or the merge" |
| S1 | ch14-board-visibility :57; ch17-23-git-slot-word :74; ch13-23-merge-default :73; ch17-next-free-line :62; ch08-next-free-line :53; ch07-09-manual-wording :56; ch09-slow-tests :37; manual-pypdf-install :44 | seen, medium | `make book` run and PDF paths ticked, none in the Proof; some ticks say the Proof records it |
| S2 | kit-record-step4 :84 vs :91; m22-records-commits :89 vs :102; m23-records-crossrefs :68; ch07-09-manual-wording :57, :75; ch09-slow-tests :55; docs05-author-word :54, :76; the other fix-round pages' review items | seen, medium | Delivery review ticked "with the session's advisor" or "as docs/05 §5 says", the advisor unrecorded; some reviews read only the chapter files |
| S3 | kit-record-step4 :7, :64, :73; kit-2026-10-19-2 :84, :87 | seen, low | the Environments pointer filed as "which step 4 does not check", though step 4 checks a slot's shape and :87 says so |
| S4 | ch13-23-merge-default :36 | seen, low | `ch12-14-parallel-token` called M24's; docs/06 :615 has it under M25 |
| S5 | ch07-09-manual-wording :3, :32, :69 | weak | the Objective speaks of the reader; nothing false is recorded |
| S6 | ch08-next-free-line :23 | seen, low | Step 5 cited at :89; it is kit-2026-10-19-2 :93 |
| S7 | ch08-next-free-line :10, :24, :58 | seen, low | says ch07-09-manual-wording edits chapter 8 at pt :71; its page and commit `7660dfc` do not |
| S8 | manual-link-pointers :59 | seen, low | ticks "prints nothing" while its parenthesis says it prints three messages |
| S9 | ch08-13-17-next-line :72; ch08-13-20-default-review :69 | weak | the items allow the driver's run, and the range's edits did not touch them |
| S10 | ch17-23-git-slot-word :37; ch13-23-merge-default :36 | seen, low | name three slugs no committed line holds, `ch13-19-session-folder` in M25 against m23-records-crossrefs :57's M26 |

Dropped, weak: C7, S5, S9. No latent. P8 seen, left to M25's page (Decisions taken alone in /apply).

**Findings.** The seen candidates, grouped by file or cause, six lines handed to the driver to open under this review in docs/06 (this session does not edit docs/06):

```
[ ] ch08-23-fetch-taken      chapters 8, 13, 14, 17 and 23: wherever a session reads lines off trunk it runs `git fetch` first and counts a line whose branch exists as taken before any mark is pushed (C2, C3), chapter 14 :62 and :172 read each slug's line from its branch as its key point does (C6), and pt chapter 8's excerpt says "ocupada" (C5); both editions · after m24-review
[ ] ch18-19-fetch-resume     chapters 18 and 19: chapter 18 says what a remote, `git fetch` and `git push -u` are where it first uses them, so docs/03's `remote` row cites it truly (C4, P1), and chapter 19 :179 reuses an existing branch only when the definition resumes (C1); both editions · after m24-review
[ ] ch07-review-merge        chapter 7 :82: where the Git slot lets the agent commit and merge, the person reviews the commit or the merge, as chapter 13 :169 says citing it (D1); both editions · after m24-review
[ ] docs03-free-line-held    docs/03's `free line` row: the next delivery is the first free line no session holds, as chapter 14 :185 says (P6) · after m24-review
[ ] m24-records-proof        the pages of kit-2026-10-20, ch08-update-2026-10-20, ch12-14-17-20-branch-claim and M23's fix round: Done when ticks only what the Proof records, the `make book` run pointing to m24-review's at `2fccad2`, the Delivery review with the advisor and what it read, and manual-link-pointers' grep as it printed (P2, P7, S1, S2, S8) · after m24-review
[ ] m24-records-crossrefs    the pages of kit-2026-10-20, ch08-update-2026-10-20, ch12-14-17-20-branch-claim, ch13-23-merge-default, ch17-23-git-slot-word, ch08-next-free-line, kit-record-step4 and kit-2026-10-19-2: no slug or milestone no committed line holds, the real headings, the branch-claim line's six chapters, the right milestone and line cites, no chapter 8 edit for ch07-09-manual-wording, and the Environments pointer as a slot shape step 4 checks (P3, P4, P5, S3, S4, S6, S7, S10) · after m24-review
```

**Done when.**

* [x] Every line in this review's `after` is `[x]`, and every clause above has the review's answer from its reading of the passages in both PDFs, recorded as the review's, not the author's.
* [x] Base, end commit, the inventory of paths by area, the slow tests (none), each reader's paths read and every checked candidate with its mark are recorded on this page.
* [x] Every seen candidate but P8 (Decisions taken alone in /apply) is in a `[ ]` line under this review, shared causes sharing a line, six lines, handed to the driver to add to docs/06; every latent and weak candidate is listed as dropped; nothing is fixed here.
* [x] The mechanical checks above are recorded with their results; `make verify` is green after the last edit and `make book` built both PDFs at the end commit, both run by this /apply; the staging is the driver's at its word: this session staged nothing.

**Divergences.** The finding lines are not in docs/06: the batch's lane rules leave docs/06 to the driver, who adds the six lines above under m24-review and marks it `[x]`. The staging and the commit are the driver's. P8 is seen but opens no line here, being M25's in-flight page. Two clause answers record failures (C1 in clause 2, C3 in clause 3), each already a seen candidate in a finding line.

**Proof.** The skills' versions and their byte comparison with SETUP.md at `0223e14`, the migrated passages, the branch and push state, and the PDFs' text and start pages, all above; `make book` run by this /apply at `2fccad2` with `book/` clean; `make verify` green after the last edit of this page.

**Delivery review.** One read-only Opus agent with the advisor, run once the readers and the checker had ended, read this page against its define version at `2fccad2`, docs/04, docs/05 §§5, 6 and 8, docs/06's line format and the cited files at the end commit. It found five: this paragraph, which said no review ran; `kit-2026-10-19-2` missing from `m24-records-crossrefs`'s pages though S3 sits on it; clauses 2 and 3 answered "holds" with a failure, where Behaviour asks "holds, or fails"; the L4 note's lines read as docs/03's; P2's row without M25's :64. All fixed here. It confirmed the counts, the six lines' format, slugs and coverage (every seen id but P8), the inventory, the mechanical checks, the clause answers' cited lines in both editions and a dozen candidates.

```commit
docs(m24-review): review M24, six findings

- four readers and a checker over ac44bea..2fccad2, 75 paths read
- clauses 1 and 4 hold; 2 fails at chapter 19 :179, 3 at chapter 17
- 26 candidates: 23 seen, 3 weak; P8 left to M25's page
- six finding lines under m24-review for docs/06
- skills byte-equal to SETUP.md at 0223e14; make book at the end

work/done/m24-review.md
```
