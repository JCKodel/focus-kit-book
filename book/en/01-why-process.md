# 1. Why process, when AI writes fast

A coding agent writes code faster than you can read it, and projects still arrive late.
After this chapter you can explain why, and name the three things a minimal process gives the agent: a decision in writing, a limit on scope, and a check before "done".

## Speed moved the bottleneck

Building software has three parts: deciding what to build, writing it, and checking that it works.
An agent makes the writing almost free.
The deciding and the checking stay with you.
Typing is fast.
Deciding and checking are slow.
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
  Work that does not fit one page is two deliveries, and your review stays the size of one page ([chapter 14](14-propose.md)).
* **A check before "done".**
  A command that must pass, and proof that the result works, run before anyone calls the work finished ([chapter 15](15-apply.md)).

The method this book teaches, focus-kit, is built on these three pieces, and Part II teaches it.

## Too much process fails too

A process can cost more than it saves: every document is one more thing to write, read and keep true.
On Ninjobs, my own product, writing the spec became the work; [chapter 3](03-spec-driven.md) counts it and [chapter 9](09-birth-of-focus-kit.md) tells the story.

## What the team gains

The team learns where its time goes.
Experienced developers measured 19% slower with AI while they believed they were 20% faster,[^metr-2025] and teams that adopted more AI delivered a little less and broke a little more.[^dora-2024]
The typing was never the slow part, so the gain lies in the deciding and the checking: a decision written before the build, a scope that fits one page, and a check that must pass before anyone says "done".

## Key points

* An agent speeds up writing code; deciding what to build and checking that it works stay slow, and that is where projects lose time.
* In a controlled trial, experienced developers were slower with AI and believed they were faster.
* Without a process, the agent guesses what you did not decide, grows the scope and declares "done" without proof.
* A minimal process gives the agent a decision in writing, one page per delivery and a check before "done".
* Too much process fails too, when writing the spec becomes the work.

[^metr-2025]: METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", 2025. <https://arxiv.org/abs/2507.09089>
[^dora-2024]: DORA, "Accelerate State of DevOps Report 2024", 2024. <https://dora.dev/research/2024/dora-report/>
