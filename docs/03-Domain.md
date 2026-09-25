# Domain

This table is also the book's glossary.
The Portuguese term is fixed: the Portuguese edition uses it and no synonym.
A new concept enters here first, in both languages.

| Term | Portuguese | Identifier | Meaning |
|---|---|---|---|
| Spec-Driven Development (SDD) | Desenvolvimento Guiado por Especificação | `sdd` | Deciding in writing before building, so the written decision guides the agent. |
| spec | especificação | none | A written, behaviour-oriented description of what the software must do, in natural language, that guides a coding agent (after Böckeler, 2025). |
| spec-first | spec-first | none | A spec is written before the task and guides it; kept in English in both editions, with "especificação primeiro" in parentheses on its first use in Portuguese. |
| spec-anchored | spec-anchored | none | The spec is kept after the task and used to evolve and maintain the feature; Portuguese first use: "ancorado na especificação". |
| spec-as-source | spec-as-source | none | The spec is the main source over time; a person edits only the spec, never the code; Portuguese first use: "especificação como fonte". |
| focus-kit | focus-kit | `focus-kit` | The method this book teaches, and the one-file kit that installs its four commands. |
| setup file | arquivo de setup | `SETUP.md` | The one file of focus-kit that an agent reads to install or update the kit's commands in a repository, for every host at once. |
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
| token | token | none | The unit of text a model reads and counts; a word is one token or a few. |
| context rot | degradação de contexto | none | The loss of accuracy as the context grows. |
| compaction | compactação | none | The host summarizes a conversation near the limit of the context window and continues from the summary; detail is lost. |
| FOCUS | FOCUS | `view`, `orchestrator`, `use-case`, `repository` | The optional architecture: four pieces, flow in one direction. |
| Result | Result (erro como valor) | `Result<T, E>` | A failure returned as a value; `throw` is never used for flow. |
| vertical slice | fatia vertical | `features/<name>/` | Code organized by feature, not by layer. |
| trunk | trunk | `main` | Working on the main branch, one delivery at a time. |
| git-flow | git-flow | `develop`, `feature/*`, `release/*`, `hotfix/*` | A branching model with long-lived branches for teams that ship versions. |
| worktree | worktree | `git worktree` | A second working directory on its own branch, so agents build in parallel. |
| case | caso | `ninjobs`, `case-a`, `case-b` | A real project the book draws on; anonymous when private. |
| guided project | projeto guiado | `JCKodel/focus-kit-clinic` | The scheduling app the reader builds through the book. |
| chapter tag | tag do capítulo | `book-v1/<chapter-slug>` | The annotated tag on the guided project's commit that a chapter quotes; only a chapter that changes the project has one, and a published tag never moves. |
| brownfield project | projeto brownfield | `JCKodel/clahub@book-v1` | The frozen open-source fork used for `/analyze`. |
| edition | edição | `en`, `pt` | One language of the book; `en` is the source. |
| chapter | capítulo | `book/<edition>/NN-<slug>.md` | One file per edition; one delivery. |
| draft marker | marca de rascunho | `status: draft` | The front matter line of a chapter not yet done; the site shows a banner and a mark in the navigation, and the chapter's delivery removes it. |
| chapter shape | formato do capítulo | docs/04 §Chapter shape | The fixed order of a chapter: title, opening, sections, key points, exercises. |
| opening | abertura | none (first paragraph after the H1) | At most three sentences saying what the reader can do after the chapter; it has no heading. |
| key points | pontos-chave | `## Key points` / `## Pontos-chave` | At most five bullets closing every chapter's content. |
| exercise | exercício | `## Exercises` / `## Exercícios`, then `### Exercise N.M` / `### Exercício N.M` | A task on the guided project at the end of a chapter, from Part II on; answered in an appendix. |
| source note | nota de fonte | `[^<key>]` | A footnote that gives the source of a number or a quoted claim; the key is the same in both editions. |
| disclosure list | lista de exposição | `FKB_DENYLIST` | The private terms that must never appear in the repository; kept outside it. |

## Entities and invariants

* A chapter exists in both editions with the same file name and the same heading structure.
* A chapter opens with what the reader can do after it, in at most three sentences.
* A chapter is as long as it needs to be to prove the value it opens with: no filler added, no useful content removed to fit a limit.
* Case A and Case B are never named, dated to a meeting, located, or described by business detail.
* Ninjobs is named, but only its process artifacts and published numbers appear, paraphrased; never its infrastructure, credentials, users or commercial plans.
* Every number in the book cites where it was measured.
