# 15. Closing a milestone

After this chapter you can close a milestone: plan its review as the milestone's last line, test each clause of its paragraph by hand, and turn each finding into a `[ ]` line in the same milestone, under the review.
You can also say what that review reads, the paragraph by hand and, on the person's word, the code changed since the milestone's base, split by areas with one read-only agent each and a checker before the person sees a candidate, and why its findings get no review of their own.

## The problem

Each page of a milestone was read before `/apply` built it, and each staged change was reviewed before its commit.
Nobody looked at what they add up to.
A light process has no gate between deliveries, so the risk it carries is the sum: every delivery right on its own page, and the whole still wrong.
A claim of the milestone that no delivery took on, a step that works on its own and fails once the next delivery follows it, such as a loan the lending screen records and the member's list never shows: none of them fails a single delivery's review.

## The review is a delivery

The kit closes that gap in one rule, §8 of the process document it writes, docs/05.
A milestone is planned with its review as its last line, `<milestone>-review`, a delivery like the others: `/propose` writes its page, and `/apply` runs it.
Its page takes the milestone's paragraph clause by clause and writes, for each, which delivery answers it and how a person tests it.
It fixes nothing.
The review also reads the code, the one look at the whole instead of a delivery, because every page can be right and the whole wrong.
Its page names as the base the commit of the previous milestone's review, or, for a first milestone, the project's first commit, and lists, by the areas docs/05's Milestone review slot names, the paths the range since it changed.
The previous review's commit sits before every commit of the next milestone, whose deliveries can land before the previous one's findings close, so the range from it holds all of them, the fixes of those findings included.
The reading costs, so the session says when it is time and starts it only on the person's word: each area gets a reader of its own, which reads it with the whole repository open.
The first commit, the base of a first milestone, makes the review read the whole project.
Each delivery's code is still read where its change is small enough to read: by the delivery review before `/apply` ends and in the staged change before its commit (chapter 13), and in the pull request, when the team lands its deliveries through one (chapter 20); the milestone's readers look for what those could not see.

## Test each clause by hand

A milestone ends with a paragraph written as a test a person can check against the product.
For a milestone of the lending library, written for this chapter:

```
When it closes, a librarian can lend a copy and record its return, and a
member sees their loans with the due date of each.
```

The person runs the test the page wrote for each clause, on the running product, end to end, once, in the order a librarian and a member would meet them: lend a copy, record its return, open the member's loans and read the due dates.
Each delivery's check tested its own part; this one runs them together, as the product is used.
A person does it by hand because the paragraph is a promise to the people who will use the product, and only someone using it as they will sees whether it holds.
A clause no delivery answers, or one that fails in the person's hands, is a finding.
There is nothing to confirm or reject: the failure happened in your hands.

## Read the code since the base, by areas

The hand test sees the product as a user meets it, and so it sees nothing a user cannot see.
A call that takes hundreds of milliseconds still answers.
A page that can be framed, shown by another site inside its own to trick a visitor into a click, still looks right.
Data sent to a service it should not reach leaves no trace on the screen, and a function that reaches a network it should not still returns the right result.
None of them fails a clause tested by hand; all of them are in the code.

The milestone is every change since its base, and the reading covers all of them.
`git diff <base>..HEAD` shows them: `git diff` prints what changed between two commits, line by line, and `<base>..HEAD` is the range from the base to `HEAD`, the commit you are on, usually the last (chapter 18 teaches `HEAD`), so the diff holds every change made after the base, whichever delivery made it.
A review given one commit reads what that commit changed, the milestone's last delivery, and misses the others.
`git diff --stat <base>..HEAD` lists the range's paths, and the review's page writes them down by area, so the paths the readers read can be checked against it.

docs/05's Milestone review slot says how the range is split: the areas a milestone's changes split into, one reader each, and the model its readers and its checker run on, or the session's.
For the lending library, written for this chapter, it reads:

```
Milestone review: by areas, one reader each: src/features/loans/,
src/features/members/, src/features/catalog/, the documents and the
rest; readers and checker on the session's model.
```

Each area is a slice of chapter 4, because a slice's changes are read together; the documents and the rest is the area for what lives outside the slices.
An area too large for one careful reading splits again, as `src/features/loans/` would into its lending and its `return/`.

The reading runs in any host.
Where the host runs agents, the session launches one read-only agent per area, the agent of chapter 13 that reads files and edits nothing, all in parallel.
Where it runs none, the person opens one fresh session per area and gives it its area.
Each reader has the whole repository open and reads its area's changes for what no delivery's own review could see: one delivery's work against another's, a document against another, the whole against docs/01.
It reports candidates, each by file and line, and the paths it read; a candidate is what a reviewer reports before anyone acts on it.

The review's page compares the paths read with the range's.
When they miss some, the page says which, and the review line waits as `[?]` with `· resume: apply` and `· blocked: <what was read>` (chapter 14) until they are read, because a reader that read part of its area reports the same way as one that read it all.

One checker, an agent or the review's session itself, opens each candidate's file and marks it before the person sees it: seen when it is true in the file today, latent when nothing triggers it today, or weak when the claim does not hold as stated.
A reader's candidate is a claim about a file, and some do not hold once the file is opened; the checker spends that opening so the person does not.
Three candidates on the lending library, written for this chapter, one per mark, as the checker hands them to the person:

```
src/features/members/myLoans.server.ts:12
  the query of my-loans reads the table loan directly; loan code
  lives in src/features/loans/, and other slices import it
  seen: true today, and no hand test shows it
src/features/members/myLoans.server.ts:14 and
src/features/loans/return/repository.server.ts:21
  each writes its own condition for an open loan, returned_at null
  latent: the same today; they part the day a loan gains another state
src/features/loans/return/repository.server.ts:18
  return-book records a return for a copy never lent
  weak: its UPDATE matches only an open loan and refuses the rest
```

The seen and the latent candidates each sit across two slices, which no delivery's review reads together, and the weak one, unchecked, would have spent the person's time on a claim the file refutes.

The readers and the checker fix nothing.
A candidate becomes a finding only when the person confirms it, and then it is a finding like the others, a `[ ]` line under the review line.
A project whose Milestone review slot says none has no code reading, and the hand test still runs.

## A line, and not a fix

Each finding becomes a `[ ]` line in the same milestone, under the review line, waiting for `/propose`.
Each line says what will be true, never how to fix it.
If the returned copy stayed among the member's loans, the milestone's lines would end this way, written for this chapter:

```
[x] lend-book      the librarian lends a copy
[x] return-book    the librarian records a return
[x] my-loans       a member sees their loans and due dates
[x] m1-review      the paragraph tested by hand, the code read
[ ] returned-loan  a returned copy leaves the member's loans
```

Each finding line is a delivery: `/propose` will write its page and `/apply` will build it.
The milestone closes when those lines are `[x]`, each with its proof.

A line, and not a fix, because a fix made in the middle of the next milestone has no page and no review.
Nobody reads its scope before it is built, nobody checks it against a page afterwards, and it lands in a milestone whose paragraph does not mention it.
As a line it waits its turn, and gets both.
And it stays in the milestone whose paragraph it fails, so that milestone closes only when its paragraph holds.

## No second review

The finding lines get no review of their own.
Each one passes through its own page, its proof and the person's commit, which is the review.
Their code is still read with the whole: the next milestone's review names this review's commit as its base, so on the lending library `m2-review`'s range starts at `m1-review`'s commit and holds `returned-loan`'s fix.
I keep it that way because a review of the fixes finds findings of its own, and a review of those finds more, and a milestone that keeps opening rounds of fixes never closes.

## When the findings became one delivery

On Ninjobs the review at the public opening returned eight findings, with the whole test suite green.
Queries took hundreds of milliseconds, a large job posting would have timed out, and three of the findings were about security.
That review read the code, and it is the reason the kit's milestone review reads it too: every delivery had passed its own tests and its own review, and only the look at the whole saw the eight.

I put all eight into one delivery instead of eight lines.
Its page says, in its own words, that it does not fit a page and that it breaks the rule on purpose, and it ran to 879 lines, the longest page of the project.
The fixes held: the page measured job triage at about 620 ms on the development database when the work began, and at 94 ms when it ended.
But when I checked the result myself, I found faults its tests had not caught.
The process was not the cause; my choice was.
Eight lines would have been eight pages, each small enough to read before it was built and to check after.

## What the team gains

A hand test of the whole product sees what no single delivery's check can: a clause no delivery took on, a step that fails once the deliveries run together, met the way a user will meet them, before users do.
The read of the whole code adds what no hand test can see, the kind of fault the review at the Ninjobs opening found.
The checker spends the person's time on the candidates that hold, and the paths each reader lists make a part of the milestone left unread show on the page instead of passing as read.
And because each finding becomes a line, the team sees the cost of the milestone's gaps in the queue, next to everything else it plans, instead of in fixes nobody reviewed.

## Key points

* A milestone review looks at what the deliveries add up to, which no review of a single page or staged change can see.
* A milestone is planned with its review as its last line, `<milestone>-review`, run with `/propose` and `/apply`: its page names as the base the commit of the previous milestone's review, or the project's first commit for a first milestone, writes for each clause of the paragraph the delivery that answers it and how a person tests it, and fixes nothing.
* The person tests each clause by hand, and on the person's word the session reads the range since the base by the slot's areas, one read-only agent each listing the paths it read, and a checker marks each candidate; a clause no delivery answers, one that fails in the person's hands, or a candidate the person confirms is a finding.
* Each finding becomes a `[ ]` line in the same milestone, under the review line, never a fix in the middle of the next milestone; the milestone closes when those lines are `[x]`.
* The finding lines get no review of their own: each passes through its own page, its proof and the person's commit.
