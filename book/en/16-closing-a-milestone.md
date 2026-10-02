# 16. Closing a milestone

After this chapter you can close a milestone: plan its review as the milestone's last line, test each clause of its paragraph by hand, and turn each finding into a `[ ]` line in the same milestone, under the review.
You can also say why that review reads no code and why its findings get no review of their own.

## The problem

Each page of a milestone was read before `/apply` built it, and each staged change was reviewed before its commit.
Nobody looked at what they add up to.
A light process has no gate between deliveries, so the risk it carries is the sum: every delivery right on its own page, and the whole still wrong.
A claim of the milestone that no delivery took on, a step that works on its own and fails once the next delivery follows it, such as a loan the lending screen records and the member's list never shows: none of them fails a single delivery's review.

## The review is a delivery

The kit closes that gap in one rule, §8 of the process document it writes, docs/05.
A milestone is planned with its review as its last line, `<milestone>-review`, a delivery like the others: `/propose` writes its page, and `/apply` runs it.
Its page takes the milestone's paragraph clause by clause and writes, for each, which delivery answers it and how a person tests it.
It reviews no code and fixes nothing.
Code is read where each change is small enough to read: in the staged change before each delivery's commit (chapter 15), and in the pull request, when the team lands its deliveries through one (chapter 21).

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

## A line, and not a fix

Each finding becomes a `[ ]` line in the same milestone, under the review line, waiting for `/propose`.
Each line says what will be true, never how to fix it.
If the returned copy stayed among the member's loans, the milestone's lines would end this way, written for this chapter:

```
[x] lend-book      the librarian lends a copy
[x] return-book    the librarian records a return
[x] my-loans       a member sees their loans and due dates
[x] m1-review      each clause of the paragraph tested by hand
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
I keep it that way because a review of the fixes finds findings of its own, and a review of those finds more, and a milestone that keeps opening rounds of fixes never closes.

## When the findings became one delivery

On Ninjobs the review at the public opening returned eight findings, with the whole test suite green.
Queries took hundreds of milliseconds, a large job posting would have timed out, and three of the findings were about security.
That review read the code; the kit's milestone review no longer does, since each delivery's code is read before its commit.
Every delivery had passed its own tests and its own review; only the look at the whole saw them.

I put all eight into one delivery instead of eight lines.
Its page says, in its own words, that it does not fit a page and that it breaks the rule on purpose, and it ran to 879 lines, the longest page of the project.
The fixes held: the page measured job triage at about 620 ms on the development database when the work began, and at 94 ms when it ended.
But when I checked the result myself, I found faults its tests had not caught.
The process was not the cause; my choice was.
Eight lines would have been eight pages, each small enough to read before it was built and to check after.

## What the team gains

A hand test of the whole product sees what no single delivery's check can: a clause no delivery took on, a step that fails once the deliveries run together, met the way a user will meet them, before users do.
This gain has no number in this book.
And because each finding becomes a line, the team sees the cost of the milestone's gaps in the queue, next to everything else it plans, instead of in fixes nobody reviewed.

## Key points

* A milestone review looks at what the deliveries add up to, which no review of a single page or staged change can see.
* A milestone is planned with its review as its last line, `<milestone>-review`, run with `/propose` and `/apply`: its page writes, for each clause of the paragraph, the delivery that answers it and how a person tests it; it reviews no code and fixes nothing.
* The person tests each clause by hand; a clause no delivery answers, or one that fails in the person's hands, is a finding.
* Each finding becomes a `[ ]` line in the same milestone, under the review line, never a fix in the middle of the next milestone; the milestone closes when those lines are `[x]`.
* The finding lines get no review of their own: each passes through its own page, its proof and the person's commit.
