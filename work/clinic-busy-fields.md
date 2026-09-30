# clinic-busy-fields

**Objective.** In the guided project, the weekly hours editor's time inputs and the booking form's name and phone are disabled while a save or a booking is in flight, as the add, remove and submit buttons already are, so the screen shows only what was sent and a successful save closes no unsent edit; built by the clinic's own `/propose` and `/apply` and recorded, an eighth recorded clinic run, with no chapter and no tag.

This settles findings 1 and 2 of `m4.1-code-review`, which the author decided one change settles. It follows the pattern `clinic-booking-submit` set up (the first occurrence) and the other M4.1 clinic runs repeated: a recorded run of a finding with a brief word for word. This page restates none of it. It is the first of M4.2's two clinic lines; `clinic-hours-answer`, which also touches `useWeeklyHours`, runs after this one and starts from this run's last commit.

**Behaviour.**

* In the clinic, `WeeklyHoursView`'s From and To time inputs take `disabled={busy}`, the section's `busy` its buttons already use.
* `BookingView`'s name and phone inputs take `disabled={busy}`, the booking state's `busy` its Book and Back buttons already use.
* So, while the call is in flight, nothing can be typed into those fields: when the answer comes, the screen shows what was sent, and "saved" closes the editor with no unsent edit in it. After "failed", a refusal or `SlotTaken`, `busy` is false again and the fields take input, as the buttons do.
* The two Playwright tests that hold a call in flight with a route never answered, "disables every button of the editor while a save is in flight" in `WeeklyHoursView.e2e.ts` and "disables Book and Back while a booking is in flight" in `BookingView.e2e.ts`, also assert those inputs disabled; their names may say so.
* The Vitest test "sends the checked form and keeps a name typed after the click" in `bookingEvents.test.ts`, and its weekly hours twin "sends the checked week and keeps a time typed after the click" in `weeklyHoursEvents.test.ts`, no longer present an edit typed after the click as correct: each asserts that the in-flight update of a sent call, applied to the state that was checked, keeps what was sent, under a name that says so.
* No event, hook or route changes; every other Vitest and Playwright test passes without changing what it asserts; `npm run verify` is green, and the author checks by hand on `npm run dev` that a save and a booking behave as before.
* The clinic's documents say it: its queue has the line, done; docs/01 changes only if a sentence there stops being true.

**Contract.**

*Before the run.* `clinic-event-shapes` is `[x]` in this book's docs/06, the last clinic run of M4.1. The clinic is on `main`, clean, equal to `origin/main`, at `6edc9ad` ("Name every event shape in docs/01 (event-shapes)"), with focus-kit `bff8414` as installed by `a3e2470`; the kit is not updated. That commit is checked at run time and written in the record; if the clinic has moved past `6edc9ad`, /apply stops and asks. This book has other pages in flight; this delivery's /apply stages only its own paths.

*The run.* docs/05 §5, "A recorded clinic run", as `clinic-booking-submit` runs it, with this slug and this brief. The first `/propose` is:

```
claude -p "/propose busy-fields" <common flags>
```

followed, in the same session with `--continue`, by this brief, word for word:

```
The weekly hours editor's From and To time inputs and the booking form's name and phone inputs stay enabled while a save or a booking is in flight, while the buttons beside them are disabled. So a time typed during a save is shown but not sent, and "saved" closes the editor and drops it without a word; a name or phone changed during a booking is shown but was not booked. Disable those four inputs with busy, the same busy the buttons of each view already use: the section's busy in WeeklyHoursView.tsx, the booking state's busy in BookingView.tsx. Extend the two Playwright tests that hold a call in flight, "disables every button of the editor while a save is in flight" in WeeklyHoursView.e2e.ts and "disables Book and Back while a booking is in flight" in BookingView.e2e.ts, to assert those inputs disabled too; their names may say so. Change the Vitest tests "sends the checked form and keeps a name typed after the click" in bookingEvents.test.ts and "sends the checked week and keeps a time typed after the click" in weeklyHoursEvents.test.ts so they no longer present an edit typed after the click as correct: each asserts what the in-flight update of a sent call does applied to the state that was checked, under a name that says so. Leave the refused-save test and "keeps a name typed in flight through a taken slot" as they are. No event, hook or route changes; the update is still applied to the current state, as docs/01 says, so its sentence "what was typed meanwhile survives" stays: the cancel form and the professionals section still rely on it. Leave the cancel form's and the professionals section's inputs as they are: not this finding. No new dependency. The app behaves as before apart from those four inputs. Say whether any document of this project states which controls a view disables while busy, and change it only if a sentence there stops being true. Add the line to milestone 1.1, just after event-shapes and before m1.1-review.
```

Every later round of questions, the reviews, a split and the commits: as `clinic-booking-submit`.

*The record,* `work/done/clinic-busy-fields-run/`: the format of docs/05 §5, with the brief above and the start commit in the README, and `verify.txt`, `npm run verify` on the clinic's last commit.

*This book's documents, in the same delivery.*

* docs/06: `clinic-busy-fields` `[>]` (marked by the driver of this /propose), `[x]` by /apply. Its text stays.
* docs/05: unchanged, as `clinic-booking-submit` left it.
* docs/03: no new term (guided project, event, orchestrator exist; "in flight" is used as the queue line and the sibling runs use it).

*Numbers.* None enters the book here.

**Out of scope.**

* `WeeklyHoursAnswer`'s report and `"saving"`: `clinic-hours-answer`, finding 4, which runs after this one.
* The cancel form's phone and booking code, and the professionals section's add and rename name inputs: they also stay enabled while busy, but the M4.1 review did not report them and the line names neither; the clinic's `m1.1-review` or `m4.2-review` decides.
* The refused-save test and "keeps a name typed in flight through a taken slot": a refused save sends nothing and the form stays, and after `SlotTaken` the name kept is the one the next booking sends, so neither presents an unsent edit as sent.
* Changing any event, hook or the update rule: docs/01's shapes stay as `clinic-event-shapes` wrote them.
* Any chapter text and any tag: chapters 14 to 16 quote the clinic at `book-v1/four-pieces`, which never moves.
* Updating focus-kit in the clinic: the run cites `bff8414`.

**Done when.**

* [ ] `clinic-event-shapes` was `[x]`, and the clinic clean at `6edc9ad`, equal to `origin/main`, before the first run; that commit is in the README.
* [ ] The clinic delivery (or each part of a split) ran the five steps, each turn recorded; nothing in the clinic edited by hand.
* [ ] On the clinic's last commit, `grep -c "disabled={busy}"` counts two more in `src/features/weeklyHours/WeeklyHoursView.tsx` and two more in `src/features/appointments/BookingView.tsx` than on `6edc9ad`, on the time, name and phone inputs.
* [ ] The two in-flight Playwright tests assert those inputs disabled; `grep -n "keeps a name typed after the click\|keeps a time typed after the click"` finds nothing in `src/` on the clinic's last commit.
* [ ] No file under `src/` other than the two views and the four test files in the diff; no new dependency in `package.json`; `npm run verify` green on the clinic's last commit, saved as `verify.txt`.
* [ ] The author's manual check recorded in the README.
* [ ] Each clinic delivery committed by the author, no tag; pushed.
* [ ] No note of the host left outside the clinic's repository.
* [ ] `work/done/clinic-busy-fields-run/` as the Contract says; docs/06 as the Contract says.
* [ ] `make verify` green in this book, the disclosure scan included.
* [ ] Page in `work/done/`, only this delivery's paths staged, commit message suggested.

**Decisions.** Each taken on the recommended option, not asked:

* The clinic's slug is `busy-fields`, the book's slug without `clinic-`, as `event-shapes` was.
* One clinic delivery for both views, not two: the author decided findings 1 and 2 share one change, and the fix is the same attribute on the same `busy`.
* The clinic's line goes to its milestone 1.1, after `event-shapes` and before `m1.1-review`, since it corrects code of the same milestone's lines.
* The start commit is `6edc9ad`, M4.1's last clinic run; `clinic-hours-answer` runs after this one and starts from this run's last commit, so the two never edit the clinic at once.
* The fix disables the fields, as the line says, and does not change the events: the update applied to the current state stays docs/01's rule, which other forms rely on.
* The weekly hours twin of the booking test changes too, though the line names only the booking one: it presents the same lost edit as correct on the sent path, and leaving it would keep finding 1's claim in the tests.
* The refused-save test and the taken-slot test stay: neither shows an unsent edit as sent.
* The cancel form's and the professionals section's inputs are named out of scope rather than fixed: the line and the review name neither, and the clinic's own review decides.
* The in-flight disabling is proven by Playwright, whose routes hold the call; a real server answers too fast to see it by hand, so the manual check covers only that a save, a refused period and a booking behave as before, collected at the end of the M4.2 loop as M4.1's were.
* docs/05 is not edited: the recipe exists and needs no eighth name.
