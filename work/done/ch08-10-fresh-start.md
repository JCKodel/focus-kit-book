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
* [x] Every Behaviour scenario is checked against the English and Brazilian Portuguese text; both editions are changed in the same delivery.
* [x] Each chapter opens with its reader value and retains its evidenced team gain; no filler and nothing useful cut; every number and quoted artifact remains sourced.
* [x] Terms follow docs/03, examples remain identified as written for the chapter, no em dash or private detail is introduced, and no run is narrated (docs/04).
* [x] `make verify` is green and `make book` builds both PDFs and EPUBs; the page records the results and gives the author both PDF paths for review (docs/05 §5).
* [x] No new private-case passage or measurement is introduced; the install-to-start boundary is identical in both editions.

**Proof.** Scenario 1: chapter 8, Install, now ends with the agent naming `/brainstorm` on a repository without code, to type in a fresh session; chapter 10, new project, step 1 shows that naming and step 2 opens the fresh session before `/brainstorm`. Scenario 2: chapter 8 names `/analyze` the same way; chapter 10, existing project, step 1 shows it, step 2 keeps `context/`, step 3 opens the fresh session before `/analyze`. Scenario 3: chapter 8's update section, unchanged, still says an update reports migrations and never asks for `/brainstorm` or `/analyze` again; the new install paragraph speaks of a first install. Scenario 4: both chapters give `$brainstorm` and `$analyze` with no slug; chapter 8 says Copilot asks for none and its host sentence names `/propose` and `/apply` as the commands with a slug; no table row changed. Both editions carry the same sentences. `make verify` green after the last edit; `make book` is run once by the batch driver.

**Review.** One Opus context reviewed the hunks against this page and docs/04. Points and answers: the slug sentence before the host table implied every command takes one, now limited to `/propose` and `/apply`; Copilot asking for a slug read as general, the install paragraph now says it asks for none for these two; "names `/brainstorm` or `/analyze` in a fresh session" was ambiguous, now "to run in a fresh session"; two Portuguese steps chained "e ... e então", rewritten; a Portuguese wording drifted from the English, restored; the chapter link in the Install section became a plain "(chapter 9)" as the section does elsewhere.

**Decisions.** No reason for the fresh session is given in the install text: the source states the rule without one, and docs/03 already defines the term. Divergences: none.
