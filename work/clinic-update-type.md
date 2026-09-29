# clinic-update-type

**Objective.** In the guided project, the update type `(current) => State` is declared once in `src/lib/` and every events file uses it, and so is the starter shape that `submitStarted` and `saveStarted` share, each with its first occurrence named, as the clinic's AGENTS.md asks; built by the clinic's own `/propose` and `/apply` and recorded, a sixth recorded clinic run, with no chapter and no tag.

This settles finding 5 of `m4-code-review`. It follows the pattern `clinic-booking-submit` set up (the first occurrence) and `clinic-hours-save` and `clinic-hours-report` repeated: a recorded run of an M4.1 finding with a brief word for word. This page restates none of it. It falls under the clause of the clinic's milestone 1.1 paragraph "the code repeated across features has one shared copy", under no line of it. The change is to types only: nothing a client or the owner sees changes.

**Behaviour.**

* In the clinic, one file in `src/lib/` declares the update type, generic in the state; no file in `src/features/` writes `(current: X) => X` out, and every events file that answered with it before uses the shared type.
* The same or another file in `src/lib/` declares the starter shape, generic in the state; `submitStarted` in `bookingEvents.ts` and `saveStarted` in `weeklyHoursEvents.ts` return it and write it out no longer. `cancelEvents.ts`' `submitStarted` returns a state, not that shape, and stays.
* The clinic's page names the first occurrences: for the update type, `bookingEvents.ts`, the first events file the clinic's `orchestrator-tests` wrote (its record, `work/done/clinic-orchestrator-tests-run/`); for the starter, `submitStarted`, in the shape `booking-submit` gave it.
* No event changes what it does. Every Vitest and Playwright test that existed passes without changing what it asserts; no test is added, since a type has no behaviour and `npm run verify`'s typecheck is its proof; `npm run verify` is green, and the author checks by hand on `npm run dev` that a client books a time and that the owner saves a professional's hours.
* The clinic's documents say it: its queue has the line, done; its docs/01 `lib/` listing names the new file or files.

**Contract.**

*Before the run.* `clinic-hours-report` runs first and is `[x]` in this book's docs/06, which means `clinic-booking-submit` and `clinic-hours-save` are too. The clinic is on `main`, clean, equal to `origin/main`, at the last commit `hours-report` left, with focus-kit `bff8414` as installed; the kit is not updated. That commit is checked at run time and written in the record; if `clinic-hours-report` is not done, or the clinic has moved past its record's last commit, /apply stops and asks. This book has other pages in flight; this delivery's /apply stages only its own paths.

*The count.* The docs/06 line says seven files; it is taken again on the start commit, from the clinic's root, and written in the README:

```
grep -rlE "\(current: [A-Za-z]+\) => [A-Za-z]+" src | grep -v "\.test\."
```

counts the files that write the update type out. The starter's shape is the return type `submitStarted` and `saveStarted` write out; `clinic-booking-submit` left that shape to the clinic's agent, so the README records the shape found on the start commit and the grep that finds it. On `a3e2470`, before the three earlier runs, the first grep finds eight files: the seven the finding's summary names (`ownerEvents.ts`, `professionalsEvents.ts`, `clinicEvents.ts`, `healthEvents.ts`, `cancelEvents.ts`, `rememberedEvents.ts`, `weeklyHoursEvents.ts`) and `bookingEvents.ts`, whose `BookingOutcome` writes it inside `{ update }`; the finding's failure scenario says eight. The starter's shape there is `{ state; send: boolean }`, and `grep -rn "send: boolean" src/features` finds its two lines. If on the start commit the two starters' written-out return types differ, the earlier runs parted them, and /apply stops and asks. The brief carries no number, so a count that moved changes nothing in it.

*The run.* docs/05 §5, "A recorded clinic run", as `clinic-booking-submit` runs it, with this slug and this brief. The first `/propose` is:

```
claude -p "/propose update-type" <common flags>
```

followed, in the same session with `--continue`, by this brief, word for word:

```
The update type (current) => State is written out again in every events file that answers with one, and the starter shape that submitStarted in bookingEvents.ts and saveStarted in weeklyHoursEvents.ts share, as booking-submit and hours-save left it, is written out twice. AGENTS.md asks for an abstraction on the second concrete occurrence, naming the first, and docs/01 says code moves to lib/ on its second use. Declare each once in src/lib/, generic in the state, and have every events file use them, so no file in src/features/ writes either out. Name the first occurrences on your page: for the update type, bookingEvents.ts, the first events file orchestrator-tests wrote; for the starter, submitStarted. cancelEvents' submitStarted returns a state, not the starter shape, so it stays. Types only: no event changes what it does, no test changes what it asserts, no new test, no new dependency. Leave the event shapes as they are, BookingOutcome and { update, report } included, only spelled with the shared type: another delivery has docs/01 name every event shape, so do not do it here. docs/01's lib/ listing names the new file or files. The app behaves exactly as before. Say the names and files you chose and why. Add the line to milestone 1.1, just after hours-report and before m1.1-review, saying it settles its clause that the code repeated across features has one shared copy.
```

Every later round of questions, the reviews, a split and the commits: as `clinic-booking-submit`.

*The record,* `work/done/clinic-update-type-run/`: the format of docs/05 §5, with the brief above and the count on the start commit in the README, and `verify.txt`, `npm run verify` on the clinic's last commit.

*This book's documents, in the same delivery.*

* docs/06: `clinic-update-type` `[>]` (this /propose), `[x]` by /apply. Its text keeps "seven": the line records what the review said, and the record says what the count found.
* docs/05: unchanged, as `clinic-booking-submit` left it.
* docs/03: no new term.

*Numbers.* None enters the book here; the count lives in the record.

**Out of scope.**

* docs/01 naming every shape an event with a call takes, `{ update, report }` and the starter included: `clinic-event-shapes`, which documents what this delivery leaves.
* Changing what the starter or any event returns: `clinic-booking-submit`, `clinic-hours-save` and `clinic-hours-report` set those shapes; this delivery only spells them once.
* `cancelEvents.ts`' `submitStarted`: it returns a state, a different shape.
* The clinic's other shared copies, the route answers and the "HH:MM" parser: its `route-errors` and `minutes-of` lines.
* A test of the shared types or of the hook: a type has no behaviour; finding 9, rejected, keeps the hook out of the tests.
* Any chapter text and any tag: chapters 14 to 16 quote the clinic at `book-v1/four-pieces`, which never moves.
* Updating focus-kit in the clinic: the run cites `bff8414`.

**Done when.**

* [ ] `clinic-hours-report` was `[x]`, and the clinic clean at its last commit, equal to `origin/main`, before the first run; that commit and the count are in the README.
* [ ] The clinic delivery (or each part of a split) ran the five steps, each turn recorded; nothing in the clinic edited by hand.
* [ ] On the clinic's last commit, the count's first grep finds only files in `src/lib/`; `submitStarted` and `saveStarted` return the shared type and write no object type out, and the starter's grep the README recorded finds nothing in `src/features`.
* [ ] The clinic's page names `bookingEvents.ts` and `submitStarted` as the first occurrences; its docs/01 `lib/` listing names the new file or files.
* [ ] No test changed what it asserts and none was added; no new dependency in `package.json`; `npm run verify` green on the clinic's last commit, saved as `verify.txt`.
* [ ] The author's manual check recorded in the README.
* [ ] Each clinic delivery committed by the author, no tag; pushed.
* [ ] No note of the host left outside the clinic's repository.
* [ ] `work/done/clinic-update-type-run/` as the Contract says; docs/06 as the Contract says.
* [ ] `make verify` green in this book, the disclosure scan included.
* [ ] Page in `work/done/`, only this delivery's paths staged, commit message suggested.

**Decisions.** Each taken on the recommended option, not asked:

* The clinic's slug is `update-type`, the book's slug without `clinic-`, as `hours-report` was.
* The clinic's line goes to its milestone 1.1, after `hours-report` and before `m1.1-review`, and says it settles the paragraph's clause on repeated code, since no line there covers it.
* This delivery waits for `clinic-hours-report`, since the three earlier runs change the starters and the answers this one spells once; the start commit is whatever `hours-report` leaves, checked at run time.
* The count is a grep of the type written out, taken on the start commit; it finds eight today where the line says seven, because the finding's summary left out `bookingEvents.ts`. The line's text stays; the brief carries no number.
* The update type's first occurrence is `bookingEvents.ts`: all eight came in one commit, and the record of `orchestrator-tests` shows it the first events file written. The starter's is `submitStarted`, which `booking-submit` shaped and `hours-save` followed.
* The shared types go to `src/lib/`, as the clinic's docs/01 says for code on its second use; their names and files are left to the clinic's agent, which says what it chose.
* No new test: a type has no behaviour and the typecheck in `npm run verify` proves it; the manual check covers a booking and a save, the two starters.
* docs/05 is not edited: the recipe exists and needs no sixth name.
