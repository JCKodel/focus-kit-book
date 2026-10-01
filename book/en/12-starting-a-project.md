# 12. Starting: `/brainstorm` and `/analyze`

After this chapter you can start a new project with `/brainstorm`, or document an existing one with `/analyze`, by conversation, and review the documents either command writes before you commit them.
You can also choose a stack by what the project needs and by how well the agent knows it, and keep what the code cannot say where the agent reads it.

## The problem

Every later session reads the project documents before it acts, so they have to exist before the first delivery.
An agent that starts with nothing written decides everything alone, and a questionnaire fails the other way: it asks a person what they cannot answer yet, or what the code already says.
focus-kit has two commands for this, one for an empty repository and one for a repository with something in it, and both write the same documents by conversation and write no code.

## `/brainstorm`: a new project

`/brainstorm` is the command for a repository with no code yet.
It talks one subject at a time, in this order, and moves on when it could write that document itself, as the kit's file for the command says:

1. **The product** (docs/00): what it is in one sentence, for whom, what it is not, what a good decision looks like here.
2. **The vocabulary** (docs/03): the ten to twenty words the product cannot be described without, each with its name in code.
3. **How it is built** (docs/01): the stack and the shape of the code, with the kit's two choices, FOCUS and the git strategy, each with the agent's recommendation for this stack.
4. **The conventions** (docs/04): the documentation language and the identifier language, the style, where tests live, the commit format.
5. **The process slots** (docs/05): the verify command, the environments, how a screen is proven, when an environment beyond your machine is updated.
6. **The first milestone** (docs/06): three to eight deliveries, one line each, in order, then its review; the first ones are the skeleton the others stand on.

### A default with every question

The agent asks only what it cannot decide with a sensible default, and it states the default with the question.
So "your call" is always a valid answer: the agent keeps its default, and a person who cannot answer still gets a good document.
It never asks about a tool by name when the question is about what you want, and it asks in rounds of at most four questions, its recommendation first.
What cannot be known yet, such as a verify command before any code exists, it writes as "created by the first delivery".

### Choosing the stack

When the conversation reaches how the project is built, three questions choose the stack, in this order.

**What does the project need?**
Start from its value, and leave the language for later: who opens it, on what device, which rules must never break, what it may cost to run.
A stack that cannot deliver that is out, however well the agent knows it.

**How much public code in that stack did the agent learn from?**
A model writes best what it saw most while it was trained, and the nearest public measure of that is how many people write a language in the open.
By GitHub's count, TypeScript became the most used language on GitHub in August 2025, with 2,636,006 monthly contributors, ahead of Python and JavaScript.[^octoverse]
The count is of people and says nothing about lines of code, so read it as a ranking and never as a size.
On Ninjobs the same agent kept missing the design in Flutter, where it had few examples of a customised design system to learn from, and got it right in React.

**Does the stack check itself?**
A compiler that rejects a wrong type and tests that run in seconds tell the agent it made a mistake before you have to.
A stack where a mistake shows only at run time, on a screen, leaves that check to you.

### What it writes, and where it stops

When the six subjects are covered, `/brainstorm` writes docs/00 to 06, one ADR for each decision a later session might undo (the stack, FOCUS or not, git, anything you hesitated on), `AGENTS.md`, `CLAUDE.md` holding the line `@AGENTS.md`, and an empty `work/done/`.
Then it shows the queue and stops.
It writes no code, no configuration and no dependency file: the first delivery does that, with a page of its own, through `/propose` in a fresh session ([chapter 14](14-propose.md)).

For the lending library of Part I, a first milestone could read like this, written for this chapter:

````markdown
## Milestone 1: a librarian lends and takes back

When it closes, a librarian can register books, their copies and members,
lend a copy to a member for 21 days and record its return; a member with an
overdue book or a suspended membership is refused.

```
[ ] skeleton      empty app and server, npm run verify, first screenshot
[ ] catalog       the librarian registers books and their copies
[ ] members       the librarian registers, suspends and reinstates members
[ ] lend-book     the librarian lends a copy, and the rules may refuse it
[ ] return-book   the librarian records a return, and the copy is free again
[ ] m1-review     the milestone checked against its paragraph
```
````

The paragraph says what a person can check when the milestone closes, and the first line, `skeleton`, creates the verify command every later delivery runs; [chapter 13](13-queue-and-milestones.md) teaches the queue.

## `/analyze`: an existing project

`/analyze` is the command for a repository that already has something in it: code, documents, or both.
It works like `/brainstorm`, with a default for every question and the same documents at the end, but it reads before it asks, and what the code says, it does not ask.

### What it reads

The kit's file for the command has it read:

* the README and any documentation already there;
* the manifests, such as `package.json`, `pyproject.toml` or `go.mod`;
* the folder tree, two levels deep;
* the entry points;
* the tests, and how they run;
* the CI configuration;
* the last fifty commit subjects;
* any agent rules file already there, such as `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md` or `.cursorrules`.

From that it infers the stack, how the code is organized, where the business rules live, how errors travel, the verify command and the environments, and it marks each as observed.
What the project does not have, it skips: on a repository with no code the documents describe what the files say.

### What it asks

One round, of four subjects only:

1. The documentation language. Default: the language of the README.
2. The product's purpose and audience in your words, only when no README says it.
3. FOCUS and the git strategy. The default of each is what the code already does, and the agent says what that is, so "your call" keeps it.
4. The first milestone: three to eight deliveries, or where to read them from (issues, a TODO file, a roadmap), then its review.

A rules file already there does not stay beside `AGENTS.md`: its rules move into `AGENTS.md`, and the file keeps only the line that imports it and what applies to its host alone.
The documents describe what exists, not what should exist.
The agent shows the change before it writes, and it changes no code.

### Where the code contradicts itself

Code that has lived for a while says two things at once: a style file asks for single quotes and the code uses double, a guide names a tool that is not installed, a README gives a setup step the configuration does not read.
`/analyze` does not ask you which side is right.
It records an open question in the document that owns the subject, says what each side says, and takes neither; settling it is a delivery of its own, with a page.

### Legacy code: the strangler fig

On code with no clear architecture the default for FOCUS is "neither", because the code does not do it, and FOCUS whole would mean rewriting it.
There is a way between the two: the strangler fig, Martin Fowler's name for replacing an old system gradually, after a vine that grows around a tree until it stands on its own.[^strangler-fig]
New code grows beside the old: every new feature is a vertical slice in FOCUS ([chapter 6](06-features-not-layers.md) and [chapter 7](07-four-pieces.md)), every part a delivery changes moves into one, and the old code goes away one delivery at a time while the project keeps working.
Give it as your answer to the FOCUS question, for example "FOCUS whole, as a strangler fig: new features and every part a delivery touches become vertical slices; the rest stays until then", and `/analyze` writes it into docs/01 and an ADR, so every later `/propose` and `/apply` follows it.

## What the code cannot say: the context folder

The code says what a project does; it rarely says why, for whom, or what was promised.
That knowledge lives in proposals, contracts, emails, meeting transcripts, tickets and slides, and what the agent does not read, it has to guess.
Put everything you have about the project in one folder at the root, `context/`, as it is, with no sorting and no summary, and keep it apart from `docs/`: `context/` is what the agent reads from, `docs/` is what it writes.
The more the folder holds, proposals to the client, meeting transcripts, emails, the better the documents the agent writes from it, and the more of the team it can answer, well beyond the code.
It is the difference between "this was built this way because the client asked for it, in the email of the 12th" and "nobody knows why it is like this".
When a new document arrives, put it in the folder and ask the agent to read it and bring into the project what it changes: a rule into docs/00, a term into docs/03, a line into the queue.
Neither command looks for the folder by name, so say it in the same message, `/analyze Read context/ first, whole.`; that sentence is your instruction, and it works for `/brainstorm` too when a brief or a proposal exists before the code.
Whether the folder is committed, and what must never be, is a decision of its own ([chapter 18](18-project-as-assistant.md)).

## Review before you commit

Either command stages nothing and commits nothing: you read what it wrote first.
Check that:

* every answer you gave landed in the document that owns it: the product in docs/00, the stack in docs/01 and its ADR, the milestone in docs/06;
* every default the agent kept is one you accept knowingly; each one you reject is a correction now, before a delivery builds on it;
* every ADR records a decision you took, or says it was the agent's call;
* on an existing project, every observed statement is true in the code (open the file it names), every open question is a contradiction the code really holds, and nothing describes what should exist instead of what does.

When something is wrong, ask the agent for the fix in the same session, which still holds the conversation, and let it write the change; never edit by hand, because the agent knows which other documents the fix touches.
Read with suspicion.
An agent's text reads as right even when it is wrong: a skipped subject leaves no gap in the prose, and a README's claim copied as a fact reads as well as one the agent checked.
Only a check against what you answered, or against the code, finds either.

## What the team gains

A person who cannot answer a question still gets a good document, because every question carries a default; and nobody is asked what the code already says, because `/analyze` reads it first.
The team starts its first delivery with the product, the vocabulary, the decisions and the queue written down, and every contradiction the code holds recorded as a question instead of settled by a guess.
There is no number for this gain: this book has no count of projects started with and without the two commands.

## Key points

* `/brainstorm` talks through six subjects in order (product, vocabulary, how it is built, conventions, process slots, first milestone) and writes the documents, the ADRs, `AGENTS.md` and `CLAUDE.md`, never code; the first delivery writes the code.
* Every question comes with a default, so "your call" is a valid answer, and you check each default the agent kept.
* Choose a stack by what the project needs, then by how much public code the agent learned from, then by whether types and tests let it check its own work.
* `/analyze` reads the repository first and asks one round; the default of each choice is what the code does, a contradiction becomes an open question, and legacy code can move to FOCUS as a strangler fig.
* Review before you commit, against your answers and against the code, and ask the agent for every fix: its text reads as right even when it is wrong.

[^octoverse]: GitHub, "Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1", 2025, the latest report on 2026-09-28: monthly contributors on GitHub, August 2025. <https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/>
[^strangler-fig]: Martin Fowler, "Strangler Fig", 2024. <https://martinfowler.com/bliki/StranglerFigApplication.html>
