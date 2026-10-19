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
* [x] Every Behaviour scenario is checked against the English and Brazilian Portuguese text; both editions are changed in the same delivery.
* [x] Each chapter opens with its reader value and retains its evidenced team gain; no filler and nothing useful cut; every number and quoted artifact remains sourced.
* [x] Terms follow docs/03, examples remain identified as written for the chapter, no em dash or private detail is introduced, and no run is narrated (docs/04).
* [x] `make verify` is green and `make book` builds both PDFs and EPUBs; the page records the results and gives the author both PDF paths for review (docs/05 §5).
* [x] Existing Case A passages remain intact; any changed passage drawn from them is listed and approved by the author (docs/00 OD-3).

**Build.** Chapter 17, both editions. The opening says the agent can read the material and the reader brings what it decides into the documents. In "The context folder", `/brainstorm` and `/analyze` read the folder whole when they start and no session rereads it on its own; the fines message changes nothing until the person asks for its reading, then the rule goes to docs/00, a new term to docs/03 and a new delivery to docs/06; `/propose` reads the decision, not the message; the ignored folder is read when asked, not every session, and needs its own backup; with no folder the agent has no correspondence, since it reads files, not a mailbox, and this book's public repository keeps `context/` out under its docs/05 Context slot. The second key point says the same in one line.

**Proof.** `make verify` green after the last edit. Every Behaviour scenario checked against both editions; claims match the installed brainstorm and analyze skills, their `references/documents.md` context entry, docs/05 §5 Context and docs/03. The Case A paragraph is unchanged, so no passage needs approval. `make book` and the PDF paths are the batch driver's, run once at the end: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Review.** One read-only Opus agent over both chapter files and this page. Applied: the line after the fines example repeated it, and became "Each new message or document goes the same way."; "a new term would go" became "goes" in both editions. `make verify` green again after the fixes.

**Decisions taken alone.** The work record's "kept up to date by the agent whenever a message goes out or an answer comes in", outside the page's sections, stays as it is: it describes what the agent does when the person brings a message, not an automatic read. The book's own Context slot is named in one sentence, since docs/05 is public and the reader can open it.

```commit
docs(ch17-context-read): read context/ at start and on request only

- /brainstorm and /analyze read context/ whole when they start
- a later message changes docs/00, docs/03 or docs/06 only when read on request
- an ignored folder is not reread every session and needs its own backup
- no folder means no correspondence; this book keeps context/ out

work/done/ch17-context-read.md
```
