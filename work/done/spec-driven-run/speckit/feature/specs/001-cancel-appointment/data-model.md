# Data Model: Client Appointment Cancellation

**Feature**: [spec.md](./spec.md) | **Plan**: [plan.md](./plan.md)

All data lives in memory in the module-level `appointments` array in `src/appointment.ts`. Nothing
is persisted.

## Appointment

| Field        | Type                        | Notes                                                      |
|--------------|-----------------------------|------------------------------------------------------------|
| `id`         | `number`                    | `appointments.length + 1` at booking. Unique because records are never removed. |
| `clientName` | `string`                    | Who booked it. It is also the identity used for the ownership check (no login). |
| `startsAt`   | `Date`                      | Start instant, created from the clinic's local time. It identifies the slot. |
| `status`     | `"booked" \| "cancelled"`   | Widened from `"booked"`. Starts as `"booked"`.             |

**Validation rules**

- On `book`: refused with `slot-taken` if any appointment with the same `startsAt.getTime()` has
  status `"booked"` (FR-007). Cancelled appointments at that time don't block a booking (FR-006).
- On `cancel`: see the refusal order in [contracts/appointment-module.md](./contracts/appointment-module.md).

**State transitions**

```text
          book()                 cancel() — owner, ≥ 24 h before startsAt
  (none) ────────▶ booked ─────────────────────────────────────────▶ cancelled
                     │                                                   │
                     └── any refused cancel(): unchanged (FR-004)        └── terminal; record kept (FR-005)
```

`cancelled` is terminal. There is no un-cancel. To get the time back, the client makes a new
booking, which gets a new `id`.

## Slot (derived, not stored)

A start instant. It is **taken** when some appointment has `startsAt` at that instant and
`status === "booked"`, and **free** otherwise. Two `Date`s refer to the same slot when their
`getTime()` values are equal. No separate slot table exists.

## Result (cancellation or booking outcome)

```text
Result = { ok: true,  appointment: Appointment }
       | { ok: false, reason: RefusalReason, message: string }

RefusalReason = "not-found" | "not-yours" | "already-cancelled" | "too-late" | "slot-taken"
```

`cancel` returns only the first four reasons and `book` returns only `slot-taken`. The contract
lists the exact English message for each reason (FR-003, FR-010).
