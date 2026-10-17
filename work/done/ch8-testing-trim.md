# ch8-testing-trim

**Objective.** After chapter 8 a reader knows which test each of the four pieces gets, what a fake is and why it beats a mock, and why an agent's test must be seen red before it is trusted green, with the chapter opening on the agent that writes too many tests and saying each thing once.

**Behaviour.**

* A reader opens on the pain the chapter now keeps for its penultimate section: an agent writes a test in seconds, so it writes too many, the same case five ways, until nobody runs the suite before "done"; then the question of chapter 4, which broken rule would this test catch that no other does. The problem of the whole-application test follows as the second paragraph.
* A reader finds the TDD cycle taught here, once in the book, in "One rule through its tests": red, green, clean up, with `[^beck-tdd]`, and the `mayBorrow` test that chapter 5 used to show it moved here if the section lacks an equivalent (it has `lend refuses a member with an overdue book`; the chapter uses that one).
* A reader finds Meszaros's name once, with the sentence that this book calls stubs and fakes both fakes; Fowler's "Mocks Aren't Stubs" is kept for the mock's cost ("Coupling Tests to Implementations"), one citation.
* Failure: a reader looking for Beck in "Test names are sentences" finds the sentence without the third citation of the book; the rule stands on its own.
* A reader finds one gain section: "What this gives an agent" is folded into it; the "no baseline count" sentence is gone (the prologue says it once).
* Edge: "What tests prove, and what they do not" keeps red and green, the wrong test that passes, and the end-to-end gap; it loses only its first three sentences, which moved to the opening.
* Edge: the key points stay five; the last one loses the clause that repeats the proof.

**Contract.**

* **Chapter 8, both editions, file name and title kept.** Sections:
  1. Opening: unchanged in intent, three sentences.
  2. `## The problem`: new first paragraph from "What tests prove" (the three sentences from "For years the reason to have few tests" to "which broken rule would it catch"), then the existing paragraph on the whole-application test.
  3. `## A test for each piece`, `## Swap only I/O and the clock`: unchanged.
  4. `## What a fake is`: Meszaros's first sentence and the sentence on this book's use of "fake" kept; Fowler's summary of stub, mock and fake reduced to the mock's definition and the cost paragraph with `[^fowler-mocks]`.
  5. `## One rule through its tests`: gains, before its first test, the TDD cycle in three sentences with `[^beck-tdd]` (the text from chapter 5's "The rule is born with its test", shortened: red, green, clean up; a pure rule is the easiest place; the page's behaviours become red tests and "done" is green).
  6. `## Test names are sentences`: the Beck sentence removed.
  7. `## What tests prove, and what they do not`: its first three sentences removed (now the opening of the problem); "Red and green are how an agent's test earns trust" loses the pointer to chapter 5 and points to the section above.
  8. `## What the team gains`: the two paragraphs of "What this gives an agent" and the gain merged into one of at most four sentences; the baseline sentence removed.
  9. `## Key points`: five, the fourth shortened.
* **Notes:** `[^vitest]`, `[^playwright]`, `[^vocke-pyramid]`, `[^meszaros]`, `[^fowler-mocks]`, `[^beck-tdd]`, `[^cohn]` kept; each cited once in prose unless a second claim needs it; same count in both editions.
* **Pointers:** "chapter 5 showed the cycle" becomes this chapter's section; pointers to chapter 7 become chapter 6 only if `focus-and-slices` has run (checked by /apply; otherwise left for `renumber-chapters`).
* **Terms:** fake, test, piece, as docs/03 has them; unchanged.
* **Code:** unchanged blocks.
* **Cases:** none.

**Out of scope.**

* Chapter 5's TDD section: removed by `simplicity-and-results`; this page adds the cycle here so the book keeps it once. If this delivery runs first, chapter 5's section is left for that delivery to cut.
* The "no baseline" rule for other chapters: `one-gain-section`.

**Done when.**

* [x] Chapter 8 changed in both editions, same headings; opens with the agent that writes too many tests; the TDD cycle taught here; Beck cited once, Meszaros once, Fowler once; one gain section; no filler and nothing useful cut.
* [x] Parity of notes green.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* The opening pain: docs/04 §Value first and §Teach, do not report; the review found the chapter's best pain in its penultimate section.
* The TDD cycle lives in the testing chapter: DRY applied to the book; chapter 8 already says "red and green are how an agent's test earns trust".
* One gain section: docs/04 §A gain per chapter names one section.

**Decisions in the review.** None.

**Decisions made in /apply.**

* The opening gains a third sentence, the one thing the chapter now teaches anew: a test an agent wrote is trusted green only after it was seen red.
* The paragraph moved to `## The problem` had four sentences, not three; the first two became one, so the chapter 4 question, which the Behaviour names, stays and the paragraph is three sentences.
* Once the two paragraphs of `## The problem` sat together, both said "nobody runs it before saying done"; the whole-application paragraph now says it "takes minutes to start too" and "is skipped as well", and keeps the user who finds the broken rule.
* `## What a fake is`: Meszaros's second mention ("In Meszaros's names") became "In his names", and it carries the fake's definition that Fowler's summary held; the mock's definition joins "A mock does assert that"; the cost sentence names the article, since "the same article" lost its antecedent.
* The TDD cycle is chapter 5's text adapted to `lend` and to the use case's first test, with its "(chapter 14)" pointer for the delivery page, the chapter's only pointer to chapter 14; "done stops being the agent's opinion" went to the gain.
* "Red and green" points to "One rule through its tests" by name in prose, not by an anchor link: the book has no in-page links.
* The merged gain names the whole verify without a second link to chapter 15 (docs/04 §Chapter pointers, once per chapter per target); the link stays in "What tests prove".
* Key point four: the Edge says "the last one", the Contract "the fourth"; the fourth holds the proof clause, so "and keep the proof" is cut there.
* Pointers to chapter 7: `focus-and-slices` had already repointed both to `06-focus.md`; nothing left here.

**What happened.**

* `book/{en,pt}/08-testing-each-piece.md`: opening of three sentences; `## The problem` opens with the agent that writes too many tests and the chapter 4 question, then the whole-application test; `## What a fake is` cites Meszaros once and `[^fowler-mocks]` once, for the mock's cost; `## One rule through its tests` teaches red, green and clean up with `[^beck-tdd]`; the Beck sentence left `## Test names are sentences`; `## What tests prove, and what they do not` lost its first paragraph and points to the section above; "What this gives an agent" folded into `## What the team gains`, four sentences, the baseline sentence gone; key point four shortened. Code blocks and the table unchanged.
* docs/00 Contents names chapter 8 by title only; docs/04 §Chapter pointers already says "chapter 8's red and green cycle", which now holds. No other document changed.
* Dependents: `one-gain-section` also waits on `method-said-once`, `ch20-21-git-cut` and `ch22-26-team-cut`, so it keeps `[>]`; `renumber-chapters` does not name this slug.

**Proof.**

* Same nine H2 headings in both editions.
* Citations per edition, en and pt equal: `[^vitest]` 1, `[^playwright]` 1, `[^cohn]` 1, `[^vocke-pyramid]` 1, `[^meszaros]` 1, `[^fowler-mocks]` 1, `[^beck-tdd]` 1. In prose, Meszaros and Beck appear once each; Fowler twice, once as the owner of the site that hosts Vocke's guide.
* The Portuguese code keeps its names (`emprestar`, `emprestimoPedido`, `falsos`, `buscarMembro`).
* `make verify` green; `make book` built both editions, and the PDFs are `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

```commit
docs(ch8-testing-trim): chapter 8 opens on the agent that tests too much

- ch8: the problem opens with too many tests and the chapter 4 question
- ch8: the TDD cycle taught once, before the rule's tests
- ch8: Meszaros, Fowler and Beck cited once each
- ch8: one gain section; the baseline sentence gone
- both editions

work/done/ch8-testing-trim.md
```
