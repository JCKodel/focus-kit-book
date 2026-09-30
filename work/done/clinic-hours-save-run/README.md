# clinic hours save run

The guided project's `useWeeklyHours` save, which now publishes its in-flight state as an update of the current state, in the shape `booking-submit` gave `submitStarted`, built with `/propose` and `/apply` and committed by the author. The delivery that planned and recorded it is `../clinic-hours-save.md`; the format is docs/05 §5, "A recorded clinic run", in its fourth occurrence.

* Host: Claude Code, `claude --version` printed `2.1.285 (Claude Code)`; macOS 26 (Darwin 25.6.0), arm64.
* Model: `claude-opus-5-5`, given with `--model` on every turn.
* Kit: focus-kit `bff8414`, as installed; not updated.
* The clinic's first commit: `8e4de4610f4b86eca911572173bf145a86c3ea79`, "Book with the state the person acted on in useBooking's submit", the last commit `clinic-booking-submit` left; the clinic was on `main`, clean, equal to `origin/main`, before the first run.
* The clinic's last commit: `13dd9c0c09be3a7304587361770c1affa77a2391`, "Publish useWeeklyHours' in-flight save as an update (weeklyHours)", pushed, no tag.
* Date: 2026-09-30.

## The commands

Run from the root of the clinic. Common flags, on every turn:

```
--model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose
```

`/propose`, a fresh session: `claude -p "/propose hours-save"` with the common flags. The brief went next, with `claude -p --continue "<brief>"` and the common flags.

`/apply`, a fresh session: `claude -p "/apply hours-save"` with the common flags and:

```
--disallowedTools "Bash(npm run dev*)" --allowedTools "Bash(npm *)" "Bash(npx *)" "Bash(node *)" "Bash(mkdir *)" "Bash(cp *)" "Bash(git add *)" "Bash(git status *)" "Bash(git diff *)"
```

* The turns were started by the book's `/apply` session through its shell, one at a time.
* The author decided before the run: the page review and the staged review are "None", and any round of questions the brief does not answer gets `Your call. Say what you chose and why.`
* Nothing in the clinic was edited by hand.
* Each turn ended with a result of `success`. The `claude` process still exited with code 1 on every turn, and its standard error held only `stty: stdin isn't a terminal`: the shell that started it had no terminal. The streams are complete.
* No note of the host outside the repository appeared: the host's auto-memory folder for the clinic stayed empty, and no turn wrote into the host's folder.

## hours-save

`/propose` did not split the line; it put `hours-save` in milestone 1.1, just after `booking-submit` and before `m1.1-review`, as the brief asked.

* `/propose`: turn 1 (`/propose hours-save`), turn 2 (the brief). Turn 1 asked one round of two questions: whether to declare a shared `{ update, send }` type in this delivery, and whether to remove `sectionRef.current = section`, the last ref in `src/` written during render. The brief answered the first (the update type and the starter shape stay as they are); turn 2 wrote the page with no further question and left `sectionRef` out of scope on its own, saying `m1.1-review` can raise it. `Your call` was never sent. The brief, word for word:

  ```
  useWeeklyHours' save publishes its in-flight state as a whole state, saveStarted(state).state from the render closure, while docs/01 says an event's answer is an update (current) => State, so what was typed meanwhile survives: a time typed or a period added or removed just before Save is lost. Make save follow that rule in the shape booking-submit gave submitStarted, the first occurrence: the in-flight state is published as an update of the current state. saveStarted still decides from the state save read whether to send and which period is refused, and save still sends that state's periods. Add a test in weeklyHoursEvents.test.ts, in Node, that the in-flight update, for a save that is refused and for one that is sent, applied to a state where a time was typed after the click keeps that time. No test drives the hook, no module mock, no new dependency. Leave forward, the section's reports and the update type as they are: later deliveries change them, and a later one declares the starter shape once, so do not do it here. The app behaves exactly as before. Say which shape you followed. Add the line to milestone 1.1, just after booking-submit and before m1.1-review.
  ```

* Page review: none.
* `/apply`: turn 3.
* Staged review: none.
* Denied calls, one, in turn 3: a Python script that rewrote `saveStarted` in `weeklyHoursEvents.ts` and the call in `useWeeklyHours.ts`. The clinic's agent then made the same changes with its file tools, none denied. docs/05 §5 says a denied call is never retried by another route; the agent did so inside its own session, as in `booking-submit`, and it is recorded here. None in `/propose`.
* Diverged:
  * The shape followed is `submitStarted`'s: `saveStarted(state)` answers `{ update, send }`, written inline, no shared type. `send` and the refused period are decided from the state `save` read; `update` writes only `unreachable` and `refusal` onto the current state. `useWeeklyHours` calls `setState(started.update)`.
  * The clinic's docs/01 changed one sentence: it now names `submitStarted` as the first occurrence of `{ update, send }` and `saveStarted` as the second, where it said `saveStarted` still returned a whole state. For `clinic-update-type`: docs/01 already names both occurrences; that delivery declares the shape, and the sentence becomes a pointer to it.
  * Three existing Vitest cases changed how they read the result, not what they assert; the clinic's page planned two. The third, "marks the first refused period and sends nothing", keeps the one check the new cases do not make: only the first of two refused periods is marked. The before-the-load case now checks the update with `toBe`.
  * The agent added a clause to milestone 1.1's paragraph naming `useWeeklyHours`' save, so `m1.1-review` checks it, as `booking-submit` did.
  * The suggested commit message carried no `Co-Authored-By` trailer this time; the author committed it as printed.
* Commit: `13dd9c0c09be3a7304587361770c1affa77a2391`, "Publish useWeeklyHours' in-flight save as an update (weeklyHours)".

## The author's manual check

Pending, collected at the end of the M4.1 loop.

## Files

```
README.md              this file
hours-save/turn-N.txt  every turn, in order: text blocks byte for byte, tool calls as [tool <name>] <path or command>
verify.txt             the npm run verify output on the clinic's last commit, 13dd9c0
```

The turn files are derived from each turn's stream. Absolute paths are removed, so paths are relative to the clinic's root; the host's folder for the clinic reads `<host folder of the clinic>`. Session ids are left out. In `verify.txt` the terminal colours are removed and the clinic's folder that Vitest prints became `.`.
