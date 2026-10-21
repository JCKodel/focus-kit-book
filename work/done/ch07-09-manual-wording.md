# ch07-09-manual-wording

**Objective.** After chapters 7, 8 and 9 the reader knows a manual is named after what it does, as the kit's docs/05 says it today, with no rule on the language of its name, and the Portuguese reader meets one phrase for the manual of running the product owed by the first delivery after which a person can run it: "devido pela".

**Behaviour.**

* A reader of chapter 7's "Manuals" / "Manuais" reads that each action gets one file in `docs/manuals/`, named after what it does, so whoever needs it finds it by its name; the sentence no longer says the name is in the documentation language (en :102, pt :103; finding K1, P2 of `work/done/m23-review.md`).
* A Portuguese reader of chapter 7's "Um lugar para cada fato" reads that the kit's folders stay in English in every project and the files inside them do not: a manual has the name of what it does, as `docs/manuals/publicar-o-app.md` (pt :17; K1, P2).
* A Portuguese reader of chapter 9 reads `/brainstorm`'s fifth subject (pt :22) and "O que ele escreve, e onde para" (pt :62) naming the manual of running the product as "devido pela primeira entrega depois da qual uma pessoa consegue rodá-lo", the words chapter 8's update excerpt uses (pt :71), with no "a cargo da" (finding C5).
* A Portuguese reader who meets "devido" alone (pt 07:109, :173, :181; pt 09:122) or the verb "deve" (pt 07:99, :181) reads the same term as above, unchanged.
* Fails: a sentence in either edition that says a manual is named in the documentation language; a Portuguese sentence that names the delivery owing the manual with "a cargo da" or any phrase other than "devido pela"; one edition changed without the other where both say it.
* Edge: chapter 7 :16 in both editions ("the name after the number is in the documentation language", `00-Produto.md`) stays: it is about the numbered documents, and the kit's `references/documents.md` :5 still says it. Chapter 8 :52 ("the wording it proposes, in the project's documentation language") stays: it is about the update's migration text, not a manual's name.

**Contract.** English is the source (ADR-0004); line numbers as the files are now. Headings unchanged.

* `book/en/07-the-documents.md` :102:
  * now: "Each of these gets a manual, one file in `docs/manuals/`, named in the documentation language after what it does, so whoever needs it finds it by its name."
  * becomes: "Each of these gets a manual, one file in `docs/manuals/`, named after what it does, so whoever needs it finds it by its name."
* `book/pt/07-the-documents.md` :103:
  * now: "Cada uma dessas ações ganha um manual, um arquivo em `docs/manuals/`, com o nome na língua da documentação dizendo o que ele faz, para que quem precisa dele o encontre pelo nome."
  * becomes: "Cada uma dessas ações ganha um manual, um arquivo em `docs/manuals/`, com o nome do que ele faz, para que quem precisa dele o encontre pelo nome."
* `book/pt/07-the-documents.md` :17 (Portuguese only; the English edition has no such sentence, docs/04 asks it of the Portuguese edition alone):
  * now: "As pastas `docs/`, `docs/adr/`, `docs/manuals/`, `work/` e `work/done/` (onde fica a página de uma entrega feita) ficam em inglês em todo projeto, como o kit as escreve; os arquivos dentro delas levam a língua da documentação, como `docs/manuals/publicar-o-app.md`."
  * becomes: "As pastas `docs/`, `docs/adr/`, `docs/manuals/`, `work/` e `work/done/` (onde fica a página de uma entrega feita) ficam em inglês em todo projeto, como o kit as escreve; os arquivos dentro delas, não: um manual tem o nome do que faz, como `docs/manuals/publicar-o-app.md`."
* `book/pt/09-starting-a-project.md` :22, the manuals clause only:
  * now: "os manuais (o de rodar o produto, a cargo da primeira entrega depois da qual uma pessoa consegue rodá-lo; os outros nenhum ainda, em um projeto novo)"
  * becomes: "os manuais (o de rodar o produto, devido pela primeira entrega depois da qual uma pessoa consegue rodá-lo; os outros nenhum ainda, em um projeto novo)"
  * the rest of the sentence is left as it is.
* `book/pt/09-starting-a-project.md` :62:
  * now: "O slot Manuals (manuais) nomeia o manual de rodar o produto como devido, a cargo da primeira entrega depois da qual uma pessoa consegue rodá-lo, de instalar..."
  * becomes: "O slot Manuals (manuais) nomeia o manual de rodar o produto como devido pela primeira entrega depois da qual uma pessoa consegue rodá-lo, de instalar..."; the rest of the sentence unchanged, as en :62 ("as owed by the first delivery") says.
* Chapter 8: no change. pt :71 ("devido pela primeira entrega", inside a fenced block) is already the chosen phrase; en 08 and en 09 already say "owed by".
* Terms: `manual` as docs/03 has it (`docs/manuals/<what-it-does>.md`); "owed" / "devido" is not a docs/03 term and gets no row; the Portuguese phrase is fixed here, on this page.
* Sources: the kit's docs/05 §5 Manuals slot, "named after what it does" (this repository's docs/05 :250-251, installed from the kit; `.claude/skills/brainstorm/references/documents.md` :352-353), named in plain words as the kit's docs/05, as chapter 7 already does; no source note.
* Cases: none; no Case A or B, Ninjobs unchanged. Code examples: none.
* Neighbouring line on the same file: `ch09-slow-tests` (docs/06 :586) edits pt 09 :22 too, the verify clause at the start of the sentence, and comes after this line in queue order; it takes the sentence with the manuals clause above. No other line in flight or queued touches chapter 7; the `ch08-update-*` lines of M24 and later rewrite chapter 8's update example, which this delivery leaves untouched.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.**

* Chapter 7 :16 and chapter 8 :52 in both editions: true as written (Behaviour, Edge).
* The other uses of "devido" and "deve" (pt 07:99, :109, :173, :181; pt 09:122): already the chosen term.
* A docs/03 row for "owed": not a domain term; the phrase lives on this page.
* `work/done/pt-placeholders.md`, whose sentence pt 07:17 changes: the record says what it wrote then and stays as it is.
* `work/done/m23-review.md`: its row C5 cites pt 07:99 as one of the variants; today :99 says "todo projeto o deve", the chosen term, so nothing there changes and the record stays.

**Done when.**

* [x] The five lines changed as the Contract says, chapter 7 in both editions and pt 09; same headings; each chapter still opens with its value; no filler and nothing useful cut.
* [x] `grep -n "língua da documentação" book/pt/07-the-documents.md` prints only :16 and :46; `grep -n "documentation language" book/en/07-the-documents.md` prints only :16 and :45.
* [x] `grep -n "a cargo da" book/pt/0[789]-*.md` prints nothing.
* [x] No numbers, no history of the kit, no run narrated; no em dash.
* [x] `make verify` green; `make book` built both PDFs: the batch's driver ran it after the last M23 fix lane, at `16fdca6` (exit 0), and `work/done/m24-review.md` records the build at `2fccad2`, whose chapters 7 and 9 are the same, with both PDF paths.
* [x] Delivery review by one read-only Opus agent this lane launched, over the three chapter files against this page and docs/04 (Delivery review); whether it kept the session's advisor, as docs/05 §5 asks, is not recorded.
* [x] Page in `work/done/`, the commit suggested in a `commit` block; the line's `[x]` and the staging by paths and hunk are the driver's steps.

**Decisions taken from the documents.**

* "Named after what it does", with no language: the kit's docs/05 §5 Manuals slot as installed (docs/05 :250-251) and docs/03's `manual` row.
* Chapter 7 :16 stays: the kit's `references/documents.md` :5 still puts the numbered documents' names in the documentation language.

**Decisions taken alone.**

* The phrase is "devido pela", not "a cargo da": "devido" is already the word at five of the seven places (pt 07:109, :173, :181; pt 08:71; pt 09:122), "devido por" is idiomatic Portuguese for owed by ("o valor devido pelo cliente"), and pt 08:71 sits inside a fenced block of the update excerpt, which the M24-and-later `ch08-update-*` lines rewrite; standardizing on it changes only two prose lines of chapter 9. No kit wording decides it: the kit's README.pt.md fixed "o manual de rodá-lo" (`work/done/ch13-apply-run-manual.md` :18), not the verb.
* pt 07:17 keeps its purpose, telling the Portuguese reader once that the kit's folders stay in English, and its example; only the claim that the files inside take the documentation language goes, replaced by the manual's naming rule. The example stays in Portuguese because the Portuguese edition's example names are Portuguese (docs/04).
* Chapter 8 and the English chapter 9 need no change; the queue line's wording could say "chapters 7 and 9", left to the driver.

**Divergences.** None: the five lines are the Contract's.

**Proof.** The three Done-when greps print what they say (pt 07 :16 and :46; en 07 :16 and :45; no "a cargo da" in pt 07 to 09); `make verify` green after the last edit; `make book` run by the batch's driver at `16fdca6` (exit 0), and `work/done/m24-review.md` records the build at `2fccad2`, the same chapters 7 and 9, with both PDF paths.

**Delivery review:** a read-only Opus agent, launched by this lane, over the three chapter files against this page and docs/04: no findings; one stylistic note (pt 07:17 "tem o nome do que faz" beside pt 07:103 "com o nome do que ele faz"), both correct, no change.

```commit
docs(ch07-09-manual-wording): name a manual after what it does

- en/pt 07: a manual is named after what it does, no language rule
- pt 07: the files inside the kit's folders do not stay in English
- pt 09: the run manual is "devido pela" first delivery, as ch 8 says

work/done/ch07-09-manual-wording.md
```
