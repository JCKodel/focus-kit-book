# ch14-catch-all

**Objective.** A reader of chapter 14 can see that the clinic's `query` catches every thrown value, so a bug inside it becomes `DatabaseFailed`. They can also say how that fits "Error: a bug, thrown and never caught": the definition says what the code aims for, and a catch at I/O is where a bug can be caught by accident.

**Behaviour.**

* After "This is the one `try`/`catch` a repository's SQL runs inside, and it turns the database's exception into a value." (en/14:127, pt/14:127), a short paragraph of two or three sentences says:
  * `query` catches every thrown value, not only the database's, so a bug inside `run`, such as a `TypeError` or a malformed statement, becomes `DatabaseFailed` too.
  * A narrower catch would not separate the two: SQLite reports a malformed statement with the same code, `ERR_SQLITE_ERROR`, as a missing table or a locked file. The claim carries a source footnote.
  * The definition of an error says what the code aims for. A catch at I/O is where a bug can be caught by accident.
  * The routes answer `DatabaseFailed` with its code alone and log nothing, so a bug caught there reaches neither your screen nor your analytics.
* English proposal, for `/apply` to tighten: "`query` catches every thrown value, not only the database's, so a bug inside `run`, a `TypeError` or a malformed statement, becomes `DatabaseFailed` too. A narrower catch would not tell them apart: SQLite reports a malformed statement with the same code as a missing table or a locked file, `ERR_SQLITE_ERROR`.[^node-sqlite-error] The definition of an error says what the code aims for, and a catch at I/O is where a bug can be caught by accident. The routes answer `DatabaseFailed` with its code alone and log nothing, so such a bug reaches neither your screen nor your analytics."
* Portuguese, with the same meaning: "`query` captura todo valor lançado, não só os do banco, então um bug dentro de `run`, um `TypeError` ou um comando malformado, também vira `DatabaseFailed`. Uma captura mais estreita não separaria os dois: o SQLite informa um comando malformado com o mesmo código de uma tabela ausente ou de um arquivo travado, `ERR_SQLITE_ERROR`.[^node-sqlite-error] A definição de erro diz o que o código busca, e uma captura no I/O é onde um bug pode ser capturado por acidente. As rotas respondem `DatabaseFailed` só com o código e não registram nada, então esse bug não chega nem à sua tela nem ao seu analytics."
* These stay unchanged: the Error definition (en/14:85, pt/14:85), the error key point (en/14:249, pt/14:249), `query`'s excerpt and its tag.
* Both editions say the same.
* Finding F5 of the M4 review is settled.

**Contract.**

* Files:
  * `book/en/14-errors-and-slices.md`: one paragraph after line 127, and the footnote `[^node-sqlite-error]` with the others at the end of the chapter.
  * `book/pt/14-errors-and-slices.md`: the same places.
  * The line numbers are from before `ch14-feature-boundary` and `ch14-refusal-io`, which move the lines below 53 and 84. The quoted sentences are the reference.
* Footnote, English: `[^node-sqlite-error]: Node.js, "Errors", API reference, ERR_SQLITE_ERROR, accessed <date of /apply>: "An error was returned from SQLite." <https://nodejs.org/api/errors.html#err_sqlite_error>`. The Portuguese keeps the quote in English, as `[^dart-core]` does, with "acesso em".
* Terms of docs/03: none new. docs/03 is not touched, and the error row (line 51) stays.
* Sources: the clinic at `book-v1/closing-a-milestone`, the tag the chapter uses. `src/server/database.server.ts:33-40` is `query`, identical at `book-v1/four-pieces`. The routes answer with code alone: `appointments/route.server.ts:71`, `professionals/route.server.ts:40`, `weeklyHours/route.server.ts:28`, `clinic/route.server.ts:8`, `signIn/route.server.ts:44`, all `c.json({ error: { code: "DatabaseFailed" } }, 500)` with no log. The shared code for a malformed statement was checked by running `prepare("SELEC 1")` on `node:sqlite` (Node v26.10.0): `code` is `ERR_SQLITE_ERROR`. The clinic already treats a missing table as an exception on purpose (`professionals/repository.server.test.ts:87`).
* Cases: none. Exercises: unchanged. Exercise 14.1 already asks the reader to list every `try`/`catch`.

**Out of scope.**

* Changing the clinic's `query` or logging the message in `databaseFailed`: the person chose the book only and no new line. The clinic repository is not touched.
* Rewording the Error definition, its key point, en/pt 06:108 or docs/03:51 and :53: the definition stays and the new paragraph does the reconciling.
* The refusal definition (line 84), key point 3 (line 248) and the refusal row of docs/03: `ch14-refusal-io`, in flight.
* The first key point, line 53 and the slice text: `ch14-feature-boundary`, in flight.
* The route that reads the request body, lines 208 and 209, and docs/03:45 ("the only code with `try`/`catch`"): the later line `ch15-route-io`.

**Done when.**

* [x] Both editions changed with the same meaning. Chapter 14 opens with its value, with no filler and nothing useful cut.
* [x] The claim about `ERR_SQLITE_ERROR` has its footnote in both editions.
* [x] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author: run once at the end of the M4.1 loop by the driver.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* The paragraph went in as four lines after the anchor sentence, in both editions, one sentence per line. Tightened from the proposal: "a `TypeError` or a malformed statement" became "such as a `TypeError` or a malformed statement", the third sentence joins its halves with a semicolon, and the last says "a bug caught there".
* The footnote went last, after `[^book-adr-0016]`, since its first reference follows that one. Access date 2026-09-30; the quote was checked on nodejs.org, and `prepare("SELEC 1")` and a missing table both throw `ERR_SQLITE_ERROR` on the local Node.
* Diverged: the page asked the Portuguese footnote to keep the quote in English "as `[^dart-core]` does", but `[^dart-core]` translates its quotes and keeps only the titles in English. The Portuguese follows `[^dart-core]`: title "Errors" in English, the quote translated.
* The routes' claim was checked at `book-v1/closing-a-milestone`: every `DatabaseFailed` answer in the five `route.server.ts` files is the code alone, and no route logs.
* Finding F5 of the M4 review is settled.
