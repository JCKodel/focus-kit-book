# Domain

| Term | In code | Meaning |
|---|---|---|
| Appointment | `Appointment` | A client's reserved time at the clinic |
| Appointment number | `id` | The number the module gives an appointment, from 1 |
| Client name | `clientName` | Who the appointment is for; the only identity a client has |
| Start time | `startsAt` | When the appointment starts, in the clinic's local time |
| Status | `status` | Where the appointment is in its life |
| Booked | `"booked"` | The status of an appointment just made; today the only one |
| Book | `book` | Make an appointment for a client at a start time |

## Entities
**Appointment**: `id: number`, `clientName: string`, `startsAt: Date`, `status: "booked"`.

## Invariants
Enforced today:
- An appointment number is unique within the running process, starting at 1 and rising by one.
- A new appointment's status is booked.

Not enforced yet (milestone 1): a non-empty client name; a start time not in the past; no two appointments in the same slot.
