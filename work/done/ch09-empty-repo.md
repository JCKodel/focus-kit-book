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

* [x] Both editions answer all four scenarios without treating a README or installed skill as application code.
* [x] The opening value and evidenced team gain remain; there is no filler or useful content cut, and all existing numbers keep their sources.
* [x] No private-case passage is used, so OD-3 approval is inapplicable.
* [x] `make verify` and `make book` pass, and both PDFs are given to the author to review.

**Build.** Chapter 9, both editions: "The problem" now says that code chooses the command, `/brainstorm` for a repository with no application code yet, even one that already holds a README, notes or the kit's own files, and `/analyze` for a repository with code; and that a project already documented runs neither again when it updates the kit, with a link to chapter 8. The `/analyze` opening now says a repository that already has code, with or without a README or documentation of its own, in place of "something in it: code, documents, or both". In "What it reads", the clause "on a repository with no code the documents describe what the files say" is removed: it described `/analyze` on the repository the rule sends to `/brainstorm`, and the kit's analyze skill does not say it; "What the project does not have, it skips." stays. The `/brainstorm` opening already said "no code yet" and is unchanged.

**Proof.** focus-kit SETUP.md §1 step 5 (no code means `/brainstorm`, code means `/analyze`; an already documented project is not asked to repeat either) and §3.2, the analyze skill, which has no no-code case. Chapter 8's update passage carries the migration workflow; this chapter only points to it. Opening value, team gain and the Octoverse number with its source are unchanged.

**Review.** One read-only Opus agent over `git diff HEAD` of the two chapter files, against this page and docs/04. Points: (1) "with or without documents about it" could read as the project documents, inviting an already documented project to `/analyze`: now "with or without a README or documentation of its own", both editions. (2) the `/brainstorm` opening says "no code" where "The problem" says "no application code": kept, since the first choice settles the meaning and chapter 8 uses the same short form. The removed clause was judged right. `make verify` green after the fix.

**Decisions.** The distinction is said once, in "The problem", where the reader first chooses. `make book` and the PDFs are run once by the batch driver, which gives both PDF paths to the author.

```commit
docs(ch09-empty-repo): choose /brainstorm when a repository has no code

- chapter 9: code, not "something in it", chooses /brainstorm or /analyze
- a README, notes or the installed kit alone still mean /brainstorm
- a documented project updating the kit runs neither again (chapter 8)
- drop the unsourced /analyze case for a repository with no code
```
