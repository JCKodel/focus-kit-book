# testing-and-agents

**Objective.** After chapter 16 the reader can say which test guards each FOCUS piece and why that test needs no mock but the clock, follow one rule of the clinic through a test at every level, and say, with the clinic's own record, how a slice and its tests keep an agent's reading small and tell it when it is done.

**Behaviour.**

* The reader can name, for each piece, the test that guards it in the clinic and what that test swaps: a use case gets its data and `now` and swaps nothing; a repository runs against an in-memory SQLite with the real migrations; the server orchestrator is driven through `app.request` with that database and a fake clock; the phone's storage (`remembered.ts`) gets a fake `localStorage`; the network (`api.ts`) is guarded through the shared `request`, tested with a fake `fetch`; the view and the client orchestrator are driven in a browser by Playwright.
* The reader can follow the 24-hour cancellation rule through four tests, the use case, the repository, the route and the screen, and say what each asserts that the others do not.
* The reader can say why the route's test fakes the clock and the use case's test does not: the route is the piece that reads `new Date()` and hands it on, so the rule's test passes time as data (chapter 15's "one event, one new state" as one test, as chapter 15 promised).
* The reader can say what has no test of its own in the clinic, the client orchestrators (`useBooking.ts`, `useCancel.ts`) and the network repositories (`api.ts`), why that is tolerable today (they hold no rule; `request` has its tests; the end-to-end tests drive them) and why it is a candidate for the clinic's queue, not a fix now.
* The reader can say, from the clinic's run record, how many files of `src/` the agent read to build a delivery inside the appointments slice, how many of them were in that slice, what it read to start a new slice (a sibling slice as its model), and that it ran the slice's tests alone before the whole verify (chapter 14's promise that the slice bounds what an agent reads).

**Contract.**

Chapter 16, `book/en/16-testing-and-agents.md` and `book/pt/16-testing-and-agents.md`:

* Title: "Testing, and FOCUS with agents" / "Testes, e FOCUS com agentes" (docs/00 §Contents). No part heading, as chapters 14 and 15.
* Voice: instruction to the reader as "you" (docs/04 §Voice).
* Sections, in order (headings may be reworded; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. A test for each piece. The clinic's test table, "Level | Tool | What", from its docs/04 §Tests, linked at the tag (the Portuguese edition translates it and says before it that the original is in English, docs/04 §Evidence), then the clinic's rule quoted: "Every rule has a test. A rule without a test is not done." One sentence each on Vitest (runs a unit test in Node, no browser) and Playwright (drives the app in a browser), with their notes. The two docs/03 terms, unit test and end-to-end test, are said here, with `.test.ts` and `.e2e.ts` pointed back to chapter 14.
  3. One rule, four tests. The rule: a client cancels up to 24 hours before the start (the clinic's `cancel`, chapter 14's exercise 14.2 pointed to, not repeated). Excerpts, each with its path and a link at the tag, in this order:
     * `rules.test.ts`: `describe("cancel", ...)`, whole with its comment (the use case: `now` passed as data; one millisecond before, at and after the deadline; no database, no mock; the helper `at` named, not shown).
     * `testDatabase.server.ts`: `memoryDatabase`, whole with its comment (the one swap the server needs: an in-memory SQLite with the real migrations).
     * `repository.server.test.ts`: `it("cancels once, keeping the row, and frees the slot", ...)`, whole (the repository against that database: the row stays `cancelled` and the slot is free for the next insert).
     * `route.server.test.ts`: from the comment `// Monday 28 September 2026, 01:00 in Lisbon.` to the end of `afterEach`, whole, `setUpClinic` included (the fake clock by `vi.useFakeTimers({ toFake: ["Date"] })`, `memoryDatabase`, `appointmentsRoute(db)` mounted in a `Hono` app), then `it("cancels at the deadline, and answers 409 one millisecond later, keeping it booked", ...)`, whole. Said: one event, one request, and one new state, the answer and the rows; this is chapter 15's `appointmentsRoute(db)` and `app.request` (chapter 15, pointed to). Said: the route fakes the clock because it is the piece that reads `new Date()`, after the clinic's docs/01 bullet chapter 15 quoted, pointed to.
     * `CancelView.e2e.ts`: `test("an appointment under 24 hours away is refused by the typed form, and shows no Cancel when remembered", ...)`, whole (the view and the client orchestrator in a browser; the helpers it calls named, not shown).
     Then two sentences on what each level adds: the use case proves the boundary to the millisecond, the repository that the row is kept, the route that the server refuses and changes nothing, the screen that the client sees why.
  4. The client's I/O. `remembered.test.ts`: the `let stored`, `beforeEach` and `afterEach`, whole (the phone's storage with `localStorage` replaced by a `Map` through `vi.stubGlobal`). `src/lib/request.test.ts`: the names of its `it`s under `describe("request")`, listed, no body (the network through one shared function, `fetch` faked: a refusal named by status, `ServerUnreachable` for anything else). One sentence: on the client, as on the server, only the I/O is swapped.
  5. What has no test of its own. `useBooking.ts` and `useCancel.ts`, the client orchestrators, and each feature's `api.ts`, the network repositories, have no `.test.ts`, and the clinic's table has no row for them. They hold no rule, since the rules are in `rules.ts`; `api.ts` only names which status is which refusal, over `request`, which is tested; the end-to-end tests drive them all. Told as a gap the reader can find with the agent, a candidate for the clinic's queue, not a fix now, as chapter 15 told `session.server.ts`. The clinic does not change.
  6. How many. The counts of the clinic's `npm run verify` at the last commit of its milestone 1, from the record's `verify.txt`: 25 Vitest files, 238 tests; 144 Playwright runs, which count the owner screens' tests twice, once per viewport (the clinic's docs/04 §Tests), with the number of distinct Playwright tests counted by /apply at the tag; the durations only if `verify.txt` prints them. Said: the tag `book-v1/closing-a-milestone` (`c54d011`) differs from that commit (`f16f83b`) only in docs/06, so the counts hold at the tag.
  7. What the slice gives an agent. From the clinic's run record, `work/done/clinic-milestone-1-run/` of this repository, counted by script:
     * `cancel-appointment`, a delivery inside an existing slice: the files of `src/` its `/apply` turn read, how many were in `src/features/appointments/`, against the files of `src/` at that delivery's parent commit (95 at `442f88a`).
     * `book-appointment`, a new slice: the same counts against its parent commit, and the files of `src/features/weeklyHours/` it read, named as the sibling slice it took as its model.
     * The slice's tests run alone: the `npx vitest run src/features/appointments` and `npx playwright test src/features/appointments` calls of those turns, before `npm run verify`.
     Counting rule, in one sentence of prose, with the note only linking the record: distinct paths under `src/` whose contents the `/apply` turn read, by a `Read` call or a shell call that prints a file (`cat`, `sed -n`, `head`, `tail`); a `grep` or an `ls` is not a read; a denied call read nothing; the `/apply` turn is the one the record's README names for that delivery; the total is `git ls-tree -r --name-only <parent> src`. Then the link to chapter 2 (context window and context rot, pointed to): fewer files read is less context. And the person's part: a test's name is a sentence of the rule ("is too late one millisecond after the deadline"), so reviewing an agent's staged tests starts by reading their names (chapter 11's review, pointed to).
  8. Key points, at most five, one of them: a test swaps only I/O and the clock, because only the repositories do I/O and only the orchestrators read the clock.
  9. Exercises (below).
* Code: TypeScript, byte for byte from the clinic at `book-v1/closing-a-milestone` (`c54d011`), identical in both editions, comments included, outer indentation removed as docs/04 §Writing the book says, fence `ts`. The docs/04 table and rule are prose artifacts: byte for byte in English, translated in Portuguese. The guided project does not change: no run, no new tag.
* Numbers, and only these: the statuses the excerpts show; the 24 hours and the millisecond of the rule; the counts of section 6 from `verify.txt`, and the distinct Playwright tests counted at the tag; the counts of section 7 from the record, by the rule above; 95 and 442f88a checked again by the script.
* docs/03 terms: introduced: unit test, end-to-end test (added by this /propose). Used: view, orchestrator, use case, repository, driver, event, state, refusal, Result, vertical slice, guided project, chapter tag, context window, context rot, verify, stage.
* Sources (`[^key]`, same keys in both editions):
  * `[^vitest]`: Vitest, the documentation's guide, accessed on the day of writing, <https://vitest.dev/guide/>.
  * `[^playwright]`: Playwright, the documentation, accessed on the day of writing, <https://playwright.dev/docs/intro>.
  * `[^clinic-milestone-1-run]`: this book's record of the clinic's milestone 1, `work/done/clinic-milestone-1-run/`, on `main`.
  * The clinic's files and docs are linked in the text at the tag, with no note (docs/04).
* Exercises, on the clinic, by conversation with the agent, never by hand:
  * 16.1 Ask the agent which tests guard the rule that a client's name has at most 80 characters, at every level, and to run only those. Compare what it ran with what `npm run verify` runs.
  * 16.2 Take exercise 15.2's rule, at most two future appointments per client. Ask the agent which test files change, and what each new test asserts, at each level. Nothing is built.
  * 16.3 In a fresh session, ask the agent which files it would read to add a delivery in which the owner sees the day's appointments, and why. Compare its list with the slices it names and with the counts of section 7. Nothing is built.
* Documents: docs/03 gains unit test and end-to-end test (this /propose). The Portuguese of chapter 14, line 51, says "testes unitários" in place of "testes de unidade", so the term is one from chapter 8 on (chapter 8 already says "testes ponta a ponta", chapter 11 "testes unitários"). docs/06: `testing-and-agents` `[>]` (this /propose), `[x]` by /apply. docs/00 §Contents already names chapter 16. The page's What happened records the exercise answers for the `exercise-answers` appendix and the counts with the script's output.

**Out of scope.**

* Writing a test for `useBooking.ts`, `useCancel.ts` or an `api.ts`, or any change to the clinic: the gap is named, a new tag costs more than it teaches.
* A new agent run to show what it reads: the record already holds two `/apply` turns.
* Coverage percentages, test-first as a doctrine, the testing pyramid as theory: the chapter shows the clinic's four levels and what each proves.
* Mock libraries and dependency-injection frameworks: the clinic swaps only the database, `localStorage`, `fetch` and the clock.
* Every other rule and slice: one rule followed through every level carries the idea; exercise 16.1 takes a second.
* Parallel agents: Part IV.
* The queue listing of chapter 9, which shows this line as `[ ]`: it is a snapshot of that day.
* Ninjobs: no case is needed, and FOCUS is never told as a warning.
* Examples in other languages (ADR-0008).

**Done when.**

* [x] Both editions written, same file name and heading structure, opening with the Objective in at most three sentences; no draft marker.
* [x] No filler and nothing useful cut; every number cites its source.
* [x] Every code excerpt matches `git show c54d011:<path>` byte for byte once its outer indentation is put back, checked by script, in both editions; the English docs/04 excerpts match too.
* [x] The counts of section 7 produced by a script over the record with the rule above, its output in What happened.
* [x] Chapter 14's Portuguese uses "testes unitários".
* [x] `make verify` green, the link check and the disclosure scan included.
* [x] `make book` builds; both PDF paths given to the author.
* [x] docs/06 line `[x]`, page in `work/done/`, staged, commit message suggested.

**What happened.**

* Written as the Contract says, in both editions, with no draft marker. Sections 2 to 7 are H2 sections; the four tests of section 3 are bold labels, as chapter 15's steps.
* Section 3: `memoryDatabase` is shown whole, as the page asks, though chapter 14 already showed it; the chapter says so, pointed to. Every excerpt names its helpers without showing them, not only the end-to-end one: `at` (rules), `appointment` and `rows` (repository), `booked`, `valid`, `postCancel`, `expectError`, `statuses` (route), and the file's and slice's helpers (screen). The route's test runs `deadline + 1` (409) before `deadline` (200), the reverse of its title; the prose follows the code's order.
* Diverged from the page, section 3: exercise 14.2 is linked at chapter 14's `#exercises`. `#exercise-142` passed the site build, but `make book` failed to resolve it (pandoc keeps the dot of `14.2` in the id); the section anchor resolves in both.
* Diverged from the page, section 5: the page names `useBooking.ts` and `useCancel.ts`; at the tag no client orchestrator has a test, `useRemembered.ts` in the same slice included, and none of the six `api.ts`. The chapter says "the hooks `use<Feature>.ts`" and names the slice's three. The page's "as chapter 15 told `session.server.ts`" has no match in chapter 15's text (only in `four-pieces`'s exercise answers), so the chapter points to exercise 15.1 ("a candidate for your queue, not a fix now").
* Section 6: `verify.txt` prints durations, so they are in: Vitest `Duration 1.10s`, Playwright `144 passed (21.0s)`. The 91 distinct Playwright tests are the lines starting `test(` in the seven `.e2e.ts` files at `c54d011` (BookingView 16, CancelView 13, ClinicView 5, HealthView 4, ProfessionalsView 22, OwnerView 13, WeeklyHoursView 18); the 53 run twice are OwnerView, ProfessionalsView and WeeklyHoursView; 91 + 53 = 144, and `verify.txt` shows 91 `[phone]` and 53 `[desktop]` lines. The 25 Vitest files equal the `.test.ts` files at the tag. `git diff --stat f16f83b c54d011` shows only `docs/06-Queue.md`.
* Section 7, the counting rule gained one clause: "that existed at the delivery's parent commit". The `book-appointment` turn read two files it had written itself (`BookingView.tsx`, `BookingView.e2e.ts`); without the clause the count is not a part of the parent's total. Denied calls come from the record's README; the only ones that would read `src/` are the shell loops (turn 3 of `cancel-appointment`, line 5; turn 4 of `book-appointment`, lines 13 and 15), which the script skips.
* Section 7, the commands are the record's, not the page's: `cancel-appointment` ran `npx playwright test --project=phone src/features/appointments`, and `book-appointment` ran `npx playwright test src/features/appointments src/features/clinic` and then `--repeat-each=3`, before `npm run verify`. "The sibling slice as its model" is the agent's own sentence, quoted: "I've studied the `weeklyHours` slice to use as the pattern." (turn 4, line 89); the Portuguese edition gives it in English and then its translation.
* The counting script, outside the repository (not a check of `make verify`: it names no error that happened), parsed each `[tool Read]` and `[tool Bash]` line of the two turns and `git ls-tree` in the clinic. Its output, without the file lists:

  ```
  == cancel-appointment, /apply turn-3.txt, commit f16f83b, parent 442f88a
  src/ files at parent: 95
  denied shell loops skipped at lines: [5]
  read, existing at parent: 20
    in src/features/appointments/: 15
  read, not at parent (written by the turn itself): []
  test and verify runs, in order:
    line 89: npx vitest run src/features/appointments
    line 149: npx playwright test --project=phone src/features/appointments
    lines 155, 181, 195: npx playwright test --project=phone src/features/appointments/Shots.e2e.ts
    line 219: npm run verify
    line 223: npx playwright test --project=phone src/features/appointments/CancelView.e2e.ts --repeat-each=3

  == book-appointment, /apply turn-4.txt, commit 442f88a, parent afc833a
  src/ files at parent: 77
  denied shell loops skipped at lines: [13, 15]
  read, existing at parent: 33
    in src/features/appointments/: 0
    in src/features/weeklyHours/: 9
  read, not at parent (written by the turn itself): [BookingView.e2e.ts, BookingView.tsx]
  test and verify runs, in order:
    line 151: npx vitest run src/features/appointments
    line 177: npx playwright test src/features/appointments src/features/clinic
    line 187: npx playwright test src/features/appointments --repeat-each=3
    line 191: npm run verify
  ```

  `cancel-appointment` read 15 of the slice's 17 files (not `clinicTime.ts` and its test) and five outside: `src/app/main.tsx`, `src/lib/request.ts`, `src/lib/result.ts`, `src/server/database.server.ts`, `src/features/professionals/repository.server.ts`. `book-appointment` read 9 of `weeklyHours`'s 11, 7 of `professionals`, 6 of `clinic`, 1 of `health`, 4 of `src/lib/`, 5 of `src/server/` and `src/app/main.tsx`.
* The byte check: a script outside the repository took every `ts` block of both editions, put back 0 to 7 tabs, and found it as a substring of `git show c54d011:<path>`, the path taken from the last clinic link before the block: all 7 blocks passed in each edition (the route's `it` at 1 tab, the rest at 0), and the blocks of the two editions are identical. The English table's five lines are lines of the clinic's docs/04, the rule sentence is in it, and the docs/01 quotation matches once line breaks are collapsed. The six `request.test.ts` names are the file's `it` strings.
* Notes: `[^vitest]` and `[^playwright]` carry the pages' titles, "Getting Started" and "Installation"; `[^clinic-milestone-1-run]` links the record's folder with `tree/`, since the counts come from `verify.txt` and the turn files, not the README alone.
* Numbers in the prose: 24 hours, one millisecond, 409, 200; 25, 238, 1.10 s, 144, 21.0 s from `verify.txt`; 91 and 53 counted at the tag; 390×844 and 1280×800 from the clinic's docs/04; 20 of 95, 15, 17, 33 of 77, 9 from the script; the dates and times of the excerpts.
* Proof: `make verify` green, the link check and the disclosure scan included; `make book` built both editions with no error. No screenshot: tables, TypeScript blocks and quotations rendered before (docs/05 §5).
* Chapter 14's Portuguese, line 51, says "testes unitários".
* Exercise answers, for the `exercise-answers` appendix:
  * 16.1: the client's name uses `checkName` of `src/lib/name.ts` through `checkClientName` in `appointments/rules.ts`. The tests: `src/lib/name.test.ts` ("accepts 80 characters and refuses 81", and the trimming and character-count tests); `appointments/rules.test.ts`, under `book`, "refuses a blank name and one of 81 characters"; `appointments/route.server.test.ts`, the two `InvalidClientName` rows of "answers each refusal of the use case, storing nothing" and "checks the body, then the professional, then the rule"; `appointments/BookingView.e2e.ts`, "refuses a bad name and a bad phone beside the field, sending nothing" (a blank name; no 81 at the screen). No repository test: the column's comment says 80, but the repository holds no rule. The professionals' and the clinic's 80-character tests guard other names. Run alone: `npx vitest run src/lib/name.test.ts src/features/appointments/rules.test.ts src/features/appointments/route.server.test.ts` (or with `-t`) and `npx playwright test src/features/appointments/BookingView.e2e.ts -g "refuses a bad name"`; `npm run verify` runs typecheck, lint, all 25 Vitest files, all 144 Playwright runs and the build.
  * 16.2: `appointments/rules.test.ts`: the new use case (say `checkClientLimit`) accepts a second future appointment and refuses a third, counts only starts after `now` (passed as data), and `book` returns its refusal after the phone. `appointments/repository.server.test.ts`: the new query returns only `booked` rows, only after the instant given, only for those phone digits. `appointments/route.server.test.ts`: a third booking for the same phone answers the refusal's status (not 409, which `api.ts` reads as `SlotTaken`) and stores nothing; a cancelled one frees a place; the fake clock makes "future" exact. `appointments/BookingView.e2e.ts`: the form step shows the message and keeps what was typed. Unchanged: `request.test.ts`, `remembered.test.ts`, the cancel tests; `api.ts` gains a status with no test of its own, the gap of section 5.
  * 16.3: the owner screen is `signIn/OwnerView.tsx`, which places `ProfessionalsView`; the day's list is read on the server by an owner-only route. Expected reads: the appointments slice (`repository.server.ts` for a query by day, `route.server.ts`, `clinicTime.ts` for the day in the clinic's time zone, `strings.ts`, `rules.ts` if a rule appears), `professionals` as the model of an owner-only slice (its route behind `requireSession`, its hook, view and e2e with `signIn` of `e2eClinic.server.ts`), `signIn/OwnerView.tsx`, `src/server/session.server.ts` and `main.server.ts`, and `src/lib/request.ts` and `result.ts`. The count should fall between the 20 of a delivery inside one slice and the 33 of a new one, since it adds to one slice and copies the owner pattern of another.
* Documents: docs/03 gained unit test and end-to-end test (this /propose); docs/06 line `[x]`. No ADR, and no rule changed.
