# The documents

After this chapter you can say what each of the seven project documents, the ADRs and `AGENTS.md` hold, and decide which one a new fact belongs in.
You can also explain why an agent that reads them in a fresh session builds what was decided.

## One place per fact

A fresh session knows only what is written in files ([chapter 2](02-how-agents-see.md)), and a decision written in several places goes stale in some of them ([chapter 4](04-birth-of-focus-kit.md)).
So each fact of the project lives in one place, and the agent reads it there.
focus-kit gives those places a fixed shape: seven numbered documents, `docs/00` to `docs/06`; a folder of decisions, `docs/adr/`; the rules file, `AGENTS.md`; and `work/`, which holds one page per delivery.[^focus-kit-documents]
The numbers are fixed because the commands cite them; the name after the number is in the documentation language, `00-Product.md` in this book and `00-Produto.md` in a project documented in Portuguese.[^focus-kit-documents]

This book is written with focus-kit, so its repository has the same set, and the excerpts below come from it, as it was at one commit.[^book-docs]
Chapter 7 writes the set for the clinic.

## The seven documents

`/brainstorm` and `/analyze` write the seven documents; `/propose` and `/apply` read them before they act.
`/propose` reads docs/00, docs/03, docs/05, docs/06 and the pages in `work/`, and docs/01 to see where a change lands; `/apply` reads `AGENTS.md`, docs/01, docs/04 and docs/05.[^focus-kit-commands]

### docs/00, the product

docs/00 says what the product is and for whom: its purpose in one paragraph, its audience, how it works in the user's words, what it is not, the values decisions are measured against, the product questions and the open decisions.[^focus-kit-documents]
Nothing may contradict it without changing it in the same delivery.
You read it when a decision is in doubt, and `/propose` reads it before it writes a page.
These are the product questions of this book's docs/00, the checklist every delivery of the book is held to:

```markdown
## Product questions

Every decision must answer yes to all of these:

1. Does the chapter open with what the reader can do after reading it?
2. Does every sentence carry value, and is nothing the reader needs left out?
3. Is every artifact real and every number traceable to a source?
4. Would the text be safe if the private case it draws on were read by its owner's competitor?
5. Can a reader who has read only the previous chapters follow it?
6. Are both editions updated in this delivery?
```

Each question can be answered yes or no about one chapter, so a page can be checked against it: this chapter was read against question 2, sentence by sentence, before it was done.

docs/00 ends with its open decisions: what nobody closes alone, so an agent never settles it by assumption.[^focus-kit-documents]
This book's OD-3 says that the author approves the anonymized text of every passage drawn from a private case before the chapter is done.
An agent that writes such a passage reads that line and stops to ask, where it would otherwise have judged its own anonymization good enough.

### docs/03, the domain

docs/03 is one table of the project's terms, then the entities and the rules that always hold for them.[^focus-kit-documents]
The table is also the vocabulary: every page, identifier and test uses its terms, and a new concept enters here before it enters anywhere else.
This book's table has a column for the Portuguese term, since the book has two editions; this is its header and the row for delivery, the unit of work each page describes:

```markdown
| Term | Portuguese | Identifier | Meaning |
|---|---|---|---|
| delivery | entrega | `<slug>` | The smallest unit of work with value; it fits on one page. |
```

The row fixes the word, the name files use for it and what it means, so a page that says "delivery" and a file named after a slug mean the same thing.

### docs/01, the architecture, and docs/02, the backend

docs/01 holds the design in one sentence, the stack with the reason for each choice that had an alternative, how the code is organized, how data is accessed, how errors travel, the environments, and what was tried and removed on purpose, so it is not rebuilt.[^focus-kit-documents]
`/apply` reads it to know where each piece goes.
docs/02 exists only when a server holds rules the client must not duplicate: the schema, the access rules, the functions the client may call; otherwise it is one line.[^focus-kit-documents]
This book's docs/02 is that line: "There is none. The book is static; no server holds rules."
The kit offers two choices and imposes neither, and the documents record them: the architecture, FOCUS or the project's own, in docs/01, and the git strategy in docs/05; Parts III and IV teach them.

### docs/04, the conventions

docs/04 holds the documentation and identifier languages, naming, style and the tool that enforces it, where tests live and the commit message format; section 6 shows one of its rules.[^focus-kit-documents]

### docs/05, the process

docs/05 is the kit's process template, the same in every project, with one section filled in by the project: §5, "This project", whose entries are the slots, the facts of this project that the commands read.[^focus-kit-documents]
These are two slots of this book's §5, the command that checks a delivery and the git strategy:

```markdown
* **Verify:** `make verify`, which runs the strict site build, edition
  parity, the em dash check, the prose rules, the link check and the
  disclosure scan. Green before anything is declared done. Created by
  `site-skeleton` (build, parity, em dash); `disclosure-scan`,
  `prose-rules` and `link-check` add their checks to it; `commit-hooks`
  adds the commit messages and the hooks to the disclosure scan.
* **Git:** trunk. The agent stages; it never commits or merges.
```

The names in backticks after "Created by" are this book's deliveries, lines of its queue, and the slot records which one added each check.
`/apply` reads the verify command here, so its command file holds none: the rule that came later on Ninjobs, that a command holds no fact of the project.
docs/05 also holds the flow from queue to commit, §2, and the shape of a page, §3; chapters 10 and 11 teach them.

### docs/06, the queue

docs/06 lists the milestones, each with a paragraph saying what is true when it closes, and under each one line per delivery, in order, with a mark for its state.[^focus-kit-documents]
Chapter 9 teaches it.

## ADRs

An ADR (architecture decision record) is one file per decision, `docs/adr/ADR-NNNN-<slug>.md`, with its context, the decision, its consequences and its date.[^focus-kit-documents]
An ADR is amended, never rewritten: when the decision changes, an amendment below it says what changed and when, and the original reason stays above, so the next person who wants to change it again reads why it was so.
This is this book's ADR-0010, which chose the git strategy of the Git slot above:

```markdown
# ADR-0010: trunk

**Date:** 2026-09-24

## Context

A worktree per delivery would let agents write chapters in parallel, but shared files (navigation, glossary, queue) would conflict, and the author reviews every delivery alone.

## Decision

Everything happens on `main`, one delivery at a time.
The agent stages and suggests the message; the author reviews and commits.

## Consequences

The simplest history. Part IV still teaches branches and worktrees, from the other cases.
```

The context keeps why the alternative lost (a worktree is a second working folder where another agent builds at the same time; Part IV teaches it): if the book gains a second reviewer, an amendment can answer that reason and not guess at it.

## AGENTS.md

Chapter 2 showed the start of this book's rules file, up to the list of documents to read before acting.
This is the rest of it:

```markdown
## Non-negotiables
- Nothing private enters the repository: private cases are only Case A and Case B, with no name, place, date of meeting, path or business detail; the disclosure scan is green (docs/03, ADR-0012).
- Ninjobs appears only through its process artifacts and published numbers, paraphrased; never its infrastructure, credentials, users or commercial plans (docs/03).
- A change to one edition is a change to both, in the same delivery; English is the source (ADR-0004).
- Every chapter opens with what the reader can do after it and is as long as proving that takes: no filler, nothing useful cut, no length target (ADR-0015).
- Every artifact shown is real and every number cites its source (docs/04).
- The book mentions none of the author's earlier books and copies no text from them (ADR-0005).
- One delivery = one page in work/<slug>.md: /propose to define, /apply to build.
- No em dash in any text a user reads.
- The agent stages and suggests the commit message. It never commits.

## Do not rebuild
- A GitHub wiki, written or mirrored (ADR-0001).
- Code examples in several languages (ADR-0008).
- A link shortener or playground server for snippets; the guided project's tags do that (docs/01).
- The `[?]` mark (ADR-0013).

## How to work
- Chapters are `book/<edition>/NN-<slug>.md`, same file name in both editions; scripts in `scripts/` (docs/01).
- Every check prints `file:line: rule: message` and exits non-zero (docs/01).
- `make verify` before declaring anything done.
- Abstraction on the second concrete occurrence, and the delivery says which was the first.
- Ambiguity → ask. Documents are living: a delivery that changes behaviour updates the document that owns it, in the same delivery.
```

Most lines end with the document or the ADR that holds the rule whole: the line reminds the agent at the start of every session, and the owner holds the reason.

The kit's rules for this file are three: sixty lines at most, everything in it points at a document, and nothing in it is the only place a rule is written.[^focus-kit-documents]
It is loaded whole into every session, so it stays short, and a rule that lived only here would have no reason written anywhere; Claude Code also reads it through the `CLAUDE.md` of chapter 5.

## Living documents

When I reviewed chapter 3, its excerpts showed each tool's scenario without the project or the brief it answered, and one was a single line that leaned on the line above it.
I fixed the chapter, and in the same commit I wrote the fix into docs/04, the conventions, as two rules for every chapter, "Context before an excerpt" and "Teach, do not only show".[^book-docs-context]
This is the first, as docs/04 holds it:

```markdown
* **Context before an excerpt.** A reader who has read only the previous chapters understands every artifact shown without opening anything else (docs/00 product question 5).
  Before it, the text gives what the artifact is about: the project, the problem it answers, where it comes from.
  An excerpt is a whole unit that means something on its own (a user story with its scenarios, a requirement, a page's section), never a loose line that leans on the lines around it; when several tools are compared, each shows the same unit.
```

The rule names the product question it serves, so the reason travels with it.
Chapter 5 was written after that commit: its page put the clinic and its starting tag before the install report, and its delivery added two sentences introducing the guided project, citing the rule; nobody repeated the request.[^book-docs-context]
Every section of this chapter follows the same rule.

That is a living document: a delivery that changes behaviour updates the document that owns it, in the same delivery.[^focus-kit-documents]
The next session reads the change with everything else, and follows it without being told again.

You do not have to edit the documents by hand, and I recommend you do not.
Talk to the agent: point at a gap, a wrong detail, something to add, change or remove, and it finds the document that owns the fact and writes the change there, faster and more precisely than you would by hand, since the documents tell it where each fact lives.
Your part is to interpret, guide and validate: say what the change means, steer it, and read it before you commit.
An agent's text reads as right even when it is wrong, so you check it against what you know and never accept it on trust; you are the brain of the operation, and the agent writes.

## Key points

* Each fact of a project lives in one place: seven numbered documents, `docs/adr/`, `AGENTS.md` and `work/`, with numbers fixed because the commands cite them.
* docs/00 is the product and its open decisions, docs/03 the vocabulary, docs/01 and docs/02 how it is built, docs/04 the conventions, docs/05 the process with the project's slots, docs/06 the queue.
* An ADR records one decision with its reason, and is amended, never rewritten, so the reason survives the next change.
* `AGENTS.md` is short and only points: nothing in it is the only place a rule is written, and the commands hold no fact of the project.
* A delivery that changes behaviour updates the document that owns it, in the same delivery, and every later session follows the change; the agent writes it, and you guide it and check it, never on trust.

## Exercises

### Exercise 6.1

In your clone of the guided project, check out `book-v1/install-and-hosts` and open `.claude/skills/brainstorm/references/documents.md`, the kit's own description of the documents.
Which of the clinic's documents might read "there is none", and what would decide it?

### Exercise 6.2

Write by hand the clinic's docs/00 Purpose paragraph and three non-negotiables.
Keep them, to compare with what `/brainstorm` writes in chapter 7.

### Exercise 6.3

In this book's [`AGENTS.md`](https://github.com/JCKodel/focus-kit-book/blob/6c2713b63af7397ee00142497287b8408a5651b1/AGENTS.md), find the document each line points at, and any line that is the only place its rule is written.

[^focus-kit-documents]: J.C. Ködel, "focus-kit", `SETUP.md` §3.5, the file `references/documents.md`, at commit 26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b. https://github.com/JCKodel/focus-kit/blob/26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b/SETUP.md
[^focus-kit-commands]: J.C. Ködel, "focus-kit", `SETUP.md` §3.3 and §3.4, the files of `/propose` and `/apply`, at commit 26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b. https://github.com/JCKodel/focus-kit/blob/26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b/SETUP.md
[^book-docs]: J.C. Ködel, "One Page at a Time", this book's repository at commit 6c2713b63af7397ee00142497287b8408a5651b1: the excerpts of docs/00, docs/03, docs/05, ADR-0010 and `AGENTS.md`. https://github.com/JCKodel/focus-kit-book/tree/6c2713b63af7397ee00142497287b8408a5651b1
[^book-docs-context]: J.C. Ködel, "One Page at a Time", commit 297af60dedb088bad441555c8bc019a60ce4e612, which fixed chapter 3 and added "Context before an excerpt" to docs/04, https://github.com/JCKodel/focus-kit-book/commit/297af60dedb088bad441555c8bc019a60ce4e612; and chapter 5's page, which cites it. https://github.com/JCKodel/focus-kit-book/blob/6c2713b63af7397ee00142497287b8408a5651b1/work/done/install-and-hosts.md
