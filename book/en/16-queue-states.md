# 16. The queue while it happens

After this chapter you can read any queue line's state among focus-kit's six marks, say who sets each one and at what moment, and mark a line that waits with its reason and take it out again.
You can also lay the queue out as a kanban board that shows the work while it happens, and say where each mark is seen.

## The problem

On Case A, a client project on a low-code platform, the project manager followed the work on an Azure DevOps kanban board that a script filled from the queue, one way: `[ ]` went to To Do, `[>]` to Doing, `[x]` to Done.
Each mark changed when a command ended.
So a delivery stayed in To Do for as long as the author and the agent talked its page through, and reached Doing only once `/propose` had written it; and a card in Doing could be a page nobody was building yet.
Lines blocked on the client's answers had no mark of their own: five of them sat in Doing and read as work nobody had started.
The project added a fourth mark by hand, `[?]`, for a line waiting on a person.

Two errors, then: Doing came late, and waiting looked idle.
focus-kit answers both since its version 2026.10.05, with six marks, each set at the moment the work changes.[^setup]

## Six marks

| Mark | Means | Set by |
|---|---|---|
| `[ ]` | not defined | the conversation that adds the line |
| `[~]` | being defined | `/propose`, when it starts |
| `[>]` | defined: the page exists | `/propose`, when the page is written |
| `[*]` | being built | `/apply`, when it starts |
| `[x]` | done: the page is in `work/done/` | `/apply`, with verify green |
| `[?]` | waiting | any session, in the three cases below |

This is the lending library's first milestone on one afternoon, written for this chapter, with every mark in use:

```
[x] catalog       the librarian registers books and their copies
[x] members       the librarian registers and suspends members
[*] lend-book     the librarian lends a copy, the rules may refuse
[>] return-book   the librarian records a return
[~] reservations  a member reserves a copy that is on loan
[?] my-loans      a member sees their loans · blocked: after lend-book
[?] due-reminder  a text before the due date · blocked: which provider?
[ ] m1-review     the milestone checked against its paragraph
```

Anyone reading it knows, without asking, that a session is building `lend-book`, that `return-book` has a page ready for `/apply`, that someone is talking `reservations` through right now, and what each waiting line waits on.

## At the moment the work changes

A mark set when a command ends is wrong for as long as the command runs.
`/propose` can talk for an hour before it writes a page; under three marks that hour reads as "not defined", and the delivery shows up as started only once its definition is over.
So each mark is set when the work starts or stops: `[~]` when the conversation begins, `[>]` when the page is written, `[*]` when the build begins, `[x]` when it ends green.
The queue then says what is happening now, not what last finished.

Where a mark is seen depends on where the session works (chapter 20).
On trunk, the mark changes in the queue of the folder where the session runs, at once, and reaches the history with the person's commit.
On a branch or a worktree, the `[~]` and `[*]` live on that branch, and the main branch sees them only once the delivery's merge lands, so the main branch's queue holds what has landed.
A board refreshed by the command that changed the mark shows it at once, whichever branch the work is on.

## Waiting: `[?]`

A line waits in three cases:

* **The person says it is blocked.** The library has not bought its barcode scanners yet, so the librarian asks to hold `scan-copy`: `· blocked: no scanners yet`.
* **An answer was asked and not given.** `due-reminder` needs a text-message provider, the question went to the library's director, and nobody has answered: `· blocked: which provider?`.
* **Another line must be done first.** In the middle of `/apply my-loans`, the build finds that `lend-book` sets the due date one day early at the end of a month; the fix becomes a `[ ]` line above it, and `my-loans` waits: `· blocked: after fix-due-date`.

The reason goes at the end of the line, in words, `· blocked: <reason>`, or as the lines that must be `[x]` first, `· blocked: after <slug>, <slug>`.
Any mark before `[x]` can become `[?]`: a line can wait before anyone defines it, while its page is being written, or halfway through its build.

A line leaves `[?]` when the reason is resolved.
The person says so; or the session that records the answer clears it, as when the provider's name arrives and becomes a line of docs/00; or `/apply` clears it when it marks `[x]` the last line an `after` names.
It goes back to `[>]` when its page exists and to `[ ]` when it has none, and the next command marks it again.

`/propose` and `/apply` both stop on a `[?]` line: they say what it waits on, and go on only when the person says it is resolved.
A command that ran past the reason would build on an answer nobody gave.

## The queue as a kanban board

A kanban board shows work as cards in columns, one column per state, and a card moves from column to column as its state changes.
Toyota's factories used kanban, cards to say which parts were needed, where and when, and adopted them at every plant in 1963.[^toyota-kanban]
Software teams took the idea as a board where, in Microsoft's words for Azure DevOps, "*team members drag cards across columns to update status*".[^azure-kanban]

Read as a board, the queue has a column per mark, six of them, and each mark change moves a card.
A team whose board has three columns folds them: `[ ]` to To Do; `[~]`, `[>]` and `[*]` to Doing; `[x]` to Done.
A `[?]` card stays in the column it was in, tagged blocked, with its reason, so waiting never looks idle.
The milestone above, on a three-column board:

```
TO DO                 DOING                  DONE
due-reminder BLOCKED  reservations           catalog
m1-review             return-book            members
                      lend-book
                      my-loans BLOCKED
```

`reservations` is in Doing from the first minute of its conversation, which is the error Case A's board had.
Chapter 22 shows how a script mirrors the queue to a team's own board, one way.

## What the team gains

A manager reads where every delivery stands, and what each waiting one waits on, without asking anyone and without a status meeting.
On Case A, five lines blocked on the client read as idle work, and every delivery reached Doing only after its definition was over, counted by the author on the project's queue and board; a mark set when the work changes, and one for waiting, answer both.

## Key points

* Six marks: `[ ]` not defined, `[~]` being defined, `[>]` defined, `[*]` being built, `[x]` done, `[?]` waiting.
* A mark changes when the work changes, not when a command ends: `/propose` sets `[~]` and `[>]`, `/apply` sets `[*]` and `[x]`, any session sets `[?]`.
* A line waits when the person says so, when an answer was asked and not given, or when another line must be done first; the reason goes at the end, `· blocked: <reason>` or `· blocked: after <slug>`.
* A line leaves `[?]` when the reason is resolved, back to `[>]` with a page or `[ ]` without; `/propose` and `/apply` stop on a `[?]` line until the person says it is resolved.
* The queue is a kanban board, a column per mark; on three columns, Doing holds `[~]`, `[>]` and `[*]`, and a `[?]` card is tagged blocked where it was.

[^setup]: J.C. Ködel, focus-kit, `SETUP.md`, version 2026.10.05, the process document's §4. <https://github.com/JCKodel/focus-kit/blob/main/SETUP.md>
[^toyota-kanban]: Toyota Motor Corporation, "75 Years of Toyota", Part 2, Chapter 1, Section 4, Item 4, "Development and Deployment of the Toyota Production System", accessed 2026-10-05. <https://www.toyota-global.com/company/history_of_toyota/75years/text/entering_the_automotive_business/chapter1/section4/item4.html>
[^azure-kanban]: Microsoft Learn, "About Kanban boards", Azure Boards, accessed 2026-09-30. <https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-overview>
