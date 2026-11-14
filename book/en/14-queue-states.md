# 14. The queue while it happens

After this chapter you can read any queue line's state among focus-kit's six marks, say who sets each one, at what moment, and how, one byte through the kit's mark script while every other edit of the queue changes only its own lines, since a program that writes the whole queue can empty it, and why the script refuses a second start of one line, name the next delivery, even past a milestone that waits, list every open line of a queue with one search, say which lines can run at the same time from the queue tree the kit's script draws, and say why a build stops on files another build is changing.
You can also write that a line needs another first, `· after`, whenever the need is found, read for each command and never a wait, mark a line that waits, `[?]`, in its three cases, with its reason and the phase to resume, and take it out again; tell a line from a finding by its `· from <slug>`, say where it goes in its milestone and why every other finding is a note and not a line, and read the `findings:` line the queue script prints; and lay the queue out as a kanban board that shows the work while it happens, and say where each mark is seen.
And you can resume a line whose session ended, and record a delivery the person cancels so that it never reads as built nor keeps the milestone's review waiting.

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
| `[?]` | waiting, never on another line | any session, in the three cases below |

`· dropped:` is a suffix on `[x]`, not a seventh mark: a cancelled delivery is closed like a built one, and the suffix says nothing was delivered (below).

A page that exists is not yet `[>]`: a draft saved for a `[ ]` line is a file in `work/` too ([chapter 11](11-queue-and-milestones.md)).
The page is complete when every section is filled or says it does not apply and no scope question is open; only then does `/propose` mark the line `[>]`, and `/apply` builds it once every line its `after` names is integrated (below).
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
[ ] m1-review       the milestone against its paragraph · after all
```

Anyone reading it knows, without asking, that a session is building `lend-book`, that `search-catalog` is completely defined and ready for `/apply`, that someone is talking `reservations` through right now, that `return-book` and `my-loans` come after `lend-book`, and what `due-reminder` waits on and which command picks it up again.

> **Note.** To see every open line of a queue at once, search docs/06 for the regular expression `^\[[^x]\]`, a pattern that a search matches against each line.
> `^` is the start of a line, `\[` and `\]` are the brackets themselves, and `[^x]` is any one character but `x`, so it finds every line that starts with a mark other than `[x]`: not defined, being defined, defined, being built and waiting; a cancelled line is `[x]` with `· dropped:`, and is left out like a done one.
> Turn on regular expressions in an editor's search, or run `grep -nE '^\[[^x]\]' docs/06-Queue.md` in a terminal: `grep`, on every Unix-like system and in the shell Git for Windows installs, prints the lines of a file that match a pattern, and `-n` adds each line's number.
> On the nine lines above it finds seven, all but `catalog` and `members`; on 2026-11-14 this book's own queue held 515 lines, 509 of them `[x]`, and the search showed the other six.
> The search reads no `after` and only the copy of the file in front of you, so what may run now is still the queue tree's answer (below).

## At the moment the work changes

A mark set when a command ends is wrong for as long as the command runs.
`/propose` can talk for an hour before it writes a page; a mark set only when the page is written reads that hour as "not defined", and the delivery shows up as started only once its definition is over.
So each mark is set when the work starts or stops: `[~]` when the conversation begins, `[>]` when the page is complete, `[*]` when the build begins, `[x]` when it ends green.
The queue then says what is happening now, not what last finished.

Where a mark is seen depends on where the session works (chapter 18).
On trunk, the mark changes in the queue of the folder where the session runs, a board that reads that queue sees it at once, and it reaches the history with the person's commit.
With a branch or a worktree per delivery, the mark lives on the delivery's branch, pushed when `/propose` creates it, and the main branch shows the line as it was until the merge.
After `git fetch`, a line whose branch exists is taken, whatever the main branch shows: the branch is the claim of the line, on the remote from the moment the work starts, before any mark on it is pushed, so the main branch's queue changes only through merges.
So whoever reads the queue, a board or a session picking free lines or resolving an `after`, runs `git fetch` and takes each slug's line from its branch on origin, which holds the current copy until the merge, the main branch's after it, and adds the lines only a branch has, never one branch's whole file.
The marks change at once for the same reason either way, a board people pull work from: on trunk the board reads the one queue, and with a branch or a worktree per delivery it reads each slug's line where that line lives.
Where the line lives decides how soon a reader sees it: a reader sees the mark once its commit is pushed to the branch on origin and fetched.
A project's own one-way mirror, refreshed by the commands when a mark changes, shows the mark at once on trunk; with a branch or a worktree per delivery it pushes the queue read the same way, so it shows a mark at the first refresh after the mark is pushed to the delivery's branch, and each delivery's refresh carries every other delivery's mark pushed so far, never one branch's copy of the file.

## How a mark changes

The queue is one file that every session edits, each its own line, often at the same time, while a board reads it.
An agent that changes its mark with a small program of its own, one that reads docs/06, replaces the mark and writes the file back, can lose the whole queue: a program that opens the file for writing before it reads it empties the file first.
On 2026-10-18 in one project and on 2026-10-26 in another, a subagent marking its line ran such a one-line program: the write emptied docs/06 before the read, and the queue was left at zero bytes.
Both subagents were staging their own hunk of a queue that other sessions also edit, a hunk being the piece of a file that git stages as one change.

So a mark changes one way only: the agent runs the kit's mark script, `propose/scripts/mark.sh`, through git's own shell, as the claim script of chapter 13 is run, `git -c "alias.fm=!sh .agents/skills/propose/scripts/mark.sh" fm <slug> "<mark>"`.
The six marks differ only in the character between the brackets, so a mark is one byte.
The script finds the slug's one line, changes that byte, writes the result to a file beside the queue and renames it over the queue, so the queue itself is never opened for writing; and it refuses before it writes the queue unless the result keeps the queue's size and differs from it in at most that byte.
With `stage` at the end, it changes the same line in the index and nothing else there, so another session's staged lines stay as they were: that is how `/apply` stages its `[x]`, even when another session changed the line next to its own.

Two sessions that start one line both read it free until one of them marks it, so a session that reads the line `[>]` and then marks it cannot tell whether another read it `[>]` a moment before.
On 2026-10-26, in one project, `/apply` of one slug was typed in two sessions six seconds apart, in one folder on trunk; the second read the line `[>]`, marked it `[*]` and built it too.
So the script checks the line where it sets the mark, against what the line holds at that moment: it sets a `[~]` only on a `[ ]` line and a `[*]` only on a `[>]` one, and on any other line it refuses before it writes anything, saying that a `[~]` or `[*]` is another session's, resumed only on the person's word.
The other four marks are set without that check.

Every other edit to docs/06 is the host's own file edit, the tool the agent changes a file's lines with, on the lines it changes, never a program that writes the whole file: a line added, a suffix such as `· blocked:` or `· dropped:`, a line moved to change its priority.
So putting a line on hold, below, is two edits: `[?]` by the script, its reason and its phase to resume by the file edit.

## The next line, and which run together

A line is free for a command when it is not `[x]` and not `[?]` and its `after` lets that command start, and `after` is read for each command.
`/propose` starts when every line its `after` names is `[>]` or beyond, because the definition needs their pages; `/apply` starts when every one is integrated, because the build needs their code.
Integrated is `[x]` on trunk; with a branch or a worktree per delivery it is the delivery merged into the main branch, and an `[x]` on a branch not yet merged is built, awaiting integration (an `[x]` that was cancelled asks the person first, below).
A milestone's review line is written `· after all`: every line above it in its milestone but the cancelled ones, so its `/propose` starts when they are all defined and its `/apply` when they are all integrated.

In the milestone above, `return-book` and `my-loans` are free for `/propose` while `lend-book` is `[*]`: their pages can take what `lend-book`'s page says.
Their `/apply` waits until `lend-book` is integrated, since a return needs the code of the loan.
`search-catalog` is free for `/apply`; `m1-review` waits, with four lines above it not yet defined, and `due-reminder` waits on its reason.
The next delivery is the first free line no session holds, counting down the queue, whichever command it takes: a session is building `lend-book` and another is defining `reservations`, and the first free line down the queue that neither holds is `return-book`, free for `/propose`, so a new session's next delivery is `/propose return-book`.
With a branch or a worktree per delivery, the session runs `git fetch` first, counts a line whose branch exists as taken, and judges free lines and `after` from each slug's line read as the section above says, so `return-book`'s `after` reads `lend-book`'s mark on `lend-book`'s branch, and `return-book`'s build waits for `lend-book`'s merge, not for the `[x]` on its branch.
From the main branch's copy alone, `lend-book` would read `[ ]`, free and held by no one, and the answer would name a delivery another session is building; `lend-book`'s branch on the remote says it is taken even before any of its marks is pushed.
When `lend-book` is integrated, the builds of `return-book` and `my-loans` are free from that moment, with nothing to clear and no mark to change; the `· after` stays on the line as the record of the order.
A line with two orders, `· after lend-book, members`, is free for a command only when both let it start.

A milestone's end sets priority, not whether a line is free.
Chapter 11's `due-date-format` sits under milestone 2, below `m1-review`, and names no `after`: it is free, and does not wait for `m1-review`.
But the next delivery is the first free line counting down the queue, so a session asked for the next one reaches it only once milestone 1 holds no free line.
A line added later goes in the milestone whose paragraph needs it, never higher in the queue because it is new: its place is its priority, and the lines already there keep their order and their `after`.

`/propose` and `/apply` do not start a line that is not free for them: once `my-loans`'s page is complete and its line `[>]`, run `/apply my-loans` while `lend-book` is `[*]`, and it says what the line waits on, leaves the mark as it is, and stops.

Free lines can run at the same time when they touch different files, judged from their pages and from docs/01, which says where each part of the code lives.
`search-catalog` and `reservations`, in `src/features/catalog/` and `src/features/reservations/`, can.
Two lines that both change `src/features/loans/`, as `lend-book` and a line to renew a loan would, cannot run together in one folder: the second build would edit files the first is still changing.

Which files a build touches is known only once its page exists, so the queue does not say it, and the check is `/apply`'s.
Before its first edit, `/apply` compares the files its page touches with those of the builds in flight, `[*]`, and of the builds done and not yet integrated; a file both touch is a conflict, and it stops before marking its line `[*]`, names the other line and the files they share, and leaves the mark as it is.
The same library, in four lines written for this chapter:

```
[x] members         the librarian registers and suspends members
[*] lend-book       the librarian lends a copy
[>] search-catalog  a member searches the catalog
[>] renew-loan      a member renews a loan once
```

Neither `search-catalog` nor `renew-loan` names an `after`, so both are free for `/apply`.
`search-catalog`'s build lives in `src/features/catalog/`, which `lend-book` does not touch, so it builds now.
`renew-loan`'s page changes `src/features/loans/`, as `lend-book`'s does, so `/apply renew-loan` stops before its first edit, says it shares that folder with `lend-book`, and leaves the line `[>]`; it builds once `lend-book` is integrated.
A command typed with several slugs makes the same check for each line: `/apply search-catalog renew-loan` builds `search-catalog` and reports that `renew-loan` stops on `lend-book`'s files, without waiting for it ([chapter 12](12-propose.md)).

[Chapter 19](19-worktrees.md) shows how two sessions run in one folder, and when they need two.

## What may run now

Asked what may run now, the agent does not read the end of every line for its `after`: it runs the kit's queue script, `propose/scripts/queue.sh`, in one line, `git -c "alias.fq=!sh .agents/skills/propose/scripts/queue.sh" fq <strategy>`, the same alias trick and the same strategy word as the claim script of [chapter 13](13-apply.md).
The script reads docs/06 and edits nothing: on trunk the queue of the folder where the session runs, and with a branch or a worktree per delivery, after `git fetch`, each delivery's line from its branch on origin, as the section above says, and chapter 19 says which copy counts in a delivery's own worktree and for a `[?]`, and which heading counts when a branch rewords one.
It draws every milestone with a line not `[x]`, each under its own `milestone:` line, as a tree, the queue tree: each line not yet `[x]`, under the last line it waits on, the one furthest down the queue of the pending lines its `after` names, with the others named after `+ after`, and its state.
On trunk, a state is one of these: in flight, by the command its mark names; `propose now` or `apply now`, free for that command; `waits:`, with what it waits on; or `blocked:`, with its reason and the command that resumes it.
When a milestone holds a line from a finding, two more lines may come between its heading and its tree, `findings:` and a warning, read in the section on findings below.
Then come the lines free for `/apply` and for `/propose`, each list in queue order across the milestones, and last `next:`, the command for the first free line down the queue.
Milestone 1 in six lines, written for this chapter like the four above, with `return-book` already defined:

```
[x] catalog         the librarian registers books and their copies
[x] members         the librarian registers and suspends members
[*] lend-book       the librarian lends a copy, or a rule refuses
[>] return-book     records a return · after lend-book
[>] search-catalog  a member searches the catalog
[ ] m1-review       the milestone against its paragraph · after all
```

On them the script prints this, the milestone's heading first:

```
milestone: Milestone 1: a librarian lends and takes back
[*] lend-book · in flight: apply
 └[>] return-book · waits: after lend-book
[>] search-catalog · apply now
 └[ ] m1-review + after lend-book, return-book · propose now

free for /apply, in order: search-catalog
free for /propose, in order: m1-review
next: /apply search-catalog
```

The `└` draws a line under the one it waits on.
`return-book`'s page is complete though `lend-book` is still being built, since its definition needed only `lend-book`'s page; its build waits until `lend-book` is integrated.
`search-catalog` may be built now, and `m1-review` sits under it, the last line its `after all` names, with the other two after `+ after`: every line above it is defined, so it may be defined now, and its build waits until they are all integrated.
The next delivery is `/apply search-catalog`, the first free line down the queue.
When a list holds more than one line, as on the nine lines above, where the script prints `free for /propose, in order: return-book my-loans`, the agent offers them as one command, `/propose return-book my-loans`, saying each slug is one more agent and costs as much as one session ([chapter 12](12-propose.md)).
`/propose` and `/apply` typed with no slug show the same tree and ask which line to take, and `/apply` ends with it.

A milestone that waits hides no free line of the next one.
On the library, in an example written for this chapter, every other line of milestone 1 is integrated and its review is defined, `[>]`, when the director wants to try the product before the review is built, so the person says `m1-review` is blocked, and it waits as `[?]`, ending `· resume: apply · blocked: the director tries it on Monday`; milestone 2, chapter 11's, holds `due-date-format`, not yet defined, and its review, `· after all`.
On that queue the script prints this:

```
milestone: Milestone 1: a librarian lends and takes back
[?] m1-review · blocked: the director tries it on Monday, then apply

milestone: Milestone 2: loan dates read at a glance
[ ] due-date-format · propose now
 └[ ] m2-review · waits: due-date-format not defined

free for /apply, in order: none
free for /propose, in order: due-date-format
next: /propose due-date-format
```

`m1-review` waits on the director, so milestone 1 holds nothing free, and the script draws milestone 2 under its own `milestone:` line and offers its first free line: `next:` is `/propose due-date-format`.
A free line of a later milestone comes after every free line of the milestones above it, in the queue's order, since a milestone's end sets priority (above), so a line parked under the next milestone is offered, and offered last.
A tree of the first open milestone alone would end at its waiting review: in one project, on 2026-11-13, a tree drawn that way answered `next: none` over a review waiting as `[?]` on an acceptance outside the team, while seven lines of the next milestone were free for `/propose`.

## Waiting: `[?]`

A line waits in three cases, never on another line:

* **The person says it is blocked.** The library has not bought its barcode scanners yet, so the librarian asks to hold `scan-copy`: `· resume: propose · blocked: no scanners yet`.
* **An answer was asked and not given.** `due-reminder` needs a text-message provider, the question went to the library's director, and nobody has answered: `· resume: propose · blocked: what provider?`.
* **A milestone review's code reading missed part of its range.** The review that closes a milestone reads, on the person's word, every change since the milestone's base, split into areas with one reader each that lists the paths it read ([chapter 15](15-closing-a-milestone.md)), and a reader that read part of its area reports the same way as one that read it all, so when, in the middle of `/apply m1-review`, the review's readers list no path of `src/features/catalog/`, the line waits with what was read as its reason: `· resume: apply · blocked: read all but catalog/`.

The reason goes at the end of the line, in words, `· blocked: <reason>`, never another line.
Before it goes the phase to resume, `· resume: propose` for a line that was `[ ]` or `[~]`, `· resume: apply` for one that was `[>]` or `[*]`, so the session that takes the line up again knows which command it needs.
Any mark before `[x]` can become `[?]`: a line can wait before anyone defines it, while its page is being written, or halfway through its build.

A line leaves `[?]` when the reason is resolved.
The person says so; or the session that records the answer clears it, as when the director names the provider and the name becomes a line of docs/00.
Both suffixes go, `resume` and `blocked`, and the resume phase says where the line goes back.
`due-reminder`, with `resume: propose`, goes back to `[ ]`, and any draft of its page stays for `/propose` to finish: a draft is a page begun, not a definition complete.
A line with `resume: apply` goes back to `[>]`.

`/propose` and `/apply` both stop on a `[?]` line: they say what it waits on, and go on only once the reason is resolved, in one of those two ways.
A command that ran past the reason would build on an answer nobody gave.

## A line that needs another

A line that needs another line first is not waiting: it ends `· after <slug>` and keeps the mark that names its next command, so the mark alone says whether `/propose` or `/apply` comes next.
When the need is known as the line is added, the suffix is written then: `my-loans` needs loans to show, so it was added as `[ ] my-loans ... · after lend-book`.
When work already started finds the need, the session adds the slug to the line's `after` and returns the line, from `[~]` to `[ ]` with its draft kept, or from `[*]` to `[>]` with its page saying what was built and what it waits on (chapter 13 says what happens to the files already built).
That is two edits: the mark by the script, the suffix by the file edit.

In the middle of `/apply my-loans`, the build finds that `lend-book` sets the due date one day early at the end of a month.
The fix becomes a `[ ]` line above `my-loans`, `fix-due-date`, ending `· from my-loans`, and `my-loans` goes back to `[>]`, ending `· after lend-book, fix-due-date`.
In the middle of `/propose reservations`, the definition finds it needs `search-catalog` first: the line goes back to `[ ]`, ending `· after search-catalog`, and its draft stays.

A `[?]` in their place hides the next command.
In one project, on 2026-11-13, a session that found two lines needed another first left both at `[?]`, ending `· after <slug> · resume: propose · blocked: after <slug>`: reading the queue, the person could not tell from the mark whether `/propose` or `/apply` came next, and a single line said "after" in two ways; another project's queue held four such lines.

The library's milestone 1 once both lines went back, written for this chapter: `catalog`, `members` and `lend-book` integrated, `fix-due-date` and `my-loans` as above, `search-catalog` defined and `reservations` returned to `[ ]`.
The queue script draws it so:

```
milestone: Milestone 1: a librarian lends and takes back
findings: 1 open of 1 from a finding · 3 planned open
[ ] fix-due-date · propose now
 └[>] my-loans · waits: after fix-due-date
[>] search-catalog · apply now
 └[ ] reservations · propose now

free for /apply, in order: search-catalog
free for /propose, in order: fix-due-date reservations
next: /propose fix-due-date
```

`my-loans` keeps `[>]` under `fix-due-date`, and `waits:` is the tree's word for an `after` that does not let the next command start yet, where a `[?]` line shows `blocked:`; once `fix-due-date` is integrated, `my-loans` is free for `/apply` with nothing to clear.

That is the cost of reading `after` per command: `reservations` is free for `/propose` as soon as `search-catalog`'s page is complete, as here, not once its code is integrated.
Where a definition needs the other line built, the project's docs/05 says so, and the queue script does not know it.
With a branch or a worktree per delivery, a returned line's branch is still its claim, and the tree shows it `waits:` for as long as its `after` waits.

## A line from a finding

A delivery reads code it did not write, and sometimes finds a flaw there: `/propose return-book`, reading `lend-book`'s code, finds that a member suspended from the members screen can still borrow: `lend` refuses a member whose `suspended` is true, as its tests prove with a member built that way, but suspending a member from that screen records it in another field, which `findMember` does not read.
A flaw a delivery finds in what it built itself is fixed in that delivery; a finding is a flaw it finds anywhere else, `/propose` while it defines included.
Each finding made a line looks reasonable on its own, and lines from findings, added one by one, can stand ahead of the work the milestone's paragraph asks for, so the milestone fills with repairs while its features wait (chapter 13 tells where it went wrong).

So a finding becomes a line only when it is grave: it breaks a clause of the milestone's paragraph for a person on its usual path, loses or exposes data, or leaves verify red; a fix a delivery in flight cannot go on without is grave too, as `fix-due-date` is for `my-loans`.
A grave finding becomes a `[ ]` line ending `· from <slug>`, the delivery that found it, as `fix-due-date` ends `· from my-loans` above.
A loan to a suspended member is one a rule should refuse, going through on the librarian's usual path, so `fix-suspended` is grave, and its line ends `· from return-book`.

A finding's place is its priority, as for any line added later, and the work the paragraph asked for comes first.
A planned line is a line of the milestone that is not from a finding and is not its review: the lines the paragraph's clauses asked for.
A grave finding goes above the open planned lines only when verify is red or one of them needs it, as `fix-due-date` stands above `my-loans`, which names it in its `after`.
Otherwise it goes below them, above the review, or under the review once the review ran.
Verify is green and neither `return-book` nor `search-catalog` needs `fix-suspended`, so it goes below `search-catalog`, above `m1-review`.

Every other finding is a note on the page of the delivery that found it, under the heading `## For the review`, above the page's `commit` block, one line each: the file and line, and what a person would see.
A note written for this chapter, on the library:

```
## For the review

* `src/features/catalog/search.ts:41`: an accented title is never found
```

A note is not a line: it waits for the next milestone review, which copies it onto its page (chapter 15 grades it).
A finding nobody can say is grave is a note.

A line that delivers a test, a proof tool or a change to the process, and is not a grave finding, enters the queue only on the person's word; without it, it is a note.
Such lines look like progress and deliver nothing the paragraph asks for: in one project, on 2026-11-12, a proof run in parallel, a proof split by state and test helpers were queued while the project's features waited.

The queue script counts the lines from findings and warns when one stands ahead of planned work.
The library's milestone 1 in five lines, written for this chapter, with `fix-suspended` put above the planned lines:

```
[x] lend-book       the librarian lends a copy, or a rule refuses
[ ] fix-suspended   a suspended member borrows · from return-book
[>] return-book     records a return · after lend-book
[ ] search-catalog  a member searches the catalog
[ ] m1-review       the milestone against its paragraph · after all
```

These are the first three lines the script prints on them; the tree follows, read as in the section on what may run now:

```
milestone: Milestone 1: a librarian lends and takes back
findings: 1 open of 1 from a finding · 2 planned open
⚠️ ahead of planned lines: fix-suspended
```

`findings:` counts the milestone's lines ending `· from <slug>`, then how many of them are open, a finding line already `[x]` staying in the first number only, then the open planned lines; the review and a cancelled line are not counted.
The warning names `fix-suspended`, an open finding line standing ahead of `return-book` and `search-catalog`, though neither needs it, and the tree ends with `next: /propose fix-suspended`: the repair comes before the planned work.
Moved below `search-catalog`, above `m1-review`, the line no longer stands ahead and the warning goes, `findings:` stays as it is, and `next:` is `/apply return-book`.
A finding line an open line names in its `after` is left out of the warning: `fix-due-date`, which `my-loans` names, stands above because a planned line needs it.
The warning is a look, not a verdict: a finding that leaves verify red stands ahead and warns too, and the person reads which it is, one verify needs or one that should move below.
Since `/apply` ends with the tree, the drift shows at the end of every build without anyone asking.

## A session that ended, a delivery cancelled

A session can end without anyone blocking its line: the host closes, the connection is lost, the plan's limit is reached.
Its line keeps its mark.
`reservations` stays `[~]` after the conversation that was defining it ends; nothing waits on anyone, so it does not become `[?]`.
The mark alone cannot tell that the session ended: a `[~]` or `[*]` line is held by a session, and that session may be talking in another folder or on another machine right now.
So a new session does not take the line over because it sees the mark; the person, who knows the session ended, says so and runs `/propose reservations` again.
The command then inspects the page, the working folder and the index before editing, and goes on from what the earlier conversation wrote.
`lend-book`, `[*]` when its build lost the connection, resumes the same way with `/apply lend-book`: the files already built and what is already in the index stay the delivery's, and the line stays `[*]`, never put back to `[>]` or `[ ]` as if nothing had been done; neither resumed command marks its line again, and the mark script would refuse a second `[~]` or `[*]` on it.

A delivery the person cancels, because the work proved it impossible, because it was refused, or because nobody wants it any more, stays in the queue too.
It ends `[x]` with the reason at the end of the line, `· dropped: <reason>`, and its page goes to `work/done/` like any other, saying what was built and what was undone, or that nothing was built.
The library wanted the librarian to print a member's card from the browser, and the card printer turned out to have no driver the browser could reach; the librarian cancels the line, and `reprint-card`, added after it, waits on it, in two lines written for this chapter:

```
[x] print-card      prints a member card · dropped: no printer driver
[ ] reprint-card    reprints a lost card · after print-card
```

`[x]` alone says the delivery's promise holds, with verify green; `[x]` with `· dropped:` says the decision is taken and the promise does not exist.
The person sets it, not `/apply`, because cancelling is a decision about scope, and the line stays so that nobody later asks whether `print-card` was forgotten.
By the free rule alone, `reprint-card`'s build is free once `print-card` is `[x]`, and that is the trap: the `[x]` it names is a decision, not a card printer that works.
So a line whose `after` names a cancelled delivery is the person's to re-decide: drop it too, as `reprint-card` would be, or rewrite it on what does exist.

A milestone's review would have no good way out.
A review that named every line above it would name the cancelled one too and wait, as `reprint-card` does, on a line only the person's decision clears; and of the person's ways out, dropping the review loses the test of the milestone's paragraph, and rewriting it on what exists turns its `after all` into a list of every other line above it.
On 2026-10-26, in one project, a Milestone 1 review waited on a line the person had dropped: the queue script answered `after <slug>, dropped: re-decide`, and the review's `after all` was replaced by a list of the other 27 slugs.
So `after all` names no cancelled line: it is every line above the review in its milestone but the cancelled ones, and it leaves them out.
Suppose the two lines above, written for this chapter, sit in the library's milestone 1, above `m1-review`.
`after all` leaves `print-card` out, so the cancelled line never keeps the review waiting.
`reprint-card` is not cancelled, so `after all` counts it: the queue tree prints it with `waits: after print-card, dropped: re-decide`, and the review waits with it until the person re-decides `reprint-card`.
Dropped too, it leaves the review's `after all` as well; rewritten on what exists, the review waits for it like any other line.

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
Resolving the reason removes both suffixes and the tag with them.
`my-loans`, back at `[>]` when its build found it needs `fix-due-date`, stays in Doing with no tag, as `[>]` and not as a `[*]` no session is building: it is queued, not stuck.

Chapter 20 shows how a script mirrors the queue to a team's own board, one way.

A board can also read the queue itself, with nothing to mirror.
It reads docs/06 and the pages in `work/` by slug, on trunk from the folder's own files and with a branch or a worktree per delivery from each slug's own branch on origin, after `git fetch`, with the lines only a branch has, and moves its cards as each mark becomes visible to it while the agent works.

## What the team gains

A manager reads where every delivery stands, and what each waiting one waits on, without asking anyone and without a status meeting.
On Case A, five lines blocked on the client read as idle work, and every delivery reached Doing only after its definition was over, counted by the author on the project's queue and board; a mark set when the work changes, and one for waiting, answer both.
A request that proved impossible there was closed in the queue with its reason instead of left in silence ([chapter 23](23-adoption.md)), and the kit writes such a closure as `[x]` with `· dropped:`, and a line closed that way keeps no review waiting.

The queue also says which lines can run together: without that, a person who wants two sessions has to work it out alone before opening the second; the queue tree draws it from the queue, without a meeting, each line under what it waits on, and ends with the command to run next, and `/apply` checks the files before its first edit, so two builds never change the same file at once.
A line that needs another keeps the mark of its next command, so the queue shows no blocked line where nothing went wrong.
The tree also says how much of the milestone came from findings and names a finding line standing ahead of planned work, so the drift shows the day it starts; and a finding that is not grave waits on its delivery's page for the review instead of entering the queue.
Every open milestone is drawn, so a milestone waiting on someone outside the team hides none of the work after it.
And no session marking its line can leave the queue empty under the board and the other sessions, nor can two sessions that start one line both build it: a mark is one byte, changed whole or not at all, and a start on a line already taken is refused.

## Key points

* Six marks, `[ ]` not defined, `[~]` being defined, `[>]` completely defined and ready for `/apply`, `[*]` being built, `[x]` done, `[?]` waiting, each changed when the work changes, not when a command ends: `/propose` sets `[~]` and `[>]`, `/apply` sets `[*]` and `[x]`, the person sets `[x]` with `· dropped: <reason>` when cancelling, any session sets `[?]`; every mark changes through the kit's mark script, one byte, `[~]` only on a `[ ]` line and `[*]` only on a `[>]` one, `/apply`'s `[x]` staged on its line alone with `stage`, and any other edit to the queue is the host's file edit on its lines, never a program that writes the whole file; a line whose session ended keeps its mark, and its command resumes it on the person's word, inspecting the page, the folder and the index first, and a cancelled delivery's page in `work/done/` says what was built and undone.
* A line is free for a command when it is not `[x]` nor `[?]` and its `after` lets that command start: `/propose` when every line it names is `[>]` or beyond, `/apply` when every one is integrated, `[x]` on trunk, merged into the main branch with a branch or a worktree per delivery; the review line's `· after all` names every line above it in its milestone but the cancelled ones, and a line whose `after` names a cancelled one is the person's to re-decide; with a branch or a worktree per delivery, a line whose branch exists after `git fetch` is taken, whatever the main branch shows; the next delivery is the first free line no session holds, and before its first edit `/apply` stops on a file a build in flight or not yet integrated is changing.
* Asked what may run now, the agent runs the kit's queue script and shows its tree: every open milestone under its own `milestone:` line, with `findings:` and its `⚠️` warning under a milestone's heading when it holds a line from a finding, each line not `[x]` under the last line it waits on with its state, then the lines free for `/apply` and for `/propose`, in the queue's order across the milestones, so a milestone that waits hides no free line of the next, and `next:`, the command for the first; it offers the free lines as one command with several slugs, each slug one more agent costing as much as one session, and `/propose` and `/apply` typed with no slug show the tree and ask.
* `· after` is an order, written with the line or by the work that finds the need, which returns `[~]` to `[ ]` with the draft kept or `[*]` to `[>]`, never `[?]`; it is read per command, and where a definition needs the other line built, docs/05 says so; a line waits in three cases, when the person says so, when an answer was asked and not given, or when a milestone review's code reading missed part of its range, with the phase to resume and the reason in words at its end, `· resume: propose · blocked: what provider?`; when the reason is resolved, both suffixes go and it returns as that phase says, `resume: propose` to `[ ]` with any draft kept, `resume: apply` to `[>]`, and until then `/propose` and `/apply` stop on it, as on a line not free; a grave finding is a `[ ]` line ending `· from <slug>`, above the open planned lines only when verify is red or one of them needs it, every other finding a note under `## For the review` on the page of the delivery that found it, and a line that delivers a test, a proof tool or a change to the process enters only on the person's word.
* The queue is a kanban board, a column per mark, a `[?]` card in Waiting until it returns to `[ ]` or `[>]`; on this chapter's three columns, Doing holds `[~]`, `[>]` and `[*]`, and a `[?]` card is tagged blocked in the column its resume phase names, To Do for `propose`, Doing for `apply`; a board that reads the queue sees a mark at once on trunk, and with a branch or a worktree per delivery from each slug's own branch on origin, after `git fetch`, pushed when `/propose` creates it, since the main branch shows the line as it was until the merge.

[^toyota-kanban]: Toyota Motor Corporation, "75 Years of Toyota", Part 2, Chapter 1, Section 4, Item 4, "Development and Deployment of the Toyota Production System", accessed 2026-10-05. <https://www.toyota-global.com/company/history_of_toyota/75years/text/entering_the_automotive_business/chapter1/section4/item4.html>
[^azure-kanban]: Microsoft Learn, "About Kanban boards", Azure Boards, accessed 2026-09-30. <https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-overview>
