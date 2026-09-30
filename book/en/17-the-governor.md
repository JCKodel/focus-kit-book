# The governor

After this chapter you can ask of anything that wants to enter your process, and of every step already in it, which concrete error it would have caught, and accept only an answer that names an error that happened.
You can also list what the process does not have, and say what does each of those jobs instead.

## The problem

A process grows one reasonable step at a time.
A check here, a template there, a review before each build: each one is sensible on its own, and each one is paid again by every delivery that follows, which runs it, satisfies it and waits for it.
On Ninjobs the steps piled up to 29 checks that never caught an error in the product, costly to satisfy and cheap to get around (chapter 9).[^ninjobs]
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

On Ninjobs, when I restarted the project, the 29 checks left: none of them could name an error in the product it had caught.[^ninjobs]
Two checks took their place, both guarding the product's promise of privacy, where a leak is the error the product cannot afford: a proof of what each privacy level may show, and a test of the database access rules.[^ninjobs]

What entered later came in the same way.
Supabase, the database vendor, ships its own lint, and one of its warnings sat in a report that nobody opened.
It pointed at an index identical to one that already existed, so every write to that table wrote the same index twice, and no test saw it.
On 2026-09-02 the vendor's lint entered verify, and the duplicate index was the error it named.[^ninjobs]
Two rules came with it: a new warning fails verify, and a warning already decided goes on a list of exceptions with its reason.
An entry on that list with no live warning behind it also fails, because a list with dead entries is a list nobody reads anymore: the governor applied to the list itself.

In code the governor has its own form, the second-occurrence rule of chapter 4: one copy is no evidence that a shared version is needed, and two copies are the error that happened.

## What the process does not have

§7 of docs/05 lists seven things the process does not have.
Each job still gets done, by something the process already has:

* **No formal spec:** the page, `work/<slug>.md`, says what the delivery does, in the words of the person who reads it (chapter 14).
* **No spec delta**, the OpenSpec file that lists only the requirements a change adds, changes or removes, merged into the specs when the change is archived:[^openspec-glossary] the documents the delivery changes, in the same delivery, say what changed.
* **No change folder:** the page is the change, in `work/<slug>.md` while it is built and in `work/done/` afterwards.
* **No numbered tasks:** the Behaviour lines, each one a test or a check.
* **No gate before implementation:** the person who reads the page before `/apply`, and asks for what is missing.
* **No specialized subagent**, an agent that another agent launches for one narrow role with its own instructions, such as a planner or a reviewer:[^claude-code-subagents] one agent that reads the documents.
* **No tool the deliveries did not ask for:** the governor itself, which keeps it out until a delivery names the error it would have caught.

## The governor decides per project

The question gives different answers in different projects, and it should.

Case A, a client project on a low-code platform, added a fourth mark to its queue, `[?]`, for a line waiting on a person.[^case-a]
The kit's three marks read `[>]` as "defined and waiting to be built", and five lines blocked on the client's answers looked like work nobody had started.[^case-a]
That was the error, and the mark named it.

This book considered the same mark for its own queue and rejected it.[^adr-0013]
Its one outside answer is the author's approval of the anonymized passages, and that approval is an item of a page's Done when, so no line of its queue ever waits on a person.
The same mark, the same question, and two answers, each from the project's own history.

## What the team gains

Every step of a process is paid by every delivery, so a step that catches nothing is a tax on all of them.
Ninjobs reached its public opening on a process of six rules, the ones the kit's `SETUP.md` now lists for every project, and two checks, after 29 checks had gone with it through fifteen days that built four screens.[^ninjobs]
The governor keeps a process that small, and it lets a team say yes to a step with the error that justifies it written down.

## Key points

* Ask anything that wants to enter the process, and every step already in it: which concrete error would it have caught?
* The answer names an error that happened; a possible error justifies anything, and every step is paid by every delivery after it.
* A step that names no error leaves, and a list of exceptions fails on an entry with no live warning.
* Each of the seven things the process does not have has its job done by something it has: the page, the documents, the Behaviour lines, the person, one agent, and the governor itself.
* The governor decides per project: Case A added a mark for lines waiting on a person, and this book, whose lines never wait on one, did not.

[^ninjobs]: Ninjobs, the author's product, a private repository, read by the author in its ADR-0022, for the 29 checks, the fifteen days and four screens of the era before the pivot and the two checks kept after it, and in the amendment of 2026-09-02 and its docs/05 §5, for the database lint and its list of exceptions, paraphrased.
[^openspec-glossary]: Fission AI, "Glossary", OpenSpec 1.13.2. <https://github.com/Fission-AI/OpenSpec/blob/v1.13.2/docs/glossary.md>
[^claude-code-subagents]: Anthropic, "Create custom subagents", Claude Code documentation, accessed 2026-09-29. <https://code.claude.com/docs/en/sub-agents>
[^case-a]: Case A, a client project on a low-code platform, a private repository, read by the author in its docs/05 and its ADRs: the fourth mark and the reason recorded for it. Its owner, its client and its business are not disclosed.
[^adr-0013]: This book's ADR-0013, "three marks only", 2026-09-24. <https://github.com/JCKodel/focus-kit-book/blob/main/docs/adr/ADR-0013-three-marks.md>
