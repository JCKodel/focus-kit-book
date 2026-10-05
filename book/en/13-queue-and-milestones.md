# 13. The queue and milestones

After this chapter you can read a queue, say what each mark means, and write a milestone paragraph a person can check.
You can also size and order a milestone, and add or change a line by conversation.

## The problem

A team that keeps its plan in a tracker, its decisions in a chat and its progress in someone's head cannot answer "what is left, and what was done?" without a meeting.
An agent cannot answer it at all: it knows nothing at the start of a session, so what is not written where it reads does not exist for it.
The queue is one file, docs/06, that says what comes next, what is in flight and what was delivered, in an order a person and an agent both read.

## The line

docs/06 holds the project's milestones, each with a paragraph saying what is true when it closes, and under each one line per delivery, in order.
A line has three parts, a mark, a slug and what the delivery gives, in one line:

```
[ ] <slug>    <what it delivers, one line>
```

The slug is the delivery's name, in lowercase words joined by hyphens ([chapter 14](14-propose.md)).
It names the delivery's page, `work/<slug>.md`, and it is the argument of the commands, `/propose <slug>` and `/apply <slug>`, so the line, the page and the commands all point at the same delivery.

The kit asks for one line, and the reasoning goes on the page.
On Ninjobs I let the lines grow: its queue held 102 deliveries in 1,711 lines, 1,052 of them continuations of a line, decisions that belonged on the pages.
A line that grows into a paragraph is a decision in the wrong place, since the page is where the next session looks for it.

## The marks

A line has one of six marks, which says where its delivery stands:

* `[ ]` not yet defined: the delivery has a line and no page.
* `[~]` being defined: a conversation is writing its page.
* `[>]` defined: its page, `work/<slug>.md`, exists and waits to be built.
* `[*]` being built: a session is building it.
* `[x]` done: it was built, and its page moved to `work/done/` ([chapter 15](15-apply.md)).
* `[?]` waiting: it cannot go on until something else happens, and the line says what.

[Chapter 16](16-queue-states.md) shows who sets each mark and at what moment, and how a line waits and leaves `[?]`.

A line never leaves the queue; it changes mark.
So the queue is also the history of what was delivered, in the order it was planned, and the page in `work/done/` behind each `[x]` says what happened.
On trunk the page waits uncommitted between the two commands, and `/apply` reads it from the working tree, so a fresh session finds it whether or not it was committed ([chapter 20](20-git-essentials.md)).

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
[ ] return-book   the librarian records a return, and the copy is free again
[ ] m1-review     the milestone checked against its paragraph
```
````

Anyone can read the state from it: three deliveries done, `lend-book` has a page waiting for `/apply`, and two lines have no page yet.

## Milestones

### The paragraph is a test

A milestone's paragraph says what is true when the milestone closes, in sentences a person can check against the running product.
It is a test, never a theme and never a list of the lines under it: "a librarian can lend a copy to a member for 21 days" can be checked, "loans" cannot.
Every sentence of the paragraph should have a line that makes it true, and every line should serve a sentence; a sentence with no line, or a line with no sentence, is a queue to fix before the work starts.

### Size and order

A milestone holds three to eight deliveries, then its review: the kit's rule for the first milestone and a good size for any.
The first ones are the skeleton the others stand on: the library's `skeleton` creates `npm run verify`, which every later delivery runs.
Then each line comes after the lines it needs: a librarian cannot lend a copy before the catalog holds copies and the members exist.

### The review, and its findings

A milestone is planned with its review as its last line, `<milestone>-review`, a delivery like the others, which takes the paragraph clause by clause ([chapter 17](17-closing-a-milestone.md)).
It reviews no code and fixes nothing: a person tests each clause by hand.
Each finding becomes a `[ ]` line in the same milestone, under the review line, and those lines get no second review.

## Changing the queue

No command owns the queue.
A new idea becomes a line by conversation, in any session: you tell the agent, and it writes the line in the milestone where it belongs, with a new slug and `[ ]`.
A milestone's paragraph or a line's description changes the same way, and the slug stays, since a page or a commit may already use it.
Lines also come from a milestone's review and, on an existing project, from its issues or roadmap.
You read the change before you commit it, as with every document, and nobody edits the queue by hand.

## What the team gains

The queue is the team's shared status board and its history in one file: what is next, what is in flight, what was done and in what order, readable by a manager without a tool and by an agent at the start of every session.
On Ninjobs it held 102 deliveries, done and not yet done alike, in one file.
On Case A, a client project on a low-code platform, Microsoft Power Apps with Copilot Studio, the status report and the risk estimate for the project manager were written from the queue and the pages, not from memory, and the queue gave the pace: about 9 lines closed and 6 opened a day.
[Chapter 19](19-project-as-assistant.md) tells the rest of Case A, and [chapter 22](22-team-tools.md) shows how its queue was mirrored on the board its project manager already used.

## Key points

* docs/06 holds milestones, each with a paragraph, and one line per delivery under it: a mark, a slug and what it delivers, in one line; the reasoning goes on the page.
* Six marks: `[ ]` not defined, `[~]` being defined, `[>]` the page exists, `[*]` being built, `[x]` done, `[?]` waiting; a line never leaves, so the queue is also the history.
* A milestone paragraph is a test a person can check against the product, never a theme.
* Three to eight deliveries, the skeleton first, each line after the lines it needs, and last the review, whose findings become lines under it in the same milestone.
* No command owns the queue: lines and paragraphs change by conversation, in any session, with the slug kept.

