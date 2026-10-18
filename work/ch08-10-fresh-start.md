# ch08-10-fresh-start

**Objective.** After chapters 8 and 10 the reader starts `/brainstorm` or `/analyze` in a fresh session after installation.

**Behaviour.**
* Given a repository without code after setup, chapter 8 tells the reader to open a fresh session and invoke `/brainstorm` in the host syntax; chapter 10 makes that action explicit before its questions.
* Given a repository with code after setup, chapter 10 likewise opens a fresh session before `/analyze`, preserving its existing preparation of context material.
* Given an already documented repository being updated, the reader reviews migrations instead of restarting `/brainstorm` or `/analyze`.
* A Codex reader sees `$brainstorm` or `$analyze` with no delivery slug; references to the host table remain consistent without expanding its rows in this delivery.

**Contract.** Files: `book/en/08-install-and-hosts.md`, `book/pt/08-install-and-hosts.md`, `book/en/10-quick-guide.md`, `book/pt/10-quick-guide.md`. Sections: chapter 8 install and next-command explanation; chapter 10 new-project and existing-project steps and affected key points. Source: focus-kit `SETUP.md`, install step 5, version 2026.10.18.1 read from the local source checkout on 2026-10-18; the source is uncommitted, so no commit identifies it. It explicitly requires a fresh session for both initial commands. docs/03 defines fresh session; docs/04 requires describing the current rule without a version-history narrative. No new terms or cases.

**States.** Inapplicable: chapter prose, no new screen.

**Visual reference.** Inapplicable: existing book layout, no new visual content.


**Out of scope.** Host table corrections, update-report version, staging commands and the separate proposal-session policy are other queue lines. No install, migration or skill changes.

**Done when.**
* [ ] Every Behaviour scenario is checked against the English and Brazilian Portuguese text; both editions are changed in the same delivery.
* [ ] Each chapter opens with its reader value and retains its evidenced team gain; no filler and nothing useful cut; every number and quoted artifact remains sourced.
* [ ] Terms follow docs/03, examples remain identified as written for the chapter, no em dash or private detail is introduced, and no run is narrated (docs/04).
* [ ] `make verify` is green and `make book` builds both PDFs and EPUBs; the page records the results and gives the author both PDF paths for review (docs/05 §5).
* [ ] No new private-case passage or measurement is introduced; the install-to-start boundary is identical in both editions.
