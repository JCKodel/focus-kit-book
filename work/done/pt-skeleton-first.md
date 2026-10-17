# pt-skeleton-first

**Objective.** A reader of the Portuguese edition's chapter 11 reads in the example queue that the `esqueleto` delivery left the first screenshot, as the English row says "first screenshot", and the row still fits in 74 columns. Found by the review of `code-width` (work/done/code-width.md, Review: "pt 11's `esqueleto` row, "tela capturada", loses the "primeira" of the English "first screenshot"").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one. Review these first.

1. Which word says screenshot? "screenshot", the word the Portuguese edition already uses for it: pt 12:44 ("o screenshot confere") and pt 13:50 and 13:76 ("um screenshot contra o design", "uma tela é provada por um screenshot"). "tela capturada" and "captura de tela" were the alternatives: two more words for one thing, and "tela" is docs/03's Portuguese for the FOCUS piece `view`, so "primeira tela" would read as "first view" (AGENTS.md, one word per thing; docs/03 `view` / `tela`).
2. How does "first" fit? As "1º": "primeiro screenshot" makes the row 79 columns, and the slug column stays aligned with the five rows under it, so the description has 53 columns. "app e servidor vazios, npm run verify, 1º screenshot" gives 73. The edition already abbreviates ordinals ("2ª ed." in pt 18's notes). Dropping "npm run verify" was rejected: chapter 11 says right after that the skeleton creates `npm run verify`, which every later delivery runs (pt 11:74), so the row is that sentence's evidence. Source: docs/04 **Width of a block**; scripts/check_width.py.
3. The English edition does not change: its row already says "first screenshot" in 72 columns; this delivery makes the Portuguese mean what the English means (ADR-0004, English is the source; AGENTS.md, a change to one edition is a change to both, satisfied here as parity restored with the English untouched, as `pt-free-line-done` did).
4. docs/03 needs no change and no queue line is added: "screenshot" is not a domain term of docs/03, and the edition's existing word is reused (docs/03; docs/05 §2).

**Behaviour.**

* A reader of pt chapter 11, in the queue of Marco 1 (§ before "Qualquer pessoa lê o estado nele"), reads the row `[x] esqueleto        app e servidor vazios, npm run verify, 1º screenshot`, and understands what the English reader understands from `[x] skeleton      empty app and server, npm run verify, first screenshot`: the skeleton produced the project's first screenshot.
* Failure: a reader of "tela capturada" learns that a screen was captured, not that it was the first; after this delivery no row of pt 11 says "tela capturada".
* Edge: the row is 73 columns; `python3 scripts/check_width.py` prints nothing for pt 11, and the PDF does not wrap it.
* Edge: the slug column of the block keeps its alignment: the description still starts at column 22, as in the rows `catalogo`, `membros`, `emprestar-livro`, `devolver-livro` and `m1-review`.
* Edge: the rest of the block, the milestone paragraph above it and the sentence about `npm run verify` below it stay word for word.
* Edge: the English edition reads the same before and after; parity holds, since one row inside a code block changes and no heading, line count or link does.

**Contract.**

The finding was re-checked, not taken on trust: pt 11:52 reads `[x] esqueleto        app e servidor vazios, npm run verify, tela capturada` (74 columns), en 11:49 reads `[x] skeleton      empty app and server, npm run verify, first screenshot`. Before `code-width` the Portuguese row said "primeira captura de tela" (82 columns). It holds.

* **Chapter 11, Portuguese edition** (`book/pt/11-queue-and-milestones.md`), file name, title and headings kept. In the queue block under "## Marco 1: uma bibliotecária empresta e recebe de volta" (line 52 when this page was written; find it by text), the row

  `[x] esqueleto        app e servidor vazios, npm run verify, tela capturada`

  becomes

  `[x] esqueleto        app e servidor vazios, npm run verify, 1º screenshot`

  with the same eight spaces after `esqueleto` (Decided 1, 2). Nothing else changes.
* **English edition:** unchanged (Decided 3).
* **Terms:** none new; docs/03 unchanged. "screenshot" as pt 12 and 13 already use it. No new queue line.
* **Sources:** none cited. **Cases:** none. **Code examples:** none (the row is a queue artifact written for the chapter, not code).

**Overlap with the lines in flight (docs/06).**

* `pt-placeholders` edits pt 11 too (at 19, per work/done/code-width.md), not this row. Different lines of one file: on trunk the two should not run at the same time, or the second stages by hunk. If another session's unstaged edit sits in the same queue block, /apply stops and reports per docs/05 §4 and §6 instead of staging a mixed hunk.

**States.** Not applicable: no screen.

**Visual reference.** Not applicable: no screen.

**Out of scope.**

* "tela" and "captura" elsewhere in the edition (pt 3's "capturada" is an exception caught; pt 13:84's "captura a tela" is a verb in prose): not this row, and not the same thing.
* Other queue rows of chapter 11 and the other chapters' blocks: `code-width` already fit them, and the review found no other meaning lost.
* The English edition and docs/03: unchanged (Decided 3, 4).

**Done when.**

* [x] pt chapter 11 changed as the Contract says, same headings; the English edition untouched; the chapter still opens with its value; no filler and nothing useful cut.
* [x] `grep -n "tela capturada" book/pt/11-queue-and-milestones.md` prints nothing.
* [x] `grep -n "npm run verify, 1º screenshot" book/pt/11-queue-and-milestones.md` prints the one row.
* [x] `python3 scripts/check_width.py` prints nothing.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Proof.**

* `grep -n "tela capturada" book/pt/11-queue-and-milestones.md` prints nothing; `grep -n "npm run verify, 1º screenshot"` prints pt 11:52 alone.
* The row measures 73 columns; `python3 scripts/check_width.py` prints nothing. The description starts at column 22, as in the five rows under it.
* `git diff --stat -- book/en` is empty.
* `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`; in the Portuguese PDF the row sits on one line.

**Divergences.** None.

**Review.**

A read-only Opus agent read the staged diff of pt 11 and this page, and docs/06's line, against this page, docs/03, docs/04 and the English edition. It confirmed the row at 73 columns with its description at column 22, "º" as the ordinal indicator, the English untouched, the Proof and every citation on this page. No findings. No new queue line.

```commit
docs(pt-skeleton-first): say the skeleton left the first screenshot

- pt 11's esqueleto row says "1º screenshot", as en says "first"
- the row stays at 73 columns, aligned with the rows under it

work/done/pt-skeleton-first.md
```
