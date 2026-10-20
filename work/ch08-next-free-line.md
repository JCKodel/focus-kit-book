# ch08-next-free-line

**Objective.** After chapter 8 the reader reads the update excerpt's next command as the record wrote it: the line that comes next, and the condition under which it is free, never a line called the queue's first free line while its `after` is still in flight.

**Behaviour.**

* Given the excerpt in "What an update reports" / "O que uma atualização relata", the reader sees its last line name `/propose ch08-update-2026-10-19-2` and the condition the record's Step 5 gives, once `kit-2026-10-19-2`, the update itself, is `[x]`: at the time of the report that line's `after` was the update in flight, so it was not yet free (docs/03 `free line`).
* The reader can square that line with the paragraph after the excerpt (en 103, pt 105), which says the update names the command docs/06's first free line wants: the line named becomes the first free line when the update's own line closes, and the excerpt says so.
* Fails: an excerpt `Next:` that calls `ch08-update-2026-10-19-2` "the queue's first free line" (en :84, pt :85-86, finding C2 of `work/done/m23-review.md`, from lead L2); a condition the record does not hold; a row of the block over 74 columns (docs/04, **Width of a block**); one edition changed without the other.
* Edge: nothing else in the excerpt or the chapter changes; the Portuguese manual phrase at pt :71 ("devido pela") inside the same block is `ch07-09-manual-wording`'s, not this delivery's.

**Contract.** Both editions, same change; English is the source (ADR-0004). Line numbers as the files are now.

* `book/en/08-install-and-hosts.md`, the excerpt's last line, :84:
  * now: `Next: /propose ch08-update-2026-10-19-2, the queue's first free line.`
  * becomes: `Next: /propose ch08-update-2026-10-19-2, once kit-2026-10-19-2 is [x].` (70 columns)
* `book/pt/08-install-and-hosts.md`, the excerpt's last two lines, :85-86:
  * now: `Próximo: /propose ch08-update-2026-10-19-2, a primeira linha livre` / `da fila.`
  * becomes: `Próximo: /propose ch08-update-2026-10-19-2, quando` / `kit-2026-10-19-2 estiver [x].`
* The mark is written `[x]` without backticks, since the line sits inside a fenced block where backticks would print.
* Nothing else in either file changes: the lead-in, the other excerpt lines, the explanation after the block and the other sections stay.
* Terms of docs/03: `free line` / `linha livre`, already present; no new row.
* Sources: the record already named in the lead-in, `work/done/kit-2026-10-19-2.md`, Step 5 (:89) and its Behaviour (:9): "the next command is the first free line's, `/propose ch08-update-2026-10-19-2`, once this line is `[x]`". No source note added.
* Neighbouring line on the same files: `ch07-09-manual-wording` (docs/06 :585) edits chapter 8 too, at pt :71 in the same block; this line comes first in queue order, and its change sits on other rows, so the two do not overlap.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.**

* The record page `work/done/ch08-update-2026-10-19-2.md`, whose Decisions taken alone (:49) dropped the condition and left it to the review: kept as written, history; the review's finding is the correction. Its other fixes are `m23-records-proof`'s and `m23-records-crossrefs`'s.
* Chapter 8's other passages and the excerpt's other items, including M23's weak candidates C1, C3, L1b, L1d: the checker dropped them.
* Chapter 17's sample next free line: `ch17-next-free-line`.
* The excerpt at 2026.10.20: `ch08-update-2026-10-20` rewrites it later, after `kit-2026-10-20`.

**Decisions from the documents.**

* Keep the record's condition rather than only drop "the queue's first free line": the excerpt says it is paraphrased from the record (en :56), and the record's Step 5 holds the condition; docs/03 `free line` makes a line whose `after` is not `[x]` not free.
* Both editions in one delivery (ADR-0004, AGENTS.md); 74 columns per block row (docs/04).

**Decisions taken alone.**

* Of the queue line's two options, the first: the condition kept, naming the update's line by its slug, `kit-2026-10-19-2`, since a reader of the chapter has no "this line" to resolve.
* Portuguese wording "quando kit-2026-10-19-2 estiver [x]", the plain reading of "once ... is [x]".
* The record page `ch08-update-2026-10-19-2` is not edited: its decision was real, and the change belongs to this page.

**Done when.**

* [ ] en :84 and pt :85-86 read as the Contract says; nothing else in either file changed.
* [ ] Both editions written, the chapter still opens with its value, no filler, nothing useful cut, every number sourced.
* [ ] `make verify` green (parity, width, em dash, prose rules, links, disclosure).
* [ ] `make book` run, both PDF paths given, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, with the excerpt's last line read in each.
* [ ] The Delivery review as docs/05 §5 says.
