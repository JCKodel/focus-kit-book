# 11. The queue and milestones

After this chapter you can read a queue, say what each mark means, and write a milestone paragraph a person can check.
You can also write a line as one sentence with its suffixes, order a milestone so that its order is its priority, write on a line which line must be done before it, `· after <slug>`, add, move or change a line by conversation, and turn a code change asked outside `/apply` into a line and a draft for its page.

## The problem

A team that keeps its plan in a tracker, its decisions in a chat and its progress in someone's head cannot answer "what is left, and what was done?" without a meeting.
An agent cannot answer it at all: it knows nothing at the start of a session, so what is not written where it reads does not exist for it.
The queue is one file, docs/06, that says what comes next, what is in flight and what was delivered, in an order a person and an agent both read.

## The line

docs/06 holds the project's milestones, each with a paragraph saying what is true when it closes, and under each one line per delivery, in order.
A line is the mark, the slug, one sentence of what the delivery gives, and its suffixes, such as `· after <slug>`, which names a line that must be done before it:

```
[ ] <slug>    <what it delivers, one sentence> · after <slug>
```

The slug is the delivery's name, in lowercase words joined by hyphens ([chapter 12](12-propose.md)).
It names the delivery's page, `work/<slug>.md`, and it is the argument of the commands, `/propose <slug>` and `/apply <slug>`, so the line, the page and the commands all point at the same delivery.

The kit asks for one sentence, and what happened goes on the page, because `/propose` reads the whole queue before it defines a delivery: every word on a line is read by every definition.
On Ninjobs I let the lines grow: its queue held 102 deliveries in 1,711 lines, 1,052 of them continuations of a line, decisions that belonged on the pages.
A line that grows into a paragraph is a decision in the wrong place, since the page is where the next session looks for it.

## The marks

A line has one of six marks, which says where its delivery stands:

* `[ ]` not yet defined: the delivery has a line and no page.
* `[~]` being defined: a conversation is writing its page.
* `[>]` defined: its page, `work/<slug>.md`, exists and waits to be built.
* `[*]` being built: a session is building it.
* `[x]` done: it was built, and its page moved to `work/done/` ([chapter 13](13-apply.md)).
* `[?]` waiting: it cannot go on until something else happens, and the line says what.

[Chapter 14](14-queue-states.md) shows who sets each mark and at what moment, when a line is free to start, and how a line waits and leaves `[?]`.

A line never leaves the queue; it changes mark and keeps its sentence.
So the queue is also the history of what was delivered, in the order it was planned, and what happened is on the page in `work/done/` behind each `[x]`, never added to the line.
On trunk the page waits uncommitted between the two commands, and `/apply` reads it from the working tree, so a fresh session finds it whether or not it was committed ([chapter 18](18-git-essentials.md)).

This is the lending library's first milestone some days into the work, written for this chapter:

````markdown
## Milestone 1: a librarian lends and takes back

When it closes, a librarian can register books, their copies and members,
lend a copy to a member for 21 days and record its return; a member with an
overdue book or a suspended membership is refused.

```
[x] skeleton      empty app and server, npm run verify, first screenshot
[x] catalog       the librarian registers books and their copies
[x] members       the librarian registers, suspends and reinstates members
[>] lend-book     the librarian lends a copy, and the rules may refuse it
[ ] return-book   the librarian records a return · after lend-book
[ ] m1-review     the milestone checked against its paragraph
```
````

Anyone can read the state from it: three deliveries done, `lend-book` has a page waiting for `/apply`, and two lines have no page yet, of which `return-book` comes after `lend-book`, since a copy is returned only after it was lent.

## Milestones

### The paragraph is a test

A milestone's paragraph says what is true when the milestone closes, in sentences a person can check against the running product.
It is a test, never a theme and never a list of the lines under it: "a librarian can lend a copy to a member for 21 days" can be checked, "loans" cannot.
Every sentence of the paragraph should have a line that makes it true, and every line should serve a sentence; a sentence with no line, or a line with no sentence, is a queue to fix before the work starts.

### Size and order

A milestone holds three to eight deliveries, then its review: the kit's rule for the first milestone and a good size for any.
The first ones are the skeleton the others stand on: the library's `skeleton` creates `npm run verify`, which every later delivery runs.
Then each line comes after the lines it needs: a librarian cannot lend a copy before the catalog holds copies and the members exist.

The order is the priority.
Asked which delivery matters most, you answer from the queue: the one higher in it; the next delivery is the first one free to start ([chapter 14](14-queue-states.md)).
There is no priority field and no label to keep in step with the order.

When you add a line and already know it needs another done first, you write that with it, at the end: a return needs a loan, so `return-book` ends with `· after lend-book`.
That is an order, not a wait: the line keeps its mark, `[ ]`, and is free to start once `lend-book` is `[x]`.
`lend-book` carries no `after`: the lines it needs, `catalog` and `members`, are already `[x]`.
A line written `[?]` instead would read as stuck when nothing has gone wrong; chapter 14 keeps `[?]` for a wait found on the way.

### The review, and its findings

A milestone is planned with its review as its last line, `<milestone>-review`, a delivery like the others, which takes the paragraph clause by clause ([chapter 15](15-closing-a-milestone.md)).
It fixes nothing: a person tests each clause by hand and launches the deep code review the project's docs/05 names, when it names one.
Each finding becomes a `[ ]` line in the same milestone, under the review line, and those lines get no second review.

## Changing the queue

No command owns the queue.
A new idea becomes a line by conversation, in any session: you tell the agent, and it writes the line in the milestone where it belongs, with a new slug and `[ ]`.

The code has one owner, `/apply`, the command that builds a delivery (chapter 13).
A change to it asked in any other session, however small, becomes a `[ ]` line: the agent writes the line, writes in a draft page what you said that the line cannot hold, says so, and the answer stops there, with no file of the app changed.
Asked in an ordinary session to show the due date on the loan screen as day/month/year, and told how it should look on a narrow screen and that the catalog keeps the ISO form, year-month-day, the agent adds this line to the milestone above, just above `m1-review`, a line written for this chapter:

```
[ ] due-date-format   the loan screen shows the due date as day/month/year
```

The narrow-screen rule and the catalog exception do not fit the line's one sentence, so they go into a draft `work/due-date-format.md`, and the answer stops there, naming `/propose due-date-format` for a fresh session, written as your host invokes it; a request the line holds whole gets no draft.
The line gets what every delivery gets, a page, a proof and the person's commit; an edit made on the spot would have skipped the line, the page and verify.
The draft is where the detail waits: `/propose due-date-format`, in a fresh session, starts from it and writes the page (chapter 12 shows `/propose`), so nothing you said in the first session is said twice.
Saying "define it now" changes nothing: the agent cannot run `/propose` on its own, since it is a command the host runs, and a page written without it starts without what `/propose` reads.
The answer is the same during `/propose`, which writes no code: a new line, and the page unchanged unless you ask for that change to be part of it.
An agent that edits the code anyway, to "just change the label", is asked for the line instead, and the edit is reverted before anything is committed.
The rule covers `/apply`'s own session too: a fix it finds outside its page becomes a line above it, and the delivery waits for that line (chapter 14).
Documents still change by conversation, in any session; the rule covers the code: the app's source, its tests, a migration, its configuration.

A milestone's paragraph or a line's description changes by conversation too, and the slug stays, since a page or a commit may already use it.
Moving a line up or down is changing its priority, and it happens the same way: you ask the agent to move it.
Lines also come from a milestone's review and, on an existing project, from its issues or roadmap.
You read the change before you commit it, as with every document, and nobody edits the queue by hand.

## What the team gains

The queue is the team's shared status board and its history in one file: what is next, what is in flight, what was done and in what order, readable by a manager without a tool and by an agent at the start of every session.
On Ninjobs it held 102 deliveries, done and not yet done alike, in one file.
On Case A, a client project on a low-code platform, Microsoft Power Apps with Copilot Studio, the status report and the risk estimate for the project manager were written from the queue and the pages, not from memory, and the queue gave the pace: about 9 lines closed and 6 opened a day.
[Chapter 17](17-project-as-assistant.md) tells the rest of Case A, and [chapter 20](20-team-tools.md) shows how its queue was mirrored on the board its project manager already used.

Three rules of the queue each prevent an error.
The order is the priority, written down: without it, a team looks for a way to rank its deliveries, and with it the queue already is the ranking.
Code changes only inside `/apply`: without that rule, an agent asked for a correction in an ordinary session edits the code directly, with no line in the queue, no page and no verify; with it, a change asked outside `/apply` costs one line, and it gets a page, a proof and the person's commit.
A line holds one sentence: when the detail of a request has nowhere to go but the line, the lines grow and every session reads them; with one sentence, the detail goes to the page, or to its draft until `/propose` writes it.
This book's own queue shows `· after` at work: in its milestone M12, seven lines end with `· after kit-2026-10-13`; each needs the update `kit-2026-10-13` done first, and none of them reads as stuck while it waits its turn.[^queue-m12]

## Key points

* docs/06 holds milestones, each with a paragraph, and one line per delivery under it: a mark, a slug, one sentence and its suffixes; what happened goes on the page.
* Six marks: `[ ]` not defined, `[~]` being defined, `[>]` the page exists, `[*]` being built, `[x]` done, `[?]` waiting; a line never leaves, so the queue is also the history.
* A milestone paragraph is a test a person can check against the product, never a theme.
* Three to eight deliveries, the skeleton first, each line after the lines it needs, and last the review, whose findings become lines under it in the same milestone.
* The order is the priority: the higher line matters more, and moving a line is changing its priority.
* A dependency known when a line is added is written with it, `· after <slug>`: an order, not a wait, so the line keeps `[ ]`.
* No command owns the queue: lines and paragraphs change by conversation, in any session, with the slug kept; code changes only inside `/apply`, and a change asked anywhere else becomes a line, with a draft page for what the line cannot hold, and `/propose` in a fresh session.

[^queue-m12]: J.C. Ködel, "One Page at a Time", the queue, `docs/06-Queue.md`, milestone M12, 2026-10, in the book's repository. <https://github.com/JCKodel/focus-kit-book/blob/main/docs/06-Queue.md>

