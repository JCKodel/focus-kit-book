# ch15-uncaught-pieces

**Objective.** A reader of chapters 14 and 15 can place `openDatabase` and `migrate` in the clinic: they are no piece, they are the server's start code, which runs once before any request, makes ready the driver every repository receives, and stops the server when it cannot. They can also read the table's "the only place an infra exception becomes a Result" as holding for the pieces that serve an event.

**Behaviour.**

* In chapter 15, section "What the clinic injects", right after the paragraph "The server's orchestrator receives the database, ..." (en/15:403, pt/15:404), a new paragraph says where that database comes from. It names `openMigratedDatabase` in `src/server/start.server.ts`, which calls `openDatabase` and `migrate` and is called by `main.server.ts`, which hands its database to every route. It says neither is a piece, because no event reaches them: they run once, at start. They catch where they do I/O, as a repository does, and return a Result, and `openMigratedDatabase` turns a failure into a message and exit code 1. It ends by squaring the table: among the pieces that serve an event, only the repository turns an infra exception into a Result.
* English proposal, for `/apply` to tighten: "That database is opened before the first request arrives, by the server's start code: `openMigratedDatabase`, in [`src/server/start.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/server/start.server.ts), calls `openDatabase` and `migrate`, and `main.server.ts` hands the database it returns to every route. Neither is a piece: no event reaches them, and they run once, at start, to make the driver ready. They catch where they do I/O, as a repository does, and return a `Result`; `openMigratedDatabase` turns a failure into a message and exit code 1, because a server with no database has nothing to serve. So the table's "only" holds where events are served: of the four pieces, the repository alone turns an infra exception into a `Result`."
* Portuguese, with the same meaning: "Esse banco é aberto antes que chegue a primeira requisição, pelo código de partida do servidor: `openMigratedDatabase`, em [`src/server/start.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/server/start.server.ts), chama `openDatabase` e `migrate`, e `main.server.ts` entrega o banco que ela devolve a cada rota. Nenhuma das duas é uma peça: nenhum evento chega a elas, e elas rodam uma vez, na partida, para deixar o driver pronto. Elas capturam onde fazem I/O, como faz um repositório, e devolvem um `Result`; `openMigratedDatabase` transforma uma falha numa mensagem e no código de saída 1, porque um servidor sem banco não tem o que servir. Então o "único" da tabela vale onde os eventos são servidos: das quatro peças, só o repositório transforma uma exceção de infra num `Result`."
* In chapter 14, after "Each route that reads a request body catches too, ..." (en/14:240, pt/14:240), one sentence says that `openDatabase` and the migration runner run once, when the server starts, before any request, and links to where chapter 15 places them. English: "`openDatabase` and the migration runner run once, when the server starts, before any request; [chapter 15](15-four-pieces.md#what-the-clinic-injects) says where they stand among the pieces." Portuguese: "`openDatabase` e o executor de migrations rodam uma vez, quando o servidor parte, antes de qualquer requisição; o [capítulo 15](15-four-pieces.md#o-que-a-clinica-injeta) diz onde eles ficam entre as peças."
* The table row (en/15:27, pt/15:28) stays, because it quotes the clinic's docs/01 word for word.
* Both editions say the same.
* Finding F10 of the M4.1 review is settled.

**Contract.**

* Files:
  * `book/en/15-four-pieces.md` and `book/pt/15-four-pieces.md`: one paragraph after the server orchestrator's paragraph of "What the clinic injects" / "O que a clínica injeta".
  * `book/en/14-errors-and-slices.md` and `book/pt/14-errors-and-slices.md`: one sentence after the route-body sentence of "Exceptions as values in the clinic" / "Exceções como valores na clínica".
  * Line numbers are from `main` at the time of this page; sibling M4.2 lines may move them. The quoted sentences are the reference.
* Terms of docs/03: none new. "Start code" and "código de partida" are plain words, not a term; "driver" is docs/03's. The repository row already says "the only piece that catches an exception from data", which this reading keeps.
* Sources: the clinic at `book-v1/four-pieces`: `src/server/start.server.ts` (`openMigratedDatabase`, exit code 1 on either failure), `src/server/database.server.ts` (`openDatabase` returns `Result<DatabaseSync, DatabaseOpenFailed>`), `src/server/migrate.server.ts` (`migrate` returns `Result<string[], MigrationFailed>`), `src/server/main.server.ts` (`const db = openMigratedDatabase()`, then every route of `db`); the four files are unchanged at `6edc9ad`. ADR-0016's amendment ch15-route-io already says startup code catches where it does I/O outside the four pieces; no new amendment. F10 is in `work/done/m4.1-review-run/findings.md:55`.
* Cases: none. Exercises: unchanged.

**Out of scope.**

* The clinic and its docs/01 table: the book only; the table is quoted, not changed.
* The setup command, `request.ts` and `remembered.ts`: the setup command shares `openMigratedDatabase` and needs no separate placing; `request.ts` and `remembered.ts` already sit under client repositories in chapter 15.
* `query`'s catch-all and a bug it hides: `ch14-swallowed-bug`. Routes importing `DatabaseSync`'s type: `ch14-library-types`.
* `memoryDatabase`, which calls `migrate` and throws: chapter 14 already explains it as test-only.

**Done when.**

* [x] Both editions changed with the same meaning. Chapters 14 and 15 open with their value, with no filler and nothing useful cut.
* [x] `openDatabase` and `migrate` are placed in chapter 15 in both editions, and chapter 14 links there.
* [x] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author. Left unticked on purpose: in this batch the driver runs `make book` once at the end of the loop.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Revalidated against the tree after `ch14-keepless-feature`, `ch14-swallowed-bug` and `ch14-library-types`: the quoted sentences had moved (en/14:246, pt/14:246; en/15:403, pt/15:404) but were unchanged. The four clinic files at `book-v1/four-pieces` say what the Contract says.
* Diverged, taken alone (batch, no conversation): "hands the database it returns to every route" became "to every route that needs it" (pt "a cada rota que precisa dele"), because `healthRoute` is mounted without `db` in `main.server.ts`, and `ch14-keepless-feature` now names `health` as the feature that keeps nothing.
* Diverged, taken alone: the new paragraph goes after the whole server discussion, after "Vitest is the clinic's test runner, ..." and before "The client's orchestrator receives ...", not between the orchestrator's paragraph and its next line, "The route's test passes `memoryDatabase` ...", which continues that paragraph; inserting it there would have cut the route's test away from the route.
* The rest of the proposed text is used as written, in both editions. `make verify` green. No document other than the chapters changed: no new term, no new rule, no ADR amendment (ADR-0016's ch15-route-io amendment already covers start code).
* Finding F10 of the M4.1 review is settled.
