# docs04-gain-number

**Objective.** A reader of docs/04 finds one rule for the numbers of a chapter's gain that agrees with the rest of docs/04 and with the chapters, every "docs/03 §..." pointer in docs/04 naming a section that exists, and no rule of docs/04 naming the retired guided project as evidence. Findings L5 and the docs/04 part of D7 of `m14-review` (C8), re-checked, and docs/04:15, found while the line `docs01-retired-projects` was defined.

**Behaviour.**

* The rule is docs/04:32. Held: it says `## What the team gains` "gives the one number that sums the chapter", while docs/04:45 (**A gain per chapter**) and docs/00 product question 7 allow "a number or a sourced claim", or a sentence saying there is none, and three gains keep a pair: chapter 3 (37,228 lines of spec for four screens against 22,650 lines in 93 pages), chapter 9 (four screens in fifteen days against the opening in thirteen) and chapter 26 (the answers a blind judge would send in 9 of 9 pairs, for about 3 to 9 times the time and tokens).
* The rule changes, not the chapters. `plain-numbers` decided it on chapter 3 (decision 5: the pair "is the gain", docs/00 product question 7) and kept chapter 26's 9 of 9 and 3 to 9 times as "the gain's number" (its Behaviour, key point 5); chapter 9's gain was cut to its pair in the same delivery (its Divergences). The pair is one claim whose two figures cannot be cut apart without losing the claim, which is what "one number" protects against: a run of numbers. The chapters are right; the sentence is the shorter one.
* docs/04:32, second sentence, reads: `## What the team gains` gives the one number that sums the chapter, or, when the gain is a comparison, the one pair that is the gain (a figure before and after, a result and its cost); a chapter with no number follows **A gain per chapter**; each key point carries at most that number or pair (first: `plain-numbers`, from `m13-review`; the pair: `docs04-gain-number`, from `m14-review`).
* docs/04:45 is not edited: it already allows a gain with no number, and the new sentence defers to it.
* docs/04:26: "the vocabulary of docs/03 §running example gives the words" reads "the running example row of docs/03 gives the words". docs/03 has no heading of that name: it is a row of the glossary. Held.
* docs/04:15, **Teach, do not report.**: "A run of the guided project or a case is evidence" reads "A run or a case is evidence". The guided project is retired (ADR-0017, docs/05 §5); the book's runs in `work/done/*-run/` stay evidence. Held.
* Every other "§..." pointer in docs/04 (lines 6, 20, 40, 48, 117, 135, 137, 165, 169) names a heading, a bold rule or a section of another file that exists; checked, unchanged. Line 137's `SETUP.md` §3 is the kit's file, outside this repository.
* Fails: a rule that still says "the one number" beside a gain that keeps a pair; a rule that allows any list of numbers (the pair is two figures of one claim, not a table); a chapter edited by this delivery.

**Contract.** None. Three sentences of `docs/04-Conventions.md` (lines 15, 26 and 32 today); no chapter, no check and no other document changes. `check_prose.py` has no rule on gains (`plain-numbers` decision 6), so nothing mechanical moves.

**Out of scope.**

* The chapters 3, 9 and 26: their gains are right under the new sentence. A chapter whose gain still lists more than one claim's figures is `one-gain-section`'s pass over all chapters, not this page.
* docs/04:45 and docs/03's `team gain` row ("with a number or a sourced claim, or one sentence saying it has none"): they agree with the new sentence.
* The rest of **Numbers that prove** (the detail of a measurement stays at the source): unchanged.

**Done when.**

* [ ] docs/04:32 reads as Behaviour says, docs/04:26 names the glossary row and docs/04:15 names no guided project; no other line of docs/04 changes.
* [ ] `grep -n "docs/03 §running example" docs/04-Conventions.md` finds nothing.
* [ ] No file of `book/` is in the delivery's staged paths.
* [ ] `make verify` green.
* [ ] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**In flight.** Four pages in `work/` touch docs/04, and two touch the same lines.

* `renumber-chapters` edits "chapter 24" in docs/04:26 and "Chapter 4" in :27, the same line as the pointer fixed here: the hunks join. Whichever runs second reads docs/04:26 again and edits only its own words; /apply stops and reports if the line no longer reads as this page says.
* `one-gain-section` adds a bullet **One gain** after **Numbers that prove** (so beside docs/04:32) and removes the "or one sentence saying the gain has no number" of docs/04:45 and of **A gain per chapter**; its decision 2 says a key point carries "the gain's one number". It should run after this page and read "that number or pair": it is queued after M15's cuts, so the order holds, but its page should be corrected when it is applied.
* `focus-and-slices` edits the orchestrator example in docs/04 §Say it where the doubt is born (line 39), `simplicity-and-results` and `prologue-and-why` the pointers that name their chapters: other lines, no overlap with 26 or 32.

**Decisions in the review.** Choices made alone.

* The rule changes and the chapters stay, from `plain-numbers` decision 5 and its Behaviour. The reverse, making chapters 3, 9 and 26 keep one number, would cut the pair that is their claim and was kept on purpose.
* The sentence says "pair" and gives two kinds (before and after, result and its cost), not a general "numbers", so a gain cannot grow back into the run that `plain-numbers` cut.
* The "first" attribution adds this delivery next to `plain-numbers` rather than replacing it, as docs/04 does for amended rules.
* No chapter number appears in the rule, so `renumber-chapters` has nothing to follow here.
* docs/04:15 joined this page after it was written, by the session that drove the proposals: the line is per file, and the stale mention is docs/04's.
