# 22. What agents cost, and where they pay

After this chapter you can read a token count from your host's logs, turn it into a cost per delivery your team can repeat, and say why the page and the documents keep that cost small.
You can also say where an agent pays for itself, where it pays less, and where it does not pay.

## The problem

Ask a team what one delivery cost in agent time, and nobody knows.
The bill arrives once a month, for everyone together, and nothing in it says which work it paid for.
So the decision to use an agent, or to use it more, is a feeling: one person swears by it, another thinks it burns money, and neither can show a number.

## What a host bills

A model reads and writes tokens, the units of text [chapter 1](01-how-agents-see.md) explains: a common word is one token, a long or rare word is a few.
The host, the program you run, bills every call to the model in tokens, and it counts four kinds apart.

* **Input**: new text the model reads for the first time in this call.
* **Cache write**: text the host stores so that later calls can reuse it.
* **Cache read**: stored text a later call reuses.
* **Output**: the text the model writes, its answer and the commands it asks the host to run.

The model remembers nothing between calls, so the host sends the whole context again every time: its own instructions, the rules file, every file read so far and the conversation.
The cache keeps that repeated part, so the next call reads it back at a fraction of the price of new input.
Anthropic's pricing documentation gives the multipliers: a cache write costs 1.25 times a normal input token for a five-minute cache, and a cache read costs a tenth of one or less, depending on the model.[^anthropic-pricing]

## What a delivery cost on Ninjobs

Ninjobs is my own product, built with the method this book teaches.
Claude Code keeps a log of every session, with the tokens of every call, and I counted those logs for the 21 days the host still held, from 221 sessions and 18,945 calls.

| Kind | Tokens in 21 days | Share |
|---|---:|---:|
| Input | 271,807 | 0.01% |
| Cache write | 54,527,957 | 1.4% |
| Cache read | 3,940,576,768 | 98.3% |
| Output | 13,871,893 | 0.3% |
| All | 4,009,248,425 | 100% |

The project had 93 finished pages, one per delivery; each total divided by 93 gives 43.1 million tokens per delivery, 149 thousand of them output and 738 thousand without cache reads.

Forty-three million tokens reads as a lot, and 98.3% of it is the cheapest kind.
The count sets a baseline: this project, this method, this many tokens per delivery.

## Why cache reads are counted apart

Each call reads the whole context again, so the cache reads say how much context each call carried.
On Ninjobs that is about 208 thousand tokens of cached context per call on average (3,940,576,768 / 18,945).
Output says how much the agent wrote; cache reads say how much it had to carry to write it.

Counted together, the two hide each other.
A session that grows by one file adds that file to every call after it, so the cost of a long session grows faster than the work done in it.
That is the number the process can move, and output is the number it cannot: the code a delivery needs is the code it needs.
Keep cache reads in their own column, and a change in how the team works shows there first.

## Why the page and the documents keep sessions small

[Chapter 1](01-how-agents-see.md) showed that everything in the context window rides along on every call, and that a long session also gets worse at recalling what is in it.
The method answers with a fresh session per delivery.
`/apply` starts from the rules file, the documents it names and one page, so the context holds what this delivery needs and nothing from the one before.
The page is what makes that possible: it carries every decision the build needs, so the session does not have to inherit the conversation that took them.
The queue is among those documents, whole, and what it reads at the start rides along on every call of the session; with chapter 11's one-sentence line, that read grows by a sentence per delivery, not by a page.

So the context stays the size of the delivery, and so does the bill.
A team that keeps one long session for a week pays, on every call of Friday, for the files read on Monday.

## Where an agent pays

**It pays** on work whose decision is written and whose check is mechanical.
The page says what to build, the tests and `verify` say whether it is built, and the agent can loop between writing and checking without a person in the loop.
That is where the tokens buy the most: the person's time goes to reading one page and one staged change.

**It pays less** on work whose decision is still being made.
A `/propose` conversation is cheap in tokens and expensive in the person's time, because the person is the one deciding.
The agent helps there by asking the right questions in order, and the cost to watch is hours of a person, which no token count shows.
On Ninjobs everything the agent wrote for a delivery, its page included, averaged 149 thousand output tokens, and the hours I spent deciding those pages are in none of the table's columns.

**It does not pay** on a stack the agent has seen too little of.
On Ninjobs, before the method, that stack was Flutter: each attempt at the design cost tokens and a person's review, and neither bought a finished screen.
Choosing a stack by the questions of chapter 9 is a cost decision as much as a technical one.

## How a team decides

Measure before you argue.
Your host keeps a log of each session on your machine, and the log records the tokens of each call, in the four kinds above.
Count one milestone, divide by the pages it finished, and you have your tokens per delivery.

In Claude Code's logs, one line per event, a streamed answer logs its usage on more than one line, so count each pair of `message.id` and `requestId` once.

Count soon after the milestone closes: the host deletes logs older than its retention period, and on Ninjobs the logs before those 21 days had already gone.

Then compare milestones, not vendors.
The second milestone against the first, on the same project, tells you whether the team's way of working got cheaper or dearer; a vendor's price list tells you the price of a token, and nothing about how many your work needs.
When a number moves, the columns say why: output up means more was built, cache reads up means sessions grew.
That is why I compare Ninjobs with nothing outside: I have no other project measured the same way, and a number from another team, another model or another price table would compare things that do not match.

## What the team gains

A number per delivery that anyone on the team can repeat from the host's logs, in place of a feeling.
On Ninjobs it is 43.1 million tokens per delivery.

## Key points

* A host bills four kinds of token: input, cache write, cache read and output; a cache read costs a fraction of an input token, because the host re-sends the same context on every call.
* Cache reads, nearly all of a delivery's tokens on Ninjobs, are counted apart because they measure how much context each call carried, and that is what the page, a fresh session per delivery and one-sentence queue lines keep small.
* An agent pays where the decision is written and the check is mechanical, pays less where the decision is still being made, and does not pay on a stack it has not seen.
* Measure tokens per delivery on your own project for one milestone, from the host's logs, and compare milestones, not vendors.

[^anthropic-pricing]: Anthropic, "Pricing", Claude Platform documentation, section "Prompt caching", accessed 2026-09-30. <https://docs.anthropic.com/en/docs/about-claude/pricing>
