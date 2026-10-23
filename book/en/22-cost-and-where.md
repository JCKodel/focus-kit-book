# 22. What agents cost, and where they pay

After this chapter you can read a token count from your host's logs, measure what one milestone's deliveries cost with a window and a set of sessions written down so your team can repeat the count, and say what a fresh session carries into its context and what it leaves out.
You can also say where an agent pays for itself, where it pays less, and where it does not pay.
And you can say why the first call after a long pause can cost many times the call before it, and set how long the cache lasts.

## The problem

Ask a team what one delivery cost in agent time, and nobody knows.
The bill arrives once a month, for everyone together, and nothing in it says which work it paid for.
So the decision to use an agent, or to use it more, is a feeling: one person swears by it, another thinks it burns money, and neither can show a number.

## What a host bills

A model reads and writes tokens, the units of text [chapter 1](01-how-agents-see.md) explains: a common word is one token, a long or rare word is a few.
The host, the program you run, bills every call to the model in tokens, and it counts four kinds apart.

* **Input**: new text the model reads for the first time in this call.
* **Cache write**: text kept where the model runs, at the host's request, so that later calls can reuse it.
* **Cache read**: stored text a later call reuses.
* **Output**: the text the model writes, its answer and the commands it asks the host to run.

The model remembers nothing between calls, so the host sends the whole context again every time: its own instructions, the rules file, every file read so far and the conversation.
The cache keeps that repeated part, so the next call reads it back at a fraction of the price of new input.
Anthropic's pricing documentation gives the multipliers: a cache write costs 1.25 times a normal input token for a five-minute cache and 2 times for a one-hour cache, and a cache read costs a tenth of one or less, depending on the model.[^anthropic-pricing]

## How long the cache lasts

The host sends the context, but the cache is kept where the model runs, not on your machine: on Anthropic's infrastructure with a Claude subscription or an API key, or on the cloud provider's when you reach the model through one.[^claude-code-prompt-caching]
That infrastructure keeps a stored context only for a while, the cache lifetime: five minutes or one hour,[^anthropic-pricing] which the host chooses for each request.[^claude-code-prompt-caching]
Every call that reads the cache renews that lifetime, so the cache stays while the conversation keeps working.[^claude-code-prompt-caching]
The lifetime counts from the start of the call that wrote or read the cache, not from the end of its answer: an answer that takes 4 minutes to stream leaves about 1 minute of a five-minute cache for the next call.[^anthropic-prompt-caching]

A pause past the lifetime has a price.
The next call finds no cache, so the whole context the host sends is written again, at the write price instead of the read price.[^claude-code-prompt-caching]
A write costs 1.25 times an input token for a five-minute cache or 2 times for a one-hour cache, and a read 0.1 times, or 0.05 or 0.025 times on the models the pricing page names.[^anthropic-pricing]
Divide the write by the read, and the context of that first call after the pause costs 12.5 times what it cost on the call before it at the least (1.25 / 0.1) and 80 times at the most (2 / 0.025).
The new text the call adds and the answer it writes cost what they cost on any call; the jump is in the context, which on a long session is most of what a call sends.

Claude Code chooses the lifetime per request, in two groups.[^claude-code-prompt-caching]
The main conversation, the one you type in, gets one hour on a Claude subscription while you are within the plan's usage, and five minutes with an API key, through a cloud provider, or once the plan draws on its usage credits.
Subagents and most other requests outside the main conversation get five minutes.

Two settings change it, from Claude Code v2.1.242: `promptCacheTtl` for the main conversation and `subagentPromptCacheTtl` for the rest, each set to `5m` or `1h`; Claude Code ignores any other value.[^claude-code-prompt-caching]
The hour pays when you leave a session idle and come back to it, because the next call reads the context instead of writing it again.
It costs more on short bursts of work that never pause past five minutes, where every write pays 2 times instead of 1.25 and the longer lifetime is never used.

## What Ninjobs recorded in tokens

Ninjobs is my own product, built with the method this book teaches.
Claude Code keeps a log of every session, with the tokens of every call, and I once counted those logs over the 21 days the host still held: 221 sessions and 18,945 calls.

| Kind | Tokens in 21 days | Share |
|---|---:|---:|
| Input | 271,807 | 0.01% |
| Cache write | 54,527,957 | 1.4% |
| Cache read | 3,940,576,768 | 98.3% |
| Output | 13,871,893 | 0.3% |
| All | 4,009,248,425 | 100% |

Those 21 days are the limit of the count.
Their dates, and the rule that decided which sessions it took in, were not written down with it, and the logs it read are gone.
The commits cannot rebuild them: a commit records what changed, not the calls to the model that changed it.
So no list survives of the deliveries those 221 sessions worked on, and the table cannot be divided into a cost per delivery; dividing it by a page count taken from another window would mix two samples.

What the table does say is how that sample's tokens split among the four kinds: 98.3% of them were cache reads, the cheapest kind.

## Why cache reads are counted apart

Each call reads the whole context again, so the cache reads say how much context each call carried.
In that sample it is about 208 thousand tokens of cached context per call on average (3,940,576,768 / 18,945).
Output says how much the agent wrote; cache reads say how much it had to carry to write it.

Counted together, the two hide each other.
A session that grows by one file adds that file to every call after it, so the cost of a long session grows faster than the work done in it.
That is the number the process can move, and output is the number it cannot: the code a delivery needs is the code it needs.
Keep cache reads in their own column, and a change in how the team works shows there first.

## What a fresh session carries

[Chapter 1](01-how-agents-see.md) showed that everything in the context window rides along on every call, and that a long session also gets worse at recalling what is in it.
The method answers with a fresh session per delivery.
`/apply` starts from the rules file, the documents it names and one page, so the context holds none of the conversation of the delivery before.
The page is what makes that possible: it carries every decision the build needs, so the session does not have to inherit the conversation that took them.
The queue is among those documents, and a session reads it whole, done lines included, so what it reads at the start grows with the project's history and rides along on every call of the session.
Chapter 11's one-sentence line makes that growth a sentence per delivery, not a page, but it does not stop it.

So a fresh session's context is one page plus documents that grow with the project, and both the context and the bill grow with that history as well as with the delivery.
What the fresh session removes is the conversation of the deliveries before: a team that keeps one long session for a week pays, on every call of Friday, for the files read on Monday.

## Where an agent pays

**It pays** on work whose decision is written and whose check is mechanical.
The page says what to build, the tests and `verify` say whether it is built, and the agent can loop between writing and checking without a person in the loop.
That is where the tokens buy the most: the person's time goes to reading one page, using what was built and reading one staged change.

**It pays less** on work whose decision is still being made.
A `/propose` conversation is cheap in tokens and expensive in the person's time, because the person is the one deciding.
The agent helps there by asking the right questions in order, and the cost to watch is hours of a person, which no token count shows.
On Ninjobs the table counts tokens only, and the hours I spent deciding the pages are in none of its columns.

**It does not pay** on a stack the agent has seen too little of.
On Ninjobs, before the method, that stack was Flutter: each attempt at the design cost tokens and a person's review, and neither bought a finished screen.
Choosing a stack by the questions of chapter 9 is a cost decision as much as a technical one.

## How a team decides

Measure before you argue.
Your host keeps a log of each session on your machine, and the log records the tokens of each call, in the four kinds above.
Before you divide one milestone's tokens by its deliveries, write down what you counted, so that someone else can count it again and get the same number:

* the window: the first and the last moment counted, and the time zone the log writes them in;
* the sessions and calls in that window that worked on the milestone, proposals, retries and sessions shared with other work included, and the rule that chose them;
* the deliveries those same sessions finished;
* the work in the window that matches no delivery, counted on its own line.

Divide the tokens of the calls that worked on those deliveries by those deliveries, and you have your tokens per delivery for that milestone.
The line that matches no delivery is reported beside it, never divided by a page count from another window.

In Claude Code's logs, one line per event, a streamed answer logs its usage on more than one line, so count each pair of `message.id` and `requestId` once.

Count soon after the milestone closes: the host deletes logs older than its retention period, and on Ninjobs the logs before those 21 days had already gone, and the logs of those 21 days have gone since, so the table cannot be counted again.

Then compare milestones, not vendors.
The second milestone against the first, on the same project, tells you whether the team's way of working got cheaper or dearer; a vendor's price list tells you the price of a token, and nothing about how many your work needs.
When a number moves, the columns say why: output up means more was built, cache reads up means sessions grew, cache writes up means the cache was rebuilt, by pauses past its lifetime or by new sessions.
That is why I compare Ninjobs with nothing outside: I have no other project measured the same way, and a number from another team, another model or another price table would compare things that do not match.

## What the team gains

A number per delivery that anyone on the team can repeat from the host's logs, because its window, its sessions and its deliveries are written down, in place of a feeling.
In the sample Ninjobs recorded, 98.3% of the tokens were cache reads, the column the way a team works can move.
The team also knows what a pause past the cache lifetime costs, from Anthropic's price multipliers, and sets the lifetime to how it works.[^anthropic-pricing]

## Key points

* A host bills four kinds of token: input, cache write, cache read and output; a cache read costs a fraction of an input token, because the host re-sends the same context on every call.
* Count cache reads apart, because they measure the context each call carried: a fresh session per delivery leaves earlier conversations out of it, and the queue, read whole, still adds a sentence per delivery to it.
* An agent pays where the decision is written and the check is mechanical, pays less where the decision is still being made, and does not pay on a stack it has not seen.
* Measure tokens per delivery on your own project for one milestone, from the host's logs, with its window, sessions and deliveries written down and unmatched work on its own line, and compare milestones, not vendors.
* Keep the cache in use: every read renews it, and a pause past its lifetime makes the next call write the whole context again at the write price; Claude Code gives the main conversation an hour on a subscription within its usage and five minutes otherwise, and `promptCacheTtl` changes it.

[^anthropic-pricing]: Anthropic, "Pricing", Claude Platform documentation, section "Prompt caching", accessed 2026-10-22. <https://platform.claude.com/docs/en/about-claude/pricing>
[^claude-code-prompt-caching]: Anthropic, "How Claude Code uses prompt caching", Claude Code documentation, sections "Where the cache lives" and "Cache lifetime", accessed 2026-10-23. <https://code.claude.com/docs/en/prompt-caching>
[^anthropic-prompt-caching]: Anthropic, "Prompt caching", Claude Platform documentation, section "How prompt caching works", accessed 2026-10-22. <https://platform.claude.com/docs/en/build-with-claude/prompt-caching>
