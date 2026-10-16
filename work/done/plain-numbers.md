# plain-numbers

**Objective.** A reader of either edition meets, in chapters 3, 9, 24 and 26, each claim with the number that proves it and no run of numbers around it, and docs/04 holds the rule so later deliveries keep it.

**Decided.**
1. The passages are chapters 26, 24, 9 and 3, chosen by the author in this /propose from the candidates the agent found by counting numbers per paragraph; chapter 5's benchmark (lines 103, 187), chapter 21's parallel run (line 277), chapter 1's METR and DORA, chapters 13, 18, 23 and the prologue (line 58) stay as they are. This closes the deferral `kit-as-it-is` left to this line (its Out of scope).
2. What stays, the author's answer: each claim keeps the number that proves it; the detail of the measurement (per-arm seconds and tokens, arithmetic, sub-sample counts, a fact said twice in two numbers) leaves the text and stays at the source the note already points to. No number is rounded or invented to replace one.
3. Repetition, the author's answer: `## What the team gains` gives the one number that sums the chapter; each key point carries at most that number. Measured numbers only: "four kinds of token" or "four turns" are counts of things taught, not measures.
4. The rule goes in docs/04 §Writing the book, as `kit-as-it-is` did (the author's answer).
5. Chosen on the author's behalf, to question in review: chapter 24's second table becomes one sentence that keeps the method, each total divided by the 93 pages, because the chapter asks the reader to repeat the count (docs/04, a parenthesis "where the method matters to a reader repeating a count"); chapter 3's gain keeps its pair, 37,228 lines of spec for four screens against 22,650 lines in 93 pages for the whole product, because that pair is the gain (docs/00 product question 7), and only "fifteen days", which chapter 9 owns, leaves it.
6. No `check_prose.py` rule: no count of numbers per line separates a run from chapter 1's proof, which the author keeps (docs/05 §7).
7. No Case A or Case B passage changes; no OD-3 approval is needed. Ninjobs' numbers are kept or cut, never reworded into new claims.

**Behaviour.**

* Chapter 26 §Why the first answer feels final: Skitka keeps "right 59% of the time against 97% without it" and "all but one participant followed at least one" of the six wrong recommendations, without the missed 41% against 3% (the same fact) and without the average of 65%; Randazzo keeps 244 consultants, 27% who handed the task over and 44% of those who took it unchanged, without "(63)" and "(28 of 63)"; Dell'Acqua keeps, inside the frontier, 25.1% faster with quality up 29.9% to 33.9%, without 12.2% more tasks, and outside it 19 percentage points less likely to be correct, without 60%, 70.6% and 84.5%. Lee's 319, 44 and 72 stay.
* Chapter 26 §What the protocol bought, and what it cost: the reader reads that the challenged sessions took 2.9 to 8.8 times as long and wrote 2.7 to 9.4 times the output tokens, and the per-session 24 seconds to just over 2 minutes against 3 to 9 minutes, with no seconds or tokens per arm. The cost arm's use reads: all 30 answers correct; in every run the challenged setup answered in 14% to 26% less time, and wrote fewer output tokens in two runs and 9% more in the third. The table, the 1-to-5 scoring, the session-limit story and the limits stay.
* Chapter 26 key points: the fourth says "Are you sure?" invites sycophancy, a new answer chosen to please, without 32% to 86% (which stays in §Turn 2); the fifth keeps 9 of 9 and 3 to 9 times, the gain's number.
* Chapter 24 §What a delivery cost on Ninjobs: the first table (four kinds, 21 days) stays; the second table, with its Arithmetic column, becomes one sentence: divided by the project's 93 finished pages, 43.1 million tokens per delivery, 149 thousand of them output and 738 thousand without cache reads. "Forty-three million tokens reads as a lot" and §Why cache reads are counted apart, with its one division, stay.
* Chapter 24 §What the team gains gives 43.1 million tokens per delivery, without 149 thousand, 738 thousand and 93; key point 2 reads one delivery cost 43.1 M tokens, nearly all of them cache reads, without 98.3%, 149 k, 738 k and 93.
* Chapter 9's opening paragraph of the story reads fifteen days, 37,228 lines of spec, four screens and one table of data, without 87 commits and 35 changes; 29 checks and the restart's date, 91 deliveries and 19 boards in §the restart stay.
* Chapter 9 §What the team gains reads the old process gave four screens in fifteen days and one page per delivery gave the public opening in thirteen, with no recount of six places, 29 checks, 91 deliveries and 19 boards; key point 1 keeps four screens in fifteen days and names the causes without "six places" and "29 checks".
* Chapter 3 §Where the cost of many places begins keeps the three counts (8 files and 756 lines, 6 and 180, 1 page of 82) and the 8 of 8 and 4 of 6, and says the rule restated is read in each place and changed in each, without "8 times" and "8 places" again. §What the team gains keeps its pair without "fifteen days"; key point 4 says Spec Kit and OpenSpec wrote a folder of files where focus-kit wrote one page, without 8, 6 and 1.
* Checks, both editions (en / pt formats): `grep -nE "87 commits|35 (changes|mudanças)|1[,.]337|147[,.]419|24[,.]220|68[,.]989|110[,.]334|271[,.]807 \+|68[,.]671[,.]657|12[,.]2%|70[,.]6%|84[,.]5%|28 (of|de) 63|\(63\)" book/*/[0-9]*.md` finds nothing; `43[,.]1` appears only in chapter 24: the sentence that replaces the second table, the gain and key point 2.
* Each `[^...]` key of the four chapters keeps a reference and each reference its definition (`[^skitka-1999]`, `[^randazzo-hbs-26-036]`, `[^dell-acqua-2026]`, `[^ask-for-more-run]`, `[^spec-driven-run]`); `make verify` fails otherwise.
* Fails: a sentence that keeps a cut value in one edition only; a number rounded to replace one cut; a gain or key point that lists more than the chapter's one number; a claim left with no number where it had one that proved it.

**Contract.**

Sections touched (en lines at the start; pt the same sections, chapter 24 offset by 2 after its first table):
3 §Where the cost of many places begins (63 to 65), §What the team gains (72 to 75), key point 4 (86). 9 the story's opening (12), §What the team gains (78 to 80), key point 1 (84). 24 §What a delivery cost on Ninjobs (39 to 45), §What the team gains (136), key point 2 (142). 26 §Why the first answer feels final (33, 34, 42, 45, 46), §What the protocol bought, and what it cost (129 to 131, 140), key point 4 (161).

docs/04 §Writing the book, after **The kit as it is**, a new bullet: **Numbers that prove.** A passage keeps the numbers that prove its point and no more: the detail of a measurement (per-run values, arithmetic, sub-sample counts, one fact said in two numbers) stays at the source the note points to or in the run's record. `## What the team gains` gives the one number that sums the chapter, and each key point carries at most that number (first: `plain-numbers`, from `m13-review`).

docs/06: this line `[>]`, `[*]`, `[x]`. docs/03: no new term. No ADR.

**Out of scope.**

* Chapters 1, 5, 13, 18, 21, 23 and the prologue: the author kept them (decision 1).
* `ch21-worktree-first`: its own line; it touches chapter 21 only, which this page does not.
* The run records in `work/done/*-run/`: they keep every number the text drops.
* A prose check for runs of numbers (decision 6).
* The 91 of chapter 9 against the 93 of chapters 3 and 24: deliveries at the opening and pages at the count, both real; not a run of numbers.

**Done when.**

* [x] Both editions changed in every section of Contract; the checks of Behaviour hold in `book/en` and `book/pt`.
* [x] docs/04 holds **Numbers that prove**.
* [x] Each chapter touched still opens with its value, keeps its gain with its number, no filler and nothing useful cut.
* [x] Every number left is sourced as before; no note definition left without a reference.
* [x] `make verify` green, disclosure scan included.
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, line `[x]`, staged, commit message in a `commit` block.

**Tree before editing (docs/05 §6).** `M docs/06-Queue.md` (this line `[>]`, from this delivery's /propose) and `?? work/plain-numbers.md`; nothing staged, nothing unrelated.

**Built.** Every section of Contract, in both editions. Chapter 26 keeps each study's claim with its number (Skitka 59% against 97% and all but one following a wrong recommendation; Randazzo 27% and 44%; Dell'Acqua 25.1% faster with quality up 29.9% to 33.9%, and 19 points less likely to be correct), the protocol's cost as 2.9 to 8.8 times the time and 2.7 to 9.4 times the output tokens, and the cost arm's use in one sentence. Chapter 24's second table is one sentence with its method, each total divided by 93. Chapter 9's story opens with fifteen days, 37,228 lines, four screens and one table. Chapter 3 says a restated rule is read and changed in each file. Gains and key points carry each chapter's one number. docs/04 §Writing the book holds **Numbers that prove**.

**Divergences.**
* Chapter 9's gain also leaves out 37,228 lines, which Behaviour did not name: the gain's one number is four screens in fifteen days against the opening in thirteen, and the 37,228 lines stay in the story's opening and in chapter 3's gain, where they are the pair.
* Chapter 9's gain and key point 1 say "many places" and "checks" (pt "muitos lugares", "verificações") where they said six places and 29 checks, so the causes stay named; the counts stay in the story.
* Dell'Acqua's outside-the-frontier sentence now ends "than those without it" (pt "do que quem não tinha"), the comparison its cut percentages carried.

**Proof.**
* The grep of Behaviour finds nothing in `book/en` and `book/pt`; `43[,.]1` appears only in chapter 24 lines 39, 130 and 136 (pt 39, 132 and 138): the sentence that replaces the table, the gain and key point 2.
* Every note key of chapters 3, 9, 24 and 26 keeps a reference in both editions (`[^sharma-2024]` stays referenced in chapter 26 §Turn 2).
* `make verify` green, disclosure scan included; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Decisions.** Decision 5 held as chosen. No Case A or Case B passage changed, so no OD-3 list. No line in docs/06 waits on this one.

```commit
docs(plain-numbers): keep the numbers that prove each claim
- chapter 26: each study keeps its claim's number; no per-arm seconds or tokens
- chapter 24: the per-delivery table becomes one sentence with its method
- chapters 3 and 9: no count said twice; gains carry one number
- docs/04: numbers that prove, a rule of writing the book
work/done/plain-numbers.md
```
