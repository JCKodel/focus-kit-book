# ch11-blocking-fix

**Objective.** A reader of chapter 11 learns that a fix `/apply` finds outside its page becomes a `[ ]` line and makes the delivery wait only when the delivery needs it first, as chapter 13 teaches, and reads in both editions' queues of the lending library the same lines, word for word in meaning; both editions. Found by `m16-review` (work/done/m16-review.md): chA-3, "11:151 (pt :156) says every fix found outside the page is a line above that the delivery waits for; chapter 13:71 and the apply skill block only on a prerequisite"; chA-8, "pt 11:55, 56, 101 drop 'exemplar', the librarian and 'de empréstimo' from the en queue, a cut the 74-column width forced". Both seen.

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *The blocking rule is chapter 13's.* Chapter 13 says the build stops "when another line must be done first (a fix it found becomes a `[ ]` line above this one)" (13:43) and that anything else the review finds "becomes a `[ ]` line in the queue" with no wait (13:71); the kit's file for `/apply` says "A prerequisite fix becomes a `[ ]` line above this one"; chapter 14:76 shows the case. Chapter 11's clause is rewritten to say both halves. Source: chapters 13 and 14, `.claude/skills/apply/SKILL.md`, docs/05 §4 ("work already started finds it needs another line done first").
2. *The queues say the same by the English lines saying what the Portuguese can hold.* No Portuguese wording keeps the English lines' words inside docs/04's 74 columns, measured on 2026-10-18 with the slugs docs/03 fixes (`emprestar-livro`, `devolver-livro`) and the chapter's `formato-devolucao`:
   * "[>] emprestar-livro  a bibliotecária empresta um exemplar, e as regras podem recusar": 84 columns; the shortest with the librarian and `exemplar` that keeps "may refuse", "... um exemplar, a regra pode recusar", 79.
   * "[ ] devolver-livro   a bibliotecária registra a devolução · after emprestar-livro": 81; `· after emprestar-livro` takes 23 of them.
   * "[ ] formato-devolucao   a tela de empréstimo mostra a data de devolução em dia/mês/ano": 86; "data de devolução" is docs/03's term for due date and has no shorter synonym.
   So the English lines lose what the Portuguese cannot carry, and the Portuguese lines stay as they are: English is the source (ADR-0004), and a queue written for the chapter may say less as long as both editions say the same. The milestone paragraph above the queue still says the librarian lends a copy, and the sentence before the `due-date-format` line still names the loan screen, in both editions. The alternative, a Portuguese line that drops a different word (the librarian kept, "may" lost), changes what the line says and still differs from the English. Source: docs/04 §Writing the book, Width of a block; docs/03 (`running example`); the measures above.
3. *Every copy of the `due-date-format` line changes together.* The line appears at en 98 and 144 (pt 101 and 149), before and after its delivery; both English copies change, and the Portuguese pair already match. Source: chapter 11 as it stands.
4. *Chapter 14's queue is not this page's.* pt 14:34 has the same cut ("a bibliotecária empresta, e as regras podem recusar" against en "the librarian lends a copy, the rules may refuse") and pt 14:36 another ("o membro vê os dele" against "a member sees their loans"); chapter 14 is `ch14-four-waits`'s file in M17, and the finding named chapter 11. Reported to the driver for a line of its own; not fixed here.
5. No docs/03 term, no new queue line written by this page, no split.

**Behaviour.**

* A reader of chapter 11 §Changing the queue (pt §Mudando a fila), in the paragraph after the `due-date-format` page, reads the rule with its clause on `/apply` as:
  * en: "The rule holds in every session: during `/propose` the change is a new line, unless you ask for it on the page being written; during `/apply`, a fix found outside its page becomes a `[ ]` line, and only a fix the delivery needs first goes above it and makes it wait (chapter 14); and an edit made anyway, to "just change the label", is reverted before anything is committed."
  * pt: "A regra vale em toda sessão: durante o `/propose` a mudança é uma linha nova, a não ser que você a peça na página que está sendo escrita; durante o `/apply`, uma correção encontrada fora da sua página vira uma linha `[ ]`, e só uma correção de que a entrega precisa antes fica acima dela e a faz esperar (capítulo 14); e uma edição feita mesmo assim, para "só trocar o rótulo", é desfeita antes de qualquer commit."
* The same reader sees the lending library's queue in English as (widths 63, 52):
  * `[>] lend-book     the librarian lends, and the rules may refuse`
  * `[ ] return-book   records a return · after lend-book`
  
  matching the Portuguese lines, unchanged: `[>] emprestar-livro  a bibliotecária empresta, e as regras podem recusar` and `[ ] devolver-livro   registra a devolução · after emprestar-livro`.
* And the `due-date-format` line, both copies, in English as (width 69) `[ ] due-date-format   the screen shows the due date as day/month/year` and `[x] due-date-format   the screen shows the due date as day/month/year`, matching the Portuguese `formato-devolucao` lines, unchanged.
* Checked: `grep -c "is a line above it, which the delivery waits for"` on `book/en/11-queue-and-milestones.md` and `grep -c "é uma linha acima dele, pela qual a entrega espera"` on `book/pt/11-queue-and-milestones.md` give 0; `grep -c "only a fix the delivery needs first"` (pt `"só uma correção de que a entrega precisa antes"`) gives 1; `grep -c "lends a copy, and the rules\|the librarian records a return\|the loan screen shows"` on the English file gives 0; `grep -c "the screen shows the due date as day/month/year"` gives 2.
* Fails: one edition's clause changed and not the other's; the clause still saying every fix makes the delivery wait; a queue line over 74 columns (`make verify`, rule `width`); a Portuguese queue line changed; the two `due-date-format` lines differing; any other line of chapter 11 changed; an em dash.

**Contract.**

* Files: `book/en/11-queue-and-milestones.md`, `book/pt/11-queue-and-milestones.md`; no other file.
* Lines (working tree of 2026-10-18; the text is the locator, the numbers a courtesy): the rule's sentence in §Changing the queue, en 151, pt 156; the queue of §Milestone 1: a librarian lends and takes back (pt §Marco 1: uma bibliotecária empresta e recebe de volta), en 52 and 53 (pt 55 and 56 unchanged); the `due-date-format` line, en 98 and 144 (pt 101 and 149 unchanged).
* Terms of docs/03: none new (`queue line`, `dependency`, `waiting mark` as they are). Sources: none added or removed. Cases: none; no Case A, Case B or Ninjobs passage. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on nearby chapters.**

* `ch14-four-waits` (M17): chapter 14, which this page reads (14:76) and does not change (decision 4).
* `ch13-created-files` (M17): chapter 13 §What `/apply` does; this page leans on 13:43 and 13:71, which that line does not reword.
* `pt-ninjobs-article`, applied last: the Portuguese chapter 11 already writes "Na Ninjobs", so no hunk is shared.

**Out of scope.**

* Chapter 14's queue: decision 4.
* Chapter 15:107's `return-book` line, "the librarian records a return": its own chapter's example; after this page it differs from chapter 11's "records a return", reported to the driver beside decision 4.
* Rewording the Portuguese lines: decision 2.
* The section headings, the key points (none says a fix makes a delivery wait) and the rest of §Changing the queue: right as they stand.

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the results it names; the Portuguese queue lines byte for byte as before.
* [x] Chapter 11 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] `make verify` green: width, edition parity, prose rules, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, the change draws on no Case A or Case B passage (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block; decision 4's chapter 14 lines reported to the author.

**Proof.** On `book/en/11-queue-and-milestones.md`, `grep -c "is a line above it, which the delivery waits for"` gives 0, `grep -c "only a fix the delivery needs first"` gives 1, `grep -c "lends a copy, and the rules\|the librarian records a return\|the loan screen shows"` gives 0 and `grep -c "the screen shows the due date as day/month/year"` gives 2; on `book/pt/11-queue-and-milestones.md`, `grep -c "é uma linha acima dele, pela qual a entrega espera"` gives 0 and `grep -c "só uma correção de que a entrega precisa antes"` gives 1. `git diff book/` changes en 52, 53, 98, 144 and 151 and pt 156 only; the Portuguese queue lines are byte for byte as before. The changed queue lines are 63, 52 and 69 columns wide. `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences.** None from Behaviour.

**Decisions taken in /apply.**

* The English clause keeps the page's "goes above it", though the review noted "it" could be read as the `[ ]` line rather than the delivery ("goes above the delivery's line" would be clearer): Behaviour quotes the sentence whole, and the Portuguese "acima dela" points to "a entrega" by gender. Left as the page wrote it.
* Decision 4's chapter 14 lines (pt 14:34 and 14:36) and chapter 15:107's `return-book` wording are reported to the driver, not written as queue lines here: decision 5 says this page writes no new queue line.

**Review.** One read-only agent on Opus read the chapter's diff and this line of docs/06 against this page, docs/04 and chapters 13 and 14: no findings. One optional wording note, recorded under Decisions taken in /apply.

```commit
docs(ch11-blocking-fix): block only on a prerequisite fix in chapter 11

- Chapter 11: a fix found outside the page is a `[ ]` line; only a prerequisite makes the delivery wait
- English queue lines say what the Portuguese ones can hold

work/done/ch11-blocking-fix.md
```
