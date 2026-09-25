# Proposal

## Why

Clients can book appointments but have no way to cancel one, so a slot they can no longer use stays taken. Clients need to cancel their own appointments with enough notice (24 hours) that the clinic can give the slot to someone else. Today `book()` does not track slots at all: two clients can book the same start time. So "freeing a slot" only means something once booking respects slots.

## What Changes

- Add a `cancel` function to `src/appointment.ts`. A client, identified by `clientName`, uses it to cancel their own appointment.
- A cancellation is allowed only when the appointment starts at least 24 hours after the moment of cancellation. Exactly 24 hours before is still allowed.
- A refused cancellation throws an error whose message says why: too late (less than 24 hours before the start), not the client's appointment, unknown appointment, or already cancelled.
- A cancelled appointment keeps its record, gets the status `"cancelled"`, and no longer holds its slot.
- **BREAKING**: `book()` now refuses a start time that already has a booked appointment. Cancelled appointments don't count. Code that relied on double-booking the same time will now get an error.
- `Appointment.status` widens from `"booked"` to `"booked" | "cancelled"`.
- Add tests under `node --test` for booking and cancellation.

Not in scope: notifications, login or authentication, a user interface, persistent storage, time-zone conversion (all times are the clinic's local time), and rules for overlapping durations (a slot is one exact start time).

## Capabilities

### New Capabilities
- `appointment-booking`: booking an appointment for a client at a start time, including the rule that only one booked appointment can hold a given start time.
- `appointment-cancellation`: a client cancelling their own appointment, the 24-hour notice rule, refusal messages, and releasing the slot.

### Modified Capabilities
<!-- None: no specs exist yet. -->

## Impact

- Code: `src/appointment.ts` gets a new `cancel` export, a slot check in `book`, and a wider `status` type.
- Tests: new `src/appointment.test.ts`, run by the existing `npm test` (`node --test`).
- Dependencies: none added. Storage stays in memory.
