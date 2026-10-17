# pt-fixed-terms

**Objective.** A reader of the Portuguese edition meets one word for each thing the English names with one word, the word docs/03 fixes (data de devolução, engine de banco de dados, tela, falso, worktree, verificação), one slug for `fix-due-date`, and reads in chapters 11 and 14 what the English says: the loan screen shows the due date, and the rules may refuse. Found by `m15-review` (work/done/m15-review.md: A6, A7, K4, B14, B15, B16, B17).

**Decided without the author.** The batch had no one to answer; each choice is the recommended one. Review these first.

1. Board columns (B15) leave the scope. `case-a-board-once` replaced chapter 20's fold with a pointer to chapter 14 (pt 20: "na coluna em que o capítulo 14 as dobra nas colunas de um quadro"), so pt 14 holds the only fold, with one set of names, A fazer, Fazendo, Feito, in its prose, its block and its key point. "To Do", "Doing" and "Done" in pt 14 (the opening and §O que o time ganha) are Case A's real Azure DevOps columns, the same names the English gives them, and stay. The queue line's text still names "board columns"; the driver may shorten it. Source: work/done/case-a-board-once.md; m15-review B15; docs/06.
2. The checks (K4) say "verificação" everywhere: pt 16's "checagem/checagens" for a step of a process and Ninjobs' 29 and 2 checks become "verificação/verificações", as pt 3 and 6 already say them. The other reading, "checagens" in pt 3 and 6 too, would leave "verificação" for `make verify` alone but costs some twenty sentences in two chapters the finding does not fault, and a check a delivery must pass before done is what the verify command runs; pt 16 already says "verificação" for the command two paragraphs later, so after this the chapter uses one word. "checagem manual" (pt 12, the Behaviour section; pt 16's "cada uma um teste ou uma checagem") names a different thing, a check a person makes by hand, and stays. Source: m15-review K4; docs/03 `verify` / `verificação`; pt 3, 6, 12, 16.
3. The `fix-due-date` slug (B17) is `corrigir-devolucao` in pt 14 and pt 20. It follows chapter 11's `formato-devolucao` (en `due-date-format`), where the slug's stem "devolucao" stands for the due date; `corrigir-vencimento` keeps the word docs/03 does not use, and `corrigir-data-de-devolucao` puts chapter 20's row at 82 columns, past docs/04's 74. Source: docs/03 running example row; docs/04 **Width of a block**; pt 11, 14, 20.
4. Due date, "data de devolução", replaces every noun that stands for it: "vencimento" and "data de vencimento" (pt 4), "a devolução" in the loan screen's line (pt 11), "o prazo" (pt 14, where "prazo" is docs/03's loan period, a different thing), and "devolução prevista" (pt 12 and 13, outside the review's chapters, included because the line asks for docs/03's word and these are the same noun). The verb "vencer" ("vence hoje", "vencer hoje ainda não é estar em atraso", pt 12 and 13) stays: it is the verb "is due", not a second noun. Source: docs/03 running example row ("data de devolução (due date)", "prazo de empréstimo (loan period)"); m15-review A6, A7.
5. Chapter 11's queue line keeps 74 columns by saying "a tela mostra a data de devolução em dia/mês/ano" (72): "do empréstimo" drops from the line, and the sentence before the block and the page's Objective both say "na tela do empréstimo". Source: docs/04 **Width of a block**; chapter 11 (one sentence per line).
6. A fake, as a noun, becomes "implementação falsa", or "repositório falso" when the thing is a repository, since docs/03 fixes "falso" as an adjective; the two section headings follow. Gerard Meszaros' own names in pt 5 (§O que é...) stay in English, in italics, as his: *fake* and *stub*, like "test doubles" beside them; "mock" stays, not a docs/03 term. The code's `falsos` (pt 5) is a name and stays. No anchor points to either heading, and parity compares heading levels, not their words. Source: docs/03 `fake` / `falso`; scripts/check_parity.py; m15-review A7.
7. The view, pt 4's "a view", becomes "tela", docs/03's word, and the sentence that said a view is not only a screen now says a tela is not only a graphical interface, which is what pt 4 already wrote; MVVM's "view model" (pt 4) is that pattern's name and stays. Source: docs/03 `view` / `tela`; m15-review A7.
8. Engine, pt 5's "motor" for a database engine, becomes "engine de banco de dados", feminine as pt 4 already writes it ("uma engine de banco de dados"); pt 16's "motor" is the governor's machine, not a database engine, and stays. Source: docs/03 `driver` row ("engine de banco de dados", never "motor" alone).
9. Worktree (B14) is masculine, "um worktree", as pt 7, 8, 14 and 19 write it; pt 10's sentence also says "uma branch", which becomes "um branch" in the same edit, since every other chapter says "um branch". Source: docs/03 `worktree`; m15-review B14.
10. The English edition does not change: it is the source and already says each of these things with one word; this delivery makes the Portuguese mean what it means (AGENTS.md; ADR-0004).
11. No docs/03 term, no new queue line, no split: about forty word swaps in ten Portuguese chapters, grouped by term, fit one page. Source: docs/03; docs/05 §1.
12. (/apply) The queue line drops "board columns" from its list, as Decided 1 allows: it now names due date, engine, view, fake, worktree, the checks and the fix-due-date slug. Source: the driver's brief; Decided 1.

**Behaviour.**

Passages are found by their words; line numbers are as of commit `7a3c4f5`. The proposed text is what /apply writes unless a better wording keeps the meaning, docs/03's word and, inside a code block, 74 columns.

* Due date. A reader of pt 4's numbered walk-through reads that `emprestar` returns an `Emprestimo` "com data de devolução 21 dias depois" (was "com vencimento 21 dias depois", 4:138), and that `Emprestado` "mostra a data de devolução" (was "a data de vencimento", 4:140).
* A reader of pt 11 reads the queue line, in both blocks (11:100 and 11:148): `[ ] formato-devolucao   a tela mostra a data de devolução em dia/mês/ano` (and `[x]` in the second), 72 columns; and in the page's first Behaviour bullet, "* Um empréstimo com data de devolução 2026-03-05 mostra 05/03/2026, numa" / "  tela estreita também." (72 and 23 columns).
* A reader of pt 12's page reads the first Behaviour bullet's middle as "aparece como emprestado a ele, com data de devolução 21 dias depois" / "(docs/00)." rewrapped under 74 (69 columns for the long row); a reader of pt 13 reads "o empréstimo com a data de devolução 21 dias depois" (13:78).
* A reader of pt 14 reads that `emprestar-livro` "põe a data de devolução um dia antes no fim de um mês" and that the fix is `corrigir-devolucao`, in 14:77 (twice: the line and `blocked: after corrigir-devolucao`) and 14:85; and a reader of pt 20 reads the issue row `[ ] corrigir-devolucao  data de devolução um dia antes no fim do mês (#42)`, 74 columns.
* B16. A reader of pt 14's queue reads `[*] emprestar-livro   a bibliotecária empresta, e as regras podem recusar` (73 columns), as the English "the rules may refuse".
* Engine. A reader of pt 5's table reads the repository row's last cell as "o arquivo do banco, pela mesma engine de banco de dados em memória" and, at the unique index, "testada contra a engine de banco de dados real e o esquema real" (5:26, 5:85).
* View. A reader of pt 4 §As quatro peças (4:115-116) reads: "Uma tela não é só uma interface gráfica." / "O JSON que uma API responde é uma tela, e o texto que uma ferramenta de linha de comando imprime também: a tela é a saída da computação, entrada, processamento, saída, em qualquer forma que deixe o programa."
* Fake. A reader of pt 3, 4 and 5 meets no "fake" as the book's word:
  * pt 3:135: "o teste dele passa a precisar de um repositório falso para cada um";
  * pt 4:189: "**Um teste passa repositórios falsos.** Um repositório falso é uma segunda implementação que responde o que o teste define, ..." (the gloss "(um falso)" goes);
  * pt 4:192 heading: "## Dependências só onde existe uma implementação falsa";
  * pt 4:201: "a real e a falsa que os testes passam";
  * pt 4:237: "só onde o teste dela passa uma implementação falsa";
  * pt 5:4: "Você também consegue escrever uma implementação falsa que faz o teste falhar ..." (the gloss "(uma implementação falsa)" goes);
  * pt 5:33 heading: "## O que é uma implementação falsa";
  * pt 5:36: Meszaros' names in italics, "é um *fake*, e ... é um *stub*";
  * pt 5:37: "Este livro chama os dois de implementações falsas";
  * pt 5:42: "Uma implementação falsa deixa o teste conferir o que importa";
  * pt 5:48: "um teste que o troca por uma implementação falsa não testa nada";
  * pt 5:112: "o repositório falso lançaria e o teste falharia";
  * pt 5:155: "Uma implementação falsa responde o que o teste define ...; prefira-a a um mock".
* Worktree. A reader of pt 10:31 reads "trunk, um branch por entrega ou um worktree por entrega", and of pt 14:53 "Em um branch ou em um worktree".
* The checks. A reader of pt 16 reads "Uma verificação aqui, um modelo ali" (16:9), "29 verificações que nunca pegaram um erro no produto" (16:10), "aquelas verificações saíram" (16:26), "Duas verificações ficaram no lugar delas" (16:27), and "e duas verificações, depois de as verificações antigas a terem acompanhado" (16:60); "cada uma um teste ou uma checagem" (16:46) stays (Decided 2).
* Edge: the English edition reads the same before and after; parity holds, since no heading level, line count outside the rewrapped rows, note key or link changes.
* Edge: every code-block row this page changes measures 74 columns or fewer, a column being a character, so it passes `code-width`'s check whichever lands first.
* Fails: a pt chapter still saying "vencimento", "motor" for a database, "a view" for the piece, "fake" as the book's word, "uma worktree", "checagens" for Ninjobs' checks, or `corrigir-vencimento` / `corrigir-data-de-devolucao`; a changed row past 74 columns; a sentence whose meaning differs from the English one beside it.

**Contract.**

The findings were re-checked against the tree, not taken on trust: each holds as quoted in m15-review, except B15, whose chapter-20 half `case-a-board-once` removed (Decided 1).

* **Portuguese edition only**, file names, titles and heading levels kept: `book/pt/03-simplicity-and-results.md`, `04-focus.md`, `05-testing-each-piece.md`, `10-quick-guide.md`, `11-queue-and-milestones.md`, `12-propose.md`, `13-apply.md`, `14-queue-states.md`, `16-the-governor.md`, `20-team-tools.md`; the passages of Behaviour, nothing else. Two headings change their words: pt 4 §Dependências só onde existe uma implementação falsa and pt 5 §O que é uma implementação falsa.
* **Code blocks changed**, with their width: pt 11 queue row, twice (72); pt 11 page bullet (72, 23); pt 12 page bullet (69 and shorter rows); pt 14 queue row (73); pt 20 issue row (74). Slug columns stay aligned as they are.
* **English edition:** unchanged (Decided 10).
* **Terms of docs/03** used, none added: `due date` / `data de devolução` and `loan period` / `prazo de empréstimo` (running example row), `driver` (its "engine de banco de dados"), `view` / `tela`, `fake` / `falso`, `worktree`, `verify` / `verificação`. docs/03 unchanged.
* **Sources:** none added or removed; pt 5's Meszaros note stays where it is.
* **Cases:** Ninjobs' published counts in pt 16 (29 checks, 2 kept) keep their numbers; only the word changes. No Case A or Case B passage changes; Case A's board columns stay (Decided 1).
* **Queue:** no new line. The driver may shorten this line's text to drop "board columns" (Decided 1).

**Overlap with the lines in flight (docs/06).**

* `code-width` changes pt 11's milestone paragraph and its other queue rows (`esqueleto`, `emprestar-livro`, `devolver-livro`), pt 13's commit bullet and en 14's `due-reminder` row; this page changes pt 11's `formato-devolucao` rows and Behaviour bullet, and pt 14's `emprestar-livro` row, in the same files and, for pt 14, the same block. Run the two one after the other, either order, or stage by hunk; /apply stops and reports per docs/05 §4 and §6 when another session's unstaged edit sits in a hunk it would stage.
* `pt-placeholders` (pt 11, 13, 19, 21) touches pt 11 and pt 13 at other passages (pt 13:167-176); same rule.
* `ch10-commit-message` (chapter 10's commit message) and `ch12-review-skill` touch chapters 10 and 12 elsewhere; same rule.

**Out of scope.**

* Case A's "To Do", "Doing", "Done" in pt 14: the real board's names, as the English gives them (Decided 1).
* "checagens" in pt 3 and 6, and "checagem" for a manual check (pt 12, 13, 16:46, 21): Decided 2.
* The verb "vencer" for "is due" (pt 12, 13) and "vencidos" (pt 19's `lista-de-atrasos` row): verbs and an adjective, not a second noun for the due date.
* The slugs `formato-devolucao` (pt 11, 17) and `aviso-prazo` (pt 14): not named by the findings; "prazo" in `aviso-prazo` reads as a deadline, and renaming it touches a block `code-width` also edits.
* "bibliotecária" against docs/03's "bibliotecário", and "verify" (A7, B13): marked weak by the review, not this line's.
* pt 16's "motor" in the governor's image: a machine, not a database engine (Decided 8). MVVM's "view model": a pattern's name (Decided 7).
* "mock", "stub", "test doubles": the literature's names, not docs/03 terms.

**Done when.**

* [x] The ten Portuguese chapters changed as Behaviour says, same heading levels; the English edition untouched; each chapter still opens with its value; no filler and nothing useful cut.
* [x] `grep -n -E "vencimento|motor em memória|motor real|a view\b|é uma view|\bfakes?\b|uma worktree|uma branch|devolução prevista|corrigir-vencimento|corrigir-data-de-devolucao|regras recusam|checagens" book/pt/0[345]*.md book/pt/1[0-46]*.md book/pt/20*.md` prints only pt 5's italic *fake* (Meszaros' name) and nothing else.
* [x] `grep -n -E "corrigir-devolucao|podem recusar|data de devolução 21 dias|engine de banco de dados|implementação falsa|um worktree por entrega" book/pt/0[45]*.md book/pt/1[0-4]*.md book/pt/20*.md` prints the passages of Behaviour.
* [x] Every changed code-block row measures 74 columns or fewer (the widths in the Contract), checked by `code-width`'s `scripts/check_width.py` if it has landed, else by counting characters.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Proof.**

* Both Done when greps run as written: the first prints only pt 5:36's italic *fake*; the second prints pt 4:122 (already there), 4:138, 4:192, 4:237; pt 5:4, 26, 33, 42, 48, 85, 155; pt 10:32; pt 11:55 (already there); pt 12:56; pt 13:78; pt 14:34, 77 (twice), 85; pt 20:42.
* Widths, measured in characters after `code-width` landed: pt 11 queue rows 72 and 72, page bullet 72 and 23; pt 12 bullet 69 and 12; pt 14 row 73; pt 20 row 74. `scripts/check_width.py` green inside `make verify`.
* `git diff --stat -- book/en` is empty.
* `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences.** Two, from the review, both pt 5 sentences this delivery touched: 5:4 now says the implementação falsa "é chamada sem ser esperada", agreeing with its feminine subject; 5:48's "um caso de uso nunca é falso" became "nunca é trocado", since with "falso" now the book's word for a fake it read as "is never false", where the English says "is never faked". Found outside scope and left: pt 24:102's "o vencimento de uma subvenção" is a grant's deadline in chapter 24's experiment, not the lending library's due date.

**Review.**

A read-only Opus agent read the staged diff of these paths and docs/06's line against this page, docs/03, docs/04 and the English edition. It confirmed the Proof, the widths, the agreement after each swap and the meaning beside the English. Findings: the line still `[*]` (it becomes `[x]` as /apply's last edit); pt 5:4's participles and pt 5:48's "nunca é falso", fixed as Divergences say; pt 4:115-116's "o JSON ... é uma tela", correct by docs/03 and left for the author's reading of Decided 7; pt 20's "no fim do mês", left since "de um mês" puts the row at 77 columns. No new queue line.

```commit
docs(pt-fixed-terms): use docs/03's one Portuguese word for each thing

- data de devolução for the due date in pt 4, 11, 12, 13 and 14
- implementação falsa and repositório falso for a fake in pt 3, 4, 5
- engine de banco de dados, tela, um worktree, verificações (pt 4-16)
- corrigir-devolucao slug and "as regras podem recusar" in pt 14, 20

work/done/pt-fixed-terms.md
```
