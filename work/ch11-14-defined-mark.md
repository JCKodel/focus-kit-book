# ch11-14-defined-mark

**Objective.** After chapters 11 and 14 the reader can distinguish a saved draft from a completely defined delivery ready for `/apply`.

**Behaviour.**
* Given `[ ] due-date-format` and a draft in `work/`, the reader says the delivery is not defined and starts `/propose`; the file alone does not authorize `/apply`.
* Given a page with all sections filled or explicitly inapplicable and no unresolved scope decision, the reader explains why `/propose` marks `[>]` and `/apply` may then start if dependencies are done.
* Given a page with an unanswered scope question, the reader does not call it `[>]`: active definition is `[~]`, and a missing requested answer invokes the waiting rule.
* The chapter 11 milestone explanation no longer infers that a `[ ]` line has no page; the chapter 14 mark table says completely defined and ready for `/apply`.

**Contract.** Files: `book/en/11-queue-and-milestones.md`, `book/pt/11-queue-and-milestones.md`, `book/en/14-queue-states.md`, `book/pt/14-queue-states.md`. Sections: chapter 11 marks and milestone interpretation; chapter 14 six marks and affected key points. Sources: docs/05 §§3 and 4, docs/03 (mark, draft page and page), and the installed propose and apply skills; these already distinguish a complete definition from a file that exists. No new term or case evidence. Decisions follow the existing documents; no scope question remains.

**States.** Inapplicable: chapter prose, no new screen.

**Visual reference.** Inapplicable: existing book layout, no new visual content.


**Out of scope.** Session policy, queue placement, blocked-line return and board placement belong to their own queued deliveries. Existing private-case passages and numbers stay intact.

**Done when.**
* [ ] Every Behaviour scenario is checked against the English and Brazilian Portuguese text; both editions are changed in the same delivery.
* [ ] Each chapter opens with its reader value and retains its evidenced team gain; no filler and nothing useful cut; every number and quoted artifact remains sourced.
* [ ] Terms follow docs/03, examples remain identified as written for the chapter, no em dash or private detail is introduced, and no run is narrated (docs/04).
* [ ] `make verify` is green and `make book` builds both PDFs and EPUBs; the page records the results and gives the author both PDF paths for review (docs/05 §5).
* [ ] Existing Case A evidence is retained; any changed passage drawn from it is listed for the author and approved before completion (docs/00 OD-3).
