# clinic booking submit run

The guided project's `useBooking` submit, which now publishes its in-flight state as an update of the current state and books with the state passed into `run`, built with `/propose` and `/apply` and committed by the author. The delivery that planned and recorded it is `../clinic-booking-submit.md`; the format is docs/05 §5, "A recorded clinic run", in its third occurrence.

* Host: Claude Code, `claude --version` printed `2.1.285 (Claude Code)`; macOS 26 (Darwin 25.6.0), arm64.
* Model: `claude-opus-5-5`, given with `--model` on every turn.
* Kit: focus-kit `bff8414`, as installed; not updated.
* The clinic's first commit: `a3e2470`, "Update focus-kit to bff8414"; the clinic was on `main`, clean, equal to `origin/main`, before the first run.
* The clinic's last commit: `8e4de4610f4b86eca911572173bf145a86c3ea79`, "Book with the state the person acted on in useBooking's submit", pushed, no tag.
* Date: 2026-09-30.

## The commands

Run from the root of the clinic. Common flags, on every turn:

```
--model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose
```

`/propose`, a fresh session: `claude -p "/propose booking-submit"` with the common flags. The brief went next, with `claude -p --continue "<brief>"` and the common flags.

`/apply`, a fresh session: `claude -p "/apply booking-submit"` with the common flags and:

```
--disallowedTools "Bash(npm run dev*)" --allowedTools "Bash(npm *)" "Bash(npx *)" "Bash(node *)" "Bash(mkdir *)" "Bash(cp *)" "Bash(git add *)" "Bash(git status *)" "Bash(git diff *)"
```

* The turns were started by the book's `/apply` session through its shell, one at a time.
* The author decided before the run: the page review and the staged review are "None", and any round of questions the brief does not answer gets `Your call. Say what you chose and why.`
* Nothing in the clinic was edited by hand.
* Each turn ended with a result of `success`.
* No note of the host outside the repository appeared: the host's auto-memory folder for the clinic stayed empty.

## booking-submit

`/propose` did not split the line; it put `booking-submit` in milestone 1.1, just before `m1.1-review`, as the brief asked.

* `/propose`: turn 1 (`/propose booking-submit`), turn 2 (the brief). Turn 1 asked one round of questions, since the slug is not in the clinic's queue; the brief answered it, and turn 2 wrote the page with no further question, so `Your call` was never sent. The brief, word for word:

  ```
  useBooking's submit publishes its in-flight state as a whole state taken from the ref shown, written during render, while docs/01 says an event's answer is an update (current) => State, so what was typed meanwhile survives, and the hook already publishes loadSlotsStarted and loadProfessionalsStarted that way. Make submit follow that rule: the in-flight state is published as an update of the current state, and the hook's submit and retry pass the state they read into run, which books with it, so shown leaves. submitStarted still decides from that state whether to send. Add a test in bookingEvents.test.ts, in Node, that the in-flight update applied to a state where a name was typed after the click keeps that name. No test drives the hook, no module mock, no new dependency. The shape you give the starter is the first occurrence: useWeeklyHours' save will follow it in a later delivery, and a later one declares the shape once, so do neither here; say what shape you chose and why. The app behaves exactly as before. Add the line to milestone 1.1, just before m1.1-review.
  ```

* Page review: none.
* `/apply`: turn 3.
* Staged review: none.
* Denied calls, one, in turn 3: one compound call that updated the page with a Python script, marked docs/06, moved the page with `git mv` or `mv` and ran `git add -A`. The clinic's agent then did the same work another way, with its file tools, a plain `mv` and `git add -A`, none denied. docs/05 §5 says a denied call is never retried by another route; the agent did so inside its own session, and it is recorded here. None in `/propose`.
* Diverged: the starter shape the agent chose is `submitStarted(state)` answering `{ update, send }`; the submit event carries its state as `{ next: "submit", state }`. Three existing Vitest cases changed how they read the result, not what they assert. The agent also added a clause to milestone 1.1's paragraph and a paragraph to the clinic's docs/01 on the starter's update and shape. The suggested commit message carried a `Co-Authored-By` trailer; with the staged review "None", the driver dropped it at commit, by the author's rule.
* Commit: `8e4de4610f4b86eca911572173bf145a86c3ea79`, "Book with the state the person acted on in useBooking's submit".

## The author's manual check

Run on 2026-09-30, collected at the end of the M4.1 loop with the manual checks of `clinic-update-type`, `clinic-hours-save` and `clinic-hours-report`, which point here for the setup.

* Setup: Chrome, driven by Claude in Chrome at the author's request, the author present, against the clinic's `npm run dev` at `http://localhost:5173`, on the clinic's commit `6edc9ad`, in a desktop window.
* The owner's password of the dev database was forgotten. The driver reset it with the clinic's own `hashPassword`, writing into `data/clinic.sqlite`, ignored by git, after a backup of that file. Nothing in the clinic's repository changed.
* Booked with the name Test on Mon 5 Oct at 09:00.
* Book with an empty name was refused with "Type a name of 1 to 80 characters.", and the phone with "Type a phone number with 6 to 15 digits.".
* A valid booking showed the booking code and listed it under "Your appointments".
* Passed.

## Files

```
README.md                  this file
booking-submit/turn-N.txt  every turn, in order: text blocks byte for byte, tool calls as [tool <name>] <path or command>
verify.txt                 the npm run verify output on the clinic's last commit, 8e4de46
```

The turn files are derived from each turn's stream. Absolute paths are removed, so paths are relative to the clinic's root; the host's folder for the clinic reads `<host folder of the clinic>`. Session ids are left out. In `verify.txt` the terminal colours are removed and the clinic's folder that Vitest prints became `.`.
