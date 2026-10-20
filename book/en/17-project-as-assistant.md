# 17. The project as the team's assistant

After this chapter you can keep a project's emails, proposals and meeting notes where the agent can read them, bring what they decide into the documents, and ask the project, in plain words, where it stands and what to run next, what is pending, how it is going and who owes an answer.
You can also say what a person must still do with every answer the agent gives.

## The problem

The developer asks the agent about the code.
The manager asks the developer about the status.
The client's emails live in one person's mailbox, and what was agreed on a call lives in the memory of whoever was on it.
Nobody can ask the project itself, so every question costs a person's time, and the answer is only as good as that person's memory on that day.

## What the agent already reads

A focus-kit project already writes most of what a team asks about, because the agent needs it to build:

* **The documents**: the product and its rules in docs/00, the vocabulary in docs/03, the decisions and their reasons in the ADRs.
* **The queue**: every delivery, one line each, with the mark that says where it stands and, on a waiting line, what it waits on (chapter 14).
* **The pages in `work/`**: what is defined now, and what each delivery will do.
* **The pages in `work/done/`**: what each finished delivery did, and what happened while it was built.
* **The git history** (chapter 18): when each commit happened, and which delivery it belongs to, since the commit that closes a delivery ends with the path of its page, `work/done/<slug>.md`.

Read together, they answer the status questions without anyone writing a status.
Pending is every line not yet `[x]`, in the order of the queue.
In progress is the `[~]` and `[*]` lines, and blocked is the `[?]` lines, each with its reason.
How long a delivery took runs from the commit that added its line to the queue to the commit that closed it: from asked to done, the waits included.
The closing commit cannot say it alone, because on trunk a delivery is one commit, which dates its end and not its start; a line added in that same commit has no earlier date, and the history cannot tell how long it took.
None of this was written for the manager; a document that answers the build also answers the team.

## The context folder

What the code and the documents cannot say lives in a folder at the project's root, `context/`: the client's emails, the proposal, the notes of a meeting, a decision the client took on a call.
The agent reads text, so every item is a pair: the original as it arrived, kept as it is, and beside it a Markdown file with the same name plus `.md` (`proposal.pdf.md`) that holds what the original says, whole, not a summary of it; the agent can do the conversion, once, when it arrives, and an item that arrives as text is the Markdown file alone.
Write every message you send there first, as the record, and send a copy of it.
A layout for the lending library of Part I, written for this chapter:

```text
context/
  notes/        one file per meeting, named by its date
  received/     each email or document from outside, with its Markdown
  sent/         each message sent, written here before it goes out
  work-record.md
```

The folder holds what people said; the documents hold what the project decided from it.
`/brainstorm` and `/analyze` read the folder whole when they start, so they do not ask what it already answers.
After that, no session rereads it on its own.
When the client decides that fines do not exist, the message goes to `context/received/`, and nothing changes yet: you ask the agent to read it, and the rule becomes a line of docs/00; a new term goes to docs/03, and a new delivery to the queue in docs/06.
`/propose` reads the decision there, not the message.
Each new message or document goes the same way.
From then on the agent can say why a thing is as it is, and name the message that decided it.

Whether `context/` is committed depends on who will read the repository.
When the repository stays with the team, commit it: a new person, or a new session, finds the history of every decision beside the decision.
When the repository is itself delivered to a client, or will be public, list the folder in `.gitignore` and let only engineering facts cross into the documents.
An ignored folder is still on the disk, so the agent can read it when you ask; only git does not keep it, so back it up somewhere else.
Personal data and anything under a confidentiality clause stay out of the repository in every case, because git keeps a removed file in its history.
With no folder, the agent has no correspondence at all: it reads files, not a mailbox.
This book's own repository is public, so its docs/05 lists `context/` in `.gitignore` and never creates it.

On Case A, a client project on a low-code platform, the repository itself was the contracted deliverable.
Its correspondence folder was kept out of the repository, and only engineering facts crossed over: a decision the client took in a message became a line of a document, never the message.

## The questions the team asks

These are the questions a team asks every week, and the file that answers each:

* **Where are we, and what comes next?** The queue's lines in flight with their marks, the `[?]` lines with their reasons, and the next free line with the command that starts it (the manager's session below shows an answer).
* **What is pending?** The queue's lines not yet `[x]`, milestone by milestone.
* **What is blocked, and on what?** The `[?]` lines, and the reason at the end of each.
* **How is it going?** Lines closed and lines opened per day, from the queue and the commit dates, against the milestone paragraph that says what "closed" means.
* **Who owes me an answer?** The table of questions sent and not answered, in the work record.
* **What must I ask, and whom?** The open decisions in docs/00, and the pages that wait on someone.
* **What did we agree with the client?** docs/00 and the ADRs for what became a rule; the context folder for the message it came from.
* **How long did the last five deliveries take?** For each, the date its line entered the queue and the date of the commit that closed it.

The work record is a file with two tables, in the context folder, or in the repository when it names nobody private, kept up to date by the agent whenever a message goes out or an answer comes in.
For the lending library, written for this chapter:

```markdown
## Questions sent

| Sent  | To             | About                            | Answered |
|-------|----------------|----------------------------------|----------|
| day 3 | head librarian | Are there fines? How much a day? | day 5    |
| day 4 | IT office      | May the system email members?    |          |

## Still open

| Line           | Waits on                    | Since |
|----------------|-----------------------------|-------|
| overdue-notice | IT office: email to members | day 4 |
```

The first table says who was asked what, and when they answered.
The second says which queue line is blocked, on whom, and for how long, so "who owes me an answer" is one table and a reminder to that person is written from it.

Case A kept both tables: questions sent, with to whom, about what and answered when; and still open, with the line, what it waits on and since when.
Its end-of-day status report and its schedule and risk estimate for the project manager say they were written from the queue and the pages, not from memory.
The pace the queue gave, lines closed against lines opened a day, put a scope cut in front of the project manager in the middle of the project, as a decision for them to take.

## The person is the brain

The agent's answer may miss a message nobody put in the folder, read a draft as sent, or count a line whose page says it waits on someone.
So the person keeps three jobs, the same three the prologue gives the person for code.
They interpret: what the answer means for the client, the budget and the date.
They guide: they ask the next question, and point the agent to the file it missed.
They validate: they open the line, the table or the commit the answer rests on.

Ask the agent to name the file behind every answer.
An answer with a file to open is checked in a minute; an answer without one is a guess, however well it is written.

## The manager's session

A manager needs no code editor.
They open the host in the project's root folder, the one with the rules file, and ask in plain words.
The host loads the rules file at the start of the session, and the rules file tells the agent to read the documents before acting, so the manager's session starts from the same documents as the developer's.

The rules file also holds a line for the question a manager asks first: asked where things stand, the agent answers from the queue and `work/`, with the next command written as that host invokes it.
There is no status command, because the queue already is the status.
Asked "where are we?" on the lending library, a session answers this way, in an answer written for this chapter:

```text
Milestone 1, a librarian lends and takes back: 4 of 6 lines done.
In flight: return-book [*], being built.
Waiting: none.
Next free line: m1-review [ ], no page yet.
Run: /propose m1-review (Codex: $propose m1-review)
```

Every part of it is read from docs/06: the milestone's count, the line in flight with its mark, the waits, and the first free line, with the command chapter 8's table gives for each host.
On trunk that is the queue of the folder where the session runs; with a branch or a worktree per delivery the main branch shows each line as it was until its merge, so the session takes each slug's line from its worktree or branch, local or remote, and reconciles them by slug (chapter 14): from the main branch's copy alone, `return-book` would read `[ ]`, and "In flight" would miss the build under way.
A `[?]` line would appear under "Waiting" with its reason and the phase it resumes in, as the line holds them.
An answer from what the session remembers, an offer to keep a status file, or a suggestion to add a status command means the agent did not read the queue: ask for the file behind the answer.

A question touches no code, and the host's plan mode (chapter 12) keeps a session from editing anything.
When the manager wants something changed, such as a new line in the queue, the agent writes it by conversation, as in any session, and a person reviews it and commits it, by default, or asks the agent to; when the Git slot's word lets the agent commit, the person reviews the commit once it lands.
A change to the code, however small, becomes a line as well, with a draft page for the detail, and the answer stops there, naming `/propose` for that session, out of plan mode, or a fresh one (chapter 11).

## What the team gains

One assistant for engineering and product alike: the same documents answer a developer's "where does this rule live" and a manager's "who owes us an answer", and nobody writes a status by hand.
On Case A, twenty questions to outside people were followed to their answers, the two left open were named at the close, and the status and the risk estimate came from a queue that closed about nine lines and opened about six a day.

## Key points

* The documents, the queue, the pages and the git history already answer what is pending, what is in progress and how long each delivery took.
* The context folder holds what the code cannot say, each original beside its Markdown; `/brainstorm` and `/analyze` read it whole when they start, a later item is read when you ask, and what it decides goes into the documents, where `/propose` reads it; it is committed when the repository stays with the team, and kept out when the repository is delivered or public.
* A work record with two tables, questions sent and still open, answers "who owes me an answer" and writes the reminder.
* Ask for the file behind every answer, and interpret, guide and validate it.
* A manager opens the host at the project's root and asks in plain words; the same rules file makes the agent read the documents first; asked where things stand, it answers from the queue, read on trunk in its one file and with a branch or a worktree per delivery from each slug's worktree or branch, with the next command; there is no status command.

