# ch14-m1-return-book

**Objective.** A reader who follows the lending library's first milestone from chapter 11 through 14 to 15 finds the same delivery, `return-book` (pt `devolver-livro`), in chapter 14's queue and board too, with what chapter 14 says about free lines and the board still true of it; both editions.

**Decided without the author** (batch rule of this run: the recommended answer, no question asked).

1. *Mark, words and place.* The line is chapter 11's, word for word: en `[ ] return-book ... records a return · after lend-book`, pt `[ ] devolver-livro ... registra a devolução · after emprestar-livro`, right after `lend-book` (pt `emprestar-livro`), as chapters 11 and 15 order it (`m17-review`, R2-5). It is `[ ]`: `lend-book` is `[*]` in chapter 14, so a line after it is not free, and chapter 14 says `/propose` does not start a line that is not free, so it cannot be `[~]` or `[>]`.
2. *Width.* The slug column of the block is 16 wide in English and 18 in Portuguese, so the new lines are 54 and 66 columns, under docs/04's 74. A longer description ("o bibliotecário registra uma devolução") would pass 74 in Portuguese; chapter 11's shorter one is taken.
3. *The sentences that lean on the queue follow it.* Chapter 14 classifies the milestone's lines by name: who is being built, what is free, what waits, and the board that shows "the milestone above". With `return-book` in the queue, five places stay true only if they name it beside `my-loans`, which it matches (`[ ]`, `· after lend-book`): the sentence after the block, the free lines, the moment `lend-book` becomes `[x]`, the board's To Do column and the sentence after the board. Each gets `return-book` beside `my-loans` and nothing else.
4. *Nothing else moves.* The examples that name `my-loans` alone (`/propose my-loans` while `lend-book` is `[*]`, the third waiting case, the `· after` paragraph) stay: each is about that one line. No line counts the queue's lines.
5. *Chapter 14's other lines stay.* Its queue holds `search-catalog`, `reservations` and `due-reminder`, which chapters 11 and 15 do not; each chapter's queue is written for it, and only the missing `return-book` is this finding.
6. *No docs/03 change.* The running example row already gives `devolver-livro`.
7. *Order with `pt-librarian-masculine`.* That page, earlier in this batch's order, changes the three librarian lines of the Portuguese block; this page's new line has no word for the librarian, and the Contract's Portuguese block is quoted after that page. If that delivery is not committed when this one applies, this one's hunk is staged by hunk against the index, which already holds those lines. No other session's line touches chapter 14.
8. *Trunk; nothing staged by this definition; the driver sets docs/06's marks.*

**Behaviour.**

* Reading chapter 14's first milestone, a reader finds `return-book` (pt `devolver-livro`) after `lend-book`, `[ ]`, with `· after lend-book`, as in chapter 11.
* Asked which lines are free in that milestone, the reader answers from the text: `lend-book`, `search-catalog` and `reservations`; `return-book` and `my-loans` are not, since `lend-book` is not `[x]`; `due-reminder` waits.
* On the three-column board, `return-book` sits in To Do with no tag, beside `my-loans`.
* Edge: the queue and the board keep to 74 columns in both editions.
* Failure: `return-book` missing from the queue or the board in either edition, a sentence that still lists the free or waiting lines without it, a line of chapter 14 changed beyond the Contract, or one edition changed and not the other.

**Contract.** Chapter 14, both editions (`book/en/14-queue-states.md`, `book/pt/14-queue-states.md`), found by text:

* **The queue**, a new line after the `lend-book` line:
  * en `[ ] return-book     records a return · after lend-book` (the slug padded to 16 columns, as the block's other slugs).
  * pt `[ ] devolver-livro    registra a devolução · after emprestar-livro` (padded to 18).
* **After the block:** en "that `my-loans` comes after `lend-book`," becomes "that `return-book` and `my-loans` come after `lend-book`,"; pt "que `meus-emprestimos` vem depois de `emprestar-livro`," becomes "que `devolver-livro` e `meus-emprestimos` vêm depois de `emprestar-livro`,".
* **Free lines:** en "`my-loans` is not, since `lend-book` is not `[x]` yet" becomes "`return-book` and `my-loans` are not, since `lend-book` is not `[x]` yet"; pt "`meus-emprestimos` não, já que `emprestar-livro` ainda não está `[x]`" becomes "`devolver-livro` e `meus-emprestimos` não, já que `emprestar-livro` ainda não está `[x]`".
* **The moment it is free:** en "When `lend-book` becomes `[x]`, `my-loans` is free from that moment" becomes "When `lend-book` becomes `[x]`, `return-book` and `my-loans` are free from that moment"; pt "Quando `emprestar-livro` vira `[x]`, `meus-emprestimos` fica livre nesse momento" becomes "Quando `emprestar-livro` vira `[x]`, `devolver-livro` e `meus-emprestimos` ficam livres nesse momento".
* **The board**, To Do gets `return-book` (pt `devolver-livro`) on the second row, the other columns unchanged:
  ```
  TO DO                 DOING                  DONE
  due-reminder BLOCKED  reservations           catalog
  return-book           search-catalog         members
  my-loans              lend-book
  m1-review
  ```
  ```
  A FAZER              FAZENDO                    FEITO
  aviso-prazo TRAVADA  reservas                   catalogo
  devolver-livro       buscar-catalogo            membros
  meus-emprestimos     emprestar-livro
  m1-review
  ```
* **After the board:** en "`my-loans` sits in To Do with no tag: it waits its turn, not on anyone," becomes "`return-book` and `my-loans` sit in To Do with no tag: they wait their turn, not on anyone,"; pt "`meus-emprestimos` fica em A fazer sem etiqueta: espera a sua vez, não por alguém," becomes "`devolver-livro` e `meus-emprestimos` ficam em A fazer sem etiqueta: esperam a sua vez, não por alguém,".
* The rest of each sentence and every other line of chapter 14 are unchanged.
* **Terms of docs/03.** `mark`, `queue`, `running example` (`devolver-livro`); no new term.
* **Sources.** None added or removed. **Cases.** None.
* **docs/06.** None from this page; the driver sets its line's marks.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* The other lines of chapter 14's milestone that chapters 11 and 15 do not have (decision 5).
* Chapter 17's "4 of 7": another chapter's own example.
* The librarian's gender in the Portuguese block: `pt-librarian-masculine`.

**Done when.**

* [x] Both editions written in the places the Contract names, the English first; parity green.
* [x] `grep -c "return-book" book/en/14-queue-states.md` gives 6, and `grep -c "devolver-livro" book/pt/14-queue-states.md` gives 6 (queue, after the block, free lines, the moment, board, after the board).
* [x] The queue and the board within 74 columns in both editions (`make verify`'s width rule).
* [x] Chapter 14 still opens with its value; no filler, nothing useful cut; still four waiting cases and five key points.
* [x] No em dash; `make verify` green (build, parity, em dash, prose, width, links, disclosure).
* [x] The Delivery review ran on this delivery's paths and the files it created (docs/05 §5), and the page records it.
* [x] The author's approval of an anonymized passage: inapplicable, no Case A or Case B passage.
* [x] `make book` builds; the delivery ends with the paths of both PDFs for the author's review.
* [x] Page moved to `work/done/`, the line `[x]`, staged by explicit paths (by hunk for the Portuguese chapter if `pt-librarian-masculine` is staged and not committed) and this line's hunk of docs/06; the commit message suggested, `docs(ch14-m1-return-book): ...`.

**Built.** Chapter 14, both editions, in the six places the Contract names, English first: the queue's new line after `lend-book` (pt `emprestar-livro`), the sentence after the block, the free lines, the moment `lend-book` becomes `[x]`, the board's To Do column and the sentence after the board. `grep -c` gives 6 in each edition.

**Decisions at apply time.** Chapter 11's line was checked before writing: `records a return · after lend-book`, pt `registra a devolução · after emprestar-livro`, word for word as the Contract gives it. `pt-librarian-masculine` was committed before this delivery began, so `book/pt/14-queue-states.md` is staged whole. docs/06's hunk also holds other sessions' marks set by the driver, so only this line's mark is staged, from an index copy built on HEAD with this one line changed; the working tree keeps the other marks (the shared-hunk question is `conflict-same-lines`, already in the queue; no new line).

**Divergences and omissions.** None.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure); `make book` builds `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review.** One read-only agent on Opus read this delivery's diff of both chapter files and its line of docs/06 against this page and docs/04. It found nothing to fix: every Contract item applied with the block columns kept (slug fields 16 and 18, To Do columns 22 and 21), nothing else in chapter 14 changed, the Portuguese verbs agree with their two subjects, the new line matches chapter 11, no em dash, every block line within 74 columns, the Behaviour statements true of the text.

```commit
docs(ch14-m1-return-book): add return-book to chapter 14's milestone

- Queue gets `return-book` (pt `devolver-livro`) after `lend-book`, as chapter 11
- Free lines, the moment it frees and the board name it beside `my-loans`
- Both editions

work/done/ch14-m1-return-book.md
```
