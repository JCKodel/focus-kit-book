# The documents

Seven numbered documents, a folder of decisions, a rules file and a work
folder. The numbers are fixed, because the four commands cite them; the
name after the number is in the documentation language (`00-Product.md`,
`00-Produto.md`, `00-Produkt.md`). Prose in the documentation language;
identifiers in English unless docs/04 says otherwise.

## What each one holds

**docs/00, the product.** Purpose in one paragraph. Audience: who uses it,
and when there are two sides, which side each requirement serves.
Mechanics: how it works, in user language. Non-goals: what it is not, one
line each. Values: the five or six words decisions are measured against.
Product questions: the checklist every decision must answer yes to. Open
decisions: what nobody may close alone, so an agent never settles them by
assumption. Nothing may contradict this document without changing it in the
same delivery.

**docs/01, the architecture.** The design in one sentence. The stack, with
the reason for each choice that had an alternative. How the code is
organized (§Choices, FOCUS). How data is accessed. How errors travel. The
environments (local, staging, production, or whatever exists) and what runs
where. What was tried and removed on purpose, so it is not rebuilt.

**docs/02, the backend.** Only when there is a server holding rules the
client must not duplicate: schema, access rules, the functions the client
may call. Otherwise one line: "there is none".

**docs/03, the domain.** One table: term, identifier in code, meaning. Then
entities and invariants. Every page in `work/`, every identifier and every
test uses the terms of this table. A new concept enters here first.

**docs/04, the conventions.** Documentation language and identifier
language. Naming. Style and formatting, and the tool that enforces them.
Where tests live and what is tested at each level. Commit message format.

**docs/05, the process.** The template below, with its slots filled.

**docs/06, the queue.** Milestones, each with a paragraph saying what is
true when it closes, and under it one line per delivery, in order:

```
[ ] <slug>    <what it delivers, one line>
```

`[ ]` not yet defined · `[>]` defined, `work/<slug>.md` exists · `[x]` done,
page in `work/done/`. A line never leaves; it changes mark. The queue is
edited by conversation in any session; no command owns it.

**docs/adr/.** One file per decision, `ADR-NNNN-<slug>.md`: context, the
decision, the consequences, the date. An ADR is amended, never rewritten.

**AGENTS.md.** The template below. Read at the start of every session by
every host in the table of SETUP.md §1, on its own or through the pointer
the table names; Claude Code reads it through `CLAUDE.md`, which holds `@AGENTS.md`
and, below that line, only what applies to Claude Code alone: a tool name,
a command that exists only there. `AGENTS.md` itself names no host's tool,
so it reads the same in every one.

**work/.** One page per delivery in flight; `work/done/` holds the finished
ones. Created with a `.gitkeep` in `work/done/`, so the folder survives a
clone.

## Choices

Two things the kit offers and never imposes. Present each in the person's
language, in your own words, with a recommendation for this stack.

**FOCUS.** An architecture in four pieces with flow in one direction. The
View fires events and renders the state it receives, nothing else. The
Orchestrator turns an event into the next state: it fetches, calls the
rule, publishes one state. Use Cases hold every business rule as pure
functions that take data and return a Result, no IO, no framework. The
Repository fetches and saves, and is the only place an infrastructure
exception becomes a value. Code is organized by feature (vertical slices),
not by layer, and a layer exists only when it pays its own way. The book is
FOCUS by J.C. Ködel (https://books.kodel.com.br). Three answers:

* **FOCUS whole:** the four pieces, errors as values, vertical slices.
  docs/01 gets the responsibility table below and names the pieces a slice
  has in this stack;
* **the two principles only:** vertical slices and errors as values, with
  whatever structure the stack favors. Ninjobs, a thin PWA over a backend
  as a service, chose this: component, one function per feature, client
  library, `{ data, error }` everywhere, `throw` never as flow;
* **neither:** the project's own conventions, written in docs/01.

On a repository with code the default is what the code already does.

| Piece | Does | Forbids |
|---|---|---|
| View | fires events, renders state | business rules, data access |
| Orchestrator | converts event to state, fetches, calls use cases, publishes state | deciding rules, persisting |
| Use Case | the only place for business rules; pure; takes data, returns a Result | IO, framework, domain exception |
| Repository | fetch and save; the only place an infra exception becomes a Result | business rules |

**Git.** Three answers, and in every one the agent never commits and never
merges:

* **trunk:** everything on the main branch, one delivery at a time, the
  person reviews and commits after each. The simplest, and what Ninjobs
  did;
* **a branch per delivery:** `/apply` works on a branch named after the
  slug; the person merges. For teams where a delivery is reviewed by
  someone else before it lands;
* **a worktree per delivery:** each `/apply` runs in its own git worktree
  on its own branch, so several agents build different deliveries at the
  same time; the person merges. Costs a directory per delivery and merges
  that can conflict when two deliveries touch the same files.

## The process document (docs/05)

Write it whole, in the documentation language, with the slots of §5
filled. Keep the section numbers: the commands cite them.

```markdown
# Process

How an idea becomes code in <project>.

## 1. The rule

One delivery is one page, `work/<slug>.md`. If it does not fit one page,
it is two deliveries. The page is not a concision goal: it is the test that
the scope was understood. A scope that needs five pages has not been
decided yet.

## 2. The flow

docs/06 → /propose <slug> → work/<slug>.md → /apply <slug>, in a fresh
session → verify green, environments as §5 says → work/done/<slug>.md and
git add → a person reviews and commits.

/propose talks and writes the page, never code. /apply builds, proves,
updates the documents, stages and suggests the commit, never commits.

## 3. The page

    # <slug>

    **Objective.** One sentence: what the user can do afterwards.

    **Behaviour.** Verifiable scenarios in user language. Each line becomes
    a test or a manual check.

    **Contract.** Data, schema, API, message shapes, or "none". The only
    section that must be exact.

    **States.** Empty, loading, error, offline: one line each, or "the
    defaults". Only when there is a screen.

    **Visual reference.** Where the design is, and the viewports. Only when
    there is a screen.

    **Out of scope.** What does not enter, half a line of reason each.

    **Done when.** A mechanical checklist: tests X pass; verify green;
    screenshot matches Y.

After /apply the page also records what happened: what diverged, what was
dropped, what the proof found, the decisions taken.

## 4. The queue

docs/06: one line per delivery, in order, under milestones. The line never
leaves the queue; it changes mark: `[ ]` not defined, `[>]` defined and not
built, `[x]` done. Edited by conversation in any session.

## 5. This project

* **Documentation language:** <language>. Identifiers in <language>.
* **Verify:** `<command>`, which runs <what>. Green before anything is
  declared done. <Or: created by the first delivery.>
* **Environments:** one line each: name, what runs there, what a delivery
  must leave up to date there, and the command that does it.
* **Proof of a screen:** <tool, viewports, reference>, or "no screens".
* **Publish policy:** when an environment beyond the local one is updated,
  and whether the agent asks first.
* **Git:** trunk | a branch per delivery | a worktree per delivery. The
  agent stages; it never commits or merges.

## 6. Commit

The agent stages and suggests the message; the person commits after
reviewing. Imperative subject up to 72 characters, scope in parentheses
when it helps; body up to five one-line bullets, the highlights and not
the reasoning; last line points to `work/done/<slug>.md`, where the
reasoning lives.

## 7. What this process does not have

No formal spec, no spec delta, no change folder, no numbered tasks, no
gate before implementation, no specialized subagent, no tool the
deliveries did not ask for. When one of these is proposed, the question
is: which concrete error would it have caught? The answer names an error
that happened.

## 8. Closing a milestone

When a milestone closes, review the whole with what the host offers, and
each confirmed finding becomes a line in the queue, not a fix in the middle
of the next milestone.
```

## AGENTS.md

Sixty lines at most. Everything in it points at a document; nothing in it
is the only place a rule is written.

```markdown
# <Project>

<One sentence: what it is.> Prose in <language>; identifiers in <language>.

## Read before acting
- the product: docs/00 · the vocabulary: docs/03
- how it is built: docs/01 · the server: docs/02
- style and tests: docs/04 · process: docs/05 · queue: docs/06

## Non-negotiables
- <three to six rules that protect what the product is; from docs/00 and
  docs/01, one line each>
- One delivery = one page in work/<slug>.md: /propose to define, /apply
  to build.
- No em dash in any text a user reads.
- The agent stages and suggests the commit message. It never commits.

## Do not rebuild
- <what was tried and removed on purpose, with the ADR that says why>

## How to work
- <how the code is organized, in one line>
- <how errors travel, in one line>
- `<verify>` before declaring anything done.
- Abstraction on the second concrete occurrence, and the delivery says
  which was the first.
- Ambiguity → ask. Documents are living: a delivery that changes behaviour
  updates the document that owns it, in the same delivery.
```
