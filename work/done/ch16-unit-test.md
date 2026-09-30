# ch16-unit-test

**Objective.** A reader of chapter 16 gets a definition of a unit test that every Vitest test the chapter shows fits, the route test included, and can tell a unit test from an end-to-end test by where it runs.

**Behaviour.**

* The reader can say what a unit test is: it runs in Node, with no browser and no running server, and starts from one piece, which it calls directly: a use case with its data, a repository against an in-memory database, a route through `app.request`, or a client event function with fake repositories. It runs whatever that piece calls.
* The reader can place the route test by that definition. It starts from `appointmentsRoute(db)`, and the request goes through `app.request`, not the network, so it is a unit test that also runs the use case `cancel`, the repository and SQLite behind the route.
* The reader can say where a unit test ends and an end-to-end test begins. An end-to-end test drives the running app in a browser, through the network. A unit test has no browser, and its request never leaves the process.
* docs/03's definition of a unit test says the same as the chapter.
* Both editions say the same.
* Finding F13 of the M4 review is settled (`work/done/m4-review-run/findings.md:73`).

**Contract.**

Sentences are found by their quoted text. The line numbers below are from commit `bce05e3`. `slice-imports` (en/16:334,341; pt/16:335,343) and `ch14-feature-boundary` (pt/16:27,179,329) are in flight on chapter 16. This page does not touch their lines.

* `book/en/16-testing-and-agents.md`, section "A test for each piece" (heading and anchor unchanged):
  * "A test Vitest runs is a unit test: it runs one piece of code, such as a use case called with its data or a repository against an in-memory database." (en:24; pt:25 "Um teste que o Vitest roda é um teste unitário: ele roda um pedaço de código, …") becomes a definition that names the pieces a test can start from, the route included, and says the test runs what that piece calls. English proposal for `/apply` to tighten: "A test Vitest runs is a unit test: it runs in Node, with no browser and no server running, and calls one piece directly, such as a use case with its data, a repository against an in-memory database, or a route through `app.request`, which runs the use case and the repository behind it." Portuguese: "Um teste que o Vitest roda é um teste unitário: ele roda no Node, sem navegador e sem servidor rodando, e chama uma peça diretamente, como um caso de uso com os seus dados, um repositório contra um banco em memória, ou uma rota por `app.request`, que roda o caso de uso e o repositório por trás dela."
  * "A test Playwright runs is an end-to-end test: …" (en:25; pt:26) keeps its meaning and gains the line against the unit test: the end-to-end test's request crosses the network to a running server, and a unit test's never leaves the process. `/apply` may fold this into the sentence at en:24 instead, but it is said once only.
  * The sentence at en:26 and pt:27 ("They are the `.test.ts` and `.e2e.ts` files …") stays. `ch14-feature-boundary` owns pt:27.
* `docs/03-Domain.md:59`, the `unit test` row: the definition becomes the chapter's. The term, the Portuguese term ("teste unitário") and the pattern `*.test.ts` stay. Row 60, `end-to-end test`, stays.
* Checked and left alone, since they still fit the new definition: en/14:51 and pt/14:51 ("The `.test.ts` files are unit tests"), en/11:117 and pt/11:117 ("Seven unit tests of the migration runner and the database"), and en/08:298 and pt/08:300, which quote an artifact. Chapter 16's key point 1 (en:355, pt:357) already lists "a route through `app.request` with a fake clock" and stays.
* Terms of docs/03: none new. One changed: `unit test`, its definition only.
* Sources: the clinic at `book-v1/four-pieces`. `src/features/appointments/route.server.ts:194` calls `cancel` and `:198` calls `cancelAppointment(db, …)`, which is what the chapter already shows at en:153 and en:177. No new note or excerpt.
* Cases: none. Ninjobs is not used. Exercises: unchanged.

**Out of scope.**

* Renaming the route or repository tests "integration tests", or dropping the term: the person kept "unit test" and redefined it.
* Chapters 14 and 11: checked, and their sentences fit the new definition. Three chapter 14 pages are in flight.
* The clinic's docs/04 test table, which has no route row, and its docs/01 "Vitest for units and repositories": the clinic's documents, and the person left them out.
* The `it.each` over three refusal codes (en/16:197-215): the later line `ch16-it-each`.
* The key point's "20 of 95 files" (en/16:359): the later line `ch16-reading-count`.
* "Shared code" at en/16:334 and en/16:341: `slice-imports`, in flight.

**Done when.**

* [x] Both editions changed with the same meaning. Chapter 16 still opens with its value, with no filler and nothing useful cut.
* [x] No "it runs one piece of code" or "ele roda um pedaço de código" left in `book/` or `docs/03-Domain.md`.
* [x] The definition names the route through `app.request`, and the line against the end-to-end test is said once, in both editions.
* [x] The docs/03 `unit test` row matches the chapter's definition.
* [x] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author. Run once at the end of the M4.1 loop by the driver.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* §"A test for each piece": the unit-test sentence split in two. The first says what a unit test is: it calls one piece directly, with no server running, and runs whatever that piece calls. The second names the pieces: a use case with its data, a repository against an in-memory database, a route through `app.request`, which runs the use case and the repository behind it, or an event function with fake repositories.
* Tightened from the proposal: "runs in Node, with no browser" is left out of the chapter's sentence, since the line just above it already says "Vitest runs a test in Node, with no browser". The event function is named too, as the Behaviour asks, so every Vitest test the chapter shows fits.
* Choice taken: the line against the end-to-end test is folded into the Playwright sentence ("its requests cross the network to that server, where a unit test's request never leaves the process"), said once.
* docs/03 `unit test` row: the chapter's definition, with Node and no browser kept, since the row stands alone.
* Finding F13 of the M4 review is settled.
