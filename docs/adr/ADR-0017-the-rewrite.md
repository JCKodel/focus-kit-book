# ADR-0017: the rewrite, base before method, no guided project

**Date:** 2026-09-30

## Context

At eighteen chapters and about 50,000 words, the book read as the log of its own runs: briefs, transcripts, diffs, `git status`, commit hashes and headless flags filled about half of every method chapter, and the guided project's runs were the thread of Part II.
The author's judgement: it did not teach, it showed no value, and nobody would read it to the end.
The engineering practices the method rests on (simplicity, pure functions, exceptions as values, vertical slices, the four pieces, a test per piece) came after the process, in Part III, and Part II used them untaught.
The book's purpose is a set of proven practices a whole team can run, for readers of any level: first a shared base with evidence, then the method, then the proof of what the team gains.

## Decision

* **Order.** Part I is the base: why process, how an agent sees, Spec-Driven Development, then the practices every reader must share, KISS, YAGNI and DRY, rules as pure functions and exceptions as values, features instead of layers with dependencies only where a fake exists, FOCUS's four pieces, a test for each piece. Part II is the method. Part III is git and the team's tools. Part IV is beyond code.
* **No runs in the text.** No chapter narrates a run. A real number or a real artifact appears where it proves a point, with its source, and the record of how it was counted stays in `work/done/`.
* **No guided project, no brownfield project, no exercises.** The clinic and the frozen fork leave the book. The tags already published stay where they are and are not cited. Code examples are TypeScript written for the chapter, short, on one running example (a lending library), and the book says once that they are written for it. This supersedes the guided project of ADR-0008 and the brownfield project of ADR-0009 as parts of the book; ADR-0008's choice of TypeScript stands.
* **Evidence.** Every number and every quoted artifact (a page, a queue line, a rules file, a command's output) stays real and sourced. "Every artifact shown is real" now reads: every number and quoted artifact is real and sourced; code examples are illustrative and said so.
* **A gain per chapter.** Every chapter has a section `## What the team gains` (pt: `## O que o time ganha`) before its key points, with a number or a sourced claim, or one sentence saying the gain has no number.
* **Cases.** Ninjobs is the process case, by name, through its artifacts and counted numbers. Case A ran on the process and is the team case. Case B did not run on the process: it is a consultancy's proposal for a client's adoption program, used as the shape of a pitch and as the contrast of findings that had no queue to carry them. No chapter implies otherwise.
* **The project as the team's assistant** is the book's promise, stated in the prologue and taught right after the method (chapter 18), because it is the gain the book is written for.
* **One delivery.** The author chose to rewrite the whole book in one delivery, `rewrite`, against the one-page rule, to judge the new book whole; the page records it.

## Consequences

docs/00 gets the new contents and reworded values; docs/03 retires the guided project's terms and gains the new ones; docs/04 changes the chapter shape (a gain section, no exercises) and the code rule; docs/05 §5 retires the guided and brownfield projects; docs/06 gets M8 and marks the lines the rewrite absorbed; AGENTS.md follows.
The appendices of M7 are planned again after the author reads the new book.
Chapter files are renumbered in both editions; the site's navigation follows the file names.

## Amendment, 2026-10-02 (ask-for-more-chapter)

The book gains Part V, "The person decides", after Part IV, with one chapter, 25 "Asking for more": why an agent's first answer feels final, what an agent does not propose unasked, and the challenge protocol, with this book's experiment and the studies as the team's gain.
It stands apart from Part IV because its subject is the person's role from the prologue, not a use of the method beyond code, and every audience of docs/00 reads it.
The prologue names it where it asks the person to trust no one blindly, and its parts map gains a line for Part V.
