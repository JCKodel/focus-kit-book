# Spec-Driven Development

Spec Kit and OpenSpec have a coding agent write the decision down before the code, and on a small feature they write much more than the feature needs.
After this chapter you can say what Spec-Driven Development is and how far a tool takes the spec, name what these two tools got right, and show, with the numbers of one recorded run, where they weigh more than the feature needs.

## What a spec is

Birgitta Böckeler compared three tools that call themselves spec-driven and wrote down what the term means.[^bockeler-2025]
A spec, in her definition, is "*a structured, behavior-oriented artifact [...] written in natural language that expresses software functionality and serves as guidance to AI coding agents.*"[^bockeler-2025]
Spec-Driven Development (SDD) "*means writing a “spec” before writing code with AI (“documentation first”). The spec becomes the source of truth for the human and the AI.*"[^bockeler-2025]

She found three levels, by how long the spec lives and who edits it:

* **spec-first**: a spec is written first and guides the task at hand;
* **spec-anchored**: the spec is kept after the task and used to evolve and maintain the feature;
* **spec-as-source**: the spec is the main source over time, and a person edits only the spec, never the code.

"*All SDD approaches and definitions I've found are spec-first, but not all strive to be spec-anchored or spec-as-source.*"[^bockeler-2025]
Of her three tools, Kiro is "*the simplest (or most lightweight)*" and "*mostly spec-first*".[^bockeler-2025]
Tessl is "*the only one of these three tools that explicitly aspires to a spec-anchored approach, and is even exploring the spec-as-source level of SDD.*"[^bockeler-2025]
She adds that "*these tools are very fast evolving, so they might have already changed since I used them*".[^bockeler-2025]

This chapter looks at two other tools, at the versions a recorded run pinned.
Spec Kit, from GitHub, is a toolkit of processes for coding agents, and its Spec-Driven Development process reads: "*Constitution once per project; specify → plan → tasks → implement → converge per feature.*"[^spec-kit]
OpenSpec, from Fission AI, "*adds a lightweight spec layer so you agree on what to build before any code is written*"; its `/opsx:propose` writes one folder per change with a proposal, specs, a design and tasks.[^openspec]
In the run, both were used spec-first: each wrote its spec before the task, and what happens to that spec afterwards the run did not exercise.

## One feature, three tools

The run started from a small TypeScript project for a clinic, in four files.[^spec-driven-run]
Its code has an `Appointment` type, with a client name, a start time and the status `booked`, a list of appointments kept in memory, and a `book(clientName, startsAt)` function that adds one to the list.
It has no way to cancel, no rule about who takes which time slot, and no tests yet.

Each tool got the same brief, word for word, in the steps where its path asks for it:

```markdown
## Feature

A client can cancel their own appointment up to 24 hours before it starts. A cancelled appointment frees its slot. A cancellation later than that is refused with a message that says why.

## Answers

Storage stays in memory. There is no screen: the feature is a function in the module. The client is identified by `clientName`, with no login. Times are the clinic's local time. Tests use `node --test`. No notification is sent.

## Principles

Keep it simple. TypeScript, strict. Every rule has a test.
```

When a tool asked something the brief did not answer, the run took the tool's own default, or "the simplest option" when it offered none.
Each tool followed its default path, each step in a fresh session, and stopped before writing code.
All three ran on 2026-09-25, with the model `claude-opus-5-5`.
The third tool is focus-kit, the method this book teaches from chapter 4; here it is one row of the table.

| Tool | Row | Files | Lines | Words |
|---|---|---:|---:|---:|
| Spec Kit | installed | 29 | 5,074 | 30,174 |
| Spec Kit | once per project | 1 | 71 | 429 |
| Spec Kit | per feature | 8 | 756 | 6,498 |
| OpenSpec | installed | 12 | 2,590 | 27,015 |
| OpenSpec | once per project | 3 | 32 | 140 |
| OpenSpec | per feature | 6 | 180 | 2,201 |
| focus-kit | installed | 36 | 2,049 | 14,700 |
| focus-kit | once per project | 17 | 277 | 2,577 |
| focus-kit | per feature | 1 | 82 | 602 |

"Installed" is what the tool puts in your project before you write anything: commands, skills, templates, scripts.
"Once per project" is what you write one time and every feature reuses.
"Per feature" is what one feature costs, and it repeats with every feature.
The counts come from `find`, `wc -l` and `wc -w` over the files each step left.[^spec-driven-run]

This is one run: one model, one day, one feature.
The agent is not deterministic, so a second run gives the same kind of output, not the same numbers.
Every file of the once-per-project and per-feature rows is kept in the run's folder, and its README says how to repeat the run.[^spec-driven-run]

## What they got right

**The decision is written before the code, in files the agent reads.**
Chapter 2 showed why a decision that lives only in the conversation is lost.
All three tools stopped before code with the feature decided in files inside the project, where a fresh session finds them.

**Some decisions are written once per project.**
Spec Kit's constitution holds the rules every feature follows.
In the run it turned the brief's principles (keep it simple, strict TypeScript, a test for every rule) into one file, and the feature's plan has a section that checks itself against it.
A rule that holds for the whole project is decided once and not argued again feature by feature.

**The tool asks before it writes.**
OpenSpec read the code before creating the change and stopped with a question: "*"A cancelled appointment frees its slot" doesn't change anything today, because slots are never held.*"[^spec-driven-run]
The brief assumed slots, and the code had none.
It offered two options, recommended one, and wrote the change only after the answer.

Spec Kit asked nothing.
It met the same gap and wrote its answer under "Assumptions" in the spec: a slot is identified by its start time, and the feature adds that check to booking.[^spec-driven-run]
Its README offers clarification as an extra step "*when you need extra quality gates*"; the run followed the default path and did not run it.[^spec-kit]
The decision was the same one OpenSpec asked about, and you find it only by reading the spec.

## Where they weighed too much

Per feature, Spec Kit wrote 8 files and 756 lines, OpenSpec 6 files and 180 lines, and focus-kit 1 page of 82 lines.[^spec-driven-run]
Every one of those files is something a person has to review before the code is written.

The brief holds one rule about time: up to 24 hours before.
Spec Kit restates it in 8 of its 8 files, OpenSpec in 4 of its 6, focus-kit in its 1.[^rule-count]
Here is the same part of the decision in each tool: a cancellation made in time is accepted, and one made exactly 24 hours before counts as in time.

Spec Kit, in `specs/001-cancel-appointment/spec.md`, the first of its user stories:

```markdown
### User Story 1 - Cancel an appointment in good time (Priority: P1)

A client who has booked an appointment finds they can't make it. At least 24 hours before the
appointment starts, they cancel it. The appointment is marked as cancelled and the client gets
confirmation that the cancellation went through.

**Why this priority**: This is the core ability the feature exists for. Without it nothing else
in this spec applies.

**Independent Test**: Book an appointment more than 24 hours in the future, cancel it as the same
client, and check that it now shows as cancelled.

**Acceptance Scenarios**:

1. **Given** a client has a booked appointment starting 3 days from now, **When** that client
   cancels it, **Then** the appointment's status becomes "cancelled" and the client is told the
   cancellation succeeded.
2. **Given** a client has a booked appointment starting exactly 24 hours from now, **When** that
   client cancels it, **Then** the cancellation is accepted (exactly 24 hours counts as "up to
   24 hours before").
```

A user story, why it has its priority, how to test it on its own, and two scenarios in Given, When, Then form; the second is the 24-hour case.

OpenSpec, in the change's `specs/appointment-cancellation/spec.md`, the first of its requirements:

```markdown
### Requirement: Client cancels their own appointment with 24 hours' notice
The system SHALL let a caller cancel an appointment by giving the appointment identifier, the client name, and the current time in clinic local time. The cancellation SHALL succeed when the appointment is booked, belongs to that client name, and starts 24 hours or more after the current time. A successful cancellation SHALL set the appointment's status to `cancelled` and return the appointment. The appointment record SHALL be kept. The system SHALL NOT send any notification.

#### Scenario: Cancelling well ahead of time
- **WHEN** client "Ana" cancels their booked appointment 48 hours before it starts
- **THEN** the cancellation succeeds and the appointment's status is `cancelled`

#### Scenario: Cancelling exactly 24 hours ahead
- **WHEN** client "Ana" cancels their booked appointment exactly 24 hours before it starts
- **THEN** the cancellation succeeds and the appointment's status is `cancelled`
```

A requirement in sentences with SHALL, then two named scenarios in WHEN and THEN lines; the second is the 24-hour case.

focus-kit, in `work/cancel.md`, the page's objective and behaviour:

```markdown
**Objective.** Staff can cancel an appointment for the client whose name it
carries, up to 24 hours before it starts. The cancelled appointment frees its
slot, and a refusal comes back with a message that says why.

**Behaviour.** In the scenarios, "now" is the time the caller passes in.
- Ada has appointment 1 on 12 March at 10:00. Staff cancel it at 11 March
  09:00 (25 hours before). The answer is appointment 1 with status cancelled.
- The same thing at exactly 11 March 10:00 (24 hours before) succeeds too.
- The same thing at 11 March 10:01 (23 h 59 min before) is refused with
  `too-late`. The appointment stays booked.
- Cancelling after the start time has passed is refused with `too-late`.
- Cancelling appointment 99 when it does not exist is refused with
  `not-found`.
- Cancelling appointment 1 with the name "Bob" is refused with
  `not-your-appointment`. The appointment stays booked. Names are compared
  exactly as given.
- Cancelling appointment 1 a second time is refused with `already-cancelled`.
- When more than one refusal applies, the first in this order wins:
  `not-found`, `not-your-appointment`, `already-cancelled`, `too-late`.
- After appointment 1 is cancelled, booking another client for 12 March at
  10:00 succeeds.
- A cancelled appointment stays in memory with its number. The next booking
  still gets the next number.
- No notification is sent. Nothing is written outside memory.
```

The objective in three sentences, then the behaviour as examples with a date and a time; the second is the 24-hour case.
The page says "staff" where the brief says "client" because the project documents focus-kit wrote before the page named clinic staff as the only user, booking and cancelling for the client.[^spec-driven-run]

The three decide the same thing.
The difference is how many other files say it again: a rule written in 8 places is read 8 times in review, and when it changes, it changes in 8 places.
Böckeler found the same with Spec Kit: its files "*were repetitive, both with each other, and with the code that already existed*", and "*very verbose and tedious to review.*"[^bockeler-2025]

The light row is not free.
focus-kit writes the most once per project, 17 files and 277 lines, and its `/propose` also edited two of them, adding 6 lines and removing 3 in `docs/03` and `docs/06`.[^spec-driven-run]
The trade is to decide once per project, in documents you keep up to date, and then write one page per feature.
The run says what each tool writes before the code; it does not say which one builds better software.

## Key points

* A spec is a written, behaviour-oriented description of what the software must do, in natural language, that guides a coding agent; Spec-Driven Development writes it before the code.
* By how long the spec lives, a tool is spec-first (written for the task), spec-anchored (kept to maintain the feature) or spec-as-source (the only thing a person edits).
* Spec Kit and OpenSpec got three things right: the decision written before code in files the agent reads, rules written once per project, and a question asked before writing.
* On one recorded feature, Spec Kit wrote 8 files and 756 lines and OpenSpec 6 and 180, restating one rule in most of them, and every file is something you review.
* A lighter page per feature is paid for with documents written once per project; the run shows what each tool writes, not which builds better software.

[^bockeler-2025]: Birgitta Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl", 2025. https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
[^spec-kit]: GitHub, "Spec Kit", v1.0.11. https://github.com/github/spec-kit/tree/v1.0.11
[^openspec]: Fission AI, "OpenSpec", 1.13.2. https://github.com/Fission-AI/OpenSpec/tree/v1.13.2
[^spec-driven-run]: This book's run of Spec Kit, OpenSpec and focus-kit on one brief, 2026-09-25: the counts, the setting and how to repeat it in the README; each tool's questions and answers in its `questions.md`, in the same folder. https://github.com/JCKodel/focus-kit-book/blob/53109f372125e8aeda200bb2e5bbd1ad7bcc5d61/work/done/spec-driven-run/README.md
[^rule-count]: Counted in the run's folder with `grep -rliE '24 ?h|24-hour|24 hours' <tool>/feature | wc -l`, against the per-feature file count: Spec Kit 8 of 8, OpenSpec 4 of 6, focus-kit 1 of 1.
