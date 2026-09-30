# ch16-it-each

**Objective.** A reader of chapter 16 can match the client event's first test to its code: it is one `it.each` that Vitest runs three times, once for each of two refusals and one exception, and the reader can say what `it.each` does.

**Behaviour.**

* The reader can say what `it.each` does. It runs the test function once for each value in its list. It passes the value to the function as `code` and puts it in the name where `%s` stands.
* The reader can name the three tests Vitest runs from it: `keeps what was typed and shows AppointmentNotFound`, `keeps what was typed and shows CancellationTooLate` and `keeps what was typed and shows ServerUnreachable`.
* The reader can say what each of the three codes is: `AppointmentNotFound` and `CancellationTooLate` are refusals, and `ServerUnreachable` is an exception, what `postCancellation` returns when no usable answer arrives. The terms are the ones chapter 14 uses.
* The reader can say what all three runs check: the fake `postCancellation` answers the code, what was typed is kept, `busy` is false, and `message` is the code.
* The reader counts four tests under `describe("submitting", ...)` in the excerpt, three of them written once.
* Both editions say the same.
* Finding F14 of the M4 review is settled (`work/done/m4-review-run/findings.md:79`).

**Contract.**

Sentences are found by their quoted text. The line numbers below are from commit `fb419ac`. Three other pages are in flight on chapter 16: `ch16-unit-test` (en:24-25, pt:25-26), `slice-imports` (en:334,341; pt:335,343) and `ch14-feature-boundary` (pt:27,179,329). This page does not touch their lines.

* `book/en/16-testing-and-agents.md`, section "A test for each piece", paragraph "The client's event" (heading and anchor unchanged):
  * "These are two of its tests under `describe("submitting", ...)`:" (en:194; pt:195 "Estes são dois dos seus testes sob `describe("submitting", ...)`:") becomes "These are four of its tests under `describe("submitting", ...)`, the first three written once:". Portuguese: "Estes são quatro dos seus testes sob `describe("submitting", ...)`, os três primeiros escritos uma vez só:".
  * "In the first test the fake `postCancellation` answers `CancellationTooLate`, as the server would, and the test checks the new state, what was typed kept and the refusal named, with no screen." (en:242; pt:243 "No primeiro teste o `postCancellation` falso responde `CancellationTooLate`, como o servidor responderia, …") becomes two sentences. English proposal for `/apply` to tighten: "`it.each` runs the function once for each value in its list, passes it as `code` and puts it where `%s` is in the name,[^vitest-each] so Vitest runs `keeps what was typed and shows AppointmentNotFound`, the same with `CancellationTooLate`, and the same with `ServerUnreachable`: two refusals and one exception. In each, the fake `postCancellation` answers the code, as the server, or a failed request, would, and the test checks the new state, what was typed kept and the code named, with no screen." Portuguese: "`it.each` roda a função uma vez para cada valor da sua lista, passa o valor como `code` e o põe onde `%s` está no nome,[^vitest-each] então o Vitest roda `keeps what was typed and shows AppointmentNotFound`, o mesmo com `CancellationTooLate` e o mesmo com `ServerUnreachable`: duas recusas e uma exceção. Em cada um, o `postCancellation` falso responde o código, como o servidor, ou uma requisição que falhou, responderia, e o teste confere o novo estado, o que foi digitado mantido e o código nomeado, sem tela." In Portuguese the test names stay in English, with the translation in parentheses, as pt:311-314 already does.
  * The code excerpt (en:196-239; pt:197-240) stays as it is: it matches the clinic's `src/features/appointments/cancelEvents.test.ts:55-72` at `book-v1/four-pieces`.
* Notes, both editions: a new `[^vitest-each]`, with the same form as `[^vitest]` (en:382), placed with the chapter's other notes. "Vitest, "Test", the API reference, `test.each`, accessed <delivery date>. <https://vitest.dev/api/#test-each>". The note says `it.each` is the same function as `test.each`. `/apply` checks the page's title and anchor on the delivery date.
* `docs/06-Queue.md`, this line: "the it.each over three refusal codes" became "the it.each over two refusal codes and an exception" when this page was proposed, because docs/03:49-50 makes `ServerUnreachable` an exception.
* Terms of docs/03: none new. `refusal` and `exception` are used as docs/03:49-50 defines them.
* Sources: the clinic at `book-v1/four-pieces`. `cancelEvents.test.ts:55-72` is the `it.each`. `api.ts:25-30` types `AppointmentNotFound` and `CancellationTooLate` beside `ServerUnreachable`, which `src/lib/request.ts` exports. The clinic's docs/03:28 calls `AppointmentNotFound` a refusal. Vitest's API page for `test.each`.
* Cases: none. Ninjobs is not used. Exercises: unchanged.

**Out of scope.**

* `as const` in the excerpt: the review did not flag it.
* The `it.each` in `rememberedEvents.test.ts:102`: the book does not show it.
* "names the refusal" (en:280; pt:281): it is about the deadline rule, and it stays.
* The unit-test definition (en:24-25): `ch16-unit-test`, in flight.
* The key point's "20 of 95 files" (en:359): the later line `ch16-reading-count`.
* A listing of Vitest's output with the three names: no recorded run has one, and the names follow from the code.

**Done when.**

* [x] Both editions changed with the same meaning. Chapter 16 still opens with its value, with no filler and nothing useful cut.
* [x] `grep -n "In the first test the fake\|No primeiro teste o" book/*/16-testing-and-agents.md` finds nothing.
* [x] `grep -n "two of its tests\|dois dos seus testes" book/*/16-testing-and-agents.md` finds nothing.
* [x] `[^vitest-each]` is in both editions, and its link opens Vitest's `test.each` section.
* [x] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author: run once at the end of the M4.1 loop by the driver.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* §"A test for each piece", "The client's event": the intro line now counts four tests, the first three written once.
* The "first test" sentence became two, tightened from the proposal: the first says what `it.each` does and names the three runs, then says `AppointmentNotFound` and `CancellationTooLate` are refusals and `ServerUnreachable` the exception `postCancellation` returns when no usable answer arrives (the Behaviour's wording). The second says what each run checks. In Portuguese the first test name keeps its translation in parentheses, as the `request` list does; the other two are said as "o mesmo com".
* Choice taken: "In the second, `vi.fn` ..." became "In the last, ..." ("No último, ..."), since with `it.each` counted as three the fourth test is no longer the second.
* `[^vitest-each]` placed after `[^vitest]` in both editions. Checked on 2026-09-30: the page's title is "Test | Vitest", the anchor `#test-each` exists, and its section says "Alias: it.each".
* The excerpt, docs/03 and the exercises are unchanged.
* Finding F14 of the M4 review is settled.
