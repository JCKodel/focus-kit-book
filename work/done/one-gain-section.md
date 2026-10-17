# one-gain-section

**Objective.** Every chapter of both editions ends with one gain section whose key points do not repeat it, and the book says once, in the prologue, that it measures no baseline against a team without the method; docs/04 holds the rule.

**Decided from the documents.**
1. docs/04 §Chapter shape keeps `## What the team gains` and `## Key points` in every chapter; this delivery changes what they hold, not the shape (ADR-0015 and ADR-0017 fixed the shape; a shape change is an ADR, which no error asks for).
2. A key point is what the reader takes to their project, one line each, at most five; it does not restate the gain's sentence or carry its number again beyond the one number or pair docs/04 allows (Numbers that prove; "or pair" since `docs04-gain-number`, corrected here as that page asked). The rule goes in docs/04 §Writing the book as a bullet, **One gain**, after **Numbers that prove**, saying: the gain is said in `## What the team gains`; a key point says what to do, not what is gained; "no baseline" is the prologue's sentence, not a chapter's.
3. `## What this gives an agent` in chapters 6 and 8 merges into each chapter's gain: what the agent gets is what the team gains (docs/00 product question 7; the two sections say the same in both chapters). After `focus-and-slices` and `ch8-testing-trim`, which run before this line, the merge may already be done; this line checks and finishes it.
4. The prologue says once: no study in this book measures a team with the method against the same team without it; the evidence is each chapter's number, counted on real projects, or the loss the practice avoids. The ten sentences of "no number", "no baseline", "no measure" in chapters 2, 6, 7, 8, 11, 12, 17, 20, 21, 22 leave; a gain that has no number keeps its sentence of gain without the disclaimer (docs/04 line 45 allows "one sentence saying the gain has no number"; this line changes that allowance to the prologue's sentence).
5. Where a gain section repeats the chapter's opening or its last section word for word, the gain keeps the sentence and the other place keeps its own (docs/04, No filler); the review found this in chapters 1, 2, 7, 11, 13, 15, 21 and 26, and `method-said-once`, `ch20-21-git-cut` and `ch22-26-team-cut` cut most; this line checks every chapter.
6. This line runs after every cut line of M15 and before `m15-review`, and is the last pass over the whole book; it names what it changed per chapter on this page.

**Behaviour.**

* In every chapter, both editions, `## What the team gains` is one section of one to four sentences with at most the chapter's one number; `## Key points` has at most five bullets, each an action or a rule, none a restatement of the gain's sentence; `grep -c "^## " ` per chapter is the same in both editions.
* The prologue has the one sentence on the missing baseline, in §What the team gains or where its gain is, and `grep -il "no baseline\|no number for this gain\|no measured\|no measure of this gain\|gives no baseline" book/en/0[1-9]-*.md book/en/[12]?-*.md` lists no file; the Portuguese equivalents likewise.
* Chapters 6 and 8 have no `## What this gives an agent`; what those sections said is in the gain, once.
* A reader who reads only the key points of a chapter can act on each one (write the line this way, ask for the file behind the answer, run the review against the commit) and finds the gain's number at most once.
* Fails: a gain cut to nothing; a key point that says "the team gains X" with no action; a chapter whose gain has no number and no sentence of gain either; a chapter where the prologue's sentence is pasted again.

**Contract.**

* **docs/04 §Writing the book**: new bullet **One gain** after **Numbers that prove**: "The gain is said in `## What the team gains`, once; a key point says what the reader does, not what is gained, and carries at most the gain's one number. That the book measures no baseline against a team without the method is the prologue's sentence, said nowhere else (first: `one-gain-section`, from the author's review of 2026-10-16)." docs/04 §Chapter shape's line on `## What the team gains` loses "or one sentence saying the gain has no number".
* **Prologue** (the file `prologue-and-why` produces), both editions: one sentence on the baseline, placed in its gain section.
* **Every chapter 1 to 26** (numbers as `renumber-chapters` leaves them), both editions: the gain section and the key points checked against Behaviour; the "no baseline" sentences removed from chapters 2, 6, 7, 8, 11, 12, 17, 20, 21, 22 or wherever they still are; chapters 6 and 8 without `## What this gives an agent`.
* **This page**, after /apply: a table, one row per chapter, with what changed (gain sentences removed, key points rewritten, section merged) or "nothing".
* **Terms:** none new. **Sources:** none; a note whose only reference was in a removed sentence moves to the sentence that keeps the claim or leaves with it, and the page lists each. **Cases:** no Case A or B passage reworded. **Code:** none.

**Out of scope.**

* The chapter shape itself (two sections stay): changing it is an ADR, and no error asks for it.
* The cuts inside the sections of each chapter: the other M15 lines.
* A `check_prose.py` rule for a key point that repeats the gain: no pattern separates it from a key point that names the gain's number once (docs/05 §7).
* Appendices: none exist in the shape (docs/04).

**Done when.**

* [x] docs/04 holds **One gain** and the shape line is changed.
* [x] The grep of Behaviour lists no file in either edition; the prologue holds the one sentence.
* [x] Every chapter's gain and key points read as Behaviour says, both editions; the per-chapter table is on this page.
* [x] Every note definition keeps a reference; `make verify` green; `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Decisions in the review.**

* Key points are kept in every chapter and rewritten so that none restates the gain, as recommended; docs/04's shape and ADR-0015 stand.
* The prologue's baseline sentence goes in its gain section, as recommended.

**Chapter numbers.** This page was written before `renumber-chapters`; every chapter number above is the old one. They were resolved through the old-to-new map in `work/done/renumber-chapters.md` (file slugs unchanged): "every chapter 1 to 26" is the prologue and chapters 1 to 24; "chapters 6 and 8" with `## What this gives an agent` are the new 4 and 5; the record below uses the new numbers only. The disclaimers were not exactly where the old list pointed: they stood in the new 1, 4, 8, 9, 10, 15, 18, 20 and 23, and the prologue's own sentence covered Part I only.

**What happened.**

* docs/04 §Writing the book gains **One gain** after **Numbers that prove**, with "one number or pair" as `docs04-gain-number` left that bullet; **A gain per chapter** loses "or one sentence saying the gain has no number" and now reads "with its number or a sourced claim where the book has one, and otherwise the gain alone, with no sentence on the missing number". The page placed that phrase in §Chapter shape; it lives in **A gain per chapter**, which is where it was changed (§Chapter shape's block never held it).
* docs/00 product question 7 asked for "one sentence that it has none"; it owns the same rule, so it changes too: the gain is said once, with its number or a sourced claim where the book has one, and the prologue says once that no study measures a team with the method against the same team without it.
* The prologue's sentence on Part I ("This book measures no baseline for the practices of Part I...") is replaced, in its gain section, by the one sentence for the whole book: no study in this book measures a team with the method and its practices against the same team without them; the evidence in each chapter is its number, counted on a real project and saying where it comes from, or the loss its practice avoids.
* `## What this gives an agent` was already gone from both editions: `focus-and-slices` (chapter 4) and `ch8-testing-trim` (chapter 5) folded it into each gain. Decision 3 is checked, nothing left to finish.
* Behaviour's grep lists no file in either edition, and a wider search ("no number", "no measure", "baseline"; pt "não há número", "não há medida", "linha de base", "não tem número", "nada disso tem") finds only chapter 22's "the count sets a baseline" (a project's own count to compare milestones, not a disclaimer) and chapter 23's signed baseline document of Case A.
* Every chapter has at most five key points (11, 13 and 14 had 7, 9 and 7), at most four gain sentences outside the prologue, and the same `## ` count in both editions.

**Per chapter** (both editions alike):

| Ch. | What changed |
|---|---|
| Prologue | Gain: the Part I baseline sentence replaced by the book's one sentence. Key point 5, which repeated the gain's second sentence word for word, now says what to do: write each decision where an agent reads it, and ask the project before a colleague. |
| 1 | Gain: two paragraphs of six sentences to four; "There is no measure of this gain in this book" left, its evidence kept ("the loss this avoids, which the studies above measured"). Key point 5, a restatement of the gain, rewritten as an action: commit each page with its code, ask the agent and not a colleague. |
| 2 | nothing |
| 3 | nothing |
| 4 | Gain: three paragraphs of eight sentences to four, "removing a feature is removing a folder" left (said in §Vertical slices), the client and server orchestrator detail left; the no-baseline sentence `focus-and-slices` kept until this rule existed is gone. Key point 5, a restatement of the gain's last sentence, rewritten as an action: on the client import the server's use case, never a second copy of the rule. |
| 5 | nothing (`ch8-testing-trim` had already merged the agent section into four sentences) |
| 6 | Key point 1 (the gain's "four screens in fifteen days" and its causes, said again) cut: key point 4 already lists the failures. Key point 3 lost "and reached the public opening thirteen days later", the gain's number, and became an action: start from the least that held on Ninjobs. Four key points. |
| 7 | Gain's second sentence reworded so it does not repeat §The problem's "On Ninjobs a decision lived in six places". |
| 8 | Gain: "There is no number for this gain: it is a property of plain files." left. |
| 9 | Gain: "There is no number for this gain: this book has no count..." left. |
| 10 | Gain: the clause "there is no number for this gain, since the book counted no reader's first delivery" left. |
| 11 | Gain: the paragraph "Three rules of the queue each prevent an error" and its three sentences left; each rule's reason is already where the rule is taught (§Size and order: no priority field to keep in step; §Changing the queue: an edit on the spot skips the line, the page, the test and the review; §The line: every word on a line is read by every definition). Key points 7 to 5: the milestone paragraph merged with its size and order, the priority merged with `· after`. |
| 12 | Gain: the paragraph "`/propose` decides and drafts because each prevents an error" left. Its first reason was already in §What `/propose` does ("you correct it once, in the review, instead of answering the same question twice"); the second, the happy-path solution the client rejects, moved as a clause to §Read the page before `/apply`, after "ask the agent for the cases that must fail". |
| 13 | Gain: eight sentences to three. "The way `/apply` ends prevents two errors" left: the `commit` block's reason is already in §The commit is the human review ("you can commit the next morning, in another window, and still find it"); the Ninjobs stale site moved as one sentence to §`lend-book`, built, after "ask it for the sentence". The account-deletion story stays in the gain as its evidence, in two sentences. Key points 9 to 5: scope and docs/05 merged, the `commit` block and the last words merged, the review, automation bias and the person's commit merged; "nothing reaches the history unread", the gain's first sentence again, left. |
| 14 | Key points 7 to 5: the six marks merged with when a mark changes; waiting merged with leaving `[?]`. Gain unchanged (a Case A passage). |
| 15 | Gain: "This gain has no number in this book." left. |
| 16 | nothing |
| 17 | nothing |
| 18 | Gain: the lending library's log, shown in full earlier in the chapter, no longer printed again; one sentence points to it and says what it shows. "There is no number for this gain..." left. |
| 19 | Gain: the run's pair (155 seconds against 277.2) kept; "155 MB of `node_modules` per worktree" became "a `node_modules` folder in each worktree", the cost without a second figure; `[^parallel-run]` kept at the claim. |
| 20 | Gain: the prefix "There is no measured number for this gain:" left; the Case A sentence that followed, that its board ran on one project and its write permission was never proven, kept unreworded as the gain's limit. |
| 21 | Key point 5, which repeated the gain's Case B sentence, became the action alone: give every finding a line, or it gets lost. The gain, with Case A's and Ninjobs' counts and Case B, unchanged. |
| 22 | Key point 2 (the gain's 43.1 M tokens again) cut; its "nearly all of them cache reads" moved into key point 3. Four key points. |
| 23 | Gain: "There is no outside number to compare adoption against; the pilot's own milestone is the baseline." left. Key point 3, the gain's Case A sentence again, cut. Four key points. |
| 24 | Key point 5, the gain's pair again with the advice last, rewritten with the action first and the cost alone: send the protocol where the result is used often or read in a hurry. |

**Sources.** No note lost its reference: every `[^key]:` definition in both editions is still cited (checked per file). No note was attached to a removed sentence.

**Cases.** No Case A or Case B passage was reworded. Two were removed where they repeated the gain: chapter 21's key point 5 (Case B's fault reaching the next version) and chapter 23's key point 3 (Case A's four problems); chapter 20's Case A sentence lost only the prefix before it.

**Decisions taken alone** (batch run, no questions asked):

* The one-to-four-sentence limit of Behaviour was applied to every gain, including the reasons `method-said-once` had left in chapters 11 and 13's gains as one sentence each: docs/04 §Say it where the doubt is born puts a rule's reason where the rule is taught, so each reason was cut where the body already had it and moved as a clause where it did not. Nothing those deliveries cut came back.
* The prologue's gain keeps more than four sentences: besides its gain and the baseline sentence, it holds the private-case sentences docs/04 §Chapter shape places there and the map of the five parts, which is the shape's, not a gain; neither was moved (out of scope).
* The baseline sentence says "the method and its practices", so it covers Part I's practices as the old sentence did and the method's chapters too.
* docs/04 **A gain per chapter** reads "with its number or a sourced claim where the book has one, and otherwise the gain alone": dropping only the allowance would have demanded a number of chapters 8, 9, 10, 15, 18 and 20, which have none. docs/00 product question 7 changed the same way, since it held the same allowance.
* The key points of chapters 11, 13 and 14 were merged, not cut, to reach five: each merged bullet keeps every rule it held.
* Chapter 2's gain (37,228 lines against 22,650, with the four screens and the 93 pages they were counted over), chapter 16's (six rules and two checks against the fifteen days of four screens) and chapters 14, 17 and 21's Case A and Case B counts were left: the first two are one pair with what it was counted over; the others are Case passages this page does not reword.

**Proof.** `make verify` green (strict build, parity, em dash, prose rules, links, disclosure); `make book` built both editions' PDF and EPUB.

```commit
docs(one-gain-section): each gain said once; baseline in the prologue

- docs/04 One gain; no "the gain has no number" sentence (docs/00 too)
- prologue: one sentence on the missing baseline, for the whole book
- nine chapters lose a no-number sentence; gains of 1, 4, 11-13 cut to four
- key points act, never restate the gain; 11, 13 and 14 merged to five

work/done/one-gain-section.md
```
