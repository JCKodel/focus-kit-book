# m25-review

**Objective.** The author can see whether each promise of M25 holds in both editions and in the installed process, answered by the review's own reading of the passages on the author's word, with every checker-seen candidate recorded as a new line under this review.

**Behaviour.**

* With every line in this review's `after` `[x]`, /apply builds both PDFs at the end commit, reads in both the passages the clause table below names, at their start pages, and answers each clause's question itself: holds, or fails with what the passage says. The page records these answers as the review's, never the author's: the author reads no PDF in this run and tests no clause (docs/05 §8, the paragraph on the person's word).
* The review compares the installed commands and docs/05 §4 with focus-kit 2026.10.20.1 as `work/done/kit-2026-10-20-1.md` records it (SETUP.md at the kit's `9be385a`), then checks the book's explanations against those rules.
* The author's word that starts the readers and hands the review its tests is already given, relayed by the batch's driver and quoted under Decisions taken alone. /apply records the end commit, then launches read-only area readers over one fixed range, `git diff <base>..<end>`; one checker tests each candidate against that same snapshot and labels it seen, latent or weak.
* Each candidate the checker marks seen, low ones included, becomes a `[ ]` line under this review in docs/06, candidates sharing a file or a cause sharing a line; every latent and weak candidate is dropped and listed on this page with its mark. No fix is made here.
* A clause with no answer, a required reader that cannot run, or paths of the range no reader read leave this review waiting as `[?]` with `· resume: apply` and the reason (docs/05 §§4, 8); a partial reading that found nothing never closes it.
* A commit made during the reading does not move the end commit; what it changed is named as outside this reading.
* Edge, the next milestone: the driver's uncommitted docs/06 holds an M26 (focus-kit 2026.10.20.2) that the committed queue does not, and `work/ch13-19-session-folder.md` is untracked; neither is this review's. A commit of M26 that lands before the reading starts is inside the range: its paths are read by their area's reader and named as M26's, with no clause here. If a reinstall at 2026.10.20.2 is in the range, the skills are checked against 2026.10.20.1 as M25 left them, `git show 395975a:<path>`, and the later version is named, not counted as an M25 failure.
* Edge, the shared tree: readers and the checker read the end commit (`git diff <base>..<end>`, `git show <end>:<path>`), never the working tree, which may hold other sessions' uncommitted edits.

**Contract.** Clause checks from docs/06's M25 paragraph, each against the named deliveries' pages in `work/done/` and the cited chapter sections in both PDFs (`output/one-page-at-a-time.pdf`, `output/uma-pagina-de-cada-vez.pdf`). Lines are en / pt at `395975a`; where one number is given it is the same in both. The paragraph's "`-` waiting for them to be `[>]` or `[x]`" is read as docs/05 §4 and the chapters say it: `[>]` or beyond before /propose, `[x]` before /apply.

| Clause | Deliveries and passages | The review's question |
|---|---|---|
| The book teaches focus-kit 2026.10.20.1 and the repository runs on it | `kit-2026-10-20-1`: installed skills (`metadata.version` 2026.10.20.1), docs/05 §4's first paragraph and its last paragraph removed, docs/03's `parallel token` and `queue line` rows, ADR-0018's amendment, docs/06's header; `ch08-update-2026-10-20-1`: chapter 8, "What an update reports" / "O que uma atualização relata" (:48 to :112 / :48 to :115), the excerpt's §4 item (:64 to :75), its Git slot item and its `Next:` line, and the explanation after the excerpt | Does chapter 8's update example match what this repository's update to 2026.10.20.1 did: the report as a list by document and section, docs/05 §4 lacking the token with the template's first paragraph proposed whole and its last paragraph removed, the trunk Git slot a recorded choice with the Publish policy, and the next command with its condition, as the record's Migration report and Step 5 say? And does the repository hold what the kit asks: skills at 2026.10.20.1, docs/05 §4 in the template's words, trunk with no branch and nothing pushed? |
| A queue line may carry `(PA)` after the slug, saying whether its /propose and its /apply may run while the lines above it are in flight, `-` waiting for them to be `[>]` or `[x]` | `ch12-14-parallel-token`: chapter 11, "The line" / "A linha" (:16), key points (:191 / :196); chapter 14, "The next line, and which run together" / "A próxima linha, e quais rodam juntas" (:84 to :104 / :85 to :105, the library block at :95 to :100 / :96 to :101), key points (:206 / :207); chapter 13, "What `/apply` does" / "O que o `/apply` faz" (:26) | Does each edition say that the token is two letters right after the slug, the first for `/propose`, the second for `/apply`, `P` that the definition takes nothing from the pages above, `A` that the build touches none of their files, a `-` waiting for every line above to be `[>]` or beyond before `/propose` and `[x]` before `/apply`, `after` holding both, a token read against every line above, in docs/03's and docs/05 §4's words? |
| Whoever changes the queue re-judges the tokens | `ch12-14-parallel-token`: chapter 11, "Changing the queue" / "Mudando a fila" (:179 / :184); chapter 12, "What `/propose` does" / "O que o `/propose` faz" (:31); chapter 14 (:80 / :81, :105 / :106) | Does each edition say that whoever adds, moves or changes a line re-judges the tokens the change affects, that `/propose` corrects a line's token from its page once it knows what the page takes and which files the Contract touches, and that `/brainstorm` writes them for a first milestone run as several sessions, with a link that leads where that is taught? |
| /propose and /apply wait as the token says | `ch12-14-parallel-token`: chapter 12 (:26), key points (:172 / :181); chapter 13 (:32, :33), key points (:273); chapter 14 (:32, :106 / :107) | Does each edition have `/propose` refuse to start on a line whose token has `-` first while a line above is not yet `[>]`, and `/apply` refuse on one whose token has `-` second while a line above is not yet `[x]`, each saying what it waits on and leaving the mark as it is, in agreement with docs/05 §4 and the installed propose and apply skills? |

**Base.** `cd045ba` (`docs(m24-review): review M24, six findings`), the commit of m24-review, the previous milestone's review (docs/05 §8, docs/03's `milestone review` row). The range therefore also holds M24's fix round, the six finding lines and the one they led to (`ch08-23-fetch-taken`, `ch18-19-fetch-resume`, `ch18-switch-resume`, `ch07-review-merge`, `docs03-free-line-held`, `m24-records-proof`, `m24-records-crossrefs`), which gets no second review (docs/05 §8): the clause checks above are M25's alone, while the readers read the whole range.

**End.** The commit HEAD is when the reading starts; /apply records it before launching any reader, and nothing it records later moves it. Planned: `395975a` (`docs(ch12-14-parallel-token): chapters 11 to 14 teach the (PA) token`), HEAD when this page was written; the driver's marks and this page's define commit come after it, and a commit of M26 may too (Behaviour), so /apply records the actual end and recomputes the inventory there.

**Areas.** The paths `git diff --stat -M cd045ba..HEAD` shows today, at `395975a` (64 paths, 1573 insertions, 402 deletions), by the areas of docs/05 §5's Milestone review slot. /apply recomputes them at its end commit and places any new path in its area:

* **Build:** no path; the range changes no script, manual or `Makefile`, so no reader is planned for it.
* **Chapters** (20 files), split in two:
  * M25's chapters, both editions: `book/{en,pt}/08-install-and-hosts.md`, `11-queue-and-milestones.md`, `12-propose.md`, `13-apply.md`, `14-queue-states.md` (10 files), every passage the clause table names; chapters 8, 13 and 14 also hold `ch08-23-fetch-taken`'s hunks, read here with them;
  * the fix round's other chapters, both editions: `book/{en,pt}/07-the-documents.md`, `17-project-as-assistant.md`, `18-git-essentials.md`, `19-worktrees.md`, `23-adoption.md` (10 files).
* **The kit's skills:** `.claude/skills/{analyze,apply,brainstorm,propose}/SKILL.md`, `.claude/skills/{analyze,brainstorm}/references/documents.md`, and the same six under `.agents/skills/` (12 files), each also compared byte for byte with SETUP.md §3 of 2026.10.20.1 at the kit's `9be385a`.
* **The documents:** `docs/03-Domain.md`, `docs/05-Process.md`, `docs/06-Queue.md`, `docs/adr/ADR-0018-six-marks.md` (4 files), and this page, `work/m25-review.md`, which the define commit adds.
* **Delivery records**, the 28 paths under `work/done/`, split in two:
  * records 1, M25's three pages: `kit-2026-10-20-1` (moved from `work/` in the range), `ch08-update-2026-10-20-1`, `ch12-14-parallel-token`;
  * records 2, M24's fix round: the seven finding pages above and the eighteen earlier pages `m24-records-proof` and `m24-records-crossrefs` edited, `ch07-09-manual-wording`, `ch08-next-free-line`, `ch08-update-2026-10-20`, `ch09-slow-tests`, `ch12-14-17-20-branch-claim`, `ch13-23-merge-default`, `ch14-board-visibility`, `ch17-23-git-slot-word`, `ch17-next-free-line`, `docs05-author-word`, `kit-2026-10-19-2`, `kit-2026-10-20`, `kit-record-step4`, `m22-records-commits`, `m23-records-crossrefs`, `manual-link-pointers`, `manual-pip-floor`, `manual-pypdf-install` (25 files).

Count: 0 + 20 + 12 + 4 + 28 = 64.

**Readers.** Four read-only readers on Opus, each keeping the session's advisor, Fable, then one read-only checker on Opus; no other model runs the review (docs/05 §5, Milestone review). At most two of the review's agents run at a time, so with the review's own session no more than three run at once. Planned, lean:

* pair 1: **M25's chapters** (10 files), with both editions' chapter 9 for L1; and **skills, documents and records 1** (12 + 4 + 3 files, and this page), the installed kit, the migrated documents and the pages that did it, read together;
* pair 2: **the fix round's chapters** (10 files); and **records 2** (25 files). The checker starts when a slot frees, beside the last reader, on the candidates already in.

Each reader lists the paths it read.

**Slow tests.** The Verify slot names none (docs/05 §5); none is invented for this review.

**Known candidates for the checker**, leads to check, not findings. Each names the reader that reads it:

* L1, chapter 14 :105 / pt :106: "`/brainstorm` writes them for a first milestone that will run as several sessions ([chapter 9](09-starting-a-project.md))", while chapter 9 says nothing about tokens in either edition; the brainstorm skill's step 6 (`SKILL.md` :42) is where the kit says it. M25's chapters reader.
* L2, the records' habit of claiming runs or reviews they do not record, the cause of M24's P2, P7, S1 and S2: for M25's three pages and the seven new fix-round pages, each Done when tick against what the Proof records (`make book` run, at which commit, and both PDF paths), and each Delivery review against what it says it read; `ch12-14-parallel-token`'s review says it did not read docs/04 directly, and `kit-2026-10-20-1`'s Proof runs `make book` on the tree at `0bc6864` with uncommitted changes. Skills, documents and records 1 reader for records 1; records 2 reader for the rest.
* L3, `ch12-14-parallel-token` :90 names `ch13-19-session-folder` (M26), `ch12-14-18-several-slugs` (M27) and `ch14-after-over-token` (M29), none of which the committed docs/06 at `395975a` holds, the cause of M24's P3 and S10. Skills, documents and records 1 reader.
* L4, `ch12-14-parallel-token`'s Contract counts "Ten files" where its Divergences says eight. Skills, documents and records 1 reader.

**Mechanical checks**, run by /apply at the end commit:

* Every installed skill, `.claude/skills/*/SKILL.md` and `.agents/skills/*/SKILL.md`, carries `metadata.version` `2026.10.20.1` (or, if a later version is in the range, at `395975a`, Behaviour); the 12 skill files are byte-equal to SETUP.md §3 of `git -C ~/Projects/focus-kit show 9be385a:SETUP.md`, SHA-256 `bc2751630e03cd60628dfb279b3c2dd997b5b43158cba1a24b2adffb40209576`, the record's.
* docs/05 §4's first paragraph equals the 2026.10.20.1 `references/documents.md` word for word, whitespace normalized, and its old last paragraph is gone; `git branch --list` shows `main` alone and the range pushes nothing (trunk).
* `git status --short book/` is empty before `make book`, so the PDFs hold the end commit's `book/`; both PDFs contain the text of `395975a` (`search-catalog (PA)` / `buscar-catalogo (PA)`, chapter 14), and /apply records each chapter's start page in both editions and the start page of each section the clause table names.
* `make verify` and `make book` are rerun by /apply after its last edit; their results here are /apply's, not this page's. A failure caused by another session's uncommitted file is named as that session's.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs, `make book` at the end commit; /apply records the start page of every chapter in both editions.

**Out of scope.**

* Fixing any finding: each becomes its own line (docs/05 §8).
* Re-testing M24's clauses or its findings: m24-review answered the clauses, and the fix round is read by the area readers, not tested by clause.
* M26 and later: their lines, pages and commits are theirs; any in the range is read, not reviewed by clause (Behaviour).
* A fresh-clone rerun: no path of the build is in the range.
* Changing the readers' model or the slot: docs/05 §5 owns it.
* The author's reading of the PDFs, the author's answer to any clause and the author's confirmation of candidates: not part of this run, by the author's word (Decisions taken alone).

**Decisions from the documents.**

* The base is m24-review's commit, the previous milestone's review, the first of docs/05 §8's cases.
* The fix round is read by the area readers but has no clause here (docs/05 §8: findings get no second review).
* The kit's version and its source are `kit-2026-10-20-1`'s: 2026.10.20.1 at `9be385a`, read from the kit's history.
* The review's session takes the clause tests and the confirmation of seen candidates because the author's word, quoted below, gives them to it (docs/05 §8, the paragraph on the person's word); the checker, the range and the `[?]` for paths not read stay as §8 says.
* The end commit and the final path inventory are inputs /apply fixes before reading, not open scope (docs/05 §8).
* The line's token `(--)` holds: this review reads every page and file above it, so neither its definition nor its build may run beside them (docs/05 §4); no correction.

**Decisions taken alone** (the batch's driver asked for recommended answers; correct them in the review).

* The author's word for this run, relayed by the driver and quoted as docs/05 §8 asks: "review and fixes directly": the review's own session answers the clause tests by reading the passages, and checker-seen candidates become `[ ]` lines under m25-review; latent and weak ones are dropped and listed. The author reads no PDF in this run.
* "Seen" includes "seen, low": every seen candidate becomes a line; candidates sharing a file or a cause share one line, as m24-review grouped them.
* M25's paragraph is taken as four clauses: the opener (the book teaches 2026.10.20.1 and the repository runs on it), then the token sentence in three, by what a reader must say: what the token is and what `-` waits for; who re-judges it; the two commands waiting as it says. Different passages answer each.
* `kit-2026-10-20-1` answers the opener with `ch08-update-2026-10-20-1`, and `ch12-14-parallel-token` the other three, now over chapters 11 to 14, as its queue line reads; every delivery of M25 answers a clause.
* "At most three agents in total, the review session counting" is read as at most three at once: two of the review's agents at a time beside its session, the checker starting beside the last reader.
* Lean readers, four: the build area is empty; the skills, the documents and M25's three records join, since each record is read against the installed files and documents it changed; the chapters split as M25's (every clause passage in one reader) and the fix round's; the records as M25's and the fix round's.
* A seen candidate becomes a `[ ]` line under this review whether or not it answers a clause of M25: docs/05 §8 puts each finding in the same milestone.

**Done when.**

* [x] Every line in this review's `after` is `[x]`, and every clause above has the review's answer from its reading of the passages in both PDFs, recorded as the review's, not the author's.
* [x] Base, end commit, the inventory of paths by area, the slow tests (none), each reader's paths read and every checked candidate with its mark are recorded on this page.
* [x] Every seen candidate is in a `[ ]` line under this review, shared causes sharing a line, handed to the driver to add to docs/06; every latent and weak candidate is listed as dropped; nothing is fixed here.
* [x] The mechanical checks above are recorded with their results; `make verify` is green after the last edit and `make book` built both PDFs at the end commit, both run by this /apply and recorded in its Proof with the commit and both PDF paths.

**End commit.** `dae2358` (`docs(queue): define m25-review`), HEAD when the reading started, recorded before any reader was launched; no commit was made during the reading. The range `cd045ba..dae2358` holds the planned `395975a` and the define commit after it; no commit of M26 or later is in it, so no skill is checked against a later version.

**Inventory at the end commit.** `git diff --stat -M cd045ba..dae2358`: 65 paths, 1676 insertions, 402 deletions; the 64 of the Areas above, and this page, which the define commit adds (documents area). The define commit's other path is docs/06's own hunk. Build: none. Chapters: 20. Skills: 12. Documents: 4 and this page. Records: 28.

**Slow tests.** None (docs/05 §5's Verify slot names none).

**Readers and the paths they read.** Four read-only agents on Opus, then one read-only checker on Opus, each launched with its model set to Opus; at most two ran at a time beside this session (pair 1, then the fix-round chapters reader in pair 1's first free slot, the records 2 reader in the second, the checker beside the records 2 reader, which sent it C28 to C36 when it finished). No record here says whether an agent kept the session's advisor. Each read `git diff -M cd045ba..dae2358` of its paths and `git show dae2358:<path>`, never the working tree.

* M25's chapters: the diff in full of `book/{en,pt}/08-install-and-hosts.md`, `11-queue-and-milestones.md`, `12-propose.md`, `13-apply.md`, `14-queue-states.md`; the full text of en chapter 14 and pt 14 :1 to :110 and :196 to :212; chapter 8 en :40 to :125, pt :40 to :116; the other three by diff and targeted passages; `book/{en,pt}/09-starting-a-project.md` by grep and :20 to :25; docs/05 §4, docs/03's rows, the propose, apply and brainstorm skills and the kit-2026-10-20-1, kit-2026-10-20, ch08-update-2026-10-20-1 and ch12-14-parallel-token records by excerpt.
* Skills, documents and records 1: the 12 skill files whole, each cut from SETUP.md §3 at the kit's `9be385a` and compared; docs/03, docs/05 (§4 whole, §§5, 6 and 8), docs/06 whole, ADR-0018 by its diff; `work/done/kit-2026-10-20-1.md`, `ch08-update-2026-10-20-1.md`, `ch12-14-parallel-token.md` and this page whole.
* The fix round's chapters: the diff in full of `book/{en,pt}/07-the-documents.md`, `17-project-as-assistant.md`, `18-git-essentials.md`, `19-worktrees.md`, `23-adoption.md`, with excerpts around the hunks; chapters 8, 12, 13, 14 and 20 by the lines on fetch, resume, taken, review and branch; the first 30 lines of the seven fix-round records; docs/03 and docs/05 by excerpt.
* Records 2: the seven new pages whole (`ch07-review-merge`, `ch08-23-fetch-taken`, `ch18-19-fetch-resume`, `ch18-switch-resume`, `docs03-free-line-held`, `m24-records-proof`, `m24-records-crossrefs`); the diff of the eighteen edited pages (`ch07-09-manual-wording`, `ch08-next-free-line`, `ch08-update-2026-10-20`, `ch09-slow-tests`, `ch12-14-17-20-branch-claim`, `ch13-23-merge-default`, `ch14-board-visibility`, `ch17-23-git-slot-word`, `ch17-next-free-line`, `docs05-author-word`, `kit-2026-10-19-2`, `kit-2026-10-20`, `kit-record-step4`, `m22-records-commits`, `m23-records-crossrefs`, `manual-link-pointers`, `manual-pip-floor`, `manual-pypdf-install`); docs/05 §§3 to 6 and 8; docs/06 M22 to M25.

Every path of the range was read by a reader; none is left unread.

**Mechanical checks, at `dae2358`.**

* Every installed `SKILL.md`, the four under `.claude/skills/` and the four under `.agents/skills/`, carries `version: "2026.10.20.1"`. `git -C ~/Projects/focus-kit show 9be385a:SETUP.md` has SHA-256 `bc2751630e03cd60628dfb279b3c2dd997b5b43158cba1a24b2adffb40209576`, the record's; the 12 skill files are byte-equal (`cmp`) to SETUP.md §§3.1 to 3.5 cut at their fences.
* docs/05 §4's first paragraph equals the template's §4 first paragraph, whitespace normalized (269 words each, `cmp` equal); the old last paragraph, "Each milestone is planned with its review as the last line (§8). Edited by conversation in any session.", is removed in the range's diff.
* `git branch --list` shows `main` alone; `origin/main` is `695d69f` (`chore(release): v1.2.6`), and `cd045ba` is not an ancestor of it, so the range pushed nothing (trunk).
* `git status --short book/` was empty before `make book`, so the PDFs hold the end commit's `book/`. `make book` exit 0. `search-catalog (PA)` is on page 144 of `output/one-page-at-a-time.pdf`, `buscar-catalogo (PA)` on page 152 of `output/uma-pagina-de-cada-vez.pdf`.

**Start pages** (the PDF's page number is the printed one). Chapters, en / pt: prologue 5 / 5; 1: 11 / 11; 2: 19 / 19; 3: 24 / 24; 4: 40 / 41; 5: 54 / 56; 6: 63 / 65; 7: 68 / 70; 8: 79 / 82; 9: 89 / 93; 10: 98 / 102; 11: 105 / 109; 12: 114 / 120; 13: 124 / 130; 14: 140 / 147; 15: 152 / 160; 16: 161 / 169; 17: 169 / 177; 18: 177 / 185; 19: 188 / 197; 20: 205 / 215; 21: 211 / 221; 22: 216 / 227; 23: 222 / 234; 24: 228 / 240. Sections the clause table names, en / pt: "What an update reports" / "O que uma atualização relata" 81 / 84, its excerpt 82 / 85; "The line" / "A linha" 106 / 110; "Changing the queue" / "Mudando a fila" 109 / 114, the re-judging passage 112 / 117; chapter 11's key points 113 / 118; "What `/propose` does" / "O que o `/propose` faz" 115 / 121; chapter 12's key points 122 / 128; "What `/apply` does" / "O que o `/apply` faz" 125 / 131, the waiting passage 126 / 132; chapter 13's key points 138 / 145; "The next line, and which run together" / "A próxima linha, e quais rodam juntas" 143 / 150, the library block 144 / 152; chapter 14's key points 150 / 158.

**The clause answers**, the review's own, from its reading of the passages in both PDFs at `dae2358`; the author tested no clause.

* The book teaches focus-kit 2026.10.20.1 and the repository runs on it: **holds**, with one slip. Chapter 8's excerpt (en 82, pt 85) is a list by document and section; its §4 item says the paragraph lacks the token, proposes the template's first paragraph whole, quoting its token sentences, and removes the last paragraph, its first sentence in §8 and its second in the new first paragraph; its Git item is a recorded project choice, trunk with the Publish policy, the agent never pushing; its `Next:` is `/propose ch08-update-2026-10-20-1`, once `kit-2026-10-20-1` is `[x]`, as the record's Migration report and Step 5 say. The explanation after it (en 82 to 84, pt 85 to 87) gives the three outcomes, reported and never done. The slip (C6): the Git item also names ADR-0010 and the kit's slot offer, which the record it says it paraphrases does not hold. The repository: skills at 2026.10.20.1, docs/05 §4 in the template's words, trunk, `main` alone and nothing pushed (mechanical checks).
* A queue line may carry `(PA)` after the slug: **holds** in both. Chapter 14 (en 144, pt 152) says two letters in parentheses right after the slug, the first for `/propose`, the second for `/apply`, `P` that the definition takes nothing from the pages above, `A` that the build touches none of their files, a `-` waiting for every line above to be `[>]` or beyond, or `[x]`, `after` holding both, and (en 145, pt 152) "a token reads against every line above"; chapter 11's "The line" (en 106, pt 110) and key points (en 113, pt 118) and chapter 13 (en 125, pt 132) agree, in docs/03's and docs/05 §4's words. Chapter 11 :16 says the token says "what may run", a looser wording (C9), and its line template at :19 carries no token (C8).
* Whoever changes the queue re-judges the tokens: **fails** in both on its link. Chapter 14 (en 145, pt 152) says "Whoever changes the queue re-judges the tokens the change affects", and that `/propose` corrects a line's token from its page once it knows what the page takes and which files the Contract touches, as chapter 12 does (en 116, pt 122); but "`/brainstorm` writes them for a first milestone that will run as several sessions (chapter 9)" links a chapter that names no token in either edition (C1). Chapter 11 (en 112, pt 117) and chapter 14 (en 144, pt 151) also say a move re-judges the tokens "of the lines below it", narrower than "the tokens the change affects" (C2).
* /propose and /apply wait as the token says: **holds** in both. Chapter 12 (en 115, pt 121) has `/propose` not start on a line whose token has `-` first, `(-A)` or `(--)`, while a line above is not yet `[>]` or beyond, saying what it waits on; chapter 13 (en 126, pt 132) has `/apply` not start on `(P-)` or `(--)` while a line above is not yet `[x]`, leaving the mark as it is; chapter 14's example (en 145, pt 152) has `/apply renew-loan` say what it waits on and stop. This agrees with docs/05 §4 and with the installed skills: propose's "nor a line docs/05 §4 says waits, by its token or its `after`" and apply's "only a fully defined `[>]` line that §4's token and `after` let build becomes `[*]`". Two slips: the example's "leaves `[>]` as it is" while its block shows `[ ] renew-loan (P-)` (C4), and chapter 13 :32's "an `after` or a token is an order, not a wait" beside the waiting it describes (C3).

**Candidates and the checker's marks.** C1 to C10 from M25's chapters reader, C11 to C21 from the skills, documents and records 1 reader, C22 to C27 from the fix round's chapters reader, C28 to C36 from the records 2 reader; lines at `dae2358`, en / pt.

| Id | File:line | Mark | Claim |
|---|---|---|---|
| C1 | `book/en/14-queue-states.md:105` / pt :106; `09-starting-a-project.md` :23, :88 | seen | The chapter 9 link for `/brainstorm` writing tokens leads to a chapter that names no token; the trigger is worded three ways (ch14, docs/03 :117, the skill) |
| C2 | `book/en/11-queue-and-milestones.md:179` / pt :184; `14-queue-states.md:80` / pt :81 | seen, low | A move re-judges "the lines below it", missing the lines it passed on a move down; ch14 also leaves out the moved line's own token |
| C3 | `book/en/13-apply.md:32` / pt :32 | seen, low | "an `after` or a token is an order, not a wait", while docs/03 :117 and ch14 say `-` waits; docs/03 :114 says it of `after` alone |
| C4 | `book/en/14-queue-states.md:99`, :106 / pt :100, :107 | seen, low | "leaves `[>]` as it is" for a line the block shows `[ ]`, and only lend-book named as what it waits on |
| C5 | `book/en/13-apply.md:28`; `14-queue-states.md:62`, :193; `08-install-and-hosts.md:103` (pt :28, :63, :194, :105) against `12-propose.md:27` | seen, low | Most chapters read each slug's line from its branch, chapter 12 from its worktree or branch; ch14 :64 / :65 says a worktree's file shows a mark first |
| C6 | `book/en/08-install-and-hosts.md:76` to :79 / pt :76 to :80 | seen, low | The Git item names ADR-0010 and the kit's slot offer, which `work/done/kit-2026-10-20-1.md` :84 does not hold; they come from `kit-2026-10-20.md` :85 |
| C7 | `book/pt/14-queue-states.md:97` against :40 | seen, low | "registra" and "cadastra" for the same members line |
| C8 | `book/en/11-queue-and-milestones.md:16`, :19 / pt :16, :19 | seen, low | The line's parts list the token; the template line below has no token |
| C9 | `book/en/11-queue-and-milestones.md:16` / pt :16 | seen, low | "what may run" where the token speaks for the line's own commands |
| C10 | `book/en/08-install-and-hosts.md:103` / pt :105; `14-queue-states.md:71` / pt :72 | latent | The next command from the first free line ignores a token that holds it; matches docs/05 and docs/03, no example triggers it |
| C11 | `work/done/ch08-update-2026-10-20-1.md:107`; `ch12-14-parallel-token.md:123` | seen, low | `make book` and both PDF paths recorded with no commit or tree, for two `(PA)` lines that ran in one tree |
| C12 | `work/done/ch12-14-parallel-token.md:126`, :128 to :135 | seen | The Delivery review read docs/04 only through the brief and the page, against the slot's "against the page and docs/04"; its Done when has no Delivery review item |
| C13 | `work/done/kit-2026-10-20-1.md:116`; `ch08-update-2026-10-20-1.md:111`; `ch12-14-parallel-token.md:126` | seen, low | No Delivery review says whether its agent kept the session's advisor, as the slot asks |
| C14 | `work/done/ch12-14-parallel-token.md:90`; `ch08-update-2026-10-20-1.md:13`, :68, :76; `kit-2026-10-20-1.md:40` | seen | M26 to M29 and their slugs, which no committed docs/06 holds |
| C15 | `work/done/ch12-14-parallel-token.md:18`, :116 | seen, low | The Contract's "Ten files" for eight |
| C16 | `work/done/ch12-14-parallel-token.md:56`, :116, :126 | seen | Divergences "None" while the Contract's "and so on" shipped as "and likewise" (the pt part is weak: the Contract holds no pt wording) |
| C17 | `.claude/skills/propose/SKILL.md:14`, :17 | weak | The skill has no token-correction sentence, but it reads docs/05, whose §4 holds the rule; the record cites the skill only for waiting |
| C18 | `docs/05-Process.md:95`, :102 | latent | §4's line parts omit the token two sentences before it adds `(PA)`; the template's words |
| C19 | `work/done/kit-2026-10-20-1.md:29`, :62 | seen, low | The Contract quotes docs/03's `free line` row without "that no session holds", which the row kept, and :62 ticks "says what the Contract says" |
| C20 | `work/done/kit-2026-10-20-1.md:3`, :40; `ch08-update-2026-10-20-1.md:68` | weak | "chapters 12, 13 and 14" was the line's wording until `8da0912` |
| C21 | `work/done/kit-2026-10-20-1.md:10`, :12, :50, :62 | weak | "no token on any queue line" was true at `dd3cb78`; the tokens came at `fc7cc24` |
| C22 | `book/en/12-propose.md:27`, :172 / pt :27, :181; `20-team-tools.md:62`, :89 / pt :62, :89 | seen | Chapters 12 and 20 read each slug's line from its "worktree or branch", while docs/05 :132 and chapters 13, 14 :209, 17 :132 and 23 :66 say its branch (C5's cause) |
| C23 | `book/en/17-project-as-assistant.md:137` / pt :137 | weak | Speaks of a commit only; the merge is covered in ch18 :26 |
| C24 | `book/en/19-worktrees.md:145` / pt :145 | weak | The commit inside a worktree; the merge is covered at :194 |
| C25 | `docs/03-Domain.md:116` | latent | The `claim` row's `<prefix>/<slug>` is the worktree branch, wrong for a branch per delivery; this project runs on trunk |
| C26 | `book/en/19-worktrees.md:179` / pt :179 | latent | "reuses the worktree and branch that exist" on resumption; the kit's words, not triggered on trunk |
| C27 | `book/en/18-git-essentials.md:25` / pt :25; `19-worktrees.md:179`; `08` :103, `13` :28, `17` :119, :132, `23` :66 | seen, low | Create or reuse given as the only outcomes, an existing branch when not resuming not named as taken (ch12 :28 says it), and "the lines only a branch has" (docs/05 :132) left out |
| C28 | `work/done/m24-records-crossrefs.md:101`, :113 | seen | Ticks the review "with the advisor" while :113 says the review agent had none |
| C29 | `work/done/ch07-review-merge.md:52`; `ch08-23-fetch-taken.md:84`; `ch18-switch-resume.md:54`; `docs03-free-line-held.md:51` | seen, low | Delivery review ticked, its advisor not recorded (C13's cause) |
| C30 | `work/done/ch07-review-merge.md:51`; `ch08-23-fetch-taken.md:83`; `ch18-19-fetch-resume.md:54`; `ch18-switch-resume.md:53` | latent | Each tick says `make book` was not run by its lane and points to this review, whose Proof records the build |
| C31 | `work/done/ch08-23-fetch-taken.md:47`; `ch18-19-fetch-resume.md:33`; `ch18-switch-resume.md:20` | seen | Slugs and milestones (M26 to M28) that no committed docs/06 holds (C14's cause) |
| C32 | `work/done/m24-records-crossrefs.md:16`, :52 | seen, low | Says no replacement sits in a Proof, while replacement 16 edits `ch08-next-free-line`'s Proof |
| C33 | `work/done/m24-records-crossrefs.md:117`; `ch08-next-free-line.md:24`; `ch07-09-manual-wording.md:36` | seen, low | A stale docs/06 line cite promised as a new line that docs/06 lacks; the cite is line-number drift |
| C34 | `work/done/ch18-19-fetch-resume.md:47` to :54, :94 to :107 | seen | Done when has no Delivery review or page-move item, and two Decisions sections follow the `commit` block, though the page ends with it (its Divergences :63 against its Done when :50 is weak: :63 explains the shift) |
| C35 | `work/done/ch08-next-free-line.md:10`, :24 | weak | True of the delivery at `c42e106`, when pt :71 still held "devido pela" |
| C36 | `work/done/kit-2026-10-19-2.md:62`, :108; `m24-records-proof.md:160`; `ch12-14-17-20-branch-claim.md:68` | latent | :108 does name the advisor; the driver's runs are declared as the driver's word; :68 was true until `8da0912` |

**Findings**, the seen candidates, confirmed by this review's session as the author's word quoted under Decisions taken alone allows, grouped by file and cause into three lines handed to the driver for docs/06 under M25, after this line:

1. `ch09-14-token-wording` (C1, C2, C3, C4, C7, C8, C9): chapters 9, 11, 13 and 14 and docs/03's rows on `after` and the token, their token wording.
2. `ch08-23-branch-read` (C5, C6, C22, C27): chapters 8, 12, 13, 14, 17, 18, 19, 20 and 23, where each slug's line is read and what an existing branch means, with chapter 8's Git item, which shares its file.
3. `m25-records-claims` (C11, C12, C13, C14, C15, C16, C19, C28, C29, C31, C32, C34): nine records that claim more than they record.

Dropped: C33, seen, as a line-number drift (the driver's rule quoted under Divergences); the latent C10, C18, C25, C26, C30 and C36; the weak C17, C20, C21, C23, C24 and C35.

**Proof.** At the end commit `dae2358`: the mechanical checks above; `make book` exit 0 with `git status --short book/` empty, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`; the clause answers above from those PDFs. After this page's last edit: see the Verify and book lines below.

**Divergences.** Two from the page. C33 is seen and has no line, against Behaviour's "each candidate the checker marks seen ... becomes a `[ ]` line", by the driver's rule for this run, relayed with the task: "a record-page slip that is a line number drift is not a finding worth a line (list it as dropped)". The Readers plan says each agent keeps the session's advisor, Fable; this page does not record that any did. The checker's summary counted 25 seen; its table holds 24 seen, 6 latent and 6 weak, which this page records.

**Decisions taken by /apply.**

* The checker started beside the records 2 reader, on C1 to C27, and took C28 to C36 by message when that reader finished, so no more than two agents ran beside this session.
* C33 is seen but dropped: what it promised was a line for a line-number drift, which the driver's rule for this run keeps out of the queue.
* C6 joins the branch-read line, since both change chapter 8; C3's docs/03 root joins the token-wording line.
* The tokens of the three lines are judged in order against the lines above them, m25-review `[x]` by then: the first `(PA)`; the second `(P-)`, its build sharing chapters 13 and 14 with the first; the third `(PA)`, records only.

**The finding lines**, as handed to the driver for docs/06, in order after `m25-review`:

```
[ ] ch09-14-token-wording (PA) chapters 9, 11, 13 and 14 and docs/03 teach the token in one wording: chapter 9 shows /brainstorm writing it, a change re-judges the tokens it affects, `-` is a wait, chapter 11's line template carries the token, chapter 14's renew-loan example matches its block, and pt chapter 14 keeps one verb for members; both editions · after m25-review
[ ] ch08-23-branch-read (P-) chapters 8, 12, 13, 14, 17, 18, 19, 20 and 23 read each slug's line where docs/05 §4 says, with the lines only a branch has and an existing branch taken unless the definition resumes, and chapter 8's Git item paraphrases only what kit-2026-10-20-1 records; both editions · after m25-review
[ ] m25-records-claims (PA) the records of kit-2026-10-20-1, ch08-update-2026-10-20-1, ch12-14-parallel-token, ch07-review-merge, ch08-23-fetch-taken, ch18-19-fetch-resume, ch18-switch-resume, docs03-free-line-held and m24-records-crossrefs hold only what happened: make book with its commit, the Delivery review against docs/04 and its advisor as recorded, no slug or milestone the committed queue lacks, and counts, Contract quotes and Divergences that match, the page ending with its commit block · after m25-review
```

**Delivery review.** One read-only Opus agent, launched after the checker had reported, so no more than one agent ran beside this session; it read this page whole and its diff against `HEAD`, `git show HEAD:docs/06-Queue.md` by grep, the spot-checked lines at `dae2358` (chapters 8, 9, 11, 13 and 14, docs/03 :114 to :117, docs/05 :95, :102, :132), the range's `--stat`, `git merge-base` against `origin/main` and both PDFs by `pdftotext`; docs/04 and docs/05 §§3, 5, 6 and 8 it read by grep only. It confirmed the counts (24 seen, 6 latent, 6 weak), the grouping, the inventory, the push state and the start pages it checked. Findings, all taken: C33 dropped against Behaviour with no quoted rule, now quoted under Divergences; the advisor of the plan not recorded, now under Divergences; clause 4's answer silent on C3 and clause 2's on C8, now named; "confirmed by the author's word" reworded as the session's confirmation under that word; docs/03 added to the first finding line; C34's weak part named by file and lines. Outside this delivery: the plan's Contract places "The next line, and which run together" at :84 to :104, while the heading is at :67 at `dae2358`; the passage the clause reads is :84 to :104.

**Verify and book after the last edit.** `make verify` exit 0 after this page's last edit; then, with `git status --short book/` empty, `make book` exit 0, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, its `book/` the end commit's.

```commit
docs(m25-review): review M25, three findings

- Four clauses answered by the review from both PDFs at dae2358
- Four Opus readers over cd045ba..dae2358, one Opus checker
- 36 candidates: 24 seen, 6 latent, 6 weak; C33 dropped as drift
- Three finding lines under M25: token wording, branch read, records
- Skills byte-equal to 2026.10.20.1; docs/05 §4 the template's

work/done/m25-review.md
```
