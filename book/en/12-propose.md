# 12. `/propose`: one page

After this chapter you can turn a queue line into a page with `/propose`, read the page as the record of what the agent understood and of what `/apply` will build, cover its holes by conversation before any code exists, and split a delivery that does not fit one page.
You know that `/propose` decides what the project's documents already answer, naming the source on the page, and drafts the Behaviour lines with what must fail and the edges, so your work is to correct the page, not to write it.
You can also explore a problem you do not understand yet by talking to the agent, before there is a page.

## The problem

An agent that plans and builds in one breath takes its decisions in the middle of the build, where you do not see them.
What you did not decide, it decides for you, plausibly, and you meet the guess when a user does.
The page puts every decision where you can read it before any code exists, and it costs a turn of conversation to fix there.

## What a delivery is

Every piece of work in a focus-kit project is a delivery: the smallest change that has value, what other methods call a task or a work item.
It is named by a slug, lowercase words joined by hyphens, such as `lend-book`, written once in the queue line and used from then on for everything about it: the page `work/<slug>.md`, the argument of `/propose <slug>` and of `/apply <slug>`, and the last line of the commit that closes it.
A delivery fits on one page.
If it does not, the scope has not been understood yet, and it is two deliveries.

## What `/propose` does

`/propose <slug>` talks with you until the scope fits one page, and what the project's documents already answer, it does not ask: the kit's file for the command tells it to decide, write the decision on the page and name the document it came from, so if the document is wrong you correct it once, in the review, instead of answering the same question twice.
It asks only where the documents leave more than one reading and none closes it, its assessment first, in prose, and its recommendation first in every question.

To decide, it reads before it asks: docs/00 for the product and its rules, docs/03 for the words the page must use, docs/05 for the project's slots and the format of the page, docs/06 for what comes before and after the line, `work/` for the deliveries in flight, and docs/01 for where the change lives in the code.
When it starts, it marks the line `[~]` in the queue, so anyone reading it sees a delivery being defined, and when the page is written, `work/<slug>.md`, the mark becomes `[>]`.
It ends by showing that queue line, `[>] lend-book ...` for the page below, and asking you to read and question the page, then to run `/apply` in a fresh session.
On a line already `[?]`, it says what the line waits on and goes on only when you say it is resolved; on a line whose `after` names a line not yet `[x]`, it says the same and does not start (chapter 14).
When it finds, while defining, that the scope waits on an answer nobody has given yet or on another line that must be done first, it writes the page as far as it goes and marks the line `[?]` instead, with `· resume: propose` and what it waits on.
It never writes, edits or generates code, a migration, a test or configuration.
The kit's README gives the reason: "*Scope cannot grow during implementation because the person who decided is not in the room.*"
`/apply` starts in a fresh session, with a clean context, and the page is all it takes from this conversation, so the page has to hold everything the build needs.

## The page

The format is fixed in the project's docs/05 §3 and is the same in every project:

* **Objective.** One sentence: what the user can do afterwards.
* **Behaviour.** Verifiable scenarios in user language, each an action with a concrete input and the result the user sees, the cases that must fail and the edges included; each line becomes a test or a manual check. `/propose` drafts them from the documents, and you correct them instead of writing them.
* **Contract.** Data, schema, API, message shapes, or "none".
* **States.** Empty, loading, error, offline, one line each, or "the defaults"; only when there is a screen.
* **Visual reference.** Where the design is, and the viewports; only when there is a screen.
* **Out of scope.** What does not enter, with half a line of reason each.
* **Done when.** A mechanical checklist: tests pass, verify green, screenshot matches.

This is a page for the lending library of Part I, written for this chapter:

```markdown
# lend-book

**Objective.** A librarian records that a member borrowed a copy, and the
system refuses when the rules say no.

**Behaviour.**
* A member with no overdue books borrows an available copy, and the copy
  shows as lent to them with a due date 21 days ahead (docs/00).
* A member with an overdue book is refused with "Return your overdue books
  first"; nothing is recorded.
* A suspended member is refused with "Your membership is suspended";
  nothing is recorded.
* Two librarians lend the last copy at the same moment: one succeeds and
  the other sees "This copy was just lent to someone else".
* A member whose only loan is due today borrows an available copy: due
  today is not yet overdue.

**Contract.**
Table `loan` (copy_id, member_id, lent_at, due_at, returned_at nullable);
unique index on copy_id where returned_at is null.
`lend(copy, member, today): Result<Loan, LendRefusal>` with
`LendRefusal = "HasOverdueBooks" | "AlreadyLent" | "MemberSuspended"`.

**States.** The defaults.

**Visual reference.** The lending screen in the design file, at 390 and
1280 pixels wide.

**Out of scope.**
* Returning a copy: its own delivery, `return-book`, next in the queue.
* Reservations: not in docs/00.
* Fines: docs/00 lists them as an open decision, so nobody decides it
  here.

**Done when.**
* [ ] Unit tests of `lend` pass for the five Behaviour lines.
* [ ] The repository test proves the unique index refuses the second loan.
* [ ] `npm run verify` is green.
* [ ] The lending screen matches the design at both widths.
```

Read it as the agent's account of what it understood.
Each Behaviour line can be checked; the Contract is exact; Out of scope names what someone might have assumed was in; Done when is a list a machine or a person can tick.
Each decision taken from a document names it: the 21 days come from docs/00, and so do Out of scope's reservations and fines.
The agent drafted the cases that must fail and the edge: the Contract already had `MemberSuspended`, so a suspended member gets a line, and a rule about overdue books implies the day a loan is due, which is not yet overdue.

The Contract is the one section that must be exact.
The kit's reason: "*a wrong screen is fixed in a session, a wrong column is a migration, and a wrong access rule has already leaked*".
A screen is code you rewrite; a column holds data, and changing it means moving the data already there; an access rule decides who reads what, and a wrong one has let data out before anyone reads the page again.
No later fix undoes the third.

## Read the page before `/apply`

The page is written to be read, and the questions to ask are these:

* Can each Behaviour line be checked, as a test or by hand?
* Does Behaviour include what must fail and the edges?
* Is the Contract exact, down to the names and the types?
* Does Out of scope name something you assumed was in?
* Does each decision taken from a document name it, and do you agree?
* Do you disagree with a choice the agent made on its own?
* Does Done when list what would make you say "done", and nothing vaguer?

You ask for every correction in the same conversation, and the agent writes the fix: on the page, and in any document the fix touches.
You do not edit the page by hand: the agent knows which document owns each fact, so a fix that touches the vocabulary or the queue lands there too, and the conversation keeps the reason.
If `/propose` asks what a document already says, such as how many days a loan lasts when docs/00 says 21, say so in the conversation: the answer belongs on the page, with its source.
If Behaviour holds only the happy path, an available copy lent to a member in good standing, ask the agent for the cases that must fail and the edges before `/apply`.

The order is the cheap one.
A hole found on the page costs one turn; found after `/apply`, it costs another `/apply`, the most expensive command, which builds, tests and proves again.
On Ninjobs, the page of the delivery that computes a candidate's matching score found, while it was being written, that a candidate's approximate age already leaked at the first privacy level through the dates of their experience; it became a line for a later delivery, and no code was written past it.

Hosts have their own way to plan inside one session, such as Claude Code's plan mode, where "*Claude reads files and proposes a plan but makes no edits until you approve*";[^claude-code-plan-mode] the page is what outlives the session: a file in the repository, written from the project's documents in their words, marked in the queue, read by a fresh session to build it, and kept in `work/done/` with what happened.

## When it does not fit

A scope that does not fit one page is two deliveries: `/propose` says so, proposes the split and writes only the first page, and the second becomes a line in the queue, where it belongs.
On Ninjobs the queue's single line for a job posting became six deliveries in one `/propose`: the posting, its employer, its tags, its offer, its benefits and languages, and its life cycle; the page of the first said it was step one of six.
Each of the six was reviewed on its own page and built in its own session.

## When you do not know yet

Some scopes do not fit a page because nobody knows the answer yet: how an unfamiliar API behaves, or which of two approaches holds.
Other methods call the work that finds out a spike; here it is a conversation with the agent, in any session, before any page.
The agent is a language model you talk with, not a button that runs a fixed command, and it reads the project's documents, so what it suggests follows the project.
The conversation ends in one of three ways: a new line in the queue, with a draft page holding what the exploration found when the line cannot hold it, which `/propose` starts from in a fresh session (chapter 11); a decision you accept, written in the document that owns it (chapter 7); or nothing, when what you found leaves the plan as it is.
On my projects this was rarely needed, and the conversation was always enough, so no mark, command or kind of delivery was added for it: none would name an error it caught, which is the governor of chapter 16.

## What the team gains

The page is the review surface of the team.
A developer, a manager or the client reads one page in the language of docs/03 and knows what is about to be built, what is not, and what "done" will mean, before a line of code exists.
On Case A, the same page format carried questions to the client and documents for handover, so one review skill served every kind of work (chapter 21).
And when the build ends, the same page records what happened, so the history of a decision is one file, named by its slug, in every project the team runs.

`/propose` decides and drafts because each prevents an error.
A `/propose` that asks what docs/00 to 05 already settle makes the kit slower than working by hand; a decision written with its source leaves one correction, in the review, and only where a document is wrong.
A person who does not know the tool being built leaves the expected result to the agent, which delivers one solution, happy path only, and the client rejects it; Behaviour drafted from the documents, with what must fail and the edges, puts those cases in front of the person before any code exists.

## Key points

* A delivery is the smallest change with value, named by a slug, and it fits on one page; if it does not, it is two.
* `/propose` decides what the documents answer and names the source on the page, asks only where they leave more than one reading, recommendation first, marks the line `[~]` while it talks and `[>]` when the page is written, or `[?]` when the scope waits, and never writes code.
* The page has a fixed format and is the team's review surface, for code and for anything else that fits a page; the Contract is the one exact section, because a wrong column is a migration.
* `/propose` drafts Behaviour, what must fail and the edges included; you read the page before `/apply` and correct it by asking the agent, never by hand: a hole on the page costs a turn, after `/apply` it costs another `/apply`.
* When nobody knows the answer yet, explore it by talking to the agent, and end with a queue line, with a draft page when the line cannot hold what you found, a decision written where it belongs, or neither; nothing new is needed for it.

[^claude-code-plan-mode]: Anthropic, "Common workflows", Claude Code documentation, section "Plan before editing", accessed 2026-09-28. <https://code.claude.com/docs/en/common-workflows#plan-before-editing>
