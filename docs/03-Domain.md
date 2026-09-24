# Domain

This table is also the book's glossary.
The Portuguese term is fixed: the Portuguese edition uses it and no synonym.
A new concept enters here first, in both languages.

| Term | Portuguese | Identifier | Meaning |
|---|---|---|---|
| Spec-Driven Development (SDD) | Desenvolvimento Guiado por Especificação | `sdd` | Deciding in writing before building, so the written decision guides the agent. |
| focus-kit | focus-kit | `focus-kit` | The method this book teaches, and the one-file kit that installs its four commands. |
| host | host | `claude-code`, `codex`, `copilot`, `cursor`, `gemini-cli`, `antigravity`, `windsurf` | The program that runs the coding agent. |
| command | comando | `/brainstorm`, `/analyze`, `/propose`, `/apply` | One of the four steps the kit installs. |
| project documents | documentos do projeto | `docs/00` to `docs/06` | The project's memory, read before acting. |
| rules file | arquivo de regras | `AGENTS.md` | What every agent reads when a session starts. |
| ADR | ADR (registro de decisão de arquitetura) | `docs/adr/ADR-NNNN-<slug>.md` | One dated decision; amended, never rewritten. |
| delivery | entrega | `<slug>` | The smallest unit of work with value; it fits on one page. |
| page | página | `work/<slug>.md` | The document of one delivery, from Objective to Done when. |
| queue | fila | `docs/06` | Milestones and delivery lines, in order. |
| mark | marca | `[ ]`, `[>]`, `[x]` | The state of a queue line; a line never leaves the queue. |
| milestone | marco | `M<n>` | A group of deliveries with a paragraph saying what is true when it closes. |
| fresh session | sessão nova | none | A session with an empty context; it separates deciding from doing. |
| verify | verificação | `make verify` | The command that must be green before anything is declared done. |
| proof | prova | `work/done/<slug>-<step>.png` | Evidence that the result works, failures included. |
| slot | slot | `docs/05 §5` | A project-specific fact the commands read. |
| governor | regulador | none | The question every addition must answer: which concrete error would it have caught? |
| context window | janela de contexto | none | Everything the model sees in one call. |
| context rot | degradação de contexto | none | The loss of accuracy as the context grows. |
| FOCUS | FOCUS | `view`, `orchestrator`, `use-case`, `repository` | The optional architecture: four pieces, flow in one direction. |
| Result | Result (erro como valor) | `Result<T, E>` | A failure returned as a value; `throw` is never used for flow. |
| vertical slice | fatia vertical | `features/<name>/` | Code organized by feature, not by layer. |
| trunk | trunk | `main` | Working on the main branch, one delivery at a time. |
| git-flow | git-flow | `develop`, `feature/*`, `release/*`, `hotfix/*` | A branching model with long-lived branches for teams that ship versions. |
| worktree | worktree | `git worktree` | A second working directory on its own branch, so agents build in parallel. |
| case | caso | `ninjobs`, `case-a`, `case-b` | A real project the book draws on; anonymous when private. |
| guided project | projeto guiado | `clinic` (placeholder, OD-2) | The scheduling app the reader builds through the book. |
| brownfield project | projeto brownfield | none until OD-1 | The frozen open-source fork used for `/analyze`. |
| edition | edição | `en`, `pt` | One language of the book; `en` is the source. |
| chapter | capítulo | `book/<edition>/NN-<slug>.md` | One file per edition; one delivery. |
| draft marker | marca de rascunho | `status: draft` | The front matter line of a chapter not yet done; the site shows a banner and a mark in the navigation, and the chapter's delivery removes it. |
| exercise | exercício | `### Exercise N.M` | A task on the guided project at the end of a chapter; answered in an appendix. |
| disclosure list | lista de exposição | `FKB_DENYLIST` | The private terms that must never appear in the repository; kept outside it. |

## Entities and invariants

* A chapter exists in both editions with the same file name and the same heading structure.
* A chapter opens with what the reader can do after it, in at most three sentences.
* A chapter is as long as it needs to be to prove the value it opens with: no filler added, no useful content removed to fit a limit.
* Case A and Case B are never named, dated to a meeting, located, or described by business detail.
* Ninjobs is named, but only its process artifacts and published numbers appear, paraphrased; never its infrastructure, credentials, users or commercial plans.
* Every number in the book cites where it was measured.
