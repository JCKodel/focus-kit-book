# Quickstart: Validate Client Appointment Cancellation

**Feature**: [spec.md](./spec.md) | **Contract**: [contracts/appointment-module.md](./contracts/appointment-module.md)

## Prerequisites

- Node.js 26+ (runs `.ts` files directly through type stripping)
- `npm install` (installs `typescript` and `@types/node`)

## Run

```sh
npm run typecheck   # tsc --noEmit — must report 0 errors
npm test            # node --test — runs src/appointment.test.ts
```

Both must pass. That is the constitution's merge gate.

## Scenarios the tests must cover

Each row maps to at least one test in `src/appointment.test.ts` (SC-005). In every test, `now` is
a fixed `Date` passed to `cancel`, and each test uses its own start time (see research R4, R7).

| # | Setup                                                    | Action                               | Expected |
|---|----------------------------------------------------------|--------------------------------------|----------|
| 1 | A books at `now + 3 days`                                | A cancels                            | `ok: true`, status `cancelled` |
| 2 | A books at `now + 24 h` exactly                          | A cancels                            | `ok: true` (boundary) |
| 3 | A books at `now + 23 h 59 min`                           | A cancels                            | `too-late`, 24-hour message, still `booked` |
| 4 | A books at `now − 1 h`                                   | A cancels                            | `too-late`, still `booked` |
| 5 | A books at `now + 3 days`                                | B cancels                            | `not-yours`, still `booked` |
| 6 | A books at `now + 1 h`                                   | B cancels                            | `not-yours`, not `too-late` (ownership first) |
| 7 | A books and cancels                                      | A cancels again                      | `already-cancelled` |
| 8 | —                                                        | cancel an unknown id                 | `not-found` |
| 9 | A books time T and cancels it in good time               | B books T                            | `ok: true` (slot freed) |
| 10| A books time T                                           | B books T                            | `slot-taken`, no new appointment |

"Still `booked`" means the test reads the appointment again after the refusal and confirms that
its `status` hasn't changed.

## Try it by hand

```sh
node --input-type=module -e '
import { book, cancel } from "./src/appointment.ts";
const r = book("Ann", new Date(Date.now() + 2 * 86_400_000));
console.log(r.ok && cancel(r.appointment.id, "Ann"));
'
```

Expected output: `{ ok: true, appointment: { ..., status: "cancelled" } }`.
