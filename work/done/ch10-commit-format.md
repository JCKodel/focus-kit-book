# ch10-commit-format

**Objective.** After chapters 10 and 12 a reader looking for the format of a commit message goes to docs/05 §6, where the rest of the commit lives (what is staged, who commits, the message), and no longer to docs/04, which keeps naming, style and tests.

**Behaviour.**

* A reader asked "where does the format of a commit message live?" answers docs/05 §6, beside what is staged and who commits, from chapter 10's description of docs/05.
* A reader asked what docs/04 holds answers: the language of the documents and of the identifiers, naming, style and the tool that enforces it, where tests live and what each level tests; the commit format is not in the list.
* A reader running `/brainstorm` expects step 4, the conventions, to ask for the languages, the style and where tests live, and not for a commit format, as chapter 12 lists it.
* A reader with a new fact on how code or text is written (naming, style, tests) goes to docs/04 by chapter 10's question 5; that question no longer lists commits.
* A reader who opens a project's docs/04 on focus-kit 2026.10.13 and finds only "docs/05 §6 owns the commit format" sees what chapter 10 told them.
* Failure: no sentence in either edition says docs/04 holds the commit format or that `/brainstorm` asks for it in docs/04 (a search for "commit" near "docs/04" in `book/` finds none).

**Contract.**

* **Chapter 10, both editions, file name and headings kept.**
  1. "The seven documents", docs/04: the sentence ends at "what each level tests"; "and the format of a commit message" leaves.
  2. Same section, docs/05: "the commit" becomes "the commit and the format of its message" (pt: "o commit e o formato da sua mensagem").
  3. "Where a new fact goes", question 5: "naming, style, tests, commits?" becomes "naming, style, tests?" (pt: "nomenclatura, estilo, testes?"). No new question: the commit format is the kit's process, not a new fact of the project.
  4. Key points and "What the team gains" unchanged.
* **Chapter 12, both editions:** in "`/brainstorm`: a new project", item 4 loses "the commit format" (pt: "o formato do commit"), as the kit's file of `/brainstorm`, step 4, says: "commit format lives in docs/05 §6".
* **Terms:** none new; docs/04, docs/05 and slot as chapter 10 has them.
* **Sources:** docs/05 §6 of the kit at 2026.10.13 and the file of `/brainstorm`, named in plain words, no note (docs/04).
* **Cases:** none; no Case A or B, no Ninjobs passage.
* **Code examples:** none.
* **Queue:** the line's text gains chapter 12.

**Out of scope.**

* A gain for the move: chapter 10's thesis, one place per fact, already says why; the change corrects a sentence, it teaches nothing new.
* How an update reports the move of docs/04 as a migration: `ch11-update-migrations`.
* What docs/05 §6 says about staging and the message: chapter 15 teaches it (`ch15-apply-ends`).
* Chapter 12's `/analyze` reading the last fifty commit subjects: still true, it reads them to learn the project, not to write docs/04.

**Done when.**

* [x] Chapters 10 and 12 changed in both editions as the Contract says; same headings; no filler and nothing useful cut.
* [x] No sentence in the book says docs/04 holds the commit format.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* Chapter 12 enters this delivery: its item 4 says the same wrong fact, and the kit's file of `/brainstorm`, step 4, says the format lives in docs/05 §6. Correct here if you want chapter 12 on its own line.
* The format goes in chapter 10's description of docs/05, not as a new question in "Where a new fact goes": docs/05 §6 is the kit's section, "This section owns the commit format; docs/04 points here" (docs/05 §6), not a project slot.
* No gain section changed: AGENTS.md asks each chapter to say what the team gains, and chapter 10's already does; a one-phrase correction proves nothing new (ADR-0015, ADR-0017: as long as proving takes).

**Divergences.** None. The six sentences changed as the Contract says; headings, key points and gain sections untouched.

**Omissions.** None.

**Proof.** `make verify` green. `make book` builds; the author reviews chapters 10 and 12 in `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. A search of `book/` for "commit format", "formato do commit" and "format of a commit" finds only chapter 10's description of docs/05.

**Decisions.** None beyond those above. No document or ADR changes: docs/05 §6 already owns the format; no manual changes, nothing done by hand changed.

```commit
docs(ch10-commit-format): move commit format from docs/04 to docs/05

- chapter 10: docs/04 no longer lists the commit format; docs/05 does
- chapter 10: question 5 asks about naming, style and tests only
- chapter 12: /brainstorm step 4 no longer asks for a commit format
- both editions

work/done/ch10-commit-format.md
```
