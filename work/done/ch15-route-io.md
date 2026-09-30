# ch15-route-io

**Objective.** A reader of chapters 6, 14 and 15 can see that a server route reading its request body follows FOCUS. The request is the event, and receiving it belongs to the orchestrator, as a tap does on the client. The repository is the only piece that fetches and saves, and the only piece where an infra exception from data becomes a Result.

**Behaviour.**

* Chapter 6's sentence on the repository is described by role. It no longer says "Only the repository does I/O, so only it catches" (en/06:108, pt/06:110). It says: the orchestrator receives the event, and on a server the event is the request. The repository is the only piece that fetches and saves, so it is the only piece that catches an exception from data, an expected failure such as a lost connection, and returns it as a value, a Result. An error, a bug, is never caught. The Dart clause and its footnote `[^dart-error-exception]` stay.
* English proposal for chapter 6, for `/apply` to tighten: "The orchestrator receives the event, a request on a server; only the repository fetches and saves, so only it catches an exception from data, an expected failure such as a lost connection, and returns it as a value, a Result; an error, a bug, is never caught (Dart splits its `Exception` and `Error` classes the same way).[^dart-error-exception]"
* Portuguese, with the same meaning: "O orquestrador recebe o evento, uma requisição no servidor; só o repositório busca e salva, então só ele captura uma exceção vinda dos dados, uma falha esperada como uma conexão perdida, e a devolve como valor, um Result; um erro, um bug, nunca é capturado (o Dart separa as suas classes `Exception` e `Error` do mesmo jeito).[^dart-error-exception]"
* In chapter 15, after "In order: the body's shape, ..." (en/15:331, pt/15:332), one sentence says the route reads the body itself because the request is the event it receives. A body that cannot be read becomes `BadRequest`, as chapter 14 says. It links to [chapter 14's section](14-errors-and-slices.md#exceptions-as-values-in-the-clinic) (pt: `#excecoes-como-valores-na-clinica`). English proposal: "The route reads the body itself, because the request is the event it receives; a body that cannot be read becomes `BadRequest`, as [chapter 14](14-errors-and-slices.md#exceptions-as-values-in-the-clinic) says." Portuguese: "A rota lê o corpo ela mesma, porque a requisição é o evento que ela recebe; um corpo que não pode ser lido vira `BadRequest`, como diz o [capítulo 14](14-errors-and-slices.md#excecoes-como-valores-na-clinica)."
* The first key point of chapter 15 (en/15:432, pt/15:433) ends "and the repository is the only piece that fetches and saves" in place of "the only code that does I/O". Portuguese: "e o repositório é a única peça que busca e salva".
* The table row "the only place an infra exception becomes a Result" (en/15:18, pt/15:19) stays, because it quotes the clinic's docs/01 word for word, and under this reading it holds. The comment inside `query`'s excerpt (en/14:115-116, pt the same) stays, because it is real code.
* ch14:208-209 are unchanged, and chapter 15 points back to 209.
* Both editions say the same.
* Finding F8 of the M4 review is settled.

**Contract.**

* Files:
  * `book/en/06-the-documents.md:108` and `book/pt/06-the-documents.md:110`: the sentence above.
  * `book/en/15-four-pieces.md`: one sentence after line 331, and key point 1 at line 432. `book/pt/15-four-pieces.md`: after line 332, and line 433.
  * `docs/03-Domain.md:45`, the repository row. The meaning becomes: "The FOCUS piece that fetches and saves; the only piece that catches an exception from data, and it returns every exception as a value. The event it serves is received by the orchestrator, a request on a server." The phrase "the only code that does I/O and the only code with `try`/`catch`" goes.
  * `docs/adr/ADR-0016-the-books-definition-of-focus.md`: a new section `## Amendment, <date of /apply> (ch15-route-io)`. It says the orchestrator receives its event, and on a server reading the request body is part of that, answered `BadRequest` when it cannot be read. "Only repositories have `try`/`catch`" (line 20) reads as: only the repository catches an exception from data, and startup code (opening the database, migrations) catches where it does I/O outside the pieces. Line 20 is not rewritten.
  * Line numbers are from before `ch15-event-delivery`, which may move chapter 15's lines. The quoted sentences are the reference.
* Terms of docs/03: none new. The "repository" row changes as above.
* Sources: the clinic at `book-v1/four-pieces`, the same at `book-v1/closing-a-milestone`. Six routes read the body with `c.req.json().catch(() => undefined)`: `appointments/route.server.ts:143,177`, `professionals/route.server.ts:57,68`, `signIn/route.server.ts:39`, `weeklyHours/route.server.ts:70`. Its `docs/01-Architecture.md:33` is the table row. F8 is in `work/done/m4-review-run/findings.md:46`.
* Cases: none. Exercises: unchanged.

**Out of scope.**

* The clinic and its docs/01 table: the person chose the book only. The clinic repository is not touched.
* ch14:208-209 and the other catches they list (`openDatabase`, `query`, the migration runner, `request.ts`, `remembered.ts`): these are already placed by chapter 14 and stay unchanged.
* The refusal definition and key point 3: `ch14-refusal-io`, in flight. `query`'s catch-all and the Error definition: `ch14-catch-all`, in flight.
* "only the orchestrator has injected dependencies" (en/06:107) and key point 5 of chapter 15: the later line `ch15-injection-rule`.
* A slice importing another slice's repositories (`slotsOf`): the later line `slice-imports`. `submitEvent`: `ch15-submit-event`.

**Done when.**

* [x] Both editions changed with the same meaning. Chapters 6 and 15 open with their value, with no filler and nothing useful cut.
* [x] No "Only the repository does I/O", "Só o repositório faz I/O", "the only code that does I/O" or "o único código que faz I/O" left in `book/`. Neither docs/03 nor ADR-0016's amendment says "the only code with `try`/`catch`".
* [x] docs/03:45 updated, and ADR-0016 amended.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author: run once at the end of the M4.1 loop by the driver, on 2026-09-30, both PDFs built
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Chapter 6 takes the page's sentence as proposed, in both editions; the Dart clause and its footnote stay.
* Chapter 15's new sentence follows "In order: ..." as proposed; `ch15-event-delivery` had moved it to en/15:342 and pt/15:343, and key point 1 to en/15:441 and pt/15:442. Chapter 14's line on the route's catch is now at ch14:218 (it was 209) after the earlier chapter 14 deliveries; it is unchanged and the new sentence links to its section.
* docs/03's repository row reads as the page asked. ADR-0016's amendment is scoped to reading the request body and to where startup code catches; line 20 is not rewritten, and `ch15-injection-rule` adds its own amendment after this one.
* Finding F8 of the M4 review is settled. `make verify` green.
