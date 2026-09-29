# ch15-injection-rule

**Objective.** A reader of chapters 6 and 15 can state where FOCUS passes a dependency in, and why, in a form that fits the clinic's code: a piece receives a dependency only where its test passes a second implementation. The client orchestrator receives its repositories. On the server, the route receives the driver `db` and hands it on, and each repository function receives it too. A use case and a view receive none, and `now` is passed as data.

**Behaviour.**

* The reader can state the rule and check it against the code. The client's event functions receive their repositories, and their tests pass fakes. The route `appointmentsRoute(db)` receives the driver. Each server repository function takes `db`, and its test passes `memoryDatabase`, as chapter 16 shows. A client repository (`fetchProfessionals()`, `remember`) receives nothing, because no test passes a second implementation to it. A use case receives no repository (ADR-0016), and a view receives nothing, so a parameter there would exist for ceremony (KISS).
* The reader can tell a dependency from data: `now` is read by the route or the hook and passed on as a value. It is not a dependency, as chapter 16 already says.
* No sentence in `book/` says that only the orchestrator receives a dependency, or that nothing is passed anywhere else.
* Both editions say the same.
* Finding F11 of the M4 review is settled (`work/done/m4-review-run/findings.md:62`).

**Contract.**

Sentences are found by their quoted text. `ch15-event-delivery`, `ch15-submit-event`, `slice-imports` and `ch15-route-io` move the lines of chapters 6 and 15 before or after this delivery. The line numbers below are from commit `87433a5`.

* `book/en/15-four-pieces.md`, section "What the clinic injects" (heading and anchor unchanged):
  * The rule sentence "ADR-0016, as amended, gives the rule: the orchestrator is the only piece that receives its dependencies, and it receives them because a test passes a second implementation." (en:378, pt:379) becomes the criterion. English proposal for `/apply` to tighten: "ADR-0016, as amended, gives the rule: a piece receives a dependency only where its test passes a second implementation." Portuguese: "O ADR-0016, com as suas emendas, dá a regra: uma peça recebe uma dependência só onde o teste dela passa uma segunda implementação."
  * The server paragraph (en:381-382, pt:382-383) stays. One clause is added after "hand `db` to every repository call": each repository function receives `db` too, because its test passes `memoryDatabase` straight in, as chapter 16 shows. It links to chapter 16's section "One rule, five tests" (`16-testing-and-agents.md#one-rule-five-tests`, pt: `#uma-regra-cinco-testes`) and does not restate that test.
  * "Nowhere else is anything passed: ..." (en:413, pt:414) goes. English proposal: "A use case receives no repository (ADR-0016) and a view receives nothing: each has one implementation, so a parameter there would exist for ceremony, which KISS rules out. `now`, which the route or the hook reads, is passed on as data, a value, not a dependency." Portuguese: "Um caso de uso não recebe repositório (ADR-0016) e uma tela não recebe nada: cada um tem uma só implementação, então um parâmetro ali existiria por cerimônia, o que o KISS descarta. `now`, que a rota ou o hook lê, é passado adiante como dado, um valor, não uma dependência."
  * Key point 5 (en:436, pt:437) becomes: "A piece receives a dependency only where its test passes a second implementation, a fake: the orchestrator its repositories or the driver they use, and a server repository that driver; a use case and a view receive none, and `now` is passed as data." Portuguese: "Uma peça recebe uma dependência só onde o teste dela passa uma segunda implementação, uma falsa: o orquestrador os seus repositórios ou o driver que eles usam, e um repositório do servidor esse driver; um caso de uso e uma tela não recebem nenhuma, e `now` é passado como dado."
  * The note `[^book-adr-0016]` (en:459, pt:460): "amended 2026-09-29" names the dates of every amendment if `/apply` runs on a later day.
* `book/en/06-the-documents.md:107` and `book/pt/06-the-documents.md:109`: the clause "only the orchestrator has injected dependencies, and they are the repositories" becomes "a piece receives a dependency only where its test passes a second implementation: the orchestrator its repositories, and a server repository the driver it uses". Portuguese: "uma peça recebe uma dependência só onde o teste dela passa uma segunda implementação: o orquestrador os seus repositórios, e um repositório do servidor o driver que ele usa". The next sentence belongs to `ch15-route-io`.
* `docs/03-Domain.md`:
  * The orchestrator row (:43): "the only piece that receives its dependencies, its repositories or the driver they use, because only there a test passes a second implementation, a fake" becomes "it receives its repositories, or the driver they use, because its test passes a second implementation, a fake".
  * The repository row (:45), after `ch15-route-io` rewrites it, gains: "on the server it receives the driver it uses, because its test passes an in-memory database". If `ch15-route-io` has not been applied yet, only this clause is added and the rest of that row is left to it.
* `docs/adr/ADR-0016-the-books-definition-of-focus.md`: a new section `## Amendment, <date of /apply> (ch15-injection-rule)`, with the amendments ordered by apply date, whichever of this one and `ch15-route-io`'s comes first, and not overlapping it (route-io covers the event and the catch; this one covers injection). It says the criterion of the amendment `four-pieces-injection` stands: a dependency only where a test passes a second implementation. Two of that amendment's claims do not stand: "in FOCUS that happens only in the orchestrator" and "a view or a repository has one implementation". A server repository receives the driver it uses, because its test passes an in-memory database. A client repository receives none. A use case and a view receive none, and the clock is passed as data. The Decision's "The orchestrator is the only piece with injected dependencies" (:16) and the earlier amendment are read through this one and are not rewritten.
* Terms of docs/03: none new. Changed: orchestrator, repository (above). Used: fake.
* Sources: the clinic at `book-v1/four-pieces`. Every `src/features/*/repository.server.ts` function takes `db: DatabaseSync` first, for example `insertAppointment(db, appointment)`. `src/features/appointments/repository.server.test.ts:19` sets `db = memoryDatabase()`. Its `docs/01-Architecture.md` bullet "Use cases take the current time as a parameter" is already quoted by chapter 16. No new note or excerpt.
* Cases: none. Exercises: unchanged.

**Out of scope.**

* The clinic's code and docs/01: the person chose the book only. The repositories keep taking `db`.
* Chapter 16: it already shows the repository test against `memoryDatabase` and `now` as data. It is the second occurrence that chapter 15 points to, so it is not edited here. Its key point "only the orchestrator receives them" (en/16:356, pt/16:358) is about the repositories and stays true.
* Chapter 6's next sentence, the docs/03 repository row's I/O wording, and ADR-0016's amendment on the event: `ch15-route-io`, in flight.
* `work/done/four-pieces-injection.md`: it records the delivery that wrote the rule and is not edited.
* "When the pieces pay their way": the later line `ch15-piece-cost`. The unit test definition: `ch16-unit-test`.
* Slice imports (`slotsOf`), `submitEvent` and the event delivery: `slice-imports`, `ch15-submit-event` and `ch15-event-delivery`, in flight.

**Done when.**

* [ ] Both editions changed with the same meaning. Chapters 6 and 15 still open with their value, with no filler and nothing useful cut.
* [ ] No "Nowhere else is anything passed", "Em nenhum outro lugar se passa nada", "no other piece receives a dependency", "nenhuma outra peça recebe uma dependência", "only the orchestrator has injected dependencies", "só o orquestrador tem dependências injetadas", "the only piece that receives its dependencies" or "a única peça que recebe as suas dependências" left in `book/`. No "the only piece that receives its dependencies" left in docs/03.
* [ ] docs/03's orchestrator and repository rows updated, and ADR-0016 amended.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
