# 23. What agents cost, and where they pay

After this chapter you can read a token count from your host's logs, turn it into a cost per delivery your team can repeat, and say why the page and the documents keep that cost small.
You can also say where an agent pays for itself, where it pays less, and where it does not pay.

## The problem

Ask a team what one delivery cost in agent time, and nobody knows.
The bill arrives once a month, for everyone together, and nothing in it says which work it paid for.
So the decision to use an agent, or to use it more, is a feeling: one person swears by it, another thinks it burns money, and neither can show a number.

## What a host bills

A model reads and writes tokens, the units of text [chapter 2](02-how-agents-see.md) explains: a common word is one token, a long or rare word is a few.
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

The project had 93 finished pages, one per delivery, so each number divided by 93 is the cost of one delivery:

| Per delivery | Arithmetic | Tokens |
|---|---|---:|
| All tokens | 4,009,248,425 / 93 | 43.1 M |
| Output | 13,871,893 / 93 | 149 k |
| Without cache reads | (271,807 + 54,527,957 + 13,871,893) / 93 = 68,671,657 / 93 | 738 k |

Forty-three million tokens reads as a lot, and 98.3% of it is the cheapest kind.
The count sets a baseline: this project, this method, this many tokens per delivery.
It is my choice to compare it with nothing outside: I have no other project measured the same way, and a number from another team, another model or another price table would compare things that do not match.
The next milestone of the same project, counted the same way, is the comparison that means something.

## Why cache reads are counted apart

Each call reads the whole context again, so the cache reads say how much context each call carried.
On Ninjobs that is about 208 thousand tokens of cached context per call on average (3,940,576,768 / 18,945).
Output says how much the agent wrote; cache reads say how much it had to carry to write it.

Counted together, the two hide each other.
A session that grows by one file adds that file to every call after it, so the cost of a long session grows faster than the work done in it.
That is the number the process can move, and output is the number it cannot: the code a delivery needs is the code it needs.
Keep cache reads in their own column, and a change in how the team works shows there first.

## Why the page and the documents keep sessions small

[Chapter 2](02-how-agents-see.md) showed that everything in the context window rides along on every call, and that a long session also gets worse at recalling what is in it.
The method answers with a fresh session per delivery.
`/apply` starts from the rules file, the documents it names and one page, so the context holds what this delivery needs and nothing from the one before.
The page is what makes that possible: it carries every decision the build needs, so the session does not have to inherit the conversation that took them.

So the context stays the size of the delivery, and so does the bill.
A team that keeps one long session for a week pays, on every call of Friday, for the files read on Monday.

## Where an agent pays

**It pays** on work whose decision is written and whose check is mechanical.
The page says what to build, the tests and `verify` say whether it is built, and the agent can loop between writing and checking without a person in the loop.
That is where the tokens buy the most: the person's time goes to reading one page and one staged change.

**It pays less** on work whose decision is still being made.
A `/propose` conversation is cheap in tokens and expensive in the person's time, because the person is the one deciding.
The agent helps there by asking the right questions in order, and the cost to watch is hours of a person, which no token count shows.

**It does not pay** on a stack the agent has seen too little of.
On Ninjobs, before the method, the agent guessed the pixel values of a customised Flutter design that it had few examples to learn from, and screen after screen came close to the design without reaching it.
Each attempt cost tokens and a person's review, and neither bought a finished screen.
Choosing a stack the agent knows is a cost decision as much as a technical one.

## How a team decides

Measure before you argue.
Your host keeps a log of each session on your machine, and the log records the tokens of each call, in the four kinds above.
Count one milestone, divide by the pages it finished, and you have your tokens per delivery.

In Claude Code's logs, one line per event, the same call can appear on more than one line, so the count keeps each message and request only once.
The counting is a pure function ([chapter 5](05-rules-and-exceptions.md)), written for this chapter:

```ts
type Usage = {
	input_tokens: number;
	cache_creation_input_tokens: number;
	cache_read_input_tokens: number;
	output_tokens: number;
};

type LogLine = { requestId?: string; message?: { id?: string; usage?: Usage } };

function countTokens(lines: LogLine[]): Usage {
	const total: Usage = {
		input_tokens: 0,
		cache_creation_input_tokens: 0,
		cache_read_input_tokens: 0,
		output_tokens: 0,
	};
	const seen = new Set<string>();
	for (const line of lines) {
		const usage = line.message?.usage;
		const key = `${line.message?.id}:${line.requestId}`;
		if (!usage || seen.has(key)) continue;
		seen.add(key);
		for (const kind of Object.keys(total) as (keyof Usage)[]) total[kind] += usage[kind] ?? 0;
	}
	return total;
}
```

Count soon after the milestone closes: the host deletes logs older than its retention period, and on Ninjobs the logs before those 21 days had already gone.

Then compare milestones, not vendors.
The second milestone against the first, on the same project, tells you whether the team's way of working got cheaper or dearer; a vendor's price list tells you the price of a token, and nothing about how many your work needs.
When a number moves, the columns say why: output up means more was built, cache reads up means sessions grew.

## What the team gains

A number per delivery that anyone on the team can repeat from the host's logs, in place of a feeling.
On Ninjobs it is 43.1 million tokens per delivery, 149 thousand of them written by the agent and 738 thousand without cache reads, over 93 deliveries.
There is no outside number to set it against, by choice: the team's next milestone is the comparison.

## Key points

* A host bills four kinds of token: input, cache write, cache read and output; a cache read costs a fraction of an input token, because the host re-sends the same context on every call.
* On Ninjobs one delivery cost 43.1 M tokens, 98.3% of them cache reads, 149 k of output and 738 k without cache reads, over 93 pages.
* Cache reads are counted apart because they measure how much context each call carried, and that is what the page and a fresh session per delivery keep small.
* An agent pays where the decision is written and the check is mechanical, pays less where the decision is still being made, and does not pay on a stack it has not seen.
* Measure tokens per delivery on your own project for one milestone, from the host's logs, and compare milestones, not vendors.

[^anthropic-pricing]: Anthropic, "Pricing", Claude Platform documentation, section "Prompt caching", accessed 2026-09-30. <https://docs.anthropic.com/en/docs/about-claude/pricing>
