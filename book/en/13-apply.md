# 13. `/apply`: build, verify, prove, never commit on its own

After this chapter you can follow a reviewed page to a staged change with `/apply`, and say what "done" means: verify green, a proof, a review by a context that did not write the change, the documents updated, the page moved and its line marked.
You can then use what `/apply` built and review the staged change against the page, which is the human review of the process, and then commit it, yourself or by asking the agent.
And you can say how `/apply` ends: only its delivery staged, the suggested message in a `commit` block on the page and in the conversation, your next steps written out and, last of all, which environment is at which version.

## The problem

An agent that is told "build this" stops when the code compiles, or when the tests it wrote pass.
What it built around the request, what it chose on its own and which documents no longer say the truth are left for someone to find later, and that someone is usually a user.
Asked to check its own work, it rereads the work with the reasoning that wrote it, so what it missed while writing, it misses again.
A 2024 study of large language models on reasoning tasks, by Jie Huang and colleagues, found that they "*struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction*".[^huang-2024]
And an agent that commits on its own puts its work in the project's history before any person has read it.

## What `/apply` does

`/apply <slug>` builds the delivery that `work/<slug>.md` describes, completely, in one session: the code, the tests, the proof and the documents.
It always starts in a fresh session, even when `/propose` ran in the conversation that asked for the change (chapter 11), so the page is all it takes from the conversation that wrote it, which is why chapter 12 asks you to read the page before this command runs.

### What it reads

The page, `AGENTS.md`, and three of the project documents: docs/01, the architecture, which says where each piece goes and how errors travel; docs/04, the conventions, which say which tests to write; and docs/05, the process.
docs/05 holds the project's slots, and `/apply` follows them literally: the verify command, the environments and what a delivery leaves in each, how a screen is proven, how its changes are reviewed before it ends, the publish policy and the git strategy.
Of docs/06, the queue, it reads all of it: it must see that the lines its `· after` names are done before it starts, and it names the next free line when it ends.
So every word on a line is read by every build as well as by every definition (chapter 11).
A file in `work/` does not make a page ready: only `/propose` marks the line `[>]`, when every section is filled or explicitly inapplicable and no scope question is left open (docs/05 §3).
On a page that still has a question open, or whose line is `[ ]` or `[~]`, it refuses to build and points to `/propose`: in the lending library, in an example written for this chapter, `/apply lend-book` on a page whose Contract still has a question unanswered edits nothing and names `/propose lend-book`, where the question gets its answer.
That refusal comes before any build, so it is not the stop that "When the work cannot go on" describes: nothing was built, and the line is not marked `[?]`.
On a `[>]` line whose `after` names a line not yet `[x]`, it does not start either, and leaves the mark as it is: an `after` is an order, not a wait (chapter 14).
Only on a complete `[>]` line whose `after` lines are all `[x]` does it mark the line `[*]` in docs/06, as its first edit, so the queue shows the build under way.
On a line that is `[?]`, it first says what the line waits on, and goes on only once the reason is resolved (chapter 14); then the line goes back by its resume phase: `resume: apply` returns it to `[>]`, ready to build, and `resume: propose` returns it to `[ ]`, with any draft kept, for `/propose` to finish, because removing the reason does not complete a definition.

### The page is the scope

What the page asks is what gets built, and nothing around it.
The kit's file for the command says it in one line: "*The page is the scope; do not widen it.*"
So `/apply` adds no dependency, layer or tool the page did not name, and writes an abstraction only on the second concrete occurrence, saying which was the first (chapter 3).
A package the page did not name is a question for the person, never a choice for the agent.

### When the page contradicts a document

It stops and says which.
Either the document changes in the same delivery, or the page is wrong; it never picks one silently.
A silent choice would leave a page and a document that disagree, and the next session would build on whichever it read first.

### When the work cannot go on

It stops when the build needs an answer nobody has given yet, when another line must be done first (a fix it found becomes a `[ ]` line above this one), when you say it is blocked, or, in a milestone's review, when the reading of the code changed since the milestone's base left part of it unread.
It writes on the page what was built and what it waits on, leaves the page in `work/`, marks the line `[?]` with that reason at its end (chapter 14).
It ends the page with a partial message in a `commit` block and shows the same block in the conversation.
On trunk it stages nothing: the work stays uncommitted, and out of the index, until it is whole.
On a delivery branch it may stage the partial work for you to commit there, and the branch stays unmerged until the delivery is done (chapter 19).

### Verify and the proof

It writes the tests docs/04 names for each piece (chapter 5); one too slow for verify goes with the slow tests, whose command docs/05's Verify slot names and the milestone review runs (chapter 15), and `/apply` tells you so, because a test moved there in silence would look like coverage dropped.
Moving it deletes no test and waives none of this delivery's own proof, and it changes neither where a rule lives, in a pure use case, nor the level of test that proves each scenario.
It then runs the verify command until it is green.
Then it proves the delivery the way docs/05 says: a screenshot against the design, a run from end to end, or a check by hand.
It lists what diverges from the reference and fixes it, until only what it can justify remains.
A failure is part of the proof and is recorded, never hidden.

### The delivery review

With verify green, the proof done and the documents and manuals the delivery changes already updated, and before the page records what happened, `/apply` has its delivery's changes reviewed by a context that did not write them.
The documents come first because they are part of the delivery: a schema document or a manual written after the review is one no reviewer read.
It happens inside the same session, never in a fresh one, and docs/05's Delivery review slot names the reviewer.
The kit's first choice is the host's own review, a skill the agent invokes or a command it runs, when the agent can keep it to the delivery's paths.
Otherwise it is a read-only agent: one the session launches with its own context, which reads files and runs `git diff` and edits nothing (chapter 16 says more on agents that an agent launches).
A slot that says none means no such review, and your commit stays the only review.

The review reads the whole delivery against its base, by its paths, the files the delivery created among them, and of docs/06 only this line's hunk, against the page and docs/04.
A read-only agent reads `git diff HEAD` of those paths, which compares them with the last commit and so holds staged and unstaged changes together; a bare `git diff` compares the working folder with the index and misses whatever is already staged.
On a delivery branch where you committed the partial work a blocked `/apply` staged, the agent also reads those commits against the branch's base: when the session resumes, a clean working folder does not mean there is nothing to review, since the work so far may sit in those commits, and they are still this review's.
On trunk there are none, since blocked work stays uncommitted there.
And it opens each file the delivery created, which the session names, since it wrote them: a new file is untracked, one git does not hold yet, so no diff shows anything of it until it is staged, and `/apply` stages only after the review.
The host's review reads them its own way, kept to those paths.
Another session's files in the same folder, the ones it created included, are not this review's (chapter 19).
The reviewer brings what the writer's own reread lacks, a context free of the reasoning that wrote the change, and measures the change against the page and docs/04.

The reviewer reports candidates, faults it suspects, and fixes nothing itself.
A candidate that breaks the page, docs/04 or the text this delivery wrote is fixed in this session, and verify runs again.
That holds for any edit verify covers made after its last green run, a review's fix or a document changed late: a green run speaks for the files as they were when it ran, so the later edit runs it once more.
Anything else, a fault in code the delivery did not touch or a wish the page did not ask for, becomes a `[ ]` line in the queue, because the page is the scope.
The reviewer stays read-only because the session that built the change knows why it made each choice, so that session makes the fix and the change keeps one writer.

Your review and your commit still come after it: it is one more check before you read the diff.
And it reads one delivery while that delivery is open, where the milestone review reads across the milestone's deliveries ([chapter 15](15-closing-a-milestone.md)).

### Green is not done

Verify tells you the code does what its tests say.
It says nothing about whether the page was answered, whether the documents still hold, or whether anyone can tell later what happened.
So before it stops, `/apply` does all of this:

* It writes into the page what happened: what diverged from the plan and why, what was dropped, what the proof found, what the delivery review found and what became of each candidate, and the decisions taken, with an ADR if one was needed.
* Before the review, it updates the documents the delivery changed: a new term into docs/03, a new rule into the document that owns it, a decision into docs/adr/.
* Before the review too, when the delivery adds or changes something a person does by hand, such as publishing the app, it writes or updates its manual in `docs/manuals/` ([chapter 7](07-the-documents.md)).
* Verify is green after the last edit it covers; an edit after that green run, whatever its reason, runs it again.
* It ticks every item of Done when.
* It moves the page to `work/done/`; a `[?]` line that waits only on this one, or on lines already `[x]`, goes back by its resume phase ([chapter 14](14-queue-states.md)).
* It stages only this delivery's paths and hunks, never with `git add -A` or `git add .`, and reports what someone else had already staged without unstaging it.
* It ends the page with the suggested commit message in a `commit` block, in the format docs/05 defines, and shows the same block in the conversation, where a fenced block stands apart from the rest of the reply. There is one block: a resumed `/apply` replaces the earlier one.
* Its last edit marks the line `[x]` in docs/06 and stages that hunk, after everything else is staged, so a line marked `[x]` with nothing staged is a session that stopped early.
* Its last words are your next steps: review the staged diff, commit (and merge, on a delivery branch), and take the queue's next line, with its command written as your host invokes it, in a fresh session, so a person new to the kit does not search the documentation for what comes after. The last thing it says is which environment is at which version and the command that updates the others, and it never ends silent about it.

Done is the review and that whole list.

## `lend-book`, built

Take the `lend-book` page of chapter 12, reviewed and marked `[>]`, and open a fresh session with `/apply lend-book`.

The agent reads the page, then docs/01 to learn that loans live in `src/features/loans/`, docs/04 to learn which tests each piece gets (chapter 5), and docs/05 to learn that verify is `npm run verify` and that a screen is proven by a screenshot.
It writes the migration for the table `loan` with its unique index, the rule `lend` as a pure function returning a `Result` (chapter 3), the repository call that turns the unique index's failure into the refusal `AlreadyLent`, the orchestrator and the lending screen.
Each Behaviour line becomes a test: the loan with its due date 21 days ahead, the refusal for an overdue book, the refusal for a suspended member, the loan for a member whose only book is due today, and, against a real in-memory database, the second of two loans on the last copy refused.
It builds nothing for returning a copy, reservations or fines, because Out of scope named them.

If docs/00 said a loan lasts 14 days, the agent would stop at that line and ask which one is true: the page's 21 or the document's 14.
Whichever you answer, the other one changes in the same delivery.

It runs `npm run verify` until it is green, takes the lending screen at 390 and 1280 pixels wide, and compares both with the design file.
If a button wraps at the narrow width, it gets fixed; if the design file gives no value for a colour, the choice is written down as a divergence, with its reason.

The delivery changed the schema, so before any review it adds the table `loan` to the document that lists the schema.
Then a read-only agent reads the files the delivery created, the migration and everything in `src/features/loans/`, and `git diff HEAD` of what the delivery edited, the schema document included, against the page and docs/04, in a review also written for this chapter, and reports two candidates.
The first draft of `insertLoan` turned every failure of the write into `AlreadyLent`, while the library's docs/04 holds chapter 3's boundary: the unique index's failure becomes `AlreadyLent`, and any other failure of the write stays `DatabaseFailed`.
No test triggers it, since in the tests only the unique index ever fails, and it sits in the text this delivery wrote, so the agent narrows the catch to the unique index's error and runs verify again; the repository call chapters 3 and 4 describe is the fixed one.
`insertLoan` lives in a file this delivery created, so a review of the diff alone would have read nothing of it.
The second candidate: the refusal for a suspended member does not say until when.
The page never asked for that, so it becomes the line `suspension-end`, placed in the queue below `return-book`, which stays the next free line.
Then it writes what happened on the page, both candidates and what became of each included, ticks Done when, moves the page to `work/done/lend-book.md`, stages only this delivery's paths, and, as its last edit, marks the line `[x]` and stages that hunk of docs/06.
If another session's edit to `src/features/members/` sits in the tree, or its hunk of docs/06 is already staged, the agent leaves both as they are and tells you about the staged one (chapter 19).

The page ends with the suggested message, written for this chapter, and the conversation shows the same block:

```commit
Lend a copy to a member

- Add the table loan, one open loan per copy by a unique index
- Lend for 21 days; refuse overdue books and suspended members
- Refuse the second loan of the last copy as AlreadyLent
- Prove the lending screen at 390 and 1280 pixels wide
- List the table loan in the schema document

work/done/lend-book.md
```

Then it gives your next steps:

1. Review the staged diff: `git diff --staged`.
2. Commit with the suggested message: `git commit`, and paste the block.
3. The queue's next free line is `return-book`; in a fresh session, run `/propose return-book` in Claude Code, or `$propose return-book` in Codex (chapter 8's table).

And it ends, last of all, on the environments, in a sentence also written for this chapter: "The development database has this delivery's migration; the staging environment is still at the previous delivery, and `npm run migrate -- staging` updates it."
If a session ends without that sentence, it did not end as the kit says; ask it for the sentence.
On Ninjobs, a person who opened the published site believing it current, after a session that ended without that sentence, reviewed a version that did not hold the delivery.

## Why it stops at the stage

`/apply` never commits and never merges on its own, whatever the git strategy.
It stages only its delivery and hands you the message; the decision to commit is yours, and it comes after your review.
The kit's process document gives the flow in one line: `/apply` "*builds, proves, updates the documents, stages and suggests the commit, never commits on its own*".
*On its own* is the point: once you have used and reviewed the delivery, you may ask the agent to commit it, and it takes that step and no other (the section on the commit shows how).

## Review the staged change

The staged change is what the agent says it did; your review checks that it did it.
Read it against the page:

* Is every Behaviour line answered, each by its test or a recorded check?
* Is anything built that the page did not ask for: a file, a dependency, a layer?
* Do verify and the proof run green for you, and if a test went to the slow tests, did the agent say so, and does the slow-test command in the Verify slot run it?
* Did the documents the delivery changed get updated, and only those?
* Does the staged diff hold only this delivery, and did the agent report anything already staged?
* Is the suggested message in the `commit` block at the end of the page right: the subject, the bullets, the last line?
* What did the delivery review find, and was each candidate fixed or turned into a `[ ]` line?
* Did the review read the whole delivery, its created files and any commits it already made on its branch included, and did verify run again after the last edit it covers?

If the page records no review and docs/05's slot names one, the delivery did not end as the kit says; ask the agent for the review.
Read what happened too, and ask whether you would have decided any divergence otherwise.
Before you commit, use what the delivery built as its user would, in the environment that `/apply`'s last sentence names as holding the delivery, going through what the page changed.
The tests prove what the page wrote and the review reads the code; only using the delivery shows whether it looks right, is easy to use and answers without keeping its user waiting.
This use covers one delivery while it is open; the hand test at a milestone's close goes through its whole paragraph.
What the page asked and the build got wrong or left rough, a button out of place, a label that does not fit, a screen that takes seconds to answer, is a correction of this delivery: verify runs again and the page records it.
What the page did not ask, however small, and a problem that needs a definition of its own become a `[ ]` line, added by conversation with a draft page for what the line cannot hold; ask for it right below this delivery's line, so it is the next free line and its `/propose` starts from what you saw while you still remember it.
On Ninjobs I used each delivery before committing it: that is where I found problems with the interface, with how easy it was to use and with speed that the tests and the reviews had not shown, and where I improved what the agent made, what the page had asked for corrected in the same conversation, while the delivery was open, and the rest written as the next lines of the queue.
Ask the agent for each correction, in the same session, never by hand.
The same session keeps the reasoning of the build: it knows why it made each choice, which a fresh session would have to guess.
That holds for taste as much as for faults: when the code works but you would have written it another way, say what you want instead and why, rather than rewriting it yourself.
A preference that should hold beyond this delivery goes where the next session reads it, a convention in docs/04 or a decision with its reason in an ADR, written in this same delivery.
Whatever memory your host keeps of its own, the memory every host and every colleague reads is the project's documents.
In my experience, early in a project the agent often does things that do not suit the team's taste or needs; saying it once, so it lands in a document, cost me less than fixing the same thing by hand in every delivery.
Treat the agent as a new member of the team: you explain once what the team wants, in a place where it can read it again.

A person who commits after many good deliveries stops checking, and takes the agent's word in place of their own reading.
That is automation bias, defined and measured in chapter 24, and this review counters it in four ways.
It is a set of questions answered against a page you already read, not a glance at a diff.
The page's record of what happened shows where the agent decided alone, so you know where to look.
One page keeps the change small enough to read whole.
And verify and the proof ran before you look, so your attention goes where no check reaches.

## The commit is the human review

The agent stages and suggests the message; the person reads the diff and decides the commit.
Three reasons hold that line.

* **Nothing reaches the history unread by a person.** A commit says a person read the change and accepts it; an agent that commits on its own skips the only reader who can say the build is what was wanted.
* **A commit reverts in one step.** The page and its build are one commit on trunk, one merge on a branch, so a delivery that turns out wrong leaves the project in one command (chapter 18).
* **The person owns what ships.** The agent wrote the code, and the person answers for it to the team, the client and the user; the commit, whoever types it, is where that answer is given.

Read the staged diff, then commit:

```
git diff --staged
git commit
```

With no `-m`, git opens your editor for the message; copy it from the `commit` block at the end of the page, paste it, save and close, and the commit exists when the editor closes.
The page holds the message and the conversation only repeats it, so you can commit the next morning, in another window, and still find it.

Or, once you have read the staged diff, ask the agent: "commit this delivery with the message on its page".
It runs the commit and stops there: a request to commit is not one to merge or to push, and on a delivery branch the merge is a step you name again, after reading the branch (chapter 19).
The agent may have your host's permission to run `git commit`; that permission lets it type the command, and only your request, after your reading, says the change should enter the history.
Then check what it made with `git show --stat HEAD`, which prints the last commit's message and the files it holds: the message from the page, and this delivery's paths and nothing else.

When another session works in the same folder, commit one delivery at a time, from the index, once `git diff --staged` holds only that delivery (chapter 19).

### The message

The format is the one docs/05 defines, and the kit writes the same one into every project:

```
<subject in the imperative, up to 72 characters>

- <a highlight, one line>
- <up to five of them>

work/done/<slug>.md
```

The subject says what the delivery does, in the imperative, "Lend a copy to a member" and not "Lent" or "Lending", with a scope in parentheses when it helps.
The bullets are the highlights, never the reasoning.
The last line points to the page's actual path, where the reasoning lives, so anyone who reads the history finds the whole decision in one file: `work/done/<slug>.md` when the delivery is done.

A blocked `/apply` writes a partial message in the same shape.
It says it is partial and names the blocker, never implies that verify passed or that the delivery is done, and its last line is `work/<slug>.md`, where the page waits.

If your agent answers with `git commit -m` lines and no `commit` block on the page, the delivery did not end as the kit says; ask it for the block.

## What the team gains

Nothing ships without a check and a person: verify and the proof check the build, and a person reads the diff before it exists in the history.
A fault a delivery wrote is found by a reader that did not write it, and fixed in that delivery, before you read the diff.
And what diverged from the plan is written where the next person reads it: on Ninjobs, the page of the delivery that lets a user delete their account said the table recording a pending deletion would have no write rule at all, and the build found that a table with no write rule accepts writes from nobody, the database's own functions included.
So the page recorded the refinement, no write path reachable from the client, which the access-rules test now proves, and the commit that shipped it points to that page.

## Key points

* `/apply <slug>` builds the page in a fresh session and follows docs/05 literally: the page is the scope, with no dependency, layer or tool it did not name, and when the page contradicts a document it stops and says which, never resolving it silently.
* It marks the line `[*]` with its first edit, `[x]` with its last, after the stage, and `[?]`, with what it waits on, when it must stop.
* Green is not done: done is the whole list, from the documents updated before a review by a context that did not write the change, which reads the whole delivery, to verify green after the last edit and the line marked `[x]`.
* It ends the page with the suggested message in a `commit` block and shows the same block in the conversation, also when it stops blocked; its last words are your next steps, each command written out, and, last of all, which environment is at which version and the command that updates the others.
* Use what was built as its user would, review the staged change against the page, ask for each correction in the same session, saying what you want instead and why, make what the page did not ask the queue's next line, and then commit it, yourself or by asking the agent: that review is the defence against automation bias, the habit of trusting the agent after many good deliveries.

[^huang-2024]: Jie Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet", 2024. <https://arxiv.org/abs/2310.01798>
