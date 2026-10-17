# 14. The queue while it happens

After this chapter you can read any queue line's state among focus-kit's six marks, say who sets each one and at what moment, name the next delivery, and say which lines can run at the same time.
You can also tell an order written with a line, `· after`, from a wait found on the way, `[?]`, mark a line that waits with its reason and the phase to resume, and take it out again; and lay the queue out as a kanban board that shows the work while it happens, and say where each mark is seen.

## The problem

On Case A, a client project on a low-code platform, the project manager followed the work on an Azure DevOps kanban board that a script filled from the queue, one way: `[ ]` went to To Do, `[>]` to Doing, `[x]` to Done.
Each mark changed when a command ended.
So a delivery stayed in To Do for as long as the author and the agent talked its page through, and reached Doing only once `/propose` had written it; and a card in Doing could be a page nobody was building yet.
Lines blocked on the client's answers had no mark of their own: five of them sat in Doing and read as work nobody had started.
The project added a fourth mark by hand, `[?]`, for a line waiting on a person.

Two errors, then: Doing came late, and waiting looked idle.
focus-kit answers both with six marks, each set at the moment the work changes.

## Six marks

| Mark | Means | Set by |
|---|---|---|
| `[ ]` | not defined | the conversation that adds the line |
| `[~]` | being defined | `/propose`, when it starts |
| `[>]` | defined: the page exists | `/propose`, when the page is complete |
| `[*]` | being built | `/apply`, when it starts |
| `[x]` | done: the page is in `work/done/` | `/apply`, with verify green |
| `[?]` | waiting | any session, in the three cases below |

This is the lending library's first milestone on one afternoon, written for this chapter, with every mark in use:

```
[x] catalog         the librarian registers books and their copies
[x] members         the librarian registers and suspends members
[*] lend-book       the librarian lends a copy, the rules may refuse
[>] search-catalog  a member searches the catalog
[~] reservations    a member reserves a copy that is on loan
[ ] my-loans        a member sees their loans · after lend-book
[?] due-reminder    a reminder · resume: propose · blocked: which provider?
[ ] m1-review       the milestone checked against its paragraph
```

Anyone reading it knows, without asking, that a session is building `lend-book`, that `search-catalog` has a page ready for `/apply`, that someone is talking `reservations` through right now, that `my-loans` comes after `lend-book`, and what `due-reminder` waits on and which command picks it up again.

## At the moment the work changes

A mark set when a command ends is wrong for as long as the command runs.
`/propose` can talk for an hour before it writes a page; a mark set only when the page is written reads that hour as "not defined", and the delivery shows up as started only once its definition is over.
So each mark is set when the work starts or stops: `[~]` when the conversation begins, `[>]` when the page is complete, `[*]` when the build begins, `[x]` when it ends green.
The queue then says what is happening now, not what last finished.

Where a mark is seen depends on where the session works (chapter 18).
On trunk, the mark changes in the queue of the folder where the session runs, at once, and reaches the history with the person's commit.
On a branch or a worktree, the `[~]` and `[*]` live on that branch, and the main branch sees them only once the delivery's merge lands, so the main branch's queue holds what has landed.
A board refreshed by the command that changed the mark shows it at once, whichever branch the work is on.

## The next line, and which run together

A line is free when it is not `[x]` and not `[?]`, and every line its `after` names is `[x]`.
In the milestone above, `lend-book`, `search-catalog` and `reservations` are free; `my-loans` is not, since `lend-book` is not `[x]` yet, and `due-reminder` waits.
The next delivery is the first free line no session holds: a session is building `lend-book` and another is defining `reservations`, so a new session's next delivery is `search-catalog`.
When `lend-book` becomes `[x]`, `my-loans` is free from that moment, with nothing to clear and no mark to change; the `· after` stays on the line as the record of the order.
A line with two orders, `· after lend-book, members`, is free only when both are `[x]`.

`/propose` and `/apply` do not start a line that is not free: run `/propose my-loans` while `lend-book` is `[*]`, and it says what the line waits on and stops.

Asked what can run at the same time, you answer from the queue: the free lines, and among them those that touch different files, judged from their pages and from docs/01, which says where each part of the code lives.
`search-catalog` and `reservations`, in `src/catalog/` and `src/reservations/`, can.
Two lines that both change `src/loans/`, as `lend-book` and a line to renew a loan would, cannot run together in one folder.
[Chapter 19](19-worktrees.md) shows how two sessions run in one folder, and when they need two.

## Waiting: `[?]`

A line waits in three cases:

* **The person says it is blocked.** The library has not bought its barcode scanners yet, so the librarian asks to hold `scan-copy`: `· resume: propose · blocked: no scanners yet`.
* **An answer was asked and not given.** `due-reminder` needs a text-message provider, the question went to the library's director, and nobody has answered: `· resume: propose · blocked: which provider?`.
* **Another line must be done first, found after work started.** In the middle of `/apply my-loans`, the build finds that `lend-book` sets the due date one day early at the end of a month; the fix becomes a `[ ]` line above it, `fix-due-date`, and `my-loans` waits: `· resume: apply · blocked: after fix-due-date`.

The reason goes at the end of the line, in words, `· blocked: <reason>`, or as the lines that must be `[x]` first, `· blocked: after <slug>, <slug>`.
Before it goes the phase to resume, `· resume: propose` for a line that was `[ ]` or `[~]`, `· resume: apply` for one that was `[>]` or `[*]`, so the session that takes the line up again knows which command it needs.
Any mark before `[x]` can become `[?]`: a line can wait before anyone defines it, while its page is being written, or halfway through its build.

`· after` and `· blocked: after` look alike and say different things.
`· after` is an order known when the line is written: `my-loans` needs loans to show, so it was added as `[ ] my-loans ... · after lend-book`, and it keeps `[ ]`.
`· blocked: after` is a wait found after work started, as `fix-due-date` was.
Writing `[?] my-loans ... · blocked: after lend-book` when the line is added is wrong: the line is queued, not stuck, and on a board it would carry a blocked tag that tells a manager something went wrong when nothing did.

A line leaves `[?]` when the reason is resolved.
The person says so; or the session that records the answer clears it, as when the director names the provider and the name becomes a line of docs/00; or `/apply` clears it when it marks `[x]` the last line an `after` names.
Both suffixes go, and the resume phase says where the line goes back.
`due-reminder`, with `resume: propose`, goes back to `[ ]`, and any draft of its page stays for `/propose` to finish.
A line with `resume: apply` goes back to `[>]`; if scope became undecided, it goes back to `[ ]` instead, and the session says what `/propose` must settle.

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
my-loans              search-catalog         members
m1-review             lend-book
```

`my-loans` sits in To Do with no tag: it waits its turn, not on anyone, and only `due-reminder` is tagged blocked.

`reservations` is in Doing from the first minute of its conversation, which is the error Case A's board had.
Chapter 20 shows how a script mirrors the queue to a team's own board, one way.

## What the team gains

A manager reads where every delivery stands, and what each waiting one waits on, without asking anyone and without a status meeting.
On Case A, five lines blocked on the client read as idle work, and every delivery reached Doing only after its definition was over, counted by the author on the project's queue and board; a mark set when the work changes, and one for waiting, answer both.

The queue also says which lines can run together: without that, a person who wants two sessions has to work it out alone before opening the second; the free lines and the files they touch answer it from the queue, without a meeting.

## Key points

* Six marks, `[ ]` not defined, `[~]` being defined, `[>]` defined, `[*]` being built, `[x]` done, `[?]` waiting, each changed when the work changes, not when a command ends: `/propose` sets `[~]` and `[>]`, `/apply` sets `[*]` and `[x]`, any session sets `[?]`.
* A line is free when it is not `[x]` nor `[?]` and every line its `after` names is `[x]`; the next delivery is the first free line no session holds, and free lines that touch different files can run at the same time.
* `· after` is an order written with the line, which keeps its mark; `[?]` with `· blocked: after` is a wait found after work started.
* A line waits when the person says so, when an answer was asked and not given, or when work already started finds another line must be done first, with the phase to resume and the reason at its end, `· resume: apply · blocked: after <slug>`; it leaves `[?]` by that phase when the reason is resolved, and until then `/propose` and `/apply` stop on it, as on a line not free.
* The queue is a kanban board, a column per mark; on three columns, Doing holds `[~]`, `[>]` and `[*]`, and a `[?]` card is tagged blocked where it was.

[^toyota-kanban]: Toyota Motor Corporation, "75 Years of Toyota", Part 2, Chapter 1, Section 4, Item 4, "Development and Deployment of the Toyota Production System", accessed 2026-10-05. <https://www.toyota-global.com/company/history_of_toyota/75years/text/entering_the_automotive_business/chapter1/section4/item4.html>
[^azure-kanban]: Microsoft Learn, "About Kanban boards", Azure Boards, accessed 2026-09-30. <https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-overview>
