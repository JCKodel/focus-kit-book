# Requests

Each request sent to the review's session, word for word, in order.

## Turn 1, the review

````
You are reviewing a book as its reader would meet it, before its next part is written. Edit nothing: read and report.

The book is "One Page at a Time", in this repository, in two editions: English in `book/en/` (the source) and Brazilian Portuguese in `book/pt/` (the translation), with the same file names. Its milestone M4.1, which settled what an earlier review of Part III found, has just closed. Your review covers the Prologue and Parts I and II, which Part III builds on, and Part III itself: the chapter files `00-` to `16-` of each edition.

Read, in this order, and nothing else:

1. `docs/00-Product.md`: who the book is for, its values, its contents, and the six product questions under "Product questions".
2. `docs/04-Conventions.md`: the section "Writing the book" and the section "Prose rules".
3. The chapters, one at a time, in order from `00-` to `16-`: for each chapter, first `book/en/<file>`, then `book/pt/<file>`.

Read nothing else from `docs/`, `work/` or `scripts/`. The guided project and its tags exist only as the links the chapters print: take a tag from the link text, and do not look for the project anywhere else.

Read as a reader who has only the chapters before the one in hand. For each chapter ask the product questions, above all question 2: does every sentence carry value, and is anything the reader needs missing? Also ask: can a reader who has read only the previous chapters follow this one (question 5); can the code a chapter prints be followed from what the chapter says about it; and does the Portuguese mean what the English means, not word for word but in substance? Part III is optional in the book, as docs/00's contents say, but it still owes a reader of Parts I and II everything question 5 asks. A finding may be in any chapter from the Prologue to chapter 16.

Do not report what the build already checks: that both editions have the same structure, em dashes, the patterns in "Prose rules", broken links, and names of private cases. Spend your attention on value, on what is missing, on whether each chapter can be followed from the earlier ones alone, on whether its code can be followed from its text, and on the Portuguese meaning.

This is M4.1's paragraph, the promise of the milestone:

> When this milestone closes, every confirmed finding of the M4 review is settled: chapter 3's key points say what its run showed; Part III says what makes one feature and whether a slice may use another slice's code, and its definitions of a refusal, an error, a unit test and injection fit the clinic's code it shows; chapter 14 tells an error from an exception in any language, says why a throw must not steer the flow, and keeps a library's exceptions out of the domain; it shows a piece that has a job and still costs more than it gives; every excerpt can be followed from its text; a reader following the guided project is told to build the code that chapter 15's tag holds; the clinic's client orchestrators publish every in-flight state as an update of the current state, send the weekly hours editor's reports through one tested event, declare each repeated type once, and take only the event shapes its docs/01 describes; and the Portuguese edition means what the English means.

Check it clause by clause: for each clause, name the chapter and section that teaches it and the guided project's tag the reader follows there. A clause with nowhere to point to is a finding. One clause is the exception: "the clinic's client orchestrators publish every in-flight state as an update of the current state, send the weekly hours editor's reports through one tested event, declare each repeated type once, and take only the event shapes its docs/01 describes" is about the guided project's code, which no chapter teaches, and a separate code review checks it. Answer that clause as `<clause>: m4.1-code-review` and report no finding on it.

Report in this shape and nothing else. First the findings, one block each, numbered in the order you read them:

    ### F<n>. <one-line summary>
    * Where: `book/<ed>/<file>:<line>`[, `book/<ed>/<file>:<line>`]
    * Question: <1 to 6 of docs/00> | paragraph
    * What: <what is wrong, quoting at most one sentence of the book>
    * Reader: <what a reader loses, one sentence>

Then a section `## Paragraph`, one line per clause, in one of three forms:

    <clause>: <chapter §section> · <tag or "no tag">
    <clause>: FINDING F<n>
    <clause>: m4.1-code-review

If you find nothing in a chapter, say nothing about it. Do not suggest fixes beyond what "What" needs to make the problem clear.
````

## Turn 2, the decisions and the lines

Sent with `--resume` and the review's session.

````
My decisions on the fourteen findings:

F1: confirmed, the Portuguese says "change", "spec" and "specs" in chapters 1, 4 and 13 where chapter 3 taught "mudança" and "especificação", with no gloss.
F2: rejected, the paragraph credits the file with surviving a fresh session and a compaction, and "near the beginning of the window" claims no advantage over a first message.
F3: confirmed, chapter 3's key point credits OpenSpec with rules written once per project, which the section never shows.
F4: confirmed, the AGENTS.md excerpt of chapter 7 says "three fixed lines" but four lines follow the project's, and "An open decision in docs/00 is asked, never assumed." fits neither group.
F5: confirmed, the Portuguese summary of the skeleton diff puts exit code 1 in the Contract, where the diff has it in Behaviour, and leaves out the data/ folder.
F6: confirmed, "A feature is one thing the app keeps" leaves no place for the health slice, which keeps nothing.
F7: confirmed, narrowed: chapter 14 says query's catch turns a bug into DatabaseFailed that nobody sees, but not what the reader does about it, and reason 4 uses the same query as its example of harm.
F8: confirmed, narrowed: the repository is the I/O piece, so SQLite's text there fits; the routes importing DatabaseSync's type do not square with "changes that code alone".
F9: confirmed, chapter 15 tells the reader to answer with the author's brief but leaves it behind a note, where chapters 7, 8 and 10 print theirs.
F10: confirmed, narrowed: request and remembered.ts are client repositories, but openDatabase and migrate catch in no piece, against the table's "the only place an infra exception becomes a Result".
F11: confirmed, narrowed: tooLateToCancel is a rule's outcome in the view, and the text never says it comes from the use case the client imports.
F12: confirmed, narrowed: the section says the clinic pays for one shape across hooks, not for healthEvents.ts, but the key point states only "gives more than it costs", so the two do not meet.
F13: confirmed, narrowed: "runs whatever that piece calls" is false for the fakes and stubs the chapter shows, as its own next sentence names fake repositories.
F14: rejected, the text says a slice bounds where an agent reads, not how much, and says it has no run without slices.

Now write the confirmed findings into `docs/06-Queue.md` as a new milestone, `## M4.2. What the review of M4.1 found`, placed after M4.1's block and before `## M5`. Give it a paragraph in the form of the other milestones, starting "When this milestone closes, ", and a fenced block with one `[ ]` line per confirmed finding, slug and description in the queue's format and column alignment, ending with the line `[ ] m4.2-review` whose description follows `m4.1-review`'s, for M4.2 and a new milestone M4.3. If a finding is already covered by an existing line of the queue, add no new line: give the existing line more words only if the finding adds something, and tell me which. Touch nothing else in the file, M4.1's lines included. Write in English, with no em dash. Then stage it with `git add docs/06-Queue.md` and show me `git diff --cached docs/06-Queue.md`.
````
