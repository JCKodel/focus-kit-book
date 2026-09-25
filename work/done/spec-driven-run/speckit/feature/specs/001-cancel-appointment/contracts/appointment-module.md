# Contract: `src/appointment.ts` module API

The feature has no screen or HTTP endpoint. Its interface is the exported functions and types of
`src/appointment.ts`. Types are shown as TypeScript signatures. The implementation must match them.

## Types

```ts
export type AppointmentStatus = "booked" | "cancelled";

export type Appointment = {
  id: number;
  clientName: string;
  startsAt: Date;
  status: AppointmentStatus;
};

export type CancelRefusal = "not-found" | "not-yours" | "already-cancelled" | "too-late";
export type BookRefusal = "slot-taken";

export type Result<R extends string> =
  | { ok: true; appointment: Appointment }
  | { ok: false; reason: R; message: string };
```

## `book(clientName: string, startsAt: Date): Result<BookRefusal>`

**Changed.** It used to return `Appointment` directly.

| Condition                                                        | Result |
|------------------------------------------------------------------|--------|
| No `"booked"` appointment has `startsAt` at the same instant     | `{ ok: true, appointment }` with a new appointment whose `status` is `"booked"` |
| A `"booked"` appointment already has that instant                | `{ ok: false, reason: "slot-taken", message: "That time is already booked. Please choose another time." }` |

A refused booking adds nothing.

## `cancel(id: number, clientName: string, now: Date = new Date()): Result<CancelRefusal>`

**New.** The checks run in this order, and the first failing check decides the result:

| # | Condition                                                   | `reason`            | `message` |
|---|-------------------------------------------------------------|---------------------|-----------|
| 1 | No appointment with `id`                                    | `not-found`         | `No appointment with that number was found.` |
| 2 | `appointment.clientName !== clientName`                     | `not-yours`         | `You can only cancel your own appointments.` |
| 3 | `appointment.status === "cancelled"`                        | `already-cancelled` | `This appointment is already cancelled.` |
| 4 | `startsAt.getTime() - now.getTime() < 24 * 60 * 60 * 1000`  | `too-late`          | `Appointments can only be cancelled at least 24 hours before they start.` |
| — | Otherwise                                                   | —                   | `status` set to `"cancelled"`. Returns `{ ok: true, appointment }` |

Guarantees:

- On any refusal the stored appointment is unchanged (FR-004).
- On success the record stays in storage with `status: "cancelled"` (FR-005). Its slot is free at
  once for `book` (FR-006, SC-003).
- Checks 1 and 2 come before 3 and 4, so a client never learns about another client's appointment
  (spec edge case).
- A remaining time of exactly 24 h is accepted. Anything less, including a negative value (already
  started or past), is refused as `too-late` (FR-001, FR-002).
- `clientName` comparison is exact and case-sensitive. There is no login.
- No notification or other side effect.
- `now` exists so tests can fix the time. Production callers leave it out.
