# clinic-hours-answer

**Objective.** In the guided project, the report a weekly hours answer carries cannot be "saving": `load` answers only a refusal or nothing, `save` only "saved", "failed" or a refusal, and "saving" is a report only `useWeeklyHours` makes, before a save it sends, so no answer can leave the professionals section busy for good; built by the clinic's own `/propose` and `/apply` and recorded, a recorded clinic run with no chapter and no tag.

This settles finding 4 of `m4.1-code-review`. It follows the pattern of `clinic-hours-save` and its siblings (the first was `clinic-booking-submit`): a recorded run, a brief word for word, the name chosen by the clinic's agent. This page restates none of it. It runs after `clinic-busy-fields`, the other clinic line of M4.2. The code does nothing wrong today; the type allows what the code never does, and this delivery makes the type say what the code does.

**Behaviour.**

* In the clinic, `WeeklyHoursAnswer`'s `report` has a type without "saving": "saved", "failed" or a `SectionRefusal`. `WeeklyHoursReport`, the type `HoursSection.report` and `hoursReported` take, is that type or "saving". A `load` or `save` that answered "saving" would not type-check.
* `load` and `save` answer what they answer today, and `useWeeklyHours` still reports "saving" itself, before a save it sends, and passes each answer's report to the section.
* No new test: `npm run typecheck`, inside `npm run verify`, is the check. No `@ts-expect-error` line, no new dependency.
* The app behaves as before: every Vitest and Playwright test that existed passes without changing what it asserts, `npm run verify` is green, and the author checks by hand on `npm run dev` that the owner saves a professional's hours, that a period too short is refused with its message beside it and nothing is sent, and that the hours read back after a reload are the ones saved.
* The clinic's documents say it: its queue has the line, done; its docs/01 shape 6 names the answer's report type, since it now differs from `WeeklyHoursReport`.

**Contract.**

*Before the run.* `clinic-busy-fields` runs first and is `[x]` in this book's docs/06. The clinic is on `main`, clean, equal to `origin/main`, at the last commit `busy-fields` left, with focus-kit `bff8414` as installed; the kit is not updated. That commit is checked at run time and written in the record; if `clinic-busy-fields` is not done, or the clinic has moved past its record's last commit, /apply stops and asks. This book has other pages in flight; this delivery's /apply stages only its own paths.

*The run.* docs/05 §5, "A recorded clinic run", as `clinic-hours-save` runs it, with this slug and this brief. The first `/propose` is:

```
claude -p "/propose hours-answer" <common flags>
```

followed, in the same session with `--continue`, by this brief, word for word:

```
WeeklyHoursAnswer's report is a WeeklyHoursReport, which hours-report widened with "saving", so the types allow load or save to answer "saving", which would leave the professionals section busy for good, since hoursReported sets busy and nothing clears it. The code never does it: load answers only a refusal or nothing, save only "saved", "failed" or a refusal, and "saving" is a report only useWeeklyHours makes, before a save it sends. Make the type say so: WeeklyHoursAnswer's report takes a type without "saving", "saved", "failed" or a SectionRefusal, and WeeklyHoursReport, which HoursSection.report and hoursReported take, is that type or "saving". Name the new type and say why. load and save answer what they answer today, and the hook reports as today. No new test: typecheck is the check; no @ts-expect-error, no module mock, no new dependency. The app behaves exactly as before. Update docs/01's shape 6 to name the answer's report type. Add the line to milestone 1.1, just after busy-fields and before m1.1-review.
```

Every later round of questions, the reviews, a split and the commits: as `clinic-hours-save`.

*The record,* `work/done/clinic-hours-answer-run/`: the format of docs/05 §5, with the brief above in the README and `verify.txt`, `npm run verify` on the clinic's last commit.

*This book's documents, in the same delivery.*

* docs/06: `clinic-hours-answer` `[>]` (this /propose), `[x]` by /apply.
* docs/05: unchanged.
* docs/03: no new term.

*Numbers.* None enters the book here.

**Out of scope.**

* The fields that stay enabled while a save or a booking is in flight: `clinic-busy-fields`, which runs first.
* A separate answer type for `load`, narrower than `save`'s: the finding is "saving", and one answer type for both events is docs/01's shape 6; `load`'s narrower range stays what its code does.
* Changing `hoursReported`, `Update | Promise<Update>` or its `atOnce` test helper: finding 6 of `m4.1-code-review`, rejected.
* A refusal whose key no longer matches a row (finding 5) and `hoursRefused` (finding 3): rejected or out of M4.1's range.
* Any chapter text and any tag: no chapter quotes `WeeklyHoursAnswer`, and chapters 14 to 16 quote the clinic at `book-v1/four-pieces`, which never moves.
* A test that a "saving" answer fails to compile: the type checker already runs in `npm run verify`.
* Updating focus-kit in the clinic: the run cites `bff8414`.

**Done when.**

* [ ] `clinic-busy-fields` was `[x]`, and the clinic clean at its last commit, equal to `origin/main`, before the first run; that commit is in the README.
* [ ] The clinic delivery (or each part of a split) ran the five steps, each turn recorded; nothing in the clinic edited by hand.
* [ ] On the clinic's last commit, the type of `WeeklyHoursAnswer`'s `report` in `src/features/weeklyHours/weeklyHoursEvents.ts` holds no "saving", and `WeeklyHoursReport` is that type or "saving".
* [ ] No new test file and no new dependency in `package.json`; no `@ts-expect-error` in the diff.
* [ ] The existing tests pass without changing what they assert; `npm run verify` green on the clinic's last commit, saved as `verify.txt`.
* [ ] The author's manual check recorded in the README.
* [ ] Each clinic delivery committed by the author, no tag; pushed.
* [ ] No note of the host left outside the clinic's repository.
* [ ] `work/done/clinic-hours-answer-run/` as the Contract says; docs/06 as the Contract says.
* [ ] `make verify` green in this book, the disclosure scan included.
* [ ] Page in `work/done/`, only this delivery's paths staged, commit message suggested.

**Decisions.** Each taken on the recommended option, not asked:

* The clinic's slug is `hours-answer`, the book's slug without `clinic-`, as `hours-save` was.
* The clinic's line goes to its milestone 1.1, after `busy-fields` and before `m1.1-review`, since it corrects code of the same `hours-report` line and `busy-fields` is added there first.
* This delivery waits for `clinic-busy-fields`, which runs first; the start commit is not written here but checked at run time.
* One answer type for `load` and `save`, with a report that excludes "saving", rather than one type per event: the finding asks only that no answer carry "saving", and docs/01's shape 6 stays one shape.
* The new type's name is left to the clinic's agent, which says why, as the starter's shape was in `clinic-booking-submit`.
* No new test: the guarantee is a type, and `npm run typecheck` already runs in `npm run verify`.
* The clinic's docs/01 changes in shape 6, because the answer's report type it names changes.
* The manual check is `clinic-hours-save`'s: a save, a refused period and a reload, since the change touches the save's types.
* docs/05 is not edited: the recipe exists.
