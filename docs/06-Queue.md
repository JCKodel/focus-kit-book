# Queue

`[ ]` not yet defined · `[>]` defined, `work/<slug>.md` exists · `[x]` done, page in `work/done/`.
A line never leaves; it changes mark.

## M1. The book stands up

When this milestone closes, a chapter written in both languages builds into the website and into PDF and EPUB, `make verify` guards the build, the parity of the editions, the prose and the disclosure list, `main` publishes itself to GitHub Pages, a tag produces a Release, and the brownfield project is chosen.

```
[x] site-skeleton          MkDocs Material bilingual site, one placeholder chapter per edition, draft marker, make serve and make verify (strict build, parity, em dash)
[ ] license-and-readme     AGPL-3.0 for scripts and code, CC BY-SA 4.0 for the text; README in English and Portuguese
[ ] disclosure-scan        make scan against the out-of-repo disclosure list, locally and in Actions, part of make verify
[ ] prose-rules            the anti-AI prose rules written in docs/04 and checked by make verify
[ ] link-check             external links in the book checked, part of make verify (the strict build already fails on broken internal links)
[ ] chapter-template       the chapter shape fixed, proven by chapter 1, Why process, written in both editions
[ ] pdf-epub               make book produces PDF and EPUB in both editions from the same source
[ ] pages-and-release      Actions publish the site on push to main and a Release with PDF and EPUB on a v* tag
[ ] brownfield-research    three to five open-source candidates compared; the author picks one (OD-1); fork and tag
```

## M2. Part I, Foundations

When this milestone closes, a reader who has never followed a process knows why a coding agent needs written context, what Spec-Driven Development is, and why focus-kit exists.

```
[ ] how-agents-see         Chapter 2: statelessness, context window, context rot, fresh sessions, from primary sources
[ ] spec-driven            Chapter 3: SDD, what SpecKit and OpenSpec got right and where they weighed too much
[ ] birth-of-focus-kit     Chapter 4: the Ninjobs restart, and the kit that grew and became one file again
```

## M3. Part II, The focus-kit method

When this milestone closes, a reader can install the kit, document a new or an existing project, and deliver a milestone with `/propose` and `/apply`, following the guided project.

```
[ ] guided-project-repo    the guided project's public repository, name chosen (OD-2), a tag per chapter
[ ] install-and-hosts      Chapter 5: install, update, and how each host invokes the commands
[ ] the-documents          Chapter 6: docs/00 to 06, ADRs, AGENTS.md, and why documents do the work
[ ] brainstorm             Chapter 7: /brainstorm on the guided project
[ ] analyze                Chapter 8: /analyze on the brownfield project
[ ] queue-and-milestones   Chapter 9: the queue, the marks, milestones and their paragraphs
[ ] propose                Chapter 10: /propose, one page, and splitting what does not fit
[ ] apply                  Chapter 11: /apply, verify, proof, documents, stage, never commit
[ ] closing-a-milestone    Chapter 12: the whole-milestone review, findings become queue lines
[ ] the-governor           Chapter 13: which concrete error would it have caught, and what the process does not have
```

## M4. Part III, FOCUS architecture

When this milestone closes, a reader can organize code by feature with errors as values, and knows when the four pieces pay their way and when they do not.

```
[ ] errors-and-slices      Chapter 14: errors as values and vertical slices, the two principles that stand alone
[ ] four-pieces            Chapter 15: View, Orchestrator, Use Case, Repository, one table and one flow
[ ] testing-and-agents     Chapter 16: testing each piece, and how the architecture helps an agent
```

## M5. Part IV, Git for agents and teams

When this milestone closes, a reader can choose between trunk, a branch per delivery and a worktree per delivery, run agents in parallel, and use the commit as the human review.

```
[ ] git-essentials         Chapter 17: commits, branches, merges, trunk and git-flow
[ ] worktrees              Chapter 18: worktrees and parallel agents, and where parallelism really stops
[ ] commit-as-review       Chapter 19: the agent stages, the person commits, and why
```

## M6. Part V, Beyond code

When this milestone closes, a reader can adapt the process to a team's tools, ask the project questions as they would ask a colleague, and use the method on work that is not software.

```
[ ] customizing            Chapter 20: extra marks, question deliveries, proof files, a board mirror (Case A)
[ ] project-as-assistant   Chapter 21: what is pending, how is it going, who is away, answered from the documents
[ ] beyond-software        Chapter 22: analyses, proposals (Case B) and this book
[ ] adoption               Chapter 23: taking the method to a team and a company
```

## M7. Appendices and launch

When this milestone closes, version 1 is tagged, the PDF and EPUB are on books.kodel.com.br, and focus-kit points to the book.

```
[ ] ninjobs-case           Appendix: the Ninjobs case end to end, with its numbers and their sources
[ ] glossary               Appendix: the glossary, generated from docs/03 in both editions
[ ] templates              Appendix: every document template, annotated
[ ] workshop-map           Appendix: the parts mapped to workshop sessions, with timings and exercises
[ ] exercise-answers       Appendix: answers to every exercise, linked to the guided project's tags
[ ] launch                 v1 tag and Release; focus-kit's README repointed in its own repository (OD-4)
```
