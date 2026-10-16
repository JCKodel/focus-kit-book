# one-gain-section

**Objective.** Every chapter of both editions ends with one gain section whose key points do not repeat it, and the book says once, in the prologue, that it measures no baseline against a team without the method; docs/04 holds the rule.

**Decided from the documents.**
1. docs/04 §Chapter shape keeps `## What the team gains` and `## Key points` in every chapter; this delivery changes what they hold, not the shape (ADR-0015 and ADR-0017 fixed the shape; a shape change is an ADR, which no error asks for).
2. A key point is what the reader takes to their project, one line each, at most five; it does not restate the gain's sentence or carry its number again beyond the one number `plain-numbers` allows (docs/04, Numbers that prove). The rule goes in docs/04 §Writing the book as a bullet, **One gain**, after **Numbers that prove**, saying: the gain is said in `## What the team gains`; a key point says what to do, not what is gained; "no baseline" is the prologue's sentence, not a chapter's.
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

* [ ] docs/04 holds **One gain** and the shape line is changed.
* [ ] The grep of Behaviour lists no file in either edition; the prologue holds the one sentence.
* [ ] Every chapter's gain and key points read as Behaviour says, both editions; the per-chapter table is on this page.
* [ ] Every note definition keeps a reference; `make verify` green; `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Decisions in the review.**

* Key points are kept in every chapter and rewritten so that none restates the gain, as recommended; docs/04's shape and ADR-0015 stand.
* The prologue's baseline sentence goes in its gain section, as recommended.
