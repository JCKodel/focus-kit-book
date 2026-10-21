# m26-review

**Objective.** The author can see whether each promise of M26 holds in both editions and in the installed process, answered by the review's own reading of the passages on the author's word, with every checker-seen candidate recorded as a new line under this review.

**Behaviour.**

* With every line in this review's `after` `[x]`, /apply builds both PDFs at the end commit, reads in both the passages the clause table below names, at their start pages, and answers each clause's question itself: holds, or fails with what the passage says. The page records these answers as the review's, never the author's: the author reads no PDF in this run and tests no clause (docs/05 §8, the paragraph on the person's word).
* The review compares the installed commands with focus-kit 2026.10.20.2 as `work/done/kit-2026-10-20-2.md` records it (SETUP.md at the kit's `da29c25`), checks that docs/05 is untouched in the range, as a version that owes this trunk repository no migration predicts, then checks the book's explanations against those rules.
* The author's word that starts the readers and hands the review its tests is already given, relayed by the batch's driver and quoted under Decisions taken alone. /apply records the end commit, then launches read-only area readers over one fixed range, `git diff <base>..<end>`; one checker tests each candidate against that same snapshot and labels it seen, latent or weak.
* Each candidate the checker marks seen, low ones included, becomes a `[ ]` line under this review in docs/06, candidates sharing a file or a cause sharing a line; every latent and weak candidate is dropped and listed on this page with its mark. No fix is made here.
* A clause with no answer, a required reader that cannot run, or paths of the range no reader read leave this review waiting as `[?]` with `· resume: apply` and the reason (docs/05 §§4, 8); a partial reading that found nothing never closes it.
* A commit made during the reading does not move the end commit; what it changed is named as outside this reading.
* Edge, the later milestones: M27 to M29 are in the committed docs/06 since `6278488`, inside the range, so a slug of theirs named in an M26 record is one the committed queue holds, not a repeat of M25's C14. Their lines, pages and commits are not this review's. A commit of M27 that lands before the reading starts is inside the range: its paths are read by their area's reader and named as M27's, with no clause here. If a reinstall at 2026.10.20.3 is in the range, the skills are checked against 2026.10.20.2 as M26 left them, `git show 51334ce:<path>`, and the later version is named, not counted as an M26 failure.
* Edge, the shared tree: readers and the checker read the end commit (`git diff <base>..<end>`, `git show <end>:<path>`), never the working tree or the index. When this page was written the working tree held the driver's uncommitted docs/06 and the index a docs/06 older than HEAD (`kit-2026-10-20-2` as `[ ]` with its old sentence); both are the driver's, not findings, and /apply stages only this page and its own docs/06 hunk, as docs/05 §6 says.

**Contract.** Clause checks from docs/06's M26 paragraph, each against the named deliveries' pages in `work/done/` and the cited chapter sections in both PDFs (`output/one-page-at-a-time.pdf`, `output/uma-pagina-de-cada-vez.pdf`). Lines are en / pt at `51334ce`; where one number is given it is the same in both (chapters 13 and 19 match line for line).

| Clause | Deliveries and passages | The review's question |
|---|---|---|
| The book teaches focus-kit 2026.10.20.2 and the repository runs on it | `kit-2026-10-20-2`: installed skills (`metadata.version` 2026.10.20.2), ADR-0018's `kit-2026-10-20-2` amendment, docs/05 with no hunk, the record's Migration report and Step 5; `ch08-update-2026-10-20-2`: chapter 8, the refusal sentence in "What the install never touches, and how to update" / "O que a instalação nunca toca, e como atualizar" (:46), "What an update reports" / "O que uma atualização relata", its lead-in (:56), the excerpt (:58 to :72 / :58 to :74) with its Git item and its `Next:` line, the explanation after it (:74 to :78 / :76 to :80), the sentence on a check that concerns a choice the project did not make (:93 / :95) and the paragraph on worktree slots ending with the manual (:94 to :97 / :96 to :99) | Does chapter 8's update example match what this repository's update to 2026.10.20.2 did: a report by document and section holding no migration, the trunk Git slot a recorded choice with the Publish policy and the manual named as asked only of a worktree Git slot, the next command with its condition, the refusal check on `apply/SKILL.md` on a copy, every file unchanged, as the record's Refusal case, Migration report and Step 5 say? Does it state no count of a kit change and no comparison of versions? Does the paragraph on worktree slots agree with itself, a slot "gets a migration only when" beside a slot "reported as lacking" the manual? And does the repository hold what the kit asks: skills at 2026.10.20.2, docs/05 untouched, trunk with no branch and nothing pushed? |
| With a worktree per delivery each session opens where it works, /propose in `main/` and /apply in a fresh session inside the delivery's worktree, whose path /propose gives | `ch13-19-session-folder`: chapter 13, "What `/apply` does" / "O que o `/apply` faz" (:19), key points (:274); chapter 19, "The life of a worktree" / "A vida de um worktree" (:131), "Worktrees in the kit" / "Worktrees no kit" (:197 to :199, :214), key points (:366); for agreement, chapter 12 :32 and chapter 8 :136 / :138, on what `/propose` says last on trunk | Does each edition say that with a worktree per delivery `/propose` runs in `main/` and ends by giving the worktree's path, that `/apply` runs in a fresh session opened in that worktree, with the reason (the page and the `[>]` on the delivery's branch, the worktree's own index), that no session opens in the container, which is not a checkout, with the lending library's path as the example, in the words of the installed propose and apply skills and the Choices' worktree bullet? Do chapters 8 and 12, which show `/propose` ending on trunk, still agree with chapter 19's "ends by giving that folder's path"? |
| /apply opened anywhere else stops before any edit and gives that path | `ch13-19-session-folder`: chapter 13 (:33), beside the refusal of an incomplete page (:30 to :32); chapter 19 (:200), key points (:366) | Does each edition have `/apply`, with a worktree per delivery, opened in any folder but the delivery's worktree, `main/` included, edit nothing, leave the mark as it is, not mark the line `[?]`, and give the worktree's path, scoped to a worktree per delivery alone, in agreement with the installed apply skill's "with a worktree, only in a session opened in it: elsewhere, stop before any edit and give its path"? |
| The container's manual lets a session in `main/` edit the worktrees | `ch13-19-session-folder`: chapter 19 (:133 the manual, :135 to :145 the setting, its block and the quote), the footnote (:378), key points (:366); `ch08-update-2026-10-20-2`: chapter 8 (:97 / :99) | Does each edition say that the container's manual tells how the host lets a session in `main/`, where `/propose` runs and writes the page in the worktree, edit the worktrees, with Claude Code's `"permissions": {"additionalDirectories": ["../.focus-kit/worktrees"]}` in `main/`'s `.claude/settings.json` as the example, loading none of the worktrees' commands, the quote the documentation's own words and the footnote opening that page and section? Does chapter 8's sentence on a slot lacking the manual agree with chapter 19? |

**Base.** `7664d02` (`docs(m25-review): review M25, three findings`), the commit of m25-review, the previous milestone's review (docs/05 §8, docs/03's `milestone review` row). The range therefore also holds M25's fix round, `ch09-14-token-wording`, `ch08-23-branch-read` and `m25-records-claims`, which gets no second review (docs/05 §8): the clause checks above are M26's alone, while the readers read the whole range.

**End.** The commit HEAD is when the reading starts; /apply records it before launching any reader, and nothing it records later moves it. Planned: `51334ce` (`docs(ch13-19-session-folder): teach which folder each session opens in`), HEAD when this page was written; the driver's marks and this page's define commit come after it, and a commit of M27 may too (Behaviour), so /apply records the actual end and recomputes the inventory there.

**Areas.** The paths `git diff --stat -M 7664d02..HEAD` shows today, at `51334ce` (52 paths, 1090 insertions, 229 deletions), by the areas of docs/05 §5's Milestone review slot. /apply recomputes them at its end commit and places any new path in its area:

* **Build:** no path; the range changes no script, manual or `Makefile`, so no reader is planned for it.
* **Chapters** (22 files), split in two:
  * M26's chapters, both editions: `book/{en,pt}/08-install-and-hosts.md`, `13-apply.md`, `19-worktrees.md` (6 files), every passage the clause table names; chapter 8 also holds `ch08-23-branch-read`'s hunks, chapter 13 those of `ch09-14-token-wording` and `ch08-23-branch-read`, chapter 19 one of `ch08-23-branch-read`, read here with them;
  * the fix round's other chapters, both editions: `book/{en,pt}/09-starting-a-project.md`, `11-queue-and-milestones.md`, `12-propose.md`, `14-queue-states.md`, `17-project-as-assistant.md`, `18-git-essentials.md`, `20-team-tools.md`, `23-adoption.md` (16 files).
* **The kit's skills:** `.claude/skills/{analyze,apply,brainstorm,propose}/SKILL.md`, `.claude/skills/{analyze,brainstorm}/references/documents.md`, and the same six under `.agents/skills/` (12 files), each also compared byte for byte with SETUP.md §3 of 2026.10.20.2 at the kit's `da29c25`.
* **The documents:** `docs/03-Domain.md` (`ch09-14-token-wording`), `docs/06-Queue.md`, `docs/adr/ADR-0018-six-marks.md` (3 files), and this page, `work/m26-review.md`, which the define commit adds.
* **Delivery records**, the 15 paths under `work/done/`, split in two:
  * records 1, M26's three pages: `kit-2026-10-20-2`, `ch08-update-2026-10-20-2`, `ch13-19-session-folder`;
  * records 2, M25's fix round: its three pages, `ch09-14-token-wording`, `ch08-23-branch-read`, `m25-records-claims`, and the nine earlier pages `m25-records-claims` edited, `ch07-review-merge`, `ch08-23-fetch-taken`, `ch08-update-2026-10-20-1`, `ch12-14-parallel-token`, `ch18-19-fetch-resume`, `ch18-switch-resume`, `docs03-free-line-held`, `kit-2026-10-20-1`, `m24-records-crossrefs` (12 files).

Count: 0 + 22 + 12 + 3 + 15 = 52.

**Readers.** Four read-only readers on Opus, each keeping the session's advisor, Fable, then one read-only checker on Opus; no other model runs the review (docs/05 §5, Milestone review). At most two of the review's agents run at a time, so with the review's own session no more than three run at once. Planned, lean:

* pair 1: **M26's chapters** (6 files), with both editions' chapter 12 :32 and chapter 8 :136 / :138 for L1; and **skills, documents and records 1** (12 + 3 + 3 files, and this page), the installed kit, ADR-0018 and the pages that did it, read together;
* pair 2: **the fix round's chapters** (16 files); and **records 2** (12 files). The checker starts when a slot frees, beside the last reader, on the candidates already in.

Each reader lists the paths it read, and the page records whether each kept the session's advisor.

**Slow tests.** The Verify slot names none (docs/05 §5); none is invented for this review.

**Known candidates for the checker**, leads to check, not findings. Each names the reader that reads it:

* L1, chapter 19 :197 says `/propose` ends by giving the worktree's path, while chapter 12 :32 and chapter 8 :136 / :138 show how `/propose` ends on trunk; `ch13-19-session-folder` put both out of scope. Whether a reader of the three gets one account of what `/propose` says last. M26's chapters reader.
* L2, chapter 8's paragraph on worktree slots: :94 / :96 says a worktree Git slot that names no folder "gets a migration only when the project already works in a container", and :97 / :99 that any worktree Git slot with no manual "is reported as lacking it", a lacking outcome being a migration (:76 / :78). M26's chapters reader.
* L3, the records' Done when ticks against what their Proof and Delivery review record, M25's C11 to C13 and C28 to C29: `kit-2026-10-20-2.md` :55 ticks `make verify` green while :112 records the link check failing; its Delivery review (:104) does not say whether its agent kept the session's advisor; `ch13-19-session-folder.md` :106 ticks "`make book`: left to the driver" and :107 "with the advisor", which its Divergences (:113, :114) contradict; `ch08-update-2026-10-20-2.md` :103 records `make book` in a shared tree with no commit. Skills, documents and records 1 reader.
* L4, `ch13-19-session-folder.md`'s Contract and Sources cite chapter 19 :130 and :132 and the brainstorm `references/documents.md` :158 to :160 as they were before its own insertions; whether each cite still points where it says at the end commit (a line-number drift is dropped, as m25-review's C33). Skills, documents and records 1 reader.

**Mechanical checks**, run by /apply at the end commit:

* Every installed skill, `.claude/skills/*/SKILL.md` and `.agents/skills/*/SKILL.md`, carries `metadata.version` `2026.10.20.2` (or, if a later version is in the range, at `51334ce`, Behaviour); the 12 skill files are byte-equal to SETUP.md §3 of `git -C ~/Projects/focus-kit show da29c25:SETUP.md`, SHA-256 `c9934c3b6ef634b36d1f3645fe55a9caf990d864ee789973d73434d2ccc48edb`, the record's; no other destination of SETUP §3 is in the range.
* ADR-0018 holds the `kit-2026-10-20-2` amendment, dated 2026-10-21, its earlier amendments unchanged in the range's diff; `docs/05-Process.md` is not in the range's `--stat`; `git branch --list` shows `main` alone and `7664d02` is not an ancestor of `origin/main`, so the range pushes nothing (trunk).
* `git status --short book/` is empty before `make book`, so the PDFs hold the end commit's `book/`; both PDFs contain the text of `51334ce` (`2026.10.20.2` in chapter 8 and `additionalDirectories` in chapter 19, both editions), and /apply records each chapter's start page in both editions and the start page of each section the clause table names.
* `make verify` and `make book` are rerun by /apply after its last edit; their results here are /apply's, not this page's. A failure caused by another session's uncommitted file is named as that session's; one caused by an external host refusing the connection is named with the link.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs, `make book` at the end commit; /apply records the start page of every chapter in both editions.

**Out of scope.**

* Fixing any finding: each becomes its own line (docs/05 §8).
* Re-testing M25's clauses or its findings: m25-review answered the clauses, and the fix round is read by the area readers, not tested by clause.
* M27 and later: their lines, pages and commits are theirs; any in the range is read, not reviewed by clause (Behaviour).
* A fresh-clone rerun: no path of the build is in the range.
* Changing the readers' model or the slot: docs/05 §5 owns it.
* The author's reading of the PDFs, the author's answer to any clause and the author's confirmation of candidates: not part of this run, by the author's word (Decisions taken alone).
* The driver's uncommitted docs/06 and the stale docs/06 in the index (Behaviour).

**Decisions from the documents.**

* The base is m25-review's commit, the previous milestone's review, the first of docs/05 §8's cases.
* The fix round is read by the area readers but has no clause here (docs/05 §8: findings get no second review).
* The kit's version and its source are `kit-2026-10-20-2`'s: 2026.10.20.2 at `da29c25`, read from the kit's history; that record owes docs/05 no migration, so the check is that docs/05 has no hunk, where m25-review compared §4 with the template.
* The review's session takes the clause tests and the confirmation of seen candidates because the author's word, quoted below, gives them to it (docs/05 §8, the paragraph on the person's word); the checker, the range and the `[?]` for paths not read stay as §8 says.
* The end commit and the final path inventory are inputs /apply fixes before reading, not open scope (docs/05 §8).
* The line had no token at `51334ce`; its definition, the define commit `cfcfc9d`, gave it `(--)`: this review reads every page and file above it, so neither its definition nor its build may run beside them (docs/05 §4).

**Decisions taken alone** (the batch's driver asked for recommended answers; correct them in the review). The agent chose each of these.

* The author's word for this run, relayed by the driver and quoted as docs/05 §8 asks: "review and fixes directly" (in Portuguese, "Review e correções direto"): the review's own session answers the clause tests by reading the passages, and checker-seen candidates become `[ ]` lines under m26-review; latent and weak ones are dropped and listed. The author reads no PDF in this run.
* "Seen" includes "seen, low": every seen candidate becomes a line; candidates sharing a file or a cause share one line, as m25-review grouped them. A line-number drift in a record is dropped, as m25-review dropped C33 by the driver's rule.
* M26's paragraph is taken as four clauses, by what a reader must say: the opener (the book teaches 2026.10.20.2 and the repository runs on it); where each session opens; `/apply` stopping elsewhere; the container's manual. Different passages answer each.
* `kit-2026-10-20-2` answers the opener with `ch08-update-2026-10-20-2`, and `ch13-19-session-folder` the other three; chapter 8's manual sentence also answers the fourth; every delivery of M26 answers a clause.
* The first clause's question also asks whether chapter 8's paragraph on worktree slots agrees with itself (L2), since `ch08-update-2026-10-20-2` added the manual sentence to it.
* "At most three agents in total, the review session counting" is read as at most three at once: two of the review's agents at a time beside its session, the checker starting beside the last reader.
* Lean readers, four: the build area is empty; the skills, the documents and M26's three records join, since each record is read against the installed files and the ADR it changed; the chapters split as M26's (every clause passage in one reader) and the fix round's; the records as M26's and the fix round's.
* A seen candidate becomes a `[ ]` line under this review whether or not it answers a clause of M26: docs/05 §8 puts each finding in the same milestone.

**Done when.**

* [x] Every line in this review's `after` is `[x]`, and every clause above has the review's answer from its reading of the passages in both PDFs, recorded as the review's, not the author's.
* [x] Base, end commit, the inventory of paths by area, the slow tests (none), each reader's paths read, whether each agent kept the session's advisor, and every checked candidate with its mark are recorded on this page.
* [x] Every seen candidate is in a `[ ]` line under this review, shared causes sharing a line, handed to the driver to add to docs/06; every latent and weak candidate is listed as dropped; nothing is fixed here but C14, a sentence of this page (Divergences).
* [x] The mechanical checks above are recorded with their results; `make verify` is green after the last edit and `make book` built both PDFs at the end commit, both run by this /apply and recorded in its Proof with the commit and both PDF paths.
* [x] No separate Delivery review, a milestone review having none by the driver's word, and nothing staged, the driver staging (Divergences, which quote this item as the define wrote it); the page moved to `work/done/` and its commit message suggested in a `commit` block, which ends the page.

**End commit.** `cfcfc9d` (`docs(queue): define m26-review`), HEAD when the reading started, recorded before any reader was launched. The range `7664d02..cfcfc9d` holds the planned `51334ce` and the define commit after it, which changes only docs/06 and this page, so the clause table's `book/` lines at `51334ce` hold at `cfcfc9d`; no commit of M27 or later is in it, so no skill is checked against a later version.

**Inventory at the end commit.** `git diff --stat -M 7664d02..cfcfc9d`: 53 paths, 1196 insertions, 229 deletions; the 52 of the Areas above, and this page, which the define commit adds (documents area). Build: none. Chapters: 22. Skills: 12. Documents: 3 and this page. Records: 15.

**Slow tests.** None (docs/05 §5's Verify slot names none).

**Mechanical checks, at `cfcfc9d`.**

* Every installed `SKILL.md`, the four under `.claude/skills/` and the four under `.agents/skills/`, carries `version: "2026.10.20.2"`. `git -C ~/Projects/focus-kit show da29c25:SETUP.md` has SHA-256 `c9934c3b6ef634b36d1f3645fe55a9caf990d864ee789973d73434d2ccc48edb`, the record's; the 12 skill files are byte-equal (`cmp`) to SETUP.md §§3.1 to 3.5 cut at their fences. No other destination of SETUP §3 is in the range: every path of it is under `book/`, `docs/`, `work/`, `.claude/skills/` or `.agents/skills/`.
* ADR-0018 ends with "Amendment, 2026-10-21 (kit-2026-10-20-2)"; the range's diff of the ADR adds lines only, so its eleven earlier amendments are unchanged. `docs/05-Process.md` is not in the range's `--stat`.
* `git branch --list` shows `main` alone; after `git fetch`, `origin/main` is `695d69f` (`chore(release): v1.2.6`), and `7664d02` is not an ancestor of it, so the range pushed nothing (trunk).
* `git status --short book/` was empty before `make book`, so the PDFs hold the end commit's `book/`. `make book` exit 0. `2026.10.20.2` is in chapter 8 of both PDFs (en 81 and 82, pt 84 and 85); `additionalDirectories` is in chapter 19 of both (en 195, pt 205).

**Start pages** (the PDF's page number is the printed one). Chapters, en / pt: prologue 5 / 5; 1: 11 / 11; 2: 19 / 19; 3: 24 / 24; 4: 40 / 41; 5: 54 / 56; 6: 63 / 65; 7: 68 / 70; 8: 79 / 82; 9: 89 / 93; 10: 98 / 102; 11: 105 / 109; 12: 115 / 120; 13: 125 / 130; 14: 141 / 148; 15: 153 / 161; 16: 162 / 170; 17: 170 / 178; 18: 178 / 186; 19: 189 / 198; 20: 207 / 217; 21: 213 / 223; 22: 218 / 229; 23: 224 / 236; 24: 230 / 242. Sections the clause table names, en / pt: "What the install never touches, and how to update" / "O que a instalação nunca toca, e como atualizar" 80 / 83, its refusal sentence 81 / 84; "What an update reports" / "O que uma atualização relata" 81 / 84, its excerpt 82 / 85, the paragraph on worktree slots 83 / 86 to 87; chapter 8's `/propose` ending (:136 / :138) in "How each host finds the commands" / "Como cada host encontra os comandos", 86 / 90; "What `/apply` does" / "O que o `/apply` faz" 126 / 131, the refusal outside the worktree 127 / 132; chapter 13's key points 140 / 146; "The life of a worktree" / "A vida de um worktree" 194 / 203, the manual's setting and its footnote 195 / 205; "Worktrees in the kit" / "Worktrees no kit" 197 / 206, `/apply` stopping elsewhere 197 / 207; chapter 19's key points 205 / 215.

**Readers and the paths they read.** Four read-only agents on Opus, then one read-only checker on Opus, each launched with its model set to Opus; at most two ran at a time beside this session: pair 1, then the fix round's chapters reader in pair 1's first free slot, the records 2 reader in the second, and the checker beside the records 2 reader, on C1 to C21, taking C22 to C30 by message when that reader finished. Each read `git diff -M 7664d02..cfcfc9d` of its paths and `git show cfcfc9d:<path>`, never the working tree. On the advisor: the M26 chapters reader, the skills, documents and records 1 reader and the fix round's chapters reader each said in its own report that it consulted the session's advisor once, before reporting; the records 2 reader and the checker said nothing of it; nothing else this session holds shows whether any agent kept it.

* M26's chapters: the diff in full of `book/{en,pt}/08-install-and-hosts.md`, `13-apply.md`, `19-worktrees.md` and of `docs/03-Domain.md`; this page whole; chapter 8 en and pt :40 to :100 and :128 to :142; chapter 12 en and pt :26 to :36 and its key point; chapter 13 en :17 to :20, :30 to :35, :272 to :276; chapter 19 en :100 to :215, :364 to :368, :378, pt :100 to :132 and :146 to :215, the rest of pt 19 through the diff; docs/06's M26 section; the propose, apply and brainstorm skills and `brainstorm/references/documents.md` by excerpt; `work/done/ch08-update-2026-10-20-2.md` by excerpt; SETUP.md at the kit's `da29c25` :68 to :80; greps of chapters 8, 12 and 14, docs/03, docs/05 and the three M26 records. It did not read AGENTS.md at `cfcfc9d` or docs/05 whole.
* Skills, documents and records 1: this page and `work/done/kit-2026-10-20-2.md`, `ch08-update-2026-10-20-2.md`, `ch13-19-session-folder.md` whole, with their Done when at their define commits `52fe5f9`, `d738fe5`, `9a635ba`; the range diff of docs/03, docs/06, ADR-0018, the propose, apply and brainstorm `SKILL.md` and brainstorm's `references/documents.md`; analyze's two files by blob and `--stat` and by byte equality with brainstorm's `references/documents.md`; the six `.agents/skills/` files by blob, all equal to the `.claude/skills/` ones; docs/05, the `Makefile`, `work/kit-proposals.md` and chapters 8, 12, 13 and 19 by excerpt; SETUP.md and CHANGELOG.md at `da29c25` by excerpt; docs/06's hunk in each commit of the range.
* The fix round's chapters: the diff in full, with six lines of context, of `book/{en,pt}/09-starting-a-project.md`, `11-queue-and-milestones.md`, `12-propose.md`, `14-queue-states.md`, `17-project-as-assistant.md`, `18-git-essentials.md`, `20-team-tools.md`, `23-adoption.md`, and a grep of each whole file; docs/03's diff; docs/05 §4 whole; the propose, apply and brainstorm skills and `brainstorm/references/documents.md` by excerpt; chapters 13 :19 and 19 :196 to :200; this page whole; `work/done/ch09-14-token-wording.md` :1 to :60.
* Records 2: `work/done/ch09-14-token-wording.md`, `ch08-23-branch-read.md`, `m25-records-claims.md` whole; the range diff, six lines of context, of `ch07-review-merge.md`, `ch08-23-fetch-taken.md`, `ch08-update-2026-10-20-1.md`, `ch12-14-parallel-token.md`, `ch18-19-fetch-resume.md`, `ch18-switch-resume.md`, `docs03-free-line-held.md`, `kit-2026-10-20-1.md`, `m24-records-crossrefs.md`, and those nine at `cfcfc9d` by grep and line; this page's first 80 lines; `work/done/m25-review.md` by grep; docs/06 :615 to :672; docs/05 at the cited lines; cites checked at `7664d02`, `5a40864`, `d8b2df0` and `395975a`.
* The checker: every candidate's file at `cfcfc9d`, and the define commits a candidate names.

Every path of the range was read by a reader; none is left unread.

**The clause answers**, the review's own, from its reading of the passages in both PDFs at `cfcfc9d`; the author tested no clause.

* The book teaches focus-kit 2026.10.20.2 and the repository runs on it: **holds**, with two slips in chapter 8. The refusal sentence (en 81, pt 84) has a line appended to `apply/SKILL.md` on a copy stop the update to 2026.10.20.2, every file of the copy unchanged, as the record's Refusal case says. The excerpt (en 82, pt 85) is a report by document and section, "none pending"; its Git item is a project choice, trunk with the Publish policy, the manual asked only of a worktree Git slot; its `Next:` is `/propose ch08-update-2026-10-20-2`, once `kit-2026-10-20-2` is `[x]`, as the record's Migration report and Step 5 say. The explanation after it gives the three outcomes and says the report "compares the documents with the current templates, never one version of the kit with another"; no count of a kit change is in the chapter. The sentence on a choice the project did not make (en 83, pt 86) names the manual and trunk. The paragraph on worktree slots does not agree with itself (C1): a slot naming no folder "gets a migration only when the project already works in a container", while any worktree slot with no manual "is reported as lacking it", which is a migration. And the example of a choice "recorded with a date or an ADR, as the book's Git slot does" points to an excerpt that names neither (C3). The repository: skills at 2026.10.20.2, docs/05 with no hunk, trunk, `main` alone and nothing pushed (mechanical checks).
* With a worktree per delivery each session opens where it works: **holds** in chapters 13 and 19 of both editions, and **fails** on chapter 12's agreement. Chapter 13 (en 126, pt 131) has the fresh session open in the delivery's worktree, "the folder whose path `/propose` gives when it ends", because the page and the line's `[>]` are on the delivery's branch. Chapter 19 (en 194 to 197, pt 203 to 207) says the container is not a checkout and every session opens in `main/` or a worktree, `/propose` ends by giving the worktree's path, `/apply return-book` runs in a fresh session opened in `library/.focus-kit/worktrees/return-book` (pt `biblioteca/.focus-kit/worktrees/devolver-livro`) because the page and the `[>]` are on the branch and the index is the worktree's own, and no session opens in the container; its key points (en 205, pt 215) say the same, in the words of the propose skill ("opened in the delivery's worktree, if any, its path written out"), the apply skill and the Choices' worktree bullet. Chapter 8 :136 / :138 (en 86, pt 90) shows `/propose` ending on trunk and agrees, since chapter 19's ending is the worktree case. Chapter 12, the chapter on `/propose`, does not: its ending (:32) gives no path and its key point (en :172, pt :181) has `/propose` start "in the delivery's branch or worktree", where chapter 19 has it run in `main/` (C2, C17).
* `/apply` opened anywhere else stops before any edit and gives that path: **holds** in both. Chapter 13 (en 127, pt 132), beside the refusal of an incomplete page, has a session opened, with a worktree per delivery, in any folder but the delivery's worktree, `main/` included, refuse the same way: edit nothing, leave the mark as it is, give the worktree's path; the refusal comes before any build, so the line is not marked `[?]`. Chapter 19 (en 197, pt 207) and its key points say it stops before any edit anywhere else, in agreement with the apply skill's "with a worktree, only in a session opened in it: elsewhere, stop before any edit and give its path".
* The container's manual lets a session in `main/` edit the worktrees: **holds** in both. Chapter 19 (en 195, pt 205) says the same manual tells how the host lets a session in `main/`, where `/propose` runs and writes the page in the worktree, edit the worktrees, with `"permissions": {"additionalDirectories": ["../.focus-kit/worktrees"]}` in `main/`'s `.claude/settings.json`, loading none of the worktrees' commands; the quote "grant file access only" is the documentation's own words (pt translates it, "concedem só acesso a arquivos"), and the footnote opens "Configure permissions", section "Additional directories grant file access, not configuration"; this session fetched that page on 2026-10-21 and found both the sentence and the section. Chapter 8 (en 83, pt 87) says a worktree Git slot with no such manual is reported as lacking it, in agreement with chapter 19.

**Candidates and the checker's marks.** C1 to C3 from M26's chapters reader, C4 to C15 from the skills, documents and records 1 reader, C16 to C21 from the fix round's chapters reader, C22 to C30 from the records 2 reader; lines at `cfcfc9d`, en / pt, as the checker corrected them.

| Id | File:line | Mark | Claim |
|---|---|---|---|
| C1 | `book/en/08-install-and-hosts.md:94`, :97, :76 / pt :96, :99, :78 | seen | A slot naming no folder "gets a migration only when" a container exists, while any worktree slot with no manual is reported as lacking it, a migration; SETUP at `da29c25` gives the manual its own clause |
| C2 | `book/en/12-propose.md:32`, :36, key point :172 / pt :32, :36, :181 | seen, low | Chapter 12 never shows `/propose` ending with the worktree's path, which chapters 13 :19 and 19 :197 and the propose skill give |
| C3 | `book/en/08-install-and-hosts.md:77` / pt :79 | seen, low | "recorded with a date or an ADR, as the book's Git slot does", while the excerpt's Git item names no ADR or date since this range |
| C4 | `work/done/kit-2026-10-20-2.md:55`, :94 to :98, :112 | seen, low | The verify item reworded in /apply from its `52fe5f9` text, the rewording not in Divergences |
| C5 | `work/done/kit-2026-10-20-2.md:56`, :104 | seen | Ticks "Delivery review as docs/05 §5 says", while the review paragraph says nothing of the advisor the slot asks for |
| C6 | `work/done/ch08-update-2026-10-20-2.md:115`, :98, :107 | seen | "with the advisor" cut from the item and ticked, while Divergences says "None from the Contract" |
| C7 | `work/done/ch13-19-session-folder.md:107`, :114 | seen | Ticks "with the advisor", while :114 says nothing shows the agent kept it |
| C8 | `work/done/ch13-19-session-folder.md:106`, :113, :130 | seen | Ticks "`make book`: left to the driver", while :113 and :130 say the lane ran it |
| C9 | `work/done/ch08-update-2026-10-20-2.md:103` | seen, low | `make book` in a shared tree, with no commit |
| C10 | `work/done/ch08-update-2026-10-20-2.md:102`; `ch13-19-session-folder.md:130`; `kit-2026-10-20-2.md:112` | weak | The link passing in two records and failing in a third; each records its own run of an unreliable host |
| C11 | `work/done/ch13-19-session-folder.md:61` | weak | The `references/documents.md` :158 to :160 cite holds |
| C12 | `work/done/ch13-19-session-folder.md:16`, :61, :72, :82 to :84, :90, :94, :101, :124 | seen, drift | Chapter cites shifted by the delivery's own insertions |
| C13 | `work/done/ch08-update-2026-10-20-2.md:65`, :104 | seen, low | SETUP step 5 cited as 105 to 110; it runs to 111, the line naming the command for each mark |
| C14 | `work/m26-review.md:87` | seen, low | "The line's token `(--)` holds ... no correction", while the define commit wrote the token |
| C15 | `docs/03-Domain.md:94` | weak | The `worktree` row keeps a phrase the Choices dropped; the project's own vocabulary, and true |
| C16 | `book/en/12-propose.md:32`, :36 / pt :32, :36 | seen, low | C2 from the fix round's side; joins C2 |
| C17 | `book/en/12-propose.md:28`, key point :172 / pt :28, :181 | seen, low | The key point has `/propose` start "in the delivery's branch or worktree", against chapter 19 :135, :198, :214 |
| C18 | `book/en/12-propose.md:37`; `11-queue-and-milestones.md:125` to :126; `17-project-as-assistant.md:138` | latent | `/propose` "runs where you choose", which could be another worktree; trunk here, no example shows it |
| C19 | `book/en/14-queue-states.md:63` to :64 / pt :64 to :65; `20-team-tools.md:62`; `17-project-as-assistant.md:125` | weak | :64 already ties what a reader sees to a committed mark |
| C20 | `book/en/09-starting-a-project.md:23` / pt :23 | weak | "whether it may run" is about the line, not M25's C9 wording |
| C21 | `book/en/18-git-essentials.md:25` / pt :25 | weak | The doubled "when the definition resumes" is a recorded decision (`ch08-23-branch-read.md:113`) |
| C22 | `work/done/ch08-23-branch-read.md:93`, :115 | seen | Ticks "as docs/05 §5 says", while the reviewer never opened docs/04 and its advisor is known only from its report |
| C23 | `work/done/kit-2026-10-20-1.md:65`, :116; `m25-records-claims.md:133` | seen | Ticks "as docs/05 §5 says" while :116 says the advisor is not recorded; the new M25 line `m25-records-claims` says it reported is not in the committed docs/06 |
| C24 | `work/done/m25-records-claims.md:120`, :9, :132, :133 | seen | Ticks a search its own Divergences record failing; `kit-2026-10-20-1` :65 still breaks Behaviour :9 |
| C25 | `work/done/m25-records-claims.md:153` | seen, low | `make book` with no tree or commit, what its Objective asks of others (C9's cause) |
| C26 | `work/done/ch09-14-token-wording.md:87`, :97, :86, :99 | seen | Ticks a review "against this page and docs/04", while :97 says it did not reread docs/04; :86's "with its commit" against :99's tree with unstaged edits |
| C27 | `work/done/ch09-14-token-wording.md:52` | seen, low | Says `ch08-23-branch-read` changes chapter 14 :62, which that page keeps out of scope |
| C28 | `work/done/ch08-23-branch-read.md:15`, :100 | seen, low | Quotes chapter 14 :62 as "and the lines only a branch has", which read "adds the lines only a branch has"; not in Divergences |
| C29 | `work/done/ch09-14-token-wording.md:93`, :97 | weak | "None from the Contract" holds |
| C30 | `work/done/ch09-14-token-wording.md:91`, :99; `ch08-23-branch-read.md:109`, :117; `m25-records-claims.md:152` | weak | As C10 |

**Findings**, the seen candidates, confirmed by this review's session as the author's word quoted under Decisions taken alone allows, grouped by file and cause into three lines handed to the driver for docs/06 under M26, after this line:

1. `ch08-worktree-slot-manual` (C1, C3): chapter 8's paragraph on worktree slots and the example after the excerpt.
2. `ch12-propose-worktree-path` (C2, C16, C17): chapter 12, left as it was while chapters 13 and 19 and the propose skill gained the worktree's path.
3. `m26-records-claims` (C4, C5, C6, C7, C8, C9, C13, C22, C23, C24, C25, C26, C27, C28): seven records whose ticks, builds and cites claim more than they record.

C14 is this page's own text: fixed here, below. Dropped: C12, seen, as a line-number drift (the driver's rule, quoted under Divergences); the latent C18; the weak C10, C11, C15, C19, C20, C21, C29 and C30.

**The finding lines**, as handed to the driver for docs/06, in order after `m26-review`:

```
[ ] ch08-worktree-slot-manual (PA) chapter 8's paragraph on worktree slots says the folder migration waits for a container while the manual is reported lacking whatever the folder, and the example after the excerpt of a choice recorded with a date or an ADR matches what the excerpt shows; both editions · after m26-review
[ ] ch12-propose-worktree-path (PA) chapter 12 says that with a worktree per delivery /propose runs in main/, writes the page in the worktree and ends by giving its path for /apply's fresh session, its key points included, as chapters 13 and 19 and the propose skill say; both editions · after m26-review
[ ] m26-records-claims (PA) the records of kit-2026-10-20-2, ch08-update-2026-10-20-2, ch13-19-session-folder, ch08-23-branch-read, ch09-14-token-wording, m25-records-claims and kit-2026-10-20-1 hold only what happened: each Done when tick matches its Proof and Delivery review, a reworded item listed in Divergences, make book with its tree and commit, cites and quotes that match what they cite, and no queue line claimed that docs/06 lacks · after m26-review
```

**Divergences.**

* C12 is seen and has no line, against Behaviour's "each candidate the checker marks seen ... becomes a `[ ]` line", by the driver's rule, which m25-review quoted: "a record-page slip that is a line number drift is not a finding worth a line (list it as dropped)".
* C14 is fixed on this page instead of becoming a line, against Behaviour's "No fix is made here": it is a sentence of this page's own Decisions, and the apply skill has a delivery fix the text it wrote. The bullet now says the line had no token at `51334ce` and the define commit gave it `(--)`, and the third Done when item, which read "nothing is fixed here.", now names C14.
* No separate Delivery review ran, against the last Done when item as the define wrote it, "Delivery review as docs/05 §5 says, its advisor recorded as it ran; only this page and its docs/06 hunk staged", by the driver's word for this run: "a milestone review has no separate delivery review". Nothing is staged, by the batch's rules: the driver stages. That item is reworded below to say what happened.
* The Readers plan says each agent keeps the session's advisor, Fable; this page records only what the agents said of it (Readers above).
* The records 2 reader wrote working files into the shared scratchpad under names that may have been the driver's (`q.md` among them); no repository file was touched.

**Decisions taken by /apply.**

* The checker started beside the records 2 reader, on C1 to C21, and took C22 to C30 by message when that reader finished, so no more than two agents ran beside this session.
* C1 and C3 share chapter 8 and one line; C2, C16 and C17 share chapter 12's one cause and one line; every record candidate shares the cause of M25's `m25-records-claims` and one line.
* The tokens of the three lines are judged in order against the lines above them, m26-review `[x]` by then: the first `(PA)`, chapter 8 alone; the second `(PA)`, chapter 12 alone; the third `(PA)`, records only. M27's `ch08-update-2026-10-20-3` and `ch12-14-18-several-slugs`, which also change chapters 8 and 12, are below them; their tokens are theirs.
* The clause on where each session opens fails on chapter 12 alone: chapter 12 is not one of M26's deliveries, but the clause's question asks it for agreement, so the answer says so.

**Delivery review.** None separate: a milestone review has none, by the driver's word (Divergences); the readers and the checker above are its reading.

**Proof.** At the end commit `cfcfc9d`: the mechanical checks above; `make book` exit 0 with `git status --short book/` empty, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`; the clause answers above from those PDFs: chapter 8 read in the PDFs' text (en 81 to 84, pt 83 to 87), chapters 12, 13 and 19 read in their source at `cfcfc9d`, which is the PDFs' `book/`, each passage located in both PDFs by its text and page. After this page's last edit: see the Verify and book line below.

**Verify and book after the last edit.** `make verify` exit 0 after this page's last edit, every check passing, the link check included; then, with `git status --short book/` empty, `make book` exit 0, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, its `book/` the end commit's `cfcfc9d`.

```commit
docs(m26-review): review M26, three findings

- Four clauses answered by the review from both PDFs at cfcfc9d
- Four Opus readers over 7664d02..cfcfc9d, one Opus checker
- 30 candidates: 21 seen, 1 latent, 8 weak; C12 dropped as drift
- Three finding lines under M26: chapter 8, chapter 12, records
- Skills byte-equal to 2026.10.20.2; docs/05 untouched

work/done/m26-review.md
```
