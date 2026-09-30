# ch14-swallowed-bug

**Objective.** A reader of chapter 14 knows what to do about a bug that the boundary's catch turns into an exception: a test against the real database catches it before the app ships, and the code that turns the exception into an answer logs the message it carries, so the bug reaches the screen and the analytics after all. They can also say why reason 4 of "Why not throw" argues against a catch that steers the flow, and not against `query`.

**Behaviour.**

* The reader can say why reason 4 does not argue against `query`. Every catch wide enough to catch a library's exception also catches bugs. A catch that steers the flow pays that cost at every place the flow turns; the catch at I/O cannot be avoided, since the library throws, so the clinic pays it once, in `query`, and steers nothing with it. `query` is the example of the cost, paid in one place, not of the harm.
* The reader can say what catches such a bug before the app ships. A bug inside `run`, a `TypeError` or a malformed statement, makes `query` return `DatabaseFailed`. Every repository's SQL runs in a test against `memoryDatabase`, an in-memory SQLite with the real migrations, and the test expects `ok`, so the bug fails the test and its message reaches the screen while you develop. The text points to chapter 16, which shows these tests, and does not repeat them.
* The reader can say what makes such a bug visible once the app runs. `DatabaseFailed` carries the `message` of what was thrown. The rule: the code that turns an exception into an answer, a route in the clinic, logs what the exception carries before it answers, so a bug caught by accident reaches your analytics.
* The reader knows the clinic does not do this yet: its routes answer `DatabaseFailed` with the code alone and log nothing, the sentence the chapter already has. The text says so plainly and shows no logging code, since the clinic has none.
* The definition of an error stays: it says what the code aims for, as `ch14-catch-all` settled, and the new text says how a bug caught by accident still reaches your screen and your analytics.
* Both editions say the same.

**Contract.**

Sentences are found by their quoted text; `ch14-keepless-feature`, `ch14-library-types` and `ch15-uncaught-pieces` edit chapter 14 at the same time. The line numbers below are from commit `cad46ef`.

* `book/en/14-errors-and-slices.md`:
  * "Why not throw", reason 4 (line 114, "4. A catch wide enough to steer the flow also catches bugs, as `query` in the next section shows: a `TypeError` inside it becomes `DatabaseFailed`."), rewritten. Proposal, for `/apply` to tighten: "4. A catch wide enough to steer the flow also catches bugs. A catch at I/O cannot be avoided, since the library throws, so it pays that cost once, where the library is called, and steers nothing; a catch that steers the flow pays it at every place the flow turns. `query`, in the next section, is the clinic's one catch of that kind, and a `TypeError` inside it becomes `DatabaseFailed`."
  * "Exceptions as values in the clinic": after "The routes answer `DatabaseFailed` with its code alone and log nothing, so a bug caught there reaches neither your screen nor your analytics." (line 157), a new paragraph. Proposal: "Two things bring it back. Before the app ships, a test: every repository's SQL runs in a test against `memoryDatabase`, the in-memory SQLite with the real migrations that [chapter 16](16-testing-and-agents.md#one-rule-five-tests) shows, and the test expects `ok`, so a bug inside `run` fails it and shows its message. Once the app runs, a log: `DatabaseFailed` carries the `message` of what was thrown, so the code that turns it into an answer logs that message before it answers. The clinic does not log it yet; your app should."
  * Key points: one new point after "A library's exception belongs to the library: ...". Proposal: "The catch at the boundary also catches bugs, so every repository runs in a test against the real database, and the code that turns an exception into an answer logs what it carries."
* `book/pt/14-errors-and-slices.md`: the same places (line 114, "4. Um catch largo o bastante para conduzir o fluxo..."; line 157, "As rotas respondem `DatabaseFailed` só com o código e não registram nada..."; the key point "A exceção de uma biblioteca pertence à biblioteca: ..."). Proposals with the same meaning:
  * Reason 4: "4. Um catch largo o bastante para conduzir o fluxo também captura bugs. Um catch no I/O não pode ser evitado, já que a biblioteca lança, então paga esse custo uma vez, onde a biblioteca é chamada, e não conduz nada; um catch que conduz o fluxo o paga em cada lugar onde o fluxo muda. O `query`, na próxima seção, é o único catch desse tipo na clínica, e um `TypeError` dentro dele vira `DatabaseFailed`."
  * New paragraph: "Duas coisas o trazem de volta. Antes de o app sair, um teste: o SQL de todo repositório roda num teste contra o `memoryDatabase`, o SQLite em memória com as migrations reais que o [capítulo 16](16-testing-and-agents.md#uma-regra-cinco-testes) mostra, e o teste espera `ok`, então um bug dentro de `run` o faz falhar e mostra a mensagem. Com o app rodando, um log: `DatabaseFailed` carrega a `message` do que foi lançado, então o código que o transforma numa resposta registra essa mensagem antes de responder. A clínica ainda não a registra; o seu app deveria."
  * Key point: "O catch na fronteira também captura bugs, então todo repositório roda num teste contra o banco real, e o código que transforma uma exceção numa resposta registra o que ela carrega."
  * `/apply` takes the Portuguese anchor of chapter 16's section from the file, since the one above is assumed.
* Sources: the clinic at `book-v1/closing-a-milestone`, the tag the chapter uses. `memoryDatabase` is used by the repository tests of appointments, clinic, professionals and weeklyHours, by the five route tests and by `session.server.test.ts`; signIn has no repository test, and its repository runs through `signIn/route.server.test.ts`, so the text says "runs in a test", never "has its own test". `/apply` re-checks at the tag that every exported repository function and session query is called by a test that uses `memoryDatabase`; if one is not, the text names it instead of saying "every". The routes' answers with the code alone and no log are the lines `ch14-catch-all` listed; `git grep console` finds no log in `src` outside tests. No new note: the claims are the clinic's, linked where the chapter already links.
* Terms of docs/03: none new. The error row stays: it states the aim, as `ch14-catch-all` settled.
* Cases: none. Ninjobs is not used.
* Exercises: unchanged. Exercise 14.1 already asks for every `catch` and calls a change "a candidate for your queue, not a fix now".

**Out of scope.**

* Logging `DatabaseFailed`'s message in the clinic, or narrowing `query`: the book only, as the author chose in `ch14-catch-all`; the text says the clinic does not log yet.
* The Error definition (line 101), its key point and docs/03's error row: unchanged, as `ch14-catch-all` settled.
* A new exercise: 14.1 already covers the reader's own catches; a fourth would add work the text already states.
* The definition of a feature and key point 1: `ch14-keepless-feature`.
* "Changes that code alone" and the routes importing `DatabaseSync`'s type: `ch14-library-types`.
* Which piece `openDatabase` and `migrate` belong to (line 239): `ch15-uncaught-pieces`.
* Chapter 16's test text: `ch16-unit-test-fakes`; this delivery only links to it.

**Done when.**

* [x] Both editions changed with the same meaning. Chapter 14 opens with its value, with no filler and nothing useful cut.
* [x] Reason 4 and the new paragraph no longer leave the reader asking whether reason 4 argues against `query`.
* [x] The claim that every repository's SQL runs in a test against `memoryDatabase` was re-checked at `book-v1/closing-a-milestone`.
* [x] No logging code is shown, and the text says the clinic does not log yet.
* [x] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Revalidated against the tree after `ch14-keepless-feature`: the three quoted sentences were unchanged, now at lines 115, 158 and 302 of both editions; nothing else in the page's scope had moved.
* Re-check at `book-v1/closing-a-milestone`: every exported function of the five repositories is called by a test that uses `memoryDatabase`, directly or, for signIn's `findOwner`, through `signIn/route.server.test.ts`; `saveSession`, `findSession` and `deleteSession` run in `session.server.test.ts`, and `requireSession` through the route tests. "Every" stands.
* Divergence, taken alone in the batch: the page said `git grep console` finds no log in `src` outside tests. It does: `setup.server.ts` prints `DatabaseFailed`'s message ("Cannot read the database: ..."), and `start.server.ts` prints to the console too. The text therefore says `npm run setup` already prints the message and the routes do not log it yet, rather than "the clinic does not log it yet". Still no logging code shown.
* Divergence, taken alone: repository tests also expect refusals (`ok: false`), so "the test expects `ok`" became "the test checks the value it gets back".
* Tightened: reason 4 says "`query` ... is such a catch", not "the clinic's one catch of that kind", since chapter 14 lists other catches at I/O; the link to chapter 16 says "uses", since chapter 16 shows the tests using `memoryDatabase`. The key point says "SQLite with the real migrations", not "the real database". The Portuguese anchor of chapter 16's section, `#uma-regra-cinco-testes`, was taken from the file and passes `link-check`.
* `make book` not run: in this batch the driver builds once at the end of the loop, so that item stays unticked.
