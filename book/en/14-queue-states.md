# 14. The queue while it happens

After this chapter you can read any queue line's state among focus-kit's six marks, say who sets each one and at what moment, name the next delivery, and say which lines can run at the same time.
You can also tell an order written with a line, `· after`, from a wait found on the way, `[?]`, mark a line that waits with its reason and the phase to resume, and take it out again; and lay the queue out as a kanban board that shows the work while it happens, and say where each mark is seen.
And you can resume a line whose session ended, and record a delivery the person cancels so that it never reads as built.

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
| `[>]` | completely defined: the page is ready for `/apply` | `/propose`, when the page is complete |
| `[*]` | being built | `/apply`, when it starts |
| `[x]` | done: the page is in `work/done/`; with `· dropped:`, cancelled | `/apply`, with verify green; the person, when cancelling |
| `[?]` | waiting | any session, in the four cases below |

`· dropped:` is a suffix on `[x]`, not a seventh mark: a cancelled delivery is closed like a built one, and the suffix says nothing was delivered (below).

A page that exists is not yet `[>]`: a draft saved for a `[ ]` line is a file in `work/` too ([chapter 11](11-queue-and-milestones.md)).
The page is complete when every section is filled or says it does not apply and no scope question is open; only then does `/propose` mark the line `[>]`, and `/apply` builds it once every line its `after` names is `[x]`.
While a scope question is still being talked through, the line stays `[~]`; a question asked of someone who has not answered makes it wait, `[?]` (below).

This is the lending library's first milestone on one afternoon, written for this chapter, with every mark in use:

```
[x] catalog         the librarian registers books and their copies
[x] members         the librarian registers and suspends members
[*] lend-book       the librarian lends a copy, or a rule refuses
[ ] return-book     records a return · after lend-book
[>] search-catalog  a member searches the catalog
[~] reservations    a member reserves a copy that is on loan
[ ] my-loans        a member sees their loans · after lend-book
[?] due-reminder    a reminder · resume: propose · blocked: what provider?
[ ] m1-review       the milestone checked against its paragraph
```

Anyone reading it knows, without asking, that a session is building `lend-book`, that `search-catalog` is completely defined and ready for `/apply`, that someone is talking `reservations` through right now, that `return-book` and `my-loans` come after `lend-book`, and what `due-reminder` waits on and which command picks it up again.

## At the moment the work changes

A mark set when a command ends is wrong for as long as the command runs.
`/propose` can talk for an hour before it writes a page; a mark set only when the page is written reads that hour as "not defined", and the delivery shows up as started only once its definition is over.
So each mark is set when the work starts or stops: `[~]` when the conversation begins, `[>]` when the page is complete, `[*]` when the build begins, `[x]` when it ends green.
The queue then says what is happening now, not what last finished.

Where a mark is seen depends on where the session works (chapter 18).
On trunk, the mark changes in the queue of the folder where the session runs, a board that reads that queue sees it at once, and it reaches the history with the person's commit.
With a branch or a worktree per delivery, the mark lives on the delivery's branch, pushed when `/propose` creates it, and the main branch shows the line as it was until the merge.
After `git fetch`, a line whose branch exists is taken, whatever the main branch shows: the branch is the claim of the line, on the remote from the moment the work starts, before any mark on it is pushed, so the main branch's queue changes only through merges.
So whoever reads the queue, a board or a session picking free lines or resolving an `after`, takes each slug's line from its branch, local or remote, adds the lines only a branch has, and reconciles them by slug, each line at its latest state, never one branch's whole file.
The marks change at once for the same reason either way, a board people pull work from: on trunk the board reads the one queue, and with a branch or a worktree per delivery it reads each slug's line where that line lives.
Where the line lives decides how soon a reader sees it: a worktree's file shows the mark the moment it changes, a branch once the mark is committed on it, a remote branch once that commit is pushed.
A project's own one-way mirror, refreshed by the commands when a mark changes, shows the mark at once, and with a branch or a worktree per delivery it pushes the queue read the same way, so each refresh carries every delivery's mark as far as it can see it, not its own branch's copy.

## The next line, and which run together

A line is free when it is not `[x]` and not `[?]`, and every line its `after` names is `[x]` (an `[x]` that was cancelled asks the person first, below).
In the milestone above, `lend-book`, `search-catalog` and `reservations` are free; `return-book` and `my-loans` are not, since `lend-book` is not `[x]` yet, and `due-reminder` waits.
The next delivery is the first free line no session holds: a session is building `lend-book` and another is defining `reservations`, so a new session's next delivery is `search-catalog`.
With a branch or a worktree per delivery, the session runs `git fetch` first, counts a line whose branch exists as taken, and judges free lines and `after` from each slug's line read as the section above says, so `return-book`'s `after` reads `lend-book`'s mark on `lend-book`'s branch.
From the main branch's copy alone, `lend-book` would read `[ ]`, free and held by no one, and the answer would name a delivery another session is building; `lend-book`'s branch on the remote says it is taken even before any of its marks is pushed.
When `lend-book` becomes `[x]`, `return-book` and `my-loans` are free from that moment, with nothing to clear and no mark to change; the `· after` stays on the line as the record of the order.
A line with two orders, `· after lend-book, members`, is free only when both are `[x]`.

A milestone's end sets priority, not whether a line is free.
Chapter 11's `due-date-format` sits under milestone 2, below `m1-review`, and names no `after`: it is free, and does not wait for `m1-review`.
But the next delivery is the first free line counting down the queue, so a session asked for the next one reaches it only once milestone 1 holds no free line.
A line added later goes in the milestone whose paragraph needs it, never higher in the queue because it is new: its place is its priority, and the lines already there keep their order and their `after`.

`/propose` and `/apply` do not start a line that is not free: run `/propose my-loans` while `lend-book` is `[*]`, and it says what the line waits on and stops.

Asked what can run at the same time, you answer from the queue: the free lines, and among them those that touch different files, judged from their pages and from docs/01, which says where each part of the code lives.
`search-catalog` and `reservations`, in `src/features/catalog/` and `src/features/reservations/`, can.
Two lines that both change `src/features/loans/`, as `lend-book` and a line to renew a loan would, cannot run together in one folder.
[Chapter 19](19-worktrees.md) shows how two sessions run in one folder, and when they need two.

## Waiting: `[?]`

A line waits in four cases:

* **The person says it is blocked.** The library has not bought its barcode scanners yet, so the librarian asks to hold `scan-copy`: `· resume: propose · blocked: no scanners yet`.
* **An answer was asked and not given.** `due-reminder` needs a text-message provider, the question went to the library's director, and nobody has answered: `· resume: propose · blocked: what provider?`.
* **Another line must be done first, found after work started.** In the middle of `/apply my-loans`, the build finds that `lend-book` sets the due date one day early at the end of a month; the fix becomes a `[ ]` line above it, `fix-due-date`, and `my-loans` waits: `· resume: apply · blocked: after fix-due-date`.
* **A milestone review's code reading missed part of its range.** The review that closes a milestone reads, on the person's word, every change since the milestone's base, split into areas with one reader each that lists the paths it read ([chapter 15](15-closing-a-milestone.md)), and a reader that read part of its area reports the same way as one that read it all, so when, in the middle of `/apply m1-review`, the review's readers list no path of `src/features/catalog/`, the line waits with what was read as its reason: `· resume: apply · blocked: read all but catalog/`.

The reason goes at the end of the line, in words, `· blocked: <reason>`, or as the lines that must be `[x]` first, `· blocked: after <slug>, <slug>`.
Before it goes the phase to resume, `· resume: propose` for a line that was `[ ]` or `[~]`, `· resume: apply` for one that was `[>]` or `[*]`, so the session that takes the line up again knows which command it needs.
Any mark before `[x]` can become `[?]`: a line can wait before anyone defines it, while its page is being written, or halfway through its build.

`· after` and `· blocked: after` look alike and say different things.
`· after` is an order known when the line is written: `my-loans` needs loans to show, so it was added as `[ ] my-loans ... · after lend-book`, and it keeps `[ ]`.
`· blocked: after` is a wait found after work started, as `fix-due-date` was.
Writing `[?] my-loans ... · blocked: after lend-book` when the line is added is wrong: the line is queued, not stuck, and on a board it would carry a blocked tag that tells a manager something went wrong when nothing did.

A line leaves `[?]` when the reason is resolved.
The person says so; or the session that records the answer clears it, as when the director names the provider and the name becomes a line of docs/00; or `/apply` clears it when it marks `[x]` the last line an `after` names.
Both suffixes go, `resume` and `blocked`, and the resume phase says where the line goes back.
`due-reminder`, with `resume: propose`, goes back to `[ ]`, and any draft of its page stays for `/propose` to finish: a draft is a page begun, not a definition complete.
A line with `resume: apply` goes back to `[>]`.

`/propose` and `/apply` both stop on a `[?]` line: they say what it waits on, and go on only once the reason is resolved, in one of those three ways.
A command that ran past the reason would build on an answer nobody gave.

## A session that ended, a delivery cancelled

A session can end without anyone blocking its line: the host closes, the connection is lost, the plan's limit is reached.
Its line keeps its mark.
`reservations` stays `[~]` after the conversation that was defining it ends; nothing waits on anyone, so it does not become `[?]`.
The mark alone cannot tell that the session ended: a `[~]` or `[*]` line is held by a session, and that session may be talking in another folder or on another machine right now.
So a new session does not take the line over because it sees the mark; the person, who knows the session ended, says so and runs `/propose reservations` again.
The command then inspects the page, the working folder and the index before editing, and goes on from what the earlier conversation wrote.
`lend-book`, `[*]` when its build lost the connection, resumes the same way with `/apply lend-book`: the files already built and what is already in the index stay the delivery's, and the line stays `[*]`, never put back to `[>]` or `[ ]` as if nothing had been done.

A delivery the person cancels, because the work proved it impossible, because it was refused, or because nobody wants it any more, stays in the queue too.
It ends `[x]` with the reason at the end of the line, `· dropped: <reason>`, and its page goes to `work/done/` like any other, saying what was built and what was undone, or that nothing was built.
The library wanted the librarian to print a member's card from the browser, and the card printer turned out to have no driver the browser could reach; the librarian cancels the line, and `reprint-card`, added after it, waits on it, in two lines written for this chapter:

```
[x] print-card      prints a member card · dropped: no printer driver
[ ] reprint-card    reprints a lost card · after print-card
```

`[x]` alone says the delivery's promise holds, with verify green; `[x]` with `· dropped:` says the decision is taken and the promise does not exist.
The person sets it, not `/apply`, because cancelling is a decision about scope, and the line stays so that nobody later asks whether `print-card` was forgotten.
By the free rule alone, `reprint-card` is free once `print-card` is `[x]`, and that is the trap: the `[x]` it names is a decision, not a card printer that works.
So a line whose `after` names a cancelled delivery is the person's to re-decide: drop it too, as `reprint-card` would be, or rewrite it on what does exist.

## The queue as a kanban board

A kanban board shows work as cards in columns, one column per state, and a card moves from column to column as its state changes.
Toyota's factories used kanban, cards to say which parts were needed, where and when, and adopted them at every plant in 1963.[^toyota-kanban]
Software teams took the idea as a board where, in Microsoft's words for Azure DevOps, "*team members drag cards across columns to update status*".[^azure-kanban]

Read as a board, the queue has a column per mark, six of them, and each mark change moves a card.
A `[?]` card sits in Waiting with its reason, and when the reason is resolved it moves to the column of the mark it returns to, `[ ]` or `[>]`.
A team whose board has three columns folds them: `[ ]` to To Do; `[~]`, `[>]` and `[*]` to Doing; `[x]` to Done.
On this chapter's three-column board, an illustration and not a rule of the kit nor a feature of any board, a `[?]` card goes by its resume phase, tagged blocked with its reason, so waiting never looks idle: `resume: propose` in To Do, `resume: apply` in Doing.
The line says where the card goes, so the board keeps no memory of the column a card was in.
The milestone above, on a three-column board:

```
TO DO                 DOING                  DONE
due-reminder BLOCKED  reservations           catalog
return-book           search-catalog         members
my-loans              lend-book
m1-review
```

`return-book` and `my-loans` sit in To Do with no tag: they wait their turn, not on anyone, and only `due-reminder` is tagged blocked, in To Do because its line says `resume: propose`.

`reservations` is in Doing from the first minute of its conversation, which is the error Case A's board had.

If `reservations` were blocked in the middle of its definition, its `resume: propose` would take it from Doing to To Do, tagged blocked; resolved, it stays in To Do as `[ ]`, with its draft kept and no tag.
`my-loans`, waiting on `fix-due-date` in the middle of its build, would stay in Doing by its `resume: apply`, tagged blocked; resolved, it stays in Doing as `[>]`, not as a `[*]` that no session is building.
Either way, resolving the reason removes both suffixes and the tag with them.

Chapter 20 shows how a script mirrors the queue to a team's own board, one way.

A board can also read the queue itself, with nothing to mirror.
It reads docs/06 and the pages in `work/` by slug, on trunk from the folder's own files and with a branch or a worktree per delivery from each slug's own branch, local or remote, and moves its cards as each mark becomes visible to it while the agent works.

## What the team gains

A manager reads where every delivery stands, and what each waiting one waits on, without asking anyone and without a status meeting.
On Case A, five lines blocked on the client read as idle work, and every delivery reached Doing only after its definition was over, counted by the author on the project's queue and board; a mark set when the work changes, and one for waiting, answer both.
A request that proved impossible there was closed in the queue with its reason instead of left in silence ([chapter 23](23-adoption.md)), and the kit writes such a closure as `[x]` with `· dropped:`.

The queue also says which lines can run together: without that, a person who wants two sessions has to work it out alone before opening the second; the free lines and the files they touch answer it from the queue, without a meeting.

## Key points

* Six marks, `[ ]` not defined, `[~]` being defined, `[>]` completely defined and ready for `/apply`, `[*]` being built, `[x]` done, `[?]` waiting, each changed when the work changes, not when a command ends: `/propose` sets `[~]` and `[>]`, `/apply` sets `[*]` and `[x]`, the person sets `[x]` with `· dropped: <reason>` when cancelling, any session sets `[?]`.
* A line is free when it is not `[x]` nor `[?]` and every line its `after` names is `[x]`, and when one is cancelled the person re-decides the line; with a branch or a worktree per delivery, a line whose branch exists after `git fetch` is taken, whatever the main branch shows; the next delivery is the first free line no session holds, and free lines that touch different files can run at the same time.
* A line whose session ended keeps its mark, and its command resumes it on the person's word, inspecting the page, the folder and the index first; a cancelled delivery ends `[x] · dropped: <reason>`, its page in `work/done/` saying what was built and undone.
* `· after` is an order written with the line, which keeps its mark; `[?]` with `· blocked: after` is a wait found after work started; a line waits when the person says so, when an answer was asked and not given, when work already started finds another line must be done first, or when a milestone review's code reading missed part of its range, with the phase to resume and the reason at its end, `· resume: apply · blocked: after <slug>`; when the reason is resolved, both suffixes go and it returns as that phase says, `resume: propose` to `[ ]` with any draft kept, `resume: apply` to `[>]`, and until then `/propose` and `/apply` stop on it, as on a line not free.
* The queue is a kanban board, a column per mark, a `[?]` card in Waiting until it returns to `[ ]` or `[>]`; on this chapter's three columns, Doing holds `[~]`, `[>]` and `[*]`, and a `[?]` card is tagged blocked in the column its resume phase names, To Do for `propose`, Doing for `apply`; a board that reads the queue sees a mark at once on trunk, and with a branch or a worktree per delivery from each slug's own branch, local or remote, pushed when `/propose` creates it, since the main branch shows the line as it was until the merge.

[^toyota-kanban]: Toyota Motor Corporation, "75 Years of Toyota", Part 2, Chapter 1, Section 4, Item 4, "Development and Deployment of the Toyota Production System", accessed 2026-10-05. <https://www.toyota-global.com/company/history_of_toyota/75years/text/entering_the_automotive_business/chapter1/section4/item4.html>
[^azure-kanban]: Microsoft Learn, "About Kanban boards", Azure Boards, accessed 2026-09-30. <https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-overview>
