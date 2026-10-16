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

* [ ] Chapter 8 changed in both editions, same headings; opens with the agent that writes too many tests; the TDD cycle taught here; Beck cited once, Meszaros once, Fowler once; one gain section; no filler and nothing useful cut.
* [ ] Parity of notes green.
* [ ] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* The opening pain: docs/04 §Value first and §Teach, do not report; the review found the chapter's best pain in its penultimate section.
* The TDD cycle lives in the testing chapter: DRY applied to the book; chapter 8 already says "red and green are how an agent's test earns trust".
* One gain section: docs/04 §A gain per chapter names one section.

**Decisions in the review.** None.
