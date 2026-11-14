# m35-review

**Objective.** The author can decide whether M35's promise holds, the clauses of its paragraph tested in the PDF of both editions and on this repository, and whether everything changed since m34-review's commit holds under the code reading by areas, with every confirmed finding graded: each grave one a line under this review, the medium ones in the one `m35-fixes` line, the small ones listed here.

This page was defined by the agent before the author read it, on the author's word for this run, relayed by the driver session on 2026-11-13: "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão" (close every open line of docs/06 without supervision). Every question the documents leave open is answered by the agent's recommendation, written below as the agent's choice; the author reads the page and the diff at the end (docs/05 §4).

**Behaviour.**

* With every line above this review in M35 `[x]` and committed, /apply records the base and the end commit, builds both PDFs at the end commit with `book/` clean, and answers each clause test below: holds, or fails with what was seen. A clause no delivery answers, or one that fails, is a finding (docs/05 §8).
* The review opens by copying onto this page, verbatim, the notes under `## For the review` of every page the range delivered, naming the pages that have none (`m34-fixes` has none today); the checker marks each note as it marks a candidate (docs/05 §8).
* Read-only readers on Opus read one fixed range, `git diff <base>..<end>`, one per area the range touches, at most two running at a time; one checker on Opus then marks every candidate and every note seen, latent or weak against the end commit (docs/05 §5, Milestone review). Every launch sets its model to Opus, runs in the foreground so its report reaches this session, and keeps the session's advisor.
* On the author's word, quoted below, the review's session takes the clause tests from its own reading of both PDFs and of the repository, and the word is the confirmation of each candidate the checker marks seen; the latent and weak ones are listed as dropped. These answers are the review's, never the author's (docs/05 §8).
* Every confirmed finding is graded by docs/05 §4 and §8: grave, when it breaks a clause of M35's paragraph for a person on its usual path, loses or exposes data, or leaves verify red, each its own `[ ]` line under this review ending `· after m35-review · from m35-review`; medium, met in ordinary use while the clause holds; small, a rare case, a latent or weak candidate, a cost nobody measured.
* On the author's word for the medium pick, every medium finding enters the one `m35-fixes` line, each an item of its page, ending `· after m35-review · from m35-review`; with no medium finding, no line. Small ones are listed on this page, numbered, and none becomes a line.
* A clause with no answer, a reader or checker whose report does not reach this session, or paths of the range no reader read leave this review waiting as `[?]` with `· resume: apply` and the reason (docs/05 §§4, 8).
* Edge, later milestones: M36 to M39's chapter lines (`ch14-15-after-all-dropped`, `ch13-apply-next`, `ch13-apply-findings`, `ch14-queue-findings`, `ch15-review-grades`, `ch13-apply-after`, `ch14-after-never-waits`, `ch14-queue-every-milestone`) are open. A candidate one of them already holds is listed with that line and is no finding here.
* Edge, a later milestone's delivery in the range: another session may commit an M36 to M39 delivery before the end commit. Its paths are read by the area readers without a clause test, its notes are copied here, since the range delivered its page, and the Outcome names it so that milestone's review knows its code was read here.
* Edge, the kit's own scripts: no path under `.claude/skills/` or `.agents/skills/` is in the range today; a candidate in one is graded as any other, and its fix, when it enters, is a note in `work/kit-proposals.md`.
* Edge, the error's project: chapter 14's error of 2026-10-26 is told as the kit's changelog words it, with no project named; by the author's word of 2026-11-13 ("Sim, como o changelog") it is no Case A or Case B passage, so docs/05 §5's Case A and Case B slot asks nothing of this review. The same word closes note N3 of `m34-review`; the Outcome says so.
* Edge, the shared tree: readers and the checker read the end commit (`git diff <base>..<end>`, `git show <end>:<path>`), never the working tree or the index; a commit made during the reading does not move the end commit.

**Contract.** Clause tests from docs/06's M35 paragraph, each against its delivery's page in `work/done/` and the named passages. The chapter passages are named by chapter and section, since `ch12-14-mark-refused` is being built while this page is written; /apply finds their lines and PDF pages at the end commit. The clause ids below are this review's, not that page's C1 to C8.

| Clause | Deliveries and passages | The test |
|---|---|---|
| K1. The book teaches focus-kit 2026.10.27 | `ch12-14-mark-refused`: chapters 12, 13 and 14; chapter 8 already at 2026.11.12 (`ch08-update-2026-10-25`, M33) | Do chapters 12, 13 and 14 teach the mark script's refusal as the kit installs it, and does no other chapter tell a second start of one line otherwise (Mechanical checks)? Do the two editions say the same, in docs/03's Portuguese terms? |
| K2. And the repository runs on it | `kit-2026-10-27` (committed in `cd79120`, before the base): docs/05 §4 :215 to :216, "`mark.sh` refusing a second start of one line is that of 2026.10.27"; ADR-0018 :98 to :100, amendment `kit-2026-10-27`; the installed `mark.sh` :10 to :12, "A "[~]" goes only on a "[ ]" line and a "[*]" only on a "[>]" one"; docs/03's `mark script` row, which `ch12-14-mark-refused` extends | Does docs/05 §4 name 2026.10.27 for the refusal, and ADR-0018 hold its amendment? Does the installed `mark.sh` equal the kit's, and does docs/03's row state the refusal? |
| K3. `mark.sh` refusing a `[~]` on a line that is not `[ ]` and a `[*]` on one that is not `[>]` | `ch12-14-mark-refused`: chapter 14, its opening and `## How a mark changes`, and key point 1; chapter 12, the sentence on /propose's `[~]` through the mark script; chapter 13, /apply's `[*]` as its first edit, and key point 2 | Does chapter 14 say the script sets `[~]` only on a `[ ]` line and `[*]` only on a `[>]` one, refusing any other before it writes anything, its message saying the line is another session's, resumed only on the person's word? Do chapters 12 and 13 say which start each command's mark is refused on? |
| K4. So two sessions that start one line cannot both mark it | `ch12-14-mark-refused`: chapter 14, `## How a mark changes` (the error), `## A session that ended, a delivery cancelled`, and the team gain; chapter 13, /apply's first edit | Does chapter 14 give the reason in the present, both sessions reading the line free until one marks it, with two `/apply` of one slug six seconds apart on 2026-10-26 as the error, told with no project named? Does chapter 13 say a second `/apply` of the slug stops without building? Does chapter 14 say a resumed line keeps its mark, so a resumption on the person's word is not refused? |

The kit's changelog, `## 2026.10.27` in `CHANGELOG.md` and `CHANGELOG.pt.md` of the kit's repository, is the source the error and its six seconds are checked against.

**Base.** `1649df7` (`docs(m34-review): review M34, five clauses hold, two medium fixes`), the commit of m34-review, the previous milestone's review (docs/05 §8), the one commit `git log --diff-filter=A -- work/done/m34-review.md` returns. The range therefore holds M34's one finding line, `m34-fixes` (`79df2ee`), read by the area readers without a clause and with no second review (docs/05 §8); `28a607a` (`docs(queue): M39, ...`), an edit of docs/06 with no page and no notes; and M35's chapter delivery, `ch12-14-mark-refused`, once committed. `kit-2026-10-27` was committed before the base, in `cd79120`; K2 tests its result at the end commit.

**End.** The commit HEAD is when the reading starts, recorded before any reader; this page and its mark, uncommitted, are read from the working tree as the spec.

**Areas.** Expected from the range today and `ch12-14-mark-refused`'s page; /apply recomputes them from `git diff --stat -M <base>..<end>` at the end commit, places every path in an area of docs/05 §5's Milestone review slot, and adds a reader for any area that appears:

* **Build:** no path of the `Makefile`, `scripts/`, the READMEs, `VERSION` or `docs/manuals/`; no reader.
* **The kit's skills:** no path; no reader.
* **Chapters:** `book/{en,pt}/` 07, 11 and 18 (`m34-fixes`) and 12, 13 and 14 (`ch12-14-mark-refused`), twelve files, split in two readers.
* **The documents:** `docs/03`, `docs/06`, and the two records under `work/done/` the range adds, `m34-fixes.md` and `ch12-14-mark-refused.md`, read with the chapters they describe, docs/04 and docs/05.

**Readers.** Three read-only readers on Opus, then one read-only checker on Opus alone; each launch sets its model to Opus, runs in the foreground and keeps the session's advisor, at most two at a time (docs/05 §5):

* pair 1: **chapters 7, 11 and 18** (M34's finding line), and **chapters 12, 13 and 14** (M35's delivery), both editions, whole at the end commit and by their range diffs, against their pages and the installed `mark.sh`;
* then **the documents and records**, against each other, the chapters they describe, docs/04 and the kit's changelog;
* then the checker, on every candidate, every copied note and every lead in one report.

Each reader lists the paths it read and how (whole, diff, grep), and says whether it kept the advisor.

**Slow tests.** None (docs/05 §5's Verify slot).

**Known leads**, given to the checker with the readers' candidates:

* L1, m34-review's R3-8, "the refusal of a second start untaught" (`mark.sh` :10 to :12; docs/03's `mark script` row), held then by `ch12-14-mark-refused`: answered at the end commit, in chapters 12, 13, 14 and docs/03, both editions.
* L2, m34-review's two medium findings, read as fixed at the end commit in both editions: M1, chapters 7 and 18's free line read with `after` per command; M2, chapter 11 keeping a grave finding in its own milestone.
* L3, `ch12-14-mark-refused`'s decision that docs/03's `mark script` row did not hold the refusal before it: the row at the end commit and its Portuguese.

**Mechanical checks**, run by /apply at the end commit:

* The installed `mark.sh` in both skills folders equals the kit's `SETUP.md` §3.8 (`propose/scripts/mark.sh`) at `4f5da97`, focus-kit 2026.11.12, the version the repository runs (`kit-2026-11-13` is still open).
* The installed `mark.sh` run on a scratch repository: `[~]` on a `[ ]` line and `[*]` on a `[>]` line marked, exit 0; a second `[~]`, a `[~]` on a `[>]` line, a `[*]` on a `[ ]` line and a second `[*]` each refused with exit 2, the queue byte-identical and the message saying the line is another session's, resumed only on the person's word; against chapter 14's `## How a mark changes`.
* `book/` in both editions searched for a passage outside chapters 12, 13 and 14 that tells a second start of one line otherwise (a session marking a line already `[~]` or `[*]`, a resumed line marked again, a mark changed by hand after a refusal).
* The disclosure scan at the end commit, and chapter 14's error checked against the changelog's wording: no project, place or business detail.
* The repository's tree: `queue.sh trunk` prints M35 with `m35-review` in flight, `git status` the same before and after.
* `make book` with `book/` clean; `make verify` after the last edit.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs, `make book` at the end commit.

**Out of scope.**

* Fixing any finding: grave ones become lines, medium ones the `m35-fixes` line (docs/05 §8).
* Re-testing M34's clauses: its fix line is read by the area readers, not tested by clause.
* Teaching 2026.10.27.1 to 2026.11.13 in the chapters: M36 to M39's lines.
* That the refusal is not a lock against two runs in the same instant: `ch12-14-mark-refused` leaves it out, as the kit claims only that the second is refused.

**Decisions from the documents.**

* The base is m34-review's commit, `1649df7`, the first of docs/05 §8's cases.
* No build reader and no kit reader: the range is expected to touch neither (docs/05 §8, one reader per area it touches); /apply adds one if the inventory shows otherwise.
* The clause tests, the confirmation and the medium pick are taken on the author's word quoted below (docs/05 §8).
* The notes are copied from every page the range delivered (docs/05 §8).
* The mark script is compared with the kit at `4f5da97`, the version the repository runs, not the kit's newest (docs/05 §4's provenance paragraph ends at 2026.11.12).

**The author's word for this review.** Relayed to this session by the driver session on 2026-11-13: "Todas, médios entram": every milestone review `m35-review` to `m39-review` runs; its session takes the clause tests from its own reading of both PDFs and confirms every candidate the checker marks seen (docs/05 §8); every medium finding enters the one `m35-fixes` line; small ones stay listed on the page and none becomes a line. And, for the dated errors: "Sim, como o changelog": they are told as the kit's changelog words them, with no project named, no place and no business detail, none a Case A or Case B passage, which also closes note N3 of `m34-review`.

**Decisions taken alone.** The agent chose each of these, for the author's review.

* M35's paragraph is taken as four clauses, by what can be checked: the book teaches 2026.10.27, the repository runs on it, the refusal itself, and what it prevents.
* The chapters area splits in two, by milestone, as m34-review did: M34's fix in chapters 7, 11 and 18, M35's delivery in 12, 13 and 14 (docs/05 §8, an area too large for one careful reading).
* The chapter passages are named by chapter and section, not line, since `ch12-14-mark-refused` is being built while this page is written; /apply finds the lines and pages.
* A later milestone's delivery committed inside the range is read here without a clause and named in the Outcome, so its own review knows.
* A candidate an open M36 to M39 line holds is listed with that line, as m34-review did.

**Done when.**

* [x] Every line above this review in M35 is `[x]` and committed; every clause has the review's answer, on the author's word quoted on this page.
* [x] Base, end, the inventory by area, each reader's paths read and its advisor, every copied note and candidate with its mark are on this page.
* [x] Every confirmed finding graded; each grave one a `[ ]` line under this review; every medium one an item of the `m35-fixes` line, when any; small ones listed, numbered.
* [x] N3 of `m34-review` recorded as closed by the author's word of 2026-11-13.
* [x] The mechanical checks recorded; `make book` built both PDFs at the end commit; `make verify` green after the last edit, with its time.
* [x] The page in `work/done/`, its paths staged and its commit message suggested.

## Outcome

This review was built by the agent before the author read it, on the author's word quoted below; the author reads the page and the diff at the end (docs/05 §4).

**Precondition.** Every line above this review in M35 is `[x]` and committed: `kit-2026-10-27` before the base (its install in `5b13679`, its page added in `cd79120`; the Contract's "committed in `cd79120`" names the page's commit), `ch12-14-mark-refused` `2673874`; M34's finding line `m34-fixes` `79df2ee`. `git log --diff-filter=A -- work/done/m34-review.md` returns `1649df7` alone.

**Base and end.** Base `1649df7`; end `2673874` (`docs(ch12-14-mark-refused): teach mark.sh refusing a second start`), HEAD when the reading started, recorded before any reader. This page and its marks are uncommitted and outside the range. No M36 to M39 delivery was committed in the range.

**Inventory.** `git diff --stat -M 1649df7..2673874`: 16 paths, by area. Build: none. The kit's skills: none. Chapters (12): `book/{en,pt}/` 07, 11, 12, 13, 14, 18. The documents (4): `docs/03-Domain.md`, `docs/06-Queue.md` (with `28a607a`, M39 added, no page and no notes), and under `work/done/` `m34-fixes.md` and `ch12-14-mark-refused.md`.

**Slow tests.** None (docs/05 §5's Verify slot).

**Mechanical checks**, at `2673874`:

* The installed `mark.sh`, in `.agents/skills/` and `.claude/skills/`, byte-equal to each other and to the kit's `SETUP.md` §3.8 at `4f5da97` (`cmp`), and unchanged since the end commit.
* The installed `mark.sh` on a scratch repository: `[~]` on a `[ ]` line and `[*]` on a `[>]` line marked, exit 0; a second `[~]`, a `[~]` on a `[>]` line, a `[*]` on a `[ ]` line and a second `[*]` each refused, exit 2, the queue byte-identical, the message "error: alpha is [~], not [ ]; docs/05 §4 says how it moves, and a [~] or [*] is another session's, resumed only on the person's word; nothing written"; as chapter 14's `## How a mark changes` says.
* `book/` at the end commit, both editions: no passage outside chapters 12, 13 and 14 tells a second start of one line otherwise. Chapters 11, 17, 19 and 20 show `[~]` and `[*]` without marking a taken line again; chapter 19 :68's "`[~]` to `[*]`" is what one session sees of another's line between two looks, not one mark (R2-2, weak).
* The disclosure scan, `make scan`, green. Chapter 14 en :80 / pt :81 tells the error "in one project" / "num projeto", one folder on trunk, six seconds apart, as the kit's `CHANGELOG.md` and `CHANGELOG.pt.md` `## 2026.10.27` word it: no project, place or business detail.
* The repository's tree, `queue.sh trunk`, exit 0, `git status --porcelain` the same before and after: `milestone: M35. focus-kit 2026.10.27`, `[*] m35-review · in flight: apply`, both free lists `none`, `next: none`.
* `git diff 2673874 -- book/` empty before `make book`; `make book`, exit 0, 18 seconds: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, read with `pdftotext -layout`.

**The author's word for this review.** Relayed to this session by the driver session on 2026-11-13: "Todas, médios entram": every milestone review `m35-review` to `m39-review` runs; its session takes the clause tests from its own reading of both PDFs and confirms every candidate the checker marks seen (docs/05 §8); every medium finding enters the one `m35-fixes` line; small ones stay listed on the page and none becomes a line. And "Sim, como o changelog": the dated errors are told as the kit's changelog words them, with no project named, no place and no business detail, none a Case A or Case B passage. By it, the clause answers below are the review's, from its own reading of both PDFs and of the repository at `2673874`, never the author's; each candidate the checker marks seen is confirmed, the latent and weak ones listed as dropped.

**N3 of `m34-review`, closed.** Whether a private case is behind chapter 14's errors is closed by the author's word of 2026-11-13, "Sim, como o changelog": the errors are the kit's changelog's, told with no project named, and none is a Case A or Case B passage, so docs/05 §5's Case A and Case B slot asks nothing of them.

**The clause answers, the review's.** PDF pages en / pt; source lines en / pt.

* **K1, the book teaches focus-kit 2026.10.27: holds.** Chapter 12, p. 122 / 126 (:31): `[~]` set only on a `[ ]` line, a second `/propose` refused; chapter 13, p. 136 / 142 (:53) and the key point p. 149 / 155 (:294): `[*]` only on a `[>]` line, a second `/apply` refused; chapter 14, the opening p. 151 / 157, the rule p. 155 / 161 to 162, the resumed line p. 161 / 168, the gain and key point p. 164 to 165 / 171 to 172. No other chapter tells a second start otherwise (Mechanical checks). The two editions say the same, with docs/03's "script de marca". Chapter 12's resumed `/propose` reads as marking `[~]` again (medium 3).
* **K2, the repository runs on it: holds.** docs/05 §4 :215 to :216, "`mark.sh` refusing a second start of one line is that of 2026.10.27"; ADR-0018 :98 to :100 holds the amendment `kit-2026-10-27`; the installed `mark.sh` equals the kit's (Mechanical checks), its :10 to :12 "A "[~]" goes only on a "[ ]" line and a "[*]" only on a "[>]" one"; docs/03 :31's `mark script` row states the refusal, "any other refused with nothing written".
* **K3, the refusal: holds.** Chapter 14 en :79 to :82 / pt :80 to :83, p. 155 / 162: "it sets a `[~]` only on a `[ ]` line and a `[*]` only on a `[>]` one, and on any other line it refuses before it writes anything, saying that a `[~]` or `[*]` is another session's, resumed only on the person's word", the scratch run's message; the key point p. 165 / 172. Chapters 12 and 13 say which start each command's mark is refused on.
* **K4, two sessions cannot both mark one line: holds.** Chapter 14 gives the reason in the present, "Two sessions that start one line both read it free until one of them marks it", then the error of 2026-10-26, two `/apply` of one slug six seconds apart, with no project named; chapter 13 :53, a second `/apply` "stops without building"; chapter 14 :206 / :208, "neither resumed command marks its line again", so a resumption on the person's word is not refused.

**Readers.** Three read-only readers on Opus, the first two as a pair, the third once the first ended, then the checker on Opus alone; at most two ran at once. Each was launched from this session with its model set to Opus and in the foreground; the host ran them in the background, and each final report reached this session as its completion notice, recorded here. Working files in the session's scratchpad, `m35/`.

* **Reader 1, chapters 7, 11, 18.** Range diffs of all six files; ch11 en :1 to :12, :55 to :125, :150 to :205 and ch07 en :55 to :90 whole; ch11 pt and ch07 pt at the lines named; ch18 both editions by its hunk; `m34-fixes.md` whole; docs/05 §§4, 8; by grep docs/03, docs/04, docs/06, `m34-review.md`, chapters 12, 13, 14, 15, 19. Chapter 18's trunk section and ch11 pt were not read whole; each hunk matched sentence for sentence. Advisor present, called once.
* **Reader 2, chapters 12, 13, 14.** Whole: `ch12-14-mark-refused.md`, en 14, `mark.sh`, the changelog entries; en 12 :1 to :45 and en 13 :1 to :60 whole, the rest by grep; pt 14 :68 to :87 and :200 to :209 whole; range diffs of the six files; docs/05 :150 to :219; by grep docs/03, docs/04, the propose and apply skills, chapters 10, 15, 19; nine scratch runs of `mark.sh`. Advisor present, called once.
* **Reader 3, the documents and records.** Whole: the two pages, the three commit messages, `mark.sh`, docs/05 §§3, 4, 6; range diffs of docs/03, docs/06 and the chapter files; ADR-0018 :98 to :105; docs/04 in part; the propose and apply skills in part; the kit's `CHANGELOG.md` `## 2026.10.27` and `## 2026.11.13`, `CHANGELOG.pt.md` `## 2026.10.27`. Advisor present, called once.
* **The checker**, one agent on every candidate, note and lead in one report, each file opened at `2673874`, chapters 11 and 14 and docs/03 also at `1649df7`: 8 seen, 2 weak, 0 latent, none held by an open line, and a weak half of R2-1. Advisor present, called once.

Every path of the inventory was read by at least one reader, by its range diff at the least.

**Notes copied**, from the `## For the review` headings of the range's pages: none. Neither `m34-fixes` nor `ch12-14-mark-refused` has the heading; the checker confirmed it.

**Candidates.** The checker's marks, lines at `2673874`, en / pt; `=` joins duplicates, graded once.

| Id | Where | Claim | Mark |
|---|---|---|---|
| R1-1 | ch11 :79, :81 / :82, :84 | A grave finding stays in its milestone, then "a line enters the current milestone only through a clause" | seen |
| R1-2 | ch19 :24 / :24 | "A free line ... needs no other line done first", M1's wording left in a third chapter | seen |
| R1-3 | ch11 :79 / :82 | "a grave finding, a flaw a delivery finds outside what it built" read alone | seen |
| R2-1 | ch12 :30 to :31 / :30 to :31 | A resumed `/propose` whose first edit marks `[~]`, which the script refuses; chapter 14 :206 says no resumed command marks again | seen (ch12); weak (the ch13 half) |
| R2-2 | ch19 :68 / :68 | "`[~]` to `[*]`, say" as one move | weak |
| R2-3 = R3-1 | `ch12-14-mark-refused.md` :73 | Outcome C1, "the opening keeps its two sentences"; it has three | seen |
| R3-2 | docs/06 :800 | M39's clause "reading a delivery's own line from its worktree" named by no M39 line | seen |
| R3-3 | docs/06 :803 | `kit-2026-11-13` leaves out §4's sentence on a branch's line under main's heading | seen |
| R3-4 | `.agents/skills/propose/SKILL.md` :27 to :30 | After `claim: taken` resumed, "your first edit there marks it `[~]`", refused on a `[~]` line | seen |
| R3-5 | ADR-0018 :100 | "No document changes" against the range's docs/03 row | weak |
| L1 | ch12, 13, 14; docs/03 :31 | m34-review's R3-8, the refusal untaught | answered, both editions |
| L2 | ch07 :81 / :82, ch18 :186, ch11 :78 to :79 / :81 to :82 | m34-review's M1 and M2 | fixed where named; R1-1 and R1-2 left |
| L3 | docs/03 :31 | The row lacked the refusal at `1649df7` | holds it at `2673874`; "script de marca" in pt |

**Findings.** By the author's word, every candidate marked seen is confirmed; the weak ones are dropped and listed under small (docs/05 §8). None is held by an open line.

*Grave*: none. Every clause holds, nothing loses or exposes data, and verify is green.

*Medium*, met in ordinary reading while the clauses hold, each an item of `m35-fixes` by the author's word:

1. M1, R1-1: chapter 11 en :79 / pt :82 keeps a grave finding in its milestone "even when no clause needs them", and en :81 / pt :84, two lines later, "a line enters the current milestone only through a clause, so to bring one in you widen the paragraph by conversation first"; `m34-fixes` added the first and left the second.
2. M2, R1-2: chapter 19 en :24 / pt :24, "A free line is a line of the queue that is not done, not waiting, and needs no other line done first", against `after` read per command (chapters 7 :81, 14, 18 :186, docs/03's free line row); m34-review's M1 named chapters 7 and 18 only.
3. M3, R2-1: chapter 12 en :30 to :31 / pt :30 to :31, a definition "reused when the definition resumes", then "Its first edit there marks the line `[~]` ... so a second `/propose` of the slug is refused there": a resumed `/propose` reads as marking `[~]` again, which the script refuses, while chapter 14 :206 / :208 says neither resumed command marks its line again (docs/05 §4, a resumed line keeps its mark).

*Small*, each a record's precision, a rare case or a dropped candidate:

4. R1-3: chapter 11 :79 / :82's gloss of a grave finding, which :74, :98 and :181 bound.
5. R2-3 = R3-1: `ch12-14-mark-refused.md` :73 counts chapter 14's opening as two sentences; it has three.
6. R3-2: docs/06's M39 paragraph names `queue.sh` reading a delivery's own line from its worktree, which no M39 line names; m39-review would find the clause unanswered.
7. R3-3: docs/06's `kit-2026-11-13` line leaves out §4's sentence on a branch's line under main's heading, which its "apply its migration report" still covers.
8. R3-4: the kit's propose `SKILL.md` :27 to :30 has a resumed `/propose` mark `[~]` again; a kit file, so its fix, if the author picks it, is a note in `work/kit-proposals.md`.
9. Dropped, weak: R2-2, R3-5, and R2-1's chapter 13 half.

**Proof.** The mechanical checks and the clause answers above; `make book` at `2673874`; `make verify` green after the last edit to this page and docs/06, 13 seconds, under the five-minute ceiling.

**The medium pick.** By the author's word quoted above, M1, M2 and M3 enter the one `m35-fixes` line, each an item of its page, which is their list and is not split; no small finding is picked, so none becomes a line (docs/05 §8). The line sits under this review, `· after m35-review · from m35-review`, added with the host's file edit on that one line.

**Decisions taken alone in /apply.** For the author's review.

* The checker's grades are taken as they stand: R2-1 medium, not grave, since the script still refuses a second start and chapter 14 teaches the resumption right, so the clause holds; R3-2 small, since M39 is not yet defined and its /propose can widen a line.
* R2-1's source, the kit's propose `SKILL.md`, is kept as its own small finding (R3-4), not joined, since the fix of each lives in a different repository.
* The checker's summary sentence says six seen, its table marks eight; the page follows the table.
* The readers were asked for the foreground and ran in the background, the host's way; each report reached this session, so no `[?]` was needed.

The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

```commit
docs(m35-review): review M35, four clauses hold, three medium fixes

- Base 1649df7, end 2673874; every clause of M35 holds in both PDFs
- mark.sh equal to the kit and run on a scratch repository
- Three readers and a checker: 8 seen, 2 weak, none held
- m35-fixes under m35-review with the three medium findings
- N3 of m34-review closed by the author's word of 2026-11-13

work/done/m35-review.md
```
