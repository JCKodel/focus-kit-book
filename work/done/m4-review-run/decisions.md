# Requests

Each request sent to the review's session, word for word, in order.

## Turn 1, the review

````
You are reviewing a book as its reader would meet it, before its next part is written. Edit nothing: read and report.

The book is "One Page at a Time", in this repository, in two editions: English in `book/en/` (the source) and Brazilian Portuguese in `book/pt/` (the translation), with the same file names. Its milestone M4, Part III, has just closed. Your review covers the Prologue and Parts I and II, which Part III builds on, and Part III itself: the chapter files `00-` to `16-` of each edition.

Read, in this order, and nothing else:

1. `docs/00-Product.md`: who the book is for, its values, its contents, and the six product questions under "Product questions".
2. `docs/04-Conventions.md`: the section "Writing the book" and the section "Prose rules".
3. The chapters, one at a time, in order from `00-` to `16-`: for each chapter, first `book/en/<file>`, then `book/pt/<file>`.

Read nothing else from `docs/`, `work/` or `scripts/`. The guided project and its tags exist only as the links the chapters print: take a tag from the link text, and do not look for the project anywhere else.

Read as a reader who has only the chapters before the one in hand. For each chapter ask the product questions, above all question 2: does every sentence carry value, and is anything the reader needs missing? Also ask: can a reader who has read only the previous chapters follow this one (question 5); can the code a chapter prints be followed from what the chapter says about it; and does the Portuguese mean what the English means, not word for word but in substance? Part III is optional in the book, as docs/00's contents say, but it still owes a reader of Parts I and II everything question 5 asks. A finding may be in any chapter from the Prologue to chapter 16.

Do not report what the build already checks: that both editions have the same structure, em dashes, the patterns in "Prose rules", broken links, and names of private cases. Spend your attention on value, on what is missing, on whether each chapter can be followed from the earlier ones alone, on whether its code can be followed from its text, and on the Portuguese meaning.

This is M4's paragraph, the promise of the milestone:

> When this milestone closes, a reader can organize code by feature with exceptions as values, and knows when the four pieces pay their way and when they do not.

Check it clause by clause: for each clause, name the chapter and section that teaches it and the guided project's tag the reader follows there. A clause with nowhere to point to is a finding.

Report in this shape and nothing else. First the findings, one block each, numbered in the order you read them:

    ### F<n>. <one-line summary>
    * Where: `book/<ed>/<file>:<line>`[, `book/<ed>/<file>:<line>`]
    * Question: <1 to 6 of docs/00> | paragraph
    * What: <what is wrong, quoting at most one sentence of the book>
    * Reader: <what a reader loses, one sentence>

Then a section `## Paragraph`, one line per clause, in one of two forms:

    <clause>: <chapter §section> · <tag or "no tag">
    <clause>: FINDING F<n>

If you find nothing in a chapter, say nothing about it. Do not suggest fixes beyond what "What" needs to make the problem clear.
````

## Turn 2, the decisions and the lines

Sent with `--resume` and the review's session.

````
My decisions on the fifteen findings:

F1: confirmed, chapter 3's key point credits both tools with asking before writing, when the run showed Spec Kit asked nothing on its default path.
F2: confirmed, the Portuguese says "horário livre" for a slot of the `slotMinutes` grid in chapter 6's invariant and ADR, the same words it uses for a free slot.
F3: confirmed, chapter 14 never says what makes one feature, and its booking slice holds cancelling while weekly hours and professionals get slices of their own.
F4: confirmed, narrowed: the chapter does say an exception can become a refusal, but its definition ("no I/O involved") and its key point ("a refusal only in a rule") still contradict `SlotTaken`, its main example.
F5: confirmed, `query` catches every thrown value, so a bug inside it becomes `DatabaseFailed`, against the chapter's "Error: a bug, thrown and never caught", and the text does not say so.
F6: confirmed, the Portuguese "fatia de saúde" reads as a slice for medical data, where chapter 10 kept "fatia de health" for the server check.
F7: confirmed, chapter 15's tag holds a delivery of milestone 2 the reader never queued nor was told to build, so a reader's code has no event functions and cannot match the tag.
F8: confirmed, the route reads the request body, which is I/O, against the table's "the only place an infra exception becomes a Result", and neither chapter squares the two.
F9: confirmed, the hook calls `submitEvent` while the text says `submit`, with no word that it is `bookingEvents.ts`'s `submit` imported under another name, and `shown` and `latest` go unexplained.
F10: confirmed, `slotsOf` imports repositories of three other slices, and no chapter says whether a slice may import another slice's code or when it must move to `src/lib/`.
F11: confirmed, every repository function receives `db`, against the key point "no other piece receives a dependency" and "Nowhere else is anything passed".
F12: confirmed, narrowed: the section names the cost of FOCUS whole (ADR-0002, the brownfield project), but gives no case of a piece that has a job and still costs more than it gives, so a reader cannot weigh one.
F13: confirmed, the route test drives the route, the use case, the repository and SQLite, against the definition of a unit test as "one piece of code".
F14: confirmed, the text speaks of one test answering `CancellationTooLate` where the code is an `it.each` over three codes, and `it.each` is never explained.
F15: confirmed, narrowed: the text explains the 33 of 77 of `book-appointment`, but the key point's "20 of 95" has no baseline, so "small" is described, not measured.

Now write the confirmed findings into `docs/06-Queue.md` as a new milestone, `## M4.1. What the review of M4 found`, placed after M4's block and before `## M5`. Give it a paragraph in the form of the other milestones, starting "When this milestone closes, ", and a fenced block with one `[ ]` line per confirmed finding, slug and description in the queue's format and column alignment. If a finding is already covered by an existing line of the queue, add no new line: give the existing line more words only if the finding adds something, and tell me which. Touch nothing else in the file. Then stage it with `git add docs/06-Queue.md` and show me `git diff --cached docs/06-Queue.md`.
````
