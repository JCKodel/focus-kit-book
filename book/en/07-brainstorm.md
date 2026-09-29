# `/brainstorm`, a new project

After this chapter you can run `/brainstorm` on a new project, answer its questions or say "your call", and review the documents it writes before you commit them.
You can also choose a stack by what the project needs and by how well the agent knows it.

## What it asks

`/brainstorm` is the command for a repository with no code yet.
It talks one subject at a time, in this order, and moves on when it could write that document itself, as its file, `brainstorm/SKILL.md`, says:

1. The product (docs/00): what it is, for whom, what it is not, what a good decision looks like.
2. The vocabulary (docs/03): the words the product cannot be described without, each with its name in code.
3. How it is built (docs/01): the stack and the shape of the code, with the kit's [two choices](06-the-documents.md#the-two-choices), FOCUS and the git strategy.
4. The conventions (docs/04): languages, style, where tests live, the commit format.
5. The process slots (docs/05): the verify command, the environments, how a screen is proven, the publish policy.
6. The first milestone (docs/06): its first deliveries, one line each, in order.

It asks only what it cannot decide with a sensible default, and it states the default with the question.
So "your call" is always a valid answer: the agent keeps its default, and a person who cannot answer a question still gets a good document.
What you do not know yet, such as a verify command before any code exists, it writes as "created by the first delivery".

When the six subjects are covered, it writes docs/00 to 06, one ADR per decision a later session might undo, `AGENTS.md`, `CLAUDE.md` holding the line `@AGENTS.md`, and an empty `work/done/`.
It writes no code, no configuration and no dependency file: the first delivery does that, with a page of its own.

## Choosing the stack

When the conversation reaches how it is built, three questions choose the stack, in this order.

**What does the project need?**
Start from its value, not from a language: who opens it, on what device, which rules must never break, and what it may cost to run.
A stack that cannot deliver that is out, however well the agent knows it.

**How much public code did the agent learn from?**
A model writes best what it saw most while it was trained, and the nearest public measure of that is how many people write a language in the open.
By GitHub's count, TypeScript became the most used language on GitHub in August 2025, with 2,636,006 monthly contributors, ahead of Python and JavaScript.[^octoverse]
It counts people, not lines of code, so read it as a ranking, not as a size.
On Ninjobs the same agent kept missing the design in Flutter and wrote it right in React ([chapter 4](04-birth-of-focus-kit.md)).

**Can the agent check its own work there?**
A compiler that rejects a wrong type and tests that run in seconds tell the agent it made a mistake before you have to.
A stack where a mistake only shows at run time, on a screen, leaves that check to you.

The clinic answers them this way:

* TypeScript, strict: the most used language by that count, and its types catch the agent's mistakes before anything runs.
* A React PWA (a web app a phone opens in the browser, with no install): clients book from their phones, and React is where the agent got Ninjobs' design right.
* A small Node server: the client and the owner share the same appointments, so the rules that keep them right run where a phone cannot skip them, in the same language as the screens.
* SQLite in a file: one clinic's data fits in one file, with no database server to run, and a backup is a copy.
* No paid service: it runs on a machine at the clinic or on any free host.

The brief below gives this stack, so the run shows the criteria behind the answer, not a live choice.

## The run on the clinic

The run started from the clinic at the chapter tag `book-v1/install-and-hosts`: the README, the licenses and the kit that chapter 5 installed, with no document and no code.
It was answered from a brief, the same shape as chapter 3's: one section per subject, plus the rule for a question the brief does not answer.[^brainstorm-run]

```markdown
# Brief

## Product
A scheduling app for one neighbourhood clinic. Clients book and cancel their own appointments with the clinic's professionals from their phones; the owner registers the professionals and their weekly hours.
Two sides: the client, who has no account and gives a name and a phone number; the owner, who signs in (your call how).
Rules: a professional cannot have two appointments at the same time. A client can cancel their own appointment up to 24 hours before it starts; a cancelled appointment frees its slot; a later cancellation is refused with a message that says why. Times are the clinic's local time.
Not: payments, notifications (SMS, email, push), medical records or any health data, more than one clinic.

## Stack
TypeScript, strict. A React PWA that the client and the owner open in the browser, over a small Node server that keeps the data in a SQLite file. No paid service: it runs on a machine at the clinic or on any free host.
Why: the most public code the agent learned from is in this language and library, and types and tests let it check its own work.

## Choices
FOCUS: FOCUS whole. Git: trunk.

## Conventions and process
English for documents and identifiers. Verify: created by the first delivery. Everything else: your call.

## First milestone
When it closes, the owner can register professionals and their weekly hours, a client can book a free slot, and a client can cancel up to 24 hours before. A professional's absences and the owner's view of the day come in the second milestone.

## Principles
Keep it simple. Every rule has a test. No em dash in any document.

## Rule for a question the brief does not answer
Answer "your call".
```

Open your host at the root of your repository, in a fresh session, and type `/brainstorm`; I ran it headless in Claude Code and answered each round with the brief's sections for the subjects asked, word for word, or "your call".[^brainstorm-run]
A headless run is Claude Code run from the terminal with `claude -p`, one prompt per call: it prints the answer and exits, with no one there to approve anything.[^claude-code-headless]
Each answer to a round was a new call with `--continue`, which sends it to the most recent conversation in that directory.[^claude-code-headless]
The book's runs are headless so every turn is recorded; in an interactive session you just type your answer in the same session.
It asked in rounds of one or two subjects.
In the round about how the clinic is built, it wrote:[^brainstorm-run]

```markdown
## 3. How it is built (docs/01)

What the product needs from the stack:
- a phone-first web page for clients, with no install and no account
- a sign-in for one owner
- a **server that holds the rules**, because a phone can't be trusted to enforce the 24-hour deadline or stop double bookings
- rules that are easy to test, since every rule has a test

**1. Stack. My recommendation: one TypeScript web app (SvelteKit) with a SQLite database, on one small server.**
- It's one language and one project, and the rules run on the server as plain functions that Vitest tests in milliseconds.
- A double booking is impossible at the database level: slots are aligned, so a unique index on (professional, start) over booked appointments settles any race.
- The owner's sign-in is a hashed password plus a session cookie, about a page of code.
- The data is one file, and a backup is a copy of that file.

The alternative is a thin page over a hosted backend service (Postgres plus built-in sign-in). You get hosting and auth for free, but the rules would live in SQL functions and be tested in a second language. That's a worse fit for "every rule has a test" and "keep it simple". Does the recommendation hold?

**2. How the code is organized.** The kit offers FOCUS, an architecture in four pieces where data flows one way:
- the **screen** only shows state and reports what the user did
- an **orchestrator** turns what the user did into the next state
- **use cases** hold every business rule as pure functions that take data and return a result or a refusal
- a **repository** is the only code that talks to the database

Code is grouped by feature (book, cancel, weekly hours…), not by layer, and errors are returned as values instead of thrown.

You can take it whole, take only the two principles (feature folders + errors as values), or take neither. **My recommendation: FOCUS whole.** It maps onto SvelteKit with no extra machinery: the page is the screen, the page's server file is the orchestrator, `rules.ts` holds the use cases and `repository.ts` holds the queries. It also puts the 24-hour rule and the slot rule in pure functions, which is where "every rule has a test" is cheapest.

**3. Git.** In every option the agent never commits or merges; it stages and suggests the message. You can work on the main branch one delivery at a time and review and commit after each. Or each delivery gets its own branch that you merge. Or each delivery gets its own branch in a separate folder, so several agents can build at once. **My recommendation: the main branch**, since you're one person working through one delivery at a time.
```

The answer was the brief's two sections for that subject:[^brainstorm-run]

```markdown
## Stack
TypeScript, strict. A React PWA that the client and the owner open in the browser, over a small Node server that keeps the data in a SQLite file. No paid service: it runs on a machine at the clinic or on any free host.
Why: the most public code the agent learned from is in this language and library, and types and tests let it check its own work.

## Choices
FOCUS: FOCUS whole. Git: trunk.
```

The agent started from what the product needs, the first question of the stack, stated a default for each choice with its reason and its alternative, and asked whether it held; the brief kept SvelteKit out and React in, and the agent then chose the smaller pieces inside that stack itself, which its ADR records as its own call.

After the round on the conventions and the process slots it wrote the documents, and `git status --short` showed:[^brainstorm-run]

```
?? AGENTS.md
?? CLAUDE.md
?? docs/
?? work/
```

These lines hold docs/00 to 06, an ADR each in `docs/adr/` for the stack, FOCUS whole, trunk, clients without an account, and one fixed appointment length, `AGENTS.md`, `CLAUDE.md` and `work/done/.gitkeep`.[^brainstorm-run]
The three below are quoted at the chapter tag `book-v1/brainstorm`, as committed.

docs/00 opens with the product's purpose in one paragraph; exercise 6.2 asked you to write the clinic's by hand.
This is [`docs/00-Product.md`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/brainstorm/docs/00-Product.md) §Purpose:

```markdown
## Purpose

A scheduling app for one neighbourhood clinic. Clients book and cancel their
own appointments with the clinic's professionals from their phones, without
creating an account. The owner registers the professionals and their weekly
hours, and sees who is coming. The app replaces the phone call and the paper
diary for the simple case: pick a professional, pick a free time, done.
```

It is the brief's product with the client's lack of an account folded in, and its last sentence is the conversation's: what the app replaces, which tells a later session how small "simple" is here.

Chapter 5 said this chapter writes `AGENTS.md`, the rules file every session reads first.
Its non-negotiables are the kit's template with the project's own rules above the three fixed lines.
This is [`AGENTS.md`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/brainstorm/AGENTS.md) §Non-negotiables:

```markdown
## Non-negotiables
- Every business rule is a pure use case with a test. The server enforces
  it; the client reuses it only for display (docs/01).
- No payments, no notifications, no health data, one clinic (docs/00).
- A client has no account: a name, a phone number, a booking code, nothing
  more (ADR-0004).
- Instants are stored in UTC and reasoned in the clinic time (docs/03).
- No paid service (ADR-0001).
- An open decision in docs/00 is asked, never assumed.
- One delivery = one page in work/<slug>.md: /propose to define, /apply
  to build.
- No em dash in any text a user reads.
- The agent stages and suggests the commit message. It never commits.
```

Each project line points at the document or ADR that holds its reason, and the booking code comes from a "your call": the agent's answer to how a client with no account proves an appointment is theirs.

docs/06 is the queue: milestones, each with a paragraph saying what is true when it closes, and one line per delivery under it (chapter 9 teaches the marks).
This is the first milestone of [`docs/06-Queue.md`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/brainstorm/docs/06-Queue.md):

````markdown
## Milestone 1: a client books and cancels

When it closes, the owner can register professionals and their weekly hours,
a client can book a free slot, and a client can cancel up to 24 hours before.

```
[ ] skeleton             empty PWA and server in one project, npm run verify, first screenshot
[ ] clinic-setup         a setup command creates the clinic and the owner; the owner signs in and out
[ ] professionals        the owner registers, renames and removes professionals
[ ] weekly-hours         the owner sets each professional's weekly hours
[ ] book-appointment     a client sees free slots for 30 days and books with name and phone
[ ] cancel-appointment   a client cancels up to 24 hours before, or is told why not
```
````

Since focus-kit's commit `bff8414`, `/brainstorm` ends the first milestone with one more line, its review, `m1-review` ([chapter 12](12-closing-a-milestone.md)).
This run used the kit at `26e5e1e`, before that rule, so your queue has one line more than the one above.
The paragraph is the brief's sentence, and the first line is the skeleton the others stand on, which creates `npm run verify`; the next section shows that the first version of this milestone said something else.

## Review before you commit

In the run the command staged nothing and committed nothing, and it ended by showing the queue: you read what it wrote first.[^brainstorm-run]
Check that:

* every answer you gave landed in the document that owns it: the product in docs/00, the stack in docs/01 and its ADR, the milestone in docs/06.
* every "your call" default is one you accept. In the run the agent listed them at the end; each one you reject is a correction now, before a delivery builds on it.
* every ADR records a decision you took, or says it was the agent's call.

When something is wrong, ask the agent for the fix in the same session, which still holds the conversation, and let it write the change ([chapter 6](06-the-documents.md)).

In the run, the agent wrote the documents without asking about the first milestone, its last subject.[^brainstorm-run]
Its milestone 1 held a line `owner-schedule`, the owner's view of the day, and a paragraph that said the owner "sees the day's schedule", while the brief puts that view in the second milestone.
The documents read well, and nothing in them said a subject had been skipped: an agent's text reads as right even when it is wrong, and only a check against what you answered finds it.
The fix was the brief's section for that subject, sent to the same session:[^brainstorm-run]

```markdown
## First milestone
When it closes, the owner can register professionals and their weekly hours, a client can book a free slot, and a client can cancel up to 24 hours before. A professional's absences and the owner's view of the day come in the second milestone.
```

The agent changed only docs/06:[^brainstorm-run]

````diff
--- a/docs/06-Queue.md
+++ b/docs/06-Queue.md
@@ -5,11 +5,8 @@
 
 ## Milestone 1: a client books and cancels
 
-When it closes, the owner has set up the clinic, registered its
-professionals and their weekly hours, and sees the day's schedule; a client
-on a phone books a free slot with a name and a phone number and cancels it up
-to 24 hours before; and the app runs outside the developer's machine with no
-paid service.
+When it closes, the owner can register professionals and their weekly hours,
+a client can book a free slot, and a client can cancel up to 24 hours before.
 
 ```
 [ ] skeleton             empty PWA and server in one project, npm run verify, first screenshot
@@ -18,6 +15,16 @@
 [ ] weekly-hours         the owner sets each professional's weekly hours
 [ ] book-appointment     a client sees free slots for 30 days and books with name and phone
 [ ] cancel-appointment   a client cancels up to 24 hours before, or is told why not
+```
+
+## Milestone 2: the owner runs the day
+
+When it closes, the owner can record a professional's absences, which remove
+their slots, and sees the day's appointments per professional; and the app
+runs outside the developer's machine with no paid service.
+
+```
+[ ] absences             the owner records a professional's absences, and their slots disappear
 [ ] owner-schedule       the owner sees the day's appointments per professional
 [ ] deploy               the app runs on a clinic machine or a free host, with a backup of the data
 ```
````

It also moved `deploy` to the second milestone on its own reasoning, and said so in its reply, so the choice was there to accept or refuse, and the review accepted it.

## Key points

* `/brainstorm` talks through six subjects in order (product, vocabulary, how it is built, conventions, process slots, first milestone) and writes the project documents, the ADRs, `AGENTS.md` and `CLAUDE.md`, never code.
* Each question comes with a default, so "your call" is a valid answer, and you check each default the agent kept.
* Choose a stack by what the project needs, then by how much public code the agent learned from, then by whether types and tests let it check its own work.
* Review before you commit: every answer in the document that owns it, every default one you accept, every ADR a decision you took.
* Ask for a fix in the same session and let the agent write it; the documents read as right even when a subject was skipped.

## Exercises

### Exercise 7.1

In your clone of the guided project, check out `book-v1/install-and-hosts` on a branch of your own, run `/brainstorm`, and answer it with the brief of this chapter.
Compare what you get with `book-v1/brainstorm`: what differs, and does any difference break an answer of the brief?

### Exercise 7.2

Take the Purpose and the three non-negotiables you wrote in exercise 6.2 and compare them with the clinic's.
What did the conversation add that you did not write?

### Exercise 7.3

Pick a stack for a project of your own by the three questions of this chapter, and say which question decided it.

[^octoverse]: GitHub, "Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1", 2025, the latest report on 2026-09-28: monthly contributors on GitHub, August 2025. <https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/>
[^brainstorm-run]: This book's `/brainstorm` run on the guided project, 2026-09-28, with Claude Code 2.1.283 and the model `claude-opus-5-5`, from `book-v1/install-and-hosts` to the chapter tag `book-v1/brainstorm`: the brief, the commands, every turn's output, each question and answer, and the fix. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/brainstorm-run/README.md>
[^claude-code-headless]: Anthropic, "Run Claude Code programmatically", Claude Code documentation, accessed 2026-09-29. <https://code.claude.com/docs/en/headless>
