# Why process, when AI writes fast

A coding agent writes code faster than you can read it, and projects still arrive late.
After this chapter you can explain why, and name the three things a minimal process gives the agent: a decision in writing, a limit on scope, and a check before "done".

## Speed moved the bottleneck

Building software has three parts: deciding what to build, writing it, and checking that it works.
An agent makes the writing almost free.
The deciding and the checking stay with you.
Typing is fast.
Deciding and checking are slow.
When only the writing speeds up, the result is more code waiting for a decision or a review.

In early 2025, METR ran a randomized controlled trial with 16 experienced open-source developers on 246 real tasks, in mature projects they had worked on for 5 years on average.[^metr-2025]
Each task was randomly assigned to allow or forbid AI tools.
Before starting, the developers forecast that AI would cut their completion time by 24%.
After the study, they estimated it had cut the time by 20%.
Measured, AI increased their completion time by 19%.
They were slower, and they believed they were faster.

A survey of teams points the same way.
The 2024 DORA report estimated that for every 25% increase in AI adoption, delivery throughput fell 1.5% and delivery stability fell 7.2%.[^dora-2024]
Its authors point to the basics of delivery, small batches and solid testing, and suspect that changes grow larger when AI lets people produce more code in the same time.[^dora-2024]

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

The method this book teaches, focus-kit, is built on these three pieces.

## Too much process fails too

A process can cost more than it saves: every document is one more thing to write, read and keep true.
On Ninjobs (<https://www-ninjobs-app.translate.goog/?_x_tr_sl=pt&_x_tr_tl=en&_x_tr_hl=en>, through Google Translate: the product is in Brazilian Portuguese only), my own product, fifteen days, 87 commits and 35 OpenSpec changes produced 37,228 lines of spec for four screens and one domain table.[^ninjobs-adr-0022]
Chapter 4 tells that story and how focus-kit came out of it.

## Key points

* An agent speeds up writing code; deciding what to build and checking that it works stay slow, and that is where projects lose time.
* In a controlled trial, experienced developers were slower with AI and believed they were faster.
* Without a process, the agent guesses what you did not decide, grows the scope and declares "done" without proof.
* A minimal process gives the agent a decision in writing, one page per delivery and a check before "done".
* Too much process fails too, when writing the spec becomes the work.

[^metr-2025]: METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", 2025. https://arxiv.org/abs/2507.09089
[^dora-2024]: DORA, "Accelerate State of DevOps Report 2024", 2024. https://dora.dev/research/2024/dora-report/
[^ninjobs-adr-0022]: Ninjobs, a private repository, counted by the author over its history up to 2026-08-29, when its ADR-0022 dropped OpenSpec: days with a commit and commits from `git log`, changes from the OpenSpec archive, lines with `wc -l` over every file under `openspec/`. The screens and the table are the ones that ADR lists.
