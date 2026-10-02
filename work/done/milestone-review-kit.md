# milestone-review-kit

**Objective.** A reader of chapters 13, 16 and 17, in either edition, plans and runs a milestone review exactly as focus-kit defines it today (its docs/05 §8 since kit commit d333348): the review is the milestone's last planned line, it names for each clause of the paragraph the delivery that answers it and how a person tests it, it reviews no code and fixes nothing, the person tests each clause by hand, each finding becomes a `[ ]` line in the same milestone under the review line, and those lines get no second review.

**Decided by the author.**
1. Ninjobs: that review read code. The story stays as history, with one sentence saying that review read the code and that the kit's milestone review no longer does (code is read at each delivery's commit, chapter 15, and in the pull request, chapter 21). "Three of the findings were about security" stays as a fact of that review, with nothing suggesting today's review catches them. The gain is rewritten as what a hand test of the whole product sees.
2. "Review everything the milestone built" and "Decide each finding" are cut whole, not reworded: the kit has no code review in the milestone review and no confirm or reject step, since a clause that fails in the person's hands is the finding. One sentence says where code is read instead: at each delivery's commit (chapter 15) and pull request (chapter 21).
3. The book's own process (its docs/05 §4, §7 and §8, and M7's `m7-review` line) is the next queue line, `milestone-review-process`, right after this one; not this page.

**Behaviour.** Line numbers en / pt, as found before /apply; each passage changes in both editions, English first.
* Chapter 16 (`16-closing-a-milestone.md`), restructured into: The problem · The review is a delivery · Test each clause by hand · A line, and not a fix · No second review · When the findings became one delivery · What the team gains · Key points.
  * 3-4 / 3-4, "review everything it built with what your host offers, and decide each finding ... a new milestone, `<M>.1`": you plan the review as the milestone's last line, test each clause of its paragraph by hand, and turn each finding into a `[ ]` line in the same milestone, under the review.
  * 11 / 11, "A query that was fast ... a helper copied into four features": examples a hand test of the whole sees (a claim no delivery took on, a step that works alone and fails once the next delivery follows it); no code-only examples.
  * 15-19 / 15-19: "planned with its review as its last line"; its page takes the paragraph clause by clause and writes, for each, which delivery answers it and how a person tests it; it reviews no code and fixes nothing. Gone: "range of commits", "the review command of the host with its level", "reviews the code".
  * 21-33 / 21-34, "Check the paragraph", becomes "Test each clause by hand": the person runs the test the page wrote for each clause; a clause no delivery answers, or one that fails in the person's hands, is a finding. The lending library paragraph and its walk-through stay.
  * 35-50 / 36-51, "Review everything the milestone built", and footnotes 106-108 / 107-109 (`claude-code-review`, `codex-review`, `copilot-review`): cut, with decision 2's sentence.
  * 52-61 / 53-62, "Decide each finding": cut (decision 2).
  * 65-68 / 66-69: each finding becomes a `[ ]` line in the same milestone, under the review line, waiting for `/propose`; the milestone closes when those lines are `[x]`. Gone: "new milestone", `.1`, "milestone 1.1", "No confirmed finding, no new milestone", and the copied-code clause of 66 / 67; "says what will be true, never how to fix it" stays.
  * 74-77 / 75-78 become "No second review": the finding lines get no review of their own; each passes through its own page, its proof and the person's commit, which is the review. The reason stays, in the author's voice: a review of the fixes finds findings of its own, and a review of those finds more. Gone: `.1`, `.2`, "The kit's file lets ... I stopped allowing that".
  * 81-83 / 82-84: the story stays; one sentence says that review read the code and the kit's milestone review no longer does, code being read at each delivery's commit (chapter 15) and in the pull request (chapter 21). "Three of the findings were about security" stays as a fact of that review.
  * 94-95 / 95-96, What the team gains: what a hand test of the whole product sees (a clause no delivery took on, a step that fails once the deliveries run together); Ninjobs' eight findings and their security share are not offered as what today's review catches. 96 / 97 ("because each finding becomes a line") stays.
  * 100-104 / 101-105, Key points: rewritten to the sections above; no `<M>.1`, no "reviews the milestone's range", no "decide each finding".
* Chapter 13 (`13-queue-and-milestones.md`)
  * 75 / 75, "### The review, and `.1`": "### The review, and its findings".
  * 77-79 / 77-79: the review is planned as the milestone's last line, a delivery like the others, which takes the paragraph clause by clause ([chapter 16]); it reviews no code and fixes nothing; each finding becomes a `[ ]` line in the same milestone under the review line, and those lines get no second review.
  * 101 / 101: "... and last the review, whose findings become lines under it in the same milestone".
* Chapter 17 (`17-the-governor.md`)
  * 41 / 41 "seven things" / "sete coisas": eight.
  * 44-50 / 44-50: a new bullet after "No gate before implementation", **No review of a review:** each line a milestone review adds passes through its own page, its proof and the person's commit.
  * 75 / 75: "eight", and the list of what does the job includes the person's commit.

**Contract.** docs/03, the two rows, exactly:
* `| milestone review | revisão de marco | <milestone>-review, docs/05 §8 | The last line every milestone is planned with: its page takes the milestone's paragraph clause by clause and writes which delivery answers each and how a person tests it; it reviews no code and fixes nothing, and the person tests each clause by hand. |` (identifier column keeps its backticks)
* `| finding | achado | none | A clause of a milestone's paragraph that no delivery answers, or that fails in the person's hands; it becomes a [ ] line in the same milestone, under the review line, never a fix in the middle of the next milestone, and gets no second review. |` (`[ ]` in backticks)

Terms stay: revisão de marco, achado, marco. No new term.

**Must not change.** Chapter 4's Caution box (en 131 / pt 132): the spiral it tells is the error d333348 names. The queue examples in chapter 13 (55) and chapter 12 (70): mid-milestone, no findings yet, `m1-review` already last. Chapter 12 (22, 104), "then its review". Chapter 21 (28-32, `[^copilot-review]` at 95): pull request review, not the milestone's. Chapter 24 (66, 78, 114): already "the team, on the running product, against the paragraph". Chapter 16's lending library paragraph and the 879-line story.

**Out of scope.** The book's own docs/05 and the `m7-review` line: `milestone-review-process` (decision 3). The kit itself. Any chapter not listed.

**Done when.**
* [x] Every passage above changed in both editions; Portuguese means what English means.
* [x] `grep -rn -i -E 'code-review|codex review|`\.1`|M1\.1|<M>\.1|\.2`|confirmed finding|achado confirmado|second review|segunda revisão|decide each finding|decida cada achado' book/` prints nothing outside the passages listed as must not change (see What happened: the page's own "No second review" passages).
* [x] Chapter 17 says eight in both editions, the list has eight bullets.
* [x] docs/03 rows as Contract; no em dash; `make verify` green.
* [x] `make book` builds; the author gets the paths of both PDFs.

## What happened

* **The grep of Done when contradicts Behaviour on one term.** Behaviour asks for the chapter 16 section "No second review" and for chapter 13's "those lines get no second review", and `SETUP.md` §8 says "They get no second review"; the grep lists `second review|segunda revisão`. Behaviour was followed. The grep prints, besides chapter 21's `[^copilot-review]` note at line 95 (must not change), only those passages: en and pt 13:79, and the headings en 16:59 "No second review" and pt 16:60 "Nenhuma segunda revisão". Chapter 16's last key point says "no review of their own" (pt "revisão própria") so no other passage matches. The grep term is stale for the next page that copies it.
* **Chapter 17's eighth item checked against the kit.** `SETUP.md` §7 of focus-kit lists "no review of a review" among eight; the new bullet takes that name.
* **Chapter 16, beyond the letter of Behaviour.** "Test each clause by hand" gains two sentences the reader's doubt asks for where it is born (docs/04): why a person and by hand (the paragraph is a promise to the people who use the product), and why there is nothing to confirm or reject (the failure happened in the person's hands). "A line, and not a fix" shows the lending library milestone's lines with one finding line under `m1-review`, a queue written for the chapter and said so (pt with Portuguese slugs, `m1-review` kept as chapter 13 keeps it; widest row 67 columns), and one sentence on why the line stays in the same milestone: that milestone closes only when its paragraph holds. "with their proof" from the old `.1` sentence moved to "the milestone closes when those lines are `[x]`, each with its proof".
* **Where code is read, said twice and differently.** In "The review is a delivery": in the staged change before each delivery's commit (chapter 15) and in the pull request, when the team lands its deliveries through one (chapter 21); the qualifier is there because on trunk there is no pull request. In the Ninjobs story: that review read the code, the kit's milestone review no longer does, since each delivery's code is read before its commit; no second pointer, so chapter 21 is pointed at once per chapter.
* **The gain.** Ninjobs' eight findings cannot stand for what today's review catches (decision 1), and the book has no count of a milestone closed by a hand test, so the section says "This gain has no number in this book", as docs/04 allows.
* **Footnotes.** `[^claude-code-review]`, `[^codex-review]` and `[^copilot-review]` left chapter 16 in both editions with the cut sections; chapter 21 keeps its own `[^copilot-review]`.
* **Chapter 17's bullet carries no pointer to chapter 16**, as the page wrote it: the reader in order has just read it (docs/04, pointers back).
* **Known disagreement left for the next line.** docs/03's two rows now follow the kit, while this book's own docs/05 §8 still says `.1`, confirmed findings and a code review; decision 3 gives that to `milestone-review-process`.
* **Proof.** `make verify` green with the disclosure list present and the hooks on (link check online). `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` (EPUBs beside them), with weasyprint's usual `user-select` warnings.
