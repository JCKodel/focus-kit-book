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

* [x] Chapter 3 changed in both editions, same headings; no mention of the three levels, Kiro or Tessl in either edition; the caveat said once.
* [x] Every number still sourced; parity of notes green.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* The taxonomy is cut because no chapter after 3 uses it and docs/00's non-goals say the book is not a reference for tools (grep over `book/en` for "spec-anchored", "Kiro", "Tessl": chapter 3 only).
* The caveat stays in the body and leaves the key points: docs/04 §Numbers that prove, each key point carries at most the chapter's number.

**Decisions in the review.** None.

**Decisions in /apply.** Chosen alone, under the batch's rule; corrections go in the review.

* The opening's promise "say what Spec-Driven Development is and how far a tool takes the spec" (pt "até onde uma ferramenta leva a especificação") becomes "say what a spec and Spec-Driven Development are" (pt "dizer o que são uma especificação e o Desenvolvimento Guiado por Especificação"): "how far a tool takes the spec" is the taxonomy the page cuts, and the opening must say what the reader can do after the chapter (ADR-0015). The Contract did not list the opening; the Done when's "no mention of the three levels" decided it.
* "Two tools" loses its last sentence, "Both are spec-first by default: the spec is written for the task at hand." (pt "Os dois são spec-first por padrão ..."), although the Contract says the section is unchanged: the sentence uses a cut term, and the Done when and the failure Behaviour forbid it. Rewording it without the term was rejected: without the taxonomy it says nothing the run's paragraph does not.
* The `[^bockeler-2025]` note keeps the article's real title, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl": a source's title is quoted as published (docs/04), so "no mention of Kiro or Tessl" is read as the chapter's text, not the citation.
* Sections are not reordered. After the cut the counts arrive after "Two tools" and "What they got right", at about 56% of the chapter's words (from about 59% before), not in the first third the Behaviour estimated; moving "Where the cost of many places begins" ahead would break the Contract's "headings kept, unchanged" and the hand-off from its last paragraph into the gain. A reorder, if wanted, is a fresh /propose.
* docs/03 keeps its rows for spec-first, spec-anchored and spec-as-source, as the Contract says (no check reads docs/03 against the book); they are now used by no chapter, a candidate `[ ]` line for the author.

**What happened.**

* `book/en/03-spec-driven.md` and `book/pt/03-spec-driven.md`: line 4's opening as above; "What a spec is" keeps the three Böckeler paragraphs and the note box, and loses the three levels, the quotations on them, Kiro, Tessl and the "fast evolving" sentence (nine source lines, the bullet list included); "Two tools" loses its spec-first sentence; "Key points" go from five to four, the taxonomy point removed and the fifth ending at "documents written once per project" (pt "uma vez por projeto").
* "What they got right", "Where the cost of many places begins" (the restated-rule count and its closing caveat) and "What the team gains" (the Ninjobs count and the chapter 9 cause sentence of `ch03-restated-rule`) unchanged.
* No document changes; no dependent queue line waits on this one.

**Proof.**

* `grep -n -i -e kiro -e tessl -e spec-first -e spec-anchored -e spec-as-source book/*/03-spec-driven.md` finds only the `[^bockeler-2025]` note's title, in both editions.
* Citations per edition, en and pt equal: `[^bockeler-2025]` 4, `[^spec-driven-run]` 8, `[^spec-kit]` 1, `[^openspec]` 1. The caveat "one feature on one day is not a benchmark" appears once, at the end of "Where the cost of many places begins".
* `make verify` green; `make book` built both editions, and the PDFs are `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

```commit
docs(ch3-spec-cut): chapter 3 drops the taxonomy and the unused tools

- ch3: no spec-first, spec-anchored or spec-as-source, no Kiro or Tessl
- ch3: the opening promises what a spec and SDD are
- ch3: four key points, the caveat said once in the body
- both editions

work/done/ch3-spec-cut.md
```
