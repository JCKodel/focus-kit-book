# two-choices

**Objective.** After chapter 6 the reader can say what the kit's two choices are, FOCUS and the git strategy, what each of their three answers means, and where the documents record the answer; chapters 7 and 8 point back to it.

**Behaviour.**

* The reader can expand FOCUS letter by letter (Feature-oriented, Clean, Unidirectional, Scalable) and say in one sentence what each letter gives.
* The reader can say what an orchestrator, a use case and a repository do, and that only the orchestrator has injected dependencies, which are the repositories.
* The reader can tell an exception (expected, at I/O, returned as a value) from an error (a bug, never caught) and knows the principle as "exceptions as values", which the field calls "errors as values".
* The reader can name the three FOCUS answers (whole, the two principles, neither) and the three git answers (trunk, a branch per delivery, a worktree per delivery), and in every git answer the agent never commits or merges.
* ~~The reader can say why Ninjobs is the warning: FOCUS required on every feature lost KISS and YAGNI~~ (dropped, see What happened); nothing exists for ceremony.
* A reader of chapters 7 and 8 finds a link back to the section where the choices first appear.

**Contract.**

* **Section.** `## The two choices` / `## As duas escolhas`, in `book/<edition>/06-the-documents.md`, after `### docs/06, the queue` and before `## ADRs`. Two paragraphs, FOCUS then git, plus at most one sentence of transition; no table, no code, no list of pieces with more than one sentence each.
  * FOCUS: the four letters, the three pieces behind the view, exceptions as values with the Dart split in half a sentence, "nothing exists for ceremony" with KISS, YAGNI and DRY, the three answers, where the answer is recorded (docs/01, and an ADR), and the Ninjobs warning pointing to chapter 4. Drivers, BLoC and Mediator, and the exhaustive switch stay in Part III.
  * Git: the three answers from the kit, who each suits, the agent never commits or merges, the answer recorded in the docs/05 Git slot and an ADR; this book's is trunk (ADR-0010, shown below in the chapter). Part IV teaches them.
* **Edits elsewhere in chapter 6.** The sentence in `### docs/01 ... docs/02` that announces the two choices becomes a pointer to the new section. The parenthesis after ADR-0010 that explains a worktree shrinks to a pointer, since the section defines it. The opening gains the two choices, still at most three sentences. Key points stay at most five: the choices enter by merging, not by adding a sixth. One new exercise, 6.4: pick an answer for each choice for the clinic, one reason each, then compare with the brief of chapter 7.
* **Pointers.** Chapter 7, the numbered list where the choices first appear (the line "How it is built (docs/01) ... FOCUS and the git strategy"), and chapter 8, the line "FOCUS and the git strategy. The default of each ...", link to `06-the-documents.md#the-two-choices` (pt: `#as-duas-escolhas`). The agents' quoted output in chapters 7 and 8 is not edited: it is real.
* **Terms of docs/03 introduced.** FOCUS (rewritten), view, orchestrator, use case, repository, exception, error, Result, exceptions as values, vertical slice (rewritten), KISS, YAGNI, DRY; driver is in docs/03 and not in the chapter. Portuguese terms as docs/03 fixes them; KISS, YAGNI and DRY get their expansion in parentheses on first use in both editions.
* **Sources.** focus-kit `SETUP.md` §Choices at 26e5e1e (the existing `[^focus-kit-documents]` note, the three answers of each choice); Dart API, `dart:core`, classes `Error` and `Exception` (a new source note `[^dart-error-exception]`, both URLs); ADR-0016 of this book (a new note `[^book-adr-0016]`, at the commit that adds it; /apply uses the staged file's path on `main` if the commit does not exist yet, and says so). The Ninjobs eight files stay cited in chapter 4, not repeated.
* **Cases.** Ninjobs only, as chapter 4 already tells it. No Case A or B.
* **Documents.** Already written by this /propose: docs/03, ADR-0016, and docs/06 (M4's paragraph and the `errors-and-slices` line, slug kept, now say "exceptions as values"). Left to /apply: docs/00 §Contents, chapter 14 becomes "Exceptions as values and vertical slices".
* **Exercises.** 6.4 as above; its answer is for the exercise-answers appendix.

**Out of scope.**

* Teaching FOCUS or git in depth: Parts III and IV do.
* Changing the kit's `SETUP.md` wording ("errors as values"): another repository; the book states the difference once.
* Editing chapter 4's Ninjobs passage: it already says FOCUS stayed useful and cost more applied everywhere.
* Renaming the slug `errors-and-slices`: slugs never change.
* Adding "branch per delivery" to docs/03: plain words in the chapter, no identifier.

**Done when.**

* [x] Both editions written, same heading structure; the section opens nothing new before the opening.
* [x] The chapter still opens with its value in at most three sentences; key points at most five.
* [x] No filler and nothing useful cut: the two paragraphs read against product question 2, sentence by sentence.
* [x] Every claim about the kit or Dart has its source note; ADR-0016 cited.
* [x] Links from chapters 7 and 8 resolve in both editions (strict build).
* [x] docs/00 §Contents renamed as in Contract.
* [x] `make verify` green; `make book`, and the paths of both PDFs given to the author.

**What happened.**

* **ADR-0016 note.** The staged file's path on `main` answers 404 until the author pushes, so `make verify` (link check) would stay red. The author chose to link the ADR folder on `main`, which resolves today, and name the file in the note: `[^book-adr-0016]` points at `tree/main/docs/adr`. A later delivery may pin it to the commit that adds the ADR.
* **`[^focus-kit-documents]` widened.** The note cited only `SETUP.md` §3.5; it now also names §Choices, the source of the three answers of each choice, same commit.
* **`[^dart-error-exception]`** quotes the two class descriptions of the Dart API (accessed 2026-09-28): an `Error` is "a program failure that the programmer should have avoided"; an `Exception` "is intended to be caught".
* **Ninjobs warning dropped, by the author's review.** The sentence "Ninjobs is the warning: FOCUS required whole on every feature lost KISS and YAGNI" read as if FOCUS were the problem; it is the solution, and the author let the complexity grow. It is out of both editions, and so is the Behaviour line about it. For the same reason the author had chapter 4's passage removed (it said FOCUS "applied everywhere cost more than it gave"), against this page's Out of scope: its section became "A lesson beyond the process" / "Uma lição além do processo", its fifth key point keeps only the stack, and the `four-pieces` line in docs/06 no longer cites "the Ninjobs lesson of chapter 4". ADR-0016 stays as written, by the author's choice.
* **Transition sentence** placed before the two paragraphs; each paragraph closes with the Part that teaches it.
* **The proof found a PDF defect.** `make book` failed to resolve the Portuguese link to `04-birth-of-focus-kit.md#duas-licoes-alem-do-processo`: MkDocs drops accents from heading ids, pandoc kept them. This is the first cross-chapter `#anchor` to an accented heading. Fix: pandoc reads with `+ascii_identifiers` (`scripts/build_book.py`), documented in docs/01's `make book` row. No new tool.
* **Git paragraph rewritten, and the kit with it, by the author's review.** The first text said `/apply` works on the branch, as the kit did, and did not say who each answer fits. The author's rule: the page `/propose` writes and the build `/apply` makes land in the same commit, so with a branch or a worktree `/propose` creates it before writing the page; trunk is only for one person working alone; a branch per delivery fits sequential work merged through a pull request; a worktree per delivery fits parallel work, after deciding which deliveries can run together; a strategy, not a silver bullet. The author chose to fix the kit too (against Out of scope): focus-kit `SETUP.md` §Choices, `/propose` (§3.3) and `/apply` (§3.4), and both READMEs, staged in `../focus-kit`, not committed. The new note `[^focus-kit-git]` links `SETUP.md` on the kit's `main`; pin it to the kit commit once it exists. The name stays "a branch per delivery"; git-flow in docs/03 keeps its own meaning. docs/03 gains "pull request" and trunk's row says it is for one person.
* **Pointers.** Chapter 7's numbered list and chapter 8's third point link to the section; the agents' quoted output ("errors as values" in both runs) is untouched.
* **Exercise 6.4 answer**, for the `exercise-answers` appendix: any answer with a reason holds; the clinic's brief in chapter 7 answers "FOCUS whole" (a small app whose rules, the 24-hour and slot rules, want pure functions and tests) and "trunk" (one person reviews each delivery).
* **Documents.** docs/00 §Contents: chapter 14 is "Exceptions as values and vertical slices". docs/01: the `make book` row. docs/03, ADR-0016 and docs/06 were written by /propose; docs/06 now marks the line `[x]`.
