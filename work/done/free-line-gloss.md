# free-line-gloss

**Objective.** A reader of chapters 7 and 18 understands a free line as docs/03 defines it, a queue line not done, not waiting, whose `after` lines are done, `[ ]` lines included, and not as a delivery ready to build.

**Decided without the author.** Chosen under the batch's rule, the recommended option each time; review these first.

1. Do chapters 7 and 18 both gloss a free line, or does chapter 18, which comes after chapter 14, only point to it? Both gloss it, as the queue line asks, with the smallest correct gloss in the place the wrong one stands, and both point to chapter 14, which stays the one owner of the definition; pointing only, in chapter 18, was the alternative, closer to "a rule said once" (docs/06 line `free-line-gloss`; docs/03 `free line`; AGENTS.md).
2. How do the chapters say "`[ ]` lines included" to a reader of chapter 7, who has not met the marks? In words, "defined yet or not", with no mark: chapter 11 leaves the marks other than `[ ]` and `[x]` to chapter 14 (en 11:33, pt 11:35; docs/03 `free line`).
3. Is the gloss a sentence of its own or kept where the wrong one stands? Kept in place, as a parenthesis that ends with the pointer, so no new sentence restates chapter 14 or chapter 19's gloss (docs/04 Writing the book, No filler).
4. docs/03 needs no change: `free line` already holds the definition the chapters now follow; no new queue line (docs/03).

**Behaviour.**

* A reader of chapter 7 §The git strategy reads that trunk fits one person, alone or with several sessions on free lines, queue lines not done, not waiting and needing no other line done first, defined yet or not, that touch different files, with chapter 14 named as where free lines are taught.
* A reader of chapter 18 §Choosing reads the same gloss and pointer in the Trunk bullet.
* Failure: a reader who meets "free lines, deliveries ready to build" (7:59) or "free lines, queue lines ready to build" (18:165) takes a line with no page yet, or one being defined, for not free, and so thinks two sessions on trunk can only build, not define, at once; after this delivery no sentence in either chapter, in either edition, glosses a free line as ready to build.
* Edge: a line whose `after` names a line not done is not free; the gloss says so with "needing no other line done first", as chapter 19 already does.
* Edge: chapter 14's definition (en 14:57 and 14:129, pt 14:58 and 14:130), chapter 19's gloss (19:23) and chapter 18's key point (18:185) agree with docs/03 already and stay as they are.
* Edge: the Portuguese edition says the same with its fixed words, "linha livre", "fila", as pt 14 and pt 19 already do.

**Contract.**

The finding was re-checked, not taken on trust: en and pt 7:59 gloss free lines as "deliveries ready to build" / "entregas prontas para construir", and en and pt 18:165 as "queue lines ready to build" / "linhas da fila prontas para construir"; docs/03's `free line` row is "a line not `[x]` and not `[?]` whose `after` lines are all `[x]`", which includes `[ ]`, `[~]`, `[>]` and `[*]`. It holds.

* **Chapter 7, both editions** (`book/en/07-the-documents.md`, `book/pt/07-the-documents.md`), file name, title and headings kept.
  1. Line 59, en: "alone or with several sessions on free lines, deliveries ready to build, that touch different files;" becomes "alone or with several sessions on free lines (queue lines not done, not waiting and needing no other line done first, defined yet or not; [chapter 14](14-queue-states.md)) that touch different files;". The rest of the sentence is unchanged.
     pt: "sozinha ou com várias sessões em linhas livres, entregas prontas para construir, que mexem em arquivos diferentes;" becomes "sozinha ou com várias sessões em linhas livres (linhas da fila que não estão prontas, não estão esperando e não precisam de outra linha pronta antes, já definidas ou não; [capítulo 14](14-queue-states.md)) que mexem em arquivos diferentes;".
  2. Nothing else in chapter 7 changes.
* **Chapter 18, both editions** (`book/en/18-git-essentials.md`, `book/pt/18-git-essentials.md`), file name, title and headings kept.
  1. Line 165, en: "alone or with several sessions open on free lines, queue lines ready to build, that touch different files:" becomes "alone or with several sessions open on free lines (queue lines not done, not waiting and needing no other line done first, defined yet or not; [chapter 14](14-queue-states.md)) that touch different files:". The rest of the bullet is unchanged.
     pt: "sozinha ou com várias sessões abertas em linhas livres, linhas da fila prontas para construir, que mexem em arquivos diferentes:" becomes "sozinha ou com várias sessões abertas em linhas livres (linhas da fila que não estão prontas, não estão esperando e não precisam de outra linha pronta antes, já definidas ou não; [capítulo 14](14-queue-states.md)) que mexem em arquivos diferentes:".
  2. Nothing else in chapter 18 changes; the key point at line 185 stays.
* **Terms:** `free line` / `linha livre`, as docs/03 has it; docs/03 unchanged. No new term, no new queue line.
* **Sources:** docs/03 `free line`, and chapter 14 §The next line, and which run together, the book's own definition; no source note.
* **Cases:** none. Code examples: none.

**Overlap with the lines in flight (docs/06 M15).**

* `ch18-log-evidence` also edits chapter 18, the log (18:45, 49) and the gain (18:177); this page touches only 18:165. Different lines of one file: on trunk the two should not run at the same time, or the second stages by hunk.
* `stack-rule-once` (chapters 6, 9, 22), `code-width` and `pt-fixed-terms` touch neither chapter 7 nor chapter 18.

**Out of scope.**

* Chapter 19:23's gloss, after chapter 14: whether it should only point is not this line's; a candidate for the next review, with chapters 7 and 18 now glossing too.
* Chapter 10:90, which points to chapter 11 for the next free line while chapter 14 defines it: not named by this line; a candidate for the next review.
* Chapter 14's definition and key point: correct, unchanged.
* docs/03, docs/05, docs/06 wording: unchanged.

**Done when.**

* [x] Chapters 7 and 18 changed in both editions, same headings; each still opens with its value; no filler and nothing useful cut.
* [x] `grep -n -i -E "ready to build|prontas? para construir" book/*/07-the-documents.md book/*/18-git-essentials.md` prints nothing.
* [x] Both chapters' glosses say a free line may be not yet defined and needs no other line done first, and link chapter 14.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Built.** The four sentences changed as the Contract says, word for word, in both editions; nothing else in chapters 7 and 18 changed. The first occurrence of this gloss is chapter 19's sentence; chapters 7 and 18 now say the same in place, with "defined yet or not" added, and point to chapter 14, which keeps the definition. No abstraction, no new term, no queue line from the build.

**Divergences.** None. Line numbers on the page held (7:59 and 18:165 in both editions).

**Proof.** `grep -n -i -E "ready to build|prontas? para construir" book/*/07-the-documents.md book/*/18-git-essentials.md` prints nothing. `make verify` green. `make book` builds `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, given to the author.

**Decisions in /apply.** None taken without the author beyond the page's own list.

**Review.** A read-only agent on Opus read this delivery's diffs against the page and docs/04. Findings:

1. The queue line was still `[*]` while the page sat in `work/done/`: the review ran before the last edit; fixed, the line is `[x]`.
2. In Portuguese, "pronta" means both done and ready, so "não estão prontas" can read as "not ready", the reading this delivery removes; chapter 14's marks say done with "feita". The page fixes this wording and it matches chapter 19's gloss, so it stays here; the change for chapters 7, 18 and 19 together became the queue line `pt-free-line-done`.

No other finding: the four sentences match the Contract, both editions mean the same, no em dash, the link targets exist, the gloss matches docs/03.

```commit
docs(free-line-gloss): gloss a free line as docs/03 defines it

- chapter 7's git strategy glosses a free line, defined yet or not
- chapter 18's Trunk bullet says the same and points to chapter 14
- both editions; no other sentence of either chapter changes
- queue line pt-free-line-done added from the review

work/done/free-line-gloss.md
```
