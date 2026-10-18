# pt-ch19-index-word

**Objective.** A reader of the Portuguese chapter 19 reads its key point on committing as "a partir do índice", the word chapter 13 and chapter 19's batch paragraph use for the staged copy, so the edition names one thing with one word, as the English does with "index".

**Decided without the author.** This page was written in a batch /propose with no question asked (the author's instruction for this run); each decision names its source, so the author corrects it in the review of this page.

1. Portuguese only. The English key point, `book/en/19-worktrees.md:321`, already says "Commit from the index", so the source holds and only the translation follows it (ADR-0004: English is the source; the change brings the Portuguese to it, and no English text changes).
2. The word is "índice", as `book/pt/13-apply.md:194` ("faça o commit de uma entrega por vez, a partir do índice") and `book/pt/19-worktrees.md:274-275` say; 19:274 glosses it ("a cópia em stage de onde o commit é feito") before the key point, so the key point needs no gloss of its own.
3. Only the noun at 19:321 changes. The verb "colocar em stage" and "o que está em stage" elsewhere in the chapter stay: they are docs/03's term `stage` (pt "stage"), the action, not the staged copy. The noun "o stage" at 19:272 ("O que ele muda é o stage") also stays: it names the act of staging, as the English "the staging" does, not the index; changing it is a widening (docs/05 §8).
4. No docs/03 row: "índice" is not a term there, and the finding asks for none.
5. Kit: nothing to tell; this is the book's translation.

**Behaviour.**

* A reader of the Portuguese chapter 19 §Pontos-chave reads, in the third bullet: "Faça o commit a partir do índice quando `git diff --cached --stat` guarda só aquela entrega; ...", the rest of the bullet as it is.
* The same reader finds "índice" for the staged copy in chapter 13's commit sentence, in 19's batch paragraph and in 19's key point, and "stage" nowhere as a name for it.
* The English edition reads as before.
* Edge: a search of `book/pt/19-worktrees.md` for "a partir do stage" finds nothing.

**Contract.**

* `book/pt/19-worktrees.md:321`: "Faça o commit a partir do stage" becomes "Faça o commit a partir do índice"; nothing else on the line or in the file changes.
* `book/en/19-worktrees.md`: unchanged (decision 1).
* No new docs/03 term; no source note; no case drawn on.

Shared files and order: in this M17 batch, `conflict-same-lines`, `ch19-adjacent-mark-staging` and `pt-librarian-masculine` also edited `book/pt/19-worktrees.md`, and all three are done, so this page reads the file as they left it. No other line of the batch touches it. /apply stages its one hunk of `book/pt/19-worktrees.md` and its own line of docs/06 by hunk (docs/05 §6), since other sessions change docs/06 at the same time.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* "o stage" at 19:272: the act, not the copy (decision 3).
* The verb "colocar em stage" across the edition: docs/03's term.
* A docs/03 row for "índice" / index: not asked by the finding.

**Done when.**

* [x] `book/pt/19-worktrees.md:321` says "a partir do índice"; `grep -n "a partir do stage" book/pt` finds nothing.
* [x] The English edition unchanged (`git diff book/en` empty for this delivery).
* [x] `make verify` green.
* [x] `make book`, and the paths of both PDFs given to the author.
* [x] The delivery review run as docs/05 §5 says, and recorded.
* [x] Page in `work/done/`, line `[x]`, staged by hunk as the Contract says, commit message in a `commit` block.

**Built.** `book/pt/19-worktrees.md:321`: "Faça o commit a partir do stage" is now "Faça o commit a partir do índice"; nothing else in the file changed. The English edition is unchanged.

**Decisions at apply time.**

* Staging: the driver runs parallel sessions in one tree; this session staged nothing, and the driver commits the delivery from its own index. The driver runs `make book` once at the end.

**Divergences and omissions.** `make book` was not run in this session (the driver's instruction). The driver gives the PDF paths, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Proof.** `grep -n "a partir do stage" book/pt` finds nothing; `git diff book/en` holds nothing from this delivery; `make verify` is green.

**Delivery review.** One read-only Opus agent read the diff of `book/pt/19-worktrees.md` and `book/en/19-worktrees.md` against this page and docs/04. It had no findings.

```commit
docs(pt-ch19-index-word): say "a partir do índice" in chapter 19's key point

- The Portuguese key point names the staged copy "índice", as chapter 13 and the batch paragraph do
- Portuguese only; the English already says "index"

work/done/pt-ch19-index-word.md
```
