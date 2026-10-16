# ch14-propose-decides

**Objective.** After chapter 14 a reader knows that `/propose` decides what the project's documents already answer, writes each such decision on the page with the document it came from, and asks only where the documents leave more than one reading; that it drafts the Behaviour scenarios itself, each an action with a concrete input and the result the user sees, the cases that must fail and the edges included; and that the reader's work is to correct the page, not to write it, as focus-kit 2026.10.13 says.

**Behaviour.**

* A reader whose library's docs/00 says a loan lasts 21 days expects `/propose lend-book` not to ask the loan period: the page says "21 days ahead (docs/00)", and the reader corrects it in the review if docs/00 is wrong, instead of answering it twice.
* A reader asked "when does `/propose` ask?" answers from chapter 14: only where the documents leave more than one reading and none closes it, with its assessment and its recommendation first; "your call" stays a valid answer.
* Failure: a reader whose `/propose` asks "how many days does a loan last?" while docs/00 says 21 knows from chapter 14 that the agent asked what a document answers, and says so in the conversation.
* A reader of the example page finds five Behaviour lines, each with a concrete input and the result the user sees: the loan due 21 days ahead; the overdue member refused with "Return your overdue books first"; the suspended member refused with "Your membership is suspended" (new; the Contract already had `MemberSuspended` and Behaviour did not); the two librarians and the last copy; and the edge, a member whose only loan is due today borrows, since due today is not yet overdue (new).
* A reader asked "who writes the Behaviour lines?" answers: `/propose` drafts them from the documents, failures and edges included; the person corrects them and does not write them.
* Failure: a reader whose page holds only the happy path (an available copy lent to a member in good standing) knows from chapter 14's review questions to ask the agent for the cases that must fail and the edges before `/apply`.
* A reader reviewing the page checks, among the questions of "Read the page before `/apply`", that each decision taken from a document names that document and that they agree with it, and that Behaviour holds what must fail.
* A reader running `/propose return-book` while `lend-book` is not `[x]` knows from chapter 14 that the command does not start it, as for a `[?]` line, and says what it waits on (chapter 16); a dependency found only while defining makes the draft wait as `[?]` with `· resume: propose` and its reason.
* A reader knows `/propose` ends by showing the page's queue line, `[>] lend-book ...`, and asking them to read and question the page, then to run `/apply` in a fresh session.
* A reader of chapter 15's `lend-book, built` finds five tests, one per Behaviour line of chapter 14's page, not three.
* A reader looking for the source finds the kit's changelog, entries 2026.10.08.3 and 2026.10.08, named in plain words, and the file of `/propose`.

**Contract.**

* **Chapter 14, both editions, file name and title kept.**
  1. Opening: the reader can also expect `/propose` to decide what the documents answer, naming the source, and to draft Behaviour with failures and edges, which they correct.
  2. "What `/propose` does": the "asks only where..." sentence becomes: it decides what the documents already answer, writes the decision on the page naming the document, and asks only where they leave more than one reading, assessment and recommendation first; a correction happens once, in the review. The "or on another line not yet done" sentence is replaced: a line whose `after` is not `[x]` is not started, as a `[?]` line; a dependency or answer found missing while defining makes the draft `[?]` with `· resume: propose` (chapter 16). It ends by showing the page's queue line and asking for the review, then `/apply` in a fresh session.
  3. "The page": the Behaviour bullet reads: scenarios in user language, each an action with a concrete input and the result the user sees, the cases that must fail and the edges included; drafted by `/propose`, corrected by the person.
  4. Example page: Behaviour as in Behaviour above (five lines), "21 days ahead (docs/00)"; Done when's "three Behaviour lines" becomes "five". Messages as chapter 5 has them; pt: "A sua matrícula está suspensa", and the pt names already in the example.
  5. The paragraph under the example says where the decisions show their source (the 21 days, Out of scope's docs/00) and that the failures and the edge were drafted by the agent.
  6. "Read the page before `/apply`": the questions gain "Does each decision taken from a document name it, and do you agree?" and "Does Behaviour include what must fail and the edges?"; "Do you disagree with a choice the agent made on its own?" stays.
  7. "What the team gains": the kit's changelog paraphrased, no note (docs/04): entry 2026.10.08.3, a user measured the kit against working by hand on a copy of the same project and found it much slower, in part because `/propose` asked what docs/00 to 05 already settled; entry 2026.10.08, a person who did not know the tool being built left the expected result to the agent, which delivered one solution, happy path only, and the client rejected it. Case A's paragraph kept.
  8. Key points: the `/propose` point says it decides what the documents answer and names the source; a new point on Behaviour drafted by the agent, with failures and edges, corrected by the person.
* **Chapter 15, both editions:** line 69's list of tests gains the suspended member's refusal and the loan for a member whose book is due today; "Each Behaviour line becomes a test" stays. Nothing else in chapter 15 (`ch15-apply-ends` owns it).
* **Chapter 3:** unchanged; its note's example is already a failure case with a concrete input and the message the user sees (decided with the author).
* **Terms:** behaviour, page, free line, dependency, resume suffix, as docs/03 has them; docs/03 unchanged.
* **Sources:** the kit's CHANGELOG, entries 2026.10.08.3 and 2026.10.08, and the file of `/propose`, named in plain words, no note (docs/04); the plan-mode note kept.
* **Cases:** Ninjobs's two passages and Case A's paragraph, unchanged; no new private passage.
* **Code examples:** the example page and its Contract, written for the chapter on the lending library, said so; Portuguese names in the Portuguese edition.

**Out of scope.**

* Chapter 3's note: it already teaches behaviour with a failure case (author's choice).
* The commit block, staging and `/apply`'s next steps in chapter 15: `ch15-apply-ends`.
* "Each command names the next one as the host invokes it": `ch11-update-migrations`; chapter 14 says `/apply` comes next without the host forms.
* Code only inside `/apply`: `ch18-19-only-apply`.
* A new run or count: the changelog is the evidence (ADR-0017).

**Done when.**

* [x] Chapter 14 changed in both editions, same headings; opens with its value; no filler and nothing useful cut.
* [x] No sentence in the book says `/propose` asks what a document answers, or that it starts a line whose `after` is not `[x]`.
* [x] The example page has five Behaviour lines, Done when says five, chapter 15 names five tests, in both editions.
* [x] The changelog entries and the file of `/propose` named in plain words, no note to focus-kit's repository; every number and quote sourced.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* Two changelog stories as the evidence, Case A kept (asked; author chose).
* The example gains the suspended member and the due-today edge, with the 21 days sourced inline, and chapter 15's test list follows (asked; author chose).
* Chapter 3's note unchanged (asked; author chose).
* The not-started rule for an `after` line and the `· resume: propose` draft are taught here because chapter 14's current sentence, "or on another line not yet done", contradicts docs/05 §4; chapter 16 keeps the full rule (`ch13-16-queue-order`'s Out of scope).
* Showing the queue line at the end is taught here, since the file of `/propose` does it; the host's form of the next command stays with chapter 11 (docs/06, `ch11-update-migrations`).

**What happened.**

* Chapter 14, both editions: the opening gains a sentence on deciding and drafting; "What `/propose` does" says it decides what the documents answer, names the document, and asks only where they leave more than one reading, names the kit's file for the command as the source, ends by showing the page's `[>]` line and asking for the review and `/apply` in a fresh session, does not start a line whose `after` is not `[x]`, and saves a draft found waiting as `[?]` with `· resume: propose`; the page's Behaviour bullet, the five-line example with "21 days ahead (docs/00)", Done when's "five", the paragraph under the example, two review questions, two sentences after them for the agent that asks what a document says and the page with only the happy path, the changelog paragraph in the gain, and the key points.
* Chapter 15, both editions: the list of tests names five, adding the suspended member's refusal and the loan for a member whose only book is due today.
* The book's other mentions of `/propose` were searched; none says it asks what a document answers or starts a line whose `after` is not `[x]`.
* The queue line until kit-2026-10-16 said: chapter 14: /propose decides what the documents answer and names the source on the page; Behaviour with a concrete input, the result the user sees, the cases that must fail and the edges, drafted by /propose and corrected by the person; chapter 3's note if it needs it; both editions.

**Divergences.**

* Key points: the chapter had six, over docs/04's five; adding the Behaviour point would make seven, so the page format and the review surface share one point, and the Behaviour point carries "read the page before `/apply`". Five points, nothing dropped.
* The example block was rewrapped to docs/04's 74 columns where it was over: one line of the English Out of scope, and the Portuguese Contract, Visual reference, Out of scope and Done when, which were already over before this delivery.
* The Portuguese example block, 46 lines after the wrap (the English one has 39), no longer fits one A5 page: in the PDF it runs from page 105 to the first three lines of page 106, with no row wrapped or clipped. The English block fits page 100. Kept: shortening the Portuguese example would cut a Behaviour line or its message.

**Proof.**

* `make verify` green: build, parity, em dash, prose, links, disclosure.
* `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, and both EPUBs; the example page read in both PDFs as rendered.

**Decisions.**

* The edge and the failure lines are justified under the example from the Contract (`MemberSuspended`) and from the overdue rule, so the reader sees why the agent drafted them.
* No document changes: docs/03's terms and docs/05 already say what the chapter now teaches.
* No manual: nothing a person does by hand changed.


```commit
docs(ch14-propose-decides): teach /propose to decide and draft Behaviour

- chapter 14: /propose decides what the documents answer, naming the source
- example page: five Behaviour lines, failures and the due-today edge
- review questions for sourced decisions and the cases that must fail
- the kit's changelog as the gain; key points kept to five
- chapter 15: five tests, one per Behaviour line

work/done/ch14-propose-decides.md
```
