# ch3-spec-cut

**Objective.** After chapter 3 a reader knows what a spec is, what Spec-Driven Development is, and what one feature cost in three tools and on Ninjobs, with the measured numbers reached in half the reading, and without the taxonomy and the tools the book never uses again.

**Behaviour.**

* A reader reaches the counts (8 files and 756 lines, 6 and 180, 1 page of 82) within the first third of the chapter, right after the definition of a spec and the note box on behaviour.
* A reader can define a spec and SDD in Böckeler's words, and finds the behaviour note box where it is today.
* Failure: a reader looking for spec-first, spec-anchored and spec-as-source, Kiro or Tessl does not find them; no later chapter relies on the three levels (checked: no chapter names them).
* A reader finds the caveat that the counts say what each tool writes and not which builds better software once, at the end of "Where the cost of many places begins", and not again in the key points.
* A reader finds the Ninjobs count (37,228 lines for four screens, 22,650 for 93 pages after) in the gain section as today, with chapter 9 pointed for the causes.
* Edge: Böckeler's quotations about Spec Kit's files ("repetitive", "very verbose and tedious to review") stay, since they are evidence about a tool the chapter measured.
* Edge: the key points go from five to four, the taxonomy point removed and the caveat folded into the last point's half sentence.

**Contract.**

* **Chapter 3, both editions, file name, title and headings kept,** except as listed:
  1. "What a spec is": keep the three Böckeler paragraphs that define spec and SDD and the note box. Cut from "She found three levels" to "...since I used them" (seven source lines in en).
  2. "Two tools", "What they got right": unchanged.
  3. "Where the cost of many places begins": unchanged, keeps the closing caveat sentence.
  4. "What the team gains": unchanged.
  5. "Key points": the second point (spec-first, spec-anchored, spec-as-source) removed; the fifth point ends at "documents written once per project", the "the counts show..." clause removed since the section says it.
* **Notes:** `[^bockeler-2025]` keeps its remaining citations (definition, SDD, the two quotations on Spec Kit); `[^spec-kit]`, `[^openspec]`, `[^spec-driven-run]` unchanged. Both editions keep the same keys cited the same number of times (parity).
* **Terms:** none change; docs/03 unchanged.
* **Sources:** none added.
* **Cases:** Ninjobs, as today.

**Out of scope.**

* The run's numbers and their record: unchanged (ADR-0017).
* The gain section's wording and the sentence on where the counts come from: `one-gain-section` and `plain-numbers` already shaped them.

**Done when.**

* [ ] Chapter 3 changed in both editions, same headings; no mention of the three levels, Kiro or Tessl in either edition; the caveat said once.
* [ ] Every number still sourced; parity of notes green.
* [ ] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* The taxonomy is cut because no chapter after 3 uses it and docs/00's non-goals say the book is not a reference for tools (grep over `book/en` for "spec-anchored", "Kiro", "Tessl": chapter 3 only).
* The caveat stays in the body and leaves the key points: docs/04 §Numbers that prove, each key point carries at most the chapter's number.

**Decisions in the review.** None.
