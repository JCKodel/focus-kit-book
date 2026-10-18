# ch17-context-read

**Objective.** After chapter 17 the reader can put incoming material into the project documents at the right time without assuming every session rereads all correspondence.

**Behaviour.**
* Given `context/` exists when `/brainstorm` or `/analyze` starts, the reader expects the command to read it whole before asking questions already answered there.
* Given a later message says the library has no fines, storing it alone does not change a rule: the person requests its reading and the decision is written in docs/00; a new term goes to docs/03 and a delivery to docs/06.
* Given a later `/propose`, the reader expects it to read those documented decisions and does not infer an automatic reread of all messages.
* Given `context/` is ignored, the reader knows the local files remain readable on request and need their own backup; ignored does not mean automatically read each session.
* Given no context folder, the text promises no hidden correspondence or synchronized mailbox; this public book keeps the folder absent under its Context slot.

**Contract.** Files: `book/en/17-project-as-assistant.md` and `book/pt/17-project-as-assistant.md`. Sections: opening where needed, The context folder, affected key points. Sources: installed brainstorm and analyze skills, their `references/documents.md` context definition, docs/05 §5 Context, docs/03 (context folder and project documents). Preserve original-plus-whole-Markdown format, privacy boundary and request-driven ingestion. Decision: disk availability is not an automatic read trigger; the installed commands and template already settle it.

**States.** Inapplicable: chapter prose, no new screen.

**Visual reference.** Inapplicable: existing book layout, no new visual content.


**Out of scope.** Email tools, automated ingestion, creating context/ in this repository, status-session policy changes, new private case evidence.

**Done when.**
* [ ] Every Behaviour scenario is checked against the English and Brazilian Portuguese text; both editions are changed in the same delivery.
* [ ] Each chapter opens with its reader value and retains its evidenced team gain; no filler and nothing useful cut; every number and quoted artifact remains sourced.
* [ ] Terms follow docs/03, examples remain identified as written for the chapter, no em dash or private detail is introduced, and no run is narrated (docs/04).
* [ ] `make verify` is green and `make book` builds both PDFs and EPUBs; the page records the results and gives the author both PDF paths for review (docs/05 §5).
* [ ] Existing Case A passages remain intact; any changed passage drawn from them is listed and approved by the author (docs/00 OD-3).
