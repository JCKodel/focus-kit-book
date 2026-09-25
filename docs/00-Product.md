# Product

## Purpose

*One Page at a Time: Delivering Software and Projects with Coding Agents*
(Portuguese edition: *Uma Página de Cada Vez: entregando software e projetos com agentes de IA*)
is a free book, by J.C. Ködel, that takes a reader who has never followed any process to running whole projects with coding agents.
It teaches one method end to end: Spec-Driven Development as the idea, focus-kit as the method and its tool, FOCUS as the optional architecture, and just enough git to work with parallel agents and teams.
It argues for the method with real cases and measured results, and it doubles as the curriculum of adoption workshops.

## Audience

* **Developers new to any process**, indie or in a company: they read Parts I and II and can deliver their first milestone with an agent.
* **Experienced developers and tech leads**: they skim Part I, use Part II as a manual, and take Parts III to V for architecture, git and team practice.
* **People who run or analyse projects without writing code** (managers, analysts, consultants, pre-sales): Parts I, II and V, where the method is applied to proposals, analyses and a book.
* **Workshop instructors**: the parts map to sessions (appendix), and every chapter from Part II on ends with exercises on the guided project.

## Mechanics

* One Markdown source per chapter per edition.
  English is the source; Portuguese is the translation, kept in step in the same delivery.
* Published as a website on GitHub Pages, updated on every push to `main`, and as PDF and EPUB in both languages on every tagged GitHub Release; the author uploads those to books.kodel.com.br.
* Every chapter opens with what the reader can do after it, then delivers exactly that, then ends with key points and, from Part II on, exercises.
* A guided project runs through the book: a neighbourhood clinic or salon scheduling app, built greenfield with `/brainstorm`, in TypeScript, in its own public repository with a tag per chapter.
  A real open-source project, CLAHub, frozen in the fork `JCKodel/clahub` at tag `book-v1`, is the brownfield example for `/analyze`.
  This repository, a book written with focus-kit, is the non-software example.
* Cases: Ninjobs by name (the author's product, where the method was born); the author's company projects only as **Case A** (a Power Platform project for a client) and **Case B** (a proposal for a company adoption program), with no names and no business details.

### Contents

| Part | Chapters |
|---|---|
| I. Foundations | 1 Why process, when AI writes fast · 2 How an agent sees your project · 3 Spec-Driven Development · 4 How focus-kit was born |
| II. The focus-kit method | 5 Install, and the hosts · 6 The documents · 7 `/brainstorm` · 8 `/analyze` · 9 The queue and milestones · 10 `/propose`, one page · 11 `/apply`: build, verify, prove, never commit · 12 Closing a milestone · 13 The governor, and what the process does not have |
| III. FOCUS architecture (optional) | 14 Errors as values and vertical slices · 15 The four pieces · 16 Testing, and FOCUS with agents |
| IV. Git for agents and teams | 17 Essentials: trunk, branches, git-flow · 18 Worktrees and parallel agents · 19 The human commit as the review |
| V. Beyond code | 20 Customizing the process · 21 The project as an assistant · 22 Projects that are not software · 23 Adoption in teams and companies |
| Appendices | The Ninjobs case · Glossary · Templates · Workshop map · Exercise answers |

The contents are a starting point; chapters are split, merged or moved by conversation, and docs/06 follows.

## Non-goals

* Not a reference for any host's features: hosts change monthly; the book points to SETUP.md and vendor docs.
* Not a prompt-writing book: the method works because of documents, not phrasing.
* Not a git manual: only what parallel agents and teams need.
* Not commercial material: no length for its own sake, no sales pitch, no employer.
* Not a sequel: it cites none of the author's earlier books and presents none as a prerequisite or a complement.
  Fundamentals are rewritten from primary sources.
* Not a tour of several languages: code examples are TypeScript only.

## Values

* **Value first.** Every chapter opens with what the reader gains.
* **No filler.** Every sentence carries information; the length is whatever proves the value, never a target.
* **Proven.** Every artifact shown is real and every number has its source.
* **Safe to publish.** Nothing private reaches the repository.
* **Beginner to advanced.** No step assumed; no step repeated.
* **Both languages, same book.** The two editions never drift.

## Product questions

Every decision must answer yes to all of these:

1. Does the chapter open with what the reader can do after reading it?
2. Does every sentence carry value, and is nothing the reader needs left out?
3. Is every artifact real and every number traceable to a source?
4. Would the text be safe if the private case it draws on were read by its owner's competitor?
5. Can a reader who has read only the previous chapters follow it?
6. Are both editions updated in this delivery?

## Open decisions

Nobody closes these alone; an agent never settles them by assumption.

* **OD-1, the brownfield project.** Which open-source project is forked and frozen for `/analyze`.
  Closed on 2026-09-25: CLAHub, `JCKodel/clahub@book-v1` (ADR-0009, amendment).
* **OD-2, the guided project's name and repository.** A public repository under the author's account; the name is a placeholder (`clinic`) until the author chooses.
* **OD-3, what each private case may show.** For every passage drawn from Case A or Case B, the author approves the anonymized text before the chapter is done.
* **OD-4, repointing the kit.** focus-kit's README and `documents.md` point FOCUS at books.kodel.com.br and the earlier FOCUS book.
  The change is made in the focus-kit repository when this book launches, not here.
