# clinic-event-shapes

**Objective.** In the guided project, the clinic's docs/01 names every shape an event of a `<name>Events.ts` file takes, each with when it is used and the file of its first occurrence, as the code stands once the four earlier M4.1 clinic lines are done; built by the clinic's own `/propose` and `/apply` and recorded, a seventh recorded clinic run, with no chapter and no tag.

This settles finding 4 of `m4-code-review`. It follows the pattern `clinic-booking-submit` set up (the first occurrence) and `clinic-hours-save`, `clinic-hours-report` and `clinic-update-type` repeated: a recorded run of an M4.1 finding with a brief word for word. This page restates none of it. Those four runs set the shapes; this one only writes down the ones they leave. The change is to the clinic's docs/01 only: no code, no test, nothing a client or the owner sees.

**Behaviour.**

* In the clinic, docs/01 no longer gives one shape of an event with a call as the rule: it names every shape the inventory below finds on the start commit, each with when it is used and the file that holds its first occurrence.
* Every event of every `src/features/*/*Events.ts` file on the clinic's last commit takes a shape docs/01 names.
* No file in `src/` changes; no test is added or changed; `npm run verify` is green.
* The clinic's documents say it: its queue has the line, done; its docs/01 is the one document that changes besides the queue.

**Contract.**

*Before the run.* `clinic-update-type` runs first and is `[x]` in this book's docs/06, which means `clinic-booking-submit`, `clinic-hours-save` and `clinic-hours-report` are too. The clinic is on `main`, clean, equal to `origin/main`, at the last commit `update-type` left, with focus-kit `bff8414` as installed; the kit is not updated. That commit is checked at run time and written in the record; if `clinic-update-type` is not done, or the clinic has moved past its record's last commit, /apply stops and asks. This book has other pages in flight; this delivery's /apply stages only its own paths.

*The inventory.* Taken on the start commit, from the clinic's root, and written in the README:

```
grep -nE "^export (async )?function" src/features/*/*Events.ts
```

lists every exported function; each one's parameters and return type are read from its file, and the functions are grouped by shape. A function that works out a value to show (`daysOf`, `tooLateToCancel`, `linesOf`) is not an event and is listed apart. On `a3e2470`, before the four earlier runs, the inventory finds seven shapes; the expected set on the start commit is the same seven, as those runs leave them:

1. No call: `(state, ...inputs) => State`, or `(...inputs) => State` when the result does not depend on the state (`cancelEvents.ts`' `open` and `close`, `ownerEvents.ts`' `submitSignInStarted` and `submitSignOutStarted`).
2. A call with a starter: `<event>Started(state, ...inputs) => State`, then `<event>(...inputs, now?, repositories)` resolving to the update (`cancelEvents.ts`' `submit`, `rememberedEvents.ts`' `confirm`, `professionalsEvents.ts`' `add`, `rename` and `remove`, `ownerEvents.ts`' `submitSignIn` and `submitSignOut`); after `clinic-update-type`, spelled with the shared update type.
3. A load at mount with no starter, the initial state being the in-flight one (`clinicEvents.ts`' `load`, `healthEvents.ts`' `check`, `professionalsEvents.ts`' `load`, `ownerEvents.ts`' `checkSession`, `weeklyHoursEvents.ts`' `load`). Neither docs/01 nor finding 4 names it.
4. A starter that decides whether to send, `{ state; send: boolean }` today (`submitStarted` in `bookingEvents.ts`, `saveStarted` in `weeklyHoursEvents.ts`); after `clinic-update-type`, the shared starter type it declares.
5. An answer that may be the next event: `BookingOutcome`, an update or a `BookingNext` the hook runs next, and `retryOf(state)` returning a `BookingNext`; `submit` books with the state the starter accepted, as `clinic-booking-submit` leaves it.
6. An answer that carries a report to another section: `WeeklyHoursAnswer`, `{ update, report? }`; after `clinic-hours-report`, `WeeklyHoursReport` includes `saving` and the professionals section takes every report with one event.
7. A call that does not wait: `initialRememberedState(now, repositories)` and `reread(state, now, repositories)`, plain functions.

The docs/06 line names three shapes docs/01 lacks; the inventory also finds shape 3 and shape 1 without the state. The line's text stays; the record says what the inventory found. If the start commit shows a shape this set and the four runs do not account for, docs/01 names it too and the README says it was not expected; a shape that left changes nothing. The brief carries the method and this set as a floor, so a moved set changes nothing in it.

*The run.* docs/05 §5, "A recorded clinic run", as `clinic-booking-submit` runs it, with this slug and this brief. The first `/propose` is:

```
claude -p "/propose event-shapes" <common flags>
```

followed, in the same session with `--continue`, by this brief, word for word:

```
docs/01 gives one shape for an event with a call, a Started function and an update (current) => State, while the events files use more, written only in work/done, so the next person who follows docs/01 for an orchestrator gets a shape the booking and the weekly hours contradict. AGENTS.md says documents are living and that an abstraction names its first occurrence. Make docs/01 name every shape an event takes. Find them this way: grep -nE "^export (async )?function" src/features/*/*Events.ts, read each function's parameters and return type, and group them; a function that works out a value to show, such as daysOf or linesOf, is not an event. Expect at least these, and name every one you find: an event with no call, with or without the state; a call with a Started and an update; a load at mount with no Started, whose in-flight state is the initial one; the starter that decides whether to send, as update-type declared it; the booking's answer that may be the next event, BookingOutcome and BookingNext, with retryOf; the weekly hours' answer that carries a report, { update, report }; and the remembered list's plain functions, a call that does not wait. For each shape, say when it is used and which file holds its first occurrence. Documentation only: no file in src/ changes, no test, no new dependency. Say where in docs/01 you put it and why. Add the line to milestone 1.1, just after update-type and before m1.1-review, saying docs/01 names every event shape the code uses.
```

Every later round of questions, the reviews, a split and the commits: as `clinic-booking-submit`.

*The record,* `work/done/clinic-event-shapes-run/`: the format of docs/05 §5, with the brief above and the inventory on the start commit (the list and its groups) in the README, and `verify.txt`, `npm run verify` on the clinic's last commit.

*This book's documents, in the same delivery.*

* docs/06: `clinic-event-shapes` `[>]` (this /propose), `[x]` by /apply. Its text keeps its three shapes: the line records what the review said, and the record says what the inventory found.
* docs/05: unchanged, as `clinic-booking-submit` left it.
* docs/03: no new term (event, orchestrator, guided project exist).

*Numbers.* None enters the book here; the inventory lives in the record.

**Out of scope.**

* Changing any shape: `clinic-booking-submit`, `clinic-hours-save`, `clinic-hours-report` and `clinic-update-type` set them; this delivery writes down what they leave.
* The hooks' interfaces, `HoursSection` and its `report` included: not functions of an events file.
* The values worked out to show (`daysOf`, `tooLateToCancel`, `linesOf`): not events; `orchestrator-tests` moved them and docs/01's listing of the events file stays as it is.
* The clinic's other milestone 1.1 lines, `route-errors` and `minutes-of` among them: not this finding.
* Any chapter text and any tag: chapters 14 to 16 quote the clinic at `book-v1/four-pieces`, which never moves.
* Updating focus-kit in the clinic: the run cites `bff8414`.

**Done when.**

* [x] `clinic-update-type` was `[x]`, and the clinic clean at its last commit, equal to `origin/main`, before the first run; that commit and the inventory are in the README.
* [x] The clinic delivery (or each part of a split) ran the five steps, each turn recorded; nothing in the clinic edited by hand.
* [x] On the clinic's last commit, `git diff --stat <start commit> HEAD -- src` prints nothing.
* [x] The inventory taken again on the clinic's last commit: every event it lists takes a shape the clinic's docs/01 names, each shape with when it is used and the file of its first occurrence.
* [x] No test added or changed; no new dependency in `package.json`; `npm run verify` green on the clinic's last commit, saved as `verify.txt`.
* [ ] The author's check recorded in the README: docs/01 read against the events files; pending, collected at the end of the M4.1 loop.
* [x] Each clinic delivery committed by the author, no tag; pushed.
* [x] No note of the host left outside the clinic's repository.
* [x] `work/done/clinic-event-shapes-run/` as the Contract says; docs/06 as the Contract says.
* [x] `make verify` green in this book, the disclosure scan included.
* [x] Page in `work/done/`, only this delivery's paths staged, commit message suggested.

**Decisions.** Each taken on the recommended option, not asked:

* The clinic's slug is `event-shapes`, the book's slug without `clinic-`, as `update-type` was.
* The clinic's line goes to its milestone 1.1, after `update-type` and before `m1.1-review`, with no clause added to the paragraph, as `booking-submit` added none: no clause there covers a living document.
* This delivery waits for `clinic-update-type`, the last of the four runs that change the shapes; the start commit is whatever `update-type` leaves, checked at run time.
* The set is the inventory's, found by a grep and a read of each return type on the start commit, not the three shapes the finding and the line name; the load at mount with no starter is in it. The line's text stays.
* A shape the four runs did not predict is named, not a reason to stop: the Objective is every shape.
* Each shape says the file of its first occurrence, since AGENTS.md asks an abstraction to name it and the finding's breach is a rule written without its exceptions.
* Every event is covered, not only those with a call: the no-call shape without the state is a second exception docs/01 does not state, and naming it costs one clause.
* No manual check on `npm run dev`: nothing a user sees changes; the author's check is reading docs/01 against the events files.
* docs/05 is not edited: the recipe exists and needs no seventh name.

## What happened

* The precondition held: `clinic-update-type` was `[x]`; the clinic was on `main`, clean, at `181286f`, equal to `origin/main`, with focus-kit `bff8414`.
* The inventory on `181286f` found 55 exported functions: three values worked out to show and 52 events in eight shapes, one more than expected. `hoursReported`, which `clinic-hours-report` left answering `Update | Promise<Update>`, is a shape of its own, a report received, and was not expected; the weekly hours' `load` answers `WeeklyHoursAnswer`, so it belongs with the report shape, not the loads at mount. No expected shape left. The list and its groups are in the run's README.
* One clinic delivery, `event-shapes`, four turns: `/propose` (the slug, the brief), `/apply` and one staged review. `/propose` did not split the line and put it in milestone 1.1, after `update-type` and before `m1.1-review`. Its first turn asked four questions; the brief answered them and no later round came, so `Your call` was never sent. The page review was the author's "None".
* The clinic's docs/01 has a new `### Event shapes` subsection with the eight shapes, each with when it is used and its first occurrence, following the order `orchestrator-tests` wrote the files in, since all eight came in one commit; the orchestrator bullet points to it. On `6edc9ad` the same grep prints the same 55 functions, and each takes a shape the subsection names.
* The milestone 1.1 paragraph did not change, as the brief asked only for the line; the clinic's agent noted that without a clause there, `m1.1-review` does not check this delivery.
* `/apply` stopped short: four of its calls were denied, `npm run verify` redirected to a file and `git mv` of the page among them, so nothing was staged. The book's session ran `npm run verify` on the unstaged tree: green. The author then sent one staged review, with `Bash(git mv *)` added to the allowed tools for that turn only, a deviation from docs/05 §5 recorded in the README. `git mv` failed because the page was never committed, and the agent moved it with a plain `mv`, which `acceptEdits` allowed; it ran verify, staged, and printed the same message. Verify on the staged tree, rerun by the book's session: green.
* Calls denied: five, one in `/propose` (a chain with a `git log`, rerun without it) and four in `/apply`; recorded in the README.
* Every `claude` turn ended with a result of `success` but exited with code 1, standard error holding only `stty: stdin isn't a terminal`; recorded in the README.
* The suggested commit message carried no trailer; the author committed it as printed: `6edc9ad`, pushed, no tag. The diff is docs/01, docs/06 and the clinic's page; nothing in `src/` or `package.json`.
* `npm run verify` green on `6edc9ad`: 328 Vitest and 144 Playwright, the counts `update-type` left, and build.
* The author's check, docs/01 read against the events files, is collected at the end of the M4.1 loop; its item stays open.
* No note of the host outside the repositories: the clinic's auto-memory folder was there and empty before the run and stayed empty, and the host's folder gained only the two sessions' transcripts, so nothing was deleted. No ADR, no new term; docs/05 unchanged; docs/06's line keeps its text.
