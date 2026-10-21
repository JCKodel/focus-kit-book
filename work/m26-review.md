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
* The line's token `(--)` holds: this review reads every page and file above it, so neither its definition nor its build may run beside them (docs/05 §4); no correction.

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

* [ ] Every line in this review's `after` is `[x]`, and every clause above has the review's answer from its reading of the passages in both PDFs, recorded as the review's, not the author's.
* [ ] Base, end commit, the inventory of paths by area, the slow tests (none), each reader's paths read, whether each agent kept the session's advisor, and every checked candidate with its mark are recorded on this page.
* [ ] Every seen candidate is in a `[ ]` line under this review, shared causes sharing a line, handed to the driver to add to docs/06; every latent and weak candidate is listed as dropped; nothing is fixed here.
* [ ] The mechanical checks above are recorded with their results; `make verify` is green after the last edit and `make book` built both PDFs at the end commit, both run by this /apply and recorded in its Proof with the commit and both PDF paths.
* [ ] Delivery review as docs/05 §5 says, its advisor recorded as it ran; only this page and its docs/06 hunk staged; the page moved to `work/done/` and its commit message suggested in a `commit` block, which ends the page.
