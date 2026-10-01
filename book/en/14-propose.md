# 14. `/propose`: one page

After this chapter you can turn a queue line into a page with `/propose`, read the page as the record of what the agent understood and of what `/apply` will build, cover its holes by conversation before any code exists, and split a delivery that does not fit one page.

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

`/propose <slug>` reads before it asks: docs/00 for the product and its rules, docs/03 for the words the page must use, docs/05 for the project's slots and the format of the page, docs/06 for what comes before and after the line, `work/` for the deliveries in flight, and docs/01 for where the change lives in the code.
Then it talks with you until the scope fits one page, and it asks only where there is more than one reading and no document closes it, its assessment first, in prose, and its recommendation first in every question.
"Your call" is always a valid answer, and a person who cannot answer still gets a good page.

It writes `work/<slug>.md`, marks the line `[>]` in the queue, and stops.
It never writes, edits or generates code, a migration, a test or configuration.
The kit's file for the command gives the reason: "*separating deciding from doing is what keeps scope from growing during implementation*".
`/apply` starts in a fresh session, with a clean context, and the page is all it takes from this conversation, so the page has to hold everything the build needs.

## The page

The format is fixed in the project's docs/05 §3 and is the same in every project:

* **Objective.** One sentence: what the user can do afterwards.
* **Behaviour.** Verifiable scenarios in user language; each line becomes a test or a manual check.
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
  shows as lent to them with a due date 21 days ahead.
* A member with an overdue book is refused with "Return your overdue books
  first"; nothing is recorded.
* Two librarians lend the last copy at the same moment: one succeeds and
  the other sees "This copy was just lent to someone else".

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
* Fines: docs/00 lists them as an open decision, so nobody decides it here.

**Done when.**
* [ ] Unit tests of `lend` pass for the three Behaviour lines.
* [ ] The repository test proves the unique index refuses the second loan.
* [ ] `npm run verify` is green.
* [ ] The lending screen matches the design at both widths.
```

Read it as the agent's account of what it understood.
Each Behaviour line can be checked; the Contract is exact; Out of scope names what someone might have assumed was in; Done when is a list a machine or a person can tick.

The Contract is the one section that must be exact.
The kit's reason: "*a wrong screen is fixed in a session, a wrong column is a migration*".
A screen is code you rewrite; a column holds data, and changing it means moving the data already there.

## Read the page before `/apply`

The page is written to be read, and the questions to ask are these:

* Can each Behaviour line be checked, as a test or by hand?
* Is the Contract exact, down to the names and the types?
* Does Out of scope name something you assumed was in?
* Do you disagree with a choice the agent made on its own?
* Does Done when list what would make you say "done", and nothing vaguer?

You ask for every correction in the same conversation, and the agent writes the fix: on the page, and in any document the fix touches.
You do not edit the page by hand: the agent knows which document owns each fact, so a fix that touches the vocabulary or the queue lands there too, and the conversation keeps the reason.

The order is the cheap one.
A hole found on the page costs one turn; found after `/apply`, it costs another `/apply`, the most expensive command, which builds, tests and proves again.
On Ninjobs, the page of the delivery that computes a candidate's matching score found, while it was being written, that a candidate's approximate age already leaked at the first privacy level through the dates of their experience; it became a line for a later delivery, and no code was written past it.

Hosts have their own way to plan before editing; in Claude Code it is plan mode, where "*Claude reads files and proposes a plan but makes no edits until you approve*".[^claude-code-plan-mode]
Plan mode works inside one session, for the change at hand.
The page works for the project: a file in the repository, in a format every project shares, written from the project documents and in their words, marked in the queue, read by a fresh session to build it, and kept in `work/done/` with what happened.
Use plan mode inside a session if it helps you; the page is what outlives the session.

## When it does not fit

A scope that does not fit one page is two deliveries: `/propose` says so, proposes the split and writes only the first page, and the second becomes a line in the queue, where it belongs.
On Ninjobs the queue's single line for a job posting became six deliveries in one `/propose`: the posting, its employer, its tags, its offer, its benefits and languages, and its life cycle; the page of the first said it was step one of six.
Each of the six was reviewed on its own page and built in its own session.

## What the team gains

The page is the review surface of the team.
A developer, a manager or the client reads one page in the language of docs/03 and knows what is about to be built, what is not, and what "done" will mean, before a line of code exists.
On Case A, the same page format carried questions to the client and documents for handover, so one review skill served every kind of work (chapter 22).
And when the build ends, the same page records what happened, so the history of a decision is one file, named by its slug, in every project the team runs.

## Key points

* A delivery is the smallest change with value, named by a slug, and it fits on one page; if it does not, it is two.
* `/propose` reads the documents, asks only where no document closes a reading, recommendation first, and writes the page and the mark `[>]`, never code.
* The page has a fixed format; the Contract is the one exact section, because a wrong column is a migration.
* Read the page before `/apply` and cover each hole by asking the agent, never by hand: a hole on the page costs a turn, after `/apply` it costs another `/apply`.
* The page is the team's review surface, for code and for anything else that fits a page.

[^claude-code-plan-mode]: Anthropic, "Common workflows", Claude Code documentation, section "Plan before editing", accessed 2026-09-28. <https://code.claude.com/docs/en/common-workflows#plan-before-editing>
