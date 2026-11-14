# m40-review

**Objective.** The author can decide whether M40's promise holds, the clauses of its paragraph tested in the PDF of both editions and on this repository, and whether everything changed since the end m39-review's page names holds under the code reading by areas, with every copied note checked and every confirmed finding graded: each grave one a line under this review, the medium ones in the one `m40-fixes` line, the small ones listed here.

This page was defined by the agent before the author read it, on the author's word for this run, relayed by the driver session on 2026-11-14: "Vamos rodá-la de ponta a ponta automaticamente, sem pausas para concluir o milestone" (run M40 end to end without pauses). Every question the documents leave open is answered by the agent's recommendation, written below as the agent's choice; the page is built before the author read it, and the author reads the page and the diff at the end (docs/05 §4).

**Behaviour.**

* With every line above this review in M40 `[x]` and committed (`kit-2026-11-14` in `4dc1a44` and `d26ccc7`, `ch15-base-last-end` `cf628af`, `ch12-pages-on-branches` `cd5612d`), /apply records the base and the end commit, reads both PDFs at the end commit, runs §5's slow tests (none today), and answers each clause test below: holds, or fails with what was seen. A clause no delivery answers, or one that fails, is a finding (docs/05 §8).
* The review opens by copying onto this page, verbatim from the end commit, the notes under `## For the review` of every page the range delivered, naming the pages that have none (today `m39-fixes` has one; `m39-review`, `kit-2026-11-14`, `ch15-base-last-end` and `ch12-pages-on-branches` have none; `ced5c8a`, the release, and `6a91138`, a queue-only edit, have no page); the checker marks each note as it marks a candidate (docs/05 §8).
* Read-only readers on Opus read one fixed range, `git diff <base>..<end>`, one per area the range touches, at most two running at a time; one checker on Opus then marks every candidate, every copied note and every lead seen, latent or weak against the end commit (docs/05 §5, Milestone review). Every launch sets its model to Opus, runs in the foreground so its report reaches this session, and keeps the session's advisor.
* On the author's word, quoted below, the review's session takes the clause tests from its own reading of both PDFs and of the repository, and the word is the confirmation of each candidate and note the checker marks seen; the latent and weak ones are listed as dropped. These answers are the review's, never the author's (docs/05 §8).
* Every confirmed finding is graded by docs/05 §4 and §8: grave, when it breaks a clause of M40's paragraph for a person on its usual path, loses or exposes data, leaves verify red, or is a fix a delivery in flight cannot go on without, each its own `[ ]` line under this review ending `· after m40-review · from m40-review`; medium, met by a person in ordinary use while the clause holds; small, a rare case, a latent or weak candidate, a cost nobody measured.
* On the author's word ("Corrigir em m40-fixes", below), every medium finding enters the one `m40-fixes` line, each an item of its page, which is their list and is not split, the line under this review ending `· after m40-review · from m40-review`; with no medium finding, no line. Small ones are listed on this page, numbered, and none becomes a line.
* A reader or checker whose report does not reach this session, or paths of the range no reader read, leave this review waiting as `[?]` with `· resume: apply` and `· blocked: <what was read>`, the third of docs/05 §4's three cases (docs/05 §8). A clause with no answer is a finding, not a wait.
* Edge, the base this milestone teaches: this is the first review whose base is the previous review's recorded end, not its commit. m39-review's page names its end `8d5d063` (Outcome, "End `8d5d063`"), and `b3afef0`, its own commit, is that end's child, so the range holds m39-review's page itself, which is read as a document.
* Edge, M39's fix line in the range: `m39-fixes` (`4130e9e`, five items in chapters 8, 12, 14, 19 and 21) is read by the area readers without a clause test and with no second review (docs/05 §8); its five items are given to the checker as a lead, read as fixed.
* Edge, the kit's update in the range: `kit-2026-11-14` (`4dc1a44`, the kit's files in both skills folders; `d26ccc7`, docs/05, docs/03, ADR-0018, `work/kit-proposals.md` and its record) was applied outside /propose and /apply, with no page defined first and no Delivery review; the readers of the kit's skills and of the documents are its only reading, and K2 tests its result.
* Edge, the commits with no page: `ced5c8a` (`VERSION` only, `make release`'s commit, docs/05 §6) and `6a91138` (M40's paragraph and lines, docs/06 only) are in the range, read by the documents reader.
* Edge, the kit's own text: a candidate in the kit's files or in its template's wording is graded as any other, and its fix, when it enters, is a note in `work/kit-proposals.md`, since the project does not edit the kit's files.
* Edge, the shared tree: readers and the checker read the end commit (`git diff <base>..<end>`, `git show <end>:<path>`), never the working tree or the index; scripts of the kit run only on scratch repositories, never on this one's origin. The PDFs read are the ones built at the end commit.

**Contract.** Clause tests from docs/06's M40 paragraph (:819, "When this milestone closes, the book teaches focus-kit 2026.11.14 and the repository runs on it: the base of a milestone review's range being the end the last review's page names, the commit its reading started at, so a delivery committed while a review reads falls in the next range, also after a dropped review; docs/05 §8 saying what a Milestone review slot that says none means; `/propose` reading the page of each delivery in flight in `work/` or on its own branch, and a resumed `/propose` keeping its line's mark; no sentence of the kit telling a line held by `after` as waiting; `queue.sh` clearing a `[?]` a line's own branch inherited once main clears it, and naming an `after` in its two error lines."), each against its delivery's page and the named passages; lines en / pt at `cd5612d`. The clause ids are this review's.

| Clause | Deliveries and passages | The test |
|---|---|---|
| K1. The book teaches focus-kit 2026.11.14 | `ch15-base-last-end` (chapter 15), `ch12-pages-on-branches` (chapters 12 and 19), and `m39-fixes`' rewording of chapters 8, 12, 14, 19 and 21 | Does each chapter teach what 2026.11.14 changed as the installed skills, `queue.sh` and docs/05 have it, the kit as it is, with no "no longer" of the kit (docs/04)? Does no chapter still say a phrase 2026.11.14 displaced: the base as the previous review's commit, the deliveries in flight in `work/` alone, the first edit marking `[~]` a line resumed, a line held by `after` told as waiting, the fixes "waiting for" `/propose` (Mechanical checks)? Do the two editions say the same, in docs/03's Portuguese terms? |
| K2. And the repository runs on it | `kit-2026-11-14` (`4dc1a44`, `d26ccc7`; no page first, no Delivery review): docs/05 §8 :466 to :472 and :492 to :494, §4's sentences on `after`; docs/03's milestone review and queue tree rows; ADR-0018 :118, "## Amendment, 2026-11-14 (kit-2026-11-14)"; `work/kit-proposals.md` :16 | Do the installed skills, in both folders, equal `SETUP.md` §§3.1 to 3.8 at `c6203d6`, focus-kit 2026.11.14? Does docs/05 hold the template's 2026.11.14 text where the record says it does, ADR-0018 the amendment, docs/03 rows that agree, and `work/kit-proposals.md` entries 9 to 13 and 15 as taken? Does `queue.sh` on this repository's docs/06 print M40 with every line in it? |
| K3. The base, the end the last review's page names | `ch15-base-last-end`: chapter 15 `## Read the code since the base` :23 (C1), `## No second review` :191 (C4), key point 2 :217 (C5); docs/05 §8 :466 to :470 | Do chapter 15 and docs/05 §8 name the base as the end named by the page of the last review that ran, the commit its reading started at, never that review's own commit, the first commit for a first milestone, and "where no earlier review ran" a commit the page names and why? Does this review's own base follow it? |
| K4. A delivery committed while a review reads falling in the next range | `ch15-base-last-end`: chapter 15 :25 to :27 (C2) | Does chapter 15 say that the range from that base holds what was committed while the last review read, that review's own commit and the fixes, that a delivery committed after a review's end and before its commit falls in the next range, and the error a base at the review's own commit would make, dated 2026-11-14 as a finding of this book with no project or version named? |
| K5. Also after a dropped review | `ch15-base-last-end`: chapter 15 :28 (C2's last sentence), :23 "ran" | Does chapter 15 say that after a cancelled review the base is the end of the last review that ran, with the library's `m2-review` and `m3-review`, as docs/05 §8 implies? |
| K6. docs/05 §8 saying what a slot that says none means | `kit-2026-11-14`: docs/05 §8 :492 to :494; `ch15-base-last-end`: chapter 15 :114 (C3) | Does docs/05 §8 say a slot that says none has no code reading, the page still names the range with its end the commit `HEAD` was when the review started, and the person still tests each clause, as the template at `c6203d6`? Does chapter 15 say the same, and docs/03's milestone review row agree? |
| K7. `/propose` reading the page of each delivery in flight in `work/` or on its own branch | `ch12-pages-on-branches`: chapter 12 `## What /propose does` :27 (C1), chapter 19 `## Proposing in a batch` :360 (C2); `propose/SKILL.md` :19 to :20 | Do chapters 12 and 19 say `/propose` reads the page of each delivery in flight, in `work/` or on its own branch, as the installed skill says, true on trunk and with a branch or worktree per delivery? |
| K8. A resumed `/propose` keeping its line's mark | `kit-2026-11-14`: `propose/SKILL.md` :29 to :30; `ch12-pages-on-branches` C3: chapter 12 :31 to :32 | Does the installed skill say the first edit marks a `[ ]` line `[~]` and a resumed line keeps its mark, and does chapter 12 teach it, with no chapter saying a resumed `/propose` marks `[~]` again? Does `mark.sh` refuse a second `[~]` (scratch run)? |
| K9. No sentence of the kit telling a line held by `after` as waiting | `kit-2026-11-14`: docs/05 §4 and §5, `apply/SKILL.md`, both `references/documents.md`, `queue.sh`'s comments and messages | Read every "wait" in the installed kit files and in the kit's sentences of docs/05: is each said of a `[?]` line, a note, or the tree's `waits:`, and none of a line its `after` holds? |
| K10. `queue.sh` clearing a `[?]` a line's own branch inherited once main clears it | `kit-2026-11-14`: `queue.sh` (`4dc1a44`) | On a scratch worktree container, a line `[?]` on main when its branch is claimed, then cleared on main: does `queue.sh worktree` show it unblocked, read from main, from the line's worktree, and from the worktree of a branch still where the claim created it, as the changelog's three readings? Does a `[?]` the branch itself put still block? |
| K11. `queue.sh` naming an `after` in its two error lines | `kit-2026-11-14`: `queue.sh` :376 to :377 | On a scratch queue with a line naming itself in its `after` and one naming a slug not in the queue, does the script print "names itself in its after" and "names <slug> in its after, which is not in the queue", with no "waits on"? |

The kit's changelog, `## 2026.11.14` in `CHANGELOG.md` and `CHANGELOG.pt.md` of the kit's repository, is the source the clauses and the 2026-11-14 gap are checked against.

**Base.** `8d5d063` (`docs(ch14-queue-every-milestone): the tree draws every open milestone`), the end named by the page of m39-review, the last review that ran (`work/done/m39-review.md`, Outcome, "End `8d5d063`"), docs/05 §8's first case as 2026.11.14 words it. The range holds `b3afef0` (m39-review's own commit, its page), `4130e9e` (`m39-fixes`), `ced5c8a` (the release, `VERSION`), `6a91138` (docs/06, M40), `4dc1a44` and `d26ccc7` (`kit-2026-11-14`), `cf628af` (`ch15-base-last-end`) and `cd5612d` (`ch12-pages-on-branches`), eight commits.

**End.** The commit HEAD is when the reading starts, recorded before any reader; `cd5612d` while this page is written. This page and its mark, uncommitted, are read from the working tree as the spec.

**Areas.** From `git diff --stat -M 8d5d063..cd5612d`, 37 paths, each in an area of docs/05 §5's Milestone review slot:

* **The build** (1): `VERSION`, the release's.
* **The kit's skills** (14): `.agents/skills/` and `.claude/skills/`, each `analyze/SKILL.md`, `analyze/references/documents.md`, `apply/SKILL.md`, `brainstorm/SKILL.md`, `brainstorm/references/documents.md`, `propose/SKILL.md`, `propose/scripts/queue.sh`, all `4dc1a44`'s.
* **Chapters** (12): `book/{en,pt}/` 8, 14 and 21 (`m39-fixes`), 12 and 19 (`m39-fixes`, `ch12-pages-on-branches`), 15 (`ch15-base-last-end`).
* **The documents** (10): `docs/03-Domain.md`, `docs/05-Process.md`, `docs/06-Queue.md`, `docs/adr/ADR-0018-six-marks.md`, `work/kit-proposals.md`, and under `work/done/` `m39-review.md`, `m39-fixes.md`, `kit-2026-11-14.md`, `ch15-base-last-end.md`, `ch12-pages-on-branches.md`.

**Readers.** Four read-only readers on Opus, then one read-only checker on Opus alone; each launch sets its model to Opus, runs in the foreground and keeps the session's advisor, at most two at a time (docs/05 §5):

* pair 1: **chapters 12, 15 and 19** (`ch15-base-last-end`, `ch12-pages-on-branches`, `m39-fixes`' hunks of 12 and 19), both editions, whole at the end commit and by their range diffs, against the pages, the installed `propose/SKILL.md`, docs/05 §§4 and 8 and the kit's changelog; and **chapters 8, 14 and 21 with the build** (`m39-fixes` whole, its five items against m39-review's medium findings; `VERSION` against `docs/manuals/release-the-book.md`), with chapters 11 and 13 by grep for the note `m39-fixes` left;
* pair 2: **the kit's skills**, both folders by the range diff and whole where changed, against `SETUP.md` at `c6203d6` and its changelog, `queue.sh` run on scratch containers for K10 and K11; and **the documents and records**, docs/03, docs/05, docs/06, ADR-0018, `work/kit-proposals.md` and the five records, against each other, the chapters they describe, docs/04, the template in `SETUP.md` at `c6203d6` and the changelog, the range's commit messages against the pages' `commit` blocks;
* then the checker, on every candidate, every copied note and every lead in one report.

Each reader lists the paths it read and how (whole, diff, grep, image, run), and says whether it kept the advisor.

**Notes to copy**, as they stand at the end commit: `work/done/m39-fixes.md`, one (chapters 11, 13 and 15 telling a line held by `after` as waiting); `m39-review.md`, `kit-2026-11-14.md`, `ch15-base-last-end.md` and `ch12-pages-on-branches.md` have none.

**Slow tests.** None (docs/05 §5's Verify slot).

**Known leads**, given to the checker with the readers' candidates:

* L1, m39-review's five medium findings, read as fixed at the end commit in both editions: `due-date-format`'s one story across chapters 11, 13 and 14; "every open milestone's lines" in chapters 8 and 12; no sentence of chapters 12, 14 and 19 saying a line held by `after` waits; the en PDF keeping chapter 14's `grep -nE` command whole; chapter 21's opening against its key point.
* L2, a line held by `after` told as waiting in chapters `m39-fixes` did not touch: chapter 11 :89, :90 (the tree "each line under the last line it waits on", docs/05 §4's sentence 2026.11.14 reworded to "comes after") and :95; chapter 13 :50, :80 and :223; chapter 14 :105 and :176; chapter 15 :165 ("waiting for `/propose`", docs/05 §8's sentence 2026.11.14 reworded to "go through") and :183; with their pt twins; `m39-fixes`' note; graded as m39-review graded its M3.
* L3, chapter 12 :27's "since the main branch's `work/` lacks every page not yet merged" without the page's C1 words "with a branch or a worktree per delivery": whether its Outcome records the change, the pt twin, and whether the sentence reads true on trunk (its B2).
* L4, the `kit-2026-11-14` record: "only 3.1 to 3.5 and 3.7 changed between the two versions", "entries 9 to 13 and 15", its two `commit` blocks and the two commits' subjects against docs/05 §6's form.
* L5, every phrase 2026.11.14 displaced, from the diff of `SETUP.md` `fdc845c..c6203d6`, searched in both editions of `book/`.
* L6, the range gap: m39-review's end `8d5d063` against its commit `b3afef0`, and this review's end against the commits that land before its own.

**Mechanical checks**, run by /apply at the end commit:

* The installed skills, in `.agents/skills/` and `.claude/skills/`, byte-equal to the blocks of `SETUP.md` §§3.1 to 3.8 at `c6203d6` (the four `SKILL.md`, both `references/documents.md`, `claim.sh`, `queue.sh`, `mark.sh`); the two folders differing only by each `.agents/skills/<skill>/agents/`.
* docs/05 §§4 and 8 against the template's docs/05 in that `SETUP.md`; ADR-0018 :118 holds the amendment.
* `queue.sh` on scratch repositories for K10 and K11; `mark.sh` on a scratch queue for K8.
* `book/` in both editions searched for the phrases 2026.11.14 displaced (L5) and for "wait" said of a line its `after` holds (L2).
* The PDF pages of K3 to K8's passages in both editions found with `pdftotext` and rendered to images with `pdftoppm` into the session's scratchpad.
* The disclosure scan, `make scan`.
* The repository's tree: `queue.sh trunk` prints M40 with `m40-review` in flight and every other line `[x]`.
* `make verify` after the last edit, with its time against the five-minute ceiling.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs built at the end commit, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Out of scope.**

* Fixing any finding: grave ones become lines, medium ones the `m40-fixes` line (docs/05 §8).
* Re-testing M39's clauses: its fix line is read by the area readers, not tested by clause.
* A change to the kit's own files or wording: a note in `work/kit-proposals.md`, never an edit here.
* `make book`: the driver built both PDFs at the end commit, and this review reads them.

**Decisions from the documents.**

* The base is the end m39-review's page names, `8d5d063` (docs/05 §8 at 2026.11.14), not its commit `b3afef0`.
* A reader for each area the range touches (docs/05 §8); the chapters split in two, since six chapters in two editions are too large for one careful reading; the build's one path, `VERSION`, goes with the chapters reader of `m39-fixes`.
* The clause tests and the confirmation are taken on the author's word quoted below (docs/05 §8); the medium pick on the same word.
* The notes are copied from every page the range delivered, the checker marking each (docs/05 §8).

**The author's word for this review.** Relayed to this session by the driver session on 2026-11-14: "Vamos rodá-la de ponta a ponta automaticamente, sem pausas para concluir o milestone" (run M40 end to end without pauses), and, asked about medium findings, "Corrigir em m40-fixes" (fix them in m40-fixes). By it, the review's session answers each clause test from its own reading of the passages in both PDFs and of the repository, the word confirms each candidate the checker marks seen, and every medium finding enters the one `m40-fixes` line (docs/05 §8). Those answers are recorded as the review's, never the author's.

**Decisions taken alone.** The agent chose each of these, for the author's review.

* M40's paragraph is taken as eleven clauses, by what can be checked: the book teaches 2026.11.14, the repository runs on it, the base, a delivery committed while a review reads, the base after a dropped review, the slot that says none, the pages on branches, the resumed mark, the kit's `after` wording, the inherited `[?]`, and the two error lines.
* K9 to K11 have no chapter: the book does not teach `queue.sh`'s error lines, and chapter 19 already tells the copy that put a `[?]`; they are tested on the repository and scratch runs.
* The chapters area splits in two by delivery: the three chapters M40's lines changed together, and `m39-fixes`' three others with the release's `VERSION`.
* The readers run the kit's scripts only on scratch repositories in the session's scratchpad, since `claim.sh` pushes to origin.

**Done when.**

* [x] Every line above this review in M40 is `[x]` and committed; every clause has the review's answer, on the author's word quoted on this page.
* [x] Base, end, the inventory by area, each reader's paths read and its advisor, every copied note and candidate with its mark are on this page.
* [x] Every confirmed finding graded; each grave one a `[ ]` line under this review; every medium one an item of the `m40-fixes` line, when any; small ones listed, numbered.
* [x] The mechanical checks recorded; `make verify` green after the last edit, with its time.
* [x] The page in `work/done/` and its commit message suggested.

## Outcome

This review was built by the agent before the author read it, on the author's word quoted below; the author reads the page and the diff at the end (docs/05 §4).

**Precondition and range, recorded before any reader.** Every line above this review in M40 is `[x]` and committed: `kit-2026-11-14` (`4dc1a44`, `d26ccc7`), `ch15-base-last-end` `cf628af`, `ch12-pages-on-branches` `cd5612d`; M39's finding line `m39-fixes` `4130e9e`. Base `8d5d063`, the end m39-review's page names. End `cd5612d` (`docs(ch12-pages-on-branches): /propose reads pages on their branch`), HEAD when the reading started. The range holds eight commits: `b3afef0`, `4130e9e`, `ced5c8a` (`VERSION` only), `6a91138` (docs/06 only), `4dc1a44`, `d26ccc7`, `cf628af`, `cd5612d`. This page and its mark are uncommitted and outside the range. Both PDFs were built by the driver at `cd5612d` (en 273 pages, pt 284), and this review read them as they are, with no `make book`.

**Inventory.** `git diff --stat -M 8d5d063..cd5612d`: 37 paths, by area, each with its reader, as the page expected; no area appeared that it did not name.

* Build (1), reader 2: `VERSION`.
* The kit's skills (14), reader 3, and this session for the byte equality.
* Chapters (12): `book/{en,pt}/` 12, 15 and 19, reader 1; 8, 14 and 21, reader 2 (12 and 19 also by their `m39-fixes` hunks).
* The documents (10), reader 4.

**Slow tests.** None (docs/05 §5's Verify slot).

**Mechanical checks**, at `cd5612d`:

* The installed skills, in `.agents/skills/` and `.claude/skills/`, byte-equal (`cmp`) to the blocks of `SETUP.md` §§3.1 to 3.8 at `c6203d6` (the four `SKILL.md`, both `references/documents.md`, `claim.sh`, `queue.sh`, `mark.sh`), by this session; `diff -rq` of the two folders shows only each `.agents/skills/<skill>/agents/`.
* docs/05 §8 against the template's §8 at `c6203d6`, sentence by sentence, by this session: the base ("the end named by the page of the last review that ran, the commit its reading started at, not that review's own commit") and the slot that says none are equal; the rest is the project's own wording and its own paragraphs (the author's word, M3 and M4). docs/05 §§4 and 6 against the template (reader 4): every 2026.11.14 sentence present, none of §4 or §5 telling a line held by `after` as waiting. ADR-0018 :118 holds "## Amendment, 2026-11-14 (kit-2026-11-14)".
* `queue.sh` on scratch repositories (reader 3): K10's inherited `[?]` from main, from the line's worktree and from another branch's untouched worktree, and a `[?]` the branch put still blocking; K11's two error lines; the script at `8d5d063` showing the old behaviour for both. `mark.sh` refusing a second `[~]`, exit 2 (K8). Chapter 14's every-milestone tree rebuilt and byte-equal en and pt (reader 2).
* `book/` in both editions searched for the phrases 2026.11.14 displaced (the diff of `SETUP.md` `fdc845c..c6203d6`), by this session: "previous milestone's review", "no earlier review exists", "in flight in `work/`", "left to wait on" and their pt twins, none; "waiting for `/propose`" in chapter 15 :165 / :169 only (candidate R1-2). "Wait" said of a line its `after` holds: candidates R2-1, R2-2, R2-3, R2-4.
* PDF pages, found with `pdftotext -layout` and opened as images (`pdftoppm`) by this session: en p. 179, pt p. 186; by text en p. 121, 122, 177, 178, 183, 185, 186, 187, 233 / pt p. 126, 185, 186, 190, 193, 194, 195, 243.
* The disclosure scan, `make scan`, exit 0.
* The repository's tree, `queue.sh trunk`, exit 0, `git status --porcelain` the same before and after: `milestone: M40. focus-kit 2026.11.14`, `[*] m40-review · in flight: apply`, both free lists `none`, `next: none`.

**The author's word for this review.** Relayed to this session by the driver session on 2026-11-14: "Vamos rodá-la de ponta a ponta automaticamente, sem pausas para concluir o milestone" (run M40 end to end without pauses), and, asked about medium findings, "Corrigir em m40-fixes" (fix them in m40-fixes). By it, the clause answers below are the review's, from its own reading of both PDFs and of the repository at `cd5612d`, never the author's; each candidate the checker marks seen is confirmed, the latent and weak ones listed as dropped; every medium finding enters `m40-fixes`.

**The clause answers, the review's.** PDF pages en / pt, counted from each PDF's first page; source lines en / pt at `cd5612d`.

* **K1, the book teaches focus-kit 2026.11.14: holds, with medium findings 1 and 2.** Chapter 15 (p. 177 to 187 / 184 to 195), chapter 12 :27 to :32 (p. 121 to 122 / 126) and chapter 19 :360 (p. 233 / 243) teach what 2026.11.14 changed as the installed skills and docs/05 have it, with no "no longer" of the kit, and the editions say the same. No chapter keeps a displaced phrase of `propose/SKILL.md`; but chapter 15 :165 / :169 keeps docs/05 §8's displaced "waiting for /propose", and chapters 11 and 13, which no M40 line touched, still tell a line held by `after` as waiting in the sentences 2026.11.14 reworded (medium 1), and chapter 12 :27's new reason reads false on trunk (medium 2).
* **K2, and the repository runs on it: holds, with small findings 9 to 15.** The installed skills equal the kit at `c6203d6`; docs/05 holds the template's 2026.11.14 text; ADR-0018 :118 the amendment; `work/kit-proposals.md` entries 9 to 13 and 15 under "Taken to focus-kit 2026.11.14"; `queue.sh` prints M40 with every line in it.
* **K3, the base, the end the last review's page names: holds.** Chapter 15 :23 (p. 178 / 185), "the end named by the page of the last review that ran, the commit that review's reading started at and not that review's own commit", :191 (p. 186 / 194) and key point :217 (p. 187 / 195) say it as docs/05 §8 :466 to :470 does; this review's own base is `8d5d063`, m39-review's recorded end, not its commit `b3afef0`.
* **K4, a delivery committed while a review reads falling in the next range: holds.** Chapter 15 :25 to :27 (p. 179 / 186) says what the range holds, where such a delivery falls, and the error a base at the review's own commit would make, dated 2026-11-14 as a note of this book, with no project or version named. The en "up to the review's own end" is small 5.
* **K5, also after a dropped review: holds.** Chapter 15 :28 (p. 179 / 186): with `m2-review` cancelled, `m3-review` names as its base the end `m1-review`'s page names; :23 says "where no earlier review ran".
* **K6, the slot that says none: holds.** docs/05 §8 :492 to :494 equals the template; chapter 15 :114 (p. 183 / 190) says the page still names the range, its end `<review-head>`, and the hand test still runs; docs/03 :34's milestone review row agrees ("says none reads no code, its page still naming the range and the person still testing each clause"), by this session.
* **K7, `/propose` reading the page of each delivery in flight in `work/` or on its own branch: holds, with medium finding 2.** Chapter 12 :27 (p. 121 / 126) and chapter 19 :360 (p. 233 / 243) say it as `propose/SKILL.md` :19 to :20 does; chapter 12's added reason is medium 2.
* **K8, a resumed `/propose` keeping its line's mark: holds.** `propose/SKILL.md` :29 to :30; chapter 12 :31 to :32 (p. 122 / 126) says the first edit marks the `[ ]` line `[~]` and a resumed line keeps its `[~]`; `mark.sh` refuses a second `[~]`.
* **K9, no sentence of the kit telling a line held by `after` as waiting: holds, with small finding 9.** Reader 3 classed every "wait" in the installed kit files and docs/05 §§4, 5 and 8: each is said of a `[?]` line, a note, a command, a built line awaiting integration, or the tree's `waits:`; none of a line its `after` holds. The tree's word is named by the changelog, not by docs/05 (small 9).
* **K10, `queue.sh` clearing an inherited `[?]`: holds.** Reproduced from main, from the line's worktree and from a branch still where its claim created it; a `[?]` the branch put still blocks; the script at `8d5d063` showed the old `[?]`.
* **K11, `queue.sh` naming an `after` in its two error lines: holds.** "alpha names itself in its after" and "beta names ghost in its after, which is not in the queue"; the old script said "waits on". Both exit 0 on trunk, as before.

**Readers.** Four read-only readers on Opus, two at a time (readers 1 and 2; reader 3 once reader 1 ended; reader 4 once reader 3 ended, reader 2 still running), then the checker on Opus alone; at most two ran at once. Each was launched from this session with its model set to Opus and asked for the foreground; the host ran them in the background, and each final report reached this session as its completion notice. Scratch work in the session's scratchpad, `m40/`.

* **Reader 1, chapters 12, 15 and 19.** Chapter 15 en whole and by diff, pt by diff and grep; chapters 12 and 19 en and pt by diff, the changed sections and grep (not whole); both M40 chapter records whole; `m39-fixes.md` by grep; `propose/SKILL.md` whole; docs/05 §§4 and 8; docs/03 and docs/04 in part; docs/06 M40; chapter 14 by grep; the changelog; PDF images en p. 121, 179, 186 / pt p. 126, 186, 190, the rest by text. Advisor kept, called once.
* **Reader 2, chapters 8, 14 and 21, `m39-fixes` and the build.** `m39-fixes.md` whole; `git show 4130e9e` by word diff; chapter 14 en whole, pt :1 to :203 directly and the rest by diff and grep; chapters 8 and 21 en whole, pt by diff and parts; chapters 11, 12, 13, 15 and 19 by grep and lines; docs/05 in part; `queue.sh` run on two scratch repositories; `VERSION`, `git show ced5c8a`, the tag and `release-the-book.md` whole; PDF images en p. 158, 245 / pt p. 164, 255. Advisor kept, called once.
* **Reader 3, the kit's skills.** The range diff of the seven changed files; `propose/SKILL.md`, `apply/SKILL.md` and `queue.sh` whole; `documents.md` by diff and grep; `queue.sh` at `8d5d063` run; `claim.sh` and `mark.sh` read whole and run on scratch containers; the `.claude/` copies by this session's byte equality; docs/05 §§4 and 8 whole, §5's slots; chapters 12, 13, 14 and 19 by grep; the changelog. Advisor kept, called once.
* **Reader 4, the documents and records.** The five records whole; docs/05 by diff and §§4, 6 and 8 whole against the template at `c6203d6`; `SETUP.md` `fdc845c..c6203d6` by section; docs/03, docs/06, ADR-0018 and `work/kit-proposals.md` by diff and in part; the eight commit messages against the pages' `commit` blocks (all equal); chapters by line and grep. Advisor kept, called once.
* **The checker**, one agent on every candidate, the note and the leads in one report, each file opened at `cd5612d`, the PDFs by text: 34 candidates, the note and two leads (L1, L6) marked, each mark in the table below; this session split R1-2 into S2, seen, and joined leads L2 to L5 to the rows they repeat. Advisor kept, called once.

Every path of the inventory was read by at least one reader. The partial reads are accepted: chapters 12 and 19 and the pt editions outside the range's hunks by the diff, the sections and grep; the `.claude/` copies of the skills by byte equality; so no `[?]` was needed.

**Notes copied**, verbatim from the `## For the review` headings of the range's pages at `cd5612d`; `m39-review.md`, `kit-2026-11-14.md`, `ch15-base-last-end.md` and `ch12-pages-on-branches.md` have none, and `ced5c8a` and `6a91138` have no page:

* N1, `work/done/m39-fixes.md`: "`book/en/13-apply.md:223` ("`m1-review`, written `· after all`, waits until `return-book` is defined."), `:50` and `:80` ("what it waits on" for a `[>]` line its `after` holds), `book/en/11-queue-and-milestones.md:90` ("each line under the last line it waits on") and `:95` (the review "waits for the lines above it"), `book/en/15-closing-a-milestone.md:3` ("never keeps it waiting"), `:26` ("does not wait for the review") and `:181` ("As a line it waits its turn"), with their pt twins ("espera"): the wording M3 removes from chapters 12, 14 and 19, found by this /propose's grep; a reader of those chapters meets a line held by `after` told as waiting beside chapter 13 :77's "It is not waiting". Not grave: no sentence puts a `[?]` on a line for another line. The person may apply M3's rule to them in a later delivery."

**Candidates.** The checker's marks, lines at `cd5612d`, en / pt; `=` joins one claim, graded once. R1 to R4 are the readers', S1 this session's.

| Id | Where | Claim | Mark |
|---|---|---|---|
| R2-1 = R2-2 = R3-1 = R4-1 (ch11, ch13) = N1 (ch11, ch13) | ch11 :90, :95, :181 / :93, :98, :186; ch13 :50, :80, :223 / same | A line held by `after` told as waiting, in the sentences 2026.11.14 reworded ("the last line it waits on", "what it waits on") | seen |
| R1-1 | ch12 :27 / :27 | "since the main branch's `work/` lacks every page not yet merged" false on trunk | seen |
| R2-4 | ch14 :387 / :389 | "keeps no review waiting", the kit half of a Case A sentence | seen |
| R2-8 | ch21 :89 / :89 | Case B's "each finding needed a line" against the opening and key point | seen |
| R1-5 | ch12 :27, ch19 :360; ch19 :229, :363 | "on its own branch" while a page in flight is uncommitted in its folder by default | seen |
| R1-6 | ch15 en :25 | "the review's own end" beside "that review's own commit" | seen, en only |
| R1-7 | pt ch15 :3, :18; pt ch14 :347 | "prende" / "presa" against "segura" for one en phrase | seen |
| R1-8 = R4-3 | docs/03 :121; :124 | A line held by `after` told as waiting in two rows | :121 seen; :124 weak, the tree's word |
| R1-4 | ch12 :3 to :6, :196 to :201 / :205 to :210 | Four-sentence opening, six key points | seen; m39-review small 8 |
| R2-5 | ch14 :399 / :401 | Key point 3 drops "pending" from the body's "last pending line" | seen |
| R2-6 | ch14 :55 / :56 | "(below)" right above the `grep -nE` block | seen |
| R2-7 | ch21 :4; pt p. 255 | `/apply` broken after the slash in the pt PDF | seen |
| R2-9 | ch12 :158 / :167; docs/05 :261 | Tested at the batch's start, where docs/05 tests at the others' end | seen |
| R3-2 | `queue.sh` :219 | `waits:` for a line held by `after`, a word docs/05 does not name | seen; the kit's |
| R3-4 | `documents.md` :406 | "a line its `after` still holds" lacks "whose" | seen; the kit's |
| R4-4 | ADR-0018 :119 | Cites docs/05 and docs/03 for the error-line change neither states | seen, half |
| R4-5 | `kit-2026-11-14.md` :19 to :29; `4dc1a44`, `d26ccc7` | Two `commit` blocks without docs/05 §6's form | seen |
| R4-6 | `ch15-base-last-end.md` :77; `cf628af` | The page path as a fifth bullet, not a last line | seen |
| R4-7 | `ch12-pages-on-branches.md` :5, :41, :55 to :58 | C1 and C2 ticked as their end state beside recorded departures | seen |
| R4-8 | `ch15-base-last-end.md` :16 | Names five pt words as docs/03 terms; one is | seen |
| R4-9 | `work/kit-proposals.md` :22 | Entry 11, taken, still states the rule 2026.11.14 did not take | seen |
| R4-10 | `work/kit-proposals.md` :32 | Entry 14 kept whole though its first ask is in `queue.sh` | seen |
| R4-11 | `m39-fixes.md` :174 to :178 | Lines at `4130e9e` beside a Contract at `b3afef0`, unsaid | seen |
| S1 | en p. 179, 186; pt p. 190, 194, 195 | Code spans broken at their hyphen (`m3-review`, `<review-head>`, `<head-da-revisao>`) | seen, by this session; pt p. 186 weak |
| S2 (from R1-2) | ch15 :165 / :169 | "waiting for `/propose`" / "esperando o `/propose`", docs/05 §8's sentence 2026.11.14 reworded to "go through /propose" (:523; `kit-2026-11-14.md` :7) | seen, by this session: the displaced phrase, whatever the lines' suffix |
| R1-2 = R4-2 = R4-1 (ch15) = N1 (ch15 :181) | ch15 :183 / :187 | Finding lines "waits its turn", told as held by `after` | weak: they end `· from`, not `· after` (docs/05 :522), and the turn is the queue's order |
| R1-3 | ch12 :197 / :206 | `/propose` "waits until" | weak: a command, kept by `m39-fixes` |
| R2-3 | ch14 :105, :108, :176, :177; ch11 :89 | A command's or build's "waits until" | weak: a command or build |
| R3-3 | `propose/SKILL.md` :29 to :30 | A resumed claim whose branch copy is `[ ]` | latent; the kit's |
| R3-5 | `queue.sh` :26, :331 to :335 | `blocked: after <slug>` still honoured | latent; the kit's, no line uses it |
| N1 (ch15 :3, :26) | ch15 :3, :26 | Reworded by `ch15-base-last-end` | holds no more |
| L2 | ch11, ch13, ch14, ch15 | A line held by `after` told as waiting | = R2-1 (seen), S2 (seen), R1-2 and R2-3 (weak), R2-4 (seen) |
| L3 | ch12 :27 | The cut of C1's condition | = R1-1 (seen), R4-7 (seen) |
| L4 | `kit-2026-11-14.md` | Its claims and its `commit` blocks | "only 3.1 to 3.5 and 3.7" and "entries 9 to 13 and 15" hold (reader 4); the blocks = R4-5 (seen) |
| L5 | `book/` | The phrases 2026.11.14 displaced | = S2: chapter 15 :165 / :169 only, by this session's grep |
| L1 | m39-review's M1 to M5 | Read as fixed | fixed: M1 by reader 2's byte-equal tree and grep, M2 to M5 by reader 2 and the checker |
| L6 | `8d5d063`..`b3afef0` | The range gap | holds: `b3afef0`'s parent is `8d5d063` |

**Findings.** By the author's word, every candidate and note marked seen is confirmed; the weak and latent ones are dropped and listed under small (docs/05 §8). No candidate is held by an open line: M40 has none but this review.

*Grave*: none. Every clause holds for a person on its usual path, nothing loses or exposes data, verify is green, and no delivery in flight waits on a fix.

*Medium*, met in ordinary reading while the clauses hold, each an item of `m40-fixes` by the author's word:

1. M1, R2-1 = R2-2 = R3-1 = R4-1 = N1, and S2: chapter 15 :165 / :169 says the fixes lines sit under the review line "waiting for `/propose`" / "esperando o `/propose`", docs/05 §8's sentence 2026.11.14 reworded to "go through /propose" (:523); chapter 11 :90 / :93 ("each line under the last line it waits on", where docs/05 §4 :143 now says "comes after"), :95 / :98 (the review "waits for the lines above it") and :181 / :186 (a needed fix "makes it wait"), and chapter 13 :50, :80 (the stop "writes on the page what was built and what it waits on", where `apply/SKILL.md` :38 now says "what it needs") and :223 (`m1-review` "waits until `return-book` is defined"), pt the same with "espera": a line held by `after` told as waiting, in the sentences 2026.11.14 reworded, beside chapter 11 :88's "That is an order, not a wait" and chapter 13 :77's "It is not waiting". No M40 line touched chapters 11 and 13, `ch15-base-last-end` left :165 out of scope, and the `kit-2026-11-14` record named only 12, 15 and 19.
2. M2, R1-1: chapter 12 :27 / :27 gives as the reason `/propose` reads pages on branches "since the main branch's `work/` lacks every page not yet merged" / "já que o `work/` do branch principal não tem nenhuma página ainda sem merge", without the condition its page's C1 had, "with a branch or a worktree per delivery"; on trunk, where a reader of chapter 12 most often is, the pages in flight are in the main branch's `work/`. The cut is recorded in `ch12-pages-on-branches.md` :55 to :58.

*Small*, each a record's precision, a rare case, a wording few meet, a passage of a case or a dropped candidate:

3. R2-4: chapter 14 :387 / :389's "a line closed that way keeps no review waiting", the kit half of a Case A passage; the author decides (docs/00 OD-3).
4. R2-8: chapter 21 :89's Case B "each finding needed a line" against the opening :4 and key point :102; a Case B passage, the author's (OD-3).
5. R1-6: chapter 15 en :25's "up to the review's own end" beside "that review's own commit"; pt is clear.
6. R1-7: pt chapter 15 :3 and :18 "prende" / "presa" against pt chapter 14 :347 "segura" for the same "holds back".
7. R1-5: chapters 12 :27 and 19 :360 say "on its own branch", the skill's words, while chapter 19 :229 and :363 keep a page in flight uncommitted in its folder by default. The kit's wording: a note for `work/kit-proposals.md`.
8. R2-9: chapter 12 :158 / :167 tests the line at the batch's start where docs/05 :261 tests it when the others end.
9. R3-2: `queue.sh` :219's `waits:` for a line held by `after`, sanctioned by the changelog and ADR-0018 :119, unnamed in docs/05; the kit's.
10. R3-4: both `references/documents.md` :406 lack "whose"; the kit's.
11. R1-8 (:121): docs/03 :121's dependency row "waits for the person to re-decide it", where docs/05 :212 says "is the person's to re-decide".
12. R4-4: ADR-0018 :119 cites docs/05 and docs/03 for the error-line change neither states.
13. R4-5: `kit-2026-11-14.md` :19 to :29's two `commit` blocks and its two commits without docs/05 §6's form, as `kit-2026-11-13` and `kit-2026-11-12` before it.
14. R4-9 and R4-10: `work/kit-proposals.md` entry 11 (:22), taken, still states the rule 2026.11.14 did not take; entry 14 (:32) kept whole though its first ask is in `queue.sh`.
15. Records' precision: R4-6 (`ch15-base-last-end.md` :77 and `cf628af`, the path as a bullet), R4-7 (`ch12-pages-on-branches.md` :41 ticks C1 and C2 beside recorded departures), R4-8 (`ch15-base-last-end.md` :16's docs/03 terms), R4-11 (`m39-fixes.md` :174 to :178's lines at an unsaid commit).
16. R1-4: chapter 12's four-sentence opening and six key points, m39-review's small 8, still open.
17. R2-5: chapter 14's key point 3 (:399 / :401) drops "pending".
18. R2-6: chapter 14 :55 / :56's "(below)" right above the `grep -nE` block.
19. R2-7 and S1: line breaks inside code spans in the PDFs: pt p. 255's `/apply` after the slash (chapter 21), and `m3-review`, `m1-review`, `<review-head>` (en p. 179, 186) and `<head-da-revisao>` (pt p. 190, 194, 195) at their hyphen (chapter 15).
20. Dropped, weak: R1-2 = R4-2 (chapter 15's finding lines, which end `· from`), R1-3, R2-3, R1-8 (:124); latent: R3-3, R3-5.

**The medium pick.** By the author's word quoted above, M1 and M2 enter the one `m40-fixes` line, each an item of its page, which is their list and is not split. No small finding is picked, so none becomes a line (docs/05 §8). The line sits under this review, `· after m40-review · from m40-review`; the driver adds it with the host's file edit on that one line. Small 7, 9 and 10, the kit's wording, and small 14, `work/kit-proposals.md` itself, are the driver's to note there.

**The range gap (L6).** m39-review's end `8d5d063` is the parent of its commit `b3afef0`, so nothing fell between, and this review's range holds m39-review's own page as the new base says. No commit landed after this review's end `cd5612d` while it ran (`git log cd5612d..HEAD` empty at the last check); any that lands before this page's commit is m41-review's to copy and read.

**Decisions taken alone in /apply.** For the author's review.

* M1 is medium, not grave, as m39-review graded its M3: no sentence puts a `[?]` on a line for another line, so K9 (the kit's sentences) holds; but the book teaches 2026.11.14 in sentences that keep its displaced wording, in chapters 11 and 13 a reader meets beside "not waiting".
* M2 is medium: the reason is false for a reader on trunk, the usual setup when chapter 12 is read, while K7's rule itself is right.
* The checker's weak mark on R1-2 is split: chapter 15 :165 keeps the very sentence 2026.11.14 reworded in docs/05 §8, so this session marks it seen (S2) and joins it to M1; :183's "waits its turn" stays weak, since the finding lines end `· from`, and a command or a build that waits is the wording `m39-fixes` kept by rule.
* R2-4 and R2-8 are small because each sits in a Case A or Case B passage the author approves (docs/00 OD-3), not because a reader meets them less; the author may promote either into `m40-fixes`.
* The readers were asked for the foreground and ran in the background, the host's way; each report reached this session as its completion notice.
* No Delivery review of this page: a review reviews no review (docs/05 §7), as m39-review ran.
* PDF pages are counted from each PDF's first page.

**Proof.** The mechanical checks and the clause answers above; the PDFs built at `cd5612d`; `make verify` green after the last edit to this page and docs/06, 14 to 47 seconds a run, under the five-minute ceiling.

The driver session commits this delivery with the message below, and never pushes.

```commit
docs(m40-review): review M40, eleven clauses hold, two medium fixes

- Base 8d5d063, m39-review's recorded end; end cd5612d
- Installed skills equal to the kit 2026.11.14; queue.sh fixes reproduced
- Four readers and a checker: 34 candidates, 1 note, 6 leads marked
- m40-fixes: after wording in chapters 11, 13, 15; chapter 12's reason

work/done/m40-review.md
```
