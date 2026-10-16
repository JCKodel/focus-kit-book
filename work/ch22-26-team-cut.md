# ch22-26-team-cut

**Objective.** A reader of chapters 22 to 26 meets each source, each gain and each aside once, and finds the challenge protocol of chapter 26 right after the story that needs it; both editions.

**Decided from the documents.**
1. One source per point: where two or more studies prove the same claim, the chapter keeps the one that gives the number the gain uses and sends the others out, note and all (docs/04, Numbers that prove; a note only where the reader gains something to open).
2. A gain section says once what it says; a sentence of the gain that repeats the opening or the section before it leaves (docs/04, No filler).
3. The challenge protocol moves next to §The card I accepted: the story, then the four messages, then why the first answer feels final and what the agent does not propose, then what it bought and cost (docs/04, Teach, do not report: the reader's problem, the practice, then the evidence). Chapter 26's key point that names where the protocol is written moves with it (`ch25-protocol-findable` asked that the reader find it again).
4. Chapter 25's checklist and roles stay as they are: the step-by-step for an existing project is `quick-guide`'s, and chapter 25 points to it in one sentence (M15 paragraph; the quick guide is the chapter after 12).
5. Line numbers are not cited: `ch17-review-reads-code` (M14) touches chapter 25 before this line, and `ch15-24-whole-queue` touches chapter 24.

**Behaviour.**

* Chapter 22: a reader finds kanban defined in one sentence of the chapter's own, with no Azure DevOps quotation; finds "the write permission was never proven" once, in the gain; finds Case A's `[?]` as one sentence with the link to chapter 16, since chapter 16 §The problem tells it.
* Chapter 23: a reader finds no sentence on States and Visual reference being "none" (chapter 14 §The page says when they apply); finds §This book as one paragraph inside §Case A's documents or the opening, two sentences: this book runs on the kit, and chapter 12 and the prologue say how; the gain points to Case B for what a page would have saved, and keeps 16 of 73 and 6 of 93 as what was used.
* Chapter 24: a reader finds "I compare it with nothing outside" once, in §How a team decides, and not in §What a delivery cost on Ninjobs or in the gain; finds the `countTokens` code block replaced by one sentence (count each `message.id` and `requestId` pair once, since a streamed answer logs its usage more than once) and the note to the run's record, where the script stays; §Where an agent pays keeps the Flutter case and gains one sentence of where it paid less, from the Ninjobs numbers the chapter already has (no new number).
* Chapter 25: a reader finds §The resistance, and its answer with the three objections and their answers, "My way works. It may." rewritten as a plain answer; finds "The proposal itself did not run on the process" once, in chapter 23, and chapter 25 keeps the link; finds one sentence in §One milestone as the pilot pointing to the quick guide's existing-project column.
* Chapter 26: a reader finds the opening in one sentence of value; §The card I accepted without "Before agents, I could have done the same... Models only amplify that behaviour"; then §The challenge protocol; then §Why the first answer feels final with Skitka and Dell'Acqua only (Randazzo leaves with its note); then §What the agent does not propose; then §What the protocol bought, and what it cost with the session-limit story in one sentence and without "The techniques... are taught elsewhere"; a gain of three sentences that do not repeat the opening.
* The story of the card closes with what the protocol's second turn would have asked on it: one sentence, the author's own words, no new number.
* Fails: a study cut whose number a gain or key point still uses; a note definition left without a reference; the protocol's four messages changed in any word (they are the experiment's); a Case A passage reworded (OD-3).

**Contract.**

* **22**, both editions: §Boards: the Azure DevOps quotation and its note leave, one sentence defines a kanban board; "One piece was still unproven" leaves §Boards and stays in the gain; §A mark for waiting becomes one sentence with the link to chapter 16.
* **23**: §A delivery is anything with value that fits a page: the States and Visual reference sentence leaves; §This book merges into §Case A's documents as two sentences; §What the team gains: one sentence pointing to Case B after the two counts.
* **24**: §What a delivery cost on Ninjobs: "It is my choice to compare it with nothing outside..." leaves; §How a team decides keeps "Then compare milestones, not vendors" and the paragraph after it, which is the one statement; the code block becomes one sentence and the existing note to the run's record; §What the team gains: "There is no outside number to set it against, by choice" leaves, the gain keeps its one number (43.1 million tokens per delivery); §Where an agent pays: one sentence of "pays less" from the chapter's own numbers.
* **25**: §The resistance, and its answer: tone plain, three objections kept; "The proposal itself did not run on the process. It had no queue and no page" becomes the link sentence to chapter 23; §One milestone as the pilot: one sentence to the quick guide.
* **26**: sections in the order of Behaviour; §Why the first answer feels final keeps `[^skitka-1999]` and `[^dell-acqua-2026]`, `[^randazzo-hbs-26-036]` leaves with its paragraph; §What the protocol bought keeps `[^ask-for-more-run]`, the table and the 1-to-5 scoring, the session-limit story in one sentence; the key point naming where the protocol is written stays true after the move; the gain in three sentences.
* **Terms:** none new; docs/03 unchanged.
* **Sources:** `[^randazzo-hbs-26-036]` removed in both editions; the Azure DevOps note removed; every other note keeps a reference.
* **Cases:** Case A sentences move or shorten and are not reworded; Case B unchanged; the card story is the author's own and gains one sentence. No OD-3 approval needed unless the author asks for one on the moved Case A sentences.
* **Code examples:** the `countTokens` block leaves chapter 24; it stays in `work/done/` where the run's record is.
* **Checks:** `grep -c "randazzo" book/*/26-*.md` gives 0; `grep -c "countTokens" book/*/24-*.md` gives 0; in chapter 26 of both editions "## The challenge protocol" (pt its heading) comes before "## Why the first answer feels final" (pt its heading); `grep -c "nothing outside\|nada de fora" book/*/24-*.md` gives at most 1 per edition.

**Out of scope.**

* The milestone review in chapter 25 §Roles: `ch17-review-reads-code`.
* `/apply` reading the queue in chapter 24: `ch15-24-whole-queue`.
* The protocol's text and the experiment's numbers: unchanged (`plain-numbers` set them).
* A step-by-step for adoption on an existing project: `quick-guide`.
* The gain and key points as a shape: `one-gain-section`.

**Done when.**

* [ ] Chapters 22 to 26 changed in both editions, same file names and titles, headings as Contract; each opens with its value; nothing useful cut.
* [ ] The checks of Contract hold; every note definition keeps a reference; `make verify` green.
* [ ] No Case A or Case B sentence reworded; moved sentences listed on this page.
* [ ] `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Decisions in the review.**

* Chapter 23 §This book folds into §Case A's documents, as recommended.
* Chapter 26's card story closes with the protocol's second turn in the author's words, as recommended; /apply drafts the sentence and the author corrects it in the diff.
* Randazzo is removed, as recommended.
