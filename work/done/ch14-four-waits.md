# ch14-four-waits

**Objective.** After chapter 14 a reader can name the four cases in which a line waits, the fourth a milestone review's code reading that missed part of its range, and write that line's suffixes, `· resume: apply` and a reason that says what was read; and the Portuguese example queue says what the English one says, within 74 columns; both editions.

**Decided without the author** (batch rule of this run: the recommended answer, no question asked).

1. *Where it is taught.* The mark table's `[?]` row, the sentence that counts the cases, a fourth bullet in "Waiting: `[?]`" (pt "Esperando: `[?]`") and key point 4. The opening ("mark a line that waits with its reason and the phase to resume") already covers the fourth case and stays (docs/05 §4, docs/03 `waiting mark`).
2. *The example is `m1-review`.* It is already the last line of the chapter's milestone, so the reader meets the line that can wait this way; the bullet shows only its suffixes, as the other bullets do. The example queue's marks and the board stay as they are: the free-lines paragraph and the three-column board depend on `m1-review` being `[ ]`; only two descriptions change (decision 10).
3. *The reason says what was read.* The kit's form is `· blocked: <what was read>` (docs/05 §8). The bullet's reason, `read all but catalog/`, says what was read in the fewest words: every area of chapter 15's Milestone review slot for the lending library but one, so the reader of chapter 15 meets the same areas.
4. *Why it waits, in the bullet.* One clause: a reader that read part of its area reports the same way as one that read it all, so only the paths read show the gap (chapter 15's sentence, said where the doubt is born, docs/04).
5. *How it leaves `[?]`.* No new sentence: the paragraph "A line leaves `[?]` when the reason is resolved" already says the person says so and a `resume: apply` line goes back to `[>]`, which holds for this case; `/apply m1-review` then reads what is missing.
6. *One forward pointer to chapter 15.* Chapter 14 has none today, and the milestone review's code reading is a term the reader has not been taught (docs/04 "Chapter pointers"); the bullet says what the reading is in a clause before pointing.
7. *Chapter 15's own waiting line stays.* Its "the review line waits as `[?]` with `· resume: apply` (chapter 14)" points here, where the reason is now taught; adding `· blocked: <what was read>` there is chapter 15's text, outside this line and outside `ch15-review-base`'s scope as the driver set it. Noted for the driver as a possible `[ ]` line.
8. *No docs/03 change.* The `waiting mark` row already says four cases, the fourth with its reason saying what was read (`kit-2026-10-18`).
10. *The Portuguese queue's width cuts (driver's decision, folded into this line).* Found by another propose: the Portuguese `emprestar-livro` row drops "um exemplar" ("a copy"), and the `meus-emprestimos` row says "o membro vê os dele" for "a member sees their loans". Both rows are restored to the English meaning within 74 columns, the slug column kept (it aligns on `meus-emprestimos`). `emprestar-livro` becomes "a bibliotecária empresta um exemplar ou a regra nega" (74 columns), and the English row is reworded to match, "the librarian lends a copy, or a rule refuses" (65), so both editions say the same: a copy is lent, or a rule refuses it. `meus-emprestimos` becomes "o membro vê seus empréstimos" (74 columns); the English row stays. Chapter 11's own `lend-book` row is a different queue and stays (docs/04 "Width of a block").
9. *Trunk; nothing staged by this definition; the driver sets docs/06's marks.* docs/05 §5 Git, and this batch's instructions.

**Behaviour.**

* Reading the table of six marks, a reader finds `[?]` set by any session "in the four cases below".
* Reading "Waiting: `[?]`", a reader finds four cases, the fourth: a milestone review's code reading that missed part of its range, with `m1-review` waiting as `· resume: apply · blocked: read all but catalog/`.
* A reader can say why that line waits: each reader lists the paths it read, a reader that read part of its area reports as one that read it all, and the line waits until the rest is read.
* A reader can say which phase it resumes: `apply`, since the review was being built, and that it goes back to `[>]` when the person says it is resolved, for `/apply m1-review` to read what is missing.
* Edge: a reader can tell this case from the third: nothing must be done first, no other line is named; the reason is the paths read, not `after <slug>`.
* Reading key point 4, a reader finds the four cases.
* Reading the example queue, a Portuguese reader finds `emprestar-livro` lending "um exemplar" or a rule refusing it, and `meus-emprestimos` saying a member sees their loans, as the English rows say; every row of both editions within 74 columns.
* The Portuguese edition reads the same in the same places, with the Contract's words and the lending library's Portuguese folders.
* Failure: "three cases" (pt "três casos") left anywhere in chapter 14, a mark of the example queue or the board changed, a row over 74 columns, the Portuguese queue saying less than the English, or one edition changed and not the other.

**Contract.**

* **Chapter 14, both editions** (`book/en/14-queue-states.md`, `book/pt/14-queue-states.md`), found by text:
  * the table row `| `[?]` | waiting | any session, in the three cases below |` becomes `| `[?]` | waiting | any session, in the four cases below |` (pt `| `[?]` | esperando | qualquer sessão, nos quatro casos abaixo |`).
  * "A line waits in three cases:" becomes "A line waits in four cases:" (pt "Uma linha espera em três casos:" becomes "Uma linha espera em quatro casos:").
  * after the third bullet ("**Another line must be done first, found after work started.** ...", pt "**Outra linha precisa ser feita antes, descoberto depois de o trabalho começar.** ..."), a fourth bullet, one line:
    "* **A milestone review's code reading missed part of its range.** The review that closes a milestone reads, on the person's word, every change since the milestone's base, split into areas with one reader each that lists the paths it read ([chapter 15](15-closing-a-milestone.md)), and a reader that read part of its area reports the same way as one that read it all, so when `m1-review`'s readers list no path of `src/features/catalog/`, the line waits with what was read as its reason: `· resume: apply · blocked: read all but catalog/`."
    (pt: "* **A leitura do código de uma revisão de marco não cobriu parte do seu intervalo.** A revisão que fecha um marco lê, com a palavra da pessoa, toda mudança desde a base do marco, dividida em áreas com um leitor cada que lista os caminhos que leu ([capítulo 15](15-closing-a-milestone.md)), e um leitor que leu parte da sua área aponta do mesmo jeito que um que a leu inteira, então quando os leitores de `m1-review` não listam nenhum caminho de `src/features/catalogo/`, a linha espera com o que foi lido como motivo: `· resume: apply · blocked: lidos todos menos catalogo/`.")
  * key point 4: "A line waits when the person says so, when an answer was asked and not given, or when work already started finds another line must be done first, with the phase ..." becomes "A line waits when the person says so, when an answer was asked and not given, when work already started finds another line must be done first, or when a milestone review's code reading missed part of its range, with the phase ..."; the rest of the bullet unchanged (pt "Uma linha espera quando a pessoa diz, quando uma resposta foi pedida e não veio, quando o trabalho já começado descobre que outra linha precisa ser feita antes, ou quando a leitura do código de uma revisão de marco não cobriu parte do seu intervalo, com a fase ...").
  * in the example queue after "This is the lending library's first milestone on one afternoon" (pt "Este é o primeiro marco da biblioteca em uma tarde"), two rows change, nothing else of the block:
    en `[*] lend-book       the librarian lends a copy, the rules may refuse` becomes `[*] lend-book       the librarian lends a copy, or a rule refuses`;
    pt `[*] emprestar-livro   a bibliotecária empresta, e as regras podem recusar` becomes `[*] emprestar-livro   a bibliotecária empresta um exemplar ou a regra nega`;
    pt `[ ] meus-emprestimos  o membro vê os dele · after emprestar-livro` becomes `[ ] meus-emprestimos  o membro vê seus empréstimos · after emprestar-livro`; the English `my-loans` row stays.
  Every other section of chapter 14 is unchanged, the other rows of the example queue, the board, the gain and the other key points included.
* **Portuguese words.** milestone review: `revisão de marco`; code reading: `leitura do código`; range: `intervalo`; base: `base`; reader: `leitor`; area: `área`; the person's word: `a palavra da pessoa`; waiting mark as chapter 14 writes it (`esperando`). The kit's suffixes and `m1-review` stay in English, as chapter 14 already writes them; the reason in words is translated, as its other reasons are.
* **Terms of docs/03.** `waiting mark`, `milestone review`, `resume` suffixes used as defined. No new term, no docs/03 change.
* **Sources.** None added or removed.
* **Cases.** No private case added; Case A's passage in "The problem" is unchanged. The example is the lending library's, in the milestone already said to be written for the chapter.
* **docs/06.** None from this page; the driver sets its line's marks.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Chapter 15's waiting line and its reason (decision 7): a possible separate line.
* The example queue's marks, its other rows and the board (decisions 2 and 10); chapter 11's queue rows.
* How the milestone review's readers work: chapter 15 teaches it; this chapter only points there.
* Chapter 8's report of the same migration: `ch08-update-2026-10-18`.

**Done when.**

* [x] Both editions written in the places the Contract names, the English first; parity green.
* [x] `grep -n -i "three cases" book/en/14-queue-states.md` and `grep -n -i "três casos" book/pt/14-queue-states.md` find nothing; "four cases" twice in English, "quatro casos" twice in Portuguese.
* [x] The three queue rows read as the Contract writes them; `check_width.py` green, the two Portuguese rows at 74 columns.
* [x] "Waiting: `[?]`" has four bullets in each edition; chapter 14 points to chapter 15 once.
* [x] Chapter 14 still opens with its value; no filler, nothing useful cut; still five key points.
* [x] The Portuguese uses the Contract's words and no synonym.
* [x] No em dash; `make verify` green (build, parity, em dash, prose, width, links, disclosure).
* [x] The Delivery review ran on this delivery's paths and the files it created (docs/05 §5), and the page records it.
* [x] The author's approval of an anonymized passage: inapplicable, no new Case A or Case B passage.
* [x] `make book` builds; the delivery ends with the paths of both PDFs for the author's review.
* [x] Page moved to `work/done/`, the line `[x]`, staged by explicit paths and this line's hunk of docs/06; the commit message suggested, `docs(ch14-four-waits): ...`.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure). "three cases" and "três casos" find nothing; "four cases" and "quatro casos" twice each. Queue rows: `lend-book` 65 columns, `emprestar-livro` and `meus-emprestimos` 74. Four bullets in each "Waiting" section, one pointer to chapter 15 per edition, five key points. `make book` builds:

* `output/one-page-at-a-time.pdf`
* `output/uma-pagina-de-cada-vez.pdf`

**Divergences.** None: every string is the Contract's.

**Delivery review** (docs/05 §5, one read-only agent on Opus, on both chapter diffs, this line of docs/06 and this page). Nothing breaks the page, docs/04 or this text: the strings match the Contract, both editions say the same, the Portuguese uses the Contract's words, chapter 15 lists `src/features/catalog/` (pt `catalogo/`) among the lending library's areas, and chapter 8's pointer to chapter 14 for the fourth case now holds. Two findings outside the Contract, each a `[ ]` line under M17, which `m17-review` now waits on too:

* `ch14-resume-moment`: the fourth bullet never says the review was being built when it stopped, so why it resumes by `apply` is left to the reader; the fix is a new string, outside this Contract. The review also judged the bullet dense (one sentence), correct as it stands.
* `ch15-waiting-reason`: decision 7, chapter 15's review line waits with `· resume: apply` and no reason.

**Decisions taken in /apply.** The two findings above became queue lines and not fixes, since each changes a string the Contract fixed or chapter 15's text.

```commit
docs(ch14-four-waits): a line waits in four cases in chapter 14

- add the fourth case: a milestone review's code reading that missed
  part of its range, m1-review waiting with what was read
- count four cases in the mark table, the section and key point 4
- give the Portuguese queue rows the English meaning, within 74 columns

work/done/ch14-four-waits.md
```
