# Requests

Each request sent to the review's session, word for word, in order.

## Turn 1, the review

````
You are reviewing the last round of fixes of a book's milestone, before its next part is written. Edit nothing: read and report.

The book is "One Page at a Time", in this repository, in two editions: English in `book/en/` (the source) and Brazilian Portuguese in `book/pt/` (the translation), with the same file names. Its guided project is a small clinic app kept in another repository. Milestone M4.2, the last round of fixes of M4, has just closed: twelve deliveries changed chapters, and two recorded runs changed the clinic's code. This review reads only what M4.2's lines changed, not the whole book.

Read, and nothing else:

1. `work/done/m4.2-review-run/book.diff`: every commit of M4.2 that changed the book, oldest first, from `git log -p --reverse e18dff8..9e9c282 -- book/`. Each commit's subject starts with the slug of the M4.2 line it settles.
2. `work/done/m4.2-review-run/clinic.diff`: the clinic's two commits of M4.2, oldest first, from `git log -p --reverse 6edc9ad..36d7ad9 -- src docs/01-Architecture.md`. Paths in it are the clinic's, not this repository's; the commit subjects end with the run's slug, `(busy-fields)` and `(hours-answer)`.
3. A changed chapter, `book/en/<file>` or `book/pt/<file>`, only to see the section a hunk sits in, and only that section. Do not reread the book.

Read nothing from `docs/`, `work/` or `scripts/` beyond the two diffs. Read both editions of every changed pair.

This is M4.2's paragraph, the promise of the milestone:

> When this milestone closes, every confirmed finding of the M4.1 review is settled: chapter 3's key points say only what its run showed; chapter 7 says which of the clinic's non-negotiables are the kit's; Part III's definitions of a feature and a unit test fit the clinic's code it shows, and it says what the reader does about a bug that the boundary's catch hides; chapter 14's boundary squares with the routes that import a library's type; chapter 15 places every catch in a piece, explains the rule its view excerpt shows, prints the brief the reader is told to answer with, and its key point on when a piece is written meets its section; the clinic's weekly hours editor and booking form take no edit while a save or a booking is in flight, and only the hook can report that a save is in flight; and the Portuguese edition uses the terms chapter 3 taught and summarizes chapter 10's diff as it is.

Check it clause by clause: for each clause, name the changed chapter and section that answers it, or the clinic commit that does. A clause no change answers is a finding.

Report a finding only on a changed line, or on a sentence around it in the same section. Mark each finding blocking or not blocking, with its reason. Blocking means, for the book: a sentence the book shows to be false, or a step the reader cannot follow. For the clinic's code: the code does not do what M4.2's clause says, or a test in the range fails. A finding that is real but meets neither is not blocking.

Do not report what the build already checks: that both editions have the same structure, em dashes, the book's prose patterns, broken links, and names of private cases. Check that the Portuguese means what the English means, not word for word but in substance, on every changed pair.

Report in this shape and nothing else. First the findings, one block each, numbered in the order you read them:

    ### F<n>. <one-line summary>
    * Where: `book/<ed>/<file>:<line>`[, `book/<ed>/<file>:<line>`] | clinic `<path>`
    * Clause: <the clause of M4.2's paragraph it fails, or "none">
    * What: <what is wrong, quoting at most one sentence of the book or one line of code>
    * Reader: <what a reader loses, one sentence>
    * Blocking: yes | no, <why, one sentence>

Then a section `## Paragraph`, one line per clause, in one of three forms. M4.2 made no chapter tag, so a chapter clause answers `no tag`:

    <clause>: <chapter §section> · no tag
    <clause>: clinic <short hash>
    <clause>: FINDING F<n>

If you find nothing, say so in one line before `## Paragraph`. Do not suggest fixes beyond what "What" needs to make the problem clear.
````

## The author's decisions

Not a turn: the author's answer, relayed by the driver of the batch, word for word:

> Não. M4 é M4. Chega de reviews. Senão vamos ficar corrigindo infinitamente.

F1: rejected, the author closes M4: no more rounds of fixes of M4.
F2: rejected, the author closes M4: no more rounds of fixes of M4.
F3: rejected, the author closes M4: no more rounds of fixes of M4.
F4: rejected, the author closes M4: no more rounds of fixes of M4.

## Turn 2

Not sent. Turn 2 exists only to write the kept findings into docs/06; with every finding rejected there is no line to write, so the review's session was not resumed.
