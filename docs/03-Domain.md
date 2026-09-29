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
| unit of work | unidade de trabalho | none | A delivery's page and build as one change that reverts in one step: one commit on trunk, or, on a branch or worktree, any number of commits that reach the main branch in one merge. |
| queue | fila | `docs/06` | Milestones and delivery lines, in order. |
| mark | marca | `[ ]`, `[>]`, `[x]` | The state of a queue line; a line never leaves the queue. |
| milestone | marco | `M<n>` | A group of deliveries with a paragraph saying what is true when it closes. |
| milestone review | revisão de marco | docs/05 §8 | The look at a closed milestone as a whole: its paragraph checked on the product, then a review of everything it built with what the host offers; it fixes nothing. |
| finding | achado | none | One problem a milestone review reports; the person confirms or rejects it, and a confirmed one becomes a queue line, never a fix in the middle of the next milestone. |
| fresh session | sessão nova | none | A session with an empty context; it separates deciding from doing. |
| verify | verificação | `make verify` | The command that must be green before anything is declared done. |
| proof | prova | `work/done/<slug>-<step>.png` | Evidence that the result works, failures included. |
| slot | slot | `docs/05 §5` | A project-specific fact the commands read. |
| open decision | decisão em aberto | `OD-<n>` | A decision listed in docs/00 that nobody closes alone, so an agent never settles it by assumption. |
| governor | regulador | none | The question every addition to the process must answer, and every step already in it again: which concrete error would it have caught? The answer names an error that happened; a step with none leaves. |
| context window | janela de contexto | none | Everything the model sees in one call. |
| token | token | none | The unit of text a model reads and counts; a word is one token or a few. |
| context rot | degradação de contexto | none | The loss of accuracy as the context grows. |
| compaction | compactação | none | The host summarizes a conversation near the limit of the context window and continues from the summary; detail is lost. |
| FOCUS | FOCUS | `view`, `orchestrator`, `use-case`, `repository`, `driver` | The optional architecture: Feature-oriented (vertical slices), Clean (four pieces, rules in pure use cases), Unidirectional (event, orchestrator, new state), Scalable (every piece isolated and testable, whatever the size); exceptions as values; nothing exists for ceremony (ADR-0016). |
| view | tela | `view` | The FOCUS piece that fires events and renders the state it receives, nothing else. |
| orchestrator | orquestrador | `orchestrator` | The FOCUS piece that turns one event into one new state: it validates, fetches, applies rules and formats through use cases, asks repositories to fetch and save, and returns the state; the only piece with injected dependencies, which are repositories (BLoC in Flutter, Mediator in .NET). |
| use case | caso de uso | `use-case` | A FOCUS piece holding a business rule, a validation or a format as a pure, synchronous function: data in, value out, no repository, no I/O; written only when there is a rule to hold. |
| repository | repositório | `repository` | The FOCUS piece that fetches and saves; the only code that does I/O and the only code with `try`/`catch`, and it returns every exception as a value. |
| driver | driver | `driver` | What a repository uses to reach I/O, such as a database engine or an ORM; rarely written for the project. |
| exception | exceção | `E` of `Result<T, E>` | An expected failure the caller handles, such as no connection or a missing record; it exists only at I/O and is returned as a value (after Dart's `Exception`). |
| error | erro | none | A program failure the programmer should have avoided, a bug; never caught, it reaches the developer's screen and analytics (after Dart's `Error`). |
| Result | Result | `Result<T, E>` | A value holding either the data or an exception, handled with an exhaustive switch; `throw` is never used for flow. |
| exceptions as values | exceções como valores | none | The principle that an exception is returned as a Result, never thrown; better known as "errors as values" (Go, Rust); the book says exception because an error, a bug, is never a value. |
| vertical slice | fatia vertical | `features/<name>/`, `features/<name>/<sub-feature>/` | Code organized by feature, with no folder per technology or layer (no `controllers/`): one folder holds all a feature needs, and a sub-feature is a subfolder (`authentication/change-password/`). |
| KISS | KISS | none | Keep it simple: the simplest code that does the job; with YAGNI and DRY, non-negotiable in FOCUS. |
| YAGNI | YAGNI | none | You aren't gonna need it: nothing is built before a delivery needs it, a FOCUS piece included. |
| DRY | DRY | none | Don't repeat yourself: each piece of knowledge lives in one place. |
| trunk | trunk | `main` | Working on the main branch, one delivery at a time; only for one person working alone. |
| pull request | pull request | none | A request to merge a branch that someone reviews first; how a branch per delivery lands. |
| git-flow | git-flow | `develop`, `feature/*`, `release/*`, `hotfix/*` | A branching model with long-lived branches for teams that ship versions. |
| worktree | worktree | `git worktree` | A second working directory on its own branch, so agents build in parallel. |
| case | caso | `ninjobs`, `case-a`, `case-b` | A real project the book draws on; anonymous when private. |
| guided project | projeto guiado | `JCKodel/focus-kit-clinic` | The scheduling app the reader builds through the book. |
| chapter tag | tag do capítulo | `book-v1/<chapter-slug>`, `book-v1-<chapter-slug>` in the fork | The annotated tag on the commit that a chapter quotes, in the guided project or in the brownfield project's fork; only a chapter that changes the project has one, and a published tag never moves. |
| brownfield project | projeto brownfield | `JCKodel/clahub@book-v1` | The frozen open-source fork used for `/analyze`. |
| edition | edição | `en`, `pt` | One language of the book; `en` is the source. |
| chapter | capítulo | `book/<edition>/NN-<slug>.md` | One file per edition; one delivery. |
| draft marker | marca de rascunho | `status: draft` | The front matter line of a chapter not yet done; the site shows a banner and a mark in the navigation, and the chapter's delivery removes it. |
| chapter shape | formato do capítulo | docs/04 §Chapter shape | The fixed order of a chapter: title, opening, sections, key points, exercises. |
| opening | abertura | none (first paragraph after the H1) | At most three sentences saying what the reader can do after the chapter; it has no heading. |
| key points | pontos-chave | `## Key points` / `## Pontos-chave` | At most five bullets closing every chapter's content. |
| exercise | exercício | `## Exercises` / `## Exercícios`, then `### Exercise N.M` / `### Exercício N.M` | A task on the guided project at the end of a chapter, from Part II on; answered in an appendix. |
| source note | nota de fonte | `[^<key>]` | A footnote that gives the reader something to open, or, for a private case, how its numbers were counted; the key is the same in both editions, and the PDF and the EPUB print it once per chapter. |
| disclosure list | lista de exposição | `FKB_DENYLIST` | The private terms that must never appear in the repository; kept outside it. |

## Entities and invariants

* A chapter exists in both editions with the same file name and the same heading structure.
* A chapter opens with what the reader can do after it, in at most three sentences.
* A chapter is as long as it needs to be to prove the value it opens with: no filler added, no useful content removed to fit a limit.
* Case A and Case B are never named, dated to a meeting, located, or described by business detail.
* Ninjobs is named, but only its process artifacts and published numbers appear, paraphrased; never its infrastructure, credentials, users or commercial plans. One exception, approved by the author in `the-governor`: the name of its database vendor, Supabase, where a story needs it; never its servers, projects, schema or configuration.
* Every number in the book cites where it was measured.
