# docs03-review-rows

**Objective.** Whoever reads docs/03 learns that the delivery review fixes what breaks the page, docs/04 or the text the delivery wrote, as the apply skill says, that it reads the files the delivery created as well as its diff, as docs/05 §5 says, and what a seen candidate is, beside latent and weak. Found by `m16-review` (work/done/m16-review.md, kit-1 seen: "docs/03:34, the delivery review row fixes "what breaks the page and docs/04"; the apply skill and chapter 13:70 add this delivery's own lines. The row is this repository's text"; doc-7 seen: "docs/03:36 glosses latent and weak but not seen"; decision 2 gives this page doc-7's docs/03 half).

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The delivery review row takes the apply skill's words, "what breaks the page, docs/04 or the text this delivery wrote", since the skill is what /apply runs and chapter 13:70 says the same ("a line this delivery wrote"). Source: .claude/skills/apply/SKILL.md:43-44 (the same in `.agents/skills/apply/`); book/en/13-apply.md:70.
2. Seen is glossed as docs/05 §8 glosses it, "true in the file today", the kit's wording since 2026.10.18, so docs/03 and docs/05 cannot drift. Source: docs/05:323; work/done/m16-review.md decision 2.
3. The English meaning column only: the term and its Portuguese name stay, and no new term enters. Source: docs/03.
4. No new queue line, no split: two cells of one document.
5. The driver's decision for this batch, not a finding of M16: the same cell also says the review reads the files the delivery created, which no diff shows until they are staged, as focus-kit 2026.10.18 put in docs/05 §5's Delivery review slot; one cell, so one delivery. M17's `ch13-created-files` still teaches it in chapter 13. Source: docs/05:207-212; the driver's message in this batch.

**Behaviour.**

* After the delivery, docs/03's `delivery review` row says it fixes what breaks the page, docs/04 or the text this delivery wrote, and anything else becomes a `[ ]` line.
* The same row says the review reads the files the delivery created as well as its diff, since no diff shows them until they are staged, as docs/05 §5 says.
* docs/03's `candidate` row says the checker marks a milestone review's candidate seen (true in the file today), latent (nothing triggers it today) or weak (the claim does not hold as stated).
* Edge: every other row of docs/03, the apply skill, docs/05 and both editions stay as they are.
* Fails: a delivery review row that still stops at docs/04, or that leaves out the created files; a seen glossed with other words than docs/05's.

**Contract.** docs/03, two cells of the meaning column:

* `delivery review` (line 34): "or a read-only agent; it fixes what breaks the page and docs/04, and anything else becomes a `[ ]` line." becomes "or a read-only agent; it reads the files the delivery created as well as its diff, since no diff shows them until they are staged; it fixes what breaks the page, docs/04 or the text this delivery wrote, and anything else becomes a `[ ]` line."
* `candidate` (line 36): "marked seen, latent (nothing triggers it today) or weak (the claim does not hold as stated) by the checker" becomes "marked seen (true in the file today), latent (nothing triggers it today) or weak (the claim does not hold as stated) by the checker".

No new term; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Chapter 13 on the created files: M17's `ch13-created-files`.
* The `milestone review` row's "seen, latent or weak": the `candidate` row glosses the three.
* docs/05 and the skills: kit wording, already right.

**Order with the other slugs of this batch.** Seventh; it touches only docs/03, which no other slug of the batch touches.

**Done when.**

* [x] docs/03:34 and :36 read as the Contract says, the created files included in line 34, and nothing else in docs/03 changes.
* [x] `make verify` green; no em dash.
* [x] Page in `work/done/`, line `[x]`, staged by its paths and its own hunk of docs/06 (docs/05 §6), other sessions' changes left unstaged; commit message in a `commit` block.

**Proof.** `make verify` green (exit 0): build, parity, em dash, prose, width, links, disclosure. docs/03's diff is one hunk, rows 34 and 36 only. No chapter, so no `make book`.

**Divergences.** None.

**Review.** One read-only agent on Opus read `git diff docs/03-Domain.md` and this line's hunk of docs/06 against this page, docs/04, docs/05 §§5 and 8 and the apply skill; it found nothing to fix. This delivery created no file.

**Case A and Case B.** None.

```commit
docs(docs03-review-rows): gloss seen and the created files in docs/03

- delivery review row: reads the created files, fixes the text the delivery wrote
- candidate row: seen glossed as docs/05 §8 does

work/done/docs03-review-rows.md
```
