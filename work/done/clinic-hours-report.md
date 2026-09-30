# clinic-hours-report

**Objective.** In the guided project, the weekly hours editor's reports, `saving` included, reach the professionals section through one `report` member of `HoursSection` and one professionals event tested in Node, so `forward`, the four report callbacks and the copied comment leave; built by the clinic's own `/propose` and `/apply` and recorded, a fifth recorded clinic run, with no chapter and no tag.

This settles findings 3 and 7 of `m4-code-review`, which the author made one line because they change the same report path. It finishes the clinic's milestone 1.1 line `orchestrator-tests`, which moved every event into a tested plain function but left `forward` and the `saving` report in `useWeeklyHours` with no test. It follows the pattern `clinic-booking-submit` set up (the first occurrence) and `clinic-hours-save` repeated (the second): a recorded run of an M4.1 finding with a brief word for word. This page restates neither. As there, the change keeps the rule the clinic states (no logic left in a hook untested); it does not fix a bug a client has seen.

**Behaviour.**

* In the clinic, `HoursSection` has two members: `report`, which takes a `WeeklyHoursReport`, and `close`, the view's Cancel, unchanged. `saving`, `saved`, `failed` and `refused` leave it.
* `WeeklyHoursReport` includes `saving`. The hook passes every report it gets, from the load and from the save, to `report` as it came; `useWeeklyHours.ts` has no `forward` and no chain that picks a callback by report.
* The professionals section handles every report with one event in `professionalsEvents.ts`, in place of `hoursSaving`, `hoursSaved`, `hoursFailed` and `hoursRefused`; `useProfessionals`' `hours` gives that event to `report` and keeps `close`.
* The section's state after each report is the one it is today: `saving` makes it busy; `saved` closes the row; `failed` keeps the row and ends busy; a refusal shows its message; `ProfessionalNotFound` reloads the list and shows it, and keeps the old list when that reload fails.
* A Vitest test in `professionalsEvents.test.ts`, in Node, drives that one event with each report kind, `saving` included, and the `ProfessionalNotFound` reload. The tests of the four events that leave become tests of the one event and assert the same states. No test drives the hook.
* The comment "What the editor reports to the professionals section..." appears once in `src/`.
* The app behaves as before: every other Vitest test and every Playwright test that existed passes without changing what it asserts, `npm run verify` is green, and the author checks by hand on `npm run dev` that saving a professional's hours closes the row, that a period too short is refused with its message beside it, and that saving the hours of a professional removed meanwhile in a second tab reloads the list with its message.
* The clinic's documents say it: its queue has the line, done; its docs/01 changes only if something it says changes.

**Contract.**

*Before the run.* `clinic-hours-save` runs first and is `[x]` in this book's docs/06, which means `clinic-booking-submit` is too. The clinic is on `main`, clean, equal to `origin/main`, at the last commit `hours-save` left, with focus-kit `bff8414` as installed; the kit is not updated. That commit is checked at run time and written in the record; if `clinic-hours-save` is not done, or the clinic has moved past its record's last commit, /apply stops and asks. This book has other pages in flight; this delivery's /apply stages only its own paths.

*The run.* docs/05 §5, "A recorded clinic run", as `clinic-booking-submit` runs it, with this slug and this brief. The first `/propose` is:

```
claude -p "/propose hours-report" <common flags>
```

followed, in the same session with `--continue`, by this brief, word for word:

```
The weekly hours editor reports to the professionals section through forward, an if-chain in useWeeklyHours that maps a WeeklyHoursReport onto four HoursSection callbacks, and through a saving() call written in the hook; neither has a test, so orchestrator-tests left logic in the hook untested, against its own choice that every event moves. WeeklyHoursReport, forward and the four callbacks say the same thing three times, and the comment "What the editor reports to the professionals section..." is copied in useWeeklyHours.ts and weeklyHoursEvents.ts. Make the reports one path: WeeklyHoursReport includes saving; HoursSection has one report member that takes a WeeklyHoursReport, and keeps close, the Cancel; the hook passes every report to it as it came, so forward leaves; professionalsEvents.ts handles every report with one event in place of hoursSaving, hoursSaved, hoursFailed and hoursRefused, and useProfessionals gives it to report. The section's state after each report stays as it is today, ProfessionalNotFound's reload included; the event may stay async for every report, as hoursRefused is. Test that event in professionalsEvents.test.ts, in Node, with each report kind, saving included; the tests of the four events become tests of the one event and assert the same states. The comment is written once. No test drives the hook, no module mock, no new dependency. Leave saveStarted's shape and the update type as they are: a later delivery declares the starter shape once, and another has docs/01 name every event shape, so do neither here. Say where HoursSection lives and why, and what the hook still decides. The app behaves exactly as before. Add the line to milestone 1.1, just after hours-save and before m1.1-review, saying it finishes what orchestrator-tests left.
```

Every later round of questions, the reviews, a split and the commits: as `clinic-booking-submit`.

*The record,* `work/done/clinic-hours-report-run/`: the format of docs/05 §5, with the brief above in the README and `verify.txt`, `npm run verify` on the clinic's last commit.

*This book's documents, in the same delivery.*

* docs/06: `clinic-hours-report` `[>]` (this /propose), `[x]` by /apply.
* docs/05: unchanged, as `clinic-booking-submit` left it.
* docs/03: no new term.

*Numbers.* None enters the book here.

**Out of scope.**

* `saveStarted`'s shape and declaring the update type and the starter shape once: `clinic-update-type`; `clinic-hours-save` leaves `saveStarted` in `submitStarted`'s shape, and carrying `saving` on it here would part the two starters that line declares as one.
* docs/01 naming every shape an event with a call takes, `{ update, report }` included: `clinic-event-shapes`.
* When a refusal lands: finding 8, rejected; the one event may stay async as `hoursRefused` is.
* A test of the hook: finding 9, rejected; docs/04 tests an orchestrator's events without a DOM.
* Whether a slice may import another slice's code: `slice-imports`, a chapter line; `professionalsEvents.ts` already imports `SectionRefusal` from the weekly hours slice.
* Any chapter text and any tag: chapters 14 to 16 quote the clinic at `book-v1/four-pieces`, which never moves.
* Updating focus-kit in the clinic: the run cites `bff8414`.

**Done when.**

* [x] `clinic-hours-save` was `[x]`, and the clinic clean at its last commit, equal to `origin/main`, before the first run; that commit is in the README.
* [x] The clinic delivery (or each part of a split) ran the five steps, each turn recorded; nothing in the clinic edited by hand.
* [x] On the clinic's last commit, `grep -nE "forward|saving\(\)|saved\(\)|failed\(\)|refused\(" src/features/weeklyHours/useWeeklyHours.ts` finds nothing, `grep -rnE "hoursSaving|hoursSaved|hoursFailed|hoursRefused" src/` finds nothing, and `grep -rn "What the editor reports" src/` finds one line.
* [x] The one event's tests are in `professionalsEvents.test.ts`, every report kind covered, `saving` included; no new dependency in `package.json`.
* [x] The other existing tests pass without changing what they assert; `npm run verify` green on the clinic's last commit, saved as `verify.txt`.
* [x] The author's manual check recorded in the README.
* [x] Each clinic delivery committed by the author, no tag; pushed.
* [x] No note of the host left outside the clinic's repository.
* [x] `work/done/clinic-hours-report-run/` as the Contract says; docs/06 as the Contract says.
* [x] `make verify` green in this book, the disclosure scan included.
* [x] Page in `work/done/`, only this delivery's paths staged, commit message suggested.

**Decisions.** Each taken on the recommended option, not asked:

* The clinic's slug is `hours-report`, the book's slug without `clinic-`, as `hours-save` was.
* The clinic's line goes to its milestone 1.1, after `hours-save` and before `m1.1-review`, and says it finishes what `orchestrator-tests` left.
* This delivery waits for `clinic-hours-save`, since both change `useWeeklyHours`' save; the start commit is whatever `hours-save` leaves, checked at run time.
* `saving` becomes a `WeeklyHoursReport` value, not a field of `saveStarted`'s answer, so the two starters stay alike for `clinic-update-type`. The price: the hook still decides one thing, to report `saving` when the starter says send, and no Node test reaches that line; the author's decision on finding 9 keeps the hook out of the tests, and the page does not claim otherwise.
* `close` stays on `HoursSection`: it is the view's Cancel, not a report.
* The tests of `hoursSaving`, `hoursSaved`, `hoursFailed` and `hoursRefused` change what they call, not what they assert, since those events leave; every other test keeps its assertions.
* The brief leaves to the clinic's agent the event's name, whether it stays async for every report, and where `HoursSection` lives; the agent says what it chose.
* The manual check covers a save, a refused period and a professional removed meanwhile; Playwright covers the rest.
* docs/05 is not edited: the recipe exists and needs no fifth name.

## What happened

* The precondition held: `clinic-hours-save` was `[x]`; the clinic was on `main`, clean, at `13dd9c0`, equal to `origin/main`, with focus-kit `bff8414`.
* One clinic delivery, `hours-report`, four turns: `/propose` (the slug, the brief), `/apply` and one staged review. `/propose` did not split the line and put it in milestone 1.1, after `hours-save` and before `m1.1-review`. Its first turn read the slug as an owner's report of booked hours and asked five questions; the brief answered them, and no later round came, so `Your call` was never sent. The page review was the author's "None", decided before the run.
* The staged review was not "None". `/apply` first made the one event async for every report, as the brief allowed, and said the price: Save disabled one render later, and a very fast double click could send the week twice. The author sent one request, word for word in the run's README, to make `saving`, `saved` and `failed` reach the section at once. So "The app behaves as before" holds for the Save button too.
* The one event is `hoursReported(report, repositories)`: an update at once for `saving`, `saved`, `failed` and `NotSignedIn`, a promise only for `ProfessionalNotFound`, which reloads the list. It answers an update, not a whole state, since the hook cannot read the current state at that moment. `HoursSection` stays in `useWeeklyHours.ts`, a React callback interface, since the events file deals in data.
* The hook still decides four things no Node test reaches, where the Decisions above name one: to report `saving` only when `send` is true, and before the call; to call `report` only when an answer carries one; to drop late answers of the load; and `sectionRef`, still written during render.
* For `clinic-event-shapes`: the clinic's docs/01 did not change, and it describes each event as immediate or waiting; `hoursReported` is both, which the clinic's page records and that delivery names.
* Calls denied: one in `/propose`, a shell command that printed the clinic's documents, read then with the read tool; one in `/apply`, a Python script that rewrote `weeklyHoursEvents.ts`, whose changes the clinic's agent then made with its file tools, a retry by another route inside its session, recorded in the run's README.
* Every `claude` turn ended with a result of `success` but exited with code 1, standard error holding only `stty: stdin isn't a terminal`; recorded in the README.
* The suggested commit message carried no trailer; the author committed the second one, after the staged review, as printed: `9f625cb`, pushed, no tag.
* `npm run verify` green on `9f625cb`: 328 Vitest, where one test of three reports became three tests with the same assertions, 144 Playwright unchanged, build. No `package.json`, view or `*.e2e.ts` in the diff; no module mock.
* The author's manual check on `npm run dev` held, collected at the end of the M4.1 loop on 2026-09-30 on `6edc9ad`, in Chrome driven by Claude in Chrome with the author present: a save, a refused period, and a professional removed in a second tab, which Save hours answered with "This professional no longer exists." and a reloaded list; no console errors.
* No note of the host outside the repositories: the clinic's auto-memory folder stayed empty and no turn wrote into the host's folder, so nothing was deleted. No ADR, no new term; docs/05 unchanged.
