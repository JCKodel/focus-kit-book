# case-a-board-once

**Objective.** A reader learns the kanban board, the fold of the six marks onto three columns and Case A's `[?]` story once, in chapter 14, and meets them in chapter 16 only as the governor's example of an error that let a step in, and in chapter 20 only as what the board mirror places, each with a pointer to chapter 14, in both editions. Found by `m15-review` (work/done/m15-review.md, B6 and B7: "20:51-85 and 16:55, 69: the kanban board, the fold onto three columns and Case A's `[?]`, owned by 14. Seen.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. Who owns what. Chapter 14 owns the board as a reading of the queue, the fold and the `[?]` story: its opening promises all three, §The problem tells the story, §The queue as a kanban board gives the definition and the fold, and its line "Chapter 20 shows how a script mirrors the queue to a team's own board, one way." hands the mirror on. Chapter 20 owns the board mirror (docs/03 `board mirror`) and question deliveries (docs/03 `question delivery`; chapter 21 §58 points to chapter 20 for them). Chapter 16 owns the governor's example: an error that happened let a step in. Source: m15-review B6, B7; chapter 14; docs/03; AGENTS.md (a rule or story said once in the chapter that owns it).
2. Chapter 16 keeps the error and drops the story's detail: the count "five" (chapter 14's counted number), "kanban", the mark's definition ("for a line waiting on a person") and "gives the six marks that answer that error for every team" go; what stays is that waiting lines read as idle work on Case A's board and that this error let `[?]` in, with the existing link to chapter 14 inside the sentence. Keeping "five" was the alternative; it is chapter 14's number, and the governor's point holds without it. Source: chapter 16 §The error that earned a mark, line "The question is asked in each project, and the governor decides there, with an error that project met."; docs/04 §Chapter pointers.
3. Chapter 16 keeps the gloss "a client project on a low-code platform": the book glosses Case A at its first use in each chapter (chapters 11, 14, 16, 17, 20, 21, 23), for the reader who skips (docs/00 §Audience). Source: the chapters; docs/00 line 27.
4. Chapter 16's key point keeps the governor's claim, a project decides with its own error, and drops "the kit's six marks answer the same error for every team that reads its queue as a board", chapter 14's content. Source: docs/04 **One gain** (a key point says what the reader does).
5. Chapter 20 §Boards: the board's definition ("A kanban board shows work as cards in columns ...") is cut, since it repeats chapter 14 for a reader in order and the next sentences already say "board" and, two lines down, "kanban board"; the two sentences on why a board moved by hand drifts stay, they are chapter 20's problem. Source: docs/04 §Chapter pointers (a pointer back that only repeats is cut).
6. Chapter 20 §Boards: the fold sentence is replaced by one that says what the mirror does with each card and points to chapter 14 for where it goes; no column names, no `[?]` tagging. It is not a sentence that is only a pointer: it says the mirror places every card by its mark. Source: docs/04 §Chapter pointers and §Teach, do not only show.
7. Chapter 20 §A mark for waiting: its first sentence (Case A's `[?]` and the kit's own) goes. What remains is about question deliveries, so the H3 is renamed "Question deliveries" / "Entregas de pergunta", same level in both editions, and its one sentence is rewritten to stand alone. Dropping the H3 and closing §Boards with the sentence was the alternative; the heading keeps the docs/03 term findable for chapter 21's pointer, and docs/04's chapter shape allows an H3 inside an H2. Source: docs/03 `question delivery`; docs/04 §Chapter shape; chapter 21; `check_parity.py` (heading levels).
8. Chapter 20's key point on `[?]` keeps only the question-delivery half, said as what the reader does; no pointer to chapter 14 there, the section carries it. Source: docs/04 **One gain**.
9. Pointer form: chapter 16 keeps its existing link `[chapter 14](14-queue-states.md)`; chapter 20's link moves from the cut `[?]` sentence to the new mirror sentence, so the chapter still holds one link to chapter 14 (plus its existing plain "(chapter 14)" in the pull request list, untouched). Source: chapters 16 and 20; docs/04 §Chapter pointers names no form.
10. Chapter 20's mirror passage (the script and pipeline, refresh on every mark change, never silent, why one way) and its gain sentence on Case A's board stay: they are chapter 20's own, and the finding names the board, the fold and `[?]`, not the mirror. Source: m15-review B6; docs/03 `board mirror`.
11. No docs/03 term (`board mirror`, `waiting mark`, `question delivery` exist), no new queue line, no split: two chapters, a few sentences each, one page. Source: docs/03; docs/05 §1.
12. OD-3 is not waived by the batch: every rewritten Case A sentence is on this page verbatim for the author's approval before the delivery is done. Source: docs/00 OD-3; docs/05 §3 and §5.

**Behaviour.**

Text is found by its words; line numbers are as of the working tree when this page was written (pt in parentheses).

* Chapter 16 §The error that earned a mark: the sentence beginning "On Case A, a client project on a low-code platform, five lines waiting" (en 55, pt 55) becomes: "On Case A, a client project on a low-code platform, lines waiting on the client's answers read as idle work on its board, and that error is what let in the mark the project added by hand, `[?]` ([chapter 14](14-queue-states.md) tells the story)." ("No Caso A, um projeto para um cliente em uma plataforma low-code, linhas esperando as respostas do cliente pareciam trabalho parado no seu quadro, e foi esse erro que deixou entrar a marca que o projeto acrescentou à mão, `[?]` (o [capítulo 14](14-queue-states.md) conta a história).") The sentence before it stays.
* Chapter 16 §Key points: the bullet beginning "The governor decides in each project" (en 69, pt 69) becomes: "The governor decides in each project, with an error that project met: Case A's `[?]` entered because waiting lines read as idle work." ("O regulador decide em cada projeto, com um erro que aquele projeto encontrou: o `[?]` do Caso A entrou porque linhas em espera pareciam trabalho parado.")
* Chapter 20 §Boards: the sentence "A kanban board shows work as cards in columns, one column per stage, ..." ("Um quadro kanban mostra o trabalho como cartões em colunas, uma coluna por etapa, ...") (en 51, pt 51) is deleted; the section opens on "A manager opens a board; they rarely open a repository." unchanged.
* Chapter 20 §Boards: the sentence beginning "With the six marks of chapter 14, a mirror folds them" ("Com as seis marcas do capítulo 14, um espelho as dobra") (en 58, pt 58) becomes: "Each card goes to the column where [chapter 14](14-queue-states.md)'s fold of the six marks puts it." ("Cada cartão vai para a coluna em que a dobra das seis marcas do [capítulo 14](14-queue-states.md) o põe.") The sentences before and after it stay.
* Chapter 20: the H3 "### A mark for waiting" ("### Uma marca para a espera") becomes "### Question deliveries" ("### Entregas de pergunta"); its two sentences become: "Case A recorded one more customization: question deliveries, whose only output is a written answer from someone outside the project. They close on the answer, not on the send, because a session once marked one done when the email went out." ("O Caso A registrou mais uma customização: as entregas de pergunta, cujo único resultado é uma resposta escrita de alguém de fora do projeto. Elas fecham na resposta, não no envio, porque uma sessão certa vez marcou uma delas como concluída quando o email saiu."), one sentence per line.
* Chapter 20 §Key points: the bullet beginning "`[?]` was Case A's mark" ("`[?]` foi a marca do Caso A") (en 85, pt 85) becomes: "A question delivery, Case A's own customization, closes on the answer, not on the send." ("Uma entrega de pergunta, customização do próprio Caso A, fecha na resposta, não no envio.")
* /apply may polish these sentences within these limits: same claims, no number, no column name, no definition of the board or of `[?]` outside chapter 14, the pointer inside a sentence that says something.
* Checked, both editions:
  * `grep -rln "To Do\|A fazer\|three columns\|três colunas" book/en book/pt` lists only `book/en/14-queue-states.md` and `book/pt/14-queue-states.md`.
  * `grep -n -i "five\|cinco\|kanban" book/en/16-the-governor.md book/pt/16-the-governor.md` finds nothing.
  * `grep -n "cards in columns\|cartões em colunas\|added a mark by hand\|acrescentou uma marca à mão\|A mark for waiting\|marca para a espera" book/en/20-team-tools.md book/pt/20-team-tools.md` finds nothing.
  * `grep -c "14-queue-states.md" book/en/16-the-governor.md book/pt/16-the-governor.md book/en/20-team-tools.md book/pt/20-team-tools.md` gives 1 for each file.
  * Chapter 14, both editions, unchanged; chapter 21's pointer to chapter 20 for question deliveries still lands on a section that holds them.
* Fails: one edition changed and not the other; heading levels differing between editions; chapter 16 losing that an error Case A met let `[?]` in; chapter 20 losing the mirror, its refresh, its silence rule, why it goes one way, or question deliveries; any column name, the count "five", or a definition of the board left in chapters 16 or 20; a pointer that stands as a sentence of its own; any edit to chapter 14.

**Contract.**

* Files: `book/en/16-the-governor.md`, `book/pt/16-the-governor.md`, `book/en/20-team-tools.md`, `book/pt/20-team-tools.md`; no other file.
* Sections: chapter 16 §The error that earned a mark (one sentence) and §Key points (one bullet); chapter 20 §Boards (one sentence deleted, one rewritten), its H3 renamed with its body rewritten, and §Key points (one bullet). Heading count and levels unchanged in both editions.
* Terms of docs/03: none new; `board mirror`, `waiting mark`, `question delivery` used as defined. Sources: none added or removed; chapter 14's Toyota and Azure notes stay there. Cases: Case A only, in the sentences quoted in Behaviour, for the author's OD-3 approval. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line `[>]` by the driver, `[*]` when /apply starts, `[x]` by /apply. No new queue line.
* For the driver and the author, not for /apply to edit unasked: `pt-fixed-terms` (`[ ]`) carries B15, "pt 14:104-115 against pt 20:58: one fold, two sets of column names". This delivery removes the fold from pt chapter 20, so B15's chapter-20 half is gone; if this line lands first, `pt-fixed-terms`'s /propose should check that only chapter 14's column names remain and drop "board columns" from its scope if nothing else needs it.
* Gains untouched: chapters 16 and 20 keep their gain sections; chapter 20's "Case A's board ran on one project, and its write permission was never proven." stays.

**Deliveries in flight on the same chapters.**

* `free-line-gloss` (done, staged): chapters 7 and 18; no file in common.
* `line-rule-once` (page written): chapters 13 and 22; no file in common.
* `pt-fixed-terms` (`[ ]`): pt chapters 16 and 20 among others, for term choices; see the Contract. Find passages by their words, not by line numbers.

**Out of scope.**

* Chapter 14: the owner, as it stands.
* Chapter 20's board mirror passage and gain: chapter 20's own, not the finding.
* Case A's gloss in chapters 16 and 20: the book's pattern for each chapter's first use.
* pt column and term choices: `pt-fixed-terms`.

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the results it names.
* [x] Chapters 16 and 20 still open with their value, keep their gain, no filler and nothing useful cut.
* [x] Every number still sourced; `make verify` green, parity and disclosure scan included; no em dash.
* [x] The author approves the anonymized Case A sentences quoted in Behaviour, both editions (docs/00 OD-3): pending: the author's reading at the end of the batch. The passages are listed under Case A passages.
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Divergences.**

* Chapter 20 §Boards, the mirror sentence, polished within the Behaviour's limits: en "With the kit's six marks, a mirror places each card by its line's mark, in the column where [chapter 14](14-queue-states.md) folds them onto a board's columns."; pt "Com as seis marcas do kit, um espelho coloca cada cartão pela marca da sua linha, na coluna em que o [capítulo 14](14-queue-states.md) as dobra nas colunas de um quadro." The page's draft named no actor; the sentence now says a mirror does the placing, as decision 6 asks, and, after the review, opens on the kit's six marks so it does not read as Case A's own mirror (Case A mapped its own marks, chapter 14) and does not fix the board at three columns. pt uses the verb "dobra", as chapter 14 does. Same claim, no column name, the pointer inside it.

**Omissions.** None.

**Case A passages, for the author's approval (docs/00 OD-3).** Pending: the author's reading at the end of the batch. `make scan` green.

* en 16:55: "On Case A, a client project on a low-code platform, lines waiting on the client's answers read as idle work on its board, and that error is what let in the mark the project added by hand, `[?]` ([chapter 14](14-queue-states.md) tells the story)."
* pt 16:55: "No Caso A, um projeto para um cliente em uma plataforma low-code, linhas esperando as respostas do cliente pareciam trabalho parado no seu quadro, e foi esse erro que deixou entrar a marca que o projeto acrescentou à mão, `[?]` (o [capítulo 14](14-queue-states.md) conta a história)."
* en 16:69: "The governor decides in each project, with an error that project met: Case A's `[?]` entered because waiting lines read as idle work."
* pt 16:69: "O regulador decide em cada projeto, com um erro que aquele projeto encontrou: o `[?]` do Caso A entrou porque linhas em espera pareciam trabalho parado."
* en 20:57: "With the kit's six marks, a mirror places each card by its line's mark, in the column where [chapter 14](14-queue-states.md) folds them onto a board's columns." (in Case A's mirror passage)
* pt 20:57: "Com as seis marcas do kit, um espelho coloca cada cartão pela marca da sua linha, na coluna em que o [capítulo 14](14-queue-states.md) as dobra nas colunas de um quadro."
* en 20:60, 62-63: "### Question deliveries" / "Case A recorded one more customization: question deliveries, whose only output is a written answer from someone outside the project." / "They close on the answer, not on the send, because a session once marked one done when the email went out."
* pt 20:60, 62-63: "### Entregas de pergunta" / "O Caso A registrou mais uma customização: as entregas de pergunta, cujo único resultado é uma resposta escrita de alguém de fora do projeto." / "Elas fecham na resposta, não no envio, porque uma sessão certa vez marcou uma delas como concluída quando o email saiu."
* en 20:84: "A question delivery, Case A's own customization, closes on the answer, not on the send."
* pt 20:84: "Uma entrega de pergunta, customização do próprio Caso A, fecha na resposta, não no envio."

**Proof.**

* `grep -rln "To Do\|A fazer\|three columns\|três colunas" book/en book/pt` lists only `book/en/14-queue-states.md` and `book/pt/14-queue-states.md`.
* The `five|cinco|kanban` grep on chapter 16 and the `cards in columns|...|marca para a espera` grep on chapter 20 find nothing, both editions.
* `grep -c "14-queue-states.md"` gives 1 for chapters 16 and 20 in each edition; chapter 14 has no diff; chapter 21:58 still points to chapter 20, whose H3 "Question deliveries" holds them.
* `make verify` green (build, parity, em dash, prose, links, disclosure); `make scan` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Review.** A read-only Opus agent read the staged diff and this line's hunk of docs/06 against this page and docs/04.

* Case A passages gave the chapter 20 H3 as lines 60-62: fixed to 60, 62-63.
* Chapter 20:57, both editions, could read as Case A's mirror using the kit's six-mark fold, and implied every board has the fold's columns: fixed (Divergences).
* Chapter 20:84 states a fact, not what the reader does, as decision 8 says: accepted. Every key point of chapter 20 states a fact, and the bullet still holds one gain; decision 8 stays as the batch recorded it.
* The H3 "Question deliveries" sits under §Boards: accepted as decision 7 decided; "one more customization" ties it to Case A's mirror before it.
* Parity, greps, chapter 16, chapter 21's pointer, disclosure, commit format: no findings.

```commit
docs(case-a-board-once): leave the board and its [?] story to chapter 14

- chapter 16 keeps that a waiting error let Case A's [?] in, pointing to chapter 14
- chapter 20 drops the board's definition, the fold and the [?] story; the mirror places cards by chapter 14's fold
- chapter 20's waiting H3 becomes Question deliveries
- both editions

work/done/case-a-board-once.md
```
