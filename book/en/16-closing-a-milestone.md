# Closing a milestone

After this chapter you can close a milestone: check its paragraph on the running product, review everything it built with what your host offers, and decide each finding.
You can then turn each confirmed finding into a line in a new milestone, `<M>.1`, instead of a fix.

## The problem

Each page of a milestone was read before `/apply` built it, and each staged change was reviewed before its commit.
Nobody looked at what they add up to.
A light process has no gate between deliveries, so the risk it carries is the sum: every delivery right on its own page, and the whole still wrong.
A query that was fast on the first page's data and slow once five deliveries fill the tables, a helper copied into four features, a claim of the milestone that no delivery took on: none of them fails a single delivery's review.

## The review is a delivery

The kit closes that gap in one rule, §8 of the process document it writes, docs/05.
The last line of every milestone is its review, `<milestone>-review`, a delivery like the others: `/propose` writes its page, and `/apply` runs it.
The page names what to look at: the milestone's range of commits, its paragraph, and the review command of the host with its level.
The run checks the paragraph clause by clause against what the deliveries built, reviews the code, and fixes nothing.
Each problem it reports is a finding, and the decision on each one is yours.

## Check the paragraph

A milestone ends with a paragraph written as a test a person can check against the product (chapter 13).
For a milestone of the lending library, written for this chapter:

```
When it closes, a librarian can lend a copy and record its return, and a
member sees their loans with the due date of each.
```

Check it on the running product, clause by clause, end to end, once, in the order a librarian and a member would meet them: lend a copy, record its return, open the member's loans and read the due dates.
Each delivery's check tested its own part; this one runs them together, as the product is used.
A clause that does not hold is a finding like any other, and so is a clause no delivery answered.

## Review everything the milestone built

Then review the code of the whole milestone, with what your host offers.
In Claude Code the review is `/code-review`; it takes a target, such as a branch or a range of commits, and a level that trades confidence for coverage: `low` and `medium` report only the findings it is most sure of, and `high` through `max` broaden coverage and may include findings it is less sure of.[^claude-code-review]
For a milestone, the range starts at the last commit before it and ends at its last:

```
/code-review high <commit before the milestone>...<last commit of the milestone>
```

A milestone is reviewed once, as a whole, so breadth is worth more there than certainty, and the decisions below filter out what is uncertain.
The review only reports; it changes your files only when you ask it to fix, and here you do not.[^claude-code-review]

Other hosts offer the same look.
Codex has `/review` in a session and `codex review --base <branch>` in the terminal, which review the changes against a base branch.[^codex-review]
GitHub Copilot reviews pull requests, so there the milestone goes up as one pull request from its first commit to its last.[^copilot-review]

## Decide each finding

A finding reads like a fact, and some are not.
The person is the brain of the operation (chapter 10): you check what the agent writes against what you know, and a review is the agent writing.
That means two things: you never take a finding as true without looking at the code, and you never drop one without saying why.

So each finding is confirmed or rejected, with a reason.
A rejection names what the review did not weigh: a choice a document records on purpose, an order another document fixes, a test that already guards the case, a scale the product will not reach.
A confirmation is checked in the code first.
One finding can split: a duplicated function confirmed, a slow query next to it rejected because the table holds a handful of rows.

## A line, and not a fix

Each confirmed finding becomes a `[ ]` line in a new milestone placed right after the reviewed one, numbered with `.1`: milestone 1 is followed by milestone 1.1, with its own paragraph, so nothing renumbers.
Each line says what will be true, never how to fix it, and a line about copied code names the first copy, as the second-occurrence rule asks (chapter 4).
Each one is a delivery: `/propose` will write its page and `/apply` will build it.
No confirmed finding, no new milestone.

A line, and not a fix, because a fix made in the middle of the next milestone has no page and no review.
Nobody reads its scope before it is built, nobody checks it against a page afterwards, and it lands in a milestone whose paragraph does not mention it.
As a line it waits its turn, and gets both.

Make the `.1` the last round, with no review of its own.
The kit's file lets a `.1` end with its own review, which may open a `.2`; I stopped allowing that, because a review of the fixes finds findings of its own, and a review of those finds more.
One round keeps the review a step with an end.
The `.1` closes when its lines are `[x]` with their proof, and whatever it missed is found by the review of the next milestone.

## When the findings became one delivery

On Ninjobs the review at the public opening returned eight findings, with the whole test suite green.
Queries took hundreds of milliseconds, a large job posting would have timed out, and three of the findings were about security.
Every delivery had passed its own tests and its own review; only the look at the whole saw them.

I put all eight into one delivery instead of eight lines.
Its page says, in its own words, that it does not fit a page and that it breaks the rule on purpose, and it ran to 879 lines, the longest page of the project.
The fixes held: the page measured job triage at about 620 ms on the development database when the work began, and at 94 ms when it ended.
But when I checked the result myself, I found faults its tests had not caught.
The process was not the cause; my choice was.
Eight lines would have been eight pages, each small enough to read before it was built and to check after.

## What the team gains

The milestone review catches the faults the tests do not reach, before users do.
On Ninjobs it found eight with every test green, three of them about security, on the day the product opened to the public.
And because each finding becomes a line, the team sees the cost of the milestone's gaps in the queue, next to everything else it plans, instead of in fixes nobody reviewed.

## Key points

* A milestone review looks at what the deliveries add up to, which no review of a single page or staged change can see.
* The review is the milestone's last line, `<milestone>-review`, run with `/propose` and `/apply`: it checks the paragraph clause by clause on the running product, reviews the milestone's range with what your host offers, and fixes nothing.
* Decide each finding with its reason, after looking at the code: never trust one blindly, never drop one without a reason.
* A confirmed finding becomes a `[ ]` line in a new milestone `<M>.1` right after the reviewed one, never a fix in the middle of the next milestone.
* A `.1` is the last round and has no review of its own; the next milestone's review finds what it missed.

[^claude-code-review]: Anthropic, "Code Review", Claude Code documentation, accessed 2026-09-28. <https://code.claude.com/docs/en/code-review>
[^codex-review]: OpenAI, "Developer commands", accessed 2026-09-28. <https://learn.chatgpt.com/docs/developer-commands?surface=cli>
[^copilot-review]: GitHub, "About GitHub Copilot code review", accessed 2026-09-28. <https://docs.github.com/en/copilot/concepts/agents/code-review>
