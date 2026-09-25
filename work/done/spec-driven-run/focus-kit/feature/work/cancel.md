# cancel

**Prerequisite.** `/apply cancel` starts only when `verify` and
`book-validation` are `[x]` in docs/06. `verify` provides the command that
proves this delivery; `book-validation` fixes the Result shape this page uses.
If `no-double-booking` is also `[x]` by then, the slot scenario below
exercises it; if not, `no-double-booking` has to honour the same rule.

**Objective.** Staff can cancel an appointment for the client whose name it
carries, up to 24 hours before it starts. The cancelled appointment frees its
slot, and a refusal comes back with a message that says why.

**Behaviour.** In the scenarios, "now" is the time the caller passes in.
- Ada has appointment 1 on 12 March at 10:00. Staff cancel it at 11 March
  09:00 (25 hours before). The answer is appointment 1 with status cancelled.
- The same thing at exactly 11 March 10:00 (24 hours before) succeeds too.
- The same thing at 11 March 10:01 (23 h 59 min before) is refused with
  `too-late`. The appointment stays booked.
- Cancelling after the start time has passed is refused with `too-late`.
- Cancelling appointment 99 when it does not exist is refused with
  `not-found`.
- Cancelling appointment 1 with the name "Bob" is refused with
  `not-your-appointment`. The appointment stays booked. Names are compared
  exactly as given.
- Cancelling appointment 1 a second time is refused with `already-cancelled`.
- When more than one refusal applies, the first in this order wins:
  `not-found`, `not-your-appointment`, `already-cancelled`, `too-late`.
- After appointment 1 is cancelled, booking another client for 12 March at
  10:00 succeeds.
- A cancelled appointment stays in memory with its number. The next booking
  still gets the next number.
- No notification is sent. Nothing is written outside memory.

**Contract.** In `src/appointment.ts`:

    export type Appointment = {
      id: number;
      clientName: string;
      startsAt: Date;
      status: "booked" | "cancelled";
    };

    export const CANCELLATION_NOTICE_HOURS = 24;

    export type CancelError =
      | { code: "not-found"; message: "No appointment has this number." }
      | { code: "not-your-appointment"; message: "This appointment is booked under another name." }
      | { code: "already-cancelled"; message: "This appointment is already cancelled." }
      | { code: "too-late"; message: "An appointment can be cancelled up to 24 hours before it starts." };

    export function cancel(id: number, clientName: string, now: Date): Result<Appointment, CancelError>;

- `Result` is the shape `book-validation` fixes, with `Appointment` as the
  success value and `CancelError` as the error. If that shape does not carry
  an error with `code` and `message`, /apply stops and asks.
- Cancelling is allowed when `startsAt.getTime() - now.getTime() >=
  CANCELLATION_NOTICE_HOURS * 3_600_000`. The notice is elapsed time, not
  calendar days.
- `now` comes from the caller. The module does not read the clock, so this
  page does not settle the open decision about what "now" is.
- On success the stored appointment changes status and nothing is removed from
  the array, so the `id = length + 1` numbering holds.
- Refusals change nothing.

**Out of scope.**
- Rebooking or moving an appointment: that is a different delivery.
- Undoing a cancellation: nobody asked for it.
- Staff overriding the 24-hour rule: nobody asked for it.
- Telling apart two clients who share a name: that is an open decision in
  docs/00.
- Daylight-saving shifts inside the 24 hours: no time-zone handling
  (ADR-0008).
- Notifying anyone: ADR-0009.
- Listing cancelled appointments: that belongs to `day-agenda`.

**Done when.**
- A `node --test` test for each Behaviour scenario passes.
- `verify` is green.
- docs/03 moves the cancel invariants from "Not enforced yet" to "Enforced
  today".
- docs/00 Mechanics gains the cancel line.
- The docs/06 line `cancel` is `[x]`, and this page is in `work/done/`.
