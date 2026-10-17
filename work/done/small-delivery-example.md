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

* [x] Chapter 13 changed in both editions, same headings; still opens with its value; no filler, nothing useful cut.
* [x] The page and the commit block appear once each, introduced as written for the chapter, in both editions; the Portuguese page says the original is in English.
* [x] No transcript, diff, `git status` or commit hash in the text.
* [x] `make verify` green; `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Decisions in the review.**

* The commit type is `feat`, as recommended: the example is a change to the library.
* The example ends with the `[x] due-date-format` line after the commit, one line, as recommended.

**Chapter numbers.** This page was written before `renumber-chapters`; every chapter number above is the old one, and /apply resolved each through the old-to-new table on `work/done/renumber-chapters.md` (file slugs unchanged, only the prefix): old 13 is chapter 11 (`11-queue-and-milestones.md`), 14 is 12 (`12-propose.md`, so "chapter 14 §The page" and "§When it does not fit" are chapter 12's), 15 is 13 (`13-apply.md`), 19 is 17 (`17-project-as-assistant.md`, the manager session) and 24 is 22 (`22-cost-and-where.md`). The text above keeps the old numbers as the record of what was decided; what follows, and the book, use the new ones. The queue line keeps "chapter 13", since docs/06 keeps old numbers as history (`renumber-chapters`).

**Decisions taken by /apply** (batch run: no question asked, each the recommended choice).

* The commit subject is `Show the due date as day/month/year`, with no `feat(due-date-format):` prefix. The example lives in the lending library, a kit project, and its docs/05 §6 is the kit's format, which chapter 13 §The message teaches: an imperative subject, a scope in parentheses when it helps, and `Lend a copy to a member` as its example. The `<type>(<slug>):` prefix is this repository's docs/05 §6; shown in chapter 11, it would be a format the book never explains and chapter 13 then contradicts. The review's decision chose the type among this repository's types and did not weigh that; Behaviour's `docs(` and Contract's `feat(` disagreed as well. The page's "in the format of docs/05 §6" holds for the kit's docs/05: subject, one bullet, the page's path as last line.
* The Portuguese page and commit are in Portuguese, introduced as written for this chapter, with no "the original is in English". Chapter 12's `emprestar-livro` page and chapter 13's commit `Emprestar um exemplar a um membro` set that precedent, and docs/04 Evidence says the library speaks Portuguese in that edition since `author-review-1`; "the original is in English" is for a real English artifact (a rules file, a page of this repository), and this page has no English original. Behaviour's "the commit subject in English" and Done when's "the Portuguese page says the original is in English" were therefore not applied; Done when's second item is ticked with this record. The pt page uses chapter 12's section labels (Objetivo, Comportamento, Contrato, Estados, Referência visual, Fora do escopo, Pronto quando) and the slug `formato-devolucao`; the overdue list is `lista de atrasos`, as docs/03's slug `lista-de-atrasos`.
* The page carries the two details the section already puts in the draft (the narrow-screen rule and the catalog keeping year-month-day), so a reader finds on the page what `/propose` wrote from that draft: the first Behaviour line ends "on a narrow screen too", and Out of scope names the catalog's dates before the overdue list's. One sentence after the page says so. The objective (the reader sees the delivery whole and coherent) overrode the Contract's fixed text here.
* The page is shown in the shape of chapter 12's `lend-book` page, a blank line between sections and lines wrapped to 74 columns (docs/04, Width of a block), so the text speaks of "seven sections of a line or two" where the page said "about seven lines".
* Placement: the sentence "The line gets what every delivery gets..." left, and its last clause became the sentence after the example. The example comes after "The draft is where the detail waits" and "Saying define it now", not in the removed sentence's place, since those two sentences carry the draft to `/propose`, which is where the page begins; the section's rule sentences (every session, documents by conversation) follow the example unchanged.
* The failure line of Behaviour is one sentence with no pointer: chapter 12 is already pointed to in the section. It says "a page that needs more for a change this size is defining more than one delivery", since a page longer than five lines is right for a five-line change.
* The opening gains a third sentence, "And you can say what the smallest delivery costs, from its line to its commit", so the chapter opens with this new value too (docs/04, Value first; three sentences, the shape's limit).
* The commit's one bullet is "Show nothing where a loan has no due date", the highlight the subject does not already say.
* The gain is unchanged: it already says once that a change outside `/apply` "gets a page, a proof and the person's commit", as `method-said-once` left it; the example does not restate the rule.

**What happened.**

* Chapter 11 §Changing the queue, both editions: after the draft paragraph, one sentence that a change this small goes through the whole method; the page `/propose due-date-format` writes, introduced as written for this chapter; one sentence on what the reader sees in it; one paragraph on what `/apply` did (one function and one test, about five lines, verify, the move, the stage) and the commit block, introduced as written for this chapter, with the pointer to chapter 13 for its shape; the `[x]` line; the cost, what the rule gave in return, what an edit on the spot would have skipped, and the page's size as the failure line.
* Key points: the `/apply` point gains "even a five-line change gets its page" (pt "até uma mudança de cinco linhas tem sua página"); no new point.
* No transcript, diff, `git status`, commit hash or test code in the text; no TypeScript shown.
* docs/04 Evidence gains one sentence: a page or a commit message written for the chapter on the lending library is in the edition's language with no "original" note, and its commit follows the kit's format as chapter 13 teaches it, with no `<type>(<slug>):` prefix (first: `lend-book`; second: this delivery). The /propose of this page misread both, the error the sentence prevents (docs/05 §7). No other document changed. Chapter 17's manager session already names `due-date-format` as the next free line; unchanged.
* Dependents: `one-gain-section` lists `method-said-once` and others, not this line; no dependent line changes.

**Proof.**

* `make verify` green (strict build, parity, em dash, prose, links, disclosure); both editions keep the same headings.
* Every line of the new blocks fits 74 columns, in both editions.
* `make book` built both editions: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

```commit
docs(small-delivery-example): chapter 11 shows a five-line delivery

- ch11: due-date-format from its line to its page, build and commit
- ch11: what the rule cost, and what an edit on the spot skips
- ch11: opening and key point name the smallest delivery's cost
- docs/04: library examples in the edition's language, kit commit format
- both editions

work/done/small-delivery-example.md
```
