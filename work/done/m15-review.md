# m15-review

**Objective.** The author knows, clause by clause, whether M15's paragraph holds in the hands of a reader of the book, in both editions, and whether the whole repository, its code, its documents and every chapter in both editions, holds under one deep review read from the first commit; each clause that fails and each finding the author confirms is a `[ ]` line in M15 under this review.

**Decided from the documents.**

1. The person tests the clauses alone; the agent prepares the clause table, the PDFs and the page numbers, records the answers and writes the lines (docs/05 §8; `m13-review` decision 1).
2. The deep review's base is the first commit, `3ca06b1`, which holds only `LICENSE`, so the whole repository is read: docs/05 §8 lets the page name "the commit that closed the previous milestone, or the first commit". Chapter 15 §The review is a delivery narrows that to "the project's first commit for a first milestone"; this page follows docs/05 §8, and the gap is a C7 candidate. The reason to read the whole now: M14's deep review read chapters 10 to 19, 21, 24 and 25 by the numbers of that time, and the high review the diff of `0c50f1b`, so chapters 1 to 9, 20, 22, 23 and 26 of that time were never read as a whole, and the author decided the next milestone's review answers that, not a review of M14's review (docs/05 §7, §8). The other reading, `824dbd6`, the commit of `ch26-what-counts` that closed M14, holds every chapter, since M15 renumbered them all, but leaves out ten of the eleven scripts, docs/02 and docs/05, sixteen ADRs, the manuals, the hooks, the workflow, the Makefile, `mkdocs.yml`, `pandoc/`, the READMEs, `AGENTS.md` and the installed skills. Made on the author's behalf: the first commit.
3. What the deep review reads, and what a finding from it is. It reads, whole: `book/` in both editions, `index.md` included; docs/00 to docs/06, the ADRs and the manuals; `scripts/`, the `Makefile`, `mkdocs.yml`, `requirements.txt`, `pandoc/` (its CSS), `overrides/`, `.githooks/`, `.github/workflows/`; `README.md`, `README.pt.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.gitignore`; and the kit's installed copies (`.claude/`, `.agents/`, `.windsurf/`, `.cursor/`, `.gemini/`, `.github/prompts/`). It reads code against docs/01 and docs/04, chapters against docs/00, docs/03, docs/04, `AGENTS.md`'s non-negotiables and the kit as installed, and the documents against each other. A finding is a fault in one of these files, named by file and line: a script or build that does not do what docs/01 says, a document that contradicts another or the kit, a chapter passage that breaks a non-negotiable or docs/04, teaches the kit wrongly, or says what the other edition does not. Not read: `work/done/` (596 files, the record of what happened, which a later delivery does not rewrite), this page, `LICENSE`, `LICENSE-TEXT`, fonts, images and PDFs. The kit's copies are read for agreement with each other and with docs/05; a fault in the kit's own wording is reported to the author as a note for the kit, not a line here. Made on the author's behalf.
4. How it runs: as docs/05 §5's Milestone review slot says once `review-slot-models` is `[x]`, against `3ca06b1`. Who launches it, how and on which models is as the slot and §8 say, as that line leaves them, not this page's to decide; its final page has read-only agents on Opus read `git diff 3ca06b1..HEAD`, one per area: the build, the chapters, the kit's skills, the documents. The line existed before this dependency was found, so it waits as `[?]` with `· resume: apply · blocked: after review-slot-models`, and returns to `[>]` when that line is `[x]` (docs/05 §4).
5. Each candidate is checked against the file before the author sees it, as the slot says, and labelled "seen", "latent" (nothing in the repository triggers it today) or "weak" (the claim does not hold as stated); the author confirms which count. The confirmed ones become one line per file: a chapter's two editions are one line, and a fact that stands in two files is one line holding both (the author's answer to `m14-review`'s C8).
6. The test of "a reader reaches the method in five chapters" is the contents page of each PDF and the chapter the method starts in; the test of "said once" is the checks of `method-said-once` and `one-gain-section` plus the author's reading; the test of the quick guide is the author following its two columns on paper, with no repository, and finding each pointer's chapter (docs/05 §8, a milestone of chapters is tested by the author reading). `method-said-once`'s checks name chapters by the numbers before `renumber-chapters`; /apply runs them on today's files (18 is 16, 16 is 14, 10 is 7, 15 is 13).
7. Each finding becomes one `[ ]` line under this review, saying what will be true, not how; no M15.1 (docs/05 §8; `m13-review` decision 4).

**Behaviour.**

* The author receives both PDFs (`make book`), the page where each passage below starts in each PDF, the contents page of each, and the clause table, and tests C1 to C6 in English and then in Portuguese.
* For each clause the author answers `C<n>: holds` or `C<n>: fails, <what the reader does not get>`; a clause that fails is a finding.
* The deep review runs as the Milestone review slot says, against `3ca06b1`, over decision 3's paths, and each agent's report lists the paths it read. The candidates, checked as the slot says, are shown grouped by area, as `m14-review`'s C8 was: the build, the documents, the chapters, and the kit's copies, whose faults in the kit's own wording are notes for the kit, not lines. The author names the ones that count (C7).
* Each finding becomes one `[ ]` line in M15 under `m15-review`, shown to the author before staging; the author may reword it.
* Edge: `review-slot-models` not `[x]`: the line stays `[?]` with `· resume: apply · blocked: after review-slot-models`, /apply does not start, and nothing is tested.
* Edge: the paths the agents' reports list, together, are fewer than decision 3's (an agent that covered only part of its area, a run cancelled): the page records what was read and what was not, C7 stays unanswered, and the line waits as `[?]` with `· resume: apply · blocked: deep review read <what it read>, not the whole`.
* Edge: the slot says none: no deep review runs, C7 records it, and the reason of decision 2 stays open, said in the report.
* An answer missing for some clauses: the page records the answers given, the line waits as `[?]` with `· resume: apply · blocked: <clauses> not answered`, and nothing is staged (docs/05 §4, §6).
* No file under `book/` and no document but docs/06 and this page is edited by this delivery.

**Contract.**

The clause table, what the author tests (M15's paragraph, quoted: "When this milestone closes, a reader reaches the method in five chapters instead of nine, every rule of the book is said once in the chapter that owns it with one source per point and one gain section, a reader sees what a five-line delivery costs before being asked to accept one, chapters 20 to 26 keep only what no manual gives, and a chapter after chapter 12 walks a reader from zero to the first delivery on a new project and on an existing one, step by step, with no repository."). The paragraph uses the numbers before `renumber-chapters`; the table uses today's: chapters 20 to 26 are 18 to 24, and the chapter after chapter 12 is chapter 10, after chapter 9.

| | Clause | Answered by | Passage (today's numbers; pt the same files) | How the author tests it |
|---|---|---|---|---|
| C1 | a reader reaches the method in five chapters instead of nine | `prologue-and-why`, `ch3-spec-cut`, `simplicity-and-results`, `focus-and-slices`, `ch8-testing-trim`, `renumber-chapters` | the contents page of each PDF; the prologue §What the team gains, where it names the five parts and Part II begins "from its documents"; chapters 1 to 6 | "Nine" counted the prologue: at M14's close the prologue and chapters 1 to 8 stood before chapter 9, How focus-kit was born. Counted the same way today, six stand before chapter 6, How focus-kit was born, and seven before chapter 7, The documents, where the prologue's Part II begins; five only without the prologue, where M14's close gives eight. Which chapter starts the method, which count does the author take, and does it give five against nine? Does each chapter before the method still open with what the reader can do after it, and does the author miss nothing the old chapters taught? |
| C2 | every rule of the book is said once in the chapter that owns it, with one source per point | `method-said-once`, `ch20-21-git-cut`, `ch22-26-team-cut`, the five base lines | the six marks (14 §Six marks); the lint story (16 §It works both ways); Case A's rate (17 §What the team gains); "reads as right even when wrong" (7 §Living documents); 13 §What `/apply` does; 24 §Why the first answer feels final; exceptions (3 §Exception, refusal, error); 1 §More context, less accuracy; "29 checks", found today in chapters 3, 6 and 16 | Reading each passage, does the author find it in one chapter and a pointer elsewhere? Does any point still carry more than one study for the same claim? |
| C3 | one gain section | `one-gain-section` | every chapter's last two sections; the prologue's gain | Does every chapter end with one gain and key points that do not repeat it? Is "no baseline" said only in the prologue? |
| C4 | a reader sees what a five-line delivery costs before being asked to accept one | `small-delivery-example` | 11 §Changing the queue | Can the author, as a reader, say what `due-date-format` cost and what an edit on the spot would have skipped, from the chapter alone? |
| C5 | chapters 20 to 26 (18 to 24 today) keep only what no manual gives | `ch20-21-git-cut`, `ch22-26-team-cut` | 18 §One delivery, one step to undo and §Commits and the history; 19 §What a worktree is and when it pays and §The life of a worktree; 22 §How a team decides; 24 in its new order | Does chapter 18 reach its rule in its second section? Does any passage still teach what *Pro Git* or a vendor's documentation teaches, with no decision of the kit's attached? Is the protocol next to the card's story? |
| C6 | a chapter after chapter 12 (chapter 10 today) walks a reader from zero to the first delivery, new and existing, step by step, with no repository | `quick-guide`, `renumber-chapters` | 10 §A new project and §An existing project | Following each column on paper, does the author reach a first commit with no step missing and no repository opened? Does each pointer land on the chapter that teaches the step? |
| C7 | the whole repository, read by the deep review | the Milestone review slot, as `review-slot-models` leaves it, against `3ca06b1` | decision 3's paths; the agents' reports | Do the paths the reports list cover decision 3's? Which candidates does the author confirm? |

Two C7 candidates are known before the review runs and open its list: docs/03's `finding` row names only a clause no delivery answers or one that fails by hand, where docs/05 §8 adds a finding the code review confirms; and chapter 15 §The review is a delivery gives the first commit only "for a first milestone", where docs/05 §8 gives it to any milestone.

/apply gives the PDF pages from `make book` at the start of the delivery.

The review's queue line, as this page leaves it, and the findings' lines, in docs/06 under M15 after it:

```
[?] m15-review               the review of M15 as docs/05 §8 says · resume: apply · blocked: after review-slot-models
[ ] <slug>                   <what will be true>; both editions
```

**Out of scope.**

* A second review of a finding's fix (docs/05 §8).
* Fixing anything in this delivery.
* M14's clauses: `m14-review`.
* How the deep review runs and on which models: `review-slot-models`.
* `work/done/`: history (decision 3); the disclosure list is `make verify`'s scan.

**Done when.**

* [x] Both PDFs built; the clause table with PDF pages given to the author.
* [x] The deep review run as the Milestone review slot says, against `3ca06b1`; each agent's report lists the paths it read, and together they cover decision 3's; its candidates checked and the author's confirmed ones recorded.
* [x] Every clause answered and recorded on this page; each finding a `[ ]` line under this review, in the author's words.
* [x] `make verify` green.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Decisions in the review.**

* Revised by a second /propose, after the code review of `3963cb2` found that M14's deep review read part of the chapters and Done when was ticked with no Divergence, and again after a review of that revision. Made on the author's behalf, each a recommendation the author may correct: the base is the first commit, `3ca06b1`, as docs/05 §8 permits, not `824dbd6` (decision 2); the deep review reads decision 3's paths, chapters in both editions included, and not `work/done/`; it runs as the slot says once `review-slot-models` is `[x]`, the line waiting as `[?]` until then (decision 4); candidates are labelled and confirmed one line per file, as in M14 (decision 5); the clause table uses today's chapter numbers, C1's test gives both counts and asks the author which to take, C2 names the three chapters where "29 checks" stands today, and C7 opens with two candidates known now.

**Divergences.**

* The Contract's queue line, `[?]` with `· blocked: after review-slot-models`, did not apply: when /apply started, `review-slot-models` was already `[x]` and the line `[>]`, so it went to `[*]` and the edge of Behaviour did not fire.
* The checker is not "an agent on Fable", as docs/05 §5's Milestone review slot says. Asked for the word, the author said that by Fable they meant Opus running with the host's advisor set to Fable, and that the review runs on this session's configuration, Opus 5.5 with `/advisor fable`, with nothing more to set; an Opus agent launched from this session has the advisor tool. So the readers and the checker are Opus agents, `model: opus`, each with that advisor. The slot's wording is a C7 candidate (K3 below); the installed kit's copies name no model, so the kit itself carries no such wording today.
* The chapters area ran as two readers, the prologue to chapter 11 and chapters 12 to 24, each in both editions, on the author's word, so each could read its files whole; the slot says one agent per area.

**Where each passage starts.** From `make book` at the start of the delivery, on 2026-10-17: `output/one-page-at-a-time.pdf` (en, 189 pages) and `output/uma-pagina-de-cada-vez.pdf` (pt, 198 pages), PDF page numbers, the cover counted as page 1.

| Clause | Passage | en | pt |
|---|---|---|---|
| C1 | the contents page | 4 | 4 |
| C1 | the prologue §What the team gains (the five parts) | 9 | 9 |
| C1 | 6, How focus-kit was born | 54 | 58 |
| C1 | 7, The documents (Part II begins) | 59 | 63 |
| C2 | 14 §Six marks | 117 | 122 |
| C2 | 16 §It works both ways | 130 | 135 |
| C2 | 17 §What the team gains | 139 | 145 |
| C2 | 7 §Living documents | 65 | 70 |
| C2 | 13 §What `/apply` does | 107 | 112 |
| C2 | 24 §Why the first answer feels final | 184 | 193 |
| C2 | 3 §Exception, refusal, error | 30 | 30 |
| C2 | 1 §More context, less accuracy | 14 | 14 |
| C2 | "29 checks": 3 (line 10), 6 (lines 10, 27, 42, 66), 16 (line 10) | 23, 54, 129 | 23, 58, 134 |
| C3 | each chapter's §What the team gains, prologue to 24 | 9, 16, 21, 34, 45, 53, 57, 66, 74, 82, 88, 96, 104, 114, 121, 127, 132, 139, 147, 159, 165, 169, 175, 181, 188 | 9, 16, 21, 35, 48, 57, 61, 70, 79, 87, 93, 102, 109, 119, 126, 132, 137, 145, 154, 167, 173, 178, 185, 190, 198 |
| C4 | 11 §Changing the queue | 93 | 99 |
| C5 | 18 §One delivery, one step to undo; §Commits and the history | 141 | 147 |
| C5 | 19 §What a worktree is and when it pays | 152 | 159 |
| C5 | 19 §The life of a worktree | 153 | 161 |
| C5 | 22 §How a team decides | 175 | 184 |
| C5 | 24, Asking for more | 182 | 191 |
| C6 | 10 §A new project | 85 | 90 |
| C6 | 10 §An existing project | 87 | 92 |

**What the checks give today.** `method-said-once`'s checks on today's files (18 is 16, 16 is 14, 10 is 7, 15 is 13): "29 checks" once in chapter 16; the six-mark list with meanings in chapter 14 only; "reads as right even when it is wrong" in chapter 7 only; "never commits" twice in chapter 13, lines 115 and 117, both in §Why it stops at the stage, line 117 quoting the kit, and the title reads "never commit". `one-gain-section`'s: one §What the team gains per chapter, at most five key points each, the same number of `##` headings in both editions, and the baseline grep lists no file; the prologue's gain is five sentences and the five parts, where that page said one to four sentences for every chapter. The Portuguese "29 checks" is "29 verificações" in chapters 3 and 6 and "29 checagens" in chapter 16.

**The author's answers.**

* C1 to C6: holds, in both editions, on the author's word: the author takes them as holding without reading the passages now, because they will read the whole book, both editions, at the end of M16. C1's count, with or without the prologue, was left to that reading; the two observations above (the prologue's gain, "29 checagens") go to C7 with the review's candidates.

**C7, the deep review.** Launched on the author's word in this session, against `3ca06b1`. Five read-only readers on Opus, each listing the paths it read: the build, the documents, the chapters from the prologue to chapter 11, chapters 12 to 24, and the kit's copies. Each read every path of its area; together they cover decision 3's paths. The first launch of four of them was stopped by the author near the weekly usage limit, before any report, and relaunched at 18:01; the kit's reader had finished and was not rerun. One checker on Opus, with the session's advisor, opened each candidate in its file. Labels: "seen" (the line says it and breaks the rule), "latent" (nothing triggers it today), "weak" (the claim does not hold as stated), "covered by M16" (an open M16 line plans it).

Build:

* build-1 `scripts/check_links.py:25`: only example.com, .org and .net skipped, docs/04 says `example.*`. Latent.
* build-2 `scripts/build_book.py:320`: a same-page `](#missing)` link would print at `Makefile:1`, not its line. Latent.
* build-3 `scripts/check_disclosure.py:50-56`: a file with a NUL anywhere or invalid UTF-8 gets only its path scanned, where docs/01 defines a text file by its first 8000 bytes. Latent.
* build-4 `scripts/check_disclosure.py:8`: the docstring says the run fails when the hooks are off, with none of docs/01:69's conditions. Seen.
* build-5 `scripts/release.py:67`: closed stdin gives a traceback, not the convention line. Latent.

Documents:

* K1 docs/03:34: the `finding` row leaves out a finding the code review confirms (docs/05 §8). Seen.
* K3 docs/05:228-229: the slot names a checker on Fable; the author runs the review on Opus with the host's advisor on Fable. Seen.
* doc-1 docs/03:115: the `team gain` row still allows "one sentence saying it has none", which docs/04:48 forbids. Seen.
* doc-2 ADR-0017:18: the Decision still allows that sentence, with no amendment for `one-gain-section`. Seen.
* doc-3 docs/06: M16 has no `m16-review` line, against docs/05 §4 and §8. Seen.
* doc-4, doc-5 docs/03:3, docs/00:16 and :39: a glossary and appendices that do not exist; ADR-0017 defers them. Weak.
* doc-6 docs/03:33: who launches the review. Weak.
* doc-7 docs/05:225-230: the slot holds no command. Weak.
* doc-8 README rows for the AGPL. Weak.
* kit-2 docs/05:301-303 (§8: the person launches, the agent never does) and kit-3 docs/05:285 (§7: no specialized subagent), both against the slot. Covered by M16 (`kit-2026-10-17`, `ch16-review-agents`); the kit's wording.

Chapters (A from the reader of the prologue to 11, B from the reader of 12 to 24):

* K2 15:19, both editions: the first commit "for a first milestone". Seen.
* K4 pt 16:10, 26, 27, 60: "29 checagens" beside "verificações" in pt 3 and 6. Seen.
* K5 the prologue's gain is five sentences and the parts: `one-gain-section` set four outside the prologue. Weak.
* A1 5:56: the use case `lend` pointed to chapter 3; it is chapter 4's. Seen.
* A2 7:59 and B28 18:165: free lines glossed as ready to build, narrower than docs/03:107. Seen.
* A3 10:43: a message written for the chapter with a `docs:` prefix and no imperative subject. Seen.
* A4 en 4:58, pt 4:59: Parnas named with no introduction and no note. Seen.
* A6 pt 11:100, 148: "o empréstimo mostra a devolução" for the loan screen's due date. Seen.
* A7 Portuguese terms against docs/03: "vencimento" (pt 4:138, 140), "motor" (pt 5:26, 85), "a view" (pt 4:115-116), "fake" as a noun (pt 3, 4, 5). Seen. "verify" and "bibliotecária" (also B13): weak.
* A8 3:9-14 retells chapter 6's causes and checks. Seen. The same numbers as evidence for other points (2, 3, 4, 7): weak.
* A9 and B8 the stack rule and the Flutter story in 6, 9 and 22. Seen.
* A10 and B12 code blocks over 74 columns: en and pt 1:74, 8:17, 10:12, en 11:45, pt 11:46-55, en 14:37, pt 13:94, pt 15:30-31, en and pt 21:32-45. Seen.
* A16 pt 11:19 and B18 pt 13:167-176, B19 pt 21:38, B20 pt 19:229: English placeholders or folders with no note, and pt 13:176 explaining the imperative with the English subject. Seen.
* B2 18:45, 49: the log's subject and slug for `lend-book` differ from chapter 13. Seen.
* B3 17:26, 69: a delivery's time measured between two commits that on trunk are one. Seen.
* B4 23:23: Ninjobs' two product checks given as what survives of the method. Seen.
* B5 21:67-69: the pending-deletion story of 13:188-189 retold. Seen.
* B6 20:51-85 and B7 16:55, 69: the kanban board, the fold onto three columns and Case A's `[?]`, owned by 14. Seen.
* B9 13:23 and 22:61: the one-sentence line rule, owned by 11. Seen.
* B10 21:59, 87: one fact in two numbers, and a gain with three counts. Seen.
* B11 13:87, 14:66-67, 19:25-88: `src/<slice>/` paths against `src/features/<name>/`. Seen.
* B14 pt 14:53 and pt 10:31: "uma worktree". Seen.
* B15 pt 14:104-115 against pt 20:58: one fold, two sets of column names. Seen.
* B16 pt 14:34: "as regras recusam" drops "may". Seen.
* B17 pt 14:77 and pt 20:42: two slugs for `fix-due-date`. Seen.
* B22 24:67-72: numbers with their note key only on the sentence before. Seen.
* B24 18:177: the gain calls an illustration written for the chapter its evidence. Seen.
* B25 19:84 against 19:242-268: when a worktree pays, said two ways; :84 follows the kit's wording. Seen.
* B26 en 12:141, pt 12:148: "one review skill" that does not exist. Seen.
* A5, A11 to A15, A17, A18, B1, B21, B23, B27: weak (glosses a translator adds, a number that could say when, a historical credit, a section order the fixed shape explains, a page "written" meaning complete; B1's judge matches the run's record).

Kit's copies:

* kit-1 `references/documents.md:112-113`, all six copies: "FOCUS is chapter 7", linked to `/07-four-pieces/`, a page this site does not have; FOCUS is chapter 4. Seen; the kit's wording, a note for the kit.
* kit-4 `references/documents.md:75`, all six copies: "the table of SETUP.md §1", a file the install does not place. Latent; a note for the kit.

* C7: the author counted the "seen" candidates only, one line per file, a fact that stands in several files as one line, under `m15-review` in M15. Latent, weak and covered by M16 stay recorded here with no line; kit-1 and kit-4 are notes for the kit. The author also had `m16-review` added as M16's last line, which the documents' reader found missing (doc-3), so it is a queue line of M16, not a finding of M15.

**Findings, one line per file.** In docs/06 under `m15-review`, in this order:

| Line | Files | Candidates |
|---|---|---|
| `disclosure-docstring` | `scripts/check_disclosure.py` | build-4 |
| `docs03-finding-and-gain` | docs/03 | K1, doc-1 |
| `adr17-gain-amendment` | ADR-0017 | doc-2 |
| `docs05-review-checker` | docs/05 | K3 |
| `stack-rule-once` | chapters 6, 9, 22 | A9, B8 |
| `free-line-gloss` | chapters 7, 18 | A2, B28 |
| `line-rule-once` | chapters 13, 22 | B9 |
| `case-a-board-once` | chapters 16, 20 | B6, B7 |
| `slice-paths` | chapters 13, 14, 19 | B11 |
| `code-width` | chapters 1, 8, 10, 11, 13, 14, 15, 21 | A10, B12 |
| `pt-fixed-terms` | pt chapters 3, 4, 5, 10, 11, 14, 16, 20 | A6, A7, K4, B14, B15, B16, B17 |
| `pt-placeholders` | pt chapters 11, 13, 19, 21 | A16, B18, B19, B20 |
| `ch03-opening` | chapter 3 | A8 |
| `ch04-parnas` | chapter 4 | A4 |
| `ch05-lend-pointer` | chapter 5 | A1 |
| `ch10-commit-message` | chapter 10 | A3 |
| `ch12-review-skill` | chapter 12 | B26 |
| `ch15-first-commit` | chapter 15 | K2 |
| `ch17-delivery-time` | chapter 17 | B3 |
| `ch18-log-evidence` | chapter 18 | B2, B24 |
| `ch19-when-worktrees-pay` | chapter 19 | B25 |
| `ch21-counts-once` | chapter 21 | B5, B10 |
| `ch23-what-survives` | chapter 23 | B4 |
| `ch24-note-keys` | chapter 24 | B22 |

**Notes for the kit.** kit-1: the installed `references/documents.md` sends readers to `/07-four-pieces/`, which this site does not serve; FOCUS is chapter 4, `/04-focus/`. kit-4: it points to `SETUP.md`, which the install does not place. Both are the kit's wording, to be fixed in the kit's repository; this repository's copies change only by reinstalling.

**Proof.** `make book` built both PDFs and EPUBs at the start; `make verify` green at the end. No file under `book/` changed; the delivery edited only this page and docs/06.

**Decisions.** The `m16-review` line waits on every M16 line not already named by another M16 line's `after`, so it is M16's last. M16's `kit-2026-10-17` waits only on `m15-review` (`· after m15-review`), so it is free once this line is `[x]`, while M15's findings are still open, as M14's were when M15 started.

```commit
docs(m15-review): review M15 clause by clause; 24 findings

- C1 to C6 hold on the author's word; a full reading after M16
- the deep review read the whole repository from 3ca06b1
- five Opus readers, an Opus checker with the advisor on Fable
- 24 findings, one line per file, under m15-review in docs/06
- m16-review added as M16's last line

work/done/m15-review.md
```
