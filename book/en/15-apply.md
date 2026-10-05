# 15. `/apply`: build, verify, prove, never commit

After this chapter you can follow a reviewed page to a staged change with `/apply`, and say what "done" means: verify green, a proof, the documents updated, the page moved and its line marked.
You can then review the staged change against the page and commit it yourself, which is the human review of the process.

## The problem

An agent that is told "build this" stops when the code compiles, or when the tests it wrote pass.
What it built around the request, what it chose on its own and which documents no longer say the truth are left for someone to find later, and that someone is usually a user.
And an agent that commits its own work puts it in the project's history before any person has read it.

## What `/apply` does

`/apply <slug>` builds the delivery that `work/<slug>.md` describes, completely, in one session: the code, the tests, the proof and the documents.
It starts in a fresh session, so the page is all it takes from the conversation that wrote it, which is why chapter 14 asks you to read the page before this command runs.

### What it reads

The page, `AGENTS.md`, and three of the project documents: docs/01, the architecture, which says where each piece goes and how errors travel; docs/04, the conventions, which say which tests to write; and docs/05, the process.
docs/05 holds the project's slots, and `/apply` follows them literally: the verify command, the environments and what a delivery leaves in each, how a screen is proven, the publish policy and the git strategy.
Then it marks the line `[*]` in docs/06, so the queue shows the build under way; on a line that is `[?]`, it first says what the line waits on, and goes on only when you say it is resolved.

### The page is the scope

What the page asks is what gets built, and nothing around it.
The kit's file for the command says it in one line: "*The page is the scope; do not widen it.*"
So `/apply` adds no dependency, layer or tool the page did not name, and writes an abstraction only on the second concrete occurrence, saying which was the first (chapter 4).
A package the page did not name is a question for the person, never a choice for the agent.

### When the page contradicts a document

It stops and says which.
Either the document changes in the same delivery, or the page is wrong; it never picks one silently.
A silent choice would leave a page and a document that disagree, and the next session would build on whichever it read first.

### When the work cannot go on

It stops when the build needs an answer nobody has given yet, when another line must be done first (a fix it found becomes a `[ ]` line above this one), or when you say it is blocked.
It writes on the page what was built and what it waits on, leaves the page in `work/`, marks the line `[?]` with that reason at its end, and stages what it has (chapter 16).

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
* It ticks every item of Done when.
* It moves the page to `work/done/`, and turns the line's mark in docs/06 from `[*]` to `[x]`; a `[?]` line that waited only on lines now `[x]` goes back to `[>]`, or to `[ ]` when it has no page.
* It stages everything and suggests the commit message in the format docs/05 defines.
* The last thing it says is which environment is at which version, and the command that updates the others.

Done is that whole list: verify green, the proof, what happened written on the page, the documents updated, the page in `work/done/`, the line `[x]`, and the change staged.

## `lend-book`, built

Take the `lend-book` page of chapter 14, reviewed and marked `[>]`, and open a fresh session with `/apply lend-book`.

The agent reads the page, then docs/01 to learn that loans live in `src/features/loans/`, docs/04 to learn which tests each piece gets (chapter 8), and docs/05 to learn that verify is `npm run verify` and that a screen is proven by a screenshot.
It writes the migration for the table `loan` with its unique index, the rule `lend` as a pure function returning a `Result` (chapter 5), the repository call that turns the unique index's failure into the refusal `AlreadyLent`, the orchestrator and the lending screen.
Each Behaviour line becomes a test: the loan with its due date 21 days ahead, the refusal for an overdue book, and, against a real in-memory database, the second of two loans on the last copy refused.
It builds nothing for returning a copy, reservations or fines, because Out of scope named them.

If docs/00 said a loan lasts 14 days, the agent would stop at that line and ask which one is true: the page's 21 or the document's 14.
Whichever you answer, the other one changes in the same delivery.

It runs `npm run verify` until it is green, takes the lending screen at 390 and 1280 pixels wide, and compares both with the design file.
If a button wraps at the narrow width, it gets fixed; if the design file gives no value for a colour, the choice is written down as a divergence, with its reason.
Then it writes what happened on the page, adds the table `loan` to the document that lists the schema, ticks Done when, moves the page to `work/done/lend-book.md`, marks the line `[x]`, stages everything, suggests the message, and ends by saying which environment runs this delivery and how to update the others.

## Why it stops at the stage

`/apply` never commits and never merges, whatever the git strategy.
It stages everything and hands you the message; the commit is yours, and it comes after your review.
The kit's process document gives the flow in one line: `/apply` "*builds, proves, updates the documents, stages and suggests the commit, never commits*".

## Review the staged change

The staged change is what the agent says it did; your review checks that it did it.
Read it against the page:

* Is every Behaviour line answered, each by its test or a recorded check?
* Is anything built that the page did not ask for: a file, a dependency, a layer?
* Do verify and the proof run green for you?
* Did the documents the delivery changed get updated, and only those?
* Is the suggested message right: the subject, the bullets, the last line?

Read what happened too, and ask whether you would have decided any divergence otherwise.
Ask the agent for each correction, in the same session, never by hand.
The same session keeps the reasoning of the build: it knows why it made each choice, which a fresh session would have to guess.

## The commit is the human review

The agent stages and suggests the message; the person reads the diff and commits.
Three reasons hold that line.

* **Nothing reaches the history unread by a person.** A commit says a person read the change and accepts it; an agent that commits its own work skips the only reader who can say the build is what was wanted.
* **A commit reverts in one step.** The page and its build are one commit on trunk, one merge on a branch, so a delivery that turns out wrong leaves the project in one command (chapter 20).
* **The person owns what ships.** The agent wrote the code, and the person answers for it to the team, the client and the user; the commit is where that answer is given.

Read the staged diff, then commit:

```
git diff --staged
git commit
```

With no `-m`, git opens your editor for the message; paste the suggested one, save and close, and the commit exists when the editor closes.

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
The last line points to the page in `work/done/`, where the reasoning lives, so anyone who reads the history finds the whole decision in one file.

## What the team gains

Nothing ships without a check and a person: verify and the proof check the build, and a person reads the diff before it exists in the history.
And what diverged from the plan is written where the next person reads it.
On Ninjobs, the page of the delivery that lets a user delete their account said the table recording a pending deletion would have no write rule at all.
The build found that a table with no write rule accepts writes from nobody, the database's own functions included, so the page recorded the refinement: no write path reachable from the client, which the access-rules test now proves.
The decision and its reason are on the page that built it, and the commit that shipped it points there.

## Key points

* `/apply <slug>` builds the page in a fresh session, and the page is the scope: no dependency, layer or tool the page did not name.
* It marks the line `[*]` when it starts, `[x]` when it is done, and `[?]`, with what it waits on, when it must stop.
* It follows docs/05 literally, and when the page contradicts a document it stops and says which; it never resolves it silently.
* Green is not done: done is verify green, the proof, what happened on the page, the documents updated, the page in `work/done/`, the line `[x]` and the change staged.
* Review the staged change against the page, and ask for each correction in the same session.
* The agent stages and suggests the message; the person reads the diff and commits, so nothing reaches the history unread, and a delivery reverts in one step.

