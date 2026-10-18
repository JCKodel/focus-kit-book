# 16. The governor

After this chapter you can ask of anything that wants to enter your process, and of every step already in it, which concrete error it would have caught, and accept only an answer that names an error that happened.
You can also list what the process does not have, say what does each of those jobs instead, and say why the reviews' read-only readers and their checker are the one specialized subagent it admits.

## The problem

A process grows one reasonable step at a time.
A check here, a template there, a review before each build: each one is sensible on its own, and each one is paid again by every delivery that follows, which runs it, satisfies it and waits for it.
On Ninjobs the steps piled up to 29 checks that never caught an error in the product, costly to satisfy and cheap to get around.
Nobody added them to slow the work down; nobody asked what each had caught.

## The question

The kit writes one rule into every project's process document, in §7 of docs/05, "What this process does not have": when something new is proposed, ask which concrete error it would have caught, and accept an answer that names an error that happened.
This book calls that question the governor, after the part that keeps an engine from running faster than its load asks.

The answer has to name an error that happened, because a possible error justifies anything: some error is always possible.
An error that happened is a fact you can check, in the history, on a page or in a finding.
And the cost it must outweigh is paid by every delivery after it.

## It works both ways

The question decides what enters, and it decides what stays.

On Ninjobs, when I restarted the project, those checks left: none of them could name an error in the product it had caught.
Two checks took their place, both guarding the product's promise of privacy, where a leak is the error the product cannot afford: a proof of what each privacy level may show, and a test of the database access rules.

What entered later came in the same way.
Supabase, the database vendor, ships its own lint, and one of its warnings sat in a report that nobody opened.
It pointed at an index identical to one that already existed, so every write to that table wrote the same index twice, and no test saw it.
On 2026-09-02 the vendor's lint entered verify, and the duplicate index was the error it named.
Two rules came with it: a new warning fails verify, and a warning already decided goes on a list of exceptions with its reason.
An entry on that list with no live warning behind it also fails, because a list with dead entries is a list nobody reads anymore: the governor applied to the list itself.

In code the governor has its own form, the second-occurrence rule of chapter 3: one copy is no evidence that a shared version is needed, and two copies are the error that happened.

## What the process does not have

§7 of docs/05 lists eight things the process does not have.
Each job still gets done, by something the process already has:

* **No formal spec:** the page, `work/<slug>.md`, says what the delivery does, in the words of the person who reads it.
* **No spec delta**, the OpenSpec file that lists only the requirements a change adds, changes or removes, merged into the specs when the change is archived:[^openspec-glossary] the documents the delivery changes, in the same delivery, say what changed.
* **No change folder:** the page is the change, in `work/<slug>.md` while it is built and in `work/done/` afterwards.
* **No numbered tasks:** the Behaviour lines, each one a test or a check.
* **No gate before implementation beyond a complete page:** the page is the one gate, read by the person before `/apply`, who asks for what is missing; `/apply` refuses a page that is not complete and points to `/propose`.
* **No review of a review:** each line a milestone review adds passes through its own page, its proof and the person's commit.
* **No specialized subagent beyond the reviews' readers and checker**, an agent that another agent launches for one narrow role with its own instructions, such as a planner or a reviewer:[^claude-code-subagents] one agent that reads the documents, plans and builds, and the reviews' readers and checker are the exception the next section explains.
* **No tool the deliveries did not ask for:** the governor itself, which keeps it out until a delivery names the error it would have caught.

## The subagent it admits

Two steps of the process can launch agents of their own.
The delivery review of [chapter 13](13-apply.md), where the host has no review of its own, hands a delivery's changes to a read-only agent, a context apart, because the agent that wrote a change rereads it with the reasoning that wrote it.
The milestone review of [chapter 15](15-closing-a-milestone.md) hands a milestone's changes to one reader per area, a read-only agent where the host runs agents, and a checker, an agent or the review's session, marks each candidate before the person sees it.
These readers, and the checker when an agent does that job, are specialized subagents in this chapter's sense: the session launches each one for one narrow role, and it reads files and the changes and edits nothing.

The governor let them in the way it lets in anything, each on an error that happened, all in this book's own repository, which is public:

* **The readers.** A reader of the code that builds the book, with the whole repository open, found that the function listing the repository's files dropped every file whose name holds a non-ASCII letter, such as `café.md`, so every check of `make verify` skipped it, the scan that keeps private names out of the book included, and none of them could see it, since the checks were what was broken.[^m14-review]
* **The delivery review's reader.** That fault sat in the file from the delivery that wrote it, read before its commit only by the agent that wrote it and the person who committed it, and, found only at a milestone's review, it became a line of its own instead of a fix in that delivery.
* **The paths read.** One reader of that same review read some of the chapters, and the review closed as if it had read them all.
* **The checker.** A reader said a number in one chapter had no row in the table it came from; opened, the table gave it, from two of its rows.

They read and report candidates, and the milestone's readers list the paths they read; what gets fixed is decided by `/apply` or the person, and the readers and the checker fix nothing.
The checker works inside the one review, before the person sees a candidate, so the process still has no review of a review: the person decides what counts.
The exception opens nothing else: a planner, a builder or a fixer subagent still has to name its error, and until one does, it stays out.

## The error that earned a mark

The question is asked in each project, and the governor decides there, with an error that project met.
On Case A, a client project on a low-code platform, lines waiting on the client's answers read as idle work on its board, and that error is what let in the mark the project added by hand, `[?]` ([chapter 14](14-queue-states.md) tells the story).

## What the team gains

Every step of a process is paid by every delivery, so a step that catches nothing is a tax on all of them.
Ninjobs reached its public opening on a process of six rules, the ones the kit's `SETUP.md` lists for every project, and two checks, after the old checks had gone with it through fifteen days that built four screens.
The governor keeps a process that small, and it lets a team say yes to a step with the error that justifies it written down.
The one exception carries the errors that justify it, so the team checks it the way it checks any step, and the readers stay on the job those errors gave them.

## Key points

* Ask anything that wants to enter the process, and every step already in it: which concrete error would it have caught?
* The answer names an error that happened; a possible error justifies anything, and every step is paid by every delivery after it.
* A step that names no error leaves, and a list of exceptions fails on an entry with no live warning.
* Each of the eight things the process does not have has its job done by something it has: the page, the documents, the Behaviour lines, the person, the person's commit, one agent, and the governor itself; the reviews' readers and checker are the one specialized subagent it admits, each on an error that happened.
* The governor decides in each project, with an error that project met: Case A's `[?]` entered because waiting lines read as idle work.

[^openspec-glossary]: Fission AI, "Glossary", OpenSpec 1.13.2. <https://github.com/Fission-AI/OpenSpec/blob/v1.13.2/docs/glossary.md>
[^claude-code-subagents]: Anthropic, "Create custom subagents", Claude Code documentation, accessed 2026-09-29. <https://code.claude.com/docs/en/sub-agents>
[^m14-review]: J.C. Ködel, "One Page at a Time", the record of the review of M14, 2026-10-16, in the book's repository. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/m14-review.md>