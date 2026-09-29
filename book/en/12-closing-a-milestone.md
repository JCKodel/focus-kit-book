# Closing a milestone

After this chapter you can close a milestone: check its paragraph on the running product, review everything it built with what your host offers, and decide each finding.
You can then turn the confirmed findings into lines in a new milestone, `<M>.1`, instead of fixes.

## Why review the whole

Each page of a milestone was read before `/apply` built it, and each staged change was reviewed before its commit.
Nobody looked at what they add up to.
The kit closes that gap in one rule, §8 of the process document it writes, docs/05, as it reads since focus-kit's commit `bff8414`.
The last line of every milestone is its review, `<milestone>-review`, a delivery like the others: `/propose` writes its page, and `/apply` runs it.
It checks the milestone's paragraph clause by clause against what the deliveries built, and reviews the code with what the host offers.
It fixes nothing.
Each confirmed finding becomes a `[ ]` line in a new milestone right after the reviewed one, numbered with `.1` (milestone 1 is followed by 1.1), which ends with its own review; a finding is never a fix in the middle of the next milestone.
A light process has no gate between deliveries, so the risk it carries is the sum: every delivery right on its own page, and the whole wrong.

That look is a milestone review: the milestone's paragraph checked on the product, then a review of everything the milestone built.
Each problem it reports is a finding, and you confirm it or reject it.

The review's page, written by `/propose m1-review` for a milestone 1, names what to look at: the milestone's range of commits, its paragraph, and the host's review command with its level.
`/apply m1-review` checks the paragraph clause by clause, runs the review, and stops there, because the decisions on the findings are yours.
The clinic's milestone 1 review ran before the kit made the review a line of the milestone, which is why the clinic's milestone 1 has no such line: I ran it headless, outside any delivery.
Its steps are the ones `/apply` runs, in the next two sections; the decisions after them are yours in both cases.

## Check the paragraph

The clinic's milestone 1 closed with seven commits, from `skeleton` to `cancel-appointment`, each page and each staged change reviewed by me before its commit.[^clinic-milestone-1-run]
This is its paragraph, from the clinic's docs/06:

```
When it closes, the owner can register professionals and their weekly hours,
a client can book a free slot, and a client can cancel up to 24 hours before.
```

[Chapter 9](09-queue-and-milestones.md) wrote this paragraph as a test a person can check against the product, so check it.
On a clean database, run `npm run setup` and `npm run dev`, then try each claim once, end to end, in the order the owner and a client would meet them.
Each delivery's check tested its own part; this one runs them together, as the product is used.
I did it before the review:[^closing-a-milestone-run]

* The owner registers professionals: held.
* The owner sets their weekly hours: held.
* A client books a free slot: held.
* A client cancels up to 24 hours before: held.

A claim that does not hold is a finding like any other, and goes to the decisions below with the review's.
None failed here.

## Review everything the milestone built

In Claude Code the review is `/code-review`.
Without a target it reviews the branch's commits ahead of its upstream plus the uncommitted changes, which on a `main` already pushed is nothing.[^claude-code-review]
It also takes a target: a file path, a PR number, a branch name, or a ref range.[^claude-code-review]
The milestone's range starts at the last commit before it, `3f0b47c`, and ends at its last, `f16f83b`:

```
/code-review high 3f0b47c...f16f83b
```

With three dots, git compares the second commit with the point where the two histories meet; since `3f0b47c` is an ancestor of `f16f83b`, that is exactly the milestone's seven commits.
The level trades coverage for confidence: at `low` and `medium` the review reports only the findings it is most sure of, and `high` through `max` broaden coverage and may include findings it is less sure of.[^claude-code-review]
I chose `high`: a milestone is reviewed once, as a whole, so breadth is worth more there, and the decisions of the next section filter out what is uncertain.
The review only reports; it changes your files only when you add `--fix`, and here you do not.[^claude-code-review]

Other hosts offer the same look.
Codex has `/review` in a session and `codex review --base <branch>` in the terminal, which review the changes against a base branch.[^codex-review]
GitHub Copilot reviews pull requests, so there the milestone goes up as one pull request from its first commit to its last.[^copilot-review]

I ran the review headless, from the clinic's root, allowed to run only `git diff`, `git log`, `git show`, `git status`, npm and npx, so an edit would have been refused.[^closing-a-milestone-run]
It answered with ten findings, each with a file, a line, a summary and a failure scenario.
These are the ten summaries in the run's order, as it printed them except for the numbers, added here so the decisions below can refer to them; the scenarios are in the record:[^closing-a-milestone-run]

```
1. "summary": "The partial unique index on (professional_id, starts_at) only stops two bookings with the exact same start. docs/03 invariant 2 says an appointment stays when the weekly hours change, so slots can partly overlap an existing booking, and the index does not cover that case even though docs/02 says one index on the start is enough.",
2. "summary": "A booking-code clash on the UNIQUE booking_code (cancelled rows count too) is answered as 500 DatabaseFailed, which the client shows as 'The server cannot be reached', even though the booking itself was valid.",
3. "summary": "migrate builds the pending list outside any lock and then applies each file inside a deferred BEGIN, so two processes that start together (server and `npm run setup`, which docs/02 says runs on the same machine) both apply the same migration.",
4. "summary": "SlotTaken is detected by matching the English text of SQLite's error message instead of the error code and constraint, which breaks silently if SQLite or Node changes the wording or the index gets more columns.",
5. "summary": "checkTimeZone accepts only the canonical names from Intl.supportedValuesOf, so it refuses valid IANA link names that Intl.DateTimeFormat accepts. This goes against docs/03, where UnknownTimeZone means 'not an IANA name'.",
6. "summary": "When the slots reload after a refused booking (SlotTaken) fails, 'Try again' calls loadSlots(professional) without the `after` argument, so the 'no longer free' message and the return to the chosen day are lost.",
7. "summary": "An empty line between the weekly-hours rows and the new slots/appointments rows splits the Routes table, so the three book-appointment and cancel-appointment routes do not render as table rows.",
8. "summary": "book() computes freeSlots twice over the whole 30-day window (once with booked emptied, once with it) only to test whether one instant is a member.",
9. "summary": "databaseFailed(c) is copied again (it already exists in session.server.ts, professionals/route.server.ts and weeklyHours/route.server.ts, and signIn/clinic inline it), and notFound(c) repeats weeklyHours/route.server.ts. This breaks the AGENTS.md rule on abstraction.",
10. "summary": "minutesOf is an exact copy of the private helper in weeklyHours/rules.ts:24. slotsOf (route.server.ts:100) also loads every active professional to find one by id.",
```

Read them as claims: each names where to look, and none has been checked yet.
Seven deliveries had passed their own reviews, and the whole still held a split table in docs/02, a helper copied into four files, and a retry that loses its message.

## Decide each finding

A finding reads like a fact, and some are not.
[Chapter 6](06-the-documents.md) gave the rule: you are the brain of the operation, and you check what the agent writes against what you know.
Here that means two things: you never take a finding as true without looking at the code, and you never drop one without saying why.

The agent running this book's `/apply` read each finding against the clinic's code and documents and gave me its assessment; I checked it and decided each one.
I sent the decisions to the review's session with `--continue`, the headless way of typing in the same session ([chapter 7](07-brainstorm.md)); interactively, you type them in the review's session.
I sent them in one request that also asked for the lines, word for word:[^closing-a-milestone-run]

```
My decisions on the ten findings:

1. Rejected. The route checks the free slots and inserts with no await in between, and the clinic runs one server process, so no other booking can interleave; freeSlots already refuses a start that overlaps a booked appointment.
2. Rejected. docs/02 records this on purpose: a clash answers 500 DatabaseFailed and the client's "Try again" draws a new code, with no retry loop. With 31^6 codes a clash is too rare to change it.
3. Rejected. docs/01 says npm run setup runs once, before npm run dev, so the two never start together on a new database.
4. Rejected. The repository, route and rules tests cover SlotTaken through a real insert, so a change in SQLite's wording fails npm run verify the day it happens.
5. Confirmed. checkTimeZone refuses IANA names such as US/Eastern and Etc/UTC, which docs/03 says are accepted.
6. Confirmed. After a 409 SlotTaken whose slot reload fails, "Try again" loses the "no longer free" message and the chosen date.
7. Confirmed. The empty line splits the Routes table of docs/02.
8. Rejected. Two passes over 30 days of one professional's slots cost nothing measurable at the clinic's size.
9. Confirmed. databaseFailed has four copies and notFound two, against the abstraction rule of AGENTS.md.
10. Confirmed for the duplicated minutesOf, against the same rule. Rejected for reading every active professional: the clinic has a handful.

Fix none of them. Write each confirmed finding as a [ ] line in docs/06, in the milestone where it belongs, or in a new milestone with its paragraph if none fits, and say where you put each and why. Then stage with git add.
```

Every rejection names what the review did not weigh: a choice docs/02 records on purpose, an order docs/01 fixes, tests that already guard the case, a scale the clinic will not reach, a race that needs a second server process.
Every confirmation was checked in the code first: Node refused `US/Eastern`, line 292 of `useBooking.ts` called `loadSlots` without its second argument, the empty line was in the table.
One finding can split, as the tenth did: its duplicated parser confirmed, its query rejected.

## Findings become lines

The agent found no milestone that fit the five confirmed findings: milestone 1 is closed, and the next one, "the owner runs the day", is about absences, the day's schedule and the deploy.[^closing-a-milestone-run]
So it added a milestone before that one, with its paragraph, and renumbered "the owner runs the day" as milestone 3.
This is the diff of the clinic's docs/06:[^closing-a-milestone-run]

````diff
diff --git a/docs/06-Queue.md b/docs/06-Queue.md
index 760ecff..c729d8b 100644
--- a/docs/06-Queue.md
+++ b/docs/06-Queue.md
@@ -18,7 +18,22 @@ a client can book a free slot, and a client can cancel up to 24 hours before.
 [x] cancel-appointment   a client cancels up to 24 hours before, or is told why not
 ```
 
-## Milestone 2: the owner runs the day
+## Milestone 2: what the review of milestone 1 found
+
+When it closes, every confirmed finding of the milestone 1 review is
+settled: setup accepts every IANA time zone name, a refused booking keeps
+its message through a failed reload, docs/02 renders whole, and the code
+repeated across features has one shared copy.
+
+```
+[ ] time-zone-names      setup accepts every IANA name the runtime knows, such as US/Eastern and Etc/UTC, as docs/03 says
+[ ] slot-taken-retry     after a refused booking whose slot reload fails, "Try again" keeps the "no longer free" message and the chosen date
+[ ] routes-table         the Routes table of docs/02 renders whole, with the slots and appointments routes as rows
+[ ] route-errors         one shared databaseFailed and one shared notFound answer; the first copies are in session.server.ts and weeklyHours/route.server.ts
+[ ] minutes-of           one shared "HH:MM" parser; the first copy is in weeklyHours/rules.ts, the second in appointments/rules.ts
+```
+
+## Milestone 3: the owner runs the day
 
 When it closes, the owner can record a professional's absences, which remove
 their slots, and sees the day's appointments per professional; and the app
````

Under the kit's rule since `bff8414`, that new milestone is milestone 1.1, right after milestone 1, and it ends with its own review, `m1.1-review`; "the owner runs the day" keeps the number 2, so nothing renumbers.
When the clinic updated the kit, its queue was renamed to match: the clinic's [docs/06 at `a3e2470`](https://github.com/JCKodel/focus-kit-clinic/blob/a3e2470/docs/06-Queue.md) has milestone 1.1, ending with `m1.1-review`, and milestone 2, ending with `m2-review`.

Each line says what will be true, not how to fix it, and the two lines about copied code name the first copy, as the abstraction rule asks.
Each one is a delivery: `/propose` will write its page and `/apply` will build it, like any other.

A line, and not a fix, because a fix made in the middle of the next milestone has no page and no review.
Nobody reads its scope before it is built, nobody checks it against a page afterwards, and it lands in a milestone whose paragraph does not mention it.
As a line it waits its turn, and gets both.

I asked the same session for the commit message again with one bullet per new line, as the clinic's docs/05 asks, then committed it, created the tag `book-v1/closing-a-milestone` and pushed both.[^closing-a-milestone-run]
The tag [`book-v1/closing-a-milestone`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone) holds the whole of milestone 1 with its queue of findings, so you can compare your code with it; its queue keeps the names of the diff above, since a tag never moves.

## When the findings became one delivery

Ninjobs wrote the same rule into its process on 2026-08-29: each confirmed finding of a milestone review becomes a line in the queue.[^ninjobs]
When its milestone closed, the review had eight findings, and I put all eight into one delivery instead.[^ninjobs]
Its page says, in its own words, that it does not fit a page and that it goes against the process on purpose.
It ran to 879 lines.[^ninjobs]
When I checked the result myself, I found faults its tests had not caught.
The process was not the cause; my choice was.
Eight lines would have been eight pages, each small enough to read before it was built and to check after.

## Key points

* A milestone review looks at what the deliveries add up to, which no review of a single page or staged change can see.
* Check the paragraph first, on the running product, end to end, once; a claim that fails is a finding.
* The review is the milestone's last line, `<milestone>-review`, run with `/propose` and `/apply`: it checks the paragraph, reviews the milestone's range with what your host offers (in Claude Code, `/code-review high <before>...<last>`), and fixes nothing.
* Decide each finding with its reason, after looking at the code: never trust one blindly, never dismiss one unread.
* A confirmed finding becomes a line in a new milestone `<M>.1`, not a fix: a fix in the middle of the next milestone has no page and no review.

## Exercises

These exercises use the clinic, by conversation with the agent, never by hand.

### Exercise 12.1

After exercise 11.4, check each sentence of its paragraph on your running app, and write down any that does not hold.

### Exercise 12.2

If your milestone 1 does not end with `m1-review`, ask the agent to add it as its last line.
Then run `/propose m1-review` and `/apply m1-review`, and decide each finding with its reason.

### Exercise 12.3

Ask the agent to write your confirmed findings as milestone 1.1, right after milestone 1, with its paragraph and `m1.1-review` as its last line, and check the diff.

[^claude-code-review]: Anthropic, "Code Review", accessed 2026-09-28. <https://code.claude.com/docs/en/code-review>
[^codex-review]: OpenAI, "Developer commands", accessed 2026-09-28. <https://learn.chatgpt.com/docs/developer-commands?surface=cli>
[^copilot-review]: GitHub, "About GitHub Copilot code review", accessed 2026-09-28. <https://docs.github.com/en/copilot/concepts/agents/code-review>
[^clinic-milestone-1-run]: This book's build of the guided project's milestone 1, 2026-09-28, with Claude Code 2.1.284 and the model `claude-opus-5-5`: the six deliveries after `skeleton`, each with its page review, its staged review and its commit. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/clinic-milestone-1-run/README.md>
[^closing-a-milestone-run]: This book's review of the guided project's milestone 1, 2026-09-28 and 2026-09-29, with Claude Code 2.1.284 and the model `claude-opus-5-5`, on the range 3f0b47c...f16f83b: the paragraph check, the command and its permissions, every turn, the findings, the decisions, the queue's diff and the commit message. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/closing-a-milestone-run/README.md>
[^ninjobs]: Ninjobs, a private repository: the rule in its docs/05, added on 2026-08-29; the page of the delivery that took the eight findings of its milestone review, counted by the author with `wc -l`. The content of the findings is left out.
