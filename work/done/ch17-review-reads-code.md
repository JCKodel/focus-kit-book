# ch17-review-reads-code

**Objective.** After chapter 17 a reader closes a milestone the way the kit does today: the review's page takes the paragraph clause by clause, names the commit that closed the previous milestone, and the person both tests each clause by hand and launches the deep code review the Milestone review slot of docs/05 names; a finding the code review confirms is a `[ ]` line like the others, with no second review. Chapters 13 and 25 say the same where they point to the review.

**Behaviour.**

* A reader planning the lending library's first milestone writes `m1-review` as its last line and knows from chapter 17 that its page will hold two things: for each clause, the delivery that answers it and how a person tests it; and the commit the review runs against, the one that closed the previous milestone, or the first commit for a first milestone.
* A reader whose docs/05 says `Milestone review: /code-review ultra <base>` knows, from chapter 17, that they launch it themselves against that commit, that the agent may say it is time and never launches it, and that a finding it confirms becomes a `[ ]` line under the review line, exactly as a clause that failed in their hands.
* A reader whose docs/05 says `Milestone review: none` knows the hand test still runs, that the slot is the kit's place to name a deep review when the host has one, and that nothing else of the chapter changes for them.
* Failure: a reader who reads the eight findings of the Ninjobs opening and concludes that the kit's review would have missed them. Chapter 17 now says the opposite: those findings are what the look at the whole code finds and what testing clauses by hand never does, and that is why the review reads the code.
* Failure: a reader who, with a code review's findings in hand, asks the agent to fix them in the review's session. Chapter 17 still answers: a line, not a fix; each finding gets its own page, proof and commit.
* A reader of chapter 13's "The review, and its findings" and of chapter 25's roles finds the same two tests, by hand and by the deep review, and no sentence saying the review reads no code.

**Contract.**

* **Chapter 17, both editions, file name and title kept; headings kept except where named.**
  1. Opening, second sentence: "say why that review reads no code" becomes: say what the review reads, the paragraph by hand and the whole code through the host's deep review, and why its findings get no review of their own.
  2. "The review is a delivery": "It reviews no code and fixes nothing." becomes "It fixes nothing." The sentence after it, on where code is read, is replaced: the review also reads the code, the one look at the whole instead of a delivery, because every page can be right and the whole wrong; the page names the commit that closed the previous milestone, or the first commit, and the person launches against it the deep review that docs/05's Milestone review slot names, such as Claude Code's `/code-review ultra <base>`, or none when the slot says so; the agent may say it is time and never launches it. The staged change (chapter 15) and the pull request (chapter 22) stay as where each delivery's code is read.
  3. A new short section after "Test each clause by hand", `## Read the whole code once` (pt: `## Leia o código inteiro uma vez`): what the deep review is for, in the reader's terms: a call that takes hundreds of milliseconds, a page that can be framed, data sent where it should not go, a function reaching a network it should not, none of which fails a clause tested by hand; a finding it confirms is a finding like the others, and an unconfirmed one is not. The milestone example gains nothing: the `m1-review` block in "A line, and not a fix" keeps its five lines, since the finding shown comes from the hand test.
  4. "When the findings became one delivery": the sentence "That review read the code; the kit's milestone review reads none, since each delivery's code is read before its commit." becomes: that review read the code, and it is the reason the kit's review reads it too: every delivery had passed its own tests and its own review, and only the look at the whole saw the eight. The paragraph keeps its numbers (eight findings, 879 lines, 620 ms to 94 ms) and its lesson, one delivery instead of eight lines.
  5. "What the team gains": gains one sentence, that the deep review sees what no hand test can, the kind of fault the Ninjobs opening found; "This gain has no number in this book" stays.
  6. Key points: the second point drops "it reviews no code and fixes nothing" and reads: its page names the commit that closed the previous milestone, writes for each clause the delivery that answers it and how a person tests it, and fixes nothing; the third point gains: and launches the deep review docs/05's Milestone review slot names against that commit; a finding it confirms is a finding like the others.
* **Chapter 13, both editions**, "The review, and its findings": "It reviews no code and fixes nothing: a person tests each clause by hand." becomes: it fixes nothing: a person tests each clause by hand and launches the deep code review the project's docs/05 names, when it names one (chapter 17). Nothing else in chapter 13 changes here.
* **Chapter 25, both editions**, the roles list, "Who reviews the milestone": gains "and launches the deep code review of docs/05, when the project names one"; the pointer to chapter 17 stays.
* **Chapter 22:** unchanged; its pull request review is per delivery and does not describe the milestone review.
* **Portuguese:** "revisão de marco" as docs/03 has it; "revisão profunda do código" for the deep review; `/code-review ultra <base>` and the slot name `Milestone review` stay in English as docs/05's slot names do in the Portuguese edition (chapter 10's precedent); `m1-review` stays.
* **Terms:** `milestone review` row of docs/03 is updated by `kit-2026-10-16-2` (it is a process document, not the book); the chapter uses the term as that row will read. No new term.
* **Sources:** docs/05 §8 and §5's Milestone review slot, as the kit writes them; the kit's changelog paraphrased with no note, in the present tense, with no version named (docs/04, the kit as it is): the four kinds of fault above are the changelog's own examples from Ninjobs, which the chapter already tells as the opening's eight findings. No new number.
* **Cases:** Ninjobs, already in the chapter; the four faults are named by kind, with no path, no user and no vendor, as the changelog itself names them.
* **Code examples:** the two existing blocks, unchanged.

**Out of scope.**

* docs/05 §8, §5's slot and docs/03's `milestone review` row of this repository: `kit-2026-10-16-2`.
* The book's own `m14-review` and `m15-review` pages running `/code-review ultra`: their pages, when proposed.
* The milestone review as a kind of pull request review (chapter 22): the chapter stays per delivery.
* Chapter 17's "No second review": unchanged; the kit still says it.
* Any new count or run: the changelog's examples are the evidence (ADR-0017).

**Done when.**

* [x] Chapters 13, 17 and 25 changed in both editions, same headings plus the one new section in chapter 17; chapter 17 still opens with its value; no filler and nothing useful cut.
* [x] No sentence in the book says the milestone review reads no code; `grep -rn "reviews no code\|reads none\|não lê código\|nenhum código" book/` finds nothing on the milestone review.
* [x] The chapter's description of the slot matches docs/05 §5 and §8 as `kit-2026-10-16-2` leaves them, word for word where it quotes.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* Trunk, no branch: docs/05 §5 Git.
* The review reads the code, the page names the base commit, the person launches it, the agent never does, a confirmed finding is a line: SETUP.md's docs/05 §8 and the Milestone review slot.
* The reason given in the present, the fault a hand test never finds: docs/04, the kit as it is; the kit's changelog names the four kinds, from Ninjobs, and the chapter already tells that opening.
* A new section rather than a paragraph inside "Test each clause by hand": the hand test and the code review are two tests with two actors, and docs/04 asks to say what a thing is for where it is introduced.
* Chapter 22 untouched: its review is per delivery (docs/00's part plan, chapter 22's opening).
* Chapters 13 and 25 changed here so no chapter contradicts chapter 17 (precedent: `ch13-short-lines` adjusting chapter 19).

**Decisions in the review.**

* The new section shows the slot as one line, `Milestone review: /code-review ultra <base>`, with "or none" in prose, as recommended.

**What was built.**

* Chapter 17, both editions: the opening's second sentence says what the review reads; "The review is a delivery" says it fixes nothing, that it also reads the code, the base commit its page names, the slot's command (`/code-review ultra <base>`, or none) and that the agent never launches it, and keeps the staged change and the pull request as where each delivery's code is read; the new section `## Read the whole code once` (pt: `## Leia o código inteiro uma vez`) names the four kinds of fault by kind, shows the slot as one line written for the chapter, and says a confirmed finding is a line and an unconfirmed one is not; the Ninjobs paragraph gives that review as the reason the kit's review reads the code; the gain gains one sentence; key points 2 and 3 as the Contract words them.
* Chapter 13, both editions: "It fixes nothing: a person tests each clause by hand and launches the deep code review the project's docs/05 names, when it names one."
* Chapter 25, both editions: "Who reviews the milestone" gains the launch of docs/05's deep code review, when the project names one; the pointer to chapter 17 stays.

**Divergences.**

* Chapter 13: the Contract's "(chapter 17)" after the new sentence is not written, because the sentence before it already points to chapter 17 and docs/04 allows one forward pointer per target in a chapter.
* Chapter 17's Ninjobs paragraph: the Contract's new sentence already says that every delivery had passed its own tests and review and only the look at the whole saw them, so the old sentence saying the same is merged into it rather than kept beside it.
* Chapter 25: "and launches" became "and it launches", because the item's subject has no verb of its own for "launches" to follow.
* Portuguese: the slot is glossed once at its first use, "o slot Milestone review (revisão de marco)", and its value `none` once as "none (nenhuma)", following chapter 10's precedent.

**Proof.**

* `make verify` green (build, parity, em dash, prose, links, disclosure).
* `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, given to the author.
* `grep -rn "reviews no code\|reads none\|não lê código\|nenhum código" book/` finds only `book/pt/14-propose.md:127`, on a /propose page in Ninjobs that stopped before any code, which is not the milestone review.
* The slot as the chapter quotes it, "`/code-review ultra <base>`", and "the agent may say it is time and never launches it" match docs/05 §5 and §8 as `kit-2026-10-16-2` left them.

**Decisions.**

* The four faults are given by kind, in the reader's terms, with "hundreds of milliseconds" and no 620 ms: the number stays where the Ninjobs paragraph already gives it, and the page adds no number.
* No document, ADR or manual changes: docs/05 §5, §8 and docs/03's row already say what the chapter teaches; the author launches one command, which needs no manual.

```commit
docs(ch17-review-reads-code): the milestone review also reads the code

- chapter 17: the review reads the paragraph by hand and the whole code
- chapter 17: new section on the deep review and its slot, one line
- chapter 17: Ninjobs's eight findings are why the review reads code
- chapters 13 and 25: the person launches docs/05's deep code review

work/done/ch17-review-reads-code.md
```
