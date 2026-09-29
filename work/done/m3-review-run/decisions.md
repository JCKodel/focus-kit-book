# Requests

Each request sent to the review's session, word for word, in order.

## Turn 1, the review

````
You are reviewing a book as its reader would meet it, before its next part is written. Edit nothing: read and report.

The book is "One Page at a Time", in this repository, in two editions: English in `book/en/` (the source) and Brazilian Portuguese in `book/pt/` (the translation), with the same file names. Its milestone M3, Part II, has just closed. Your review covers the Prologue and Part I, which Part II builds on, and Part II itself: the chapter files `00-` to `13-` of each edition.

Read, in this order, and nothing else:

1. `docs/00-Product.md`: who the book is for, its values, and the six product questions under "Product questions".
2. `docs/04-Conventions.md`: the section "Writing the book" (the Voice bullet is among them) and the section "Prose rules".
3. The chapters, one at a time, in order from `00-` to `13-`: for each chapter, first `book/en/<file>`, then `book/pt/<file>`.

Read nothing else from `docs/`, `work/` or `scripts/`. The guided project and its tags exist only as the links the chapters print: take a tag from the link text, and do not look for the project anywhere else.

Read as a reader who has only the chapters before the one in hand. For each chapter ask the product questions, above all question 2: does every sentence carry value, and is anything the reader needs missing? Also ask: can a reader who has read only the previous chapters follow this one (question 5), and does the Portuguese mean what the English means, not word for word but in substance? A finding may be in any chapter from the Prologue to chapter 13.

Do not report what the build already checks: that both editions have the same structure, em dashes, the patterns in "Prose rules", broken links, and names of private cases. Spend your attention on value, on what is missing, on whether each chapter can be followed from the earlier ones alone, and on the Portuguese meaning.

This is M3's paragraph, the promise of the milestone:

> When this milestone closes, a reader can install the kit, document a new or an existing project, and deliver a milestone with `/propose` and `/apply`, following the guided project.

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

Sent twice with the same text: first with `--continue`, which reached the wrong session and was stopped (README), then with `--resume`.

````
My decisions on the nineteen findings:

F1: confirmed, chapter 1 counts OpenSpec changes and lines of spec before the reader has met either, and points only to chapter 4 when chapter 3 is where OpenSpec is explained.
F2: confirmed, chapter 3 counts edits to docs/03 and docs/06 without saying what they are or that chapter 6 explains them.
F3: confirmed, the rules "A queue" and "The agent never commits" have no failure behind them, although the chapter opens by promising one for each rule.
F4: confirmed, chapter 4 leans on ADRs and docs/05 with no word of what they are and no pointer to chapter 6.
F5: confirmed, the sentence explaining the prompt file's last line exists only in the Portuguese, so the English source must gain it.
F6: confirmed, chapter 6 promises the reader can decide where a new fact belongs and never places one, in the text or in an exercise.
F7: confirmed, "section 6" sits inside the description of docs/04 and reads as docs/04's own section, not this chapter's "Living documents".
F8: confirmed, the Portuguese says "prepara" in chapters 4 to 6 and "coloca em stage" from chapter 7 for the same git step, and must use one term.
F9: confirmed, chapter 5 teaches the tag form `book-v1/<chapter-slug>` and chapter 8 uses `book-v1-analyze` without saying why the brownfield project needs a hyphen.
F10: confirmed, `acceptEdits` is a host permission mode no chapter has explained, and the reader cannot tell whether the gap will reach them.
F11: confirmed, "It" in chapter 9 has no clear antecedent, so the reader does not learn what tells `/apply` the page exists.
F12: confirmed, chapter 10's "One unit of work" repeats chapter 9's paragraph on trunk and the waiting page, where a pointer would do.
F13: confirmed, the `/usage` percentages do not say what they are a share of, so the ratio drawn from them cannot be judged.
F14: confirmed, narrowed: the chapters name the second agent, but never say that the book's runs are headless, what `--continue` does, or that in an interactive session the reader simply keeps talking in the same session.
F15: confirmed, chapter 11 asks whether every Done when item is ticked and shows its own page committed with one unticked, without saying why that item stayed open.
F16: confirmed, chapter 11 promises the reader will commit the staged change and never shows the command that commits it with the suggested message; chapter 17 can teach the rest.
F17: confirmed, between chapters 11 and 12 the reader is never told to build the rest of milestone 1 with `/propose` and `/apply`, nor given a tag to compare against, so the paragraph's "deliver a milestone, following the guided project" has nowhere to point.
F18: confirmed, the English list of the ten summaries is unnumbered while the decisions refer to them by number, and the Portuguese numbers them.
F19: confirmed, "spec delta" and "specialized subagent" appear in chapter 13 without any earlier chapter having met them.

Now write the confirmed findings into `docs/06-Queue.md` as a new milestone, `## M3.1. What the review of M3 found`, placed after M3's block and before `## M4`. Give it a paragraph in the form of the other milestones, starting "When this milestone closes, ", and a fenced block with one `[ ]` line per confirmed finding, slug and description in the queue's format and column alignment. If a finding is already covered by an existing line of the queue, add no new line: give the existing line more words only if the finding adds something, and tell me which. Touch nothing else in the file. Then stage it with `git add docs/06-Queue.md` and show me `git diff --cached docs/06-Queue.md`.
````
