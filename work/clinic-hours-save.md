# clinic-hours-save

**Objective.** In the guided project, `useWeeklyHours`' save publishes its in-flight state as an update applied to the current state, as the clinic's docs/01 says, so a time typed or a period added or removed just before Save is kept; built by the clinic's own `/propose` and `/apply` and recorded, a fourth recorded clinic run, with no chapter and no tag.

This settles finding 2 of `m4-code-review`. It is the second occurrence of the pattern `clinic-booking-submit` set up (the first): a recorded run, a brief word for word, the in-flight state published as an update, and the starter's shape chosen by the clinic's agent. This page follows that page and restates none of it. As with finding 1, the author's decision says the code breaks the rule it states; it does not fix a bug a client has seen.

**Behaviour.**

* In the clinic, the weekly hours editor's in-flight state on Save is published with an update applied to the current state (`setState` given a function), in the shape `booking-submit` gave `submitStarted`, and never as a whole state taken from the render closure.
* `saveStarted` still decides, from the state `save` read, whether to send, and which period is refused; `save` still sends that state's periods.
* A Vitest test in `weeklyHoursEvents.test.ts`, in Node, shows that the in-flight update, for a save that is refused and for one that is sent, applied to a state where a time was typed after the click keeps that time. No test drives the hook.
* The app behaves as before: every Vitest and Playwright test that existed passes without changing what it asserts (a `saveStarted` test may reach the state through the starter's shape), `npm run verify` is green, and the author checks by hand on `npm run dev` that the owner saves a professional's hours, that a period too short is refused with its message beside it and nothing is sent, and that the hours read back after a reload are the ones saved.
* The clinic's documents say it: its queue has the line, done; docs/01 changes only if the starter's shape it describes changes.

**Contract.**

*Before the run.* `clinic-booking-submit` runs first and is `[x]` in this book's docs/06. The clinic is on `main`, clean, equal to `origin/main`, at the last commit `booking-submit` left, with focus-kit `bff8414` as installed; the kit is not updated. That commit is checked at run time and written in the record; if `clinic-booking-submit` is not done, or the clinic has moved past its record's last commit, /apply stops and asks. This book has other pages in flight; this delivery's /apply stages only its own paths.

*The run.* docs/05 §5, "A recorded clinic run", as `clinic-booking-submit` runs it, with this slug and this brief. The first `/propose` is:

```
claude -p "/propose hours-save" <common flags>
```

followed, in the same session with `--continue`, by this brief, word for word:

```
useWeeklyHours' save publishes its in-flight state as a whole state, saveStarted(state).state from the render closure, while docs/01 says an event's answer is an update (current) => State, so what was typed meanwhile survives: a time typed or a period added or removed just before Save is lost. Make save follow that rule in the shape booking-submit gave submitStarted, the first occurrence: the in-flight state is published as an update of the current state. saveStarted still decides from the state save read whether to send and which period is refused, and save still sends that state's periods. Add a test in weeklyHoursEvents.test.ts, in Node, that the in-flight update, for a save that is refused and for one that is sent, applied to a state where a time was typed after the click keeps that time. No test drives the hook, no module mock, no new dependency. Leave forward, the section's reports and the update type as they are: later deliveries change them, and a later one declares the starter shape once, so do not do it here. The app behaves exactly as before. Say which shape you followed. Add the line to milestone 1.1, just after booking-submit and before m1.1-review.
```

Every later round of questions, the reviews, a split and the commits: as `clinic-booking-submit`.

*The record,* `work/done/clinic-hours-save-run/`: the format of docs/05 §5, with the brief above in the README and `verify.txt`, `npm run verify` on the clinic's last commit.

*This book's documents, in the same delivery.*

* docs/06: `clinic-hours-save` `[>]` (this /propose), `[x]` by /apply.
* docs/05: unchanged, as `clinic-booking-submit` left it.
* docs/03: no new term.

*Numbers.* None enters the book here.

**Out of scope.**

* `useBooking`'s submit: `clinic-booking-submit`, the first occurrence, already built when this runs.
* `forward`, `HoursSection`'s callbacks and the `saving` report: `clinic-hours-report`.
* Declaring the update type and the starter shape once: `clinic-update-type`, which names `submitStarted` as the first occurrence and `saveStarted` as the second.
* docs/01 naming every shape an event with a call takes, `{ update, report }` included: `clinic-event-shapes`.
* Any chapter text and any tag: no chapter quotes `useWeeklyHours`' save, and chapters 14 to 16 quote the clinic at `book-v1/four-pieces`, which never moves.
* Sending the periods typed after the click: the save sends what was on screen when Save was pressed; what came after stays in the editor.
* A test of the hook: finding 9, rejected; docs/04 tests an orchestrator's events without a DOM.
* Updating focus-kit in the clinic: the run cites `bff8414`.

**Done when.**

* [ ] `clinic-booking-submit` was `[x]`, and the clinic clean at its last commit, equal to `origin/main`, before the first run; that commit is in the README.
* [ ] The clinic delivery (or each part of a split) ran the five steps, each turn recorded; nothing in the clinic edited by hand.
* [ ] `grep -n "setState(started.state)" src/features/weeklyHours/useWeeklyHours.ts` finds nothing on the clinic's last commit, and the in-flight state is set with a function there, in `submitStarted`'s shape.
* [ ] The new test is in `weeklyHoursEvents.test.ts`; no new dependency in `package.json`.
* [ ] The existing tests pass without changing what they assert; `npm run verify` green on the clinic's last commit, saved as `verify.txt`.
* [ ] The author's manual check recorded in the README.
* [ ] Each clinic delivery committed by the author, no tag; pushed.
* [ ] No note of the host left outside the clinic's repository.
* [ ] `work/done/clinic-hours-save-run/` as the Contract says; docs/06 as the Contract says.
* [ ] `make verify` green in this book, the disclosure scan included.
* [ ] Page in `work/done/`, only this delivery's paths staged, commit message suggested.

**Decisions.** Each taken on the recommended option, not asked:

* The clinic's slug is `hours-save`, the book's slug without `clinic-`, as `booking-submit` was.
* The clinic's line goes to its milestone 1.1, after `booking-submit` and before `m1.1-review`, since it corrects code of the same `orchestrator-tests` line.
* This delivery waits for `clinic-booking-submit` and follows the shape it gave `submitStarted`, so the two starters stay alike until `clinic-update-type` declares one; the brief names that shape instead of leaving it open.
* The start commit is not written here: it is whatever `booking-submit` leaves, checked at run time.
* The test covers both starters' outcomes, refused and sent, because `saveStarted` builds the in-flight state in two places.
* `save` keeps sending the periods it read at the click, as `booking-submit` books with the state it read.
* The manual check covers a save, a refused period and a reload; the section's messages are `clinic-hours-report`'s.
* docs/05 is not edited: the recipe exists and needs no fourth name.
