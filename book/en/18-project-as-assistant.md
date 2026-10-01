# The project as the team's assistant

After this chapter you can keep a project's emails, proposals and meeting notes where the agent reads them, and ask the project, in plain words, what is pending, how it is going and who owes an answer.
You can also say what a person must still do with every answer the agent gives.

## The problem

The developer asks the agent about the code.
The manager asks the developer about the status.
The client's emails live in one person's mailbox, and what was agreed on a call lives in the memory of whoever was on it.
Nobody can ask the project itself, so every question costs a person's time, and the answer is only as good as that person's memory on that day.

## What the agent already reads

A focus-kit project already writes most of what a team asks about, because the agent needs it to build:

* **The documents** (chapter 10): the product and its rules in docs/00, the vocabulary in docs/03, the decisions and their reasons in the ADRs.
* **The queue** (chapter 13): every delivery, one line each, with its mark: `[ ]` not yet defined, `[>]` defined and waiting to be built, `[x]` done.
* **The pages in `work/`** (chapter 14): what is defined now, and what each delivery will do.
* **The pages in `work/done/`**: what each finished delivery did, and what happened while it was built.
* **The git history** (chapter 19): when each commit happened, and which delivery it belongs to, since the commit that closes a delivery ends with its slug.

Read together, they answer the status questions without anyone writing a status.
Pending is the `[ ]` and `[>]` lines, in the order of the queue.
In progress is the pages in `work/`.
How long a delivery took is the distance between the first commit that touched its page and the commit that moved it to `work/done/`.
None of this was written for the manager; a document that answers the build also answers the team.

## The context folder

What the code and the documents cannot say lives in a folder at the project's root, `context/` (chapter 12): the client's emails, the proposal, the notes of a meeting, a decision the client took on a call.
Keep it in Markdown, because the agent reads text: a PDF or an exported email becomes a Markdown file once, when it arrives, and the agent can do the conversion.
Write every message you send there first, as the record, and send a copy of it.
A layout for the lending library of Part I, written for this chapter:

```text
context/
  notes/        one file per meeting, named by its date
  received/     each email or document from outside, as Markdown
  sent/         each message sent, written here before it goes out
  work-record.md
```

The folder holds what people said; the documents hold what the project decided from it.
When the client decides that fines do not exist, the message goes to `context/received/`, and the rule becomes a line of docs/00, where `/propose` reads it.

Whether `context/` is committed depends on who will read the repository.
When the repository stays with the team, commit it: a new person, or a new session, finds the history of every decision beside the decision.
When the repository is itself delivered to a client, or will be public, list the folder in `.gitignore` and let only engineering facts cross into the documents.
An ignored folder is still on the disk, so the agent reads it in every session; only git does not keep it, so back it up somewhere else.
Personal data and anything under a confidentiality clause stay out of the repository in every case, because git keeps a removed file in its history.

On Case A, a client project on a low-code platform, the repository itself was the contracted deliverable.
Its correspondence folder was kept out of the repository, and only engineering facts crossed over: a decision the client took in a message became a line of a document, never the message.

## The questions the team asks

These are the questions a team asks every week, and the file that answers each:

* **What is pending?** The queue's `[ ]` and `[>]` lines, milestone by milestone.
* **How is it going?** Lines closed and lines opened per day, from the queue and the commit dates, against the milestone paragraph that says what "closed" means (chapter 13).
* **Who owes me an answer?** The table of questions sent and not answered, in the work record.
* **What must I ask, and whom?** The open decisions in docs/00, and the pages that wait on someone.
* **What did we agree with the client?** docs/00 and the ADRs for what became a rule; the context folder for the message it came from.
* **How long did the last five deliveries take?** The commit dates of their five slugs.

The work record is a file with two tables, in the context folder, or in the repository when it names nobody private, kept up to date by the agent whenever a message goes out or an answer comes in.
For the lending library, written for this chapter:

```markdown
## Questions sent

| Sent  | To             | About                                        | Answered |
|-------|----------------|----------------------------------------------|----------|
| day 3 | head librarian | Do fines exist, and how much per day?        | day 5    |
| day 4 | IT office      | May the system send email to members?        |          |

## Still open

| Line           | Waits on                         | Since |
|----------------|----------------------------------|-------|
| overdue-notice | IT office: email to members      | day 4 |
```

The first table says who was asked what, and when they answered.
The second says which queue line is blocked, on whom, and for how long, so "who owes me an answer" is one table and a reminder to that person is written from it.

Case A kept both tables: questions sent, with to whom, about what and answered when; and still open, with the line, what it waits on and since when.
Twenty questions to people outside the project were logged there, and two were still unanswered when it closed.
Its end-of-day status report and its schedule and risk estimate for the project manager say they were written from the queue and the pages, not from memory.
The queue gave the pace: about nine lines closed and about six new lines opened a day, so the open list shrank by about three a day.
That pace put a scope cut in front of the project manager in the middle of the project, as a decision for them to take.

## The person is the brain

The agent's answer reads as right even when it is wrong: fluent, formatted and sure of itself.
It may miss a message nobody put in the folder, read a draft as sent, or count a line whose page says it waits on someone.
So the person keeps three jobs, the same three the prologue gives the person for code.
They interpret: what the answer means for the client, the budget and the date.
They guide: they ask the next question, and point the agent to the file it missed.
They validate: they open the line, the table or the commit the answer rests on.

Ask the agent to name the file behind every answer.
An answer with a file to open is checked in a minute; an answer without one is a guess, however well it is written.

## The manager's session

A manager needs no code editor.
They open the host (chapter 11) in the project's root folder, the one with the rules file, and ask in plain words.
The host loads the rules file at the start of the session (chapter 2), and the rules file tells the agent to read the documents before acting, so the manager's session starts from the same documents as the developer's.

A question touches no code, and the host's plan mode (chapter 14) keeps a session from editing anything.
When the manager wants something changed, such as a new line in the queue, the agent writes it by conversation, as in any session (chapter 13), and a person reviews and commits it (chapter 15).

## What the team gains

One assistant for engineering and product alike: the same documents answer a developer's "where does this rule live" and a manager's "who owes us an answer", and nobody writes a status by hand.
On Case A, twenty questions to outside people were followed to their answers, the two left open were named at the close, and the status and the risk estimate came from a queue that closed about nine lines a day.

## Key points

* The documents, the queue, the pages and the git history already answer what is pending, what is in progress and how long each delivery took.
* The context folder holds what the code cannot say, in Markdown; it is committed when the repository stays with the team, and kept out when the repository is delivered or public.
* A work record with two tables, questions sent and still open, answers "who owes me an answer" and writes the reminder.
* The agent's answer reads as right even when it is wrong: ask for the file behind it, and interpret, guide and validate.
* A manager opens the host at the project's root and asks in plain words; the same rules file makes the agent read the documents first.

