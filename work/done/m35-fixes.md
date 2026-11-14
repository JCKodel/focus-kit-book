# m35-fixes

Defined before the author read it: the author's word for this run, relayed by the session that runs the queue on the author's behalf on 2026-11-13, is "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão" (close every open line of docs/06 without supervision), and for the reviews "Todas, médios entram" (every medium finding enters the one fixes line). So each question the documents leave open is answered by the agent's recommendation, marked "decided by the agent, the author corrects it in the review" (docs/05 §4, a command that says to decide alone).

**Objective.** After chapters 11, 12 and 19 the reader meets no contradiction with what the book teaches of focus-kit 2026.11.12 in the three places m35-review found: a grave finding and a review's finding stay in their milestone with no clause widened for them, a free line is one whose `after` lets its next command start, and a `/propose` resumed on a line still `[~]` marks nothing again.

**Behaviour.** What the reader can do or explain afterwards, one item per medium finding of `work/done/m35-review.md`:

* M1. From chapter 11 alone, say that a planned line enters the current milestone only through a clause of its paragraph, and that a grave finding and a finding of the milestone's own review stay in the milestone they were found in without one.
* M1, failure: asked "a delivery of milestone 1 finds a grave flaw outside what it built, and no clause of milestone 1 needs the fix; must you widen milestone 1's paragraph first to keep the line there?", the reader of chapter 11 answers "no, a grave finding stays in milestone 1 as it is", never "yes, a line enters only through a clause".
* M2. From chapter 19 alone, say that a free line is a queue line not done, not waiting, whose `after` lets its next command start, as chapters 7 and 18 say.
* M2, failure: asked "is a line whose `after` names a line not yet done ever free?", the reader of chapter 19 never answers "no, a free line needs no other line done first".
* M3. From chapter 12 alone, say that `/propose` marks `[~]` on a `[ ]` line, and that a line still `[~]` because its session ended, resumed on the person's word, keeps its `[~]` and is marked again by nothing.
* M3, failure: asked "the session defining `return-book` closed with the line `[~]`; you tell a new session to resume it; is its first edit marking the line `[~]`?", the reader of chapter 12 answers "no, the line keeps its `[~]`", never "yes, and the mark script refuses it".
* M3, edge: a line that waited as `[?]` with `· resume: propose` and went back to `[ ]` with its draft kept (chapter 14) is a `[ ]` line, so its `/propose` marks `[~]` as for any other; chapter 12 keeps saying so, and the fix speaks only of a line still `[~]`.
* In the Portuguese edition, the same, with docs/03's Portuguese terms (achado, grave, marco, revisão de marco, linha livre, script de marca).

**Contract.** Six chapter files, line numbers en / pt at `2673874`, where m35-review read them, the same at HEAD `f526e4f` (`git diff 2673874 -- book/` is empty); pt follows en sentence for sentence. The text is the agent's within these changes.

* **M1, ch11** (`book/{en,pt}/11-queue-and-milestones.md`) :81 / :84, "What you decide is the paragraph: a line enters the current milestone only through a clause, so to bring one in you widen the paragraph by conversation first, and the line then answers the new clause." / "O que você decide é o parágrafo: uma linha só entra no marco atual por uma cláusula, então para trazer uma você amplia o parágrafo conversando antes, e a linha passa a atender a cláusula nova.": the rule names its two exceptions itself, a grave finding and a finding of the milestone's own review, by name and not by position, since the example (:80 / :83) stands between this sentence and :79 / :82's "Two kinds of line stay in the milestone they were found in, even when no clause needs them ...". :78 / :81, :79 / :82, the example and the key point :201 / :206 read true and stay.
* **M2, ch19** (`book/{en,pt}/19-worktrees.md`) :24, "A free line is a line of the queue that is not done, not waiting, and needs no other line done first ([chapter 14](14-queue-states.md) teaches the queue's marks)." / "Uma linha livre é uma linha da fila que não está feita, não está esperando, e não precisa de outra linha feita antes ([o capítulo 14](14-queue-states.md) ensina as marcas da fila).": takes chapter 7 :81 / :82's wording, a queue line not done, not waiting, whose `· after` lets its next command start; the pointer to chapter 14 stays as it is. :3, :23, :26, :216, :366 and :404 use "free line" without defining it and stay.
* **M3, ch12** (`book/{en,pt}/12-propose.md`) :31, "Its first edit there marks the line `[~]` in the queue, through the kit's mark script, `propose/scripts/mark.sh`, which changes that one mark and nothing else of the file and sets `[~]` only on a `[ ]` line, so a second `/propose` of the slug is refused there; ..." / "A primeira edição dele ali marca a linha como `[~]` na fila, ...": says the first edit marks `[~]` on a `[ ]` line, and adds that a line still `[~]` because its session ended, resumed on the person's word, keeps its `[~]` and is marked again by nothing. :30 / :30's "or reused when the definition resumes" / "ou reutilizado quando a definição é retomada" stays: it is the branch or worktree reused, true for both kinds of resumption. The rest of :31 stays.
* The source of M3 is docs/05 §4 :195 to :198, "A `[~]` or `[*]` line whose session ended without blocking it ... keeps its mark; its command resumes it on the person's word", and chapter 14's `## A session that ended, a delivery cancelled`, "neither resumed command marks its line again, and the mark script would refuse a second `[~]` or `[*]` on it" (en :206 / pt :208 at `2673874`; `ch14-15-after-all-dropped` may move those lines). Not the kit's propose `SKILL.md` :27 to :30, which has the same wording as chapter 12 (m35-review's R3-4).
* No pointer added: chapter 11 already points to chapter 14, chapter 12 points to chapter 14 at :28 and :33, chapter 19 keeps its one at :24 (docs/04, chapter pointers, once per chapter for each target).

Terms of docs/03: finding (achado), grave, milestone (marco), milestone review (revisão de marco), free line (linha livre), mark script (script de marca). No new term; docs/03 unchanged, its rows :31 (mark script) and :121 (free line) read right. Sources: docs/05 §4 :106 to :115 (M1, M2), :195 to :198 (M3). No number added. No source note added. Cases: none.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable: no screen, and no new kind of content (prose).

**Out of scope.**

* The kit's propose `SKILL.md` :27 to :30 (R3-4): a kit file, not edited here; the author did not pick it, so no note in `work/kit-proposals.md`.
* m35-review's small findings 4 to 9: not picked by the author's word.
* Chapters 14 and 15: `ch14-15-after-all-dropped` is being built in them.
* Chapter 12's key point :195 / :204 and :161 / :170: they read true (below).
* No further line: a fix page opens none (docs/05 §8).

**Done when.**

* [x] M1, M2 and M3 read as the Contract says in both editions.
* [x] A sweep of `book/` in both editions for "no other line done" and "outra linha feita antes" finds none; for "only through a clause" and "só entra no marco atual" finds only the sentence that names the two exceptions; chapter 12 has no sentence that marks `[~]` on a line already `[~]`.
* [x] Both editions written; each chapter opens with its value; no filler and nothing useful cut; no number added; no em dash; no run narration; no pointer added.
* [x] `make verify` green after the last edit, with its time; the disclosure scan green.
* [x] `make book` builds both editions, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent, the author corrects it in the review: chapter 11 :81 / :84 names the two exceptions ("but for a grave finding and a finding of the milestone's own review" / "fora um achado grave e um achado da revisão do próprio marco") rather than pointing at :79 / :82, since the example stands between them, the fault `m34-fixes`' delivery review caught in its own "next sentence".
* Decided by the agent, the author corrects it in the review: chapter 19 takes chapter 7's parenthesis word for word, so the book defines a free line one way.
* Decided by the agent, the author corrects it in the review: M3 speaks of a line still `[~]` whose session ended, not of a resumed definition in general, since a `[?]` line resumed through `resume: propose` goes back to `[ ]` and its `/propose` does mark `[~]` (docs/05 §4 :190 to :193).
* Decided by the agent, the author corrects it in the review: chapter 12's key point :195 / :204, "marks the line ... `[~]` there while it talks", and :161 / :170, "which resumes the line's `[~]` on the word of your command", stay: the first describes a definition started, the second already says a resumed line keeps its `[~]`.
* From the documents: the three items and that they are one page (`work/done/m35-review.md`, the author's word; docs/05 §8); a grave finding and a review finding staying in their milestone (docs/05 §4 :111 to :115); a free line and `after` per command (docs/05 §4 :106 to :110, docs/03 :121); a resumed `[~]` keeping its mark (docs/05 §4 :195 to :198); docs/03 unchanged.

## Outcome

Built before the author read it, on the author's word relayed for this run ("Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão"). The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

**What changed.**

* M1, chapter 11 en :81 / pt :84: "What you decide is the paragraph: except for a grave finding and a finding of the milestone's own review, a line enters the current milestone only through a clause, ..." / "O que você decide é o parágrafo: fora um achado grave e um achado da revisão do próprio marco, uma linha só entra no marco atual por uma cláusula, ...". The rest of the sentence, :78, :79, the example and the key point stay.
* M2, chapter 19 :24: "A free line is a queue line not done, not waiting, whose `· after` lets its next command start (...)" / "Uma linha livre é uma linha da fila que não está feita, não está esperando e cujo `· after` deixa o próximo comando dela começar (...)"; the pointer to chapter 14 stays.
* M3, chapter 12 :31: "Its first edit there marks the `[ ]` line `[~]` in the queue, ..." / "A primeira edição dele ali marca a linha `[ ]` como `[~]` na fila, ..."; and a new line :32, "A line still `[~]` because the session defining it ended is no second start: a new session resumes it on your word, the line keeps its `[~]`, and nothing marks it `[~]` again." / "Uma linha ainda `[~]` porque a sessão que a definia terminou não é um segundo começo: uma sessão nova a retoma pela sua palavra, a linha mantém o `[~]`, e nada a marca `[~]` de novo." The edge holds: :31 still marks `[~]` on any `[ ]` line, a line back from `[?]` included.

**Decisions.**

* Decided by the agent, the author corrects it in the review: chapter 19 takes the Contract's wording of chapter 7's parenthesis, without its tail "defined yet or not" / "já definidas ou não"; the Contract is the exact section, and chapter 19 speaks of builds. The page's Decision "word for word" reads as "its definition".
* Decided by the agent, the author corrects it in the review: the M3 sentence says "is no second start", so the kept clause "a second `/propose` of the slug is refused there" cannot be read as refusing a resumption.
* Decided by the agent, the author corrects it in the review: en :81 says "except for", not the page's "but for", which the delivery review found read first as the conjunction right after the colon; pt keeps "fora".

**Sweep.** "no other line done" and "outra linha feita antes" are gone from `book/`; "only through a clause" and "só entra no marco atual" stand only in the sentence that names the two exceptions (en 11:81, pt 11:84).

**Proof.** `make verify` green after the last edit, 11 seconds, the disclosure scan included. `make book` built both editions: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review.** One read-only Opus agent read the six chapters' diff, the page, docs/04 and docs/03's rows: nothing to fix as grave; one should-fix and two small ones, all fixed in this delivery: en 11:81 "but for" to "except for"; 12:32 "nothing marks it again" to "nothing marks it `[~]` again" in both editions, since the line later turns `[>]`; pt 12:32 "com a sua palavra" to "pela sua palavra", which reads as the person's word. Verify ran again, green. Its note on chapter 19's dropped tail is the first decision above.

**Divergences.** None beyond the decisions above. No pointer, number, source note or term added; docs/03 unchanged.

```commit
docs(m35-fixes): fix M35's three medium findings in chapters 11, 12, 19

- ch11: only through a clause, except a grave or a review finding
- ch19: a free line is one whose `after` lets its next command start
- ch12: a resumed `[~]` line keeps its mark, marked again by nothing

work/done/m35-fixes.md
```
