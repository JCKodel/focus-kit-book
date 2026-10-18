# 7. The documents: one place per fact

After this chapter you can say what each of the seven project documents, the ADRs, the manuals and `AGENTS.md` hold, and decide which one a new fact belongs in.
You can also change any of them by talking to the agent, and say why that gives every session and every person the same answer.

## The problem

A fresh session knows only what is written in files.
A fact that lives in someone's head never reaches it, and a fact written in several places goes stale in some of them, so the agent reads whichever copy it finds first.
On Ninjobs a decision lived in six places, and keeping them in step cost more than the work.

## One place per fact

Each fact of the project lives in one place, and the agent reads it there.
focus-kit gives those places a fixed shape: seven numbered documents, docs/00 to docs/06; a folder of decisions, `docs/adr/`; a folder of manuals, `docs/manuals/`, one per action of more than one command, done by hand outside a delivery or a proof `/apply` runs on another machine; the rules file, `AGENTS.md`; and `work/`, which holds one page per delivery (chapter 12).
The numbers are fixed because the commands cite them; the name after the number is in the documentation language, `00-Product.md` in a project documented in English and `00-Produto.md` in one documented in Portuguese.
`/brainstorm` or `/analyze` writes them once (chapter 9); `/propose` and `/apply` read them before they act.

An agent answers from what is in its window, so what matters is which text gets there.
Retrieval-augmented generation (RAG) is one way to bring it: with each question, a retriever finds passages in a body of writing kept outside the model, and the model answers from them.
The term and the method come from a 2020 paper by Patrick Lewis and colleagues at Facebook AI Research, whose retriever searched an index of Wikipedia.[^lewis-rag-2020]
focus-kit's documents work as retrieval made for the project: the body of writing is the project's own documents, written for that use, one place per fact.
The agent finds what it needs by name, since `AGENTS.md` and the commands tell it which document holds which fact, and it reads that document when it needs it, with its own tools, which Anthropic calls loading context "*just in time*".[^anthropic-context-2025]
For me, this is the documents' main value.

Every focus-kit project gives each document the same number, as the kit's description of the documents numbers them.
So docs/06 is the queue in any focus-kit project, what to do, what is being done and what is done, and every other number holds the same document there, whatever the name after it.

## The seven documents

**docs/00, the product.** What the product is and for whom: its purpose in one paragraph, its audience, how it works in the user's words, what it is not, the values decisions are measured against, the product questions every decision must answer yes to, and the open decisions, what nobody may close alone.
Nothing may contradict it without changing it in the same delivery.

**docs/01, the architecture.** The design in one sentence, the stack with the reason for each choice that had an alternative, how the code is organized, how data is accessed, how errors travel, the environments, and what was tried and removed on purpose, so nobody rebuilds it.

**docs/02, the backend.** Present only when a server holds rules the client must not duplicate: the schema, the access rules, the functions the client may call.
Otherwise it is one line: there is none.

**docs/03, the domain.** One table of the project's terms, with the identifier each has in code and what it means, then the entities and the rules that always hold for them.
The table is the vocabulary: every page, identifier and test uses its terms, and a new concept enters here before it enters anywhere else.

**docs/04, the conventions.** The language of the documents and of the identifiers, naming, style and the tool that enforces it, where tests live and what each level tests.

**docs/05, the process.** The kit's process, the same in every project: the rule, the flow from queue to commit, the shape of a page, the queue, the commit and the format of its message, what the process does not have, and how a milestone closes.
One section is filled in by the project, "This project", whose entries are its ten slots: the documentation language, the command that verifies a delivery, the environments, how a screen is proved, when anything is published, whether `context/` is committed, who reviews a delivery's changes before `/apply` ends (chapter 13), the manuals, the areas the milestone review's code reading splits into and the model its readers and checker run on (chapter 15), and the git strategy.
Whatever the publish policy says, `/apply`'s last words say which environment is at which version (chapter 13).
A slot says what and the command, in a few lines, because `/apply` reads it every time; the steps go in a manual, and what a command prints stays in its help.
So a slot does not say which delivery created its command or how it used to work: that history is on the delivery's page in `work/done/` and in the ADR.
The commands read these facts here, so no command file holds any of them.

**docs/06, the queue.** The milestones, each with a paragraph saying what is true when it closes, and under each one line per delivery, in order, with a mark for its state (chapter 11).
It is the document you touch most: the whole of the project's work, added to and edited every day, by conversation.
It does what a kanban board or a backlog of work items does in an agile process, with one difference: the agent reads it.
Every document is read, and corrected when it is wrong; the queue is the one that gives the product its shape.

## The two choices

The kit offers two choices and imposes neither: the architecture and the git strategy.
`/brainstorm` and `/analyze` explain each one with a recommendation for the project's stack, and record the answer.

**The architecture.** FOCUS is the architecture of chapter 4: code organized in vertical slices, every business rule a pure function that returns a Result (chapter 3), and four pieces through which an event flows one way to a new state.
The kit gives three answers: FOCUS whole; the two principles only, vertical slices and exceptions as values, in whatever structure the stack favors; or neither, the project's own conventions.
With any of the three, the page, the queue, the documents, verify and the commit work the same.
What FOCUS adds is in the code: an agent reads one slice for a change (chapter 4), which the two principles give too, and each of the four pieces has its own test (chapter 5).
Ninjobs, a thin web app over a backend as a service, chose the two principles.
On a repository that already has code, the default is what the code already does.
docs/01 records the answer, and an ADR records why.

**The git strategy.** Three answers, each for one way of working: trunk, everything on the main branch, for one person, alone or with several sessions on free lines (queue lines not done, not waiting and needing no other line done first, defined yet or not; [chapter 14](14-queue-states.md)) that touch different files; a branch per delivery, merged through a reviewed pull request, for sequential work; a worktree per delivery, a second working folder on its own branch, for several people, or for one person whose deliveries touch the same files.
In every one, a delivery's page and build are one change that reverts in one step, and the agent never commits or merges.
Chapters 18 and 19 teach the three.
The Git slot of docs/05 records the answer, and an ADR records why.

## ADRs

ADR stands for Architecture Decision Record.
An ADR is one file per decision, `docs/adr/ADR-NNNN-<slug>.md`, with its context, the decision, its consequences and its date.
Michael Nygard proposed the format in 2011, because "*one of the hardest things to track during the life of a project is the motivation behind certain decisions*".[^nygard-adr]
An ADR is amended, never rewritten: when the decision changes, an amendment below it says what changed and when, and the original reason stays above.
The next person who wants to change it again reads why it was so, and weighs the old reason instead of guessing at it.

## Manuals

Some of a project's work is an action of more than one command, of two kinds.
One is done by a person, by hand, outside any delivery: publishing the app, rolling back a release, rotating a secret, setting up a service.
The other is a proof `/apply` runs on another machine: in the lending library's docs/05, written for this chapter, the Proof of a screen slot names the command that proves a screen and points to `docs/manuals/prove-on-the-test-server.md`, where `/apply` finds the steps to publish a preview to the test server and run the end-to-end tests there.
Each of these gets a manual, one file in `docs/manuals/`, named in the documentation language after what it does, so whoever needs it finds it by its name.
A manual stands alone for whoever runs it, having read nothing else, and holds six things, as the kit's docs/05 says: what it does and when, what must be in place, the commands in order, how to tell it worked, how to undo it, and what breaks if a step is skipped.
The slot says what and the command, and the manual holds the steps for whoever runs them.
A single command, such as the one that verifies a delivery, needs no manual: it stays in its slot.

In the same docs/05, the Environments slot names the command that publishes the app and points to `docs/manuals/publish-the-app.md`; the steps live only there.
`/analyze` writes the manuals for what a repository already does by hand, `/apply` writes or updates one when a delivery adds or changes it ([chapter 13](13-apply.md)), and `/brainstorm` writes none.
The folder is created with the first manual, so there is no empty folder, and `AGENTS.md` points to it.

## AGENTS.md

`AGENTS.md` is the rules file of chapter 1, an open format that coding agents read at the start of a session.[^agents-md]
Every host of chapter 8 reads it, on its own or through a pointer; Claude Code reads it through `CLAUDE.md`, which holds the line `@AGENTS.md` and, below it, only what applies to Claude Code alone.
`AGENTS.md` names no host's tool, so it reads the same in every one.

It has four short sections: what to read before acting, the non-negotiables, what not to rebuild, and how to work.
The kit's description of the documents gives it three rules: sixty lines at most, everything in it points at a document, and nothing in it is the only place a rule is written.
It is loaded whole into every session, so it stays short; and a rule that lived only there would have no reason written anywhere.

## Where a new fact goes

A new fact has one owner, and you find it by asking these questions in order; the first that fits names the document:

1. Is it a choice between alternatives, with a reason someone may want to revisit?
   An ADR holds the choice and the reason, and the document it governs holds the result.
2. Is it what the product is, for whom, what it is not, a value, or something nobody closes alone?
   docs/00.
3. Is it a word, an entity, or a rule that always holds for the data?
   docs/03.
4. Is it how the thing is built: the stack, where code goes, data access, errors, environments?
   docs/01, or docs/02 when a server holds the rule.
5. Is it how code or text is written: naming, style, tests?
   docs/04.
6. Is it a fact of this project that the commands read: the verify command, the environments, whether `context/` is committed, how a delivery and a milestone are reviewed, git?
   A slot of docs/05, what and the command, in a few lines.
7. Is it the steps a person follows by hand outside a delivery (publish, roll back, rotate a secret, set up a service), or those of a proof `/apply` runs on another machine?
   A manual in `docs/manuals/`, the slot keeping the command and pointing to it.
8. Is it work to do?
   docs/06 holds its line, and the page in `work/` holds the delivery.

`AGENTS.md` is never the answer: when every session must keep a fact in mind, a line there points at its owner.

Take the lending library of Part I, and the sentence "a member keeps a copy for 21 days".
It holds three facts, and each has a different owner.
The term and its value, the loan period of 21 days that gives a loan its due date, go to docs/03, question 3, where the table names it and gives the identifier the code uses.
The rule the member meets, that a copy comes back by its due date and a member with an overdue copy borrows nothing more, goes to docs/00, question 2, in the user's words, citing the loan period by name.
And if a server sets the due date when it records a loan, so that no client can change it, how it does so goes to docs/02, question 4.
The number is written once, in docs/03; the other two documents use the term.
One sentence of a conversation can hold several facts like these, and each lands with its owner, none repeating what another holds.

## Living documents

A delivery that changes behaviour updates the document that owns the fact, in the same delivery.
The next session reads the change with everything else and follows it without being told again.

You do not edit the documents by hand; you talk to the agent to change them, pointing at a gap, a wrong detail, something to add, change or remove.
It finds the document that owns the fact and writes the change there, since the documents tell it where each fact lives, and the conversation keeps the reason.
Your part is to interpret, guide and validate: say what the change means, steer it, and read it before you commit.
An agent's text reads as right even when it is wrong, so you check it against what you know and never trust it blindly, as you would not trust a colleague's.

The open decisions of docs/00 are where the agent stops.
The library's docs/00 lists fines for late returns as open, so a page that touches late returns names them as out of scope, and an agent asked to build them stops and asks, where it would otherwise have picked an amount and a rule on its own.

## What the team gains

The same answer in every session and for every person: a developer, a manager and a fresh agent who ask the loan period read one line in one document.
With one place per fact, a change is written once and every later session reads it, where on Ninjobs every delivery paid to keep a decision's six copies in step.
A manual puts the steps a person follows by hand where that person looks for them, in a file found by its name, and keeps a proof's steps out of the slot every `/apply` reads before its first edit.
What I value most: every session and every person retrieves a fact from the same place, and in another focus-kit project from the same number.

## Key points

* Each fact lives in one place: seven numbered documents, `docs/adr/`, `docs/manuals/`, `AGENTS.md` and `work/`; docs/00 is the product and its open decisions, docs/01 and docs/02 how it is built, docs/03 the vocabulary, docs/04 the conventions, docs/05 the process with the project's slots, each what and the command, docs/06 the queue, with numbers fixed because the commands cite them, the same in every project.
* The two choices, the architecture (FOCUS whole, the two principles, neither) and git (trunk, a branch or a worktree per delivery), are recorded in docs/01 and docs/05, each with an ADR that is amended, never rewritten; the method works the same under any of them.
* An action of more than one command, done by hand outside a delivery or a proof `/apply` runs on another machine, has a manual in `docs/manuals/`, for whoever runs it, having read nothing else; the slot keeps the command and points to it, `/analyze` and `/apply` write the manuals, `/brainstorm` none.
* A new fact goes to the first document whose question fits; one sentence can hold several facts, each with its own owner, and `AGENTS.md` only points at them.
* You change the documents by talking to the agent, and you interpret, guide and validate what it writes; an open decision makes it stop and ask.

[^nygard-adr]: Michael Nygard, "Documenting Architecture Decisions", Cognitect blog, 2011. <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions>
[^agents-md]: AGENTS.md, "AGENTS.md", accessed 2026-09-30. <https://agents.md>
[^lewis-rag-2020]: Patrick Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", 2020. <https://arxiv.org/abs/2005.11401>
[^anthropic-context-2025]: Anthropic, "Effective context engineering for AI agents", 2025. <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
