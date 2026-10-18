# ch09-empty-repo

**Objective.** The reader can choose the project-start command by whether a repository has code, even when a new project's folder already contains files.

**Behaviour.**

* Given an empty repository, the reader chooses `/brainstorm`.
* Given a repository containing only a README, notes or the installed kit, but no application code, the reader still chooses `/brainstorm`; "something in it" is not the test for `/analyze`.
* Given a repository with application code and no project documents, the reader chooses `/analyze` so the existing implementation informs its documents.
* An already documented project updating the kit is not told to recreate its documents; the text preserves the update distinction taught by chapter 8.

**Contract.** Edit `book/en/09-starting-a-project.md` and `book/pt/09-starting-a-project.md`, principally "The problem" and any directly conflicting choice sentence in the chapter.
Source: focus-kit SETUP.md §1 step 5 and the chapter's existing opening of `/brainstorm`: no code means `/brainstorm`, code means `/analyze`; installation updates report migrations for an already documented project.
SETUP.md version 2026.10.18.1 was read in the kit's working tree; the same no-code distinction is established by the installed commands and the chapter itself.
Terms remain docs/03's command and project documents.
Say the distinction where the reader first chooses, rather than adding a new decision tree or section; this follows docs/04's say-it-where-the-doubt-is-born rule.
No new count, source note, quoted artifact or case.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** Redesigning setup, defining software versus non-software adoption, or repeating chapter 8's migration workflow is outside this wording correction.

**Done when.**

* [ ] Both editions answer all four scenarios without treating a README or installed skill as application code.
* [ ] The opening value and evidenced team gain remain; there is no filler or useful content cut, and all existing numbers keep their sources.
* [ ] No private-case passage is used, so OD-3 approval is inapplicable.
* [ ] `make verify` and `make book` pass, and both PDFs are given to the author to review.
