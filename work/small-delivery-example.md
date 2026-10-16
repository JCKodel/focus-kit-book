# small-delivery-example

**Objective.** A reader of chapter 13 sees a five-line delivery on the lending library from its queue line to its commit, and can say what the smallest page costs before the rule asks them to accept one; both editions.

**Decided from the documents.**
1. The example is `due-date-format`, the line chapter 13 §Changing the queue already writes: the loan screen shows the due date as day/month/year (docs/03 running example; the line is already "written for this chapter").
2. It is told in prose and in two excerpts, the page and the commit block, with no transcript, brief, diff or `git status` (ADR-0017; docs/04, No runs).
3. The page is written for the chapter, says so where it appears, and has every section of docs/05 §3 with Contract "none", States "the defaults" and Visual reference "none" (the kit's page shape; chapter 14 §The page teaches the sections).
4. The flow is the kit's as M14 leaves it: the line, `/propose due-date-format` in a fresh session, the page, `/apply due-date-format` in a fresh session, the stage, the person's commit (docs/05 §2 after `kit-2026-10-16-2`; this line runs after `method-said-once`, which runs after `m14-review`).
5. The cost is said in what the reader does, not in minutes: one `/propose` that reads the documents and writes a page of seven short lines, one `/apply` that changes one function and one test, one review of a diff of a few lines, one commit; no number is measured or invented (docs/04, Evidence: every number is real; there is no run to count, so there is no number).
6. The example goes in chapter 13 §Changing the queue, after the `due-date-format` line, replacing the sentence "The line gets what every delivery gets, a page, a proof and the person's commit" with the delivery itself; chapter 14 and 15 keep `lend-book` as their full example.
7. Portuguese names: `formato-devolucao` for the slug, as chapters 13 and 19 already have it; the page's prose in Portuguese; `· after` and the marks in English (docs/04, Evidence; chapter 13 already says so).

**Behaviour.**

* A reader who finishes §Changing the queue has seen: the line `[ ] due-date-format`; the page `work/due-date-format.md` of about seven lines, Objective (a member sees the due date as day/month/year on the loan screen), Behaviour (a loan due 2026-03-05 shows `05/03/2026`; a loan with no due date shows nothing), Contract none, States the defaults, Visual reference none, Out of scope (the date format of the overdue list, a line of its own), Done when (the two Behaviour lines pass as tests, verify green); the sentence that `/apply` changed the formatting function of the loan screen and one test, staged them with the page and the queue line, and suggested the commit; the commit block `docs(due-date-format): show the due date as day/month/year` in the format of docs/05 §6, with the body's one bullet and the page's path.
* The reader can answer "what did the rule cost here?": two short sessions and a commit, and in return a line in the queue that says the change exists, a page that says what it does and what it leaves out, and a test that fails if the format changes back.
* The reader can answer "what would editing the label on the spot have skipped?": the line, the page, the test and the review; the text says it in one sentence after the example.
* Failure: a page longer than the change it defines is wrong, and the example says so: a five-line change takes a seven-line page, and a page that grows past that is defining more than one delivery (chapter 14 §When it does not fit).
* Failure: the example must not show the agent's turns, the diff or the test's code; the chapter says what `/apply` changed, not how (ADR-0017).
* In Portuguese, the reader sees the same page with `formato-devolucao`, `05/03/2026`, "a tela do empréstimo mostra a data de devolução como dia/mês/ano", and the commit subject in English, as commit messages are (docs/04 §Languages: commit messages in English; the Portuguese edition says before the block that the message is in English, as it does for artifacts).

**Contract.**

* **Chapter 13, both editions**, §Changing the queue (pt §Mudando a fila), after the `due-date-format` line block: the paragraph "The line gets what every delivery gets..." becomes the example: one sentence that the line went through the whole method, then the page in a fenced block, introduced as written for this chapter, then one paragraph on what `/apply` did and the commit block, then one sentence on what an edit on the spot would have skipped. The rest of the section is as `method-said-once` and `ch13-14-19-line-stops` leave it.
* **The page**, English (the Portuguese edition translates it and says the original is in English, docs/04 Evidence):

  ```
  # due-date-format

  **Objective.** A member sees a loan's due date as day/month/year on the loan screen.
  **Behaviour.** A loan due 2026-03-05 shows 05/03/2026. A loan with no due date shows nothing where the date would be.
  **Contract.** None.
  **States.** The defaults.
  **Visual reference.** None.
  **Out of scope.** The overdue list's dates: a line of its own.
  **Done when.** The two Behaviour lines pass as tests; verify green.
  ```

* **The commit block**: subject `feat(due-date-format): show the due date as day/month/year`, one bullet, last line `work/done/due-date-format.md`; after it, the queue line as `[x] due-date-format`, one line.
* **Key points** of chapter 13: the point on code changing only inside `/apply` gains "even a five-line change gets its page" (pt "até uma mudança de cinco linhas tem sua página"); no new point.
* **Terms:** page, queue line, delivery, verify, as docs/03 has them; no new term.
* **Sources:** none; the example is written for the chapter and says so.
* **Cases:** none.
* **Code examples:** the page and the commit message, written for the chapter, on the lending library; no TypeScript shown.

**Out of scope.**

* The function and test that `/apply` would write: the chapter names them and shows neither (ADR-0017).
* Chapter 14's and 15's `lend-book`: the full-size example stays theirs.
* A measured cost in time or tokens: chapter 24 owns cost, and no run of this delivery exists to count.
* Chapter 19's manager session, which names `due-date-format` as the next free line: unchanged, it already matches.

**Done when.**

* [ ] Chapter 13 changed in both editions, same headings; still opens with its value; no filler, nothing useful cut.
* [ ] The page and the commit block appear once each, introduced as written for the chapter, in both editions; the Portuguese page says the original is in English.
* [ ] No transcript, diff, `git status` or commit hash in the text.
* [ ] `make verify` green; `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Decisions in the review.**

* The commit type is `feat`, as recommended: the example is a change to the library.
* The example ends with the `[x] due-date-format` line after the commit, one line, as recommended.
