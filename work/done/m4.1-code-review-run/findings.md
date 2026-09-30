# Findings

The seven findings of `/code-review high a3e2470...6edc9ad`, turn 1, as the run reported them: the JSON block of the response, one block per finding, byte for byte.

## Finding 1

```json
  {
    "file": "src/features/weeklyHours/useWeeklyHours.ts",
    "line": 61,
    "summary": "Times typed during an in-flight save stay on screen (the new update keeps them), but `save` sends the old `state.periods`, and on \"saved\" the section sets `row: undefined`, which unmounts the editor and drops those edits without a word.",
    "failure_scenario": "Owner clicks Save, then changes Monday's end to 19:00 while the PUT is pending. The time inputs in WeeklyHoursView.tsx have no `disabled={busy}`. The server saves the old end, the \"saved\" report closes the row, and the 19:00 edit is lost, although hours-save says a time typed just before Save survives. On \"failed\" or \"NotSignedIn\" the screen instead shows periods that differ from what was sent, with no sign of it."
  }
```

## Finding 2

```json
  {
    "file": "src/features/appointments/useBooking.ts",
    "line": 43,
    "summary": "The booking is sent with `next.state` (the name and phone at click time), while the new update keeps whatever is typed into the still-enabled fields during the call, so the form shows details that were not booked.",
    "failure_scenario": "Client taps Book, then corrects the phone from 912000000 to 913000000 before the POST returns. The appointment is booked under 912000000, the confirmation shows the server's clientPhone (the old one), and the fields are emptied. On SlotTaken the corrected value stays visible as if it had been used. The test \"sends the checked form and keeps a name typed after the click\" treats this as correct."
  }
```

## Finding 3

```json
  {
    "file": "src/features/professionals/professionalsEvents.ts",
    "line": 226,
    "summary": "`hoursReported(\"ProfessionalNotFound\")` runs `reloadGone`, which sets `row: undefined` whenever the reload resolves. On the load path nothing sets `busy` first, so the late update can close a row the owner opened in the meantime.",
    "failure_scenario": "The hours editor's first fetch reports ProfessionalNotFound, so the list reload starts with `busy` still false. The owner opens rename or hours on another professional. The reload resolves and wipes that newly opened row, and any rename text typed into it."
  }
```

## Finding 4

```json
  {
    "file": "src/features/weeklyHours/weeklyHoursEvents.ts",
    "line": 40,
    "summary": "Adding \"saving\" to `WeeklyHoursReport` also widens `WeeklyHoursAnswer.report`, so the types now allow `load` or `save` to answer `report: \"saving\"`, which would leave the section busy for good.",
    "failure_scenario": "A later change returns `{ update, report: \"saving\" }` from `save` or `load` (for example by passing a code through). It type-checks, the hook forwards it, `hoursReported` sets `busy: true`, and nothing ever clears it, so every button in the section stays disabled. Keeping `\"saving\"` in `HoursSection.report`'s parameter type only would stop this."
  }
```

## Finding 5

```json
  {
    "file": "src/features/weeklyHours/weeklyHoursEvents.ts",
    "line": 149,
    "summary": "The refusal key comes from the acted-on drafts but is written onto the current state. If that period is gone from the current state, no period shows the message and nothing is sent.",
    "failure_scenario": "The acted-on state has an invalid period with key 4 and the current state no longer has key 4. `update` sets `refusal: { key: 4 }`, `send` is false, and WeeklyHoursView matches `refusal.key` against no row, so Save silently does nothing. The same design also shows a stale name or phone error next to a value the person already fixed (`submitStarted`)."
  }
```

## Finding 6

```json
  {
    "file": "src/features/professionals/useProfessionals.ts",
    "line": 87,
    "summary": "Because `hoursReported` returns `Update | Promise<Update>`, the hook needs a `typeof answer === \"function\"` branch, and docs/01 had to add a whole new event shape (7) for this one call.",
    "failure_scenario": "Every caller and test must tell the two apart (the test file adds an `atOnce` helper that throws). A simpler form: a synchronous `hoursReported(state, report)` for saving, saved, failed and NotSignedIn, and the existing `reloadGone` as a separate async event for ProfessionalNotFound. That fits shapes 1 and 2, drops the union, and needs no new shape."
  }
```

## Finding 7

```json
  {
    "file": "docs/01-Architecture.md",
    "line": 40,
    "summary": "docs/01 says every exported function of an events file is an event or one of the view values `daysOf`, `tooLateToCancel` and `linesOf`, but `retryOf` (exported from bookingEvents.ts) is neither an event nor in that list.",
    "failure_scenario": "Someone checking a new export against \"Event shapes\" finds `retryOf` breaks the stated rule. The doc then misstates the code it claims to list completely, against the AGENTS.md rule that documents are living and must match behaviour."
  }
```
