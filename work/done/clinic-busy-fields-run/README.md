# clinic busy fields run

The guided project's weekly hours editor's From and To inputs and booking form's name and phone disabled while a save or a booking is in flight, with the same `busy` as the buttons beside them, built with `/propose` and `/apply`. The delivery that planned and recorded it is `../clinic-busy-fields.md`; the format is docs/05 §5, "A recorded clinic run", in its eighth occurrence.

* Host: Claude Code, `claude --version` printed `2.1.285 (Claude Code)`; macOS 26 (Darwin 25.6.0), arm64.
* Model: `claude-opus-5-5`, given with `--model` on every turn.
* Kit: focus-kit `bff8414`, as installed; not updated. The clinic's `.claude/` has not changed since `a3e2470`, "Update focus-kit to bff8414".
* The clinic's first commit: `6edc9ad076c3758102c3570d224be8d1fa964264`, "Name every event shape in docs/01 (event-shapes)", the last commit `clinic-event-shapes` left; the clinic was on `main`, clean, equal to `origin/main`, before the first run.
* The clinic's last commit: `21522b81582a8aa7736a761b07f19eddfaab79a3`, "Disable the busy fields of the hours editor and booking form (busy-fields)", no tag, not pushed: the clinic is one commit ahead of `origin/main`.
* Date: 2026-09-30.

## The commands

Run from the root of the clinic. Common flags, on every turn:

```
--model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose
```

`/propose`, a fresh session: `claude -p "/propose busy-fields"` with the common flags. The brief went next, with `claude -p --continue "<brief>"` and the common flags.

`/apply`, a fresh session: `claude -p "/apply busy-fields"` with the common flags and:

```
--disallowedTools "Bash(npm run dev*)" --allowedTools "Bash(npm *)" "Bash(npx *)" "Bash(node *)" "Bash(mkdir *)" "Bash(cp *)" "Bash(git add *)" "Bash(git status *)" "Bash(git diff *)"
```

The staged review went to the same session with `claude -p --continue "<request>"` and the same flags.

* The turns were started by the book's `/apply` session through its shell, one at a time.
* The author decided before the run, for the M4.2 loop: no conversation; the page review and the staged review send a request only for a real hole against the book's page, otherwise "none"; the book's session commits in the clinic with the kit's message, no tag, and does not push.
* Nothing in the clinic was edited by hand.
* Each turn ended with a result of `success`. The `claude` process still exited with code 1 on every turn, and its standard error held only `stty: stdin isn't a terminal`: the shell that started it had no terminal. The streams are complete.
* No note of the host outside the repository appeared: the host's auto-memory folder for the clinic was there and empty before the run and stayed empty, and the host's folder for the clinic gained only the two sessions' transcripts. Nothing was deleted.

## busy-fields

`/propose` did not split the line; it put `busy-fields` in milestone 1.1, just after `event-shapes` and before `m1.1-review`, as the brief asked.

* `/propose`: turn 1 (`/propose busy-fields`), turn 2 (the brief). Turn 1 found the slug in no document, listed ten inputs in five views that stay enabled while their buttons are disabled, and asked one round of four questions: every field of the five views or fewer, `disabled` or `readOnly`, the place in the queue with a clause in the milestone paragraph, and whether docs/01's sentence "so what was typed meanwhile survives" changes. The brief answered them; turn 2 wrote the page with no further question, said no living document states which controls a view disables while busy, and left the cancel form, the professionals section and the owner's sign-in out of scope. `Your call` was never sent. The brief, word for word:

  ```
  The weekly hours editor's From and To time inputs and the booking form's name and phone inputs stay enabled while a save or a booking is in flight, while the buttons beside them are disabled. So a time typed during a save is shown but not sent, and "saved" closes the editor and drops it without a word; a name or phone changed during a booking is shown but was not booked. Disable those four inputs with busy, the same busy the buttons of each view already use: the section's busy in WeeklyHoursView.tsx, the booking state's busy in BookingView.tsx. Extend the two Playwright tests that hold a call in flight, "disables every button of the editor while a save is in flight" in WeeklyHoursView.e2e.ts and "disables Book and Back while a booking is in flight" in BookingView.e2e.ts, to assert those inputs disabled too; their names may say so. Change the Vitest tests "sends the checked form and keeps a name typed after the click" in bookingEvents.test.ts and "sends the checked week and keeps a time typed after the click" in weeklyHoursEvents.test.ts so they no longer present an edit typed after the click as correct: each asserts what the in-flight update of a sent call does applied to the state that was checked, under a name that says so. Leave the refused-save test and "keeps a name typed in flight through a taken slot" as they are. No event, hook or route changes; the update is still applied to the current state, as docs/01 says, so its sentence "what was typed meanwhile survives" stays: the cancel form and the professionals section still rely on it. Leave the cancel form's and the professionals section's inputs as they are: not this finding. No new dependency. The app behaves as before apart from those four inputs. Say whether any document of this project states which controls a view disables while busy, and change it only if a sentence there stops being true. Add the line to milestone 1.1, just after event-shapes and before m1.1-review.
  ```

* Page review: none.
* `/apply`: turn 3. It added `disabled={busy}` to the four inputs, renamed and changed the four tests, took three screenshots of the in-flight state with a one-off Playwright file it then removed, ran `npm run verify` green, wrote "What happened", marked the queue line `[x]` and moved the page. Its `git add -A`, run as `git -C . add -A`, was denied, and it stopped with nothing staged.
* Staged review: turn 4, one request, since a delivery left unstaged is a hole against the book's page, word for word:

  ```
  Nothing is staged: stage everything with git add -A, without -C, check it with git status --short, and print the commit message again.
  ```

  It staged the eleven files and printed the same message.
* Denied calls, three, all in turn 3: a Python script chained with `git mv`, `grep` and `git add -A` that ticked the page, wrote "What happened" and moved the page; `git -C . add -A`; `git -C . status --short`. The agent did the script's edits with its file tools and moved the page with a plain `mv`, which ran under `acceptEdits`: a retry by another route inside its own session, as in the earlier runs. It did not retry the staging and asked for it. None in `/propose`.
* Diverged:
  * The Vitest tests' new names: "sends the checked form and marks it busy" and "sends the checked week and clears its refusal and unreachable". Each applies the update to the checked state and asserts it with `toEqual`. The Playwright tests became "disables Book, Back, name and phone while a booking is in flight" and "disables every button and time input of the editor while a save is in flight".
  * The milestone 1.1 paragraph gained a clause for the line, so `m1.1-review` checks it, as `hours-save` did.
  * The clinic's page added three screenshots, `work/done/busy-fields-*-in-flight-*.png`, and a manual check with the browser's network throttled, which stays unticked on the clinic's page.
  * The refused-save test, "refuses the checked week and keeps a time typed after the click", kept its name, as the brief said, so the book page's grep for "keeps a time typed after the click" still finds it; the two tests the brief names are gone.
  * `disabled={busy}` counts: 4 and 3 on `6edc9ad`, 6 and 5 on `21522b8`, in `WeeklyHoursView.tsx` and `BookingView.tsx`.
  * The suggested commit message carried no `Co-Authored-By` trailer; it was committed as printed.
* Commit: `21522b81582a8aa7736a761b07f19eddfaab79a3`, "Disable the busy fields of the hours editor and booking form (busy-fields)", committed by the book's session under the author's authorization for the M4.2 loop, not pushed.

## The author's manual check

Pending, collected at the end of the M4.2 loop: on `npm run dev`, a save, a refused period and a booking behave as before.

## Files

```
README.md               this file
busy-fields/turn-N.txt  every turn, in order: text blocks byte for byte, tool calls as [tool <name>] <path or command>
verify.txt              the npm run verify output on the clinic's last commit, 21522b8
```

The turn files are derived from each turn's stream. Absolute paths are removed, so paths are relative to the clinic's root; the host's folder for the clinic reads `<host folder of the clinic>`. Session ids are left out. In `verify.txt` the terminal colours are removed and the clinic's folder that Vitest prints became `.`.
