# How focus-kit was born

On Ninjobs, my own product, I dropped OpenSpec and wrote the process that became focus-kit.
After this chapter you can say why, and which failure each rule of focus-kit answers.

## How it was

Ninjobs started with OpenSpec.
Every feature was a change with its proposal, specs, design and tasks, and every decision was written again in the project's documents and ADRs, the architecture decision records, one file per decision.
Before a delivery counted as done, it had to pass 29 checks.[^ninjobs]
In fifteen days that produced four screens.[^ninjobs]

## What went wrong

The process weighed more than the work it served.
A decision lived in six places that could disagree: the documents, the specs, the changes, the ADRs, an outline and the code.
Every delivery had to keep them in step, and each one could go stale on its own.
The checks were costly to satisfy and cheap to bypass, and not one had ever failed on an error in the product.[^ninjobs]
A leaner OpenSpec would not have helped: the cost was the number of places, not the size of each file.

## Where it went

On 2026-08-29 I restarted the project with a process small enough to hold in your head.[^ninjobs]

* **One page per delivery.** What to build, and what stays out, fits on one page. If it does not fit, it is two deliveries.
* **Deciding and doing in separate sessions.** `/propose` talks and writes the page; `/apply` builds it in a fresh session, with only the page and the documents: a context that grows loses accuracy ([chapter 2](02-how-agents-see.md)), so the build starts clean, from the written target, without the conversation that decided it.
* **The documents hold the facts.** The commands only say which documents to read and what never to do.
* **A queue**, one line per delivery. No formal spec, no archive, no change folder. The outline held each delivery's plan and its reasoning together, so reading the list meant reading everything; the queue keeps one line per delivery, and the page keeps the reasoning.
* **The agent never commits.** It stages the work with `git add`; the person reviews and commits. None of the 29 checks had ever caught an error in the product, so the check that looks at the product is the person's review of each commit.
* **The governor.** Anything that wants to come back answers one question: which concrete error would it have caught?

That process carried Ninjobs to its public opening on 2026-09-10.[^ninjobs]
I then turned it into focus-kit, the kit this book teaches.

One rule came later.
When Ninjobs adopted the kit, its old `/apply` still described things the project had already changed in its documents.[^ninjobs]
So a command holds no fact of the project: every such fact lives in one place, docs/05, the process document, whose "This project" section holds them, and the command reads it there ([chapter 6](06-the-documents.md) describes every document).

## A lesson beyond the process

The restart also changed the stack, from Flutter to React.
The same agent kept missing the design in Flutter and wrote it right in React.
Flutter could build the project; what the agent had seen in training was the limit.
Choose a stack by the project's value and by how well the agent knows it; chapter 7 shows how.

## Key points

* On Ninjobs, OpenSpec produced four screens in fifteen days because each decision lived in six places and 29 checks guarded the form, not the product.
* The fix was fewer places: one page per delivery, documents that hold the facts, and commands that only point at them.
* Deciding and doing happen in separate sessions, and the person commits, never the agent.
* The governor asks every addition which concrete error it would have caught.
* Choose a stack the agent knows.

[^ninjobs]: Ninjobs, a private repository, counted by the author over its history up to 2026-08-29, when its ADR-0022 dropped OpenSpec: days with a commit and commits from `git log`, changes from the OpenSpec archive, lines with `wc -l` over every file under `openspec/`. The screens and the table are the ones that ADR lists. The causes, the rejected alternative and the decision are the ADR's own, paraphrased; the outline that held each plan's reasoning and the clean session with a written target come from the independent reviews that ADR cites, paraphrased too. Its ADR-0026, dated 2026-09-21, gives the date of the public opening and the adoption of focus-kit.
