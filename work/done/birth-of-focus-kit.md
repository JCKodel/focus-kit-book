# birth-of-focus-kit

**Objective.** After chapter 4 the reader knows where each rule of focus-kit came from and which failure it answers: one page per delivery, deciding and doing in separate sessions, documents that hold the facts, an agent that never commits, and one question against weight. The reader also learns what the restart taught beyond the process: weigh a stack by what the agent knows, and apply an architecture only where it pays. The reader can also recognize a process growing heavier than the work it serves, the kit's own included.

**Behaviour.**

* The reader can name the five reasons Ninjobs restarted on 2026-08-29 and the lesson of each:
  * the agent kept missing the design in a stack it had seen little of, and matched it at once in one it had seen much of. The limit was what the agent knew, not the stack: hold to the project's value, and weigh a stack by how well the agent knows it;
  * the architecture applied whole to every feature (eight files to show one field, the same structure for a trivial record and a privacy rule). An architecture is worth its rules only where they pay; each rule is one more thing the agent carries;
  * checks that were costly to satisfy, cheap to bypass, and never failed on a product error;
  * six places where the truth could diverge. This is also why a leaner OpenSpec was rejected: the cost was the number of places, not the size of each file.
* The reader can list what the restart put in their place: one page per delivery, `/propose` and `/apply` in separate sessions, a queue, no formal spec, archive or change, the agent staging and the person committing, abstraction only on the second concrete occurrence, and the governor question.
* The reader can say why Ninjobs' two commands were short (10 and 47 lines): they only pointed at documents.
* The reader can read the kit's growth table and say which question the growth skipped, and what "one file" removed and kept.
* The reader can explain, from the drift found on 2026-09-21, why a command holds no project fact and every such fact lives in a slot of docs/05.

**Contract.**

Chapter 4, `book/en/04-birth-of-focus-kit.md` and `book/pt/04-birth-of-focus-kit.md`:

* Title: "How focus-kit was born" / "Como nasceu o focus-kit".
* Voice: first person, the author ("I restarted Ninjobs"), as chapter 1 says "my own product". The one case story of Part I.
* Sections, in order (headings may be reworded in the writing; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. Fifteen days, four screens. One clause points back to chapter 1's OpenSpec figures, with the same source note, and adds no new count (chapter 1 counted 37,228 lines, and ADR-0022 says 38,823; the book keeps its own count). Then the five reasons ADR-0022 gives, paraphrased, each followed by its lesson in one or two sentences, as in Behaviour's first bullet:
     * **The stack.** Flutter and React are named. The ADR's two stack reasons (the slow loop from screen to design, and the agent deriving a colour instead of writing it) are told as facts about the agent: the same agent on the same product. One sentence says it outright: Flutter could build the same project; what the agent had seen in training was the limit. One public indicator of how much each framework is used backs the difference, and the prose calls it an indicator, not a measure of training. /apply finds it (the Stack Overflow Developer Survey's framework table, say), checks it, and cites it with its year. If no source says it plainly, the paragraph stays an observation of one project, and the page records that. The lesson, stated plainly: hold to the project's value, not the stack; a stack the agent knows little of is a risk, whatever its quality. Chapter 7 teaches the choice.
     * **The architecture.** FOCUS is named as the architecture this book teaches in Part III. What failed was applying it whole to every feature. The kit still offers it, and Ninjobs kept its two principles. Part III (chapters 14 and 15) says when the four pieces pay their way. The prose presents FOCUS as valuable and applied without measure, never as the problem. It names no earlier book or material as a cause (ADR-0005).
     * **The checks**: the 29 checks.
     * **The six places**: docs, specs, changes, ADRs, outline, code. Then the rejected alternative, a leaner OpenSpec.
     The ADR's own split closes the section: the new stack answered the first two reasons, the new process the other three, and either change alone would have ended in the same place. The rest of the chapter follows the process.
  3. The restart: the decision of ADR-0022 §3 and the rules around it, as in Behaviour's second bullet, paraphrased. The two commands, 10 and 47 lines, said which documents to read and what never to do. The process carried Ninjobs to its public opening on 2026-09-10; that date is the only outcome given.
  4. The kit that grew: extracted as focus-kit 0.1.0 on 2026-09-15. Then the table below, then what the peak had added (installer CLI, doctor, self-test, knowledge graph, manifests, version stamp), measured against the governor question it skipped.
  5. One file: the commit of 2026-09-19 deleted 32,861 lines and left `SETUP.md` and its READMEs. What it kept is the five points of that commit's README: documents carry the weight, one page per delivery, deciding and doing in separate sessions, the agent never commits, and the governor. "One file" is a return to the size that worked in Ninjobs, not to an earlier one-file kit: 0.1.0 already had 23 files. The one addition, any host and any language, takes one sentence and points to chapter 5.
  6. Back to Ninjobs: adoption on 2026-09-21 (ADR-0026). Ninjobs' own `/apply` had drifted from its docs: it still named a test device the project had replaced, and it described the environments as they were before a change the docs recorded. So the kit installs its commands unedited, and every project fact goes into docs/05, the slots. Keep it generic: no device, server or environment names.
  7. Key points. No exercises (Part I).
* Growth table, from the public repository `JCKodel/focus-kit`, one row per commit, every column measured the same way in every row, and the method given in a source note:

  | Commit | Date | Files | Lines | `/propose` | `/apply` |
  |---|---|---|---|---|---|
  | 0.1.0, `06e923f` | 2026-09-15 | 23 | 1,889 | 60 | 76 |
  | last before one file, `438d8b8` | 2026-09-19 | 133 | 33,581 | 190 | 147 |
  | one file, `9ffe9c7` | 2026-09-19 | 8 | /apply counts | /apply counts (`SETUP.md` §3.3) | /apply counts (§3.4) |

  Files is `git ls-tree -r <sha> --name-only | wc -l`. Lines is the sum of `wc -l` over those files. A command is `wc -l` of `skills/<name>/SKILL.md`, and at `9ffe9c7` it is the lines of its `SETUP.md` section, heading to the next `###`. /apply re-runs every cell and records any change. The prose or a note says that the peak's 133 files include the kit's own delivery pages under `work/`, and that the peak commit also shipped the same four commands a second time under `.claude/skills/`. The chapter does not repeat the README's "ten times longer": the counts give other ratios.
* Numbers in the chapter, and only these: the table; five reasons; eight files for one field; 29 checks; six places; the usage indicator's figures and year, if found; 10 and 47 lines; 32,861 lines deleted; 23 files of 0.1.0; the dates 2026-08-29, 2026-09-10, 2026-09-15, 2026-09-19 and 2026-09-21; chapter 1's figures only through its note.
* docs/03 terms used: focus-kit, command, project documents, page, delivery, queue, slot, governor, rules file, fresh session. No new term. "Weight" as chapter 3 used it; no coinage such as "ceremony".
* Sources, every URL at a full SHA:
  * `[^ninjobs-adr-0022]`: chapter 1's note, word for word, plus one sentence: the causes, the rejected alternative and the decision are the ADR's own, paraphrased.
  * `[^framework-usage]`: the public usage indicator for the frameworks, at its year and URL, checked on the day of /apply. Present only if found.
  * `[^ninjobs-adr-0026]`: Ninjobs, a private repository, its ADR-0026, dated 2026-09-21: the date of the public opening, the adoption and the drift.
  * `[^ninjobs-commands]`: Ninjobs, a private repository, `/propose` and `/apply` as they were before ADR-0026, counted with `wc -l` (10 and 47). ADR-0026 and the kit's README say 11 and 48; the book keeps its own count, as chapter 1 did.
  * `[^focus-kit-growth]`: https://github.com/JCKodel/focus-kit at `06e923f0334503b3930196fe7a76696945d50fff`, `438d8b8d8164151e5fd14cc41102a705b33ef1eb` and `9ffe9c7bb7a3c9644bf6bb3fc3ae97221dc8d41f`, with the table's method.
  * `[^focus-kit-one-file]`: the commit `9ffe9c7bb7a3c9644bf6bb3fc3ae97221dc8d41f` (its `--shortstat`: 32,861 deletions) and the README at that commit, for the five points.
* Nothing from Ninjobs is shown verbatim: its artifacts are in Portuguese and private, and appear paraphrased. The only text quoted is from the public kit, and only if a quotation carries more than a paraphrase. Nothing is quoted from the README paragraph on FOCUS, which names an earlier book (ADR-0005).
* Disclosure: from ADR-0022 and ADR-0026, only what this Contract names. No host, address, port, environment file, server topology, database or function name, folder of the private repository, or backup location. The disclosure scan runs over both editions and this page.
* Cases: Ninjobs only, as docs/03 allows. No Case A or B, so no OD-3 approval.

Files:

```
book/en/04-birth-of-focus-kit.md   chapter 4, no status: draft when done
book/pt/04-birth-of-focus-kit.md   chapter 4, no status: draft when done
docs/00-Product.md                 §Contents: chapter 4's title, if it changes
docs/06-Queue.md                   the M2 line reads "... and became one file" (drop "again"); birth-of-focus-kit [x]; M2's closing review (docs/05 §8) is then due
```

**Out of scope.**

* How to choose a stack for an agent: chapter 7 (queue line widened by this /propose). When the four pieces of FOCUS pay their way: chapter 15 (likewise). Chapter 4 gives each lesson in a sentence or two.
* Any claim that one stack is better than another: the chapter makes none.
* The earlier FOCUS book, or any material, as a cause: ADR-0005.
* Ninjobs' outcome numbers (deliveries, tests, lines of code): left out by the author; the appendix owns the case end to end.
* That several models reviewed the restart plan: not taken.
* Hosts and install: chapter 5. The governor in full: chapter 13. The command texts: chapters 10 and 11.
* The kit's commits between 0.1.0 and the peak one by one: the table's three rows carry the story.
* Correcting "11 and 48" in the kit's README and Ninjobs' ADR-0026: those are other repositories; the author decides there.

**Done when.**

* [x] Both editions of chapter 4 written, same headings in the same order, `status: draft` absent from both.
* [x] Opens with its value in at most three sentences; ends with at most five key points; no exercises.
* [x] No filler and nothing useful cut: every sentence read against docs/00 product question 2.
* [x] Every number is on the Contract's list and carries a source note whose text was found in the source; the table's cells repeat with its method.
* [ ] The stack and FOCUS paragraphs read by the author: no stack comes out better than another, and FOCUS comes out valuable and optional. (Written to that rule; only the author can tick this, in the review before the commit.)
* [x] No Ninjobs text quoted; no term of the disclosure list, no private path, host or folder name in either edition or on this page.
* [x] `make verify` green (build, parity, em dash, prose, links including the focus-kit URLs, disclosure).
* [x] `make book` builds; both PDF paths given to the author for review.
* [x] docs/06 line reworded and marked `[x]`; page moved to `work/done/birth-of-focus-kit.md` with what happened.

**What happened.**

* **The table, re-run on 2026-09-25.** 0.1.0 and the one-file commit match the page. The peak `438d8b8` has 135 files, not 133; lines 33,581 as planned. At `9ffe9c7`: 8 files, 1,575 lines, `/propose` 39 (`SETUP.md` §3.3, its heading through the line before §3.4) and `/apply` 47 (§3.4). The prose says 135. The peak's second copy of the four commands under `.claude/skills/` is confirmed; the count of `work/` files is left in words, since it is not on the numbers list.
* **What the peak added, corrected.** The Contract listed the installer CLI, the doctor, the knowledge graph and the version stamp as what the peak added. 0.1.0 already had all four (its installer script had a `doctor` subcommand, graphify and a version stamp). What the peak added was the self-test and the manifests, and a doctor and graph that did far more. The chapter says so, and adds a fact that sharpens the point: 0.1.0 already shipped the governor question in its process manual, so the growth skipped a question the kit itself held.
* **The usage indicator was found.** Stack Overflow Developer Survey 2024, all respondents, "extensive development work in over the past year": React 39.5% (web frameworks and technologies), Flutter 9.4% (other frameworks and libraries). The 2025 survey dropped the second list (no Flutter on the page) and the 2026 page answered 404 on 2026-09-25, so 2024 is the latest year with both. The note names the two lists; the prose calls it an indicator of use, not of training.
* **"The kit had shipped since 0.1.0"** and the five README points are paraphrased; nothing is quoted from the kit, since no quotation carried more than the paraphrase.
* **docs/03 terms.** All listed terms appear but "rules file": nothing in the chapter's story needed it (the move of Ninjobs' rules into its rules file is detail of ADR-0026 the Contract did not name).
* **The Ninjobs stack reason** is told as the ADR gives it (the build-and-look loop, the colour derived from a base colour); that React "matched at once" is told as "the same agent wrote the value", which is what the ADR records.
* **Proof.** `make verify` green; `make book` built both editions; the growth table checked on the English PDF page (six columns fit A5). No new kind of content, so no screenshots (docs/05 §5).
* **Term check.** The Portuguese draft said "spec" three times; docs/03 fixes "especificação", so the edition uses it. Chapter 1's Portuguese edition still says "linhas de spec": a finding for M2's closing review, not fixed here.
* **Nothing dropped** from the Contract. No document changed beyond docs/06: no new term, rule or decision. M2 is now complete, and its closing review (docs/05 §8) is due.

**Author's revision, 2026-09-25.** The author read the first version and found it too heavy: too many hedges, too many commit references, data the reader does not need. The chapter's job is one story, why Ninjobs left OpenSpec for what became focus-kit: how it was, what went wrong, where it went. Everything else is a detail and gets a few sentences. The chapter was rewritten to that, and this overrides the Contract above where they differ:

* Sections now: How it was, What went wrong, Where it went, Two lessons beyond the process (stack and FOCUS, a short paragraph each), Key points.
* Dropped: the kit that grew and the one-file commit (a pivot of the kit, history that adds nothing to the objective), with the growth table, its method and the notes `[^focus-kit-growth]` and `[^focus-kit-one-file]`; the Stack Overflow indicator and `[^framework-usage]`; the command line counts and `[^ninjobs-commands]`; the ADR's split of the five reasons.
* Kept, shortened: the drift found on adoption, in three sentences, since it is why a command holds no project fact.
* Numbers left: 29 checks, six places, eight files, chapter 1's fifteen days and four screens through its note, and the dates 2026-08-29 and 2026-09-10.
* The findings above on the table and the survey stay as the record of what was measured; the chapter no longer uses them.
* docs/06 line reworded to "why Ninjobs left OpenSpec, and the process that became focus-kit".
