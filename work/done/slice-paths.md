# slice-paths

**Objective.** A reader of chapters 13, 14 and 19 meets the lending library's code where chapter 4 put it, every slice under `src/features/<name>/`, so the folders those chapters reason about (which lines can run together, what a commit takes) are the folders chapter 4 taught, in both editions. Found by `m15-review` (work/done/m15-review.md, B11: "13:87, 14:66-67, 19:25-88: `src/<slice>/` paths against `src/features/<name>/`. Seen.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one. Review these first.

1. Slices that chapter 4's tree does not list (`reservations` / `reservas` in chapter 14, `reports` / `relatorios` in chapter 19) keep their names and only gain the `src/features/` prefix; chapter 4's tree does not grow. The queue line asks for the prefix, chapter 19:25 already says its slugs and paths are an illustration written for the chapter, and docs/03's `vertical slice` and `feature` rows admit a feature that keeps nothing. Renaming `reports` to the thing it does (`overdue/`) was the alternative, closer to docs/03's wording but beyond the finding. Source: docs/06 line `slice-paths`, chapter 19:25, docs/03.
2. `return-book` / `devolver-livro` touches `src/features/loans/` / `src/features/emprestimos/`, the prefix only, not chapter 4's sub-feature `src/features/loans/return/`. The whole loans slice includes its `return/` subfolder, so the sentence stays true, and chapter 19's later sentences (19:70, 19:88) need both deliveries to share the loans folder. Naming `return/` was the alternative, more precise but it changes the illustration's reasoning in four places. Source: chapter 4 tree, chapter 19.
3. 19:69's file `src/loans/loan.ts` becomes `src/features/loans/rules.ts` (pt `src/emprestimos/emprestimo.ts` becomes `src/features/emprestimos/regras.ts`): no `loan.ts` exists in chapter 4's tree, which lists `rules.ts` / `regras.ts` in the loans slice, and the phrase is being rewritten anyway. Keeping the file name with the prefix only was the alternative, a file the book shows nowhere. Source: chapter 4 tree (en 41-44, pt 41-45).
4. `features/` stays in English in the Portuguese edition, with no note in chapters 13, 14 or 19: docs/03's running example row and docs/04 (Portuguese edition's code) fix it, and chapter 4 already shows `src/features/emprestimos/` without comment. A note on the kit's English folder names, if wanted, is `pt-placeholders`'s. Source: docs/03, docs/04.
5. Only paths change: each sentence keeps its words, its order and its meaning; no heading, no key point, no gain section moves. Source: docs/06 line `slice-paths`, AGENTS.md (no filler, nothing useful cut).
6. No docs/03 term (the `vertical slice` row already gives `features/<name>/`), no new queue line, no split: three chapters, eleven lines per edition, one page. Source: docs/03, docs/05 §1.

**Behaviour.**

* A reader of chapter 13 §What it reads (line 87) reads that another session's edit to `src/features/members/` (pt `src/features/membros/`) sits in the tree; line 76 already names `src/features/loans/` (pt `src/features/emprestimos/`) and is unchanged.
* A reader of chapter 14 (lines en 66-67, pt 67-68) reads that `search-catalog` and `reservations`, in `src/features/catalog/` and `src/features/reservations/` (pt `buscar-catalogo` e `reservas`, em `src/features/catalogo/` e `src/features/reservas/`), can run together, and that two lines that both change `src/features/loans/` (pt `src/features/emprestimos/`) cannot.
* A reader of chapter 19 (lines 25 to 88, both editions) reads the two free lines `return-book` touching `src/features/loans/` and `overdue-list` touching `src/features/reports/` (pt `devolver-livro`, `src/features/emprestimos/`; `lista-de-atrasos`, `src/features/relatorios/`), and every later mention of those folders, the commit with a pathspec and the same-hunk example in `src/features/loans/rules.ts` (pt `src/features/emprestimos/regras.ts`), with the same paths.
* A reader moving from chapter 4 to chapters 13, 14 and 19 finds no slice outside `src/features/`; `src/lib/` (chapters 3 and 4) is not a slice and stays as it is.
* Fails: any `src/<slice>/` path left in `book/` without `features/`; one edition changed and not the other; a sentence whose meaning changed beyond its path; chapter 4 or chapter 3 touched.
* Edge: chapter 19's parenthesis at line 25, "the slugs and paths are an illustration, written for this chapter", stays: the paths are still written for the chapter.

**Contract.**

The finding was re-checked, not taken on trust: chapter 4 (en 41-48, pt 41-49) lays the library out under `src/features/`; chapters 13, 14 and 19 write `src/loans/`, `src/members/`, `src/catalog/`, `src/reservations/`, `src/reports/` and their Portuguese twins. It holds.

Line numbers are as of this page; /apply finds each passage by its text. In each passage only the path changes.

* **Chapter 13** (`book/en/13-apply.md`, `book/pt/13-apply.md`), line 87: `src/members/` becomes `src/features/members/`; pt `src/membros/` becomes `src/features/membros/`.
* **Chapter 14** (`book/en/14-queue-states.md`, `book/pt/14-queue-states.md`):
  * en 66 / pt 67: `src/catalog/` and `src/reservations/` become `src/features/catalog/` and `src/features/reservations/`; pt `src/catalogo/` and `src/reservas/` become `src/features/catalogo/` and `src/features/reservas/`.
  * en 67 / pt 68: `src/loans/` becomes `src/features/loans/`; pt `src/emprestimos/` becomes `src/features/emprestimos/`.
* **Chapter 19** (`book/en/19-worktrees.md`, `book/pt/19-worktrees.md`), same lines in both editions:
  * 25: `src/loans/` and `src/reports/` become `src/features/loans/` and `src/features/reports/`; pt `src/emprestimos/` and `src/relatorios/` become `src/features/emprestimos/` and `src/features/relatorios/`.
  * 44: `src/loans/` becomes `src/features/loans/`; pt `src/emprestimos/` becomes `src/features/emprestimos/`.
  * 45: `src/reports/` becomes `src/features/reports/`; pt `src/relatorios/` becomes `src/features/relatorios/`.
  * 48: `git commit -- docs/06-Queue.md src/loans/` becomes `git commit -- docs/06-Queue.md src/features/loans/`; pt `src/emprestimos/` becomes `src/features/emprestimos/`.
  * 69: `src/loans/loan.ts` becomes `src/features/loans/rules.ts`; pt `src/emprestimos/emprestimo.ts` becomes `src/features/emprestimos/regras.ts` (Decided 3).
  * 70: `src/loans/` becomes `src/features/loans/`; pt `src/emprestimos/` becomes `src/features/emprestimos/`.
  * 88: `src/loans/` becomes `src/features/loans/`; pt `src/emprestimos/` becomes `src/features/emprestimos/`.
* Files: these six; no other file. Chapter 4 and chapter 3 unchanged.
* Terms of docs/03: none new; `vertical slice` and `feature` used as they stand. Sources: none added or removed. Cases: none. Code examples: none new; the paths belong to the lending library written for the book (ADR-0017).
* docs/00 to docs/05 and docs/03: no change. docs/06: this line `[>]` by the driver, `[*]` when /apply starts, `[x]` by /apply. No new queue line.

**Deliveries in flight on the same chapters.**

* `pt-free-line-done` (`[ ]`, page drafted): pt 19:23 only; no line in common.
* `ch19-when-worktrees-pay` (`[ ]`): chapter 19 at 84 and 242-268; no line in common.
* `batch-propose` (draft page): may add to chapter 19's section "When parallel stops paying" or to chapter 22; its draft names no line of this page.
* `code-width` (`[ ]`): code blocks in chapters 13 and 14; none of these lines is in a code block.
* `pt-placeholders` (`[ ]`): pt chapters 13 and 19, placeholders and folders written for a chapter; it may touch the same pt folder names of chapter 19. Run it after this line, or let its page read these paths as this page leaves them.
* `case-a-board-once` (`[*]`): chapters 16 and 20; no file in common.
* Rule for all: not at the same time on the same file, or staged by hunk (docs/05 §4).

**Out of scope.**

* Chapter 4's tree: the source the others follow, unchanged.
* Renaming `reports` or `reservations`, or naming the `return/` sub-feature (Decided 1 and 2): beyond the finding.
* A note on `features/` staying English in Portuguese (Decided 4): `pt-placeholders` if anywhere.
* `src/lib/` in chapters 3 and 4: not a slice.
* Any other wording in chapters 13, 14 and 19: other findings have their own lines.

**Done when.**

* [x] Both editions changed as the Contract says, same headings; each chapter still opens with its value; no filler and nothing useful cut; no em dash added.
* [x] `grep -rn -E "src/(loans|members|catalog|reservations|reports|emprestimos|membros|catalogo|reservas|relatorios)/" book/` prints nothing.
* [x] `grep -c "src/features/"` prints 2 for chapter 13, 2 for chapter 14 and 7 for chapter 19, in each edition.
* [x] `grep -rn "loan\.ts\|emprestimo\.ts" book/` prints nothing.
* [x] `book/en/04-focus.md` and `book/pt/04-focus.md` unchanged.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Proof.** The Done when greps: the `src/<slice>/` grep prints nothing; the `loan.ts` grep prints nothing; `grep -c "src/features/"` prints 2 for chapter 13, 2 for chapter 14 and 7 for chapter 19, in each edition. `git diff` shows `book/en/04-focus.md` and `book/pt/04-focus.md` unchanged, and in the six chapters only paths changed, ten lines per edition. `make verify` green (build, parity, em dash, prose, links, disclosure). `make book` builds `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences.** Decided 6 counts eleven lines per edition; the Contract lists ten (13:87, two in chapter 14, seven in chapter 19), and ten changed. The count was wrong, not the scope.

**Omissions.** None.

**Decisions taken in /apply.** None beyond the page's; no question arose.

**Review.** Delivery review by a read-only Opus agent on this delivery's diffs against the page and docs/04: nothing breaks the page, docs/04 or this delivery's lines. No `src/<name>/` path without `features/` is left in `book/` besides `src/lib/`; chapter 4's tree has `rules.ts` / `regras.ts` in the loans slice; every hunk matches across editions with Portuguese names in pt; each sentence reads correctly with the longer path; no em dash; the commit block follows docs/05 §6. Two cosmetic notes on the page, both left as written: Decided 6's "eleven", already recorded under Divergences, and Decided 3's pt range 41-45 against the Contract's 41-49, both containing `regras.ts`. No new queue line.

```commit
docs(slice-paths): put the library's slices under src/features/

- chapters 13, 14 and 19 name each slice as src/features/<name>/
- chapter 19's same-hunk example names chapter 4's rules.ts / regras.ts
- both editions changed alike; chapters 3 and 4 unchanged

work/done/slice-paths.md
```
