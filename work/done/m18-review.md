# m18-review

**Objective.** The author knows, clause by clause, whether M18's paragraph holds in the hands of a reader of the book, in both editions, having read in both PDFs the passages this page names, and whether everything changed since `a60d8f1` holds under the code reading by areas; each clause that fails, each fault the reading finds and each candidate the author confirms is a `[ ]` line in M18 under this review.

**Decided from the documents.** Each decision below names its source, so the author corrects it in the review of this page.

1. The person tests the clauses alone. The agent prepares the clause table, the PDFs and the page numbers, records the answers and writes the lines (docs/05 §8; `m17-review` decision 1).
2. The base is `a60d8f1`, `docs(m17-review): review M17, fourteen findings`, the commit of the previous milestone's review (docs/05 §8). The range from it holds, besides M18's 23 lines, the fifteen fixes of M17's findings (`conflict-same-lines` to `docs05-four-cases-sentence`, and `pt-ch19-index-word`, queued from a delivery review) and two commits outside any delivery: `bbe1347 infra: claude settings` and `8507633 style(code-blocks)`. Those fixes get no clause here, since M17's paragraph is not this milestone's; the code reading reads their files, and a fault it finds there is an M18 finding (docs/05 §8, "get no second review"; `m17-review` decision 2).
3. The author's test by hand is the passages the clause table names, in both PDFs (docs/05 §8). In `m17-review` the author waived that reading and took the clauses as holding; that was M17's choice, and §8 still asks for it, so this page asks for it again and the author decides at /apply. A fault found outside the passages is given as `outside:` and is a finding too.
4. The clauses. M18's paragraph names six results, each answered by one or two lines, and closes with "every passage the author's reading marked says what the author means", which covers the rest. That last clause is tested line by line, one row per line (C7a to C7p), because §8 tests "the passages the page names" and a single row for seventeen lines names none. Five of those lines were not marked in the author's reading but came later, from a delivery review or the author's word: `ch14-face-prototype`, `try-before-commit`, `ch19-agent-does-git`, `ch19-git-step-wording` and `docs04-code-layout`. This page reads the paragraph's last clause as covering them, since the paragraph names no other home; if the author reads it otherwise, the paragraph changes by conversation and those rows leave the table.
5. What the code reading reads, by docs/05 §5's Milestone review slot's areas, from `git diff --stat a60d8f1..HEAD` at `48de1c5` (82 files) at this /propose; /apply reruns it and adds what later commits changed:
   * the build: no file in the range (`scripts/`, `Makefile` and `mkdocs.yml` unchanged), so no reader;
   * the kit's skills: no file in the range (`.claude/skills/` and `.agents/skills/` unchanged), so no reader;
   * the chapters, 36 files, in four readers (docs/05 §8, "an area too large for one careful reading splits again"), each Portuguese file against its English one:
     * chapters 0 to 3, 8 files: `book/en/` and `book/pt/` 00, 01, 02, 03, read whole;
     * chapters 4 to 7, 8 files: `book/en/` and `book/pt/` 04, 05, 06, 07, read whole;
     * chapters 8 to 15, 12 files: `book/en/` 08, 11, 13, 14, 15 and `book/pt/` 08, 09, 11, 12, 13, 14, 15; 11, 13 and 14 read whole, the others by their range diff and the sections around it;
     * chapters 16 to 22, 8 files: `book/en/` 18, 19 and `book/pt/` 16, 17, 18, 19, 21, 22; 18 and 19 read whole, the others by their range diff and the sections around it;
   * the documents, 5 files: docs/03, docs/04, docs/05, docs/06, and `.claude/settings.json` (the one infrastructure file, read against docs/01).

   Not read: `work/done/` (40 files in the range, the record of what happened, among them two pages `8507633` re-laid out) and `work/kit-proposals.md`, notes for focus-kit's own repository, not a delivery (`m17-review` decision 4). A fault in the kit's own wording is fixed in the kit on the author's word, not here.
6. What the readers look at first, since the reading's value is one delivery against another: places where two lines of this range landed in one passage. Chapter 13's §Review the staged change, where `try-before-commit` and `ch13-teach-the-agent` sit next to each other; chapter 19's §Worktrees in the kit, written by `ch19-agent-does-git` and rewritten by `ch19-git-step-wording`, with chapter 18's gain; chapter 5's §A test for each piece against §Swap only I/O and what changes between runs (`ch05-test-time`, `ch05-random-values`); chapter 7's opening, §One place per fact and §Living documents (`early-no-forward-links`, `ch07-rag-and-numbers`, `ch07-talk-not-edit`); chapter 4, where five lines and `8507633` landed; chapter 11's §Size and order against §Changing the queue and the key points (`ch11-queue-grows`, `ch11-agent-runs-propose`); chapter 19's §What is and is not a conflict there and §Proposing in a batch (`conflict-same-lines`, `ch19-adjacent-mark-staging`) against docs/05 §4.
7. How it runs is as docs/05 §5's Milestone review slot and §8 say: on the author's word in the review's /apply session, five read-only agents on Opus, one per reader of decision 5, then one read-only checker on Opus that labels each candidate seen, latent or weak. Each launch sets its model to Opus, every agent keeps the session's advisor, and at most two run at a time. The author confirms which candidates count; confirmed ones become one line per fact: a chapter's two editions are one line, and a fact that stands in several files is one line (`m17-review` decision 5).
8. Known candidates, from searches at this /propose:
   * K1. `8507633 style(code-blocks)` is a commit outside any delivery that re-laid out code examples in chapters 3, 4 and 5 and in two `work/done/` pages; `docs04-code-layout` wrote its rule into docs/04 afterwards. The author says whether it counts. Assessment: not a finding, since the rule now lives in docs/04 and the code reading reads those chapters.
   * K2. `work/kit-proposals.md` item 3 says the kit's `references/documents.md` points to a removed chapter slug. Assessment: the kit's own wording, fixed in the kit (decision 5), not a line here.
   * Searched and clean: "a Ninjobs", "da Ninjobs", "na Ninjobs", "pela Ninjobs" in `book/pt/` and docs/03 (none); "bibliotecária" in `book/pt/` (none); "chapter N" in `book/en/` 00 to 07: every forward pointer sits in a gain section (00 §What the team gains, 02 §What the team gains); every other hit points back. No whitespace-only line is left in any chapter.
9. Each finding becomes one `[ ]` line under this review, saying what will be true and not how. There is no M18.1 and no second review of a finding's fix (docs/05 §8). Every `after` of this line is `[x]`, so the line goes to `[>]` and /apply starts it at `[*]` (docs/05 §4).
10. This definition stages nothing (docs/05 §6: the page and its line are staged with the delivery). This /propose wrote only this page and the line's mark.

**Behaviour.**

* At the start of /apply the author receives both PDFs (`make book`), the page where each passage below starts in each PDF, the cover counted as page 1, and the clause table. The author reads the passages in both PDFs, English first, and tests C1 to C7p.
* For each clause the author answers `C<n>: holds` or `C<n>: fails, <what the reader does not get>`. A clause that fails is a finding. A fault the author finds elsewhere is given as `outside: <chapter or file>, <what>` and is a finding too.
* C7p is tested by the author opening docs/04 as well as the PDF.
* The author may waive the PDF reading, as in `m17-review`. The page then records the waiver as a divergence and the answers the author gives.
* On the author's word, the code reading runs as decision 7 says, against `a60d8f1`, over decision 5's paths. Each reader's report lists the paths it read, and the candidates, once checked, are shown grouped by area, with K1 and K2 among them (C8). The author names the ones that count.
* Each finding becomes one `[ ]` line in M18 under `m18-review`, shown to the author before staging. The author may reword it.
* Edge: the author does not give the word for the code reading. Nothing is launched, C8 stays unanswered, and the line waits as `[?]` with `· resume: apply · blocked: code reading not started`.
* Edge: the paths the reports list, taken together, are fewer than decision 5's (a reader that covered only part of its area, a run cancelled or stopped by a usage limit). The page records what was read and what was not, C8 stays unanswered, and the line waits as `[?]` with `· resume: apply · blocked: <what was read>` (docs/05 §8).
* Edge: commits land after this page. /apply reruns `git diff --stat a60d8f1..HEAD`, and the areas take the paths it adds; a path in the build or the kit's skills gets its reader.
* Edge: some clauses have no answer (the reading not finished). The page records the answers given, the line waits as `[?]` with `· resume: apply · blocked: <clauses> not answered`, and nothing is staged (docs/05 §4, §6).
* No file under `book/` and no document except docs/06 and this page is edited by this delivery.

**Contract.**

The clause table is what the author tests. M18's paragraph, quoted: "When this milestone closes, a reader of chapters 0 to 7 learns each idea where it is named instead of being sent to a later chapter, a Portuguese reader reads "o Ninjobs", a reader with little TypeScript reads chapter 3's refusal without seeing a magic string, a team reads FOCUS as optional before deciding to adopt it, keeps its tests fast, and teaches the agent by talking to it instead of fixing its work by hand, and every passage the author's reading marked says what the author means."

Passages are named by chapter and section, the same in both editions; /apply adds the PDF pages.

| | Clause | Answered by | Passage (pt the same sections) | How the author tests it |
|---|---|---|---|---|
| C1 | a reader of chapters 0 to 7 learns each idea where it is named | `early-no-forward-links` | chapters 0 to 7, read straight through; their gain sections | Reading chapters 0 to 7 in order, is any idea named before it is explained in a few words? Does any pointer to a later chapter sit outside a gain section? |
| C2 | a Portuguese reader reads "o Ninjobs" | `pt-ninjobs-masculine` | every Portuguese chapter where Ninjobs takes an article, 14 of them from 0 to 22 (/apply lists them); docs/03's Ninjobs row | Does the Portuguese edition say "o Ninjobs", "do Ninjobs", "no Ninjobs" everywhere, as docs/03 fixes? |
| C3 | a reader with little TypeScript reads chapter 3's refusal without a magic string | `ch03-literal-type-comment` | 3 §A pure function, the refusal example and its comment | Can a reader who knows no TypeScript say, from the comment alone, why `err` takes no string but that one? |
| C4 | a team reads FOCUS as optional before deciding to adopt it | `ch04-focus-optional` | 4, the opening; §What the team gains | Does chapter 4 say, before FOCUS is taught, that the team decides after reading its gain? Does the gain say one pattern across projects makes moving people cheaper? |
| C5 | a team keeps its tests fast | `ch05-test-time` | 5, the opening; §A test for each piece; §What the team gains; §Key points | Can the author say, from chapter 5, why agents write slow suites and what keeps the per-delivery run fast? |
| C6 | a team teaches the agent by talking to it instead of fixing its work by hand | `ch13-teach-the-agent`, `ch07-talk-not-edit` | 13 §Review the staged change; 7, the opening and §Living documents | Does chapter 13 ask for each correction by talking, and say why it teaches the agent? Does chapter 7 say the documents change by conversation without a sentence that reads as its contradiction? |
| C7a | the passages the author marked say what the author means | `case-a-why-anonymous` | 0 §What the team gains, the sentence on Case A | Does it say why Case A has no owner, client or business? |
| C7b | | `agent-never-unsure` | 1 §What is not in the window; §Key points | Does it say an agent never says "I don't know", and that the person's judgment tells a hypothesis from a fact? |
| C7c | | `ch02-gain-less-to-read` | 2 §What the team gains | Does it say the method writes less because the person reads all of it? |
| C7d | | `pt-identifiers-choice` | the Portuguese 3 §KISS, the sentence on the code's names; docs/04's language rule | Does it call Portuguese names a teaching choice, not a recommendation, with no sentence on which names are translated? |
| C7e | | `ch03-error-languages` | 3 §Exception, refusal, error; the notes on Rust and Dart | Does it say several languages separate a bug from a handled failure, and Dart most explicitly, with a source to open? |
| C7f | | `ch04-uncle-bob` | 4 §The dependency rule | Is Uncle Bob named where Robert C. Martin first is? |
| C7g | | `ch04-scalable-meaning` | 4 §FOCUS, letter by letter, the S | Does the S say the project grows without one feature interfering with another? |
| C7h | | `ch05-random-values` | 5 §Swap only I/O and what changes between runs | Does it cover random values and anything else that changes between runs, beside the clock? |
| C7i | | `ch07-rag-and-numbers` | 7 §One place per fact; §What the team gains; §Key points | Does it say the documents work as retrieval made for the project, and that every focus-kit project numbers them alike? |
| C7j | | `ch11-queue-grows` | 11 §Size and order; §What the team gains; §Key points | Does it say three to eight lines is how a milestone starts, not a limit, and that the person decides what enters? |
| C7k | | `ch11-agent-runs-propose` | 11 §Changing the queue, the paragraph on "define it now" | Is the claim that the agent cannot run `/propose` gone, with the reason for a fresh session kept? |
| C7l | | `ch14-face-prototype` | 14 §The queue as a kanban board and its note | Is FACE shown briefly, as the author's prototype, with a link to open? |
| C7m | | `try-before-commit` | 13, the opening; §Review the staged change; §Key points | Does it advise using what the delivery built before committing, small things fixed in conversation, larger ones as next lines? |
| C7n | | `ch19-agent-does-git` | 19 §Worktrees in the kit; 18 §Choosing | Does it say the person can ask the agent for any git step the book teaches, and checks the result? |
| C7o | | `ch19-git-step-wording` | 19 §Worktrees in the kit; 18 §Choosing; the Portuguese 19 | Does it name only steps the book teaches, say conflict marker, and give the Portuguese one phrase for the agent acting alone? |
| C7p | | `docs04-code-layout` | docs/04's rule for code; the examples in chapters 3, 4 and 5 | Does docs/04 state the blank-line layout, and do the examples follow it in both editions? |
| C8 | everything changed since `a60d8f1`, read by the code reading | the Milestone review slot and §8 | decision 5's paths; the readers' reports | Do the paths the reports list cover decision 5's? Which candidates, K1 and K2 among them, does the author confirm? |

The passages answer the clauses; a fault the author finds outside them is a finding as well (decision 3).

The review's queue line, as this page leaves it, and the findings' lines, in docs/06 under M18 after it:

```
[>] m18-review               the review of M18 as docs/05 §8 says · after ch19-git-step-wording, ch14-face-prototype, try-before-commit, ch19-agent-does-git, docs04-code-layout, early-no-forward-links, pt-ninjobs-masculine, case-a-why-anonymous, agent-never-unsure, ch02-gain-less-to-read, pt-identifiers-choice, ch03-literal-type-comment, ch03-error-languages, ch04-focus-optional, ch04-uncle-bob, ch04-scalable-meaning, ch05-test-time, ch05-random-values, ch07-rag-and-numbers, ch07-talk-not-edit, ch11-queue-grows, ch11-agent-runs-propose, ch13-teach-the-agent
[ ] <slug>                   <what will be true>; both editions
```

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Fixing anything in this delivery: findings are lines (docs/05 §8).
* A second review of a finding's fix, and an M18.1 (docs/05 §8).
* M17's clauses: `m17-review` recorded them. Its fixes are read only by the code reading (decision 2).
* A reading of the whole book: the passages are the test (decision 3).
* `work/done/` and `work/kit-proposals.md`: history and notes for the kit (decision 5). The disclosure list is checked by `make verify`'s scan.
* The kit's own wording: fixed in the kit on the author's word, not here (decision 5).

**Done when.**

* [x] Both PDFs built; the clause table with PDF pages given to the author.
* [x] The author read the passages in both PDFs and answered C1 to C7p, or waived the reading; every answer and every `outside:` fault recorded on this page.
* [ ] The code reading run on the author's word as the Milestone review slot says, against `a60d8f1`, at most two agents at a time; each reader's report lists the paths it read, and together they cover decision 5's; its candidates checked and the author's confirmed ones recorded. Not run: the author closed the line without it, so this item stays open (Divergences).
* [x] Each finding a `[ ]` line under this review, in the author's words, one line per fact. None from C1 to C7p; C8 unanswered, so none from the code reading.
* [x] `make verify` green.
* [x] The delivery review run as docs/05 §5 says, on this page and this delivery's hunk of docs/06, and recorded.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

## Record

**PDF pages**, at `48de1c5`, the cover counted as page 1 (en / pt): chapters 0 to 7 start at 5, 11, 18, 23, 36, 49, 58, 62 / 5, 11, 19, 24, 39, 53, 62, 66. C2, the Portuguese chapters with an article before Ninjobs: 0 (5), 2 (19), 3 (24), 4 (39), 6 (62), 7 (66), 9 (85), 11 (100), 12 (109), 13 (117), 15 (138), 16 (146), 21 (190), 22 (195), and docs/03 line 97. C3 28 / 29. C4 36, 47 / 39, 51. C5 49, 50, 57, 57 / 53, 54, 61, 61. C6 116, 62, 69 / 125, 66, 73. C7a 9 / 9. C7b 15, 17 / 15, 17. C7c 21 / 22. C7d pt 25, docs/04 line 28. C7e 30 / 31. C7f 37 / 40. C7g 40 / 44. C7h 52 / 56. C7i 62, 69, 70 / 67, 74, 75. C7j 96, 100, 100 / 103, 107, 108. C7k 97 / 104. C7l 126 / 135. C7m 109, 116, 120 / 117, 125, 129. C7n 165, 157 / 176, 166. C7o as C7n, and the Portuguese 19 at 169. C7p docs/04 line 52, examples in chapters 3, 4 and 5.

**Answers.** The author read the passages and answered, in their words, "Está tudo certo" ("everything is right"): C1 to C7p hold. No `outside:` fault.

**C8.** Unanswered. The author chose to start the code reading, then, before any agent was launched, said to close the line. Nothing was launched. K1 was not confirmed by the author, so it is not a line; K2 is the kit's own wording, never a line here (decision 5).

**Findings.** None from C1 to C7p; C8 unanswered, so none from the code reading. No line is added under this review, so M18 closes with this line.

**Divergences.**

* The code reading did not run: decision 5's 82 paths of `a60d8f1..HEAD` were not read by any reader, and docs/05 §8's look at the whole was not taken for M18. docs/05 §8, and §4's fourth case a line waits in, say the line then waits as `[?]` with `· resume: apply`; §8 also starts the reading "only on the person's word", and the author gave the word to close the line instead. Done when's third item stays open for that reason. M19's review, based on this line's commit, does not read M18's range either; a fault from it that surfaces later is a `[ ]` line like any other.
* No document changes: docs/05 §8 stays as it is, and this waiver is the author's choice for M18, as `m17-review`'s waiver of the PDF reading was for M17.

**Proof.** `make book` built both PDFs and EPUBs; `make verify` green.

**Delivery review.** A read-only agent on Opus read this page and this line's hunk of docs/06 against docs/04, docs/05 and AGENTS.md. It confirmed every PDF page and the docs/03 and docs/04 lines the Record cites, and found four faults, all fixed here: the code-reading item was ticked though not run (now left open), "no finding" said nothing of C8, K1 was called not a finding without the author's word, and the divergence did not name docs/05 §8 and §4. It also noted that the docs/06 hunk holds another session's line, so only this line is staged, and that M17 and M18 each skipped a §8 step; whether §8 allows that is the author's call, left to conversation.

## Commit

```
docs(m18-review): review M18, no finding

- C1 to C7p hold in the author's reading of both PDFs
- the code reading did not run, on the author's word; recorded as a divergence
- M18 closes with no finding line

work/done/m18-review.md
```
