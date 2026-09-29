# clinic-booking-submit

**Objective.** In the guided project, `useBooking`'s submit publishes its in-flight state as an update applied to the current state, as the clinic's docs/01 says, and the hook passes the state it books with into `run`, so the `shown` ref written during render leaves; built by the clinic's own `/propose` and `/apply` and recorded, a third recorded clinic run, with no chapter and no tag.

This settles findings 1 and 6 of `m4-code-review`, which the author made one line because they change the same lines of `useBooking.ts`. The author's decision on finding 1 says no click reaches the overwrite today: the change keeps the rule docs/01 states, it does not fix a bug a client has seen.

**Behaviour.**

* In the clinic, the booking's in-flight state is published with an update applied to the current state (`setState` given a function), as loading the professionals and the slots already are in the same hook (the first occurrence), and never as a whole state taken from an earlier render.
* Every path that runs a booking, the view's `submit` and "Try again" after a failed booking, passes the state it read into `run`; the booking sends that state, and `submitStarted` decides from it whether to send.
* `useBooking.ts` has no `shown` ref and writes no ref during render; `latest` and what it guards stay as they are.
* A Vitest test in `bookingEvents.test.ts`, in Node, shows that the booking's in-flight update applied to a state changed after the click (a name typed meanwhile) keeps that change. No test drives the hook.
* The app behaves as before: every Vitest and Playwright test that existed passes without changing what it asserts, `npm run verify` is green, and the author checks by hand on `npm run dev` that a client books a time, that an empty name is refused with its message and nothing is sent, and that the booking code is shown after a booking.
* The clinic's documents say it: its queue has the line, done; docs/01 changes only if the starter's shape it describes changes.

**Contract.**

*Before the run.* The clinic is on `main`, clean, at `a3e2470` ("Update focus-kit to bff8414"), equal to `origin/main`, with focus-kit `bff8414` as installed; the kit is not updated. If the clinic has moved past `a3e2470` when /apply starts, /apply stops and asks. This book has other pages in flight; this delivery's /apply stages only its own paths.

*The run.* docs/05 §5, "A recorded clinic run": its five steps, common flags, `/apply` allowlist, exits and record, unchanged; this is its third occurrence. The first `/propose` is:

```
claude -p "/propose booking-submit" <common flags>
```

followed, in the same session with `--continue`, by this brief, word for word:

```
useBooking's submit publishes its in-flight state as a whole state taken from the ref shown, written during render, while docs/01 says an event's answer is an update (current) => State, so what was typed meanwhile survives, and the hook already publishes loadSlotsStarted and loadProfessionalsStarted that way. Make submit follow that rule: the in-flight state is published as an update of the current state, and the hook's submit and retry pass the state they read into run, which books with it, so shown leaves. submitStarted still decides from that state whether to send. Add a test in bookingEvents.test.ts, in Node, that the in-flight update applied to a state where a name was typed after the click keeps that name. No test drives the hook, no module mock, no new dependency. The shape you give the starter is the first occurrence: useWeeklyHours' save will follow it in a later delivery, and a later one declares the shape once, so do neither here; say what shape you chose and why. The app behaves exactly as before. Add the line to milestone 1.1, just before m1.1-review.
```

Every later round of questions is answered `Your call. Say what you chose and why.` The page review and the staged review are the author's, word for word. If the clinic's `/propose` splits the line, every part lands in this delivery, each with the five steps. The author commits each clinic delivery with the kit's message and no tag, and pushes.

*The record,* `work/done/clinic-booking-submit-run/`: the format of docs/05 §5, with the brief above in the README and `verify.txt`, `npm run verify` on the clinic's last commit.

*This book's documents, in the same delivery.*

* docs/06: `clinic-booking-submit` `[>]` (this /propose), `[x]` by /apply.
* docs/05: unchanged; the recipe already names its first two occurrences, and a third adds nothing to it.
* docs/03: no new term (orchestrator, event, guided project exist).

*Numbers.* None enters the book here.

**Out of scope.**

* `useWeeklyHours`' save: `clinic-hours-save`, which names this delivery's starter as the first occurrence.
* The weekly hours editor's reports: `clinic-hours-report`.
* Declaring the update type and the starter shape once: `clinic-update-type`.
* docs/01 naming every shape an event with a call takes: `clinic-event-shapes`.
* Any chapter text and any tag: chapters 14 to 16 quote the clinic at `book-v1/four-pieces`, which never moves, so `ch15-submit-event` stays true and the two land in either order; this settles the "for later" note of `m4-code-review`. Explaining the new code belongs to the chapter that next tags the clinic.
* A test of the hook or its `run`: finding 9, rejected; docs/04 tests an orchestrator's events without a DOM.
* The clinic's other milestone 1.1 lines: not this finding.
* Updating focus-kit in the clinic: the run cites `bff8414`.

**Done when.**

* [ ] The clinic was clean at `a3e2470`, equal to `origin/main`, before the first run.
* [ ] The clinic delivery (or each part of a split) ran the five steps, each turn recorded; nothing in the clinic edited by hand.
* [ ] `grep -n "shown" src/features/appointments/useBooking.ts` finds nothing on the clinic's last commit, and the booking's in-flight state is set with a function there.
* [ ] The new test is in `bookingEvents.test.ts`; no new dependency in `package.json`.
* [ ] The existing tests pass without changing what they assert; `npm run verify` green on the clinic's last commit, saved as `verify.txt`.
* [ ] The author's manual check recorded in the README.
* [ ] Each clinic delivery committed by the author, no tag; pushed.
* [ ] No note of the host left outside the clinic's repository.
* [ ] `work/done/clinic-booking-submit-run/` as the Contract says; docs/06 as the Contract says.
* [ ] `make verify` green in this book, the disclosure scan included.
* [ ] Page in `work/done/`, only this delivery's paths staged, commit message suggested.

**Decisions.** Each taken on the recommended option, not asked:

* The clinic's slug is `booking-submit`, the book's slug without `clinic-`, as `orchestrator-tests` was.
* The clinic's line goes to its milestone 1.1, before `m1.1-review`, since it corrects code of that milestone's `orchestrator-tests`.
* The brief states outcomes and leaves the starter's shape to the clinic's agent, as the brief of `clinic-orchestrator-tests` did; the agent says what it chose.
* The proof of the update is a Node test of the event functions only, not of the hook, following the author's decision on finding 9.
* The manual check covers a booking, a refused empty name and the booking code shown; cancelling is not touched.
* docs/05 is not edited: the recipe exists and needs no third name.
