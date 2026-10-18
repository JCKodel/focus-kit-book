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

* [x] Both editions satisfy the four Behaviour checks; no positive whole-tree staging instruction remains in the quick guide.
* [x] The chapter keeps its opening value and evidenced team gain, no filler or useful detail is cut, and existing numbers and artifacts retain their sources.
* [x] Examples fit the block-width convention; no private case is used, so OD-3 approval is inapplicable.
* [x] `make verify` and `make book` pass, and both PDFs are given to the author to review.

**Build.** Chapter 10, both editions: new-project step 3 now has the reader fix the documents, then stage by name only the files the install reported and the ones `/brainstorm` wrote, never `git add -A`, `git add .` or a whole folder such as `.claude/`; a short `git add` block of explicit files, said to be a part of the list to complete from the install's report and `/brainstorm`'s files; reading the index with `git diff --staged` as step 7 does, where a file neither wrote is not this commit's even if staged before, naming paths does not take it out, and the reader finds its owner and takes it out with `git rm --cached <path>`, since `git restore --staged` (chapter 19) needs a first commit; the subject-only message is unchanged; the "You see" line says the kit's files in the host's folders and nothing else. Existing-project step 4 reuses step 3 and now says to stage by name only what the install and `/analyze` wrote, and its "You see" line matches step 3.

**Proof.** docs/05 §6 (explicit paths, never `git add -A` or `git add .`, report pre-staged entries); docs/03's stage; focus-kit SETUP.md §1 step 5 (the install tells which files it wrote) and §3.1 (`work/done/` with a `.gitkeep`). The review checked in a fresh repository that `git diff --staged` lists entries staged before any commit and that `git restore --staged` fails with no `HEAD`.

**Review.** One read-only Opus agent over `git diff HEAD` of the two chapter files, against this page and docs/04. Points: (1) `git restore --staged` fails before the first commit: replaced by `git rm --cached <path>`, with a clause that `git restore --staged` needs a first commit. (2) the pt block named `docs/06-Queue.md`, whose name follows the documentation language: the example now names only language-neutral files, both editions. (3) the list to complete named only the install: now also the files `/brainstorm` wrote. (4) existing-project step 4 still said "the host's folders": now "the kit's files in the host's folders". (5) "neither of them" was ambiguous: now names the install and `/brainstorm`. (6) pt "esperar o próprio commit": now "ficar para um commit próprio". (7) untagged fence: kept, as chapter 19 does. `make verify` green after the fixes.

**Decisions.** The example block omits any docs/0N file, since its name differs by documentation language. `make book` and the PDFs are run once by the batch driver, which gives both PDF paths to the author.
