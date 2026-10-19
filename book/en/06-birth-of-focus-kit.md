# 6. How focus-kit was born

On Ninjobs, my own product, I dropped OpenSpec after fifteen days and wrote the process that became focus-kit.
After this chapter you can tell that story, how it was, what went wrong and where it went, and name the failure each rule of focus-kit answers.

## How it was

Ninjobs started with OpenSpec, one of the Spec-Driven Development tools of chapter 2.
Every feature was a change, a folder with its proposal, its specs, its design and its tasks, and every decision was written again in the project's documents and in its ADRs, the architecture decision records, one file per decision.
Before a delivery counted as done, it had to pass 29 checks.

In fifteen days that produced 37,228 lines of spec, for four screens and one table of data.
None of the product's core flow existed yet.

## What went wrong

When I stopped, the decision record I wrote named five causes, and four independent reviews of the project had reached the same diagnosis.

1. **Slow visual feedback.**
   The app was in Flutter, and four changes in a row went only to getting the screens close to the design.
2. **A stack the agent had seen little of.**
   The design customized Material 3, Google's design system, which Flutter implements, and the agent had seen few examples of that in training, so it guessed pixel values.
3. **Eight files to show one field.**
   I required the full form of FOCUS, the four pieces of chapter 4, on every feature, a trivial form included.
   The architecture was sound; I had lost KISS and YAGNI, the two principles of chapter 3 that decide when a piece pays its way, and let complexity grow.
4. **Checks that guarded the form.**
   The 29 checks were costly to satisfy and cheap to get around, and not one had ever failed on an error in the product.
   A check that never caught a product error is ceremony.
5. **Six places for one truth.**
   A decision lived in the documents, the specs, the changes, the ADRs, an outline of the work and the code, and each could go stale on its own.
   Every delivery had to keep all six in step.

A leaner OpenSpec would not have helped.
The cost was the number of places, not the size of each file.

## Where it went

On 2026-08-29 I started over, with a process small enough to hold in my head, and moved the app from Flutter to React, where the same agent got the design right.
The code kept the two principles of FOCUS, vertical slices and exceptions as values, and stopped requiring the four pieces on every feature.
One delivery became one page, `work/<slug>.md`.
Ninjobs' own two commands did the work: `/propose` talks with me and writes the page, never code; `/apply` builds the page, verifies it and compares the screen against the design.
The queue became one line per delivery.
Of the 29 checks, two stayed, both aimed at the product itself: a proof of what each privacy level of a profile may show, and a test of the database's access rules.
Anything that wanted to come back had to answer one question, the governor: which concrete error would it have caught?
One check did come back later, because it named an error that had happened.

Ninjobs opened to the public on 2026-09-10, thirteen days after the restart, with 91 one-page deliveries done, every one on those two commands.
Its finished queue lines cite 19 design boards, against four screens in the fifteen days before.

On 2026-09-21, after the opening, I pulled the process out of Ninjobs into focus-kit, the kit this book teaches, and planted the kit back in Ninjobs.
The numbers in this chapter come from before that day, none of them from the kit.
The trigger was a drift: the project's own command files still described steps its process document, docs/05, had already changed.
From then on the commands hold no fact of the project, and read every one of them in docs/05.

## Each rule and its failure

The kit keeps six rules in every project, the ones its `SETUP.md` lists in §2, and every rule exists because something failed without it.
Any other check is the project's own.

* **One delivery is one page.**
  It answers the change folder, a proposal, specs, a design and tasks for one feature: what to build and what stays out live on one page, and a scope that does not fit is two deliveries (chapter 12).
* **Deciding and doing in separate sessions.**
  It answers the build that decides as it goes: `/apply` starts clean, with the page and the documents, without the long conversation that decided it, since a context that grows loses accuracy; `/propose` writes no code and `/apply` widens no scope.
* **The agent stages and suggests the commit message.**
  The agent never commits or merges on its own; asked, it takes the step the person names.
  It answers the 29 checks that never looked at the product: the check that does is a person reading each change before it enters the history (chapter 13).
* **Project specifics are slots in the project's docs/05.**
  The verify command, the environments, the proof and the git strategy are filled once there, and `/apply` reads them.
  It answers the drift: a command that repeats a fact of the project goes stale when the document changes, so the command only says which slot to read (chapter 7).
* **Documents are living.**
  A delivery that changes a behaviour updates the document that owns it, in the same delivery.
  It answers the six places: each fact has one owner, and the delivery that changes the fact changes the owner, so no copy goes stale on its own (chapter 7).
* **Nothing enters without naming the concrete error it would have caught.**
  It answers the growth of the checks, each plausible on its own and all of them together heavier than the work (chapter 16).

The queue of one line per delivery serves these rules without being one of them.
It answers the outline, which held each delivery's plan and its reasoning together, so reading the list meant reading everything; the line says what, and the page keeps the reasoning (chapter 11).

## What the team gains

A process that carries a product instead of weighing on it.
Before, the old process gave Ninjobs four screens in fifteen days, with every decision repeated in many places and checks that never caught a product error.
After, one page per delivery gave the public opening in thirteen days, with each fact in one place and two checks aimed at the product.

## Key points

* The cost was the number of places, not the size of each file; the architecture was sound, and I lost KISS and YAGNI by requiring its full form on every feature.
* Start from the least that held on Ninjobs: one page per delivery, two commands, one queue line per delivery, two checks and the governor's question.
* Each of the kit's six rules answers a failure: a feature spread over a folder of files, a build that decides as it goes, checks blind to the product, commands that drift, a decision kept in many places, and checks that grew unasked; every other check is the project's own.

