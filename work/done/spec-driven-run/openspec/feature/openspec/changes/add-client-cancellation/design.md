# Design

## Context

`src/appointment.ts` keeps appointments in a module-level array and exports `book(clientName, startsAt)`. `book` doesn't check for conflicts, and `status` can only be `"booked"`. The project is ESM (`"type": "module"`) and runs on Node 26. Node 26 strips TypeScript types itself, so `node --test` finds and runs `src/*.test.ts` files that import `./appointment.ts` directly, without a build step. See proposal.md for motivation and the specs for the required behavior.

## Goals / Non-Goals

**Goals:**
- Keep the module's shape: plain exported functions working on the in-memory array.
- Make the current time something tests control, so the 24-hour rule can be tested exactly.

**Non-Goals:**
- Appointment durations or overlap checks. A slot is one exact start instant.
- Clearing state between tests through a public API (see Risks).

## Decisions

**Signature: `cancel(id: number, clientName: string, now: Date = new Date()): Appointment`.**
The caller identifies the appointment by id, and `clientName` proves ownership, as the user asked (no login). `now` defaults to the real clock but tests pass a fixed value. The function returns the updated appointment, just as `book` returns the new one. *Alternative:* look up by `clientName` + `startsAt` with no id. Rejected because `book` already hands out ids, and the pair is ambiguous if a client ever has several bookings.

**Refusals throw an `Error` with a message for people to read.**
`book` returns an `Appointment` directly, so throwing keeps both functions consistent and their return types plain. Tests check messages with `assert.throws(..., /pattern/)`. Planned messages:
- `Appointment <id> not found.`
- `Appointment <id> does not belong to <clientName>.`
- `Appointment <id> is already cancelled.`
- `Appointments can only be cancelled at least 24 hours before they start; this one starts in less than 24 hours.`
- In `book`: `The slot at <startsAt> is already taken.`
*Alternative:* return a `{ ok: false, reason }` result. Rejected because it would split the module into two error styles and make callers unwrap every success.

**Order of checks: not found → wrong client → already cancelled → too late.**
Ownership comes before status and timing. This way a client who doesn't own the appointment learns nothing about its state beyond the fact that it isn't theirs.

**Notice rule: `startsAt.getTime() - now.getTime() >= 24 * 60 * 60 * 1000`.**
This compares elapsed milliseconds, so exactly 24 hours is allowed, and any past start time gives a negative value and is refused. Both `Date`s are built from clinic local time, and no time-zone conversion is done. Across a daylight-saving change, this means 24 real hours rather than "the same clock time the day before" (the user agreed to this).

**A slot is taken when some appointment has `status === "booked"` and the same `startsAt.getTime()`.**
`book` runs this check before it creates anything. Cancelled records stay in the array (with status `"cancelled"`) and are skipped by the check. Keeping them also keeps ids unique, because ids come from `appointments.length + 1`, which is only safe if nothing is ever removed.

**Type change:** `status: "booked" | "cancelled"`.

## Risks / Trade-offs

- [Module-level state is shared by every test in the same file] → Each test books at its own distinct start times and uses the `id` it gets back. It never assumes the store is empty. No reset function is added to the public API.
- [Breaking change: `book` now refuses double bookings] → Nothing in the repo calls `book` yet, so there are no callers to migrate. This is stated in the proposal.
- [Callers could pass `clientName` with different case or spacing] → The match is exact on purpose, and the spec says so. Normalising names is left for later.
- [Invalid `Date` inputs (`NaN`)] → Out of scope. They make the arithmetic fail and the cancellation is refused as too late, which errs on the safe side.
