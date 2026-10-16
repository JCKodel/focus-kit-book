# m13-review

**Objective.** The author knows, clause by clause, whether M13's paragraph holds in the hands of a reader of the book and in this repository, in both editions, and the two findings the author named while defining this review, a book that compares focus-kit with its earlier versions and passages heavy with numbers, are `[ ]` lines in M13 under this review.

**Decided from the documents.**
1. The person tests alone; no agent proposes findings for the clause table. The agent prepares, records and writes the lines (docs/05 §8; `m12-review` did the same).
2. The paragraph's first clause has two halves: the book teaches the kit, which the chapters answer, and the repository runs on it, which `kit-2026-10-16` answers, tested by opening this repository's documents, not the PDF (docs/05 §8; `m12-review` decision 2).
3. F1 and F2 below are findings already, in the author's words in this /propose ("O livro não pode ter texto massante com vários números nem manter coisas 'como era antes' e 'como é agora'. O livro é um retrato da versão atual do focus-kit, não um change-log."): nothing to confirm in the review, only the wording of their lines. They follow `book-is-kit-today` (the author's rule while defining `ch15-24-apply-reads`), which no document holds yet; F1's delivery writes it in docs/04.
4. F1 reaches every chapter, not only M13's (the author's answer here). A number about what the kit does stays when it is about the current version; what goes is the kit compared with an earlier version of itself: a changelog entry by date or version, "before that rule", a measure taken before and after a kit change (the author's answer here). Chapter 11's update report stays: it is what the update command prints today, and its versions are its output.
5. F2 reaches the whole book, every number, chapter 9's and 24's included (the author's answer here). Which passages read as a run of numbers is decided in F2's own /propose, with the author.

**Behaviour.**

* The author receives both PDFs (`make book`), the page where each passage below starts in each PDF, and the clause table, and tests each clause by reading the passages it names, in English and then in Portuguese; C1's second half by opening the files it names.
* For each clause the author answers, in the conversation, `C<n>: holds` or `C<n>: fails, <what the reader does not get>`; a clause that fails is a finding.
* F1 and F2 become `[ ]` lines in M13 under `m13-review` with the wording in Contract, shown to the author with the others before staging; the author may reword them.
* Each other finding becomes one `[ ]` line the same way, saying what will be true, never how to fix it. No M13.1.
* A defect the author finds outside the clause table becomes a line the same way, when the author asks for it.
* An answer missing for some clauses: the page records the answers given, the line waits as `[?]` with `· resume: apply · blocked: <clauses> not answered`, and nothing is staged (docs/05 §4, §6).
* No file under `book/` and no document but docs/06 and this page is edited by this delivery.

**Contract.**

The clause table, what the author tests (M13's paragraph, quoted: "When this milestone closes, the book teaches focus-kit 2026.10.16 and the repository runs on it: a worktree per delivery in a container folder, /apply reading only its own queue lines, a queue line as mark, slug, one sentence and suffixes, a slot as what and the command, a manual for a proof on another machine, and a request that continues as /propose in the same session."):

| | Clause | Answered by | Passage (en lines; pt the same save chapter 13, +2 from line 12) | How the author tests it |
|---|---|---|---|---|
| C1 | the book teaches focus-kit 2026.10.16 and the repository runs on it | `kit-2026-10-16`; every chapter line of M13 | 11 §What an update reports (41 to 94). Repository: docs/05 §4, §5 (every slot), §2; `AGENTS.md`; `docs/manuals/`; docs/06's header | Does the book teach what 2026.10.16 asks? Does each rule below stand in this repository's docs/05 and `AGENTS.md` as the chapter teaches it? |
| C2 | a worktree per delivery in a container folder | `ch21-container` | 21 §Worktrees in the kit (184 to 198), §The life of a worktree (114 to 183) | Can a reader say where the kit puts a delivery's worktree, why one shape for every tool and person, and how to find it again? |
| C3 | /apply reading only its own queue lines | `ch15-24-apply-reads` | 15 §What it reads (18 to 25); 24 §Why the page and the documents keep sessions small (63 to 73) | Can a reader say which lines of the queue `/apply` reads, and why it reads no more? |
| C4 | a queue line as mark, slug, one sentence and suffixes | `ch13-short-lines` | 13 §The line (12 to 27), §Changing the queue (95 to 119) | Can a reader write a line, and say where the detail of a request goes instead? |
| C5 | a slot as what and the command | `ch10-12-slots-manuals` | 10 §The seven documents (19 to 44, line 37 the slot); 12 §What it writes, and where it stops (51 to 60) | Can a reader say what a slot holds, and where its steps and its history go? |
| C6 | a manual for a proof on another machine | `ch10-12-slots-manuals` | 10 §Manuals (71 to 85); 12 §`/analyze` (79 to 113), §Review before you commit (138 to 154) | Can a reader say that a manual also holds a proof `/apply` runs on another machine, and who writes it? |
| C7 | a request that continues as /propose in the same session | `ch13-short-lines` | 13 §Changing the queue (95 to 119); 19 §The manager's session (110 to 135) | Asked for a small change in an ordinary session, does a reader know the two ways on: a `[ ]` line, or `/propose` in the same session? |

Line numbers are those of `book/<edition>/NN-*.md` at the start of this delivery; the PDF pages are given by /apply from `make book`.

The findings already decided, in docs/06 under M13 (F1 and F2 first, then the clause findings):

```
[x] m13-review               the review of M13 as docs/05 §8 says
[ ] kit-as-it-is             the book describes focus-kit as it is today, never comparing it with an earlier version of itself, and docs/04 says so; both editions
[ ] plain-numbers            no passage of the book reads as a run of numbers: each keeps the numbers that prove its point; both editions
[ ] <slug>                   <what will be true>
```

F1's passages as found while defining this review, for its own /propose (en; version or entry named, or a before and after): 10 lines 144 and 147; 11 lines 87, 88, 93, 141, 143, 146; 13 lines 127 to 134; 14 lines 148 to 150; 15 lines 183 to 186; 16 lines 15, 16 (the version the book follows, already stale at 2026.10.13), 126; 17 line 69; 18 line 62; 19 line 117; 21 lines 65, 197, 281, 282; 22 line 66.

docs/06: `m13-review` `[>]` now, `[*]` when /apply starts, `[x]` by /apply; its description stays.

docs/03, docs/04, docs/05: no change in this delivery; F1 writes the rule in docs/04.

**Out of scope.**

* Fixing any finding, F1 and F2 included: each is its own line.
* Choosing F2's passages: its own /propose, with the author (decision 5).
* Chapters other than 10, 11, 12, 13, 15, 19, 21 and 24 for the clause table: M13 changed only those.
* The rest of those chapters: a finding only if the author says a clause fails on it.

**Done when.**

* [x] `make book` run; both PDF paths given to the author with the clause table and the page where each passage starts in each edition.
* [x] C1 to C7 each answered by the author, recorded under What happened in the author's words.
* [x] F1, F2 and each failed clause a `[ ]` line in M13 under `m13-review`, approved by the author.
* [x] No file under `book/` changed.
* [x] `make verify` green, disclosure scan included.
* [x] Page in `work/done/`, `m13-review` `[x]`, staged, commit message suggested in a `commit` block.

**What happened.**

* `make book` run; the author got both PDFs, the clause table and the page where each passage starts in each edition (English / Portuguese): chapter 10 §The seven documents p. 72 / 76, §Manuals p. 74 / 79; chapter 11 §What an update reports p. 82 / 86; chapter 12 §What it writes, and where it stops p. 90 / 95, §`/analyze` p. 91 / 96, §Review before you commit p. 94 / 99; chapter 13 §The line p. 97 / 103, §Changing the queue p. 100 / 106; chapter 15 §What it reads p. 113 / 119; chapter 19 §The manager's session p. 144 / 152; chapter 21 §The life of a worktree p. 162 / 171, §Worktrees in the kit p. 164 / 173; chapter 24 §Why the page and the documents keep sessions small p. 183 / 195. The line numbers in Contract matched both editions at the start.
* The author's answers, in their words:
  * C2: "o capítulo explica o que é um worktree depois de mencionar ele no começo do capítulo, o que é um pouco estranho". Confirmed in the text: the opening (line 4) and §When a worktree still pays (line 74) use the word before §What a worktree is (line 88), in both editions. The author confirmed it as C2 failing, with the line's wording: "Sim".
  * C1, C3, C4, C5, C6, C7: "o resto está ok"; each holds.
* Findings, `[ ]` lines in M13 under `m13-review`, approved by the author: `kit-as-it-is` (F1), `plain-numbers` (F2), `ch21-worktree-first` (C2). No defect named outside the clause table. No M13.1; M13 closes when the three are `[x]`.
* Nothing diverged from the plan. No file under `book/` changed; no ADR, no manual, no document but docs/06 and this page.

```commit
docs(m13-review): review M13 clause by clause; three findings

- C1 to C7 tested by the author in both PDFs; C2 fails, the rest hold
- findings queued under M13: kit-as-it-is, plain-numbers, ch21-worktree-first

work/done/m13-review.md
```
