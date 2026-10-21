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

* [ ] Every line in this review's `after` is `[x]`, and every clause above has the review's answer from its reading of the passages in both PDFs, recorded as the review's, not the author's.
* [ ] Base, end commit, the inventory of paths by area, the slow tests (none), each reader's paths read and every checked candidate with its mark are recorded on this page.
* [ ] Every seen candidate is in a `[ ]` line under this review, shared causes sharing a line, handed to the driver to add to docs/06; every latent and weak candidate is listed as dropped; nothing is fixed here.
* [ ] The mechanical checks above are recorded with their results; `make verify` is green after the last edit and `make book` built both PDFs at the end commit, both run by this /apply and recorded in its Proof with the commit and both PDF paths.
