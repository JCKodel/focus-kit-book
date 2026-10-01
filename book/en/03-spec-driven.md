# Spec-Driven Development

Spec-Driven Development has a coding agent write the decision down before the code, and the tools that practise it can write far more than a feature needs.
After this chapter you can say what Spec-Driven Development is and how far a tool takes the spec, name what Spec Kit and OpenSpec got right, and say where the cost of writing one decision in many places begins.

## The problem

An agent given a task and nothing else decides what you did not, in the middle of the build ([chapter 1](01-why-process.md)).
The first answer is to write the decision before the code, in a file the agent reads.
The second problem arrives with the first answer: every file written is a file someone reviews and keeps true, and a tool can write so much that the spec becomes the work.

## What a spec is

Birgitta Böckeler, of Thoughtworks, compared three tools that call themselves spec-driven and wrote down what the term means.[^bockeler-2025]
A spec, in her definition, is "*a structured, behavior-oriented artifact [...] written in natural language that expresses software functionality and serves as guidance to AI coding agents.*"[^bockeler-2025]
Spec-Driven Development (SDD) "*means writing a “spec” before writing code with AI (“documentation first”). The spec becomes the source of truth for the human and the AI.*"[^bockeler-2025]

> **Note.** Behaviour, here, is what the software does as its user sees it: in this situation, this happens.
> "A member with an overdue book is refused, with the message 'Return your overdue books first'" is behaviour; "add a column to the loans table" is not, it is how.
> Written this way, each line can be checked by a test or by a person, and that is why the page of a focus-kit delivery has a section named Behaviour ([chapter 14](14-propose.md)).

She found three levels, by how long the spec lives and who edits it:

* **spec-first**: a spec is written first and guides the task at hand;
* **spec-anchored**: the spec is kept after the task and used to evolve and maintain the feature;
* **spec-as-source**: the spec is the main source over time, and a person edits only the spec, never the code.

"*All SDD approaches and definitions I've found are spec-first, but not all strive to be spec-anchored or spec-as-source.*"[^bockeler-2025]
Of her three tools, Kiro is "*the simplest (or most lightweight)*" and "*mostly spec-first*", and Tessl is "*the only one of these three tools that explicitly aspires to a spec-anchored approach*".[^bockeler-2025]
She adds that "*these tools are very fast evolving, so they might have already changed since I used them*".[^bockeler-2025]

## Two tools

Spec Kit, from GitHub, is a toolkit of processes for coding agents; its Spec-Driven Development process writes a constitution once per project, then a specification, a plan and a list of tasks for each feature before the code.[^spec-kit]
OpenSpec, from Fission AI, "*adds a lightweight spec layer so you agree on what to build before any code is written*"; its propose command writes one folder per change, with a proposal, specs, a design and tasks.[^openspec]
Both are spec-first by default: the spec is written for the task at hand.

I gave both tools, and focus-kit, the method Part II teaches, the same small feature: a booking may be cancelled up to 24 hours before it starts, and a later cancellation is refused with a message that says why.[^spec-driven-run]
Each stopped before writing code.

## What they got right

**The decision is written before the code, in files the agent reads.**
A decision that lives only in the conversation is lost when the session ends ([chapter 2](02-how-agents-see.md)).
All three tools stopped with the feature decided in files inside the project, where a fresh session finds them.

**Some decisions are written once per project.**
Spec Kit's constitution holds the rules every feature follows, such as "keep it simple" or "every rule has a test", and each feature's plan checks itself against it.[^spec-driven-run]
A rule that holds for the whole project is decided once and not argued again feature by feature.

**The tool asks before it writes.**
OpenSpec read the code before it wrote the change, found that the feature assumed something the code did not have, and stopped with a question: it offered two options, recommended one, and wrote the change only after the answer.[^spec-driven-run]
Spec Kit, on its default path, met the same gap and asked nothing; it wrote its own answer under "Assumptions" in the spec, where you find it only by reading the spec.[^spec-driven-run]
A question costs one turn before the code; a guess costs a review, or a user who meets it.

## Where the cost of many places begins

For the same feature, Spec Kit wrote 8 files and 756 lines.[^spec-driven-run]
OpenSpec wrote 6 files and 180 lines.[^spec-driven-run]
focus-kit wrote 1 page of 82 lines.[^spec-driven-run]
Every one of those files is something a person reviews before the code is written.

The feature holds one rule about time: up to 24 hours before.
Spec Kit restates it in each of its 8 files, OpenSpec in 4 of its 6, focus-kit on its one page.[^spec-driven-run]
The three decide the same thing.
The difference is how many other files say it again: a rule written in 8 places is read 8 times in review, and when it changes, it changes in 8 places, or it disagrees with itself in the ones that were missed.
Böckeler found the same with Spec Kit: its files "*were repetitive, both with each other, and with the code that already existed*", and "*very verbose and tedious to review.*"[^bockeler-2025]

One page is enough because most of what those files repeat, the product, its vocabulary, its rules and the decisions already taken, is the same for every feature.
focus-kit writes that part once per project, in documents kept up to date ([chapter 10](10-the-documents.md)), so the page of a feature holds only what is new about it.
The cost is to write those documents and keep them true; the return is one page per feature, read and reviewed in one sitting, in place of a folder ([chapter 14](14-propose.md)).
The counts say what each tool writes before the code; they do not say which one builds better software, and one feature on one day is not a benchmark.

## What the team gains

One page per feature, instead of one folder per feature, is what the team reads, reviews and keeps true.
On Ninjobs, my own product, fifteen days with OpenSpec produced 37,228 lines of spec for four screens (every line under the tool's folder, counted with `wc -l`), and none of the core flow existed yet.
The causes were more than the tool, and [chapter 9](09-birth-of-focus-kit.md) tells them; the count is what a spec costs when it becomes the work.
After the move to one page per delivery, the product opened to the public, and its 93 finished pages held 22,650 lines in all.

## Key points

* A spec is a written, behaviour-oriented description of what the software must do, in natural language, that guides a coding agent; Spec-Driven Development writes it before the code.
* By how long the spec lives, a tool is spec-first (written for the task), spec-anchored (kept to maintain the feature) or spec-as-source (the only thing a person edits).
* Spec Kit and OpenSpec got three things right: the decision written before the code, project-wide rules written once, and, in OpenSpec, a question asked before writing.
* One rule restated in many files is read many times and changed in many places; for the same feature Spec Kit wrote 8 files, OpenSpec 6, focus-kit 1 page.
* A lighter page per feature is paid for with documents written once per project; the counts show what each tool writes, not which builds better software.

[^bockeler-2025]: Birgitta Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl", 2025. <https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html>
[^spec-kit]: GitHub, "Spec Kit", accessed 2026-09-30. <https://github.com/github/spec-kit>
[^openspec]: Fission AI, "OpenSpec", accessed 2026-09-30. <https://github.com/Fission-AI/OpenSpec>
[^spec-driven-run]: J.C. Ködel, "One Page at a Time", the record of the run of the three tools on one feature, 2026-09, in the book's repository. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/spec-driven-run>
