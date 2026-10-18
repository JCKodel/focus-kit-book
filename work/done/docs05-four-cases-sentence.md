# docs05-four-cases-sentence

**Objective.** A session reading docs/05 §4 reads the four cases a line waits in as four, with the fix found in the middle of an /apply an example of the third and the code reading that missed part of its range the fourth.

**Decided without the author.** This page was written in a batch /propose with no question asked (the author's instruction for this run); each decision names its source, so the author corrects it in the review of this page.

1. The sentence becomes a list of four cases separated by semicolons, after "in four cases:", as docs/03:106's waiting mark row writes them; the table row above already says "in the four cases below" (docs/05:109). The example stays inside the third case, and the fourth keeps its "(§8)".
2. The fourth case's reason, what was read, is said in the sentence, as docs/03:106 and ADR-0018's amendment say it; the sentence after, on where the reason goes, does not change.
3. Kit: `kit:` the kit's documents.md writes the same sentence (`m17-review` candidate R4-3, kit side); the author may tell the kit to list the four cases the same way. The kit is not edited here.

**Behaviour.**

* A reader of docs/05 §4 finds one sentence naming four cases: the person says the line is blocked; it needs an answer that was asked and not given; work already started finds it needs another line done first, such as a fix found in the middle of an /apply; a milestone review's code reading missed part of its range, the reason saying what was read (§8).
* Edge: the next sentence, "The reason goes at the end of the line, ...", and the rest of the paragraph read as before.
* Fails, and is fixed before done: any reading where "or when a milestone review's code reading" follows "such as".

**Contract.**

docs/05 §4, lines 115 to 118, exact; /apply rewraps the paragraph to the file's width and changes no other sentence. The sentence "A line waits when the person says it is blocked, when it needs an answer that was asked and not given, or when work already started finds it needs another line done first, such as a fix found in the middle of an /apply, or when a milestone review's code reading missed part of its range (§8)." becomes:

"A line waits in four cases: the person says it is blocked; it needs an answer that was asked and not given; work already started finds it needs another line done first, such as a fix found in the middle of an /apply; or a milestone review's code reading missed part of its range, and its reason says what was read (§8)."

No new term. No chapter changes: chapter 14 teaches the four cases as a list already (`ch14-four-waits`).

Shared files and order: this applies last of this author's four docs/05 lines, after `conflict-same-lines` (docs/05:142-143, :252-254), `docs05-fourth-case-version` (docs/05:134) and `docs05-review-concurrency` (docs/05:232-238). Each is another hunk, more than six unchanged lines from this one; earlier ones may still be staged and not committed when this runs, so /apply stages only this delivery's hunk of docs/05 with `git add -p`, and its own line of docs/06.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* docs/05:134's version sentence: `docs05-fourth-case-version`.
* docs/03:106: already lists four cases.
* The kit's documents.md: the kit's own (decision 3).
* Chapter 13's list of when /apply cannot go on: `ch13-four-waits`, another agent's line.

**Done when.**

* [x] docs/05 §4 holds the Contract's exact sentence.
* [x] `make verify` green.
* [x] The delivery review run as docs/05 §5 says, and recorded.
* [x] Page in `work/done/`, line `[x]`, staged by hunk as the Contract says, commit message in a `commit` block, `kit:` note for the author in the final report.

**Built.** docs/05 §4 holds the Contract's exact sentence, the four cases separated by semicolons, wrapped onto five lines within the paragraph's width; the next sentence and the rest of the paragraph are unchanged.

**Decisions at apply time.** The rewrap stops at the edited sentence: the short line "The reason goes at the end" that follows was already short and stays as it is, so the next sentence is unchanged byte for byte. No Case A or Case B passage.

**Divergences and omissions.** None.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure).

**Delivery review.** One read-only agent on Opus read this delivery's hunk of docs/05 and its line of docs/06 against this page, docs/04, docs/03's waiting mark row and §4's table row. No finding: the sentence matches the Contract, no line runs past the width, no em dash, and "such as" now closes the third case. It suggested, as optional, joining the next short line; kept as is (decision above).

**Kit note for the author.** `kit:` the kit's documents.md writes the same sentence; the author may tell the kit to list the four cases the same way (decision 3).

```commit
docs(docs05-four-cases-sentence): list docs/05's four waiting cases as four

- docs/05 §4 names the four cases a line waits in, separated by semicolons
- The fix found mid /apply stays an example of the third case
- The fourth case's reason says what was read

work/done/docs05-four-cases-sentence.md
```
