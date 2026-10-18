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

* [x] Chapters 22 to 26 changed in both editions, same file names and titles, headings as Contract; each opens with its value; nothing useful cut.
* [x] The checks of Contract hold; every note definition keeps a reference; `make verify` green.
* [x] No Case A or Case B sentence reworded; moved sentences listed on this page.
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Decisions in the review.**

* Chapter 23 §This book folds into §Case A's documents, as recommended.
* Chapter 26's card story closes with the protocol's second turn in the author's words, as recommended; /apply drafts the sentence and the author corrects it in the diff.
* Randazzo is removed, as recommended.

**Chapter numbers.** This page was written before `renumber-chapters`, and every chapter number above is the old one. /apply resolved each through the old-to-new table on `work/done/renumber-chapters.md` (the file slugs did not change): old 22 to 26 are now 20 to 24 (`20-team-tools.md`, `21-beyond-software.md`, `22-cost-and-where.md`, `23-adoption.md`, `24-asking-for-more.md`); old 12 is 9, old 14 is 12, old 16 is 14, and the quick guide, "the chapter after 12", is 10. The record below uses the new numbers. `ch26-what-counts` changed chapter 24 earlier in this batch; its two sentences (Skitka's group and noun, the cost arm's three runs) travel with their paragraphs word for word.

**What /apply did.** Both editions, same files, same H1s.

* Chapter 20: §Boards defines a kanban board in one sentence of its own; the Azure DevOps quotation and `[^azure-kanban]` leave (chapter 14 keeps its own copy of that note). "One piece was still unproven" leaves §Boards; the gain keeps "its write permission was never proven". §A mark for waiting is one sentence on Case A's `[?]` with the link to chapter 14, then the question-delivery sentence unchanged.
* Chapter 21: the States and Visual reference sentence leaves; §This book is gone as a heading and its content is a two-sentence paragraph at the end of §Case A's documents; the gain gains one sentence after the two counts pointing to Case B for what a page would have saved.
* Chapter 22: "It is my choice to compare it with nothing outside..." and "The next milestone of the same project... is the comparison that means something" leave §What a delivery cost on Ninjobs; §How a team decides gains, after "Then compare milestones, not vendors" and its paragraph, the one statement: "That is why I compare Ninjobs with nothing outside..."; the gain loses "There is no outside number to set it against, by choice"; the `countTokens` block is one sentence (count each pair of `message.id` and `requestId` once, since a streamed answer logs its usage on more than one line), and the Portuguese edition keeps that those names are the log's own fields; §Where an agent pays gains one "pays less" sentence from the 149 thousand output tokens per delivery the chapter already gives.
* Chapter 23: "My way works. It may." is now a plain answer in two lines; the two Case B sentences "The proposal itself did not run on the process. It had no queue and no page" are one link sentence to chapter 21, which says it did not run on the process; §One milestone as the pilot's quick-guide sentence names the guide's section for an existing project.
* Chapter 24: the opening is one sentence of value; §The card I accepted loses "Before agents, I could have done the same..." and "Models only amplify that behaviour" and ends with the sentence of the second turn; §The challenge protocol follows it, then §Why the first answer feels final (Randazzo's paragraph and `[^randazzo-hbs-26-036]` gone), §What the agent does not propose, and §What the protocol bought, and what it cost, whose session-limit story is one sentence; "The techniques... are taught elsewhere" leaves turn 3. The four messages are byte for byte as before in both editions (diffed against HEAD).

**Case A and Case B passages moved or shortened** (for the author's approval, docs/00 OD-3; none reworded beyond a cut or a join):

* Chapter 20 §A mark for waiting: "Case A's queue also lacked a word: five lines blocked on the client showed as work nobody had started, and Case A added a mark by hand, `[?]`, for a line waiting on a person." is cut to its second clause and joined with the kit's sentence: "Case A added a mark by hand, `[?]`, for a line waiting on a person, and the kit has its own, with the two other reasons a line waits ([chapter 14](14-queue-states.md) tells why)." Chapter 14 §The problem tells the five lines.
* Chapter 20 §Boards: "One piece was still unproven when the project closed: the write permission of the pipeline's identity on the board." leaves; the gain says it.
* Chapter 24 §The card I accepted: the two sentences of the author's reflection leave; the new last sentence, drafted by /apply for the author to correct: "The second of the four messages below would have made the agent test its claim and show me a card built from the client's PowerPoint before I accepted anything." (pt: "A segunda das quatro mensagens abaixo teria feito o agente testar o que afirmou e me mostrar um card construído a partir do PowerPoint do cliente antes que eu aceitasse qualquer coisa.")
* Chapter 23 §The shape of a pitch, Case B: "The proposal itself did not run on the process. It had no queue and no page, and [chapter 21] tells what that cost it." becomes "What the proposal itself lost with no queue line and no page to carry its findings, [chapter 21] tells."
* Chapter 21 §What the team gains, Case B, new: "Case B shows what a page would have saved: its analysis had none, and at least one of its six faults reached the next version of the proposal." (the facts of §Case B, the contrast; no new number).

**Checks of Contract.** `grep -c "randazzo" book/*/24-*.md`: 0 and 0. `grep -c "countTokens" book/*/22-*.md`: 0 and 0 (pt `contarTokens`: 0). `grep -c "nothing outside\|nada de fora" book/*/22-*.md`: 1 and 1, both in §How a team decides. Chapter 24: "## The challenge protocol" at line 18 before "## Why the first answer feels final" at line 55; pt "## O protocolo de desafio" at 18 before "## Por que a primeira resposta parece final" at 55. `azure-kanban` in chapter 20: 0 and 0. Every remaining note keeps a reference (parity green).

**Proof.** `make verify` green (strict build, parity, em dash, prose, links, disclosure); `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences.**

* The Contract says the `countTokens` block becomes one sentence "and the existing note to the run's record", and that the script "stays in `work/done/` where the run's record is". Chapter 22 has no such note and no run record in `work/done/` holds the script: the Ninjobs count is a private case, which takes no note (docs/04), and the prologue says the author counted it. The sentence carries no note, and the block is kept here, on this page in `work/done/`, as it was in the English edition:

  ```ts
  type Usage = {
  	input_tokens: number;
  	cache_creation_input_tokens: number;
  	cache_read_input_tokens: number;
  	output_tokens: number;
  };

  type LogLine = { requestId?: string; message?: { id?: string; usage?: Usage } };

  function countTokens(lines: LogLine[]): Usage {
  	const total: Usage = {
  		input_tokens: 0,
  		cache_creation_input_tokens: 0,
  		cache_read_input_tokens: 0,
  		output_tokens: 0,
  	};

  	const seen = new Set<string>();

  	for (const line of lines) {
  		const usage = line.message?.usage;
  		const key = `${line.message?.id}:${line.requestId}`;

  		if (!usage || seen.has(key)) continue;
  		seen.add(key);

  		for (const kind of Object.keys(total) as (keyof Usage)[]) {
        total[kind] += usage[kind] ?? 0;
      }
  	}
  	return total;
  }
  ```

* Behaviour says chapter 21's §This book becomes two sentences: "this book runs on the kit, and chapter 12 and the prologue say how". Neither old chapter 12 (now 9) nor the prologue says how this book runs on the kit, so the pointer would send the reader nowhere; the two sentences say how themselves (one page per chapter, the queue, `make verify` and its checks; done when green and the author approved the private passages).

Omissions: none.

**Decisions in /apply.** Chosen alone, as the batch rules say; corrections go in the review.

* Chapter 24's opening is one sentence that still says what the protocol is and under which section it is written, as `ch25-protocol-findable` decided; the definition of a turn moves to the first sentence of §The challenge protocol, which now comes right after the story; the experiment's 9 of 9 and 3 to 9 times leave the opening and stay in the gain, so the gain repeats nothing of the opening. The gain's three sentences are otherwise unchanged (`one-gain-section` reshapes gains and key points).
* "§Why the first answer feels final with Skitka and Dell'Acqua only" is read with the Contract, the exact section: only `[^randazzo-hbs-26-036]` leaves. Simon, Mosier and Manzey, and Lee each prove a different finding of the three, and key point 1 names them; Randazzo and Dell'Acqua proved the same point (consultants who take the answer unchecked), and Dell'Acqua carries the number the gain's sentence cites. Dell'Acqua's sentence now names the Boston Consulting Group, which "the same firm's" took from Randazzo's.
* After the move, the protocol's introducing line says the experiment is the one the chapter's last section reports, and turn 3's "two of the four things" says a section below names them; the four messages are not touched.
* Chapter 20 keeps the H3 §A mark for waiting and Case A's question-delivery sentence, word for word: chapter 21 points to chapter 20 for question deliveries, and chapter 14 tells only the `[?]` story.
* Chapter 22's one statement on comparing with nothing outside joins §How a team decides as the sentence after "Then compare milestones, not vendors" and its paragraph, so Behaviour's "once, in §How a team decides" holds and the reason (no other project measured the same way) is not cut. The sentence after it in §What a delivery cost on Ninjobs, "The next milestone of the same project... is the comparison", leaves too: it said what "Then compare milestones" says.
* Chapter 22's "pays less" sentence uses the 149 thousand output tokens per delivery and says the hours of deciding are in no column; no new number.
* Chapter 23's quick-guide sentence names the guide's section in words, with no anchor link: the book has none.
* Chapter 24's session-limit sentence speaks in the first person ("my plan"), as docs/04 Voice asks of the author's stories, and drops the host's quoted message, which docs/03 keeps.

```commit
docs(ch22-26-team-cut): chapters 20 to 24 say each source and gain once

- chapter 24: the challenge protocol follows the card story; Randazzo cut
- chapter 22: the token count in one sentence; "nothing outside" once
- chapter 20: kanban in the chapter's words; chapter 21: §This book folded
- chapter 23: plain answer to "my way works"; Case B said once, in 21
- both editions

work/done/ch22-26-team-cut.md
```
