# Product

## Purpose

*One Page at a Time: Delivering Software and Projects with Coding Agents*
(Portuguese edition: *Uma Página de Cada Vez: entregando software e projetos com agentes de IA*)
is a free book, by J.C. Ködel, that takes a reader who has never followed any process to running whole projects with coding agents.
It teaches one method end to end: Spec-Driven Development as the idea, focus-kit as the method and its tool, FOCUS as the optional architecture, and just enough git to work with parallel agents and teams.
It argues for the method with real cases and measured results, and it doubles as the curriculum of adoption workshops.

## Audience

* **Developers new to any process**, indie or in a company: they read Parts I, II and V and can deliver their first milestone with an agent.
* **Experienced developers and tech leads**: they skim Part I, use Part II as a manual, and take Parts III, IV and V for git, the team's tools, adoption and asking an agent for more.
* **People who run or analyse projects without writing code** (managers, analysts, consultants, pre-sales): the prologue, chapters 1 to 3, Part II, Part IV and Part V, where the project answers them and the method is applied to proposals, analyses and a book.
* **Workshop instructors**: the parts map to sessions (appendix).

## Mechanics

* One Markdown source per chapter per edition.
  English is the source; Portuguese is the translation, kept in step in the same delivery.
* Published as a website on GitHub Pages, updated on every push to `main`, and as PDF and EPUB in both languages on every tagged GitHub Release.
* Every chapter opens with what the reader can do after it, then delivers exactly that, then says what the team gains, with its evidence, then ends with key points.
* No guided project and no exercises (ADR-0017).
  Code examples are TypeScript written for the chapter, on one running example, a lending library, and the book says once that they are written for it.
  This repository, a book written with focus-kit, is the non-software example.
* Cases: Ninjobs by name (the author's product, where the method was born), through its process artifacts and counted numbers; the author's company projects only as **Case A** (a client project on a low-code platform that ran on the process) and **Case B** (a consultancy's proposal for a client's adoption program, which did not run on the process and serves as the shape of a pitch and as a contrast), with no names and no business details.

### Contents

| Part | Chapters |
|---|---|
| Prologue | Product, people and process |
| I. The base | 1 Why process, when AI writes fast · 2 How an agent sees your project · 3 Spec-Driven Development · 4 Simplicity is a decision: KISS, YAGNI, DRY · 5 Rules as pure functions, exceptions as values · 6 Features, not layers · 7 FOCUS: the four pieces · 8 A test for each piece |
| II. The method | 9 How focus-kit was born · 10 The documents: one place per fact · 11 Install, and the hosts · 12 Starting: `/brainstorm` and `/analyze` · 13 The queue and milestones · 14 `/propose`: one page · 15 `/apply`: build, verify, prove, never commit · 16 Closing a milestone · 17 The governor · 18 The project as the team's assistant |
| III. Git and the team's tools | 19 Git essentials · 20 Worktrees and parallel agents · 21 The team's tools: pull requests, issues and boards |
| IV. Beyond code | 22 Projects that are not software · 23 What agents cost, and where they pay · 24 Adoption in teams and companies |
| V. The person decides | 25 Asking for more |
| Appendices | The Ninjobs case · Glossary · Templates · Workshop map |

The contents are a starting point; chapters are split, merged or moved by conversation, and docs/06 follows.
The earlier contents (Parts I to V, with a guided project) were replaced whole by `rewrite` (ADR-0017).

## Non-goals

* Not a reference for any host's features: hosts change monthly; the book points to SETUP.md and vendor docs.
* Not a prompt-writing book: the method works because of documents, not phrasing.
* Not a git manual: only what parallel agents and teams need.
* Not commercial material: no length for its own sake, no sales pitch, no employer.
* Not a sequel: it cites none of the author's earlier books and presents none as a prerequisite or a complement.
  Fundamentals are rewritten from primary sources.
* Not a tour of several languages: code examples are TypeScript only.
* Not the log of its own making: no chapter narrates a run; a number or an artifact appears where it proves a point (ADR-0017).

## Values

* **Value first.** Every chapter opens with what the reader gains, and says what the team gains before it closes.
* **No filler.** Every sentence carries information; the length is whatever proves the value, never a target.
* **Any host.** The method works with any coding agent; the book shows why the hosts are alike enough.
* **Beyond code.** The documents are the source of truth for any project, software or not, including what was agreed with a client.
* **Proven.** Every number and every quoted artifact is real and has its source; code examples are written for the chapter and said so.
* **Safe to publish.** Nothing private reaches the repository.
* **Beginner to advanced.** No step assumed; no step repeated.
* **Both languages, same book.** The two editions never drift.

## Product questions

Every decision must answer yes to all of these:

1. Does the chapter open with what the reader can do after reading it?
2. Does every sentence carry value, and is nothing the reader needs left out?
3. Is every number and every quoted artifact real and traceable to a source? (The book says once, at its first code block, that code examples are written for it.)
4. Would the text be safe if the private case it draws on were read by its owner's competitor?
5. Can a reader who has read only the previous chapters follow it?
6. Are both editions updated in this delivery?
7. Does the chapter say what the team or the project gains, with a number or a sourced claim, or say in one sentence that it has none?

## Open decisions

Nobody closes these alone; an agent never settles them by assumption.

* **OD-1, the brownfield project.** Which open-source project is forked and frozen for `/analyze`.
  Closed on 2026-09-25: CLAHub, `JCKodel/clahub@book-v1` (ADR-0009, amendment).
  Superseded on 2026-09-30: the book has no brownfield project (ADR-0017).
* **OD-2, the guided project's name and repository.** A public repository under the author's account.
  Closed on 2026-09-25: `JCKodel/focus-kit-clinic`, a clinic (ADR-0008, amendment).
  Superseded on 2026-09-30: the book has no guided project (ADR-0017).
* **OD-3, what each private case may show.** For every passage drawn from Case A or Case B, the author approves the anonymized text before the chapter is done.
* **OD-4, repointing the kit.** focus-kit's README and `documents.md` point FOCUS at books.kodel.com.br and the earlier FOCUS book.
  The change is made in the focus-kit repository when this book launches, not here.
