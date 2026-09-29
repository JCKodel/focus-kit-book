# kit-milestone-review-chapters

**Objective.** After this delivery a reader of chapters 7, 8, 9 and 12 knows that the last line of every milestone is its review, a delivery run with `/propose` and `/apply`, and that its confirmed findings open a milestone `<M>.1` right after, as focus-kit `bff8414` says. Chapters 12 to 15 name the clinic's milestones as its queue names them today.

**Behaviour.**

* A reader of chapter 7 who runs `/brainstorm` with the kit from `main` gets a first milestone with one more line than the one quoted, its review, and the chapter says so and why: the run predates the rule.
* A reader of chapter 8 who runs `/analyze` gets the same extra line, and the chapter says so in the same way.
* After chapter 9 a reader can say what the last line of a milestone is, and how the milestone of its findings is numbered, with this book's M3.1 and M4.1 as the example.
* After chapter 12 a reader can:
  * put a review line at the end of a milestone;
  * say what `/propose` and `/apply` do for it: the page names the range, the paragraph and the host's review; `/apply` checks the paragraph clause by clause, runs the review and stops at the decisions;
  * decide each finding;
  * turn the confirmed ones into the milestone `<M>.1`, with its paragraph and its own review line.
* The reader of chapter 12 still sees the clinic's real review, with its paragraph check, its command, ten findings, decisions and diff. The chapter says that review ran before the kit made it a line of the milestone, which is why the clinic's milestone 1 has none. After the diff it says that the kit now names that milestone 1.1, so nothing renumbers, and that the clinic's queue was renamed to match.
* Chapter 12's quote of docs/05 §8 is the rule at `bff8414`.
* Chapters 13, 14 and 15 call the findings milestone 1.1 and "the owner runs the day" milestone 2. Where a link opens `book-v1/closing-a-milestone`, which still shows the old names, the text says so.
* Every change is in both editions and means the same.

**Contract.**

* **Chapter 7, `07-brainstorm.md`**, after the quoted milestone 1 (en line 205, pt the same place): one or two sentences. The kit since `bff8414` ends the first milestone with its review, `m1-review` (chapter 12). This run used `e7607c5`, so the reader's queue has one more line. No new section.
* **Chapter 8, `08-analyze.md`**, after the quoted milestone 1 (en line 245): the same, pointing to chapter 12. No new section.
* **Chapter 9, `09-queue-and-milestones.md`**, §Milestones:
  * The size rule reads "three to eight deliveries, then its review".
  * One short paragraph: the last line of every milestone is its review, `<milestone>-review`, a delivery like the others (chapter 12). Its confirmed findings become lines in a new milestone right after, numbered with `.1`, so nothing renumbers. That milestone ends with its own review.
  * Example: the M3.1 and M4.1 of this book's queue, linked to <https://github.com/JCKodel/focus-kit-book/blob/main/docs/06-Queue.md>.
  * Key point 4 gains the review as the last line.
  * The sentence "Closing a milestone, and reviewing the whole, is chapter 12" stays or merges into the new paragraph.
* **Chapter 12, `12-closing-a-milestone.md`**:
  * Opening: "decide each finding" stays. The second sentence becomes: the confirmed findings become lines in a new milestone `<M>.1`, instead of fixes.
  * §Why review the whole: the quote of §8 becomes the rule at `bff8414`:
    * the last line of every milestone is its review, `<milestone>-review`, a delivery: `/propose` writes its page, `/apply` runs it;
    * it checks the paragraph clause by clause and reviews the code with what the host offers;
    * it fixes nothing;
    * each confirmed finding is a `[ ]` line in `<M>.1`, right after, which ends with its own review.
  * A few sentences, in §Why review the whole or at the start of §Check the paragraph, say what the review's page names: the range, the paragraph and the host's review command with its level. They also say what `/apply` does: the paragraph check, the review, then it stops for the decisions. And they say that the clinic's milestone 1 review ran before this rule, headless and not as a delivery, and that its steps are the ones `/apply` runs.
  * §Findings become lines:
    * The real diff stays, byte for byte, with the two sentences before it.
    * After it: under the rule since `bff8414` the new milestone is 1.1, ends with `m1.1-review`, and nothing renumbers. When the kit was updated, the clinic's queue was renamed to match, linked to <https://github.com/JCKodel/focus-kit-clinic/blob/a3e2470/docs/06-Queue.md>.
    * The pt edition's sentence that translates the new milestone's name (pt line 148) stays and gains the 1.1 name if it needs it.
  * §Key points: bullet 3 says the review is the milestone's last line, run with `/propose` and `/apply`. Bullet 5 says a confirmed finding becomes a line in `<M>.1`.
  * Exercises:
    * 12.1 stays.
    * 12.2: ask the agent for `m1-review` as the last line of your milestone 1, then `/propose m1-review` and `/apply m1-review`, and decide each finding with its reason.
    * 12.3: ask the agent to write the confirmed findings as milestone 1.1, with its paragraph and `m1.1-review` as its last line, and check the diff.
* **Chapter 13, `13-the-governor.md`**:
  * Line 65: "milestone 2" becomes "milestone 1.1", with a few words saying the tag still names it milestone 2 (chapter 12).
  * Line 88 (exercise): "your milestone 2 lines" becomes "your milestone 1.1 lines".
* **Chapter 14, `14-errors-and-slices.md`** line 268: "Milestone 3 brings `absences`" becomes "Milestone 2".
* **Chapter 15, `15-four-pieces.md`** line 9: "the clinic's first delivery of milestone 2" becomes "of milestone 1.1".
* **Terms of docs/03**: milestone review, finding, both already at `bff8414`. No new term.
* **Sources**: focus-kit `bff8414` (named in the text, no note); the clinic's docs/06 at `a3e2470` and this book's docs/06 (inline links). No new note.
* **Cases**: none. Ninjobs' paragraph in chapter 12 stays as it is.
* **Unchanged, checked**: chapter 10 lines 113 and 445 (its "milestone 2" is "the owner runs the day" again); chapter 11 lines 363 to 414; chapter 16.

**Out of scope.**

* A new recorded run of a clinic review as a delivery: the clinic's next review, `m1.1-review`, comes after its milestone 1.1 lines are built.
* The F17 of this book's M3 review as chapter 12's example of what the rule catches: the clinic's paragraph check already shows the clause-by-clause check. If wanted, it gets a line of its own.
* A page of a review shown in chapter 12 (such as this book's `m4-review`): the prose says what the page names; a real clinic review page comes with `m1.1-review`.
* Any tag, in the clinic or the fork: tags never move, and this delivery changes neither repository.
* Chapter 5: it installs the kit from `main`, which already is `bff8414`.
* docs/05 and docs/03: already follow `bff8414` since `kit-milestone-review`.

**Done when.**

* [x] Every Behaviour line checked by reading both editions of chapters 7, 8, 9, 12, 13, 14 and 15.
* [x] Both editions changed in the same places; each opens with its value; no filler and nothing useful cut; every number sourced.
* [x] `grep` finds no "milestone 3" (en) or "marco 3" (pt) for the clinic, and no clinic "milestone 2"/"marco 2" that means the findings milestone, in `book/`, outside what the contract keeps (see What happened).
* [x] `make verify` green (the two new links included).
* [x] `make book`; both PDF paths given to the author.
* [x] docs/06: `[x] kit-milestone-review-chapters`; page moved to `work/done/`; staged; commit message suggested; nothing committed.

## What happened

* **The kit commit of the runs.** The Contract said chapters 7 and 8 name the run's kit as `e7607c5`. The records say otherwise: `work/done/brainstorm-run/README.md` and `work/done/analyze-run/README.md` both give focus-kit `26e5e1e`; the clinic moved to `e7607c5` only after `/brainstorm` (`3f0b47c`). Asked, the author chose to name `26e5e1e`. Hash in the sentence, no note (docs/04).
* **Chapter 15 also says the tag keeps the old name.** Behaviour asked for that only where a link opens `book-v1/closing-a-milestone`; `book-v1/four-pieces`, which chapter 15 line 9 links, has the same docs/06 headings (milestone 2 the findings, 3 the owner's day), so chapter 15 gets the same parenthesis as chapter 13.
* **Chapter 12 also says it at its own tag link** (§Findings become lines, last paragraph): the tag's queue keeps the diff's names, since a tag never moves.
* **Exercise 12.2** reads "if your milestone 1 does not end with `m1-review`, ask the agent to add it", since a reader who installed the kit from `main` after `bff8414` already has the line (chapter 7 now says so).
* **Chapter 12's example of the numbering** is "milestone 1 is followed by 1.1" instead of the kit's M3, so it points at the clinic's case and does not echo the old milestone 3 of the diff.
* **Chapter 9's example.** M3.1 of this book's queue has no review line: it closed before `bff8414`. The text says so in one clause; M4.1 ends with `m4.1-review`.
* **Chapter 12, "It fixes nothing"** was said twice after the new quote of §8 (in the rule and in the next paragraph); the second one went.
* **The grep.** What remains, and stays by contract: chapter 12's sentence that the run "renumbered 'the owner runs the day' as milestone 3" and the diff's `## Milestone 2: what the review…` and `## Milestone 3: the owner runs the day` (both editions); chapter 7's diff `## Milestone 2: the owner runs the day` and chapter 10 lines 113 and 445, where milestone 2 is the owner's day, as today; chapters 13 and 15, where "milestone 2" is the tag's old name, said as such.
* **Proof.** `make verify` green, the link check online (both new URLs answered 200). `make book` built both PDFs and EPUBs; weasyprint's usual `user-select` warning only.
* No term, note, case or ADR added; docs/03 and docs/05 unchanged, as the page said.
