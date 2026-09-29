# The governor, and what the process does not have

After this chapter you can ask one question of anything that wants to enter your process, and of every step already in it: which concrete error would it have caught?
You accept only an answer that names an error that happened.
You can also say what the process does not have, and what does each of those jobs instead.

## The question

The kit writes one rule into every project's process document, in §7 of docs/05, "What this process does not have": when something new is proposed, ask which concrete error it would have caught, and accept an answer that names an error that happened.
`SETUP.md`, the file that describes the kit, lists it among the principles: nothing enters the process without naming the concrete error it would have caught.
This book calls that question the governor, after the part that keeps an engine from running faster than its load asks.

The answer has to name an error that happened because a step is paid again by every delivery that follows it: each one runs the step, satisfies it and waits for it.
A possible error justifies anything, since some error is always possible; an error that happened is a fact you can check, in the history, on a page or in a finding.
[Chapter 4](04-birth-of-focus-kit.md) showed where the other answer leads: checks every delivery had to pass, and that had never failed on an error in the product.

## A "no" and a "yes"

The "no" came in [chapter 10](10-propose.md): the agent added to the clinic's `skeleton` page a check that client code never imports server files, a check that named no error it would have caught, and it left the page for its Out of scope.

The "yes" is in this book's own `make verify`.
Chapter 8 cited the record of its `/analyze` run 13 times in English and 14 times in Portuguese, because one Portuguese sentence carried a mention that had no counterpart in English.[^useful-notes]
The parity check then compared chapters, headings and status, and passed.
The delivery `useful-notes` extended it: a chapter's two editions must cite the same note keys, each as many times, and its page names chapter 8's mismatch as the error that happened.[^useful-notes]
The error came first; the check came after it, and could name it.

## Asking it again of what is there

The question works in both directions: it decides what enters, and it decides what stays.

On Ninjobs, when I restarted the project, I left out a check I had written myself on the form of the code.[^ninjobs]
No error in the product had ever failed it, so it had nothing to name.
Supabase, the database vendor, ships its own lint, and one of its warnings sat in a report that nobody opened.
It pointed at an index identical to one that already existed, so every write to that table wrote the same index twice.
No test saw it.

On 2026-09-02 the vendor's lint entered `verify`, and the duplicate index was the error it named.[^ninjobs]
Two rules came with it.
A new warning fails `verify`.
A warning already decided goes on a list of exceptions, with its reason, and an entry on that list with no live warning behind it also fails, because a list with dead entries is a list nobody reads anymore.
The first rule keeps new warnings from piling up in a report again; the second applies the governor to the list itself.

## What the process does not have

§7 of docs/05 lists seven things the process does not have.
Each job still gets done, by something the process already has:

* **Formal spec:** the page, `work/<slug>.md`, says what the delivery does, in the words of the person who reads it.
* **Spec delta:** the documents the delivery changes, in the same delivery, say what changed.
* **Change folder:** the page is the change, in `work/<slug>.md` while it is built and in `work/done/` afterwards.
* **Numbered tasks:** the Behaviour lines, each one a test or a check.
* **Gate before implementation:** the person who reads the page before `/apply`.
* **Specialized subagent:** one agent that reads the documents.
* **A tool the deliveries did not ask for:** the governor itself, which keeps it out until a delivery names the error it would have caught.

Two things in this book look like items of that list.
Reading the page before `/apply` ([chapter 10](10-propose.md)) is no gate: a person decides what to ask the agent, and the process runs no check between the page and the build.
The second agent that read the `skeleton` page in chapter 10 is no specialized subagent: I chose a reader once, for one page, and no step of the process calls one.

## The same question in code

In code the governor has its own rule, written in the text of `/apply` and in the AGENTS.md the kit writes: an abstraction is written on the second concrete occurrence, and the delivery says which was the first.
One copy is no evidence that a shared version is needed; two copies are the error that happened.

The review in chapter 12 found two such repetitions in the clinic, and they became two lines of its milestone 2, at the tag [`book-v1/closing-a-milestone`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone):[^closing-a-milestone-run]

```diff
+[ ] route-errors         one shared databaseFailed and one shared notFound answer; the first copies are in session.server.ts and weeklyHours/route.server.ts
+[ ] minutes-of           one shared "HH:MM" parser; the first copy is in weeklyHours/rules.ts, the second in appointments/rules.ts
```

Each line names the first copy, and `minutes-of` names the second as well, so the delivery that builds the shared version starts from both.

## Key points

* Ask anything that wants to enter the process, and every step already in it: which concrete error would it have caught?
* The answer names an error that happened; a possible error justifies anything, and every step is paid by every delivery after it.
* A step that names no error leaves, and a list of exceptions fails on an entry with no live warning.
* Each of the seven things the process does not have has its job done by something it has: the page, the documents, the Behaviour lines, the person, one agent.
* In code, an abstraction waits for the second concrete occurrence, and the delivery names the first.

## Exercises

These exercises use the clinic, by conversation with the agent, never by hand.

### Exercise 13.1

Ask the agent which are the first and the second copy behind your milestone 2 lines that make a shared copy.
For a repetition in your code with one copy only, say why it waits.

### Exercise 13.2

Ask the agent to propose one check your `npm run verify` lacks, then ask it the governor question.
Keep the check only if the answer names an error from your project's history (`git log`, `work/done/`).

### Exercise 13.3

For each of the seven items of your clinic's docs/05 §7, say what in your project does its job.

[^useful-notes]: This book's delivery `useful-notes`, whose page records chapter 8's mismatch as the error that justified extending the parity check. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/useful-notes.md>
[^closing-a-milestone-run]: This book's review of the guided project's milestone 1: the findings, the decisions and the queue's diff, from which the two lines are quoted. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/closing-a-milestone-run/README.md>
[^ninjobs]: Ninjobs, a private repository: its ADR-0022, amendment of 2026-09-02, and the page of that delivery, paraphrased; the date is the amendment's.
