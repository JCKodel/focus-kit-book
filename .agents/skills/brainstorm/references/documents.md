# The documents

Seven numbered documents, a folder of decisions, a folder of manuals, a
rules file and a work folder, written from a context folder. The numbers are fixed, because the four commands cite them; the
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
Where tests live and what is tested at each level. A pointer to docs/05 §6
for the commit message format; do not copy that format here.

**docs/05, the process.** The template below, with its slots filled.

**docs/06, the queue.** Milestones, each with a paragraph saying what is
true when it closes, and under it one line per delivery, in order, then
its review (docs/05 §8):

```
[ ] <slug>    <what it delivers, one line>
```

`[ ]` not yet defined · `[~]` being defined · `[>]` completely defined,
`work/<slug>.md` ready for /apply · `[*]` being built · `[x]` done, page in
`work/done/` · `[?]` waiting, with `· resume: propose` or `· resume: apply`
before `· blocked: <reason>` or `· blocked: after <slug>, <slug>` at the
end of the line (docs/05 §4). A line never
leaves; it changes mark, at the moment the work changes (docs/05 §4). The
order is the priority: a session asked for the next delivery takes the
first free line, and the person reorders by conversation in any session;
what is not in the current milestone is not planned yet. A line that
needs another done first ends with `· after <slug>`, written when the
line is added; it is an order, not a block. A line is free when every
`after` it names is `[x]`. Free lines that touch different files may run
at the same time, in different sessions (docs/05 §4). The
queue is edited by conversation in any session; no command owns it.

**docs/adr/.** One file per decision, `ADR-NNNN-<slug>.md`: context, the
decision, the consequences, the date. An ADR is amended, never rewritten.

**docs/manuals/.** One file per thing a person does by hand outside a
delivery, so it is found by its name and not inside a slot: publish, roll
back, set up a service. docs/05 §5 says what each one holds. Created with
the first one; there is no empty folder.

**AGENTS.md.** The template below. Read at the start of every session by
every host in the table of SETUP.md §1, on its own or through the pointer
the table names; Claude Code reads it through `CLAUDE.md`, which holds `@AGENTS.md`
and, below that line, only what applies to Claude Code alone: a tool name,
a command that exists only there. `AGENTS.md` itself names no host's tool,
so it reads the same in every one.

**work/.** One page per delivery in flight; `work/done/` holds the finished
ones. Created with a `.gitkeep` in `work/done/`, so the folder survives a
clone.

**context/.** What people said, as it arrived: the proposal, the client's
emails, the notes of a meeting, a brief. `context/` is what the agent reads
from; `docs/` is what it writes. Each item is a pair: the original, kept
byte for byte, and beside it `<original name>.md` (`proposal.pdf.md`)
holding what the original says, whole, in Markdown; a summary is not a
conversion. An item that arrives as text is the `.md` alone. Subfolders
are the project's. `/brainstorm` and `/analyze` read it whole; an item that
arrives later is read on the person's request, and what it changes goes
into the documents (a rule into docs/00, a term into docs/03, a line into
docs/06), so `/propose` reads the decision, not the message. Whether it is
committed is a slot of docs/05 §5; personal data and anything under a
confidentiality clause stay out of a committed folder, because git keeps a
removed file in its history.

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
not by layer, and a layer exists only when it pays its own way. FOCUS
is chapter 7 of the book One Page at a Time by J.C. Ködel
(https://jckodel.github.io/focus-kit-book/07-four-pieces/). Three answers:

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

**Git.** A strategy, not a silver bullet: pick the one that fits how the
project is worked. Three answers, and in every one a delivery's page and
build are one change that reverts in one step, because undoing a whole
delivery must be one step; the agent never commits and never merges:

* **trunk:** everything on the main branch. The
  page waits uncommitted in the working tree between `/propose` and
  `/apply`; page and build land in one commit, which the person makes
  after reviewing. For one person, alone or with several sessions open
  on free lines that touch different files: each session stages only its
  delivery, and the person commits one delivery at a time, from the paths
  that session staged. Not for two people: their deliveries share one
  branch and one commit carries the other's half-done work. What Ninjobs
  did;
* **a branch per delivery:** `/propose` creates a branch named after the
  slug and writes the page there; `/apply` builds on it. The branch may
  carry several commits, the page first and the build after; the person
  merges it through a pull request in one merge, so reverting the delivery
  is one revert of that merge. For sequential work reviewed by pull
  request;
* **a worktree per delivery:** `/propose` creates a git worktree on a
  branch named after the slug and writes the page there; `/apply` runs in
  it; the branch reaches the main branch in one merge, as above. For
  parallel work by several people, or by one person whose deliveries
  touch the same files: one branch does not touch
  another, so several agents build different deliveries at the same time.
  Before running two at once, pick free lines (docs/06's `after`) and
  decide which touch the same files, including docs/06 and other shared
  documents. Reconcile the queue by docs/05 §4 when their branches are
  integrated. Costs a directory per delivery.

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
Code changes only inside /apply: a change asked anywhere else, however
small, becomes a `[ ]` line in docs/06 and the answer stops there.

Before /propose changes the queue or the page, use §5's git strategy:
create the branch or worktree named after the slug, or reuse its existing
one on resumption. Add a missing queue line where it belongs and say so.
Start defining with `[~]`; start building only a completely defined `[>]`
page, with `[*]`. Follow §4 for blocked lines and §6 before changing code
or staging. Keep project slots and rules current before using them; report
a missing process rule rather than falling back to a retired instruction.

## 3. The page

    # <slug>

    **Objective.** One sentence: what the user can do afterwards.

    **Behaviour.** Verifiable scenarios in user language, each an action
    with concrete input and the result the user sees. Include the cases
    that must fail and the edges the documents imply. Each line becomes a
    test or a manual check.

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
dropped, what the proof found, the decisions taken. It ends with the commit
message /apply suggested, in a fenced block whose info string is `commit`.
There is one final block: a resumed /apply replaces the earlier suggestion.

A draft with unanswered scope questions is not ready for /apply, even
when its file exists. Before marking `[>]`, every section above is filled
or explicitly inapplicable and no scope decision remains open. Ask the
person to review the page: Behaviour is checkable, Contract exact, Out of
scope names what they assumed was included, and choices made on their
behalf are explicit. Corrections happen in the /propose conversation;
/apply starts in a fresh session afterwards.

## 4. The queue

docs/06: one line per delivery, in order, under milestones. The order is
the priority: the next delivery is the first free line, and the person
reorders by conversation. A line that needs another done first ends with
`· after <slug>`, written when the line is added; it is free when every
line it names is `[x]`. Asked what can run at the same time, answer from
the queue: the free lines, and among them the ones that touch different
files, judged from their pages and docs/01. The line never
leaves the queue; it changes mark, at the moment the work changes, so the
queue shows what is happening while it happens:

| Mark | Means | Set by |
|---|---|---|
| `[ ]` | not defined | the conversation that adds the line |
| `[~]` | being defined | /propose, when it starts |
| `[>]` | completely defined, page ready for /apply | /propose, when §3 is complete |
| `[*]` | being built | /apply, when it starts |
| `[x]` | done, page in `work/done/` | /apply, with verify green |
| `[?]` | waiting | any session, in the three cases below |

A line waits when the person says it is blocked, when it needs an answer
that was asked and not given, or when work already started finds it needs
another line done first, such as a fix found in the middle of an /apply.
The reason goes at the end
of the line, `· blocked: <reason>` or `· blocked: after <slug>, <slug>`.
A dependency known when the line is added is `· after <slug>` alone,
without `[?]`: an order, not an interruption.
Before that reason, record the phase to resume: `· resume: propose` for
`[ ]` or `[~]`, and `· resume: apply` for `[>]` or `[*]`. A draft saved
by /propose always uses `resume: propose` until §3 is complete.
Any mark before `[x]` can become `[?]`. The line leaves `[?]` when the
reason is resolved: the person says so, the session that records the
answer clears it, or /apply clears it when it marks `[x]` the last line of
an `after`. Remove both suffixes and return `resume: propose` to `[ ]`,
keeping any draft for /propose to finish; return `resume: apply` to `[>]`
only when its page still satisfies §3. Existence alone is insufficient.
If scope became undecided, return `[ ]` and say what /propose must settle.
For an old blocked line without `resume`, recover the phase from its page
and history; if completeness cannot be established, return `[ ]`.

Two sessions in one working tree, on free lines that touch different
files, are the normal case of parallel work on trunk. Another line
changing mark, another delivery's page or files appearing in the tree,
and another session's index entries are that session's work, not a
conflict: do not stop for them, do not touch them, change only this
delivery's line and stage only this delivery's paths and hunks, including
its own hunk of docs/06. A conflict is the same hunk edited by both, or a
file this page needs that the other delivery is changing; then stop and
report. In worktrees, each worktree's queue shows that branch's state, not a
global live view. Change only the current delivery's line, its new findings
and the dependent lines this session can resolve. When branches are
integrated, reconcile docs/06 by slug: retain every delivery and finding,
and each owning branch's latest state. Do not replace the whole file with
one side or downgrade a completed line using a stale copy. Check the page
at the expected path and keep a dependency blocked until its completed
changes are available in the branch that needs them. A conflicting state
or scope is reported for resolution, never guessed. Apply the same care
to shared domain terms and ADRs.

Each milestone is planned with its review as the last line (§8). Edited by
conversation in any session.

## 5. This project

* **Documentation language:** <language>. Identifiers in <language>.
* **Verify:** `<command>`, which runs <what>. Green before anything is
  declared done. <Or: created by the first delivery.>
* **Environments:** one line each: name, what runs there, what a delivery
  must leave up to date there, and the command that does it, or its
  manual when a person does it by hand.
* **Proof of a screen:** <tool, viewports, reference>, or "no screens".
* **Publish policy:** when an environment beyond the local one is updated,
  and whether the agent asks first.
* **Context:** `context/` is committed | listed in `.gitignore`, and why
  (who reads the repository).
* **Manuals:** `docs/manuals/`, one file per thing a person does by hand
  outside a delivery (publish, roll back, rotate a secret, set up a
  service), named in the documentation language after what it does. Each
  stands alone for a person who has read nothing else: what it does and
  when, what must be in place, the commands in order, how to tell it
  worked, how to undo it, what breaks if a step is skipped. A slot that
  names such a command points to its manual instead of holding the steps;
  a delivery that changes one updates its manual. <The manuals, one line
  each, or: none yet.>
* **Git:** trunk | a branch per delivery | a worktree per delivery. A
  delivery's page and build are one change: one commit on trunk, one merge
  otherwise. The agent stages; it never commits or merges.

## 6. Commit

This section owns the commit format; docs/04 points here. Before editing,
inspect git status, the staged and unstaged diffs, and untracked files.
Record which changes already belong to this delivery (its /propose page
and queue changes, or a previous partial /apply) and which are unrelated;
do not assume an existing edit belongs to it because it shares a path.
Another delivery's page, its files and its hunk of docs/06 belong to the
session building it (§4); they are unrelated here. Preserve unrelated
edits and the pre-existing index entries. If ownership of a change this
delivery must edit cannot be established, or changes overlap in the same
hunk, stop and report the affected paths before editing them or staging;
do not reset or stash them.

Stage only this delivery's files or hunks, including the page move and its
documentation changes. Use explicit paths for files wholly owned by it,
and selective staging for mixed files; never `git add -A` or `git add .`.
Inspect the staged diff afterwards and report any unrelated entries that
were already staged, so the person knows a plain commit would include
them. Do not unstage those entries yourself. A commit must contain only
this delivery for the one-change promise to hold: with two sessions on
trunk, the person commits one delivery at a time, naming its paths.

The agent suggests the message; the person commits after reviewing.
Imperative subject up to 72 characters, scope in parentheses
when it helps; body up to five one-line bullets, the highlights and not
the reasoning; last line points to the page's actual path, where the
reasoning lives: `work/done/<slug>.md` when done, `work/<slug>.md` when
blocked. A partial message says it is partial and names the blocker;
it must not imply verify passed or the delivery is done.

When blocked on trunk, keep the work uncommitted and do not add it to the
index; the `commit` block is a draft for the eventual whole delivery.
Resume with the same page and record the current verify result. If a
prerequisite must be implemented separately before resumption, move this
partial delivery to its own branch/worktree, preserving its edits and
index ownership, before starting the prerequisite; ask for help if safe
separation is not possible. Do not mix their commits on trunk.
On a delivery branch or worktree, partial changes may be staged and
suggested for the person to commit there. Keep the branch unmerged until
the delivery is complete, so one merge still contains the whole delivery.

## 7. What this process does not have

No formal spec, no spec delta, no change folder, no numbered tasks, no
gate before implementation, no review of a review, no specialized
subagent, no tool the deliveries did not ask for. When one of these is
proposed, the question is: which concrete error would it have caught? The
answer names an error that happened.

## 8. Closing a milestone

A milestone is planned with its review as its last line,
`<milestone>-review`, a delivery like the others: /propose writes its
page, /apply runs it. It takes the milestone's paragraph clause by clause
and writes, for each, which delivery answers it and how a person tests it.
It reviews no code and fixes nothing. The person tests each clause by
hand: a clause no delivery answers, or one that fails in the person's
hands, is a finding.

Each finding becomes a `[ ]` line in the same milestone, under the review
line, waiting for /propose. The milestone closes when those lines are
`[x]`. They get no second review: each one passes through its own page,
its proof and the person's commit, which is the review. A finding is
never a fix in the middle of the next milestone.
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
- what a person does by hand (publish, roll back): docs/manuals/, when
  it exists

## Non-negotiables
- <three to six rules that protect what the product is; from docs/00 and
  docs/01, one line each>
- One delivery = one page in work/<slug>.md: /propose to define, /apply
  to build. Code changes only inside /apply: a change asked outside it,
  however small, becomes a `[ ]` line in docs/06 and the answer stops
  there.
- No em dash in any text a user reads.
- The agent stages and suggests the commit message. It never commits.
- Stage only this delivery's changes as docs/05 §6 says; preserve unrelated
  edits and existing index entries.

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
- Asked where things stand, answer from docs/06 and work/: the lines in
  flight, their marks, and the next command, as this host invokes it.
```
