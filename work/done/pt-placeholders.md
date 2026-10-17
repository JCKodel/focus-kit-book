# pt-placeholders

**Objective.** A reader of the Portuguese edition reads every placeholder and folder a chapter wrote in Portuguese, learns once, where the kit's folders and `features/` first appear, that those names stay in English and why, and reads the imperative of a commit subject explained with chapter 13's own commit, "Emprestar um exemplar a um membro". Found by `m15-review` (work/done/m15-review.md: A16, B18, B19, B20: "English placeholders or folders with no note, and pt 13:176 explaining the imperative with the English subject").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one. Review these first.

1. What is translated: a placeholder is a description the reader replaces and never types, so one a chapter wrote is in the reader's language, as pt 19 already does (`<oculta>`, `<prefixo>`, `<os caminhos dela>`) and as docs/04 asks of every name the code invents, comments included; a folder a chapter invents for its example is translated the same way (`guide/` becomes `guia/`, next to `guia-do-administrador` in the same block). What the reader types or finds in a file stays: the kit's folders and suffixes, `features/`, commands and their output. Source: docs/04 (Portuguese edition's code); pt 19:170, 267; pt 21.
2. "Every placeholder" reaches past the four findings to the two other English-word placeholders in the Portuguese edition: `· blocked: <reason>` (pt 14:79) becomes `<motivo>`, and `git switch -c <name>` (pt 18:64) becomes `<nome>`; leaving them would teach the rule in four chapters and break it in two. Placeholders whose word the Portuguese edition already uses as its own stay: `<slug>`, `<commit>`, `<merge>`, `<hash>`, `<url>`, `<base>` (pt prose says "o slug" and "o commit" throughout, and pt 15:20 writes "que é o `<base>`"). Source: docs/06 (this line: "every placeholder"); pt 11, 18.
3. `<milestone>-review` (pt 11:87, 15:16, 15:110) stays: it is docs/03's own form for the milestone review and docs/05 §8's, written by the kit, and the queue shows it as `m1-review`. Its first appearance, pt 11:87, says so in a clause: it stays in English as the kit writes it, `m1-review` for the first milestone. pt 15 keeps it without a second note. Source: docs/03 `milestone review` row; docs/05 §8; pt 11:57.
4. The mood of the subject: the Portuguese subjects the book writes for its chapters are infinitives ("Mostrar a data de devolução como dia/mês/ano", pt 11; "Emprestar um exemplar a um membro", pt 13), which is how Portuguese gives an instruction; calling "Emprestar" an imperative would be wrong Portuguese. So pt 13 says the subject is "no infinitivo, como uma ordem", with the chapter's own subject against "Emprestou" and "Emprestando", the same verb in the forms that match the English "Lent" and "Lending", and the template's placeholder agrees. The meaning is the English one, a command form; docs/05 §6's "imperative" is the kit's English. Source: docs/05 §6; pt 11, 13 commit blocks; ADR-0004 (the Portuguese means what the English means).
5. Where the kit's English names are noted: once each, where the reader first meets them, not in every chapter. The kit's folders (`docs/`, `docs/adr/`, `docs/manuals/`, `work/`, `work/done/`) in pt 7:16, the sentence that already says the documents' numbers are fixed and their names follow the documentation language; `features/` in pt 4, under the folder tree where the vertical slice is taught (its passing use in a path in pt 3:98 comes first but teaches nothing about the folder). This is what docs/04 asks ("the text says so where such a name appears") and what `slice-paths` left to this line (work/done/slice-paths.md, Decided 4). The queue suffixes are already noted (pt 11:22, pt 14:29). Source: docs/04; docs/03 `feature` and `vertical slice` rows; work/done/slice-paths.md.
6. git's own message in pt 19:226, `leftover conflict marker`, stays in English with no note: it is a command's output, which docs/04 keeps as it is, and the sentence around it already says what it reports. Only `<file>` and `<line>` become `<arquivo>` and `<linha>`. Source: docs/04 ("Commands and their output stay as they are").
7. The English edition does not change: it is the source and already writes its placeholders in its language; the notes on names that stay in English exist only in the Portuguese edition, as pt 11:22, pt 14:29 and pt 22:88 already do. Source: ADR-0004; pt 11, 14, 22.
8. docs/04 owns the Portuguese edition's naming rule, so it gains the placeholder rule in the same delivery (AGENTS.md: documents are living). No docs/03 term (`slug`, `marco`, `feature` are already the edition's words), no new queue line, no split: about a dozen passages in eight Portuguese chapters and one sentence of docs/04 fit one page. The queue line's "(chapters 11, 13, 19, 21)" names the findings' chapters; the driver may extend it to the eight this page touches (4, 7, 11, 13, 14, 18, 19, 21). Source: AGENTS.md; docs/03; docs/05 §1; docs/06.

**Behaviour.**

Passages are found by their words; line numbers are as of the working tree on 2026-10-17, after `code-width` (38f60db) and `pt-fixed-terms`. The proposed text is what /apply writes unless a better wording keeps the meaning, docs/03's words and, inside a code block, 74 columns.

* A reader of pt 11 §A linha reads the line's form as `[ ] <slug>  <o que ela entrega, uma frase> · after <slug>` (57 columns; was `<what it delivers, one sentence>`), with the slug column as it is.
* A reader of pt 11:87 reads: "Um marco é planejado com a sua revisão como a última linha, `<milestone>-review` (em inglês, como o kit a escreve: `m1-review` para o primeiro marco), uma entrega como as outras, que pega o parágrafo cláusula por cláusula ([capítulo 15](15-closing-a-milestone.md))." (Decided 3).
* A reader of pt 13 §A mensagem reads the format block as:
  * `<assunto no infinitivo, até 72 caracteres>` (42 columns);
  * `- <um destaque, uma linha>` (26);
  * `- <até cinco deles>` (19);
  * `work/done/<slug>.md`, unchanged.
* A reader of pt 13:176 reads: "O assunto diz o que a entrega faz no infinitivo, como uma ordem, "Emprestar um exemplar a um membro" e não "Emprestou" nem "Emprestando", com um escopo entre parênteses quando ajuda." (Decided 4).
* A reader of pt 14:79 reads `· blocked: <motivo>`; `· blocked: after <slug>, <slug>` stays.
* A reader of pt 18:64 reads `git switch -c <nome>`.
* A reader of pt 19 reads `<arquivo>:<linha>: leftover conflict marker` (19:226), `git reset --hard <o commit antes do merge>` (19:229) and `git commit -- <caminhos>` (19:266).
* A reader of pt 21's page `guia-do-bibliotecario` reads, in its Contract, "Markdown em guia/, e um PDF gerado a partir dele." (49 columns).
* A reader of pt 7, right after 7:16 (the documents' numbers fixed, their names in the documentation language), reads one new sentence: "As pastas, `docs/`, `docs/adr/`, `docs/manuals/`, `work/` e, dentro dela, `work/done/`, para a página de uma entrega feita, ficam em inglês em todo projeto, como o kit as escreve; os arquivos dentro delas levam a língua da documentação, como `docs/manuals/publicar-o-app.md`."
* A reader of pt 4, after the paragraph that explains the files of `src/features/emprestimos/` (4:50), reads one new sentence: "A pasta `features/` fica em inglês, como o kit a escreve e como este livro diz *feature*; cada fatia dentro dela tem um nome da biblioteca de empréstimos, `emprestimos/`, `membros/`, `catalogo/`."
* docs/04's Portuguese-edition rule (the paragraph that begins "Since `author-review-1`") also says: a placeholder a chapter writes (`<o que ela entrega, uma frase>`) is translated; the kit's own names (`docs/adr/`, `docs/manuals/`, `work/`, `work/done/`, the queue's suffixes, `<milestone>-review`) and `features/` stay, and the Portuguese edition says so once, where the reader first meets them (chapters 4, 7, 11, 14).
* Edge: the English edition reads the same before and after; parity holds, since no heading, heading level or note key changes.
* Edge: every code-block row this page changes measures 74 columns or fewer (widths above), so `scripts/check_width.py` passes.
* Edge: pt 19's already Portuguese placeholders (`<oculta>`, `<prefixo>`, `<os caminhos dela>`) and every `<slug>` stay as they are.
* Fails: a Portuguese chapter still showing `<what it delivers`, `<subject in the imperative`, `<a highlight`, `<up to five`, `<reason>`, `<name>`, `<file>:<line>`, `<the commit before the merge>`, `<paths>` or `guide/`; pt 13 explaining the subject with an English example or calling "Emprestar" an imperative; a note on English names repeated in a chapter after its first; `leftover conflict marker` translated; a changed row past 74 columns.

**Contract.**

The findings were re-checked against the tree: each holds as quoted in m15-review; the sweep for English-word placeholders found two more (Decided 2).

* **Portuguese edition only**, file names, titles and heading levels kept: `book/pt/04-focus.md`, `07-the-documents.md`, `11-queue-and-milestones.md`, `13-apply.md`, `14-queue-states.md`, `18-git-essentials.md`, `19-worktrees.md`, `21-beyond-software.md`; the passages of Behaviour, nothing else. Two sentences are added (pt 4, pt 7), one clause (pt 11:87).
* **Code blocks changed**, with their width: pt 11 line form (57); pt 13 message format (42, 26, 19); pt 21 page Contract row (49).
* **English edition:** unchanged (Decided 7).
* **docs/04:** the Portuguese edition's naming paragraph adds the placeholder rule and where the kit's English names are noted, as Behaviour says. No other document changes.
* **Terms of docs/03** used, none added: `milestone` / `marco`, `milestone review` (`<milestone>-review`), `feature`, `vertical slice`, `queue line`. docs/03 unchanged.
* **Sources:** none added or removed.
* **Cases:** none touched.
* **Queue:** no new line. The driver may extend this line's chapter list to the eight files above (Decided 8).

**Overlap with the lines in flight (docs/06).** /apply finds passages by their words; when another session's unstaged edit sits in a hunk this delivery would stage, it stages by hunk or stops and reports per docs/05 §4 and §6.

* `pt-fixed-terms` changed pt 14:77 and 14:85, around this page's 14:79, and pt 11 and 13 elsewhere; it is applied before this line.
* `pt-skeleton-first` (pt 11's queue block at about 11:51) and `ch04-parnas` (pt 4:58-59): same files, other passages.
* `ch13-delivery-review` (chapter 13), `ch18-log-evidence` (chapter 18's log), `ch19-when-worktrees-pay` and `batch-propose` (chapter 19, the key points at 19:266-267 likely), `ch21-counts-once` (chapter 21 at 59-87): same files; pt 19:266 sits next to 19:267, so run this line and `ch19-when-worktrees-pay` one after the other.

**Out of scope.**

* `<slug>`, `<commit>`, `<merge>`, `<hash>`, `<url>`, `<base>`: words the Portuguese edition uses as its own (Decided 2).
* `<milestone>-review` in pt 15:16, 15:110 and the slot text `Milestone review: /code-review ultra <base>` (pt 8:75, 15:53): docs/03's and the kit's forms; the slot is already glossed in pt 15:20 (Decided 3).
* A note at every later use of `work/done/` or `features/` (pt 3:98, 10, 11, 13, 14, 19): one note, at the first meeting (Decided 5).
* pt 13's bullets in the third person ("Cria", "Empresta"): docs/05 §6 sets the mood of the subject only, and no finding names them.
* git-flow branch prefixes (`feature/`, `hotfix/`, `release/`, pt 18:157) and the layer folders (`controllers/`, `models/`, pt 4:11): conventions of other tools the chapters quote, not names they wrote.
* `leftover conflict marker`: git's output (Decided 6).

**Done when.**

* [x] The eight Portuguese chapters changed as Behaviour says, same heading levels; the English edition untouched; each chapter still opens with its value; no filler and nothing useful cut.
* [x] `grep -n -E "<what it delivers|<subject in|<a highlight|<up to five|<reason>|<name>|<file>|<line>|<the commit before|<paths>|guide/" book/pt/*.md` prints only pt 5's Vitest note URL (`vitest.dev/guide/`).
* [x] `grep -n -E "<o que ela entrega|<assunto no infinitivo|<motivo>|<nome>|<arquivo>:<linha>|<o commit antes do merge>|<caminhos>|em guia/|Emprestar um exemplar a um membro\" e não|ficam em inglês em todo projeto|A pasta \`features/\` fica em inglês|em inglês, como o kit a escreve: .m1-review" book/pt/*.md` prints the passages of Behaviour, each once.
* [x] docs/04 holds the placeholder rule as Behaviour says.
* [x] `python3 scripts/check_width.py` prints nothing.
* [x] Both editions checked; no em dash; no narrated run; nothing private.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Proof.**

* Both Done when greps run as written: the first prints only pt 5:159's Vitest note URL (`vitest.dev/guide/`); the second prints pt 4:56, 7:17, 11:19, 11:87, 13:168, 13:176, 14:79, 18:64, 19:226, 19:229, 19:266 and 21:41, each once.
* Widths, in characters: pt 11 line form 57; pt 13 format rows 42, 26, 19; pt 21 Contract row 49. `scripts/check_width.py` green inside `make verify`.
* `git diff --stat -- book/en` is empty.
* `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Decisions in /apply.**

* The queue line's chapter list became the eight chapters this page touches, "(chapters 4, 7, 11, 13, 14, 18, 19, 21)", as Decided 8 allowed.
* pt 4's sentence on `features/` closes the paragraph that explains the files of `src/features/emprestimos/` (now 4:56), before "A pasta de cima grita a biblioteca", which Parnas's line (`ch04-parnas`) follows.

**Divergences.** Five, from the review, all in this delivery's lines, each keeping the meaning and the Done when greps:

* pt 13:176 keeps the comma before "no infinitivo", as the English does before "in the imperative"; without it "faz no infinitivo" read as if the delivery acted in the infinitive.
* pt 7:17 names the folders without four commas before the verb: "As pastas `docs/`, `docs/adr/`, `docs/manuals/`, `work/` e `work/done/` (onde fica a página de uma entrega feita) ficam em inglês em todo projeto".
* pt 4:56 reads "assim como este livro diz *feature*, sem traduzir" and "cada fatia dentro dela tem um nome em português, da biblioteca de empréstimos:", so the name is not read as one that belongs to the library.
* docs/04's earlier clause on names that stay now names chapter 4's `features/` beside chapter 22's log fields, and the list of the kit's own names starts with `docs/`, which pt 7 notes.

**Review.**

A read-only Opus agent read the staged diff of these paths and docs/06's line against this page, docs/03, docs/04 and the English edition. It confirmed the Proof, the widths, the English edition unchanged, no English placeholder left in book/pt, no em dash, nothing private, and each passage meaning what the English means. Findings: the three wordings and the two docs/04 points fixed as Divergences say; pt 7:17's example `docs/manuals/publicar-o-app.md` comes before 7:83 introduces that manual, left as a harmless forward example. No new queue line.

```commit
docs(pt-placeholders): write the pt edition's placeholders in Portuguese

- translate the placeholders and guia/ in pt 11, 13, 14, 18, 19, 21
- explain the subject's mood with "Emprestar um exemplar a um membro"
- note once that the kit's folders and features/ stay (pt 4, 7, 11)
- docs/04 gains the placeholder rule for the Portuguese edition

work/done/pt-placeholders.md
```
