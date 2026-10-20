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

**Done when.**

* [ ] Every line in this review's `after` is `[x]`, and every clause above has the review's answer from its reading of the passages in both PDFs, recorded as the review's, not the author's.
* [ ] Base, end commit, the inventory of paths by area, the slow tests (none), each reader's paths read and every checked candidate with its mark are recorded on this page.
* [ ] Every seen candidate is a `[ ]` line under this review, shared causes sharing a line; every latent and weak candidate is listed as dropped; nothing is fixed here.
* [ ] The mechanical checks above are recorded with their results; `make verify` is green after the last edit and `make book` built both PDFs at the end commit, both run by this /apply.
