# 18. The governor

After this chapter you can ask of anything that wants to enter your process, and of every step already in it, which concrete error it would have caught, and accept only an answer that names an error that happened.
You can also list what the process does not have, and say what does each of those jobs instead.

## The problem

A process grows one reasonable step at a time.
A check here, a template there, a review before each build: each one is sensible on its own, and each one is paid again by every delivery that follows, which runs it, satisfies it and waits for it.
On Ninjobs the steps piled up to 29 checks that never caught an error in the product, costly to satisfy and cheap to get around.
Nobody added them to slow the work down; nobody asked what each had caught.

## The question

The kit writes one rule into every project's process document, in §7 of docs/05, "What this process does not have": when something new is proposed, ask which concrete error it would have caught, and accept an answer that names an error that happened.
The file that describes the kit lists it among the rules every project keeps: nothing enters the process without naming the concrete error it would have caught.
This book calls that question the governor, after the part that keeps an engine from running faster than its load asks.

The answer has to name an error that happened, because a possible error justifies anything: some error is always possible.
An error that happened is a fact you can check, in the history, on a page or in a finding.
And the cost it must outweigh is paid by every delivery after it.

## It works both ways

The question decides what enters, and it decides what stays.

On Ninjobs, when I restarted the project, the 29 checks left: none of them could name an error in the product it had caught.
Two checks took their place, both guarding the product's promise of privacy, where a leak is the error the product cannot afford: a proof of what each privacy level may show, and a test of the database access rules.

What entered later came in the same way.
Supabase, the database vendor, ships its own lint, and one of its warnings sat in a report that nobody opened.
It pointed at an index identical to one that already existed, so every write to that table wrote the same index twice, and no test saw it.
On 2026-09-02 the vendor's lint entered verify, and the duplicate index was the error it named.
Two rules came with it: a new warning fails verify, and a warning already decided goes on a list of exceptions with its reason.
An entry on that list with no live warning behind it also fails, because a list with dead entries is a list nobody reads anymore: the governor applied to the list itself.

In code the governor has its own form, the second-occurrence rule of chapter 4: one copy is no evidence that a shared version is needed, and two copies are the error that happened.

## What the process does not have

§7 of docs/05 lists eight things the process does not have.
Each job still gets done, by something the process already has:

* **No formal spec:** the page, `work/<slug>.md`, says what the delivery does, in the words of the person who reads it.
* **No spec delta**, the OpenSpec file that lists only the requirements a change adds, changes or removes, merged into the specs when the change is archived:[^openspec-glossary] the documents the delivery changes, in the same delivery, say what changed.
* **No change folder:** the page is the change, in `work/<slug>.md` while it is built and in `work/done/` afterwards.
* **No numbered tasks:** the Behaviour lines, each one a test or a check.
* **No gate before implementation:** the person who reads the page before `/apply`, and asks for what is missing.
* **No review of a review:** each line a milestone review adds passes through its own page, its proof and the person's commit.
* **No specialized subagent**, an agent that another agent launches for one narrow role with its own instructions, such as a planner or a reviewer:[^claude-code-subagents] one agent that reads the documents.
* **No tool the deliveries did not ask for:** the governor itself, which keeps it out until a delivery names the error it would have caught.

## From one project to the kit

The question is asked in each project, and an error one project proves can change the kit every project installs.

Case A, a client project on a low-code platform, read its queue on a kanban board, and the board showed what the kit's three marks hid (chapter 16).
A delivery reached Doing only once its page was written, and five lines blocked on the client's answers looked like work nobody had started.
Case A added a mark by hand, `[?]`, for a line waiting on a person: five idle-looking lines were the error, and the mark named it.

The error was not Case A's alone: any team that reads its queue as a board meets it the day a line waits, or a delivery is being defined.
So the kit took the answer in its version 2026.10.05, six marks with `[?]` among them, and this book follows the kit.[^adr-0018]
The governor still decided: the mark entered with the error that justified it, proven on one project, and the kit carried it to every project.

## What the team gains

Every step of a process is paid by every delivery, so a step that catches nothing is a tax on all of them.
Ninjobs reached its public opening on a process of six rules, the ones the kit's `SETUP.md` now lists for every project, and two checks, after 29 checks had gone with it through fifteen days that built four screens.
The governor keeps a process that small, and it lets a team say yes to a step with the error that justifies it written down.

## Key points

* Ask anything that wants to enter the process, and every step already in it: which concrete error would it have caught?
* The answer names an error that happened; a possible error justifies anything, and every step is paid by every delivery after it.
* A step that names no error leaves, and a list of exceptions fails on an entry with no live warning.
* Each of the eight things the process does not have has its job done by something it has: the page, the documents, the Behaviour lines, the person, the person's commit, one agent, and the governor itself.
* An error proven on one project can change the kit: Case A's idle-looking lines earned `[?]`, and the kit took it for every project.

[^openspec-glossary]: Fission AI, "Glossary", OpenSpec 1.13.2. <https://github.com/Fission-AI/OpenSpec/blob/v1.13.2/docs/glossary.md>
[^claude-code-subagents]: Anthropic, "Create custom subagents", Claude Code documentation, accessed 2026-09-29. <https://code.claude.com/docs/en/sub-agents>
[^adr-0018]: This book's ADR-0018, "six marks", 2026-10-05, the file `ADR-0018-six-marks.md` in its decisions folder. <https://github.com/JCKodel/focus-kit-book/tree/main/docs/adr>
