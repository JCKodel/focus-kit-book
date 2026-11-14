# 15. Closing a milestone

After this chapter you can close a milestone: plan its review as the milestone's last line (written `· after all`, so a line the person cancelled never holds it back), test each clause of its paragraph by hand, run the slow tests the project keeps out of verify, copy onto the review's page the notes the deliveries left, and grade every confirmed finding: a grave one a `[ ]` line of its own, the medium ones you pick on one `<milestone>-fixes` line, the small ones listed, every line in the same milestone, under the review, even when the next milestone is already in the queue.
You can also say what that review reads, the paragraph by hand and, on the person's word, the code changed from the milestone's base to the commit its reading started at, read by whoever docs/05's Milestone review slot names, the host's deep review or one read-only agent per area, with a checker either way before the person sees a candidate, and why its findings get no review of their own.
That range stays fixed while new commits arrive, so every reader's diff is the same.

## The problem

Each page of a milestone was read before `/apply` built it, and each delivery was used and its staged change reviewed before its commit.
Nobody looked at what they add up to.
A light process has no gate between deliveries, so the risk it carries is the sum: every delivery right on its own page, and the whole still wrong.
A claim of the milestone that no delivery took on, a step that works on its own and fails once the next delivery follows it, such as a loan the lending screen records and the member's list never shows: none of them fails a single delivery's review.

## The review is a delivery

The kit closes that gap in one rule, §8 of the process document it writes, docs/05.
A milestone is planned with its review as its last line, `<milestone>-review`, a delivery like the others: `/propose` writes its page, and `/apply` runs it.
Its line ends `· after all`, every line above it in its milestone but the cancelled ones, so `/propose` writes its page when every one of those is defined and `/apply` runs it when every one is integrated; a line the person cancelled never holds it back, and a line whose `after` names a cancelled one stays held by it, and the review with it, until the person re-decides that line.
Its page takes the milestone's paragraph clause by clause and writes, for each, which delivery answers it and how a person tests it.
It fixes nothing.
It runs the slow tests docs/05's Verify slot names, the ones kept out of verify because they take too long for every delivery, when the slot names any; a failing one is a finding, graded like the others (below); and when a delivery noted verify over its ceiling, the review says which tests go to the slow ones.
The review also reads the code, the one look at the whole instead of a delivery, because every page can be right and the whole wrong.
Its page names as the base the end named by the page of the last review that ran, the commit that review's reading started at and not that review's own commit, or, for a first milestone, the project's first commit, or, where no earlier review ran, a commit the page names with the reason it chose it, and as its end the commit `HEAD` was when the reading started, and lists the paths that range changed, by the areas docs/05's Milestone review slot names when the kit's readers read it.
A project whose earlier milestones closed with no review line names, for instance, the commit that closed the last of them, because nothing after it was read as a whole; that example is written for this chapter.
The range from that base holds every commit made after it up to the review's own end: what was committed while the last review read, that review's own commit, which adds its page, all the fixes of its findings, which close after it, and the next milestone's deliveries.
A free line of the next milestone does not come after the review (chapter 14), so a delivery can be committed while a review reads, after that review's end and before that review's own commit: outside that review's range, it falls in the next one, which starts at that end.
A base at the last review's own commit would leave such a delivery in neither range, so no review would copy its notes or read its code; on 2026-11-14 a delivery of this book noted that gap on its page, before any delivery had fallen into it.
The end of the last review that ran is also the base after a cancelled one: with `m2-review` cancelled on the lending library, `m3-review` names as its base the end `m1-review`'s page names, so milestone 2's deliveries are read with milestone 3's.
The reading costs, so the session says when it is time, and it starts only on the person's word; who reads is the slot's choice, the host's deep review or a reader per area, and the section on reading the code, below, says how.
A first milestone's range, from the project's first commit, holds every change made after that commit and not the commit itself, just as a range from a base the page names leaves that base out; recording the end changes where the range stops, not that exclusion.
What the first commit added, on a new project the kit's files and the documents (chapter 10), is in no diff of the range: the readers see it only as the repository they read their areas against, and the person read the documents before committing them.
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

## Read the code since the base

The hand test sees the product as a user meets it, and so it sees nothing a user cannot see.
A call that takes hundreds of milliseconds still answers.
A page that can be framed, shown by another site inside its own to trick a visitor into a click, still looks right.
Data sent to a service it should not reach leaves no trace on the screen, and a function that reaches a network it should not still returns the right result.
None of them fails a clause tested by hand; all of them are in the code.

The milestone is every change since its base, and the reading covers all of them.
`HEAD` is the commit you are on, usually the last (chapter 18 teaches `HEAD`), and when the reading starts the review's page records that commit; this chapter writes that recorded commit as `<review-head>`.
`git diff <base>..<review-head>` shows the changes: `git diff` prints what changed between two commits, line by line, and `<base>..<review-head>` is the range from the base to the recorded commit, so the diff holds every change made after the base, whichever delivery made it.
A review given one commit reads what that commit changed, the milestone's last delivery, and misses the others.
`git diff --stat <base>..<review-head>` lists the range's paths, which the review's page writes down, by area when the kit's readers read it, so the paths the readers read can be checked against it.
Every reader takes those two commits from the page, never `HEAD` itself, because `HEAD` moves: a free line of the next milestone may commit while the readers work, and a reader that ran `git diff <base>..HEAD` then would read a change no other reader saw and the page's list does not hold.
With the end recorded, every area's list and every area's diff come from the same range.

docs/05's Milestone review slot says who reads the range, in one of three answers: the host's deep review, when the host has one that takes the whole range; the kit's readers, by the areas a milestone's changes split into, one reader each, on the model the slot names or the session's; or none.

The host's deep review is the host's own command that reads a whole range in one launch and reports candidates by file and line, and the slot names its command.
The person launches it, once, over `<base>..<review-head>` taken from the page, never over `HEAD`.
It splits the range its own way, so the slot names no areas for it.

The kit's readers take the slot's other form; for the lending library, written for this chapter, it reads:

```
Milestone review: by areas, one reader each: src/features/loans/,
src/features/members/, src/features/catalog/, the documents and the
rest; readers and checker on the session's model.
```

Each area is a slice of chapter 4, because a slice's changes are read together; the documents and the rest is the area for what lives outside the slices.
An area too large for one careful reading splits again, as `src/features/loans/` would into its lending and its `return/`.

The kit's readers run in any host.
Where the host runs agents, the session launches one read-only agent per area, the agent of chapter 13 that reads files and edits nothing, all in parallel.
Where it runs none, the person opens one fresh session per area and gives it its area.
Each reader has the whole repository open and reads its area's changes for what no delivery's own review could see: one delivery's work against another's, a document against another, the whole against docs/01.
It reports candidates, each by file and line, and the paths it read; a candidate is what a reviewer reports before anyone acts on it.

The review's page compares the paths the readers read with the list it wrote from `<base>..<review-head>`, never with a `HEAD` that has moved since, which would list paths no reader was given.
When they miss some, the page says which, and the review line waits as `[?]` with `· resume: apply` and `· blocked: <what was read>` (chapter 14) until they are read, because a reader that read part of its area reports the same way as one that read it all.

Either way, one checker, an agent or the review's session itself, opens each candidate's file, a reader's or the deep review's, and marks it before the person sees it: seen when it is true in the file today, latent when nothing triggers it today, or weak when the claim does not hold as stated.
A candidate is a claim about a file, and some do not hold once the file is opened; the checker spends that opening so the person does not.
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

The readers, the deep review and the checker fix nothing.
A candidate becomes a finding only when the person confirms it, and then it is a finding like the others, graded with them (below).
A project whose Milestone review slot says none has no code reading, and the hand test still runs; the review's page still names the range, its end, `<review-head>`, the commit `HEAD` was when the review started, because the notes it copies come from the pages that range delivered and the next review's base is that end.

## The notes the deliveries left

While a milestone runs, its deliveries meet flaws outside what they build, such as a screen another delivery built that loses what the person typed.
A flaw that is not grave does not become a line: it waits as a note on that delivery's page, under the heading `## For the review`, one line with the file and line and what a person would see (chapter 14 shows the note).
The review is where those notes are looked at.

It opens by copying onto its page the notes of every page its range delivered, the pages committed between its base and `<review-head>`; a delivery whose page holds no notes adds none.
The checker marks each note as it marks a candidate, seen, latent or weak, because a note says what was true when it was written, and a later delivery of the range may have changed that file since.
The person confirms a note as they confirm a candidate.

One note on the lending library, written for this chapter, on `return-book`'s page: "`src/features/loans/LendView.tsx:31`: after a refused loan the form clears the member's card number, and the librarian types it again".
`return-book`'s `/propose` or its `/apply` found it in the lending screen, outside what `return-book` builds, so it stayed a note.

## Grave, medium, small

Findings differ in weight: one breaks the promise the paragraph makes, another is a rare case or a cost nobody measured.
A review that made every finding a line would fill its milestone with lines, each with its own page, proof and commit before the milestone closes, a rare case beside a broken promise, while the next milestone's work waits behind them.

So the review grades every confirmed finding.
A grave one breaks a clause of the paragraph for a person on its usual path, loses or exposes data, leaves verify red, or is a fix a delivery in flight cannot go on without, and becomes a `[ ]` line of its own.
The others stay listed on the review's page: first the medium ones, which a person meets in ordinary use while the clause still holds; then the small ones, a rare case, a latent or weak candidate, a cost nobody measured.
The person says which medium ones enter the milestone's one fixes line, `<milestone>-fixes`, each an item of its page.
That page is their list and is not split, whatever its length, since split it would be the many lines again.
A small one becomes a line only when the person picks it.
These lines end `· from <milestone>-review`, the delivery that found them (chapter 14 shows the suffix), and sit under the review line.

Suppose the hand test failed on the lending library: a returned copy stays among the member's loans.
With that failure, the note on the lending screen, which the checker marked seen and the person confirmed, and the three candidates the checker marked above, the review's page grades them this way, written for this chapter:

```
Grave
  returned-loan: a returned copy stays among the member's loans
Medium
  1. LendView.tsx:31, a note of return-book: a refused loan
     clears the member's card, and the librarian types it again
Small
  2. myLoans.server.ts:12, seen: my-loans reads the table loan
  3. myLoans.server.ts:14 and repository.server.ts:21, latent
  4. repository.server.ts:18, weak
```

The failure breaks a clause on its usual path, so it is grave and already named as its line; the note is medium, met while lending still works; the seen candidate is small, a cost nobody measured, since no person meets it in use, and the latent and the weak ones are small by their marks.

A grave finding is a line of its own because it is a promise broken, and its own page is small enough to read before it is built and to check after.
The medium ones share one page because each is a fix a person would want and none breaks the promise.
A small one waits for the person because its cost is a guess.

## A line, and not a fix

A grave finding's line, the fixes line and the line of a small one the person picked sit in the same milestone, under the review line, and go through `/propose`.
Each line says what will be true, never how to fix it.
With the returned copy among the member's loans and the medium finding picked, the milestone's lines would end this way, written for this chapter:

```
[x] lend-book      the librarian lends a copy
[x] return-book    the librarian records a return
[x] my-loans       a member sees their loans and due dates
[x] m1-review      the paragraph tested by hand, the code read
[ ] returned-loan  a returned copy leaves the loans · from m1-review
[ ] m1-fixes       the review's medium finding · from m1-review
```

Each finding line is a delivery: `/propose` will write its page and `/apply` will build it.
The milestone closes when those lines are `[x]`, each with its proof.

A line, and not a fix, because a fix made in the middle of the next milestone has no page and no review.
Nobody reads its scope before it is built, nobody checks it against a page afterwards, and it lands in a milestone whose paragraph does not mention it.
As a line it waits its turn, and gets both.
And it stays in the milestone whose review found it, so a grave one keeps that milestone open until its paragraph holds.
It stays there when the next milestone already exists: with a milestone 2 already below it, holding its own lines and `m2-review`, `returned-loan` still goes under `m1-review`, and so does `m1-fixes`, not into milestone 2, each with its own `/propose` and `/apply` and no review of its own.

## No second review

The finding lines get no review of their own.
Each one passes through its own page, its proof and the person's use, review and commit.
Their code is still read with the whole: the next milestone's review names this review's `<review-head>` as its base, so on the lending library `m2-review`'s range starts at `m1-review`'s `<review-head>` and holds `returned-loan`'s fix.
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
The grades would have given each grave one its own page, small enough to read before it was built and to check after, and the rest one shared list at most; my page put all eight on one and graded none.

## What the team gains

A hand test of the whole product sees what no single delivery's check can: a clause no delivery took on, a step that fails once the deliveries run together, met the way a user will meet them, before users do.
The read of the whole code adds what no hand test can see, the kind of fault the review at the Ninjobs opening found.
The checker spends the person's time on the candidates that hold, and, when the kit's readers read, the paths each one lists, checked against the one range the page recorded, make a part of the milestone left unread show on the page instead of passing as read.
And because the review grades its findings, the queue shows as lines the ones that break the milestone's promise and one line for what the person picked to fix, next to everything else the team plans, and the rest stays listed on the review's page, never in fixes nobody reviewed.

## Key points

* A milestone review looks at what the deliveries add up to, which no review of a single page or staged change can see.
* A milestone is planned with its review as its last line, `<milestone>-review`, written `· after all`, an `after` that leaves out the cancelled lines, run with `/propose` and `/apply`: its page names as the base the `<review-head>` of the last review that ran, never that review's own commit, or the project's first commit for a first milestone, or, where no earlier review ran, the commit the page names and why, and as its end `<review-head>`, the commit `HEAD` was when the reading started.
  It writes for each clause of the paragraph the delivery that answers it and how a person tests it, and fixes nothing; the review runs the slow tests the Verify slot names.
* The person tests each clause by hand, and on the person's word the range from the base to `<review-head>` is read by the host's deep review or by the kit's readers, one read-only agent per area of the slot, each listing the paths it read, all on those two recorded commits, and a checker marks each candidate; a clause no delivery answers, one that fails in the person's hands, a slow test that fails, or a candidate the person confirms is a finding; the review opens by copying the notes the range's pages left under `## For the review`, which the checker marks like candidates and the person confirms like them.
* The review grades every finding: a grave one a `[ ]` line of its own; the medium ones the person picks on one `<milestone>-fixes` line, whose page is their list and is not split; the small ones listed, a line only when the person picks one; every line ending `· from <milestone>-review` under the review line, even when the next milestone already exists, never a fix in the middle of the next milestone; the milestone closes when those lines are `[x]`.
* The finding lines get no review of their own: each passes through its own page, its proof and the person's use, review and commit.
