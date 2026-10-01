# How focus-kit was born

On Ninjobs, my own product, I dropped OpenSpec after fifteen days and wrote the process that became focus-kit.
After this chapter you can tell that story, how it was, what went wrong and where it went, and name the failure each rule of focus-kit answers.

## How it was

Ninjobs started with OpenSpec, one of the Spec-Driven Development tools of chapter 3.
Every feature was a change, a folder with its proposal, its specs, its design and its tasks, and every decision was written again in the project's documents and in its ADRs, the architecture decision records, one file per decision (chapter 10).
Before a delivery counted as done, it had to pass 29 checks.

In fifteen days that produced 87 commits, 35 changes and 37,228 lines of spec, for four screens and one table of data.
None of the product's core flow existed yet.

## What went wrong

When I stopped, the decision record I wrote named five causes, and four independent reviews of the project had reached the same diagnosis.

1. **Slow visual feedback.**
   The app was in Flutter, and four changes in a row went only to getting the screens close to the design.
2. **A stack the agent had seen little of.**
   The design customized Material 3, Google's design system, which Flutter implements, and the agent had seen few examples of that in training, so it guessed pixel values.
3. **Eight files to show one field.**
   I required the full form of FOCUS, the four pieces of chapter 7, on every feature, a trivial form included.
   The architecture was sound; I had lost KISS and YAGNI, the two principles of chapter 4 that decide when a piece pays its way, and let complexity grow.
4. **Checks that guarded the form.**
   The 29 checks were costly to satisfy and cheap to get around, and not one had ever failed on an error in the product.
   A check that never caught a product error is ceremony.
5. **Six places for one truth.**
   A decision lived in the documents, the specs, the changes, the ADRs, an outline of the work and the code, and each could go stale on its own.
   Every delivery had to keep all six in step.

A leaner OpenSpec would not have helped.
The cost was the number of places, not the size of each file.

## Where it went

On 2026-08-29 I started over, with a process small enough to hold in my head, and moved the app from Flutter to React.
One delivery became one page, `work/<slug>.md`.
Two commands did the work: `/propose` talks with me and writes the page, never code; `/apply` builds the page, verifies it and compares the screen against the design.
The queue became one line per delivery.
Of the 29 checks, two stayed, both aimed at the product itself: a proof of what each privacy level of a profile may show, and a test of the database's access rules.
Anything that wanted to come back had to answer one question, the governor of chapter 17: which concrete error would it have caught?
One did come back later, a lint of the database, because it named one: a duplicate index that no test had noticed.

Ninjobs opened to the public on 2026-09-10, thirteen days after the restart, with 91 one-page deliveries done.
Its finished queue lines cite 19 design boards, against four screens in the fifteen days before.

On 2026-09-21 I pulled the process out of Ninjobs into focus-kit, the kit this book teaches.
The trigger was a drift: the project's own command files still described steps its process document, docs/05, had already changed.
From then on the commands hold no fact of the project, and read every one of them in docs/05.

## Each rule and its failure

Every rule of focus-kit exists because something failed without it.

* **One page per delivery.**
  It answers the six places: what to build and what stays out live on one page, and a scope that does not fit is two deliveries (chapter 14).
* **Deciding and doing in separate sessions.**
  It answers the build that decides as it goes: `/apply` starts clean, with the page and the documents, without the long conversation that decided it, since a context that grows loses accuracy (chapter 2).
* **The documents hold the facts; the commands hold none.**
  It answers the drift: a command that repeats a fact of the project goes stale when the document changes, so it only says which documents to read (chapter 10).
* **A queue of one line per delivery.**
  It answers the outline, which held each delivery's plan and its reasoning together, so reading the list meant reading everything; the line says what, and the page keeps the reasoning (chapter 13).
* **The agent stages and the person commits.**
  It answers the 29 checks that never looked at the product: the check that does is a person reading each change before it enters the history (chapter 15).
* **Nothing enters without naming the error it would have caught.**
  It answers the growth of the checks, each plausible on its own and all of them together heavier than the work (chapter 17).

## Pick a stack the agent knows well

The restart taught one lesson beyond the process.
In Flutter the same agent kept missing the design; in React it wrote it right.
Flutter could build the product, and what the agent had seen in training was the limit, so I choose a stack by the product's needs and by how well the agent knows it (chapter 12).

## What the team gains

A process that carries a product instead of weighing on it.
Before, fifteen days on Ninjobs gave four screens and 37,228 lines of spec, with every decision in six places and 29 checks that never caught a product error.
After, thirteen days gave the public opening, 91 deliveries of one page each and 19 design boards delivered, with each fact in one place and two checks aimed at the product.

## Key points

* On Ninjobs, OpenSpec gave four screens in fifteen days: each decision lived in six places, and 29 checks guarded the form and never the product.
* The cost was the number of places, not the size of each file; the architecture was sound, and I lost KISS and YAGNI by requiring its full form on every feature.
* The restart kept one page per delivery, two commands, one queue line per delivery, two checks and the governor's question, and reached the public opening thirteen days later.
* Each rule of the kit answers a failure: six places, a build that decides as it goes, commands that drift, an outline that mixed plan and reasoning, checks blind to the product, and checks that grew unasked.
* Choose a stack by the product and by how well the agent knows it.

