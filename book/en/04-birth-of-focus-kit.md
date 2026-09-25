# How focus-kit was born

On Ninjobs, my own product, I dropped OpenSpec and wrote the process that became focus-kit.
After this chapter you can say why, and which failure each rule of focus-kit answers.

## How it was

Ninjobs started with OpenSpec.
Every feature was a change with its proposal, specs, design and tasks, and every decision was written again in the project's documents and ADRs.
Before a delivery counted as done, it had to pass 29 checks.[^ninjobs-adr-0022]
In fifteen days that produced four screens.[^ninjobs-adr-0022]

## What went wrong

The process weighed more than the work it served.
A decision lived in six places that could disagree: the documents, the specs, the changes, the ADRs, an outline and the code.
Every delivery had to keep them in step, and each one could go stale on its own.
The checks were costly to satisfy and cheap to bypass, and not one had ever failed on an error in the product.[^ninjobs-adr-0022]
A leaner OpenSpec would not have helped: the cost was the number of places, not the size of each file.

## Where it went

On 2026-08-29 I restarted the project with a process small enough to hold in your head.[^ninjobs-adr-0022]

* **One page per delivery.** What to build, and what stays out, fits on one page. If it does not fit, it is two deliveries.
* **Deciding and doing in separate sessions.** `/propose` talks and writes the page; `/apply` builds it in a fresh session, with only the page and the documents.
* **The documents hold the facts.** The commands only say which documents to read and what never to do.
* **A queue**, one line per delivery. No formal spec, no archive, no change folder.
* **The agent never commits.** It stages the work; the person reviews and commits.
* **The governor.** Anything that wants to come back answers one question: which concrete error would it have caught?

That process carried Ninjobs to its public opening on 2026-09-10.[^ninjobs-adr-0026]
I then turned it into focus-kit, the kit this book teaches.

One rule came later.
When Ninjobs adopted the kit, its old `/apply` still described things the project had already changed in its documents.[^ninjobs-adr-0026]
So a command holds no fact of the project: every such fact lives in one place, docs/05, and the command reads it there.

## Two lessons beyond the process

The restart also changed the stack, from Flutter to React.
The same agent kept missing the design in Flutter and wrote it right in React.
Flutter could build the project; what the agent had seen in training was the limit.
Choose a stack by the project's value and by how well the agent knows it; chapter 7 shows how.

Ninjobs was built with FOCUS, the architecture of Part III, applied whole to every feature: showing one field took eight files.[^ninjobs-adr-0022]
FOCUS stayed useful; applied everywhere it cost more than it gave.
Chapters 14 and 15 say where it pays.

## Key points

* On Ninjobs, OpenSpec produced four screens in fifteen days because each decision lived in six places and 29 checks guarded the form, not the product.
* The fix was fewer places: one page per delivery, documents that hold the facts, and commands that only point at them.
* Deciding and doing happen in separate sessions, and the person commits, never the agent.
* The governor asks every addition which concrete error it would have caught.
* Choose a stack the agent knows, and apply an architecture only where it pays.

[^ninjobs-adr-0022]: Ninjobs, a private repository, counted by the author over its history up to 2026-08-29, when its ADR-0022 dropped OpenSpec: days with a commit and commits from `git log`, changes from the OpenSpec archive, lines with `wc -l` over every file under `openspec/`. The screens and the table are the ones that ADR lists. The causes, the rejected alternative and the decision are the ADR's own, paraphrased.
[^ninjobs-adr-0026]: Ninjobs, a private repository, its ADR-0026, dated 2026-09-21: the date of the public opening and the adoption of focus-kit.
