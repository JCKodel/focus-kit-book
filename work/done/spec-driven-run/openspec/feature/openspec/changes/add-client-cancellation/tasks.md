# Tasks

## 1. Slots in booking

- [ ] 1.1 In `src/appointment.ts`, change `Appointment.status` to `"booked" | "cancelled"`. Verify: `node --test` still runs cleanly.
- [ ] 1.2 Make `book` throw `The slot at <startsAt> is already taken.` when an appointment with status `"booked"` has the same `startsAt.getTime()`. Check this before creating anything. Verify: the tests in 1.3 pass.
- [ ] 1.3 Create `src/appointment.test.ts` (using `node:test` and `node:assert/strict`, importing `./appointment.ts`). Add tests for "Booking a free start time" and "Booking a start time that is already taken". The second test also checks that no appointment was added (the next id is not skipped). Each test uses its own start times. Verify: `npm test` passes.

## 2. Cancellation

- [ ] 2.1 Export `cancel(id, clientName, now = new Date())` from `src/appointment.ts`. It runs the checks in the design's order (not found → wrong client → already cancelled → less than 24 hours' notice), throws the messages from design.md, and otherwise sets `status` to `"cancelled"` and returns the appointment. Verify: the tests in 2.2 pass.
- [ ] 2.2 In `src/appointment.test.ts`, add one test for each scenario in `specs/appointment-cancellation/spec.md`: 48 hours ahead succeeds; exactly 24 hours succeeds; 23h59m is refused and stays `booked`; after the start is refused; the wrong client is refused and stays `booked`; an unknown id is refused; cancelling twice is refused. Each refusal checks its message with a regex. Verify: `npm test` passes.
- [ ] 2.3 Add the test "Booking a start time whose appointment was cancelled" / "Rebooking a freed slot": book as "Ana", cancel in time, then book the same start time as "Ben" and expect `booked`. Verify: `npm test` passes.

## 3. Wrap-up

- [ ] 3.1 Add one line to `README.md` saying clients can cancel with 24 hours' notice via `cancel(id, clientName, now)`. Verify: `npm test` passes and `openspec validate add-client-cancellation --strict` reports the change as valid.
