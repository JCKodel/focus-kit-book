# ch21-done-when

**Objective.** After chapter 21 the reader can finish a non-software delivery only when every Done when item has evidence and `/apply` has ticked it.

**Behaviour.**
* Given the librarian guide whose PDF builds and refusal list is complete but whose novice-use check has not happened, the reader says the delivery is not done; `/apply` cannot leave that item for a later tick and call the delivery complete.
* Given the person reports that a new librarian lent a copy using the guide alone, `/apply` records that evidence and ticks the manual item as well as the machine checks before moving the page.
* If the manual check fails or the required answer has not arrived, the chapter directs the reader to correct or wait through the existing process, never fabricate proof or tick an unchecked condition.
* The opening, page-format definition, guide explanation and key points distinguish the person performing or confirming a check from `/apply` recording all completed checklist items.

**Contract.** Files: `book/en/21-beyond-software.md` and `book/pt/21-beyond-software.md`. Sections: opening, A delivery is anything with value that fits a page, the librarian-guide example and its explanation, affected key points and any claim that assigns final ticking to the person. Sources: installed apply skill ("Tick every Done when item"), docs/05 §§2 to 5, and docs/03 (proof, delivery). Keep the existing guide scenario and Case B explicitly outside the process. No invented experiment or result; all examples are instructional. Decision: human checks remain human, their evidence is recorded by `/apply`.

**States.** Inapplicable: chapter prose, no new screen.

**Visual reference.** Inapplicable: existing book layout, no new visual content.


**Out of scope.** Changing the kit or inventing automation for human judgment; new case facts or guide implementation.

**Done when.**
* [ ] Every Behaviour scenario is checked against the English and Brazilian Portuguese text; both editions are changed in the same delivery.
* [ ] Each chapter opens with its reader value and retains its evidenced team gain; no filler and nothing useful cut; every number and quoted artifact remains sourced.
* [ ] Terms follow docs/03, examples remain identified as written for the chapter, no em dash or private detail is introduced, and no run is narrated (docs/04).
* [ ] `make verify` is green and `make book` builds both PDFs and EPUBs; the page records the results and gives the author both PDF paths for review (docs/05 §5).
* [ ] Any changed Case A or Case B passage is listed and author-approved; the retained private evidence and Case B contrast are checked without adding a private source note (docs/00 OD-3).
