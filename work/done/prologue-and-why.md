# prologue-and-why

**Objective.** After the prologue a reader knows why a coding agent that writes fast still delivers late, what product, people and process each decide when some builders are agents, and which part of the book answers each, in one chapter instead of two, opening with the measured study and ending in the three pieces of a minimal process.

**Behaviour.**

* A reader opens the book and meets the METR trial before any definition: experienced developers measured slower with AI while they believed they were faster. From there the prologue names the three P's and what each one decides, in that order: the problem first, the frame second.
* A reader can say, after the prologue, the three things a minimal process gives an agent (a decision in writing, a limit on scope, a check before "done"), the three failures they answer, and that too much process fails too, with Ninjobs named as the case and chapters 3 and 9 as where it is told.
* A reader finds the three P's in three short sections, each one ending in the part of the book that answers it, and the parts map once, at the end of the prologue, in five lines.
* A reader finds the sentence that says Ninjobs's and Case A's repositories are private and every number about them was counted by the author, once, at their first mention; and the sentence that says the book measures no baseline for the practices of Part I, once, here, so no later chapter repeats it (the chapters that do, 2, 6, 7, 8 and 12, lose it in `one-gain-section` and `ch8-testing-trim`).
* Failure: a reader looking for the television story of Marcus Lemonis finds one sentence and the note; the five-line account is gone. A reader looking for "Nothing in this book is new" finds it gone; the sources in each chapter say it.
* Failure: the prologue's gain section no longer repeats the Ninjobs and Case A numbers before the reader knows what a delivery is; it keeps one number, the METR 19%, and the sentence that the gain the book is written for is the project that answers the whole team.
* Edge: the file keeps the name `00-product-people-process.md` and the title "Prologue: Product, people and process"; `01-why-process.md` is deleted in both editions and every link and mention of "chapter 1" in the book, docs/00 and docs/04 is resolved to "the prologue" until `renumber-chapters` closes the gap.
* Edge: chapters that pointed to chapter 1 for METR and DORA (chapter 2's rule of introducing an organization "in chapters 1 and 2", docs/04 §Teach, do not only show) now point to the prologue; chapter 3's and chapter 9's pointers from chapter 1's "Too much process" survive as pointers from the prologue.

**Contract.**

* **One file, both editions:** `00-product-people-process.md` rewritten from the two; `01-why-process.md` removed with `git rm`. H1 unchanged. The opening, at most three sentences: the agent writes faster than you can read, projects still arrive late, and after the prologue the reader can say why and what product, people and process each decide.
* **Sections, in order:**
  1. `## Speed moved the bottleneck`: from chapter 1 as it is (METR, then DORA), minus the lines "Typing is fast. / Deciding and checking are slow." which repeat the two before them.
  2. `## Three P's`: one sentence on where the idea comes from, with the note `[^lemonis-3ps]`, then the three subsections as H3: `### Product` (chapter 0's section, minus nothing), `### People` (chapter 0's section minus "Nothing in this book is new..." and the sentence after it), `### Process` (chapter 0's section; its sentence on too much process absorbs chapter 1's section "Too much process fails too": Ninjobs named, chapters 3 and 9 pointed).
  3. `## What goes wrong without a process` and `## What a minimal process is`: from chapter 1 as they are, the second ending with the sentence that focus-kit is built on the three pieces and Part II teaches it.
  4. `## What the team gains`: three sentences: where the team's time goes (METR's 19%, `[^metr-2025]`); the project that answers the whole team as the gain the book is written for (from chapter 0's Process section, moved here); and the one sentence that the book measures no baseline for the practices of Part I and says where each number it gives comes from. Then the two sentences on Ninjobs and Case A being private and counted by the author (kept, docs/04 §Source notes requires them here); the numbers "four screens in fifteen days", "73 deliveries on eight days" leave the prologue and stay in chapters 9 and 19, which tell them.
  5. The parts map, five lines, stays at the end of the gain section as today (docs/04 names it "the prologue's parts map"; ADR-0017 amendment keeps it there).
  6. `## Key points`: five, merged from both chapters' lists: the three P's; the measured trial; the three failures; the three pieces; the project that answers the team.
* **Notes:** `[^lemonis-3ps]`, `[^metr-2025]`, `[^dora-2024]`, the keys unchanged.
* **Pointers:** every `](01-why-process.md)` in both editions becomes a pointer to `00-product-people-process.md` or is cut where it only repeats (docs/04 §Chapter pointers); every "chapter 1" in prose becomes "the prologue". docs/00 Contents: Part I loses "1 Why process, when AI writes fast"; Audience: "chapters 1 to 3" becomes "chapters 2 and 3" until renumbering. docs/04's example "METR, DORA, Chroma, Liu's paper in chapters 1 and 2" becomes "in the prologue and chapter 2". docs/03 unchanged unless a row cites chapter 1 (checked by /apply).
* **Terms:** none new.
* **Sources:** the three above; nothing added.
* **Cases:** Ninjobs, by name, in one sentence; Case A, in the privacy sentence only.
* **Numbering:** chapter 2 keeps its number and file until `renumber-chapters`; the H1s are not touched here.

**Out of scope.**

* Renumbering 2 to 26: `renumber-chapters`.
* Cutting the "no baseline" sentence from chapters 2, 6, 7, 8 and 12: `one-gain-section` and `ch8-testing-trim`; this delivery adds the one sentence they will point to.
* Chapter 9's story and chapter 3's count: unchanged.

**Done when.**

* [x] One prologue in both editions, `01-why-process.md` gone from both, same headings in both; opens with METR; no filler and nothing useful cut (every claim of the two chapters is in the merged one or named as cut above).
* [x] No link to `01-why-process.md` and no "chapter 1"/"capítulo 1" left in `book/`, docs/00, docs/03 or docs/04; the list of the mentions resolved is on this page.
* [x] Every number sourced; the privacy sentence and the baseline sentence present once each.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* The prologue stays the prologue and absorbs chapter 1, rather than chapter 1 absorbing the prologue: docs/04 §Files says the file `00-` is the prologue and never chapter 0, and ADR-0017 says the project as the team's assistant is stated in the prologue.
* METR opens: docs/04 §Value first and §Say it where the doubt is born; the study is the only measured pain in the two chapters.
* The parts map stays: docs/04 and ADR-0017's amendment name it as the prologue's.
* The baseline sentence lives here: docs/00 product question 7 wants a gain per chapter with a number or one sentence saying it has none; the sentence that the book has no baseline for Part I is one fact and lives in one place (docs/04 §DRY, as chapter 4 applies it to a process).

**Decisions in the review.**

* The two hook numbers ("four screens in fifteen days", "73 deliveries on eight days") leave the prologue, as recommended; chapters 9 and 19 own them.

**What /apply did.**

* Both editions: `00-product-people-process.md` rewritten from the two chapters, in the Contract's order (Speed moved the bottleneck; Three P's with Product, People, Process as H3; What goes wrong without a process; What a minimal process is; What the team gains, with the parts map; Key points); `01-why-process.md` removed with `git rm`. H1 unchanged; same headings in both editions; METR opens the first section.
* Claims cut, as the page names them: the two lines "Typing is fast. / Deciding and checking are slow."; the television account of Marcus Lemonis (now one sentence and `[^lemonis-3ps]`); "Nothing in this book is new" and the sentence after it; the hook numbers "four screens in fifteen days" and "73 deliveries on eight days"; the DORA repeat and the "20% faster" half of the pair in the gain section (DORA stays in the body, METR's 19% is the gain's one number). Every other claim of the two chapters is in the merged prologue.
* Mentions resolved: the prologue's "chapters 1 and 9 show the second failure" became the Ninjobs sentence pointing to chapters 3 and 9 (chapter 1's two links kept); docs/00 Contents lost "1 Why process, when AI writes fast"; docs/00 Audience "chapters 1 to 3" became "chapters 2 and 3"; docs/04 §Teach, do not only show "in chapters 1 and 2" became "in the prologue and chapter 2"; docs/04 §Chapter shape "starting at chapter 1" cut. No file linked to `01-why-process.md`; docs/03 has no row citing chapter 1 (checked, unchanged).
* Case A passages, for the author's approval (docs/00 OD-3): one, the privacy sentence of the gain section: "Ninjobs and Case A, a client project that ran on the process and that chapter 19 tells, live in private repositories, so every number this book gives about them was counted by me over their histories." (pt: "A Ninjobs e o Caso A, um projeto de cliente que rodou sobre o processo e que o capítulo 19 conta, vivem em repositórios privados, então todo número que este livro dá sobre eles foi contado por mim ao longo dos seus históricos."), followed by "Ninjobs appears by name, and Case A without its owner, its client or its business." No Case B passage.
* docs/adr checked: no mention of chapter 1 or `01-why-process.md`.
* Mentions left, and why: docs/06's M1 line `chapter-template` ("proven by chapter 1, Why process") is a done line's history and outside `book/`, docs/00, docs/03 and docs/04; chapter 16's `[^toyota-kanban]` says "Chapter 1" of Toyota's own history; chapter 26's "1 to 5" is a score.
* Notes: `[^lemonis-3ps]` once, `[^metr-2025]` twice (the trial, the gain), `[^dora-2024]` twice (the body), keys unchanged. The privacy sentence and the baseline sentence appear once each, in the gain section.
* Proof: `make verify` green (build, parity, em dash, prose, links, disclosure); `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* Dependent lines: `renumber-chapters` and `one-gain-section` stay `[>]`; each still waits on other `after` lines.
* Divergences: the privacy sentence sits in the gain section, as the Contract says, while Ninjobs's first mention is now the Process subsection; that mention carries no number, so the sentence still precedes every number about either case, and docs/04 §Source notes now says "in its gain section, before any number about Ninjobs or Case A" instead of "at the first mention". Omissions: none.

**Decisions in /apply.** Chosen alone, as the batch rules say; corrections go in the review.

* The opening adds "and the three things a minimal process gives an agent" to the Contract's two clauses, so the first paragraph names what the Behaviour's second item promises; two sentences.
* The Three P's sentence keeps why product comes first ("the product is what everything else is judged by"), the one claim of the five-line account the section headings depend on.
* Chapter 1's reason why too much process fails ("every document is one more thing to write, read and keep true") is folded into the Process sentence with the Ninjobs case, and the chapter 18 pointer stays on the rule it questions.
* The Process paragraph on the project as the team's assistant stays in Process minus its last sentence; that sentence, merged with "the method is the same for one developer and for a company", is the gain's second sentence.
* The privacy sentence names Ninjobs and Case A and says what Case A is, since the sentence that introduced it left with its number; the Ninjobs URL moves to its first mention.
* The parts map's Part I line now starts "from how an agent sees a project", since the old start, why process matters, is the prologue now.
* Ninjobs is named in the Process sentence and in the two privacy sentences, which docs/04 §Source notes requires; the Contract's "in one sentence" is read as one sentence that tells its case.
* docs/04 §Chapter shape: "starting at chapter 1" cut rather than renumbered, so the sentence survives `renumber-chapters`.

```commit
docs(prologue-and-why): chapters 0 and 1 become one prologue

- the prologue opens with METR and DORA, then the three P's
- the three failures and the three pieces close it before the gain
- the gain keeps METR's 19%, the privacy and the no-baseline sentences
- 01-why-process.md removed; docs/00 and docs/04 point to the prologue
- both editions

work/done/prologue-and-why.md
```
