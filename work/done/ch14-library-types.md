# ch14-library-types

**Objective.** A reader of chapter 14 can say whether a library's type may cross the boundary, as `DatabaseSync`'s type reaches the clinic's routes, and how that squares with "changes that code alone": a type that code past the boundary only passes on, and never calls, carries none of the library's failures or methods, so a new version of the library still changes the I/O code alone; replacing the library also renames that type in each file that passes it, a change the compiler lists.

**Behaviour.**

* After "Every other file that names it, the repositories and the routes among them, imports only its type, to receive and pass the open database; no rule, hook, screen or `api.ts` imports it at all." (en/14:271, pt/14:271), two or three sentences say:
  * The routes never call the open database: they pass it to the repositories and to `requireSession`, so SQLite's methods and failures stay in the repositories and `database.server.ts`.
  * A library's type may cross the boundary as such a handle, passed on and never called; a new version of SQLite then changes the I/O code alone, as the Apple sentence says.
  * Replacing SQLite with another library changes that import line in each route too, and the compiler names every one; that is the price of passing the library's type instead of a type of the app's own.
* English proposal, for `/apply` to tighten: "The routes never call it: they hand it to the repositories and to `requireSession`, so SQLite's methods and failures stay behind them. A library's type may cross the boundary this way, as a handle passed on and never called, and a new version of SQLite still changes the I/O code alone. Replacing SQLite with another library would also change that import in each route, and the compiler would name every one."
* Portuguese, with the same meaning: "As rotas nunca o chamam: elas o entregam aos repositórios e a `requireSession`, então os métodos e as falhas do SQLite ficam atrás deles. Um tipo de biblioteca pode cruzar a fronteira assim, como uma alça repassada e nunca chamada, e uma versão nova do SQLite continua mudando só o código de I/O. Trocar o SQLite por outra biblioteca mudaria também esse import em cada rota, e o compilador apontaria cada uma."
* The key point "A library's exception belongs to the library: ..." (en/14:301, pt/14 same point) gains one clause: its type may pass the boundary only as a handle that code past it passes on and never calls.
* The Apple sentence (en/14:266, pt/14:266) and the `UNIQUE constraint` sentence (en/14:272) stay unchanged.
* Both editions say the same.
* Finding F8 of the M4.1 review, as narrowed in `work/done/m4.1-review-run/decisions.md`, is settled.

**Contract.**

* Files:
  * `book/en/14-errors-and-slices.md`: sentences after line 271 in "The boundary"; one clause in the key point at line 301.
  * `book/pt/14-errors-and-slices.md`: the same places ("A fronteira", line 271; the matching key point).
  * Line numbers are from `main` at cad46ef; sibling M4.2 lines (`ch14-keepless-feature`, `ch14-swallowed-bug`, `ch15-uncaught-pieces`) may move them. The quoted sentences are the reference.
* Terms of docs/03: none new. "Handle" is plain English here, not a term; docs/03 is not touched.
* Sources: the clinic at `book-v1/closing-a-milestone`, the tag the chapter uses. `git grep "node:sqlite" -- src` there: `import type { DatabaseSync }` in the five `route.server.ts`, the five `repository.server.ts`, `migrate.server.ts`, `session.server.ts` and `start.server.ts`; the value import only in `database.server.ts` (and `testDatabase.server.ts`). `git grep "db\.\(prepare\|exec\|close\)"` finds no call in any `route.server.ts`; outside tests, the calls are in the repositories, `database.server.ts`, `migrate.server.ts` and `session.server.ts`. Each route only passes `db` on, for example `appointments/route.server.ts:134-188` and `professionals/route.server.ts:49-87`.
* Cases: none. Exercises: unchanged (14.1 already asks for library exception types that leave the I/O code).

**Out of scope.**

* Changing the clinic, such as an app-owned `Database` type the routes import instead: the line asks the book to square the text; the clinic is not touched and no new line is added.
* The appointments repository matching SQLite's `UNIQUE` text: the review narrowed F8 and left it, since the repository is the I/O piece.
* Which piece `openDatabase` and `migrate` belong to, and the list of catches at en/14:239: `ch15-uncaught-pieces`.
* The feature definition and key point 1: `ch14-keepless-feature`. `query`'s swallowed bug and reason 4 of "Why not throw": `ch14-swallowed-bug`.
* `session.server.ts` calling the database from `src/server/`: not raised by the review.

**Done when.**

* [x] Both editions changed with the same meaning. Chapter 14 opens with its value, with no filler and nothing useful cut.
* [x] Every claim about the clinic checked again at `book-v1/closing-a-milestone`.
* [x] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Revalidated against the tree after `ch14-keepless-feature` and `ch14-swallowed-bug`: the quoted sentences and the key point were unchanged, now at lines 271, 277, 278 and 307 of both editions; the new sentences follow line 277.
* Re-check at `book-v1/closing-a-milestone`: `import type { DatabaseSync }` in the five `route.server.ts`, the five `repository.server.ts`, `migrate.server.ts`, `session.server.ts` and `start.server.ts`; the value import only in `database.server.ts` and `testDatabase.server.ts` outside tests. `git grep "db\.\(prepare\|exec\|close\)"` finds no call in any route; outside tests, the calls are in four repositories, `database.server.ts`, `migrate.server.ts` and `session.server.ts`. `requireSession` is called in three routes (professionals, signIn, weeklyHours), so "they hand it to the repositories and to `requireSession`" holds of the routes together.
* The English and Portuguese proposals went in as written; the page's wording was already short. Portuguese keeps "alça" for handle, as the page proposed, taken alone in the batch; it is plain Portuguese, not a docs/03 term.
* Key point: the clause was worded "a library's type crosses the boundary only as a handle that the code past it passes on and never calls", with "a library's type" in place of "its type", so it cannot read as the exception's type.
* `make book` not run: in this batch the driver builds once at the end of the loop, so that item stays unticked.
