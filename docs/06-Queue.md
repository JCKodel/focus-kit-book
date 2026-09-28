# Queue

`[ ]` not yet defined · `[>]` defined, `work/<slug>.md` exists · `[x]` done, page in `work/done/`.
A line never leaves; it changes mark.

## M1. The book stands up

When this milestone closes, a chapter written in both languages builds into the website and into PDF and EPUB, `make verify` guards the build, the parity of the editions, the prose and the disclosure list, `main` publishes itself to GitHub Pages, a tag produces a Release, and the brownfield project is chosen.

```
[x] site-skeleton          MkDocs Material bilingual site, one placeholder chapter per edition, draft marker, make serve and make verify (strict build, parity, em dash)
[x] license-and-readme     AGPL-3.0 for scripts and code, CC BY-SA 4.0 for the text; README in English and Portuguese
[x] disclosure-scan        make scan against the out-of-repo disclosure list, locally and in Actions, part of make verify
[x] prose-rules            the anti-AI prose rules written in docs/04 and checked by make verify
[x] link-check             external links in the book checked, part of make verify (the strict build already fails on broken internal links)
[x] chapter-template       the chapter shape fixed, proven by chapter 1, Why process, written in both editions
[x] pdf-epub               make book produces PDF and EPUB in both editions from the same source
[x] pages-and-release      Actions publish the site on push to main and a Release with PDF and EPUB on a v* tag
[x] brownfield-research    three to five open-source candidates compared; the author picks one (OD-1); fork and tag
```

## M2. Part I, Foundations

When this milestone closes, a reader who has never followed a process knows why product, people and process decide a project built with agents, why a coding agent needs written context, what Spec-Driven Development is, and why focus-kit exists.

```
[x] product-people-process Prologue: product, people and process (Marcus Lemonis's three P's) applied to software built with agents, each pointed to the part of the book that answers it; Case B in one sentence
[x] how-agents-see         Chapter 2: statelessness, context window, context rot, fresh sessions, from primary sources
[x] spec-driven-run        Spec Kit, OpenSpec and focus-kit run on the same feature and brief; files, lines and words counted and committed for chapter 3
[x] spec-driven            Chapter 3: SDD, what Spec Kit and OpenSpec got right and where they weighed too much
[x] birth-of-focus-kit     Chapter 4: why Ninjobs left OpenSpec, and the process that became focus-kit
```

## M3. Part II, The focus-kit method

When this milestone closes, a reader can install the kit, document a new or an existing project, and deliver a milestone with `/propose` and `/apply`, following the guided project.

```
[x] guided-project-repo    the guided project's public repository, name chosen (OD-2), a tag per chapter
[x] commit-hooks           pre-commit and commit-msg hooks run the disclosure list on staged files and messages; make verify checks the history's messages
[x] install-and-hosts      Chapter 5: install, update, and how each host invokes the commands; Claude Code shown running, Copilot and Codex from their cited documentation, and why the hosts are alike enough that the method does not depend on one
[x] the-documents          Chapter 6: docs/00 to 06, ADRs, AGENTS.md, and why documents do the work
[x] brainstorm             Chapter 7: /brainstorm on the guided project, and choosing a stack by what the agent knows (the Ninjobs lesson of chapter 4)
[x] analyze                Chapter 8: /analyze on the brownfield project
[x] two-choices            Chapter 6 gains "The two choices": FOCUS (four pieces, whole / two principles / neither) and git (trunk / branch / worktree) in a paragraph each, so chapters 7 and 8 point back to them; Parts III and IV still teach them
[x] queue-and-milestones   Chapter 9: the queue, the marks, milestones and their paragraphs
[x] propose                Chapter 10: /propose, one page, reading it before /apply, and splitting what does not fit
[x] apply                  Chapter 11: /apply, verify, proof, documents, stage, never commit
[x] clinic-milestone-1     the guided project's milestone 1 built line by line with /propose and /apply, each page and staged change reviewed and committed by the author, recorded; no chapter
[ ] closing-a-milestone    Chapter 12: the whole-milestone review of the clinic's milestone 1 with /code-review, findings become queue lines; Ninjobs' milestone review as the counter-example
[ ] the-governor           Chapter 13: which concrete error would it have caught, and what the process does not have
```

## M4. Part III, FOCUS architecture

When this milestone closes, a reader can organize code by feature with exceptions as values, and knows when the four pieces pay their way and when they do not.

```
[ ] errors-and-slices      Chapter 14: exceptions as values and vertical slices, the two principles that stand alone
[ ] four-pieces            Chapter 15: View, Orchestrator, Use Case, Repository, one table and one flow, and when the four pieces pay their way
[ ] testing-and-agents     Chapter 16: testing each piece, and how the architecture helps an agent
```

## M5. Part IV, Git for agents and teams

When this milestone closes, a reader can choose between trunk, a branch per delivery and a worktree per delivery, run agents in parallel, use the commit as the human review, and run a team's work on GitHub with pull requests, issues and a Projects board.

```
[ ] git-essentials         Chapter 17: commits, branches, merges, trunk and git-flow
[ ] worktrees              Chapter 18: worktrees and parallel agents, and where parallelism really stops
[ ] commit-as-review       Chapter 19: the agent stages, the person commits, and why
[ ] github-for-teams       Chapter 20: pull requests as the team's review, issues, Projects boards, and why the wiki is not docs/ (the agent reads the repository, not the wiki)
```

## M6. Part V, Beyond code

When this milestone closes, a reader can adapt the process to a team's tools, including GitHub issues and a Projects board kept in step by the kit, ask the project questions as they would ask a colleague, from how it is going to who owes them an answer, and use the method on work that is not software.

```
[ ] customizing            Chapter 21: extra marks, question deliveries, proof files, a board mirror (Case A), and the queue mirrored to GitHub issues and a Projects board, built and tagged in the guided project
[ ] project-as-assistant   Chapter 22: the documents as the whole project's memory, for engineering and product alike: what is pending, how is it going, how long each delivery took (queue plus git history), who is away; team and client conversations kept in a free notes folder, so "who owes me answers?" and "what must I ask, and whom?" are answered too (Case A, Case B)
[ ] beyond-software        Chapter 23: analyses, proposals (Case B), codeless projects (Case A), client communication as a source of truth, data work (Ninjobs' database security rules as deliveries), and this book
[ ] cost-and-where         Chapter 24: what coding agents cost, where they pay and where they do not, and how a team decides, with measured numbers
[ ] adoption               Chapter 25: taking the method to a team and a company (Case B)
```

## M7. Appendices and launch

When this milestone closes, version 1 is tagged, the PDF and EPUB are on books.kodel.com.br, and focus-kit points to the book.

```
[ ] ninjobs-case           Appendix: the Ninjobs case end to end, with its numbers and their sources
[ ] glossary               Appendix: the glossary, generated from docs/03 in both editions
[ ] templates              Appendix: every document template, annotated
[ ] workshop-map           Appendix: the parts mapped to workshop sessions, with timings and exercises
[ ] exercise-answers       Appendix: answers to every exercise, linked to the guided project's tags
[ ] cover                  a cover image per edition for the PDF and the EPUB
[ ] launch                 v1 tag and Release; focus-kit's README repointed in its own repository (OD-4)
```
