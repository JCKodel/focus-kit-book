# pt-free-line-done

**Objective.** A reader of the Portuguese edition's chapters 7, 18 and 19 reads a free line as a queue line not done ("não está feita"), with chapter 14's word for the mark `[x]`, and never as a line "not ready", the reading `free-line-gloss` removed.

**Decided without the author.** Chosen under the batch's rule, the recommended option each time; review these first.

1. Which word says done? "feita", chapter 14's word for `[x]` (pt 14:25 "`[x]` | feita", 14:129 "`[x]` feita", 14:132 "outra linha precisa ser feita antes"), as the queue line names it; "concluída" was the alternative, a second word for one thing (docs/06 line `pt-free-line-done`; work/done/free-line-gloss.md, Review finding 2; AGENTS.md, one word per thing).
2. Which "pronta" changes? Only the two in each free-line gloss, "não está(ão) pronta(s)" and "outra linha pronta antes", in 7:59, 18:165 and 19:23; both read as "ready" next to "já definidas ou não" or a queue line, and the second is the same mark said in the same sentence. The other uses of "pronta" for a delivery done (19:94, 19:202, 13, 5, 21, "Pronto quando") are positive, are not a free-line gloss and are not this line's (docs/06 line `pt-free-line-done`).
3. Does the English edition change? No: it already says "not done" and "needs no other line done first" (en 7:59, 18:165, 19:23); this delivery makes the Portuguese mean what the English means, so the two editions agree after it with the English untouched (AGENTS.md, a change to one edition is a change to both; ADR-0004, English is the source).
4. docs/03 needs no change: `free line` / `linha livre` already holds the definition, and its `mark` row gives no Portuguese word per mark, which chapter 14 owns; no new term, no new queue line (docs/03).

**Behaviour.**

* A reader of pt chapter 7 §A estratégia de git reads that trunk serves one person with several sessions on free lines, "linhas da fila que não estão feitas, não estão esperando e não precisam de outra linha feita antes, já definidas ou não", with chapter 14 linked.
* A reader of pt chapter 18's Trunk bullet reads the same gloss with "feitas" and "feita".
* A reader of pt chapter 19 §Duas sessões em uma pasta reads "Uma linha livre é uma linha da fila que não está feita, não está esperando, e não precisa de outra linha feita antes".
* Failure: a reader who meets "linhas da fila que não estão prontas ... já definidas ou não" takes a free line for one not ready to build, the contradiction `free-line-gloss` removed in English; after this delivery no free-line gloss in the Portuguese edition says "pronta" or "prontas".
* Edge: chapter 14's definition (pt 14:58, 14:130) and its marks table stay as they are; the three glosses now use its word.
* Edge: 19:202, "onde `devolver-livro` está pronta", names a line in `[x]` in a positive sentence followed by "as duas linhas em `[x]`"; it reads as done and stays.
* Edge: the English edition reads the same before and after; parity holds, since only words inside one sentence change and no heading, line or link does.

**Contract.**

The finding was re-checked, not taken on trust: pt 7:59 and 18:165 say "linhas da fila que não estão prontas, não estão esperando e não precisam de outra linha pronta antes, já definidas ou não", and pt 19:23 says "Uma linha livre é uma linha da fila que não está pronta, não está esperando, e não precisa de outra linha pronta antes"; pt 14 says done with "feita". It holds.

* **Chapter 7, Portuguese edition** (`book/pt/07-the-documents.md`), file name, title and headings kept. In the sentence of §A estratégia de git (line 59 when this page was written), "linhas da fila que não estão prontas, não estão esperando e não precisam de outra linha pronta antes, já definidas ou não;" becomes "linhas da fila que não estão feitas, não estão esperando e não precisam de outra linha feita antes, já definidas ou não;". Nothing else changes.
* **Chapter 18, Portuguese edition** (`book/pt/18-git-essentials.md`), file name, title and headings kept. In the Trunk bullet (line 165), the same phrase changes the same way, word for word. Nothing else changes; the key point at line 185 stays.
* **Chapter 19, Portuguese edition** (`book/pt/19-worktrees.md`), file name, title and headings kept. Line 23, "Uma linha livre é uma linha da fila que não está pronta, não está esperando, e não precisa de outra linha pronta antes" becomes "Uma linha livre é uma linha da fila que não está feita, não está esperando, e não precisa de outra linha feita antes"; the parenthesis that follows stays. Nothing else changes.
* **English edition:** unchanged (Decided 3).
* **Terms:** `free line` / `linha livre`, and the mark `[x]` as chapter 14 says it, "feita"; docs/03 unchanged. No new term, no new queue line.
* **Sources:** none cited; the book's own definition, docs/03 `free line` and chapter 14.
* **Cases:** none. Code examples: none.

**Overlap with the lines in flight (docs/06).**

* `ch18-log-evidence` edits pt 18 at the log (18:45, 49) and the gain (18:177); this page touches only 18:165. Different lines of one file: on trunk the two should not run at the same time, or the second stages by hunk.
* `ch19-when-worktrees-pay`, `slice-paths` and `batch-propose` (after `ch16-review-agents`) also edit chapter 19; this page touches only pt 19:23. Same rule: not at the same time, or staged by hunk.
* `line-rule-once` (chapters 13 and 22) and `case-a-board-once` (chapters 16 and 20) touch none of these files.

**Out of scope.**

* "pronta" for a delivery done elsewhere (pt 19:94, 19:202, 13, 5, 21, 6) and "Pronto quando": positive sentences that read as done, not a free-line gloss; a candidate for the next review if one word for done is wanted book-wide.
* Chapter 14's definition and marks table: already say "feita".
* The English edition: already says "not done" (Decided 3).
* docs/03, docs/05 wording: unchanged.

**Done when.**

* [x] pt chapters 7, 18 and 19 changed as the Contract says, same headings; the English edition untouched; each chapter still opens with its value; no filler and nothing useful cut.
* [x] `grep -n -E "não estão prontas|não está pronta|outra linha pronta" book/pt/07-the-documents.md book/pt/18-git-essentials.md book/pt/19-worktrees.md` prints nothing.
* [x] `grep -n -E "não estão feitas|não está feita|outra linha feita antes" book/pt/07-the-documents.md book/pt/18-git-essentials.md book/pt/19-worktrees.md` prints the three glosses.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Built.** The three Portuguese free-line glosses now say "feita(s)" where they said "pronta(s)": pt 7:59, 18:165 and 19:23, one sentence each, words only; no heading, line or link changed; the English edition untouched. The lines had not moved since the page was written; found by text.

**Proof.** The Done when greps: the "pronta" one prints nothing; the "feita" one prints the three glosses (07:59, 18:165, 19:23). `make verify` green (build, parity, em dash, prose, links, disclosure). `make book` builds `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences.** None.

**Omissions.** None.

**Decisions taken in /apply.** None beyond the page's; no question arose.

**Review.** Delivery review by a read-only Opus agent on this delivery's diffs against the page and docs/04: the three edits match the Contract word for word, agreement is correct ("não estão feitas", "outra linha feita antes", "não está feita"), the editions now mean the same with the English untouched, the word is chapter 14's for `[x]`, no em dash, only this delivery staged. One finding: the queue line was still `[*]` while the page was in `work/done/`; that was the last edit still due, made when this section was written. No new queue line.

```commit
docs(pt-free-line-done): say a free line is not done with "feita"

- pt chapters 7, 18 and 19 gloss a free line with "feita", not "pronta"
- the word matches chapter 14's for the mark [x]
- English edition unchanged; both editions now mean the same

work/done/pt-free-line-done.md
```
