# ch13-created-files

**Objective.** After chapter 13 a reader can say what the delivery review reads, the `git diff` of the delivery's paths and also the files the delivery created, which are untracked while the review runs and so in no diff, and why: on `lend-book`, whose code is all new, a review of the diff alone would have read none of it; both editions.

**Decided without the author** (batch rule of this run: the recommended answer, no question asked).

1. *Where it is taught.* In "The delivery review" (pt "A revisão da entrega"), the paragraph on what the review reads, and in `lend-book`'s review, the example that proves it. The opening, the gain and the key points stay: the opening says "a review by a context that did not write the change", the gain "a fault a delivery wrote is found by a reader that did not write it", and both already hold for created files (docs/04 "One gain", "Say it where the doubt is born").
2. *"Untracked" in plain words, and a docs/03 row proposed to the driver.* The book does not teach it yet and chapter 18 comes later, so the sentence says what it is where it appears: a file git does not hold yet, of which `git diff` shows nothing until it is staged. Chapter 8's report (`ch08-update-2026-10-18`) says the same in the same words, the second occurrence; this chapter, which teaches the rule, is the first. The glossary is the book's too, so the driver adds the row `untracked file` / `arquivo não rastreado` to docs/03 (the driver's decision for this batch), and the chapter uses it as defined there while keeping the plain-word explanation. Portuguese: `não rastreado`.
3. *Why created files are untracked at the review.* `/apply` stages only after the review, at the end of the "Green is not done" list, which the chapter already shows; the sentence says so, so the reader sees why the diff misses them (docs/05 §5 Delivery review, "which no diff shows until they are staged").
4. *Which created files are the delivery's.* The session that built the delivery wrote them and names them to the reviewer; another session's new files in the same folder are not this review's, as its edited files are not. This extends the chapter's existing sentence (docs/05 §5, "Another session's files are not this review's").
5. *The host's own review.* The sentence keeps "reads them its own way, kept to those paths", with the created files among those paths; the chapter claims no feature of any host (`ch13-delivery-review` decision 2).
6. *`lend-book`'s example.* Its migration, its rule, its repository call, its orchestrator and its screen are new files in `src/features/loans/` and the migrations' folder; the review reads them besides the `git diff` of the files it edited, the schema document and docs/06's hunk. One sentence says what that buys: the first candidate, `insertLoan`'s catch, sits in a file the delivery created, which a review of the diff alone would not have read. Nothing else of the example changes.
7. *"A line this delivery wrote" becomes "the text this delivery wrote", in both places (driver's decision, folded into this line).* The kit's `/apply` says "Fix what breaks the page, docs/04 or the text this delivery wrote", because "its own lines" read as queue lines; chapter 13 says "a line this delivery wrote" in the rule (en and pt line ~70) and in `lend-book`'s first candidate (line ~112). Both take the kit's words, so the rule and its example say the same thing: text this delivery wrote, a page, a document or code, against code it did not touch.
8. *Trunk; nothing staged by this definition; the driver sets docs/06's marks.* docs/05 §5 Git, and this batch's instructions.

**Behaviour.**

* Reading "The delivery review", a reader can say what the review reads: the delivery's changes by their paths, the files it created among them, and of docs/06 only this line's hunk, against the page and docs/04.
* A reader can say why the files the delivery created need naming: they are untracked, git does not hold them yet, so `git diff` shows nothing of them, and `/apply` stages only after the review.
* A reader can say who knows which new files are the delivery's: the session that wrote them, which names them to the reviewer.
* Edge: a reader working with a second session in the same folder can say that the other session's new files are not read by this review, as its edited files are not (chapter 19).
* Reading `lend-book`'s review, a reader sees the read-only agent read the files the delivery created, all of `src/features/loans/` and the migration, besides the `git diff` of the files it edited, and can say that the first candidate sat in a created file.
* Reading the rule on candidates, a reader finds that a candidate breaking the page, docs/04 or the text this delivery wrote is fixed in the session, and `lend-book`'s first candidate is fixed because it sits in the text this delivery wrote.
* Failure: "a line this delivery wrote" (pt "uma linha que esta entrega escreveu") left in chapter 13, a reader taking it as a queue line.
* Failure: a reader left believing the review is `git diff` alone would review a new slice and read nothing of it; the chapter's sentence and the example both say otherwise.
* The Portuguese edition reads the same in the same places, with the Contract's words and the lending library's Portuguese names.
* Failure: one edition changed and not the other, a pointer to chapter 18 added (chapter 13 explains the word itself), or a passage saying "no longer" or naming a version.

**Contract.**

* **Chapter 13, both editions** (`book/en/13-apply.md`, `book/pt/13-apply.md`), found by text:
  * In "The delivery review", the paragraph from "The review reads the delivery's changes by their paths" to "Another session's files in the same folder are not this review's (chapter 19)." (pt from "A revisão lê as mudanças da entrega pelos seus caminhos" to "Os arquivos de outra sessão na mesma pasta não são desta revisão (capítulo 19).") becomes, one sentence per line, the fourth sentence ("The reviewer brings ...", pt "O revisor traz ...") unchanged after it:
    "The review reads the delivery's changes by their paths, the files the delivery created among them, and of docs/06 only this line's hunk, against the page and docs/04."
    "A read-only agent reads their `git diff`, staged and unstaged, and opens each file the delivery created, which the session names, since it wrote them: a new file is untracked, one git does not hold yet, so `git diff` shows nothing of it until it is staged, and `/apply` stages only after the review."
    "The host's review reads them its own way, kept to those paths."
    "Another session's files in the same folder, the ones it created included, are not this review's (chapter 19)."
    (pt: "A revisão lê as mudanças da entrega pelos seus caminhos, entre elas os arquivos que a entrega criou, e do docs/06 só o trecho desta linha, contra a página e o docs/04." / "Um agente somente leitura lê o `git diff` delas, em stage e fora dele, e abre cada arquivo que a entrega criou, que a sessão cita, já que os escreveu: um arquivo novo é não rastreado, um que o git ainda não guarda, então o `git diff` não mostra nada dele até ele entrar em stage, e o `/apply` só põe em stage depois da revisão." / "A revisão do host as lê do seu jeito, mantida nesses caminhos." / "Os arquivos de outra sessão na mesma pasta, os que ela criou incluídos, não são desta revisão (capítulo 19).")
  * In "The delivery review", the sentence "A candidate that breaks the page, docs/04 or a line this delivery wrote is fixed in this session, and verify runs again." becomes "A candidate that breaks the page, docs/04 or the text this delivery wrote is fixed in this session, and verify runs again." (pt "Um candidato que quebra a página, o docs/04 ou uma linha que esta entrega escreveu é corrigido nesta sessão, e a verificação roda de novo." becomes "Um candidato que quebra a página, o docs/04 ou o texto que esta entrega escreveu é corrigido nesta sessão, e a verificação roda de novo.").
  * In "`lend-book`, built" (pt "`emprestar-livro`, construída"), the sentence "Then a read-only agent reads the `git diff` of the delivery's paths against the page and docs/04, in a review also written for this chapter, and reports two candidates." (pt "Depois um agente somente leitura lê o `git diff` dos caminhos da entrega contra a página e o docs/04, em uma revisão também escrita para este capítulo, e aponta dois candidatos.") becomes:
    "Then a read-only agent reads the files the delivery created, the migration and everything in `src/features/loans/`, and the `git diff` of what it edited, against the page and docs/04, in a review also written for this chapter, and reports two candidates."
    (pt: "Depois um agente somente leitura lê os arquivos que a entrega criou, a migration e tudo em `src/features/emprestimos/`, e o `git diff` do que ela editou, contra a página e o docs/04, em uma revisão também escrita para este capítulo, e aponta dois candidatos.")
  * In the sentence "No test triggers it, since in the tests only the unique index ever fails, and it sits in a line this delivery wrote, so ...", "it sits in a line this delivery wrote" becomes "it sits in the text this delivery wrote"; the rest of the sentence unchanged (pt "e está em uma linha que esta entrega escreveu" becomes "e está no texto que esta entrega escreveu").
  * After the sentence ending "the repository call chapters 3 and 4 describe is the fixed one." (pt "... a chamada do repositório que os capítulos 3 e 4 descrevem é a corrigida."), one sentence on its own line:
    "`insertLoan` lives in a file this delivery created, so a review of the `git diff` alone would have read nothing of it."
    (pt: "`inserirEmprestimo` fica em um arquivo que esta entrega criou, então uma revisão só do `git diff` não teria lido nada dele.")
  Every other section of chapter 13 is unchanged, the opening, "Green is not done", the gain and the key points included.
* **Portuguese words.** delivery review: `revisão da entrega`; read-only agent: `agente somente leitura`; untracked: `não rastreado`; stage: `stage` (`em stage`, `pôr em stage`); hunk: `trecho`; the lending library's names as chapter 13 already writes them (`src/features/emprestimos/`, `inserirEmprestimo`).
* **Terms of docs/03.** `delivery review`, `stage`, `candidate` used as defined. `untracked file` (`arquivo não rastreado`), the row the driver adds to docs/03, used as defined there, with the plain-word explanation kept in the sentence; docs/03's `delivery review` row ("its delivery's own changes") stays true and is M16's `docs03-review-rows`' to edit.
* **Sources.** None added or removed.
* **Cases.** No private case; the example is the lending library's, already said to be written for the chapter.
* **docs/06.** None from this page; the driver sets its line's marks.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* docs/03's `delivery review` row: `docs03-review-rows` (M16) owns it.
* Chapter 18's teaching of untracked files: chapter 13 explains the word where it needs it (decision 2).
* Chapter 8's report of the same migration: `ch08-update-2026-10-18`.
* Chapter 16's readers and chapter 19's two sessions: unchanged, still true.

**Done when.**

* [x] Both editions written in the places the Contract names, the English first; parity green.
* [x] `grep -c "created" book/en/13-apply.md` gives 5, the Contract's five new lines (0 before); `grep -n "untracked" book/en/13-apply.md` finds one line, `grep -n "não rastreado" book/pt/13-apply.md` one.
* [x] `grep -n "a line this delivery wrote" book/en/13-apply.md` and `grep -n "uma linha que esta entrega escreveu" book/pt/13-apply.md` find nothing; "the text this delivery wrote" (pt "o texto que esta entrega escreveu" / "no texto que esta entrega escreveu") twice in each edition.
* [x] docs/03 holds the `untracked file` row before this /apply edits chapter 13 (the driver's).
* [x] Chapter 13 still opens with its value; no filler, nothing useful cut; still five key points; no new chapter pointer.
* [x] The Portuguese uses the Contract's words and no synonym.
* [x] No em dash; `make verify` green (build, parity, em dash, prose, width, links, disclosure).
* [x] The Delivery review ran on this delivery's paths and the files it created (docs/05 §5), and the page records it.
* [x] The author's approval of an anonymized passage: inapplicable, no Case A or Case B passage.
* [x] `make book` builds; the delivery ends with the paths of both PDFs for the author's review.
* [x] Page moved to `work/done/`, the line `[x]`, staged by explicit paths and this line's hunk of docs/06; the commit message suggested, `docs(ch13-created-files): ...`.

**Proof.** `git diff book/` changes chapter 13 only in §The delivery review (en and pt 64 to 67 and 71) and §`lend-book`, built (111, 113 and the new 114), in both editions. `grep -c "created" book/en/13-apply.md` gives 5; "untracked" and "não rastreado" are each on one line (65); "a line this delivery wrote" and "uma linha que esta entrega escreveu" are gone; "the text this delivery wrote" and "o texto"/"no texto que esta entrega escreveu" appear twice in each edition. The opening, "Green is not done", the gain and the five key points are unchanged; no chapter pointer was added. docs/03 holds the `untracked file` / `arquivo não rastreado` row (the driver's, staged with this delivery). `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences.** One from the Contract: in the English `lend-book` sentence, "the `git diff` of what it edited" became "the `git diff` of what the delivery edited", because "it" read as the read-only agent, which edits nothing (review candidate 1). The Portuguese "do que ela editou" already names the delivery, so it stays as the Contract writes it.

**Decisions taken in /apply.**

* The driver's docs/03 row was reviewed as part of this delivery and staged with it; it matches the chapter's words and chapter 8's.
* Review candidates 2 to 5 were kept as they are: the long sentence and its "them" are the Contract's wording and read correctly; decision 2's "first" names the chapter that teaches the rule, as it says; "five new lines" counts the lines that carry "created", which the grep checks.

**Review.** One read-only agent on Opus read the chapter's diff in both editions, the docs/03 row and this line's hunk of docs/06, and this page, which the delivery's driver created, against this page and docs/04. Five candidates: the ambiguous "it" in the English `lend-book` sentence, fixed in this session (it breaks the text this delivery wrote), then verify ran again green; the other four kept, as Decisions says. No `[ ]` line added.

```commit
docs(ch13-created-files): chapter 13 reviews a delivery's created files

- Chapter 13: the delivery review opens the files the delivery created
- Say what an untracked file is and why no diff shows it at review time
- lend-book: insertLoan sits in a created file; "the text this delivery wrote"
- docs/03: the row untracked file / arquivo não rastreado; both editions

work/done/ch13-created-files.md
```
