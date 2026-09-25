# Product

## Purpose
Clinic Weigh-in (`clinic-weigh-in`) books appointments for a small clinic. It is a TypeScript module: a feature is a function the clinic's code calls with plain data, and it answers with plain data. It has no screen, no login and no storage beyond memory.

## Audience
One side: the clinic staff member who books an appointment on a client's behalf, through code that calls the module. Clients do not use it directly.

## Mechanics
- Staff book an appointment by giving the client's name and the time it starts. The module answers with the appointment: its number, the name, the time and its status, booked.
- A client is known only by the name given at booking. There is no account and no login.
- Every time is the clinic's local time.
- Appointments live in memory while the process runs; a restart starts empty.
- Nobody is notified of anything.

## Non-goals
- No screen: the product is the module's functions.
- No database, file or network storage.
- No accounts, login or client identity beyond the name.
- No time zones: one clinic, one local time.
- No notifications, by email, SMS or otherwise.
- No payments, records or clinical data.

## Values
Correct · Small · Explicit · Predictable · Plain
(Proposed from what the code is; change them by conversation.)

## Product questions
Every decision answers yes to all:
1. Can staff still do it with one function call and plain data?
2. Does every refusal come back as a value the caller reads, never as an exception?
3. Does it stay in memory, without login, notification or screen?
4. Is every time the clinic's local time?
5. Does it use the terms of docs/03?

## Open decisions
Nobody closes these alone; an agent never settles them by assumption.
- **Duration of an appointment.** `no-double-booking` must know when two appointments overlap; the code has only a start time.
- **What "local time" means in code.** `startsAt` is a `Date`, an absolute instant; it reads as the clinic's local time only if the process runs in the clinic's time zone.
- **Past bookings.** Is "now" the machine clock, and may staff record an appointment that already happened?
- **Same name, two clients.** With the name as the only identity, two clients with the same name are one client.
