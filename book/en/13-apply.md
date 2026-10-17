# 13. `/apply`: build, verify, prove, never commit

After this chapter you can follow a reviewed page to a staged change with `/apply`, and say what "done" means: verify green, a proof, the documents updated, the page moved and its line marked.
You can then review the staged change against the page and commit it yourself, which is the human review of the process.
And you can say how `/apply` ends: only its delivery staged, the suggested message in a `commit` block on the page and in the conversation, your next steps written out and, last of all, which environment is at which version.

## The problem

An agent that is told "build this" stops when the code compiles, or when the tests it wrote pass.
What it built around the request, what it chose on its own and which documents no longer say the truth are left for someone to find later, and that someone is usually a user.
And an agent that commits its own work puts it in the project's history before any person has read it.

## What `/apply` does

`/apply <slug>` builds the delivery that `work/<slug>.md` describes, completely, in one session: the code, the tests, the proof and the documents.
It starts in a fresh session, so the page is all it takes from the conversation that wrote it, which is why chapter 12 asks you to read the page before this command runs.

### What it reads

The page, `AGENTS.md`, and three of the project documents: docs/01, the architecture, which says where each piece goes and how errors travel; docs/04, the conventions, which say which tests to write; and docs/05, the process.
docs/05 holds the project's slots, and `/apply` follows them literally: the verify command, the environments and what a delivery leaves in each, how a screen is proven, the publish policy and the git strategy.
Of docs/06, the queue, it reads all of it: it must see that the lines its `· after` names are done before it starts, and it names the next free line when it ends.
So every word on a line is read by every build as well as by every definition (chapter 11).
Then, as its first edit, it marks the line `[*]` in docs/06, so the queue shows the build under way; on a line that is `[?]`, it first says what the line waits on, and goes on only when you say it is resolved.

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

It stops when the build needs an answer nobody has given yet, when another line must be done first (a fix it found becomes a `[ ]` line above this one), or when you say it is blocked.
It writes on the page what was built and what it waits on, leaves the page in `work/`, marks the line `[?]` with that reason at its end (chapter 14).
It ends the page with a partial message in a `commit` block and shows the same block in the conversation.
On trunk it stages nothing: the work stays uncommitted, and out of the index, until it is whole.
On a delivery branch it may stage the partial work for you to commit there, and the branch stays unmerged until the delivery is done (chapter 19).

### Verify and the proof

It runs the verify command until it is green.
Then it proves the delivery the way docs/05 says: a screenshot against the design, a run from end to end, or a check by hand.
It lists what diverges from the reference and fixes it, until only what it can justify remains.
A failure is part of the proof and is recorded, never hidden.

### Green is not done

Verify tells you the code does what its tests say.
It says nothing about whether the page was answered, whether the documents still hold, or whether anyone can tell later what happened.
So before it stops, `/apply` does all of this:

* It writes into the page what happened: what diverged from the plan and why, what was dropped, what the proof found, and the decisions taken, with an ADR if one was needed.
* It updates the documents the delivery changed: a new term into docs/03, a new rule into the document that owns it, a decision into docs/adr/.
* When the delivery adds or changes something a person does by hand, such as publishing the app, it writes or updates its manual in `docs/manuals/` ([chapter 7](07-the-documents.md)).
* It ticks every item of Done when.
* It moves the page to `work/done/`; a `[?]` line that waits only on this one, or on lines already `[x]`, goes back by its resume phase ([chapter 14](14-queue-states.md)).
* It stages only this delivery's paths and hunks, never with `git add -A` or `git add .`, and reports what someone else had already staged without unstaging it.
* It ends the page with the suggested commit message in a `commit` block, in the format docs/05 defines, and shows the same block in the conversation, where a fenced block stands apart from the rest of the reply. There is one block: a resumed `/apply` replaces the earlier one.
* Its last edit marks the line `[x]` in docs/06 and stages that hunk, after everything else is staged, so a line marked `[x]` with nothing staged is a session that stopped early.
* Its last words are your next steps: review the staged diff, commit (and merge, on a delivery branch), and take the queue's next line, with its command written as your host invokes it, in a fresh session, so a person new to the kit does not search the documentation for what comes after. The last thing it says is which environment is at which version and the command that updates the others, and it never ends silent about it.

Done is that whole list.

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
Then it writes what happened on the page, adds the table `loan` to the document that lists the schema, ticks Done when, moves the page to `work/done/lend-book.md`, stages only this delivery's paths, and, as its last edit, marks the line `[x]` and stages that hunk of docs/06.
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

`/apply` never commits and never merges, whatever the git strategy.
It stages only its delivery and hands you the message; the commit is yours, and it comes after your review.
The kit's process document gives the flow in one line: `/apply` "*builds, proves, updates the documents, stages and suggests the commit, never commits*".

## Review the staged change

The staged change is what the agent says it did; your review checks that it did it.
Read it against the page:

* Is every Behaviour line answered, each by its test or a recorded check?
* Is anything built that the page did not ask for: a file, a dependency, a layer?
* Do verify and the proof run green for you?
* Did the documents the delivery changed get updated, and only those?
* Does the staged diff hold only this delivery, and did the agent report anything already staged?
* Is the suggested message in the `commit` block at the end of the page right: the subject, the bullets, the last line?

Read what happened too, and ask whether you would have decided any divergence otherwise.
Ask the agent for each correction, in the same session, never by hand.
The same session keeps the reasoning of the build: it knows why it made each choice, which a fresh session would have to guess.

A person who commits after many good deliveries stops checking, and takes the agent's word in place of their own reading.
That is automation bias, defined and measured in chapter 24, and this review counters it in four ways.
It is a set of questions answered against a page you already read, not a glance at a diff.
The page's record of what happened shows where the agent decided alone, so you know where to look.
One page keeps the change small enough to read whole.
And verify and the proof ran before you look, so your attention goes where no check reaches.

## The commit is the human review

The agent stages and suggests the message; the person reads the diff and commits.
Three reasons hold that line.

* **Nothing reaches the history unread by a person.** A commit says a person read the change and accepts it; an agent that commits its own work skips the only reader who can say the build is what was wanted.
* **A commit reverts in one step.** The page and its build are one commit on trunk, one merge on a branch, so a delivery that turns out wrong leaves the project in one command (chapter 18).
* **The person owns what ships.** The agent wrote the code, and the person answers for it to the team, the client and the user; the commit is where that answer is given.

Read the staged diff, then commit:

```
git diff --staged
git commit
```

With no `-m`, git opens your editor for the message; copy it from the `commit` block at the end of the page, paste it, save and close, and the commit exists when the editor closes.
The page holds the message and the conversation only repeats it, so you can commit the next morning, in another window, and still find it.

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
And what diverged from the plan is written where the next person reads it: on Ninjobs, the page of the delivery that lets a user delete their account said the table recording a pending deletion would have no write rule at all, and the build found that a table with no write rule accepts writes from nobody, the database's own functions included.
So the page recorded the refinement, no write path reachable from the client, which the access-rules test now proves, and the commit that shipped it points to that page.

## Key points

* `/apply <slug>` builds the page in a fresh session and follows docs/05 literally: the page is the scope, with no dependency, layer or tool it did not name, and when the page contradicts a document it stops and says which, never resolving it silently.
* It marks the line `[*]` with its first edit, `[x]` with its last, after the stage, and `[?]`, with what it waits on, when it must stop.
* Green is not done: done is the whole list, from what happened written on the page to the line marked `[x]`.
* It ends the page with the suggested message in a `commit` block and shows the same block in the conversation, also when it stops blocked; its last words are your next steps, each command written out, and, last of all, which environment is at which version and the command that updates the others.
* Review the staged change against the page, ask for each correction in the same session, and commit it yourself: that review is the defence against automation bias, the habit of trusting the agent after many good deliveries.

