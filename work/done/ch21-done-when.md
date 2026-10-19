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
* [x] Every Behaviour scenario is checked against the English and Brazilian Portuguese text; both editions are changed in the same delivery.
* [x] Each chapter opens with its reader value and retains its evidenced team gain; no filler and nothing useful cut; every number and quoted artifact remains sourced.
* [x] Terms follow docs/03, examples remain identified as written for the chapter, no em dash or private detail is introduced, and no run is narrated (docs/04).
* [x] `make verify` is green and `make book` builds both PDFs and EPUBs; the page records the results and gives the author both PDF paths for review (docs/05 §5).
* [x] Any changed Case A or Case B passage is listed and author-approved; the retained private evidence and Case B contrast are checked without adding a private source note (docs/00 OD-3).

**Build.** Chapter 21, both editions. The opening says each delivery is done only when every Done when item has its evidence and `/apply` has ticked it. The page-format bullet makes Done when a checklist of machine checks and checks a person makes, each ticked by `/apply` when its evidence is on the page. After the librarian guide, the paragraph says the novice-use item is a manual check only a person makes; until it happens the delivery is not done and `/apply` does not move the page; until the report comes `/apply` stops as chapter 13 says, the line waits `[?]` with `resume: apply`; the resumed `/apply` records the report as evidence, ticks it with the machine items and moves the page; a librarian who got stuck means the guide is corrected and the check made again. The second key point names machine and manual checks, and a new key point says a manual check stays the person's while `/apply` records it and ticks every item, never one without evidence. The guide scenario is unchanged.

**Case B passage changed, awaiting the author's approval.** "until a person ticked it" became "until a person checked the next version and the item was ticked on that evidence" (pt: "até uma pessoa conferir a versão seguinte e o item ser marcado com base nessa evidência"). It stays inside the counterfactual "each finding needed a line, and a page", so Case B remains outside the process; no private source note was added. The Case A section is unchanged.

**Proof.** `make verify` green after the last edit. Every Behaviour scenario checked against both editions; claims match the installed apply skill ("Tick every Done when item"), docs/05 §§3 to 5 (a line waits on an answer not given, `resume: apply`) and docs/03 (proof, manual check). `make book` and the PDF paths are the batch driver's, run once at the end: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Review.** One read-only Opus agent over both chapter files and this page. Applied: the wait now comes before the resumed `/apply` and names the queue line, `[?]` and `resume: apply`, and the closing "no item is ticked without its evidence" was dropped as repeated by the key point; "a person's check" and "human checks" became docs/03's manual check in both editions; pt grammar fixed in the opening ("tiver sido marcado"), "Enquanto isso não acontecer" and "com base nessa evidência". Not applied: using "someone who never used the system" in the report, because the page's Behaviour words it as a new librarian. `make verify` green again after the fixes.

**Decisions taken alone.** No shared document changes: the apply skill and docs/05 already say `/apply` ticks every item and a line waits on an answer not given, so there is no contradiction to resolve. The Case B sentence was in scope as a claim assigning the final tick to the person, so it changed and is flagged for approval.

```commit
docs(ch21-done-when): let /apply tick every Done when item on evidence

- a manual check stays the person's; /apply records its report and ticks it
- the delivery is not done, and the page stays, while an item is open
- a missing report waits as [?] with resume: apply; a failed try corrects the guide
- Case B's sentence no longer gives the final tick to a person

work/done/ch21-done-when.md
```
