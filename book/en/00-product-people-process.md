# Prologue: Product, people and process

A coding agent writes code faster than you can read it, and projects still arrive late.
After this prologue you can say why, what product, people and process each decide when some of the builders are coding agents, and the three things a minimal process gives an agent.

## Speed moved the bottleneck

Building software has three parts: deciding what to build, writing it, and checking that it works.
An agent makes the writing almost free.
The deciding and the checking stay with you.
When only the writing speeds up, the result is more code waiting for a decision or a review.

METR, Model Evaluation and Threat Research, is a research organization that evaluates frontier AI models to inform the public about their capabilities and risks.
In early 2025 it ran a randomized controlled trial, the design medicine uses to test a treatment, with 16 experienced open-source developers on 246 real tasks, in mature projects they had worked on for 5 years on average.[^metr-2025]
Each task was randomly assigned to allow or forbid AI tools.
Before starting, the developers forecast that AI would cut their completion time by 24%.
After the study, they estimated it had cut the time by 20%.
Measured, AI increased their completion time by 19%.
They were slower, and they believed they were faster.

A survey of teams points the same way.
DORA, DevOps Research and Assessment, is the research program, now part of Google Cloud, that surveys software teams every year and publishes the State of DevOps report.
Its 2024 report estimated that for every 25% increase in AI adoption, delivery throughput fell 1.5% and delivery stability fell 7.2%.[^dora-2024]
Its authors point to the basics of delivery, small batches and solid testing, and suspect that changes grow larger when AI lets people produce more code in the same time.[^dora-2024]

## Three P's

Every company rests on three P's, people, process and product, an idea from the businessman Marcus Lemonis,[^lemonis-3ps] and this book puts product first, because the product is what everything else is judged by.

### Product

Many developers turn development itself into the product: the best solution, the best language, the best framework.
Along the way they lose sight of what matters, the product being built.
The code is compiled and its users never see it; only the product exists, and everything is judged by it.
That does not make code irrelevant.
Part I organizes code because a clear structure serves the product and the agent that changes it: architecture is worth what it gives them, and is never an end in itself.
The product itself is written down, in a document that the team and the agent read before they act.

### People

People, and now agents, are the most important part of a company and the most fragile.
Three fragilities repeat.

**Knowledge held by a few.**
When what a project knows lives in a few heads, it leaves when they leave, and it never reaches an agent, which knows nothing at the start of a session.
The answer is documents: what the project knows is written where a person and an agent both read it.

**Opinion in place of evidence.**
"I think" wins a meeting when nobody asks for the source.
The answer is to cite it: every number and every claim carries its source, as every note in this book does.

**Ego.**
The author of a piece of work defends it because it is theirs, whether that author is a colleague, an agent or you.
The answer is a role: the person interprets, guides and validates, and trusts no one blindly, agent or colleague, the author of the code included.
Validating includes asking for more: an agent's first answer is rarely the best it can give, and it does not offer what you did not ask for.

### Process

No software engineering survives without a process: when each person does things their own way, the result is chaos.
A process is followed because each step has a purpose, and the purpose is also the test.
A step that catches no concrete error leaves the process, a rule this book calls the governor, and too much process fails as surely as too little: every document is one more thing to write, read and keep true.
On Ninjobs (<https://www.ninjobs.app>), my own product, writing the spec became the work.

The process this book teaches runs on documents that an agent reads, and that changes who the process serves.
Once the product, its vocabulary, its decisions and its queue are written where the agent reads them, the agent can answer anyone on the team: what is pending, how it is going, who owes an answer, what was agreed with the client.
Feed it the emails and the proposals too, and the project becomes an assistant to the whole team, developers and managers alike.

## What goes wrong without a process

Three failures repeat when you hand an agent a task and nothing else.

**The agent fills gaps with guesses.**
What you did not decide, the agent decides for you, and does not tell you.
Its guesses are plausible, so they look right until a user runs into one.

**Scope grows during the build.**
Asked to fix one thing, the agent also renames, refactors and adds what it thinks comes next.
Each change looks helpful; together they make a change too large to review, and review is the slow part.

**"Done" arrives without proof.**
The agent reports the task finished because it wrote the code.
Whether it builds, whether the tests pass, whether the screen matches the design, is a question the agent asks only when something makes it ask.

All three push work into the slow parts: you decide later, under pressure, and you check more, with less to check against.

## What a minimal process is

A minimal process answers each failure with one piece.

* **A decision in writing.**
  Before the agent builds, what to build is written where the agent reads it.
  There is less to guess, so it guesses less.
* **One page per delivery.**
  The page says what enters and what stays out.
  Work that does not fit one page is two deliveries, and your review stays the size of one page.
* **A check before "done".**
  A command that must pass, and proof that the result works, run before anyone calls the work finished.

The method this book teaches, focus-kit, is built on these three pieces, and Part II teaches it.

## What the team gains

The team learns where its time goes: experienced developers measured 19% slower with AI while they believed they were faster,[^metr-2025] so the gain lies in the deciding and the checking, where the three pieces of a minimal process work.
When the process runs on documents an agent reads, the project answers the whole team, for one developer as for a company, and that is the gain this book is written for.
No study in this book measures a team with the method and its practices against the same team without them: the evidence in each chapter is its number, counted on a real project and saying where it comes from, or the loss its practice avoids.
Ninjobs and Case A, a client project that ran on the process and that chapter 17 tells, live in private repositories, so every number this book gives about them was counted by me over their histories.
Ninjobs appears by name; Case A is a private corporate project, and its name could not be published without authorization, so it appears without its owner, its client or its business.

Part I is the base, the practices every reader must share before the process, from how an agent sees a project to a test for each piece of code.
Part II is the method, focus-kit, from its documents to the project as the team's assistant.
Part III is git and the team's tools.
Part IV is beyond code: projects that are not software, what agents cost, and adoption in a company.
Part V is the person: why an agent's first answer feels final, and how to ask for more.

## Key points

* Every company that builds software rests on three P's: the product, which is what is judged; people and agents, whose fragilities are answered by documents, sources and a person who validates; and a process whose every step has a purpose.
* In a controlled trial, experienced developers were 19% slower with AI and believed they were faster: deciding and checking stay slow, and that is where projects lose time.
* Without a process, the agent guesses what you did not decide, grows the scope and declares "done" without proof.
* A minimal process gives the agent a decision in writing, one page per delivery and a check before "done"; too much process fails too, when writing the spec becomes the work.
* Write each decision where an agent reads it, and ask the project before you ask a colleague.

[^lemonis-3ps]: Marcus Lemonis Business Team, "3 Key To Business Success: People, Process & Product", accessed 2026-09-28. <https://marcuslemonis.com/business/3ps-of-business>
[^metr-2025]: METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", 2025. <https://arxiv.org/abs/2507.09089>
[^dora-2024]: DORA, "Accelerate State of DevOps Report 2024", 2024. <https://dora.dev/research/2024/dora-report/>
