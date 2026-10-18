# ch10-explicit-staging

**Objective.** The reader can commit the kit and initial documents without accidentally staging unrelated files.

**Behaviour.**

* Following chapter 10's new-project step 3 after installation and `/brainstorm`, the reader stages only the actual files those operations produced, with explicit paths, and checks the staged diff before committing.
* Given an unrelated untracked note or an edited file inside a folder that also holds a kit file, the directions do not sweep it into the commit with a whole-tree or whole-folder add.
* Given unrelated entries already in the index, the reader recognizes that the proposed commit would include them and resolves ownership before committing, rather than assuming an explicit add cleared the index.
* Reading the existing-project steps that reuse the new-project instructions, the reader gets the same selective staging rule, not a second broad command.

**Contract.** Edit `book/en/10-quick-guide.md` and `book/pt/10-quick-guide.md`, new-project step 3 and any direct reuse of that step in the existing-project path.
Replace the positive instruction `git add -A` with explicit file selection from the installation's reported paths and the documents actually written; show a short explicit-file command as an example, identifying that it is a subset to adapt, not the complete install manifest.
Do not substitute `git add .`, a wildcard, or a command that stages an entire host folder containing unrelated work.
Sources: docs/05 §6 for explicit paths, mixed hunks and preserving pre-existing index entries; docs/03's stage and commit terms; focus-kit SETUP.md §1 for the install report.
Use the existing `git diff --staged` taught later in this chapter; no `git status` or run narrative in the chapter (docs/04).
The first document commit still has the chapter's subject-only example message and no delivery page, as its current step explains.
No new domain term, source note, measured number or case is needed.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing numbered guide.

**Out of scope.** Rewriting chapter 13 or 19's index teaching, changing installation, and performing a real commit are outside this correction.

**Done when.**

* [ ] Both editions satisfy the four Behaviour checks; no positive whole-tree staging instruction remains in the quick guide.
* [ ] The chapter keeps its opening value and evidenced team gain, no filler or useful detail is cut, and existing numbers and artifacts retain their sources.
* [ ] Examples fit the block-width convention; no private case is used, so OD-3 approval is inapplicable.
* [ ] `make verify` and `make book` pass, and both PDFs are given to the author to review.
