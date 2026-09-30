# ch16-unit-test-fakes

**Objective.** A reader of chapter 16 gets a definition of a unit test that every Vitest test the chapter shows fits, the event tests with their fake repositories and the tests that replace `localStorage` and `fetch` included, so they can use it to judge their own tests.

**Behaviour.**

* The reader can say what a unit test is: it runs in Node, with no browser and no server running, calls one piece directly, and runs the code that piece calls, except the I/O and the clock, which the test may swap.
* The reader can place each Vitest test the chapter shows by that definition: the use case's test swaps nothing, the repository's runs against an in-memory database, the route's fakes the clock, the event function's passes fake repositories, and `remembered.test.ts` and `request.test.ts` replace `localStorage` and `fetch`.
* The definition agrees with what the chapter says later, "a test swaps only the I/O and the clock" (en:319, en:365), and no sentence of the chapter says a unit test runs whatever its piece calls.
* docs/03's definition of a unit test says the same as the chapter.
* Both editions say the same.
* Finding F13 of the M4.1 review is settled (`work/done/m4.1-review-run/turn-1.txt:156`).

**Contract.**

Sentences are found by their quoted text. The line numbers below are from commit `cad46ef`. No other M4.2 line touches chapter 16.

* `book/en/16-testing-and-agents.md`, section "A test for each piece" (heading and anchor unchanged):
  * "A test Vitest runs is a unit test: it calls one piece directly, with no server running, and runs whatever that piece calls." (en:24; pt:25 "… e roda tudo o que essa peça chama.") becomes a definition that says the test runs what the piece calls except the I/O and the clock, which it may swap. English proposal for `/apply` to tighten: "A test Vitest runs is a unit test: it calls one piece directly, with no server running, and runs the code that piece calls, except the I/O and the clock, which the test may swap." Portuguese: "Um teste que o Vitest roda é um teste unitário: ele chama uma peça diretamente, sem servidor rodando, e roda o código que essa peça chama, menos o I/O e o relógio, que o teste pode trocar."
  * The next sentence (en:25; pt:26), which names the pieces a test can start from, stays, and may gain a pointer that the client's storage and network are swapped too, in "The client's I/O" (en:285; pt:286). `/apply` decides whether the pointer earns its place; said once only.
  * The Playwright sentence (en:26; pt:27) and the one after it stay.
* Checked and left alone, since they fit the new definition: en:179 and pt:180 ("fakes nothing"), en:246 ("nothing is faked but the repositories"), en:319 and pt:320, the key points at en:364 to en:366 and pt:366 to pt:368, and en/14:51 and pt/14:51 ("The `.test.ts` files are unit tests").
* `docs/03-Domain.md:59`, the `unit test` row: the definition becomes the chapter's. Proposed text: "A test that runs in Node, with no browser and no server running, calls one piece directly and runs the code that piece calls, except the I/O and the clock, which the test may swap: a use case with its data, a repository against an in-memory database, a route through `app.request` with a fake clock, or an event function with fake repositories; its requests never leave the process." The term, the Portuguese term ("teste unitário") and the pattern `*.test.ts` stay. The `fake` row (58) stays.
* Terms of docs/03: none new. One changed: `unit test`, its definition only. "Stub" is not made a term: the chapter names `vi.stubGlobal` only as the call it quotes.
* Sources: the clinic at `book-v1/four-pieces`, the excerpts the chapter already shows. No new note or excerpt.
* Cases: none. Ninjobs is not used. Exercises: unchanged.

**Out of scope.**

* Renaming any of these tests "integration tests": `ch16-unit-test` kept "unit test" and redefined it; this line only fixes the clause the fakes contradict.
* The clinic's docs/04 test table and its docs/01: the clinic's documents.
* Key point 2's reason ("only the repositories do I/O"), which the client's `remembered.ts` and `request` touch: not the finding, and it stays unless the new definition makes it false.
* Chapters 14 and 15: their M4.2 lines are separate deliveries.

**Done when.**

* [x] Both editions changed with the same meaning. Chapter 16 still opens with its value, with no filler and nothing useful cut.
* [x] No "runs whatever that piece calls" or "roda tudo o que essa peça chama" left in `book/` or `docs/03-Domain.md`.
* [x] Every Vitest test the chapter shows fits the definition, as the second Behaviour line lists.
* [x] The docs/03 `unit test` row matches the chapter's definition.
* [x] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author. Left unticked: in this batch the driver builds once at the end of the loop.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Revalidated against the current tree: the definition was still at en:24 and pt:25, the docs/03 row at line 59, and every "checked and left alone" line still fits; no document contradicted the page.
* en:24 and pt:25 took the page's proposed sentences as written: tightening found nothing to cut without losing the exception.
* Decided alone (batch, no conversation): no pointer to "The client's I/O" in en:25 and pt:26. The definition already names the I/O as what a test may swap, and that section, with en:319 and pt:320, places `remembered.test.ts` and `request.test.ts` where the reader meets them; the pointer would repeat it.
* docs/03's `unit test` row now carries the chapter's definition, with "a route through `app.request` with a fake clock", as the page proposed. Term, Portuguese term and pattern unchanged.
* Every Vitest test the chapter shows fits: the use case's swaps nothing (en:179), the repository's runs against an in-memory database, the route's fakes the clock with `vi.useFakeTimers`, the event function's passes fake repositories (en:246), and the client's two replace `localStorage` and `fetch` (en:306, en:309).
* `make verify` green. F13 of the M4.1 review settled.
