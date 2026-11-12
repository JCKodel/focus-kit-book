# m33-review

**Objective.** The author can decide whether M33's promise holds, the clauses of its paragraph tested in the PDF of both editions and on this repository, and whether everything changed since m32-review's commit holds under the code reading by areas, with every confirmed finding graded: each grave one a line under this review, the medium and small ones listed here for the author's pick.

This page was defined and built by the agent before the author read it, on the author's word that the agent runs the whole queue, the milestone reviews included; the author reads the page and the diff at the end (docs/05 §4).

**Behaviour.**

* With every line above this review in M33 `[x]` and committed, /apply records the base and the end commit, builds both PDFs at the end commit with `book/` clean, and answers each clause test below: holds, or fails with what was seen. A clause no delivery answers, or one that fails, is a finding (docs/05 §8).
* The review opens by copying onto this page, verbatim, the notes under `## For the review` of every page the range delivered, naming the pages that have none; the checker marks each note as it marks a candidate (docs/05 §8).
* Read-only readers on Opus read one fixed range, `git diff <base>..<end>`, one per area the range touches, at most two running at a time; one checker on Opus then marks every candidate and every note seen, latent or weak against the end commit (docs/05 §5, Milestone review).
* On the author's word, quoted below, the review's session takes the clause tests from its own reading of both PDFs and of the repository, and the word is the confirmation of each candidate the checker marks seen; the latent and weak ones are listed as dropped. These answers are the review's, never the author's (docs/05 §8). The word does not cover the pick of medium findings.
* Every confirmed finding is graded by docs/05 §4 and §8: grave, when it breaks a clause of M33's paragraph for a person on its usual path, loses or exposes data, or leaves verify red, each its own `[ ]` line under this review ending `· after m33-review · from m33-review`; medium, met in ordinary use while the clause holds; small, a rare case, a latent or weak candidate, a cost nobody measured. Medium and small are listed on this page, numbered, medium first, each with a one-phrase reason for its grade.
* The author picks which medium findings enter the one `m33-fixes` line; until then this line stays `[*]`, uncommitted, and no `m33-fixes` line is written.
* A clause with no answer, a reader or checker whose report does not reach this session, or paths of the range no reader read leave this review waiting as `[?]` with `· resume: apply` and the reason (docs/05 §§4, 8).
* Edge, later milestones in the range: the range holds the kit at 2026.11.12 and the process migrations of 2026.10.26 to 2026.11.12 (`kit-2026-10-26`, `kit-2026-10-27`, `kit-2026-10-27-1`, `kit-2026-11-03`, `kit-2026-11-12`), whose chapter lines are open in M34 to M38. A candidate one of those open lines already holds (`ch12-14-mark`, `ch12-14-mark-refused`, `ch14-15-after-all-dropped`, `ch13-apply-next`, and M38's chapter lines) is listed with that line and is no finding here.
* Edge, the kit's own scripts: a candidate in a file the kit installs byte for byte (`.claude/skills/`, `.agents/skills/`) cannot be fixed here without leaving the kit; it is graded as any other, and its fix, when picked, is a note in `work/kit-proposals.md`.
* Edge, the shared tree: readers and the checker read the end commit (`git diff <base>..<end>`, `git show <end>:<path>`), never the working tree or the index; a commit made during the reading does not move the end commit.

**Contract.** Clause tests from docs/06's M33 paragraph, each against its delivery's page in `work/done/` and the named passages. Lines are en / pt at `a9f518e`; where one number is given it is the same in both.

| Clause | Deliveries and passages | The test |
|---|---|---|
| C1. The book teaches focus-kit 2026.10.25 | `ch08-update-2026-10-25`: chapter 8, "Install" (:22), the refusal (:51), the report excerpt (:61 to :84 / :61 to :86), the numbering map line, the update's next command (:109 / :110) | Does chapter 8 show an update's report at the version the repository runs, a migration as its next step, the one-line numbering map for a docs/05 kept by ADR, three small scripts, and the update reading each slug's line from its branch on origin, with no "local or remote"? Do the two editions say the same? |
| C2. And the repository runs on it | `kit-2026-10-25` with `kit-2026-11-12`: the eight installed `SKILL.md`, the three scripts, docs/05 §§2 to 5 and 8, docs/06, docs/03, ADR-0018, ADR-0019 | Do the installed files equal the kit's at 2026.11.12 (Mechanical checks)? Does docs/05 hold 2026.10.25's rules as the kit page lists them? Does `queue.sh` run on this repository's queue? |
| C3. The queue without the `(PA)` token | `kit-2026-10-25`: docs/06; `ch11-14-after`: chapters 11 (:16 to :19) to 14; `ch09-design-slot`: chapter 9 (:23); `ch19-claim-integration`: chapter 19's block | Does any queue line of docs/06, or any chapter's line or tree, carry a token, outside the history paragraphs? |
| C4. `· after` read per command | `ch11-14-after`: chapter 11 (:89 / :92), chapter 12 (:28 to :29), chapter 13 (:37 to :46), chapter 14 (:70 to :80 / :71 to :81) | Does each chapter say `/propose` starts when every line `after` names is `[>]` or beyond and `/apply` when every one is integrated, with the reason? |
| C5. `· after all` on the review line | `ch11-14-after`: chapter 11 (:54, :95, :118 / :57, :98, :121), chapter 14 (:46, :72, :127 / :47, :73, :129); `ch09-design-slot`: chapter 9 (:23); `kit-2026-10-25`: docs/06's review lines | Is every review line in the chapters and in docs/06 written `· after all`, and do chapters 11 and 14 say what it names? |
| C6. Integration as what frees a build | `ch11-14-after`: chapter 13 (:44 to :46, :287), chapter 14 (:71, :75, :80 / :72, :76, :81); `ch19-claim-integration`: chapter 19 (:201) | Is integrated `[x]` on trunk and merged off trunk, and does a `[x]` on an unmerged branch free no build? |
| C7. `queue.sh` reading a branch as a claim and a merge as the integration | `ch19-claim-integration`: chapter 19 (:198 to :229); `ch17-20-branch-on-origin`: chapter 17 (:132), chapter 20 (:63); `ch11-14-after`: chapter 14 (:62 to :64 / :63 to :65) | Does chapter 19 say a branch on origin is the claim, the branch's copy current until the merge and main's after, a `[?]` on any copy blocks, `built, awaiting integration`, a line only a branch has in its milestone? Is chapter 19's block the installed script's output (Mechanical checks)? |
| C8. `claim.sh` create-only and resumable | `ch19-claim-integration`: chapter 19 (:192, :238 to :257) | Does chapter 19 say the claim creates the branch on origin only when no clone has it, `taken` with exit 2, `resume` on the person's word, `here` in the slug's own worktree, the worktree from origin's main? |
| C9. The Design slot and the design delivery | `ch09-design-slot`: chapter 9 (:23 to :50, :105, :133 to :138), chapter 7 (:45, :50, :178), chapter 12 (:49); `kit-2026-10-25`: docs/05 §5 Design, ADR-0019; docs/03's design delivery row | Does chapter 9 name the three forms and "no screens", the defaults, the page not `[>]` without a reference unless the slot says prototype, `/apply` comparing, and Ninjobs' rule as the error? Does chapter 7 count eleven slots? |
| C10. The `## Outcome` heading | `ch09-design-slot`: chapter 12 (:53), chapter 13 (:112); `kit-2026-10-25`: docs/05 §3 | Do chapters 12 and 13 say `/apply` records what happened under `## Outcome` below Done when, so the definition stays as read? |
| C11. The parallel paragraphs of §4 written only where sessions overlap | `kit-2026-10-25`: docs/05 §4 (:226 to :254), kept by §5's Git slot ("Two sessions may work in one tree on free lines"); the book: no M33 line names it | Does the repository's docs/05 keep the two paragraphs because the person said sessions overlap? Does any chapter say the kit writes them only where sessions will overlap, and does any say otherwise (chapter 8 :59)? |

**Base.** `ba80036` (`docs(m32-review): review M32, four findings`), the commit of m32-review, the previous milestone's review (docs/05 §8), the one commit `git log --diff-filter=A -- work/done/m32-review.md` returns. The range therefore holds M32's four finding lines (`ec6258a`, `4459d5b`, `91fde28`, `3370f69`), read by the area readers without a clause and with no second review (docs/05 §8); the kit at 2026.10.27 and 2026.11.12 (`f73eda1`, `84de9f1`) and the five process migrations (`5b13679`, `33432ee`), read without a clause beyond C2; the queue's M33 to M38 (`cd79120`); and M33's five chapter deliveries.

**End.** The commit HEAD is when the reading starts, recorded before any reader; this page and its mark, uncommitted, are read from the working tree as the spec.

**Areas.** `git diff --stat -M <base>..<end>` at the end commit, every path placed in an area of docs/05 §5's Milestone review slot:

* **Build:** no path of the `Makefile`, `scripts/`, the READMEs, `VERSION` or `docs/manuals/` is in the range; no reader.
* **Chapters:** `book/{en,pt}/` 07, 08, 09, 11, 12, 13, 14, 17, 19 and 20, twenty files, split in two readers.
* **The kit's skills:** the eighteen paths under `.claude/skills/` and `.agents/skills/`, each `.agents/` blob equal to its `.claude/` one, read once.
* **The documents:** `AGENTS.md`, `docs/01`, `docs/03`, `docs/05`, `docs/06`, ADR-0018, ADR-0019, and the twenty-one records under `work/done/` the range adds or edits, the run record `ch08-update-2026-10-25-run/` among them.

**Readers.** Four read-only readers on Opus, each keeping the session's advisor, launched as pairs, then one read-only checker on Opus alone; each launch sets its model to Opus, at most two run at a time (docs/05 §5):

* pair 1: **chapters 7, 8, 9, 11 and 12**, and **chapters 13, 14, 17, 19 and 20**, both editions, whole at the end commit and by their range diffs, against their pages and the installed scripts;
* pair 2: **the kit's skills**, against docs/05, docs/03 and the kit pages; and **the documents and records**, against each other, the chapters they describe and docs/04;
* then the checker, on every candidate and every copied note in one report.

Each reader lists the paths it read and how (whole, diff, grep), and says whether it kept the advisor.

**Slow tests.** None (docs/05 §5's Verify slot).

**Known leads**, given to the checker with the readers' candidates:

* L1, C11: chapter 8 en :59 / pt :59 says a docs/05 whose §5 says "trunk, one session at a time" sees the wording for two sessions in one folder proposed, which 2026.10.25's rule, the paragraphs written only where sessions overlap, may no longer do.

**Mechanical checks**, run by /apply at the end commit:

* The installed skills equal the kit's `SETUP.md` §3.1 to §3.8 at `4f5da97` (focus-kit 2026.11.12), in both skills folders; all eight `SKILL.md` carry `version: "2026.11.12"`; §3.9 to §3.14's destinations are not in the range.
* No token on a queue line of docs/06 outside the milestone paragraphs that recount history.
* Chapter 14's six-line tree (en :127 to :140) and chapter 19's block (:204 to :214) rerun with the installed `queue.sh` and `claim.sh` on scratch repositories shaped as `ch11-14-after`'s and `ch19-claim-integration`'s Contracts say, both editions, compared byte for byte.
* The repository's tree: `queue.sh trunk` in this repository prints M33 with `m33-review` in flight, `git status` the same before and after.
* `make book` with `book/` clean; `make verify` after the last edit.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs, `make book` at the end commit.

**Out of scope.**

* Fixing any finding: grave ones become lines, the rest wait for the author's pick (docs/05 §8).
* Re-testing M32's clauses: its fix lines are read by the area readers, not tested by clause.
* Teaching 2026.10.26 to 2026.11.12 in the chapters: M34 to M38's lines.
* The kit's README, CHANGELOG and `test/`, which SETUP §3 does not install.
* The pick of medium findings and the `m33-fixes` line: the author's.

**Decisions from the documents.**

* The base is m32-review's commit, `ba80036`, the first of docs/05 §8's cases.
* No build reader: the range touches no build path (docs/05 §8, one reader per area it touches).
* The clause tests and the confirmation are the review's, on the author's word quoted on this page (docs/05 §8); the medium pick stays the author's (`kit-2026-11-12`, Left as they were).
* The notes are copied from every page the range delivered (docs/05 §8), the kit pages included, which hold none.

**Decisions taken alone.** The agent chose each of these, for the author's review.

* C1 reads "teaches focus-kit 2026.10.25" as teaching the version the repository runs, 2026.11.12, which holds 2026.10.25's rules: `ch08-update-2026-10-25`'s first decision and its note hand the clause to this review so.
* M33's paragraph is taken as eleven clauses, by what can be checked.
* The chapters area splits in two, twenty files being too many for one careful reading (docs/05 §8).
* A candidate an open M34 to M38 line holds is listed with that line, as m32-review did for M33's.
* A candidate in a kit-installed file is graded here; its fix, if picked, is a kit proposal.

**Done when.**

* [x] Every line above this review in M33 is `[x]` and committed; every clause has the review's answer, on the author's word quoted on this page.
* [x] Base, end, the inventory by area, each reader's paths read and its advisor, every copied note and candidate with its mark are on this page.
* [x] Every confirmed finding graded; each grave one a `[ ]` line under this review; medium and small listed, numbered, medium first.
* [x] The mechanical checks recorded; `make book` built both PDFs at the end commit; `make verify` green after the last edit.
* [x] The author's pick of medium findings recorded and, when any, the `m33-fixes` line written; the page in `work/done/`, its paths staged and its commit message suggested.

## Outcome

**Precondition.** Every line above this review in M33 is `[x]` and committed: `kit-2026-10-25` in `5b13679` and `cd79120`, `ch11-14-after` `8ff514d`, `ch19-claim-integration` `9335b2d`, `ch17-20-branch-on-origin` `e8e5673`, `ch09-design-slot` `ab3db89`, `ch08-update-2026-10-25` `a9f518e`. `git log --diff-filter=A -- work/done/m32-review.md` returns `ba80036` alone.

**Base and end.** Base `ba80036`; end `a9f518e` (`docs(ch08-update-2026-10-25): teach the 2026.11.12 update in chapter 8`), HEAD when the reading started, recorded before any reader. This page and its marks are uncommitted and outside the range.

**Inventory.** `git diff --stat -M ba80036..a9f518e`: 67 paths, by area. Build: none. Chapters (20): `book/{en,pt}/` 07, 08, 09, 11, 12, 13, 14, 17, 19, 20. The kit's skills (18): `.claude/skills/` and `.agents/skills/` each `analyze/SKILL.md`, `analyze/references/documents.md`, `apply/SKILL.md`, `brainstorm/SKILL.md`, `brainstorm/references/documents.md`, `propose/SKILL.md`, `propose/scripts/claim.sh`, `mark.sh`, `queue.sh`. The documents (29): `AGENTS.md`, `docs/01-Architecture.md`, `docs/03-Domain.md`, `docs/05-Process.md`, `docs/06-Queue.md`, ADR-0018, ADR-0019, and under `work/done/` `ch08-update-2026-10-24.md`, `ch08-update-2026-10-25.md` and its run record (`README.md`, `update.md`, `refusal.md`), `ch09-design-slot.md`, `ch11-14-after.md`, `ch11-14-queue-tree.md`, `ch14-key-points-pointers.md`, `ch17-20-branch-on-origin.md`, `ch19-claim-integration.md`, `ch19-example-marks.md`, `ch19-queue-branches.md`, `kit-2026-10-24.md`, `kit-2026-10-25.md`, `kit-2026-10-26.md`, `kit-2026-10-27.md`, `kit-2026-10-27-1.md`, `kit-2026-11-03.md`, `kit-2026-11-12.md`, `m32-records-claims.md`, `queue-tree-row-source.md`.

**Slow tests.** None (docs/05 §5's Verify slot).

**Mechanical checks**, at `a9f518e`, outside this repository:

* `git -C <kit> show 4f5da97:SETUP.md` §3.1 to §3.8 rendered to their destinations: all eighteen installed paths byte-equal, in both skills folders; each `.agents/` blob equals its `.claude/` one; all eight `SKILL.md` carry `version: "2026.11.12"`. §3.9 to §3.14's destinations are not in the range.
* docs/06: `(PA)`, `(P-)`, `(-A)`, `(--)` appear only in the milestone paragraphs and one line that recount history (:617, :622, :645, :683, :730), on no line's suffix.
* Chapter 14's six-line queue, run with the installed `queue.sh trunk` on a scratch repository under chapter 11's heading: byte-equal to en :133 to :141 and pt :135 to :143. Chapter 19's fixture (a bare origin, `main/`, both lines claimed with `claim.sh ... worktree .focus-kit focus-kit/`, `return-book` pushed at `[*]` with `damaged-copy` added, `overdue-list` pushed at `[>]`), run from `main/`: byte-equal to :205 to :213 in both editions.
* The repository's tree, `queue.sh trunk`, exit 0, `git status --porcelain` the same before and after: `milestone: M33. focus-kit 2026.10.25`, `[*] m33-review · in flight: apply`, both free lists `none`, `next: none`.
* `git status --short book/` empty before `make book`; `make book` at `a9f518e`, exit 0, 16 seconds: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. `git branch --list`: `main` alone.

**The author's word for this review.** Relayed to this session by the agent running the queue on the author's behalf, on 2026-11-12: "Rodar todas, uma por marco" (run every milestone review, one per milestone) and "Responder com a recomendada" (answer with the recommended option). By it, the clause answers below are the review's, from its own reading of both PDFs (`pdftotext -layout`) and of the repository at `a9f518e`, never the author's, and each candidate the checker marks seen is confirmed, the latent and weak ones listed as dropped (docs/05 §8). The word does not cover the pick of medium findings, which waits for the author.

**The clause answers, the review's.** Pages en / pt.

* **C1, the book teaches the kit: holds**, read as decided above. Chapter 8, en 80 / pt 83: "three small scripts the commands run through git" ("três pequenos scripts"); en 82 / pt 86: the excerpt of the 2026.11.12 report, the docs/05 migration as its next step "not a command"; en 83 / pt 87: "migrates by one line under the title of its docs/05 ... `§4 is §6 here`"; :109 / :110, the update reading each slug's line from its branch on origin. No "local or remote" in either PDF.
* **C2, the repository runs on it: holds.** The installed files are 2026.11.12's (Mechanical checks); docs/05 §§2, 3, 4, 5 and 8 hold the rules `kit-2026-10-25` lists (claim by `claim.sh`, Visual reference and Outcome, `after` per command, `after all`, integration, the file check, the Design slot); `queue.sh` runs on this queue.
* **C3, the queue without the token: holds.** No token on a line of docs/06 or in any chapter, in either PDF.
* **C4, `· after` read per command: holds.** Chapter 11, en 111 / pt 116: `/propose return-book` may start once `lend-book` is `[>]` or beyond, `/apply` once it is integrated; chapter 14, en 150 / pt 159, with the reason (pages, code); chapters 12 :28 and 13 :44 say the same.
* **C5, `· after all` on the review line: holds.** Every review line in chapters 9, 11 and 14 and in docs/06 ends `· after all`; chapter 14, en 150 / pt 159, says what it names.
* **C6, integration frees a build: holds.** Chapter 14, en 150 / pt 159: "Integrated is `[x]` on trunk; with a branch or a worktree per delivery it is the delivery merged"; chapter 13 :44 to :46; chapter 19, en 206 / pt 216, `built, awaiting integration`.
* **C7, `queue.sh` reading a branch as a claim and a merge as the integration: holds.** Chapter 19, en 206 / pt 216: the branch on origin is the claim, `claimed, progress unknown`, the branch's copy current until the merge, a `[?]` on any copy blocks; the block is the installed script's run (Mechanical checks).
* **C8, `claim.sh` create-only and resumable: holds.** Chapter 19, en 208 / pt 219: `claim: taken`, exit 2, `resume` on the person's word printing `claim: resumed`, `claim: here` in the slug's own worktree, the worktree from origin's main branch; :192, the branch created only when origin has none. Chapter 13 :29 still says "creating or reusing" (medium finding M3 below).
* **C9, the Design slot and the design delivery: holds.** Chapter 9, en 93 / pt 97: the three forms, "no screens", `docs/ui/`, the defaults, the page not `[>]` without a reference unless the slot says prototype, `/apply` comparing, Ninjobs' rule and the stretched phone layouts; chapter 7 counts eleven slots (en 70 / pt 73).
* **C10, the `## Outcome` heading: holds.** Chapter 12, en 120 / pt 126, and chapter 13, en 136 / pt 143: what happened goes under `## Outcome`, below Done when, so the definition stays as it was read.
* **C11, the parallel paragraphs of §4 written only where sessions overlap: fails in the book.** The repository holds: docs/05 §4 :226 to :254 keeps the two paragraphs because §5's Git slot says two sessions may work in one tree. No chapter teaches that the kit writes them only where sessions overlap (chapter 9 :23, `/brainstorm`'s first milestone, does not say it), and chapter 8, en 82 / pt 85, says the opposite: a docs/05 whose §5 says "trunk, one session at a time" sees the two-session wording proposed. No M33 line named this clause. Grave finding G1.

**Readers.** Four read-only readers on Opus as two pairs, then the checker on Opus alone; at most two ran at once. Each was launched from this session with its model set to Opus, ran in the background, and delivered its final report to this session as its completion notice, recorded here. Working notes in the session's scratchpad, `m33/`.

* **Reader 1, chapters 7, 8, 9, 11, 12.** Whole: en 08, 11, 12; en 07 and 09 by range diff and grep; pt five by range diff, grep and targeted ranges; the delivery pages and `update.md` by grep (`refusal.md` and the run README not opened); docs/06 M33 to M38; docs/04 and docs/05 by grep; the kit's `SETUP.md` in parts. Advisor present, called twice.
* **Reader 2, chapters 13, 14, 17, 19, 20.** Whole: en 13, 14, 19, 20; en 17 :100 to :134 and its diff; pt five by range diff, spot reads and a code-span parity script; `claim.sh` whole, `queue.sh` and apply's `SKILL.md` in parts; docs/05 :140 to :194 and :228 to :250; docs/03 and docs/04 by grep; scratch runs of chapters 13 and 14's examples. Advisor present, called twice.
* **Reader 3, the kit's skills.** Whole: the four `SKILL.md`, the three scripts, `documents.md`, docs/05, ADR-0019, the six kit pages, `work/kit-proposals.md`, AGENTS.md; docs/06 and ADR-0018 in part; docs/03 by grep; scripts run on scratch repositories. Advisor present, called twice.
* **Reader 4, the documents and records.** Whole: docs/05, docs/06's header and M31 to M38, ADR-0019, every record of the inventory and the run record; by diff and grep: AGENTS.md, docs/01, docs/03, ADR-0018 and four older records; docs/04 by grep. Advisor present, called once.
* **The checker**, one agent on every candidate, note and lead in one report, each file opened at `a9f518e`: 44 seen, 7 latent, 4 weak. Its report says it had the advisor and its one call was rate-limited, so no advice was received.

Every path of the inventory was read by at least one reader, by its range diff at the least.

**Notes copied**, verbatim from the `## For the review` headings of the range's pages; the pages with none: `ch08-update-2026-10-24`, `ch11-14-queue-tree`, `ch19-queue-branches`, `kit-2026-10-24`, `kit-2026-10-25`, `kit-2026-10-26`, `kit-2026-10-27`, `kit-2026-10-27-1`, `kit-2026-11-03`, `kit-2026-11-12`, `m32-records-claims`, `queue-tree-row-source`.

* N1 (`ch08-update-2026-10-25`): The queue line and M33's paragraph name 2026.10.25 while chapter 8 now shows the 2026.11.12 report (this page's first decision); `m33-review` reads that clause against chapter 8 as it is.
* N2 (`ch08-update-2026-10-25`): book/en/08-install-and-hosts.md:103 and :111 (pt :104 and :112) tell what happened on the book's repository at earlier updates ("at 2026.10.20.3 ... §7 now admits", "as the book's docs/05 §4 kept its sentence"), past-tense accounts of earlier runs that docs/04's No runs and The kit as it is may not allow. Older than this delivery.
* N3 (`ch09-design-slot`): book/en/09-starting-a-project.md:30 and :103 (pt the same lines) both point to chapter 15, and pt :128 points to chapter 17 where en :128 does not: a reader meets the same pointer twice, and the editions differ (docs/04, Chapter pointers). Older than this delivery.
* N4 (`ch11-14-after`): book/en/14-queue-states.md:46, pt :47: on the nine-line milestone the review's tree row prints 141 columns (en), past docs/04's 74, so a realistic milestone's tree cannot be shown whole; the chapter draws it on six lines.
* N5 (`ch11-14-after`): book/en/12-propose.md and pt, Key points: six bullets against docs/04's five, older than this delivery.
* N6 (`ch11-14-after`): book/en/12-propose.md:30, book/en/13-apply.md:29, and pt: the claim described as reusing or creating a branch; `claim.sh` is create-only and opens another clone's branch only with `resume`; `ch19-claim-integration` covers chapter 19 only.
* N7 (`ch11-14-after`): book/en/15-closing-a-milestone.md:123, pt :126: `[x] m1-review` without `· after all`, which chapters 11 and 14 now write.
* N8 (`ch11-14-after`): book/en/19-worktrees.md:205-215, pt: the tree still prints `together:` and `(P-)`, which the installed script no longer does.
* N9 (`ch14-key-points-pointers`): ch08 en :36, :42, :120 (pt :122), ch12 en :28 to :155 (pt :28 to :164), ch13 :19 to :252: forward pointers there before M32 repeat a target in the same chapter (counts under Out of scope), which docs/04 :43's "once per chapter for each target" does not allow; a reader meets "(chapter 14)" six times in chapter 12 and "chapter 19" nine times in chapter 13. The author may cut them to one per target or restate the rule.
* N10 (`ch14-key-points-pointers`): Chapters 1 (seven), 12, 21 and 24 (six each), both editions: more key points than docs/04's chapter shape allows (at most five); a reader sees the longer list. The author may fold them or restate the rule.
* N11 (`ch17-20-branch-on-origin`): work/done/kit-2026-10-25.md:20: lists chapters 17 and 20 among those that "still teach the token"; neither carried it at `9335b2d` (decision 1 above).
* N12 (`ch17-20-branch-on-origin`): book/en/14-queue-states.md:66 (pt the same): the project's mirror "shows the mark at once", with no "on trunk", and "every delivery's mark"; chapter 20 :62 to :63 now say at once on trunk and, with a branch, at the first refresh after the push, with "every other delivery's"; a reader may see the two as contradicting.
* N13 (`ch19-claim-integration`): book/en/19-worktrees.md:93 and key point 4 (pt the same): the worktree's second case, one person whose deliveries touch the same files, stays as focus-kit's `SETUP.md` Git slot names it, beside the file check that builds them one after the other; a reader may not see its gain. The author may name it (each delivery defined and committed on its own branch) or drop it.
* N14 (`ch19-claim-integration`): Kit, `claim.sh`: the "ahead" note prints twice, the second garbled (`by ;`), its `printf` given three arguments for two `%s`.
* N15 (`ch19-claim-integration`): Kit, `claim.sh`: two clones that claim one slug at once from the same commit of origin's main both get `claim: new`, the create-only push being a no-op on an equal commit.
* N16 (`ch19-claim-integration`): Kit, `claim.sh`: a clone made with `git clone --bare` after a claim answers `existing` for it, not `taken`.
* N17 (`ch19-claim-integration`): Kit, `claim.sh`: a local branch with no worktree and not on origin makes it stop with git's `fatal: a branch named ... already exists`, exit 255, not `error:` and exit 2; book/en/19-worktrees.md:255 says `existing` for "this clone's worktree or branch".
* N18 (`ch19-claim-integration`): Kit, `queue.sh`: a line only a branch has goes after the review line, so `m2-review` is `propose now` with `damaged-copy` undefined (book/en/19-worktrees.md:217, pt the same), as the chapter prints and does not explain.
* N19 (`ch19-example-marks`): book/en/19-worktrees.md :93, :97 to :101, :386 and the key points (pt the same lines): they say deliveries whose files meet build at once in worktrees, `return-book` and `overdue-list` on `src/features/loans/` "at the same time", while :215, now, shows the same pair waiting, since 2026.10.24's `-` holds `/apply` in worktrees too and 2026.10.25 makes the overlap a conflict before `/apply`'s first edit; a reader sees the chapter's case for worktrees and then the pair not built at once. The person may give it to `ch19-claim-integration` or a line of its own.

**Candidates.** The checker's marks, lines at `a9f518e`, en with pt the same unless given; `=` joins duplicates, graded once.

| Id | Where | Candidate | Mark |
|---|---|---|---|
| L1 = R1-1, R1-2 | ch08 :59; ch09 :23 | The parallel paragraphs written only where sessions overlap, taught nowhere; ch08 says a trunk one-session docs/05 sees them proposed | seen |
| R1-3 | ch11 en :74, :97, :176, :195 / pt :77, :100, :181, :200 | Every finding a `[ ]` line, against ch08 :91 and docs/05 §4 | seen |
| R1-4 | ch11 en :147, :155 / pt :151, :160 | A page that changes the loan screen with "Visual reference. None." | seen |
| R1-5 | ch07 en :62 / pt :63 | `· after` "holds a line until another is done" | seen |
| R1-6 = R2-8, N3, N9 | ch07 to ch13 | Forward pointers repeated per target (ch11 to 14, ch09 to 15, ch12 to 19, ch13 to 19) | seen |
| R1-7 | ch11 :95; ch07 :45; ch09 :22 | "Waits for the lines above it" without the dropped ones; Verify's ceiling unnamed; ch12 :31's part held by `ch12-14-mark` | seen |
| R1-8 | ch12 :29 | Branch on origin read without "until the merge" | seen |
| R2-1 = N12 | ch14 en :65 / pt :66 | The mirror "shows the mark at once" for both strategies | seen |
| R2-2 = N6 | ch13 :29 | The claim "creating or reusing it", no `taken`, no `resume`; ch12 :30's half weak | seen |
| R2-3 | ch14 :61, :247 | "A line whose branch exists is taken" against ch19's tree | seen |
| R2-4 | ch13 :117 | A `[?]` leaving at `/apply`'s end off trunk | seen |
| R2-5 | ch14 :92, :110 | Implies worktrees let same-file builds run together | seen |
| R2-6 | ch14 :160; ch19 :24 | "Must be `[x]` first", "done first" | seen |
| R2-7 | ch19 :198 | Every line from origin; the worktree's own copy is local | seen |
| R2-kit | apply `SKILL.md` :35 | File check against in-flight builds only | latent |
| R2-later | ch14 :199 | "By the free rule alone" | seen, held by `ch14-15-after-all-dropped` |
| R3-1 | `claim.sh` :84, :101 to :104, :119 to :122 | Any rejected push reported as `taken` | latent |
| R3-2 | `mark.sh` :66 to :76 | Writes, prints `marked:`, then exits 2 | seen |
| R3-3 ⊂ R4-13 | docs/03 :122 | Queue tree row without `findings:` and the warning | seen |
| R3-4 | `work/kit-proposals.md` :27 | Item 14 already taken by 2026.10.25 | seen |
| R4-1 | docs/05 :482 to :484 against :494 to :499 | Latent and weak "dropped" and also small, a line on the pick | seen |
| R4-2 | ch08 en :69, :79, :90 / pt :70, :80, :91 | The excerpt and prose give `None`, which the run record does not hold | seen |
| R4-3 | `ab3db89`'s body | Two wrapped bullets | seen |
| R4-4 | `kit-2026-11-12.md` :13; docs/06 :125, :501, :611 | docs/06 lines carrying history left unreported | seen |
| R4-5 | `kit-2026-11-12.md` :19 | "53 closed lines" | weak |
| R4-6 | three kit pages | Cite ADR-0014 for the prefix and the release commit | seen |
| R4-7 | docs/06 :747, :767, :777 | Kit lines `[x]` for reinstalls that never ran; :757 weak | seen |
| R4-8 | `f73eda1`, `5b13679`, `84de9f1`, `33432ee` | Subjects without `<type>(<slug>):`; a body naming docs/04 | seen |
| R4-9 | `kit-2026-10-26.md` :3, :10 | "Three marks" unnamed; dated 10-26, lines added 11-12 | seen |
| R4-10 = N11 | `kit-2026-10-25.md` :20 | Chapters 17 and 20 "still teach the token" | seen |
| R4-11 | docs/06 :737 | `ch09-design-slot`'s line promises `chassi-desktop` and Outcome in chapter 9 | seen |
| R4-12 | ADR-0018 :88 | A dated amendment rewritten in place | seen |
| R4-13 ⊃ R3-3 | docs/03 :116, :122 | `[x]` for integrated; no `findings:`; no `mark.sh` row | seen |
| N1 | | The version clause | weak, the queue line names 2026.11.12 and C1 reads so |
| N2 | ch08 :103, :111 | Past runs told | seen |
| N4 | ch14 :46 | The nine-line tree's review row 144 columns | seen |
| N5 ⊂ N10 | ch12 | Six key points | seen |
| N7 | ch15 en :123 / pt :126 | `[x] m1-review` without `· after all` | seen |
| N8 | ch19 | `together:` and `(P-)` | weak, fixed by `ch19-claim-integration` |
| N10 ⊃ N5 | ch01, 12, 21, 24 | Over five key points | seen |
| N13 | ch19 :93, key point 4 | The worktree's second case | seen |
| N14 to N17 | `claim.sh` | Off-trunk claim flaws | latent |
| N18 | ch19 :207 to :220 | `m2-review` free with `damaged-copy` undefined | latent |
| N19 | ch19 | Pairs on the same files at once | weak, fixed by `ch19-claim-integration` |

**Findings.** By the author's word, every candidate marked seen is confirmed; the latent and weak ones are dropped and listed under small (docs/05 §8). R2-later is held by `ch14-15-after-all-dropped`, no finding here.

*Grave*, one line each under this review in docs/06:

* G1: L1, R1-1, R1-2, C11 failing in the book: `ch08-09-parallel-paragraphs`. Grave because it breaks a clause of M33's paragraph for every reader (docs/05 §4).

*Medium*, met in ordinary reading while the clauses hold, for the author's pick:

1. M1, R1-3: chapter 11 (en :74, :97, :176, :195) says every review finding becomes a line, against chapter 8 :91 and docs/05 §4; no open line names chapter 11.
2. M2, R1-4: chapter 11 (en :147, :155) shows a page that changes a screen with "Visual reference. None.", against the Design slot chapter 9 now teaches.
3. M3, R2-2 = N6: chapter 13 :29 says the claim creates or reuses the branch, with no `taken` or `resume`, against chapter 19 and `claim.sh`.
4. M4, R2-1 = N12: chapter 14 :65 says the mirror shows a mark at once with a branch too, against chapter 20 :62 to :63.
5. M5, R1-5: chapter 7 :62 says `· after` holds a line until another is done, against `after` read per command.
6. M6, R4-2: chapter 8 :69, :79, :90 quote `None` as the report's wording, which the run record does not hold.

*Small*, each a rare case, a wording a reader rarely meets, or a record's precision:

7. R1-6 = R2-8, N3, N9: forward pointers repeated per target in chapters 7 to 13.
8. N10 ⊃ N5: chapters 1, 12, 21 and 24 over five key points.
9. R1-7: chapter 11 :95 without the dropped lines; chapters 7 and 9 without Verify's ceiling.
10. R1-8: chapter 12 :29 without "until the merge", off trunk only.
11. R2-3: "a line whose branch exists is taken" against chapter 19's tree.
12. R2-4: chapter 13 :117, a `[?]` leaving off trunk before integration.
13. R2-5: chapter 14 :92, :110 suggest worktrees lift the file check.
14. R2-6: chapter 14 :160 and chapter 19 :24, "done first".
15. R2-7: chapter 19 :198, the worktree's own copy read locally.
16. N2: chapter 8 :103, :111 tell past runs.
17. N4: the nine-line tree's review row over 74 columns.
18. N7: chapter 15 :123 without `· after all`.
19. N13: chapter 19 :93, the worktree's second case unexplained.
20. R3-2: `mark.sh` writes then exits 2 on an unstaged line (a kit proposal).
21. R3-4: `work/kit-proposals.md` item 14 stale.
22. R4-13 ⊃ R3-3: docs/03 :116, :122, no `mark.sh` row.
23. R4-1: docs/05 §8 on latent and weak, dropped and small at once.
24. R4-3: `ab3db89`'s wrapped bullets, in history.
25. R4-4: docs/06 lines carrying history left unreported.
26. R4-6: three kit pages cite ADR-0014.
27. R4-7: kit lines `[x]` for reinstalls that never ran.
28. R4-8: four commits' subjects and a body.
29. R4-9: `kit-2026-10-26` :10 and its date.
30. R4-10 = N11: `kit-2026-10-25` :20 on chapters 17 and 20.
31. R4-11: docs/06 :737 promising what chapter 9 left out.
32. R4-12: ADR-0018 :88 rewritten in place.
33. Dropped, latent: R2-kit, R3-1, N14, N15, N16, N17, N18.
34. Dropped, weak: R4-5, N1, N8, N19.

**Proof.** The mechanical checks and the clause answers above; `make book` at `a9f518e`; `make verify` green after the last edit to this page and docs/06, 13 seconds, under the five-minute ceiling.

**The author's pick.** Relayed to this session by the agent running the queue on the author's behalf, on 2026-11-12: "Todos os 6" (all six). M1 to M6 enter the one `m33-fixes` line, each an item of its page, which is their list and is not split; no small finding is picked, so none becomes a line (docs/05 §8). The line sits under `ch08-09-parallel-paragraphs`, both `· after m33-review · from m33-review`; chapter 8 is in both, and `/apply`'s file check builds them one after the other.

The author authorized one commit per slug for this run; this /apply commits this delivery itself, with the message below, and never pushes.

```commit
docs(m33-review): review M33, one grave finding, six medium fixes

- Base ba80036, end a9f518e; ten clauses hold, C11 fails in the book
- Kit files, chapter 14 and 19 trees and the repository tree checked
- Four readers and a checker: 44 seen, 7 latent, 4 weak
- ch08-09-parallel-paragraphs and m33-fixes under m33-review

work/done/m33-review.md
```

**Decisions taken alone in /apply.** For the author's review.

* The readers ran in the background and reported by completion notice, as m32-review's did.
* G1 joins chapters 8 and 9 in one line: both passages state the one rule.
* Medium is a contradiction a reader meets in an ordinary reading of a chapter against what M33 teaches; the same contradiction confined to off-trunk work, a record or a script is small. R4-2 is medium under AGENTS.md's rule that every quoted artifact is real.
