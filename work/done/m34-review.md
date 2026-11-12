# m34-review

**Objective.** The author can decide whether M34's promise holds, the clauses of its paragraph tested in the PDF of both editions and on this repository, and whether everything changed since m33-review's commit holds under the code reading by areas, with every confirmed finding graded: each grave one a line under this review, the medium ones in the one `m34-fixes` line, the small ones listed here.

This page was defined and built by the agent before the author read it, on the author's word that the agent runs the whole queue, the milestone reviews included; the author reads the page and the diff at the end (docs/05 §4).

**Behaviour.**

* With every line above this review in M34 `[x]` and committed, /apply records the base and the end commit, builds both PDFs at the end commit with `book/` clean, and answers each clause test below: holds, or fails with what was seen. A clause no delivery answers, or one that fails, is a finding (docs/05 §8).
* The review opens by copying onto this page, verbatim, the notes under `## For the review` of every page the range delivered, naming the pages that have none; the checker marks each note as it marks a candidate (docs/05 §8).
* Read-only readers on Opus read one fixed range, `git diff <base>..<end>`, one per area the range touches, at most two running at a time; one checker on Opus then marks every candidate and every note seen, latent or weak against the end commit (docs/05 §5, Milestone review).
* On the author's word, quoted below, the review's session takes the clause tests from its own reading of both PDFs and of the repository, and the word is the confirmation of each candidate the checker marks seen; the latent and weak ones are listed as dropped. These answers are the review's, never the author's (docs/05 §8).
* Every confirmed finding is graded by docs/05 §4 and §8: grave, when it breaks a clause of M34's paragraph for a person on its usual path, loses or exposes data, or leaves verify red, each its own `[ ]` line under this review ending `· after m34-review · from m34-review`; medium, met in ordinary use while the clause holds; small, a rare case, a latent or weak candidate, a cost nobody measured.
* On the author's word for the medium pick, quoted below, every medium finding enters the one `m34-fixes` line, each an item of its page, ending `· after m34-review · from m34-review`; with no medium finding, no line. Small ones are listed on this page, numbered, and none becomes a line.
* A clause with no answer, a reader or checker whose report does not reach this session, or paths of the range no reader read leave this review waiting as `[?]` with `· resume: apply` and the reason (docs/05 §§4, 8).
* Edge, later milestones: M35 to M38's chapter lines (`ch12-14-mark-refused`, `ch14-15-after-all-dropped`, `ch13-apply-next` and M38's) are open. A candidate one of them already holds is listed with that line and is no finding here.
* Edge, the kit's own scripts: no path under `.claude/skills/` or `.agents/skills/` is in the range; a candidate in one is graded as any other, and its fix, when it enters, is a note in `work/kit-proposals.md`.
* Edge, a private case: a passage that may be drawn from Case A or Case B is the author's to approve (docs/05 §5, Case A and Case B); the review records the question and does not answer it on the author's behalf.
* Edge, the shared tree: readers and the checker read the end commit (`git diff <base>..<end>`, `git show <end>:<path>`), never the working tree or the index; a commit made during the reading does not move the end commit.

**Contract.** Clause tests from docs/06's M34 paragraph, each against its delivery's page in `work/done/` and the named passages. Lines are en / pt at `2ee5bf5`; where one number is given it is the same in both.

| Clause | Deliveries and passages | The test |
|---|---|---|
| C1. The book teaches focus-kit 2026.10.26 | `ch12-14-mark`, `ch19-mark-stage`; chapter 8 already at 2026.11.12 (`ch08-update-2026-10-25`, M33) | Do chapters 12, 13, 14 and 19 teach the mark script as the kit installs it, and does no other chapter set a mark or stage a queue line another way (Mechanical checks)? Do the two editions say the same? |
| C2. And the repository runs on it | `kit-2026-10-26` (committed in `cd79120`, before this range): docs/05 §4 :163 to :167 and its provenance paragraph, ADR-0018's amendment; the installed `mark.sh` | Does docs/05 §4 hold 2026.10.26's two sentences? Does the installed `mark.sh` equal the kit's at 2026.11.12, and does docs/03 name the mark script? |
| C3. A mark changed by `mark.sh`, one byte | `ch12-14-mark`: chapter 12 (:31, :33, :195 / :31, :33, :204), chapter 13 (:34 to :35, :52, :293), chapter 14 (:3, :67 to :80 / :3, :68 to :81, :262 / :264) | Does each chapter say `[~]`, `[>]`, `[*]` and `[x]` change through the mark script, one byte, the file written beside and renamed over, refused unless the size holds? |
| C4. Staged with it on its line alone | `ch12-14-mark`: chapter 13 (:126, :154); `ch19-mark-stage`: chapter 19 (:29, :54, :370, :387, :415) | Do chapters 13 and 19 say `/apply`'s `[x]` is staged with `stage`, that line alone in the index, another session's staged lines kept, in one folder and in a batch's shared hunk, with no patch and no `git apply`? |
| C5. Any other edit to docs/06 by the host's file edit | `ch12-14-mark`: chapter 14 (:71 to :80 / :72 to :81) | Does chapter 14 say every other edit is the host's file edit on its lines, never a program that writes the whole queue, with the queue emptied on 2026-10-18 and 2026-10-26 as the error, and a `[?]` as two edits? |

**Base.** `47b35ee` (`docs(m33-review): review M33, one grave finding, six medium fixes`), the commit of m33-review, the previous milestone's review (docs/05 §8), the one commit `git log --diff-filter=A -- work/done/m33-review.md` returns. The range therefore holds M33's two finding lines, `ch08-09-parallel-paragraphs` (`32d084f`) and `m33-fixes` (`96a8a1b`), read by the area readers without a clause and with no second review (docs/05 §8), and M34's two chapter deliveries, `ch12-14-mark` (`daf31d8`) and `ch19-mark-stage` (`2ee5bf5`). `kit-2026-10-26` was committed before the base and read by m33-review; C2 tests its result at the end commit.

**End.** The commit HEAD is when the reading starts, recorded before any reader; this page and its mark, uncommitted, are read from the working tree as the spec.

**Areas.** `git diff --stat -M <base>..<end>` at the end commit, every path placed in an area of docs/05 §5's Milestone review slot:

* **Build:** no path of the `Makefile`, `scripts/`, the READMEs, `VERSION` or `docs/manuals/`; no reader.
* **The kit's skills:** no path; no reader.
* **Chapters:** `book/{en,pt}/` 07, 08, 09, 11, 12, 13, 14 and 19, sixteen files, split in two readers.
* **The documents:** `docs/03`, `docs/06`, and the four records under `work/done/` the range adds, read with the chapters they describe, docs/04 and docs/05.

**Readers.** Three read-only readers on Opus, then one read-only checker on Opus alone; each launch sets its model to Opus and keeps the session's advisor, at most two run at a time (docs/05 §5):

* pair 1: **chapters 7, 8, 9 and 11** (M33's two finding lines), and **chapters 12, 13, 14 and 19** (M34's deliveries and m33-fixes' items there), both editions, whole at the end commit and by their range diffs, against their pages and the installed scripts;
* then **the documents and records**, against each other, the chapters they describe and docs/04;
* then the checker, on every candidate, every copied note and every lead in one report.

Each reader lists the paths it read and how (whole, diff, grep), and says whether it kept the advisor.

**Slow tests.** None (docs/05 §5's Verify slot).

**Known leads**, given to the checker with the readers' candidates:

* L1, C4 and §6: chapter 19 en :54 has the other session stage its entries again, docs/05 §6 has the person do it (the note of `ch19-mark-stage`).
* L2, the M33 fixes: m33-review's six medium findings (chapter 11's findings and Visual reference, chapter 13's claim, chapter 14's mirror, chapter 7's `· after`, chapter 8's excerpt) and its grave one (chapters 8 and 9 on §4's parallel paragraphs) each read as fixed at the end commit, both editions.

**Mechanical checks**, run by /apply at the end commit:

* The installed `mark.sh` in both skills folders equals the kit's `SETUP.md` §3.8 at `4f5da97` (focus-kit 2026.11.12).
* The installed `mark.sh` run on a scratch repository: one byte changed, the size kept, a refusal writing nothing, and `stage` changing that line alone in the index with a neighbouring line already staged, against chapter 14 :74 to :80 and chapter 19 :370.
* `book/` in both editions searched for a passage outside chapters 12, 13, 14 and 19 that sets a mark or stages a queue line otherwise (a hand edit of the mark, `git add` of docs/06 whole, a patch).
* The repository's tree: `queue.sh trunk` prints M34 with `m34-review` in flight, `git status` the same before and after.
* `make book` with `book/` clean; `make verify` after the last edit.

**States.** Inapplicable: a review, no screen.

**Visual reference.** The two PDFs, `make book` at the end commit.

**Out of scope.**

* Fixing any finding: grave ones become lines, medium ones the `m34-fixes` line (docs/05 §8).
* Re-testing M33's clauses: its fix lines are read by the area readers, not tested by clause.
* Teaching 2026.10.27 to 2026.11.12 in the chapters: M35 to M38's lines.
* Whether the two projects of chapter 14's error are Case A or Case B: the author's answer (docs/05 §5).

**Decisions from the documents.**

* The base is m33-review's commit, `47b35ee`, the first of docs/05 §8's cases.
* No build reader and no kit reader: the range touches neither (docs/05 §8, one reader per area it touches).
* The clause tests, the confirmation and the medium pick are taken on the author's word quoted on this page (docs/05 §8).
* The notes are copied from every page the range delivered (docs/05 §8).

**Decisions taken alone.** The agent chose each of these, for the author's review.

* M34's paragraph is taken as five clauses, by what can be checked.
* The chapters area splits in two, by milestone: M33's fixes in chapters 7 to 11, M34's deliveries in 12 to 19 (docs/05 §8, an area too large for one careful reading).
* A candidate an open M35 to M38 line holds is listed with that line, as m33-review did.
* `ch12-14-mark`'s note on the two projects of the error is copied and marked like any other; its answer stays the author's, outside the word's confirmation.

**Done when.**

* [x] Every line above this review in M34 is `[x]` and committed; every clause has the review's answer, on the author's word quoted on this page.
* [x] Base, end, the inventory by area, each reader's paths read and its advisor, every copied note and candidate with its mark are on this page.
* [x] Every confirmed finding graded; each grave one a `[ ]` line under this review; every medium one an item of the `m34-fixes` line, when any; small ones listed, numbered.
* [x] The mechanical checks recorded; `make book` built both PDFs at the end commit; `make verify` green after the last edit.
* [x] The page in `work/done/`, its paths staged and its commit message suggested.

## Outcome

**Precondition.** Every line above this review in M34 is `[x]` and committed: `kit-2026-10-26` in `cd79120` (before the base), `ch12-14-mark` `daf31d8`, `ch19-mark-stage` `2ee5bf5`; M33's finding lines `ch08-09-parallel-paragraphs` `32d084f` and `m33-fixes` `96a8a1b`. `git log --diff-filter=A -- work/done/m33-review.md` returns `47b35ee` alone.

**Base and end.** Base `47b35ee`; end `2ee5bf5` (`docs(ch19-mark-stage): stage a queue line with mark.sh in chapter 19`), HEAD when the reading started, recorded before any reader. This page and its marks are uncommitted and outside the range.

**Inventory.** `git diff --stat -M 47b35ee..2ee5bf5`: 22 paths, by area. Build: none. The kit's skills: none. Chapters (16): `book/{en,pt}/` 07, 08, 09, 11, 12, 13, 14, 19. The documents (6): `docs/03-Domain.md`, `docs/06-Queue.md`, and under `work/done/` `ch08-09-parallel-paragraphs.md`, `m33-fixes.md`, `ch12-14-mark.md`, `ch19-mark-stage.md`.

**Slow tests.** None (docs/05 §5's Verify slot).

**Mechanical checks**, at `2ee5bf5`:

* The installed `mark.sh`, in `.agents/skills/` and `.claude/skills/`, byte-equal to the kit's `SETUP.md` §3.8 at `4f5da97`.
* The installed `mark.sh` on a scratch repository: two neighbouring lines marked `[*]` then `[x]` with `stage`, one after the other, each `staged: that line alone`, the index holding the two marks and nothing else; the queue's size the same, 116 bytes before and after; an unknown slug and an unknown mark each refused with exit 2, the queue unchanged.
* `book/` in both editions: no passage outside chapters 12, 13, 14 and 19 sets a mark or stages a queue line otherwise; chapter 10 :61 and :67 show the marks without saying how, chapter 16 :92 tells a mark a project added to its process, and chapter 19 :296 to :299 resolve a merge conflict in docs/06 by hand, as docs/05 §4's reconciliation allows.
* The repository's tree, `queue.sh trunk`, exit 0, `git status --porcelain` the same before and after: `milestone: M34. focus-kit 2026.10.26`, `[*] m34-review · in flight: apply`, both free lists `none`, `next: none`.
* `git status --short book/` empty before `make book`; `make book` at `2ee5bf5`, exit 0, 14 seconds: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**The author's word for this review.** Relayed to this session by the agent running the queue on the author's behalf, on 2026-11-12: "Rodar todas, uma por marco" (run every milestone review, one per milestone), "Responder com a recomendada" (answer with the recommended option) and, for the medium pick, "Todos os médios entram" (every medium finding enters). By it, the clause answers below are the review's, from its own reading of both PDFs (`pdftotext -layout`) and of the repository at `2ee5bf5`, never the author's; each candidate the checker marks seen is confirmed, the latent and weak ones listed as dropped; every medium finding enters the `m34-fixes` line (docs/05 §8). The word does not answer N3, below: whether a private case is behind chapter 14's error stays the author's (docs/05 §5, Case A and Case B).

**The clause answers, the review's.** Pages en / pt.

* **C1, the book teaches focus-kit 2026.10.26: holds.** Chapters 12 (en 121 / pt 125), 13 (en 133 to 141 / pt 139 to 147), 14 (en 152 to 153, 162 / pt 160 to 161, 170) and 19 (en 201 to 220 / pt 211 to 230), each passage read in both PDFs teach the mark script as the kit installs it; no other chapter sets a mark or stages a queue line another way (Mechanical checks). The two editions say the same.
* **C2, the repository runs on it: holds.** docs/05 §4 :163 to :167 holds 2026.10.26's two sentences and its provenance paragraph names them; the installed `mark.sh` is the kit's at 2026.11.12; docs/03 :31 holds the mark script row, "script de marca" in Portuguese.
* **C3, a mark changed by `mark.sh`, one byte: holds.** Chapter 12, en 121 / pt 125: `[~]` through the mark script, `[>]` by the script once the page is complete; chapter 13, en 133 / pt 139: the script's line, one byte, nothing else of the queue, and en 135 / pt 141, `[*]` through it as the first edit; chapter 14, en 152 to 153 / pt 160 to 161: the file written beside the queue and renamed over it, the refusal unless the size holds and at most that byte differs.
* **C4, staged with it on its line alone: holds.** Chapter 13, en 139 / pt 145: the last edit marks `[x]` with the mark script and `stage`, which changes that line in the index and nothing else there, and en 141 / pt 147, the walk-through's `[x]` the same way; chapter 19, en 201 to 202 / pt 211 to 212, each session stages its own line with `stage`, and stages it again after `git restore --staged`, en 217 to 218 / pt 227 to 228, in a batch's shared hunk, and en 220 / pt 230, the key point, with no patch and no `git apply`. `stage` stages the mark's byte, not other edits of the line or an added line; a reader meets that only off the usual path (small findings 8 and 9).
* **C5, any other edit to docs/06 by the host's file edit: holds.** Chapter 14, en 153 / pt 160 to 161: every other edit is the host's file edit on the lines it changes, never a program that writes the whole file, with the queue left at zero bytes on 2026-10-18 and 2026-10-26 as the error, and a `[?]` as two edits.

**Readers.** Three read-only readers on Opus, the first two as a pair, the third once the first ended, then the checker on Opus alone; at most two ran at once. Each was launched from this session with its model set to Opus, ran in the background, and delivered its final report to this session as its completion notice, recorded here. Working notes in the session's scratchpad, `m34/`.

* **Reader 1, chapters 7, 8, 9, 11.** Whole: en 07, 08, 09, 11, the pages of `m33-fixes` and `ch08-09-parallel-paragraphs`, `mark.sh`; m33-review's findings; docs/05 §§4, 5 (Git) and 8; pt four by range diff and spot reads; by grep docs/03, docs/04, the template's `documents.md`, the run record, chapters 10, 12 to 15, 18 and 19. Chapter 20 not opened (outside the range). Advisor present, called once.
* **Reader 2, chapters 12, 13, 14, 19.** Whole: en 13, 14, the pages of `ch12-14-mark` and `ch19-mark-stage`, `mark.sh`; en 12 and 19 in parts and by grep; `m33-fixes` in part; docs/05 §§4, 6; docs/04 and docs/03 in part; `claim.sh` in part; range diffs of all eight files; seven scratch runs of `mark.sh`. Advisor present, called once.
* **Reader 3, the documents and records.** Whole: the four pages, the four commit messages, `mark.sh`, `kit-2026-10-26.md`; range diffs of docs/03, docs/06 and the sixteen chapter files; docs/05, docs/04, m33-review and the run record in part; the kit's `CHANGELOG.md` and `SETUP.md` by grep; each range commit's docs/06 compared with its parent's. Advisor present, called once.
* **The checker**, one agent on every candidate, note and lead in one report, each file opened at `2ee5bf5`, two scratch runs of `mark.sh`: 20 seen, 2 latent, 7 weak, 2 held by open lines. Advisor present, called once.

Every path of the inventory was read by at least one reader, by its range diff at the least.

**Notes copied**, verbatim from the `## For the review` headings of the range's pages; the page with none: `ch08-09-parallel-paragraphs`.

* N1 (`m33-fixes`): book/en/21-beyond-software.md:103 (pt the same): the key point "Give every finding a line, or it gets lost." reads, beside chapter 11 and docs/05 §4, as if every kit finding became a queue line; the chapter's findings are those of an analysis outside software, so a person may read it either way.
* N2 (`ch12-14-mark`): book/en/12-propose.md:194-199 and book/pt/12-propose.md: six key points, docs/04 allows five; a reader sees one bullet more than every other chapter; older than this delivery, which only edited bullet 2.
* N3 (`ch12-14-mark`): work/done/ch12-14-mark.md, Decisions: the two projects of the error are told as the kit's changelog leaves them, unnamed; if either is Case A or Case B, the passage needs the author's approval (docs/00 OD-3).
* N4 (`ch19-mark-stage`): book/en/19-worktrees.md:55 and docs/05-Process.md §6 ("commits the first, and stages them again"): the chapter has the other session stage its entries again, §6 has the person do it, and a queue line goes back into the index only through the mark script's `stage`, which a session runs; the person may align §6 with §4 and the chapter in the kit or by ADR.

**Candidates.** The checker's marks, lines at `2ee5bf5`, en with pt the same unless given; `=` joins duplicates, graded once.

| Id | Where | Candidate | Mark |
|---|---|---|---|
| R1-1 | ch08 :59; ch09 :27 to :29 | The parallel paragraphs "only where sessions will run at the same time", while a branch per delivery, sequential work, also gets them | seen |
| R1-2 | ch09 :29 | A one-session team "does not read" rules for sessions it never runs | weak |
| R1-3 | ch07 en :81 / pt :82; ch18 :186 | A free line "needing no other line done first, defined yet or not", against `after` read per command | seen |
| R1-4 | ch11 en :74, :78, :80 / pt :77, :81, :83 | A grave finding sent to the next milestone; docs/05 §4 keeps it in its own | seen |
| R1-5 | ch11 en :181 / pt :186 | "Only a fix the delivery needs first goes above" | weak |
| R1-6 | ch08 en :92 / pt :93 | "Only a grave one becomes a queue line" against the fixes line | weak |
| R1-7 | ch11 en :97, :100 / pt :100, :103 | "Its findings stay ... under the review line" | seen |
| R1-8 | ch07 en :63 to :64 / pt :64 to :65 | "It is the document you touch most" after the `· after` sentence | seen |
| R1-9 | ch08 :59 | A fourth "(chapter 9)" pointer | seen |
| R1-10 | ch08 en :66 to :80, :96 / pt :68 to :81, :97 | The excerpt's heading (weak) and its order, section numbers first (seen) | seen |
| R2-1 | ch13 :126, :154, :293; ch14 en :77 / pt :78; ch19 :29, :387, :415 | `stage` stages the mark's byte, not other edits of the line | seen |
| R2-2 | ch13 :34, :126; ch14 :77; ch19 :29, :370 | `stage` refuses a line not yet in the index after writing `[x]` | seen |
| R2-3 | ch13 :153 to :154; ch19 :54 | An added line, then "that line of docs/06 alone" | held by `ch13-apply-findings`; the wording ⊂ R2-1, R2-2 |
| R2-4 | ch12 :30 to :32; ch13 :27, :34; ch14 :74 | In worktrees the mark line run from `main/` marks main's queue | seen |
| R2-5 = R3-4 | ch14 en :71 / pt :72 | The error's two dates without a source | weak |
| R2-6 = N4 = L1 | ch19 :55; docs/05 §6 | Who stages the other session's entries again | seen |
| R2-7 | ch13 :30 to :31 | The claim with a local branch, no worktree folder and no remote branch | seen |
| R2-8 | ch19 :29 | A fourth pointer to chapter 14 | seen |
| R3-1 | `m33-fixes.md` :56, :68 | Delivery review ticked as docs/05 §5 says, docs/04 not opened | seen |
| R3-2 | `m33-fixes.md` :35 | M6's line numbers are the base's | seen |
| R3-3 | docs/06 :751 | `ch19-mark-stage` without `· after ch12-14-mark` | latent |
| R3-5 ⊂ N3 | `ch12-14-mark.md` :61, :89 | "Case A or Case B", Case B never ran on the process | seen |
| R3-6 | two pages' Outcome | The delivery review's advisor unrecorded | weak |
| R3-7 | docs/05 :231 to :232, :323 | "Its own hunk of docs/06" against the template's "its own lines" | seen |
| R3-8 | `mark.sh` :10 to :12; docs/03 :31 | The refusal of a second start untaught | held by `ch12-14-mark-refused` |
| N1 | ch21 :103 | "Give every finding a line" | seen |
| N2 | ch12 en :194 to :199 / pt :203 to :208 | Six key points (chapters 1, 21 and 24 have more than five too) | seen |
| N3 ⊃ R3-5 | `ch12-14-mark.md` | The error's projects possibly a private case | latent, for the author |
| L2 | m33-review's G1, M1 to M6 | Any not fixed | weak, all fixed in both editions |

**Findings.** By the author's word, every candidate marked seen is confirmed; the latent and weak ones are dropped and listed under small (docs/05 §8). R2-3 and R3-8 are held by open lines, no finding here.

*Grave*: none. Every clause holds, nothing loses or exposes data, and verify is green.

*Medium*, met in ordinary reading while the clauses hold, each an item of `m34-fixes` by the author's word:

1. M1, R1-3: chapter 7 en :81 / pt :82 and chapter 18 :186 define a free line as needing no other line done first, defined yet or not, against `after` read per command (chapter 7 :63, chapter 11 :89, docs/03's free line row).
2. M2, R1-4: chapter 11 en :74, :78, :80 / pt :77, :81, :83 send a line no clause needs to the next milestone with only the review's own findings excepted, while docs/05 §4 keeps a grave finding in its milestone too; no open line names chapter 11.

*Small*, each a rare case, a wording a reader rarely meets, off-trunk work, or a record's precision:

3. R1-1: chapter 8 :59's "only where sessions will run at the same time" leaves out the branch per delivery chapter 9 :28 names.
4. R1-7: chapter 11 :97, "under the review line" for findings that stay on the page.
5. R1-8: chapter 7 :63 to :64, "It" after the `· after` sentence.
6. R1-9: chapter 8 :59, a fourth pointer to chapter 9.
7. R1-10: chapter 8's excerpt puts section numbers first, which the run record lists later; :96's ordering unsourced.
8. R2-1: `stage` stages the mark's byte; a line's other edits wait for the hunk, which a neighbour's line can block (chapter 19 :369).
9. R2-2: `stage` on a line not yet in the index writes `[x]` and refuses, exit 2.
10. R2-4: in worktrees the chapters never say the mark line runs at the worktree's path.
11. R2-6 = N4: chapter 19 :55 against docs/05 §6 on who stages again.
12. R2-7: chapter 13 :30 to :31, the claim's rare case of a local branch without folder or remote.
13. R2-8: chapter 19 :29, a fourth pointer to chapter 14.
14. R3-1: `m33-fixes` ticks its delivery review though docs/04 was not opened.
15. R3-2: `m33-fixes` :35's line numbers are the base's.
16. R3-5: `ch12-14-mark` names Case B as possible behind the error, which never ran on the process.
17. R3-7: docs/05 :231 and :323, "its own hunk of docs/06", where the template now says its own lines.
18. N1: chapter 21 :103's key point beside the graded findings.
19. N2: chapter 12's six key points, with chapters 1, 21 and 24.
20. Dropped, latent: R3-3, N3. N3 stays a question for the author: whether either project of chapter 14's error is Case A or Case B (docs/05 §5); the repository holds no trace of either.
21. Dropped, weak: R1-2, R1-5, R1-6, R2-5 = R3-4, R3-6, L2.

**Proof.** The mechanical checks and the clause answers above; `make book` at `2ee5bf5`; `make verify` green after the last edit to this page and docs/06, 15 seconds, under the five-minute ceiling.

**The medium pick.** By the author's word quoted above, M1 and M2 enter the one `m34-fixes` line, each an item of its page, which is their list and is not split; no small finding is picked, so none becomes a line (docs/05 §8). The line sits under this review, `· after m34-review · from m34-review`.

The author authorized one commit per slug for this run; this /apply commits this delivery itself, with the message below, and never pushes.

```commit
docs(m34-review): review M34, five clauses hold, two medium fixes

- Base 47b35ee, end 2ee5bf5; every clause of M34 holds in both PDFs
- mark.sh equal to the kit and run on a scratch repository
- Three readers and a checker: 20 seen, 2 latent, 7 weak, 2 held
- m34-fixes under m34-review with the two medium findings

work/done/m34-review.md
```

**Decisions taken alone in /apply.** For the author's review.

* The readers ran in the background and reported by completion notice, as m33-review's did; the third launched once the first ended, so two never ran with a third.
* The checker's grades are taken as they stand: R2-1 and R2-2 small, since staging the hunk first, as chapter 13 :124 says, works on the usual path, and only a neighbour's shared hunk blocks it.
* The weak R2-5 = R3-4 is dropped; the dates stay as `ch12-14-mark` decided, the error told in the present first.
