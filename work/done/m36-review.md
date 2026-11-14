# m36-review

**Objective.** The author can decide whether M36's promise holds, the clauses of its paragraph tested in the PDF of both editions and on this repository, and whether everything changed since m35-review's commit holds under the code reading by areas, with every confirmed finding graded: each grave one a line under this review, the medium ones in the one `m36-fixes` line, the small ones listed here.

This page was defined by the agent before the author read it, on the author's word for this run, relayed by the driver session on 2026-11-13: "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão" (close every open line of docs/06 without supervision). Every question the documents leave open is answered by the agent's recommendation, written below as the agent's choice; the author reads the page and the diff at the end (docs/05 §4).

**Behaviour.**

* With every line above this review in M36 `[x]` and committed, and M35's finding line `m35-fixes` committed, /apply records the base and the end commit, builds both PDFs at the end commit with `book/` clean, and answers each clause test below: holds, or fails with what was seen. A clause no delivery answers, or one that fails, is a finding (docs/05 §8).
* The review opens by copying onto this page, verbatim, the notes under `## For the review` of every page the range delivered, naming the pages that have none (`ch14-15-after-all-dropped` has none today; `m35-fixes` is read once committed); the checker marks each note as it marks a candidate (docs/05 §8).
* Read-only readers on Opus read one fixed range, `git diff <base>..<end>`, one per area the range touches, at most two running at a time; one checker on Opus then marks every candidate and every note seen, latent or weak against the end commit (docs/05 §5, Milestone review). Every launch sets its model to Opus, runs in the foreground so its report reaches this session, and keeps the session's advisor.
* On the author's word, quoted below, the review's session takes the clause tests from its own reading of both PDFs and of the repository, and the word is the confirmation of each candidate the checker marks seen; the latent and weak ones are listed as dropped. These answers are the review's, never the author's (docs/05 §8).
* Every confirmed finding is graded by docs/05 §4 and §8: grave, when it breaks a clause of M36's paragraph for a person on its usual path, loses or exposes data, or leaves verify red, each its own `[ ]` line under this review ending `· after m36-review · from m36-review`; medium, met in ordinary use while the clause holds; small, a rare case, a latent or weak candidate, a cost nobody measured.
* On the author's word for the medium pick, every medium finding enters the one `m36-fixes` line, each an item of its page, ending `· after m36-review · from m36-review`; with no medium finding, no line. Small ones are listed on this page, numbered, and none becomes a line.
* A clause with no answer, a reader or checker whose report does not reach this session, or paths of the range no reader read leave this review waiting as `[?]` with `· resume: apply` and the reason (docs/05 §§4, 8).
* Edge, M35's fix line in the range: `m35-fixes` (chapters 11, 12 and 19, both editions) is built while this page is written and committed before /apply starts. Its paths are read by the area readers without a clause test and with no second review (docs/05 §8); its three items are given to the checker as a lead.
* Edge, later milestones: M37 to M39's chapter lines (`ch13-apply-next`, `ch13-apply-findings`, `ch14-queue-findings`, `ch15-review-grades`, `ch13-apply-after`, `ch14-after-never-waits`, `ch14-queue-every-milestone`, `ch14-open-lines-search`) are open. A candidate one of them already holds is listed with that line and is no finding here.
* Edge, a later milestone's delivery in the range: another session may commit an M37 to M39 delivery before the end commit (`ch13-apply-next` is `[>]` today). Its paths are read by the area readers without a clause test, its notes are copied here, since the range delivered its page, and the Outcome names it so that milestone's review knows its code was read here.
* Edge, the kit's own scripts: no path under `.claude/skills/` or `.agents/skills/` is in the range today; a candidate in one is graded as any other, and its fix, when it enters, is a note in `work/kit-proposals.md`.
* Edge, the error's project: chapter 14's error of 2026-10-26, the review that waited on a dropped line, is told as the kit's changelog words it, with no project named; by the author's word of 2026-11-13 ("Sim, como o changelog") it is no Case A or Case B passage, so docs/05 §5's Case A and Case B slot asks nothing of this review.
* Edge, the shared tree: readers and the checker read the end commit (`git diff <base>..<end>`, `git show <end>:<path>`), never the working tree or the index; a commit made during the reading does not move the end commit.

**Contract.** Clause tests from docs/06's M36 paragraph, each against its delivery's page in `work/done/` and the named passages, lines at `46d5166` en / pt with the sentence quoted, since lines drift; /apply finds their lines and PDF pages at the end commit. The clause ids below are this review's, not that page's C1 to C6.

| Clause | Deliveries and passages | The test |
|---|---|---|
| K1. The book teaches focus-kit 2026.10.27.1 | `ch14-15-after-all-dropped`: chapter 14 :5 / :5 (the opening, "nor keeps the milestone's review waiting"), :92 / :93, :222 to :229 / :224 to :231, the gain :269 / :271 and key point 2 :277 / :279; chapter 15 :3 / :3, :18 / :18 and key point 2 :167 / :170 | Do chapters 14 and 15 teach `after all` leaving out the cancelled lines as the installed `queue.sh` reads it, and does no other chapter tell `after all` otherwise (Mechanical checks)? Do the two editions say the same, in docs/03's Portuguese terms ("cancelada", "redecidir", "revisão de marco")? |
| K2. And the repository runs on it | `kit-2026-10-27-1` (committed in `33432ee`, before the base): docs/05 §4 :104 to :105, "every line above it in its milestone but the dropped ones", and :202, "`after all` names none and leaves it out"; §8 :438 to :440, "/propose writes its page when every line above but the dropped ones is defined"; the provenance paragraph :216 to :217, "`after all` leaving out the dropped lines is that of 2026.10.27.1"; ADR-0018 :102 to :104, amendment `kit-2026-10-27-1`; docs/03 :120's `dependency` row; the installed `queue.sh` :10 to :11, :128 and :145 | Do docs/05 §§4 and 8 hold the kit's three sentences, ADR-0018 its amendment, and docs/03's row the dropped lines left out? Does the installed `queue.sh` equal the kit's? |
| K3. `· after all` leaving out the milestone's dropped lines | `ch14-15-after-all-dropped`: chapter 14 :92 / :93, "every line above it in its milestone but the cancelled ones", :225 / :227, "So `after all` names no cancelled line", and key point 2; chapter 15 :18 / :18, "Its line ends `· after all`, every line above it in its milestone but the cancelled ones" | Do chapters 14 and 15 say that `after all` is every line above the review in its milestone but the cancelled ones, the `[x]` lines ending `· dropped:`, with the review's `/propose` starting when every one of those is defined and its `/apply` when every one is integrated? |
| K4. So a review never waits on a line the person cancelled | `ch14-15-after-all-dropped`: chapter 14 :222 to :227 / :224 to :229 (the reason and the error), the opening and the gain; chapter 15 :3 / :3 | Does chapter 14 give the reason in the present, a review being neither dropped nor rewritten on what exists, so nothing the person writes would clear it, with the review of 2026-10-26 that waited on a dropped line, `after <slug>, dropped: re-decide`, and its `after all` replaced by a list of the other 27 slugs as the error, told with no project named? Does `print-card`, cancelled, leave `m1-review` free in the chapter's example? |
| K5. While a line that names a dropped one still waits for the person to re-decide it | `ch14-15-after-all-dropped`: chapter 14 :220 / :222, "So a line whose `after` names a cancelled delivery is the person's to re-decide", :228 to :229 / :230 to :231 (`reprint-card`); chapter 15 :18 / :18, "a line whose `after` names a cancelled one waits for the person to re-decide it, and the review waits with it" | Does chapter 14 say `reprint-card` is counted by `after all`, the queue tree printing `waits: after print-card, dropped: re-decide`, and the review waiting with it until the person drops it too or rewrites it on what exists? Does chapter 15 say the same in one sentence, pointing to no second telling of the error? |

The kit's changelog, `## 2026.10.27.1` in `CHANGELOG.md` and `CHANGELOG.pt.md` of the kit's repository, is the source the error, its answer and its 27 slugs are checked against.

**Base.** `4a6c02d` (`docs(m35-review): review M35, four clauses hold, three medium fixes`), the commit of m35-review, the previous milestone's review (docs/05 §8), the one commit `git log --diff-filter=A -- work/done/m35-review.md` returns. The range therefore holds M35's one finding line, `m35-fixes`, once committed, read by the area readers without a clause and with no second review (docs/05 §8); `f526e4f` (`docs(queue): M39 gains ch14-open-lines-search, the open lines tip`), an edit of docs/06 with no page and no notes; and M36's chapter delivery, `ch14-15-after-all-dropped` (`46d5166`). `kit-2026-10-27-1` was committed before the base, in `33432ee`; K2 tests its result at the end commit.

**End.** The commit HEAD is when the reading starts, recorded before any reader; this page and its mark, uncommitted, are read from the working tree as the spec.

**Areas.** Expected from the range today and `m35-fixes`' page; /apply recomputes them from `git diff --stat -M <base>..<end>` at the end commit, places every path in an area of docs/05 §5's Milestone review slot, and adds a reader for any area that appears:

* **Build:** no path of the `Makefile`, `scripts/`, the READMEs, `VERSION` or `docs/manuals/`; no reader.
* **The kit's skills:** no path; no reader.
* **Chapters:** `book/{en,pt}/` 11, 12 and 19 (`m35-fixes`) and 14 and 15 (`ch14-15-after-all-dropped`), ten files, split in two readers.
* **The documents:** `docs/06`, and the two records under `work/done/` the range adds, `m35-fixes.md` and `ch14-15-after-all-dropped.md`, read with the chapters they describe, docs/03, docs/04 and docs/05.

**Readers.** Three read-only readers on Opus, then one read-only checker on Opus alone; each launch sets its model to Opus, runs in the foreground and keeps the session's advisor, at most two at a time (docs/05 §5):

* pair 1: **chapters 11, 12 and 19** (M35's finding line), and **chapters 14 and 15** (M36's delivery), both editions, whole at the end commit and by their range diffs, against their pages and the installed `queue.sh`;
* then **the documents and records**, against each other, the chapters they describe, docs/04 and the kit's changelog;
* then the checker, on every candidate, every copied note and every lead in one report.

Each reader lists the paths it read and how (whole, diff, grep), and says whether it kept the advisor.

**Slow tests.** None (docs/05 §5's Verify slot).

**Known leads**, given to the checker with the readers' candidates:

* L1, m35-review's three medium findings, read as fixed at the end commit in both editions: M1, chapter 11's grave finding against "only through a clause"; M2, chapter 19's free line read with `after` per command; M3, chapter 12's resumed `/propose` keeping its `[~]`.
* L2, chapter 11 :95 / pt :98's "`<milestone>-review · after all`, a delivery like the others, which waits for the lines above it": whether it tells `after all` otherwise than chapters 14 and 15, which leave the cancelled lines out.
* L3, `kit-2026-10-27-1.md`'s "Chapters 14 and 15 still teach the old reading", against `ch14-15-after-all-dropped`'s decision that chapter 14 :92 already held the rule since `ch11-14-after`.
* L4, `ch14-15-after-all-dropped`'s Behaviour failure ("should I replace `after all` with the list of the other slugs?"), which its delivery review kept as answered by inference from the contrast: whether chapter 14 answers it.
* L5, `ch14-15-after-all-dropped`'s divergence, "holds" made "keeps ... waiting" (pt "faz ... esperar") in six places: each place in both editions, and no "holds the review" left.

**Mechanical checks**, run by /apply at the end commit:

* The installed `queue.sh` in both skills folders equals the kit's `SETUP.md` §3.7 (`propose/scripts/queue.sh`) at `4f5da97`, focus-kit 2026.11.12, the version the repository runs (`kit-2026-11-13` is still open).
* docs/05 §4 :104 to :105 and :202, and §8 :438 to :440, word for word the kit's `SETUP.md` at `4f5da97` (:831, :927, :1080).
* The installed `queue.sh` run on a scratch repository with chapter 14's example as one milestone: `print-card` `[x] · dropped:`, `reprint-card ... · after print-card` `[ ]`, the other lines `[>]`, and `m1-review · after all`; the tree prints `reprint-card` with `waits: after print-card, dropped: re-decide` and `m1-review` not free; with `reprint-card` dropped too, `m1-review` free for `/propose`; against chapter 14 :226 to :229 / :228 to :231.
* `book/` in both editions searched for a passage that tells `after all` otherwise than chapters 14 and 15 (today chapter 9 :23 and :110, chapter 11 :95 / pt :98, chapter 13 :177, chapter 19 :218).
* The disclosure scan at the end commit, and chapter 14's error checked against the changelog's wording: no project, place or business detail.
* The repository's tree: `queue.sh trunk` prints M36 with `m36-review` in flight, `git status` the same before and after.
* `make book` with `book/` clean; `make verify` after the last edit.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs, `make book` at the end commit.

**Out of scope.**

* Fixing any finding: grave ones become lines, medium ones the `m36-fixes` line (docs/05 §8).
* Re-testing M35's clauses: its fix line is read by the area readers, not tested by clause.
* Teaching 2026.11.03 to 2026.11.13 in the chapters: M37 to M39's lines.
* The kit's test fixture (`tooltips` above `m2-review`): the kit's own test, nothing a reader of the book runs, as `ch14-15-after-all-dropped` leaves it out.

**Decisions from the documents.**

* The base is m35-review's commit, `4a6c02d`, the first of docs/05 §8's cases.
* No build reader and no kit reader: the range is expected to touch neither (docs/05 §8, one reader per area it touches); /apply adds one if the inventory shows otherwise.
* The clause tests, the confirmation and the medium pick are taken on the author's word quoted below (docs/05 §8).
* The notes are copied from every page the range delivered (docs/05 §8).
* The queue script and docs/05's sentences are compared with the kit at `4f5da97`, the version the repository runs, not the kit's newest (docs/05 §4's provenance paragraph ends at 2026.11.12).

**The author's word for this review.** Relayed to this session by the driver session on 2026-11-13: "Todas, médios entram": every milestone review `m35-review` to `m39-review` runs; its session takes the clause tests from its own reading of both PDFs and confirms every candidate the checker marks seen (docs/05 §8); every medium finding enters the one `m36-fixes` line; small ones stay listed on the page and none becomes a line. And, for the dated errors: "Sim, como o changelog": they are told as the kit's changelog words them, with no project named, no place and no business detail, none a Case A or Case B passage.

**Decisions taken alone.** The agent chose each of these, for the author's review.

* M36's paragraph is taken as five clauses, by what can be checked: the book teaches 2026.10.27.1, the repository runs on it, the rule itself, what it prevents, and the line naming a dropped one that still waits.
* The chapters area splits in two, by milestone, as m35-review did: M35's fix in chapters 11, 12 and 19, M36's delivery in 14 and 15 (docs/05 §8, an area too large for one careful reading).
* The chapter passages are named by line at `46d5166`, with the sentence quoted, since `m35-fixes` touches neither chapter 14 nor 15; /apply finds the lines and pages at the end commit.
* The queue script is run on chapter 14's own example, so the test checks the chapter's claim and not only the script.
* A later milestone's delivery committed inside the range is read here without a clause and named in the Outcome, so its own review knows.
* A candidate an open M37 to M39 line holds is listed with that line, as m35-review did.

**Done when.**

* [x] Every line above this review in M36 is `[x]` and committed, and `m35-fixes` committed; every clause has the review's answer, on the author's word quoted on this page.
* [x] Base, end, the inventory by area, each reader's paths read and its advisor, every copied note and candidate with its mark are on this page.
* [x] Every confirmed finding graded; each grave one a `[ ]` line under this review; every medium one an item of the `m36-fixes` line, when any; small ones listed, numbered.
* [x] The mechanical checks recorded; `make book` built both PDFs at the end commit; `make verify` green after the last edit, with its time.
* [x] The page in `work/done/`, its paths staged and its commit message suggested.

## Outcome

This review was built by the agent before the author read it, on the author's word quoted below; the author reads the page and the diff at the end (docs/05 §4).

**Precondition.** Every line above this review in M36 is `[x]` and committed: `kit-2026-10-27-1` before the base (`33432ee`), `ch14-15-after-all-dropped` `46d5166`; M35's finding line `m35-fixes` `4ee7736`. `git log --diff-filter=A -- work/done/m35-review.md` returns `4a6c02d` alone.

**Base and end.** Base `4a6c02d`; end `4ee7736` (`docs(m35-fixes): fix M35's three medium findings in chapters 11, 12, 19`), HEAD when the reading started, recorded before any reader. The range holds three commits: `f526e4f` (`docs(queue): M39 gains ch14-open-lines-search, the open lines tip`, docs/06 only, no page and no notes), `46d5166` and `4ee7736`. This page and its marks are uncommitted and outside the range. No M37 to M39 delivery was committed in the range. The working tree's `book/` equalled the end commit throughout (`git diff 4ee7736 -- book/` empty).

**Inventory.** `git diff --stat -M 4a6c02d..4ee7736`: 13 paths, by area. Build: none. The kit's skills: none. Chapters (10): `book/{en,pt}/` 11, 12, 14, 15, 19. The documents (3): `docs/06-Queue.md`, and under `work/done/` `ch14-15-after-all-dropped.md` and `m35-fixes.md`. As the page expected.

**Slow tests.** None (docs/05 §5's Verify slot).

**Mechanical checks**, at `4ee7736`:

* The installed `queue.sh`, in `.agents/skills/` and `.claude/skills/`, byte-equal (`cmp`) to the kit's `SETUP.md` §3.7 at `4f5da97`, at the end commit and in the working tree.
* docs/05 §4 :103 to :106, "or `· after all`, every line above it in its milestone but the dropped ones, which is how the review is written", and :201 to :202, "a line whose `after` names it is the person's to re-decide. `after all` names none and leaves it out.", and §8 :438 to :440, "/propose writes its page when every line above but the dropped ones is defined, /apply runs it when every one of those is integrated", word for word the kit's `SETUP.md` at `4f5da97` :830 to :832, :926 to :927 and :1079 to :1081 (wrapped differently). docs/05 is unchanged since the end commit.
* The installed `queue.sh` on a scratch repository, chapter 14's example as one milestone (`lend-book` `[x]`, `return-book` and `my-loans` `[>]`, `print-card` `[x] · dropped: no printer driver`, `reprint-card` `[ ] · after print-card`, `m1-review · after all`): the tree printed `[ ] reprint-card · waits: after print-card, dropped: re-decide` and under it `[ ] m1-review + after return-book, my-loans · waits: reprint-card not defined`, `free for /propose, in order: none`. With `reprint-card` dropped too: `m1-review + after return-book · propose now`, `free for /propose, in order: m1-review`. As chapter 14 en :226 to :229 / pt :228 to :231 say. Reader 2 ran eight more cases and the checker three (below, R2-2).
* `book/` at the end commit, both editions, searched for `after all`: chapters 9 :23 and :110, 13 :177 and 19 :218 tell nothing against chapters 14 and 15; chapter 11 en :95 / pt :98, "which waits for the lines above it", gives no exception for cancelled lines (small 3).
* The disclosure scan, `make scan`, green. Chapter 14 en :224 / pt :226 tells the error "in one project" / "num projeto", a Milestone 1 review waiting on a dropped line, `after <slug>, dropped: re-decide`, its `after all` replaced by a list of the other 27 slugs, as the kit's `CHANGELOG.md` and `CHANGELOG.pt.md` `## 2026.10.27.1` word it: no project, place or business detail.
* The repository's tree, `queue.sh trunk`, exit 0, `git status --porcelain` the same before and after: `milestone: M36. focus-kit 2026.10.27.1`, `[*] m36-review · in flight: apply`, both free lists `none`, `next: none`.
* `make book` with `book/` clean, under the run's lock, exit 0, 14 seconds: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, read with `pdftotext -layout`.

**The author's word for this review.** Relayed to this session by the driver session on 2026-11-13: "Todas, médios entram": every milestone review `m35-review` to `m39-review` runs; its session takes the clause tests from its own reading of both PDFs and confirms every candidate the checker marks seen (docs/05 §8); every medium finding enters the one `m36-fixes` line; small ones stay listed on the page and none becomes a line. And "Sim, como o changelog": the dated errors are told as the kit's changelog words them, with no project named, no place and no business detail, none a Case A or Case B passage. By it, the clause answers below are the review's, from its own reading of both PDFs and of the repository at `4ee7736`, never the author's; each candidate the checker marks seen is confirmed, the latent and weak ones listed as dropped.

**The clause answers, the review's.** PDF pages en / pt, counted from the PDF's first page; source lines en / pt at `4ee7736`.

* **K1, the book teaches focus-kit 2026.10.27.1: holds.** Chapter 14: the opening p. 151 / 157 (:5 / :5, "so that it never reads as built nor keeps the milestone's review waiting"), the rule p. 156 / 162 (:92 / :93), the paragraph p. 162 to 163 / 169 to 170 (:222 to :229 / :224 to :231), the gain p. 164 / 172 (:269 / :271, "a line closed that way keeps no review waiting") and key point 2 p. 165 / 173 (:277 / :279); chapter 15: the opening and `## The review is a delivery` p. 167 to 168 / 175 to 176 (:3, :18), key point 2 p. 175 / 183 (:167 / :170). They teach `after all` leaving out the cancelled lines as the installed `queue.sh` reads it (Mechanical checks). No other chapter tells it otherwise; chapter 11's earlier "waits for the lines above it" leaves the exception out (small 3). The two editions say the same, with "cancelada", "redecidir" and "revisão de marco".
* **K2, the repository runs on it: holds.** docs/05 §4 :103 to :106 and :201 to :202 and §8 :438 to :440 hold the kit's three sentences (Mechanical checks); ADR-0018 :102 to :104 holds the amendment `kit-2026-10-27-1`; docs/03 :120's `dependency` row says "every line above it in its milestone but the dropped ones" and "a line that names a dropped one waits for the person to re-decide it"; the installed `queue.sh` equals the kit's.
* **K3, `· after all` leaving out the dropped lines: holds.** Chapter 14 :92 / :93, "every line above it in its milestone but the cancelled ones, so its `/propose` starts when they are all defined and its `/apply` when they are all integrated"; :225 / :227, "So `after all` names no cancelled line"; key point 2; chapter 15 :18, the same, with `/propose` and `/apply` per command. The cancelled lines are the `[x]` lines with `· dropped:` (chapter 14's mark table and :217 / :219).
* **K4, a review never waits on a line the person cancelled: holds, with one medium finding.** Chapter 14 gives the reason in the present (:222 to :223 / :224 to :225), the error of 2026-10-26 with no project named and its 27 slugs (:224 / :226), and `print-card`, cancelled, leaving `m1-review` free of it (:227 / :229; the scratch run). The reason's second half, "a review is neither dropped nor rewritten on what exists", is contradicted by the next sentence and by a dropped review in this repository's queue (medium 1); the rule and its example still hold for a reader who follows them.
* **K5, a line naming a dropped one still waits for re-decision: holds, with one medium finding.** Chapter 14 :228 to :229 / :230 to :231: `reprint-card` counted by `after all`, the tree printing `waits: after print-card, dropped: re-decide`, the review waiting with it until the person drops it too or rewrites it on what exists; chapter 15 :18 says it in one sentence and tells no second error. For a review's `/propose`, a re-decide line already `[>]` does not hold it (small 5); chapter 15's "re-decide it" can attach to the cancelled line (medium 2).

**Readers.** Three read-only readers on Opus, the first two as a pair, the third once the first ended, then the checker on Opus alone; at most two ran at once. Each was launched from this session with its model set to Opus and in the foreground; the host ran them in the background, and each final report reached this session as its completion notice, recorded here. Working files in the session's scratchpad, `m36/`.

* **Reader 1, chapters 11, 12, 19.** Range diffs of the six files; whole `m35-fixes.md`, en 11 and en 12; en 19 :1 to :75, :180 to :262, :340 to :370; pt 11 :76 to :106 and :183 to :210; pt 12 :26 to :45, :165 to :175, :200 to :211; pt 19 by grep; en 13 :40 to :60 and pt 13 :52 to :53; pt 14 :206 to :232; en 14 and 15 by diff and grep; docs/05 :96 to :140 and :435 to :520; docs/03, docs/04 and `m35-review.md` by grep; docs/06 :764 to :815; greps of `book/` for the free line, `after all`, resumption and em dashes. Advisor present, called once.
* **Reader 2, chapters 14, 15.** Whole: `ch14-15-after-all-dropped.md`, en 14, `queue.sh`; pt 14 :1 to :6, :198 to :232, :266 to :282; en and pt 15 :1 to :30 and :160 to :175; range diffs of the four files; docs/05 :95 to :110, :195 to :220, :430 to :445; docs/03 :120; docs/04 by grep; `book/` by grep; the changelog entries; eight scratch runs of `queue.sh`. Advisor present, called once.
* **Reader 3, the documents and records.** Whole: the two pages; range diffs of docs/06 and the chapter files; ch14 en :205 to :232 and pt :222 to :225; docs/05 §§3, 4, 6, 8 in part; ADR-0018 and `kit-2026-10-27-1.md` by grep; `m35-review.md` :170 to :196; `queue.sh` :10 to :11, :126 to :130, :143 to :157; the changelog entries; the history of `33432ee`, `8ff514d` and `28a607a`; the three commit messages against the pages' `commit` blocks; chapters 7 and en 18 by grep (pt 18 not checked, outside the range). One of its commands redirected an empty output to a file in the system's temporary folder, outside its scratch folder, never used. Advisor present, called once.
* **The checker**, one agent on every candidate, note and lead in one report, each file opened at `4ee7736`, chapters 11, 12 and 19 also by their range diff, three more scratch runs of `queue.sh`, and the pages of the open lines in `work/` read-only for ownership: 11 seen, 4 weak, 1 latent, none held by an open line. Advisor present, called once.

Every path of the inventory was read by at least one reader, by its range diff at the least.

**Notes copied**, from the `## For the review` headings of the range's pages: none. Neither `ch14-15-after-all-dropped` nor `m35-fixes` has the heading; the checker confirmed it.

**Candidates.** The checker's marks, lines at `4ee7736`, en / pt; `=` joins duplicates, graded once.

| Id | Where | Claim | Mark |
|---|---|---|---|
| R1-1 = R2-3 | ch11 :95 / :98 | "a delivery like the others, which waits for the lines above it", with no exception for cancelled lines | seen |
| R1-2 | ch13 :52 to :53 / :52 to :53 | No sentence that a resumed `[*]` keeps its mark; ch13 :20 and ch14 :206 say it | weak |
| R1-3 | ch19 :24 and :216 / same | The free line's wording makes the `[*]` line above "free"; :198 and :216 say taken, in flight | weak |
| R1-4 | ch11 :79 / :82 | "a grave finding, a flaw a delivery finds outside what it built" reads as a definition (m35-review small 4) | seen |
| R1-5 | ch11 :106 / :109, :187 / :192 | The placement rule restated without the two exceptions; their subjects are a new idea and a move | weak |
| R2-1 = R3-1 | ch14 :223 to :224 / :225 to :226 | "a review is neither dropped nor rewritten on what exists", against the next sentence's 27-slug list and docs/06 :512's dropped `m20-review` | seen |
| R2-2 | ch15 :18 / :18; ch14 :228 / :230 | "the review waits with it": not for the review's `/propose` when the re-decide line is already `[>]` (`propose now`) | seen |
| R2-4 | ch14 :226 / :228 | "written for this chapter" repeated from :210; "above" in two senses | seen |
| R2-5 | ch15 :18 / :18 | "re-decide it" / "redecidi-la": "it" can attach to the cancelled line | seen |
| R3-2 | ch14 :224 / :226 | The 27-slug list told as what happened, never said not to do; the page's Behaviour failure answered by inference (lead L4) | seen |
| R3-3 | ch14 :224 / :226 | `after <slug>, dropped: re-decide` is output the installed script cannot give for a review | weak |
| R3-4 | `ch14-15-after-all-dropped.md` Outcome | "in all six places": five per edition (lead L5) | seen |
| R3-5 | `ch14-15-after-all-dropped.md` Behaviour | "cancelada" and "redecidir" called docs/03's terms; docs/03 lists neither | seen |
| R3-6 | docs/06 :808 | `ch14-open-lines-search` has no `· after` beside its chapter 14 siblings | latent |
| R3-7 | docs/06 M39 paragraph | "reading a delivery's own line from its worktree" has no line (m35-review small 6) | seen |
| R3-8 | ch14 :224 / :226 | "a Milestone 1 review" / "Marco 1" capitalised against :226 / :228's "milestone 1" | seen |
| L1 | ch11 :81 / :84, ch19 :24, ch12 :31 to :32 | m35-review's M1, M2, M3 | fixed, both editions |
| L2 | ch11 :95 / :98 | = R1-1 | seen |
| L3 | `kit-2026-10-27-1.md` :15 | "Chapters 14 and 15 still teach the old reading" | true when written (`33432ee` precedes `8ff514d`, which added ch14 :92); no finding |
| L4 | ch14 :224 / :226 | = R3-2 | seen |
| L5 | ch14 :5, :227 / :229, :269 / :271; ch15 :3, :18 | "keeps ... waiting" / "faz ... esperar" in every place, no "holds the review" left | holds; five places, not six (R3-4) |

**Findings.** By the author's word, every candidate marked seen is confirmed; the weak and latent ones are dropped and listed under small (docs/05 §8). None is held by an open line.

*Grave*: none. Every clause holds, nothing loses or exposes data, and verify is green.

*Medium*, met in ordinary reading while the clauses hold, each an item of `m36-fixes` by the author's word:

1. M1, R2-1 = R3-1: chapter 14 en :223 / pt :225, "but a review is neither dropped nor rewritten on what exists, so no re-decision of its own would clear it", is the reason the delivery added for the rule, in the paragraph every reader of the rule meets; the next sentence, en :224 / pt :226, says that review's `after all` "was replaced by a list of the other 27 slugs", a rewrite that freed it, and this repository's docs/06 :512 holds `[x] m20-review ... · after all · dropped: its range was read by m19-review`. A reader who notices either finds the stated reason false. The same sentence holds small 6 (R3-2), which the fix may meet in passing; it is not picked.
2. M2, R2-5: chapter 15 en :18 / pt :18, "a line whose `after` names a cancelled one waits for the person to re-decide it, and the review waits with it" (pt "espera a pessoa redecidi-la"): "it" can attach to the cancelled line, the nearer noun, both feminine in Portuguese. The delivery's own review graded the same ambiguity medium in chapter 14 en :223 / pt :225 and fixed it there ("on a line only the person's decision clears"), leaving chapter 15's sentence, which carries the milestone's last clause.

*Small*, each a record's precision, a rare case, a wording few meet or a dropped candidate:

3. R1-1 = R2-3: chapter 11 en :95 / pt :98, the review line "waits for the lines above it", before the book has taught a cancelled line; chapters 14 and 15 give the exception.
4. R1-4: chapter 11 en :79 / pt :82's gloss of a grave finding, as m35-review's small 4; unchanged in the range.
5. R2-2: chapter 15 en :18 / pt :18, "the review waits with it", fails for the review's `/propose` only when the re-decide line was defined before its prerequisite was dropped; true for `/apply` and in chapter 14's example.
6. R3-2: chapter 14 en :224 / pt :226 never says not to replace `after all` with a list; the page's Behaviour failure is answered by inference from :225 to :229, as its Outcome kept.
7. R2-4: chapter 14 en :226 / pt :228 repeats "written for this chapter" and uses "above" in two senses.
8. R3-8: chapter 14 en :224 / pt :226's "Milestone 1" / "Marco 1", the changelog's capital, against the book's lower case.
9. R3-4: `ch14-15-after-all-dropped.md`'s Outcome says six places; there are five per edition.
10. R3-5: the same page calls "cancelada" and "redecidir" docs/03's terms; docs/03 lists neither.
11. R3-7: docs/06's M39 clause on reading a delivery's own line from its worktree has no line, as m35-review's small 6.
12. Dropped, weak: R1-2, R1-3, R1-5, R3-3; latent: R3-6.

**Proof.** The mechanical checks and the clause answers above; `make book` at `4ee7736`; `make verify` green after the last edit to this page and docs/06, 12 seconds, under the five-minute ceiling.

**The medium pick.** By the author's word quoted above, M1 and M2 enter the one `m36-fixes` line, each an item of its page, which is their list and is not split; no small finding is picked, so none becomes a line (docs/05 §8). The line sits under this review, `· after m36-review · from m36-review`, added with the host's file edit on that one line.

**Decisions taken alone in /apply.** For the author's review.

* R2-5 is graded medium, as the checker leaned with low confidence: the delivery's own review graded the identical ambiguity medium in chapter 14 and fixed it there, and grading the twin small would leave the two chapters graded apart for one wording.
* R3-2 stays its own small finding rather than joining M1: M1 is a false reason, R3-2 a missing instruction the delivery chose to leave to inference; the fix of M1 meets its sentence, and the page of `m36-fixes` may say so.
* R2-2 is small, and the one finding in K5's passage that is not M2: it needs a re-decide line already `[>]` when its prerequisite is dropped, a rare order of events.
* PDF pages are counted from each PDF's first page, as `pdftotext` splits them.
* The readers were asked for the foreground and ran in the background, the host's way; each report reached this session, so no `[?]` was needed.

The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

```commit
docs(m36-review): review M36, five clauses hold, two medium fixes

- Base 4a6c02d, end 4ee7736; every clause of M36 holds in both PDFs
- queue.sh equal to the kit and run on chapter 14's example
- Three readers and a checker: 11 seen, 4 weak, 1 latent, none held
- m36-fixes under m36-review with the two medium findings

work/done/m36-review.md
```
