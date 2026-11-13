# m34-fixes

Defined before the author read it: the author's word for this run, relayed by the session that runs the queue on the author's behalf on 2026-11-13, is "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão" (close every open line of docs/06 without supervision), and for the reviews "Todas, médios entram" (every medium finding enters the one fixes line). So each question the documents leave open is answered by the agent's recommendation, marked "decided by the agent, the author corrects it in the review" (docs/05 §4, a command that says to decide alone).

**Objective.** After chapters 7, 11 and 18 the reader meets no contradiction with what the book teaches of focus-kit 2026.11.12 in the two places m34-review found: a free line is one whose `after` lets its next command start, and a grave finding stays in the milestone it was found in, as the review's own findings do.

**Behaviour.** What the reader can do or explain afterwards, one item per medium finding of `work/done/m34-review.md`:

* M1. From chapter 7 or chapter 18 alone, say that a free line is a queue line not done, not waiting, whose `after` lets its next command start; with chapter 14 :89's example, `return-book · after lend-book` while `lend-book` is `[*]` is free for `/propose` and not for `/apply`.
* M1, failure: asked "on trunk, may a session define `return-book` while `lend-book` is being built?", the reader of chapter 7 or 18 answers yes, never "no, it needs another line done first".
* M2. From chapter 11 alone, say that a line no clause of the current milestone's paragraph needs goes under the next milestone, except two kinds that stay in the milestone they were found in: a grave finding a delivery makes outside what it built, and a finding of the milestone's own review.
* M2, failure: asked "a delivery of milestone 1 finds a grave flaw outside what it built, and no clause of milestone 1 needs the fix; where does the line go?", the reader of chapter 11 answers "in milestone 1", never "under the next milestone".
* In the Portuguese edition, the same, with docs/03's Portuguese terms (linha livre, achado, grave, marco, revisão de marco).

**Contract.** Six chapter files, line numbers en / pt at HEAD `28a607a`, the same as at `2ee5bf5` (no commit since has touched them); pt follows en sentence for sentence. The text is the agent's within these changes.

* **M1, ch07** (`book/{en,pt}/07-the-documents.md`) :81 / :82, the parenthesis "(queue lines not done, not waiting and needing no other line done first, defined yet or not)" / "(linhas da fila que não estão feitas, não estão esperando e não precisam de outra linha feita antes, já definidas ou não)": becomes queue lines not done, not waiting, whose `· after` lets their next command start, defined yet or not. It leans on :63 / :64, "`· after` names a line this one needs first, and it is read for each command", and adds no pointer (docs/04, chapters 0 to 7).
* **M1, ch18** (`book/{en,pt}/18-git-essentials.md`) :186, the same parenthesis inside "**Trunk** fits one person ... on free lines (...; [chapter 14](14-queue-states.md))": the same change, the one pointer to chapter 14 kept, none added.
* **M2, ch11** (`book/{en,pt}/11-queue-and-milestones.md`):
  * :74 / :77, "Lines are added while a milestone runs: a grave flaw a delivery finds outside what it built, the review's findings that become lines (below), a problem you find trying the product.": reads true and stays.
  * :78 / :81, "... a line that a clause of the current milestone's paragraph needs goes in that milestone, and any other goes under the next milestone, which the agent creates when there is none, with a paragraph the line answers and its review last.": "any other" says it leaves out the findings of the next sentence, so it no longer reads as the whole rule.
  * :80 / :83, "A finding of the milestone's own review stays in its milestone too, under the review, even when the next milestone is already in the queue (below).": says two kinds stay in the milestone they were found in, even when no clause needs them and the next milestone is already in the queue: a grave finding, the first kind of line :74 names, and a finding of the milestone's own review, under the review (below). It says nothing of where a grave line sits among the planned lines.
  * :201 / :206, key point, "... lines are added while it runs, and whoever adds one puts it in the milestone whose paragraph has a clause that needs it, or under the next, ...": adds that a grave finding stays in its milestone; the rest as it is.
  * :4 / :4 (what the reader can do), :106 / :109 and :112 / :115 (a new idea, and the line arriving after the paragraph): read true, since an idea is not a finding, and stay.
* No pointer added in chapter 11; it already points to chapter 14 at :33, :84 and :176.

Terms of docs/03: free line (linha livre), dependency, finding (achado), grave, milestone review (revisão de marco), fixes line (linha de correções). No new term; docs/03 unchanged, its rows :97 (trunk), :120 (dependency) and :121 (free line) read right. Sources: docs/05 §4 :106 to :110 and chapter 14 :84 (M1); docs/05 §4 :111 to :115, "a finding of the milestone's own review stays in it (§8), and so does a grave finding, below" (M2). No number added. No source note added. Cases: none.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable: no screen, and no new kind of content (prose).

**Out of scope.**

* Where a grave line sits among the planned lines, and the `· from <slug>` suffix: `ch14-queue-findings` in M38, as `m33-fixes` ruled.
* How the review grades and copies notes: `ch15-review-grades` in M38.
* The small findings 3 to 21 of m34-review, chapter 11 :97's "under the review line" (R1-7) among them: not picked by the author's word.
* Chapters 12, 13 and 14: `ch12-14-mark-refused` and the M36 to M38 lines hold them.

**Done when.**

* [x] M1 and M2 read as the Contract says in both editions; a sweep of both editions for "needing no other line done first" and "não precisam de outra linha feita antes" finds none; no passage of chapter 11 sends a grave finding to the next milestone.
* [x] Both editions written; each chapter opens with its value; no filler and nothing useful cut; no number added; no em dash; no run narration; no pointer added.
* [x] `make verify` green after the last edit; the disclosure scan green.
* [x] `make book` builds both editions, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent, the author corrects it in the review: "defined yet or not" stays in both parentheses, since it is true and tells the reader that a line not yet defined can be free.
* Decided by the agent, the author corrects it in the review: chapter 11's key point :201 / :206 changes with :78 and :80, since it restates the same rule and would keep the contradiction; :4, :106 and :112 stay, as they speak of ideas, not findings.
* Decided by the agent, the author corrects it in the review: chapter 11 says only that a grave finding stays in its milestone, not where it sits, so this page does not take `ch14-queue-findings`' part.
* From the documents: a free line and `after` per command (docs/05 §4, docs/03 :121, chapter 14 :84); a grave finding staying in its milestone (docs/05 §4); the two items and that they are one page (`work/done/m34-review.md`, the author's word; docs/05 §8); no forward pointer in chapter 7 (docs/04).

## Outcome

Built before the author read it, on the author's word for this run ("Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão"); the author reads the page and the diff at the end. The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

* **M1.** Chapter 7 :81 / :82 and chapter 18 :186 now read "(queue lines not done, not waiting, whose `· after` lets their next command start, defined yet or not" / "(linhas da fila que não estão feitas, não estão esperando e cujo `· after` deixa o próximo comando delas começar, já definidas ou não"; chapter 18 keeps its one pointer to chapter 14; no pointer added. The sweep of `book/` for "needing no other line done first" and "não precisam de outra linha feita antes" finds none.
* **M2.** Chapter 11 :78 / :81 says "and any other, but for the two kinds of the next sentence, goes under the next milestone" / "e qualquer outra, fora os dois tipos da frase seguinte, vai sob o marco seguinte"; the next sentence, :79 / :82, is "Two kinds of line stay in the milestone they were found in, even when no clause needs them and the next milestone is already in the queue: a grave finding, a flaw a delivery finds outside what it built, and a finding of the milestone's own review, under the review (below)." / "Dois tipos de linha ficam no marco em que foram encontrados, ..."; the `fix-overdue-return` example follows it at :80 / :83. The key point :201 / :206 ends "; a grave finding stays in the milestone it was found in." / "; um achado grave fica no marco em que foi encontrado." :4, :74, :106 and :112 unchanged.
* **Divergence.** The Contract placed the two kinds at :80, after the example; the review found that "of the next sentence" then pointed at the example, so the sentence moved up to follow the rule it qualifies, and "Two kinds" became "Two kinds of line" so the noun has something to attach to. Decided by the agent, the author corrects it in the review.
* **Proof.** `make verify` green after the last chapter edit, 12 seconds (17 on the first run), the disclosure scan included. `make book` built both editions: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* **Delivery review.** One read-only Opus agent read the six chapter diffs and this line's hunk against this page and docs/04. Must fix: the "next sentence" pointer at :78 / :81 sent the reader to the example (fixed by the move above). Should fix: "Two kinds" with no noun (fixed). Everything else fine: both Behaviour items and both failure questions hold in both editions, docs/03's Portuguese terms, no em dash, no pointer, number or note added, nothing out of scope touched.
* No line depends on this one; nothing waits.

```commit
docs(m34-fixes): fix M34's two medium findings in chapters 7, 11, 18

- Chapters 7 and 18: a free line is one whose after lets its next command start
- Chapter 11: a grave finding and a review finding stay in their milestone
- Chapter 11's key point says a grave finding stays in its milestone
- Both editions; verify green, both PDFs built

work/done/m34-fixes.md
```
