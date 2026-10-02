# ADR-003: Calendar dates as "YYYY-MM-DD" strings

- **Date:** 2026-02-24
- **Status:** Accepted
- **Deciders:** Tamsin Oduya, Marek Szolt, Rafe Lindqvist
- **Consulted:** Bex Amadi

## Context

Almost every lending rule is about days (loaned, due, overdue, suspended, withdrawn), never time of day. A book is due *on Tuesday*, not at 23:59:59.999 local time.

The first prototype used `Date` objects everywhere. Within a week, three bugs:

1. A loan created at 00:30 showed as the previous day in one test run because the date was built in local time and printed in UTC.
2. `dueOn - loanedOn` came out as 13.958… days over the spring clock change, and one place used `Math.floor`, so a 14-day loan was "13 days".
3. Two tests compared `Date` objects with `deepEqual` and passed or failed depending on milliseconds.

`Date` is also mutable: Rafe found a helper calling `setDate` on its argument, quietly moving another loan's due date.

CardBox stores `DD/MM/YYYY` text, so our format must be convertible later; not a driver.

## Decision

- A domain date is a **calendar date**: a `"YYYY-MM-DD"` string. Type alias `CalendarDate = string` in `shared/dates.ts`.
- **No times of day and no time zones** in the domain model. If something later needs an instant (audit logs, say), it gets a different type outside the domain.
- All arithmetic goes through `shared/dates.ts`:
  - `addDays(date, days)` → `CalendarDate`
  - `daysBetween(from, to)` → whole days, negative when `to` is earlier
  - `isCalendarDate(value)` → validates format *and* that the date exists
- Internally the helpers parse as **UTC midnight** (`${date}T00:00:00Z`), do the maths in milliseconds, and convert back with `toISOString().slice(0, 10)`. UTC has no DST, so a day is always 86 400 000 ms.
- Domain functions never call "now". `today` is always passed in as a `CalendarDate`; the caller (eventually the app layer) decides what today is.

## Why not `Date` objects with times?

- They model instants; we have none. "Strip the time" discipline failed in the prototype.
- Local vs UTC confusion is built in (`getDate` vs `getUTCDate`; `new Date('2026-03-01')` is UTC, `new Date(2026, 2, 1)` local).
- Mutable, breaking our `readonly` plain domain objects.
- Awkward in tests: `deepEqual` works, but messages are unreadable and per-test construction is noise.

## Why not a date library?

- We've decided on no dependencies (see the Node notes). The three functions we need are about 20 lines.
- A library would bring its own types into every slice.

## Why not a number (days since epoch)?

Marek considered it. Trivial arithmetic, but unreadable test data and messages (`20514` vs `2026-03-01`), and Odile's staff will see exports. Strings sort correctly as-is — the deciding point.

## Consequences

Good:
- Dates are readable in tests, logs and fixtures. `{ dueOn: '2026-03-22' }` is obvious.
- Equality is `===`. `deepEqual` on whole Results just works.
- String comparison orders dates correctly because the format is fixed-width.
- No DST bugs as long as nobody bypasses `shared/dates.ts`.

Bad / to watch:
- `CalendarDate` is just `string`; the compiler won't stop `"tomorrow"`. Outside inputs must go through `isCalendarDate`. A branded type was skipped for now — too much ceremony for this size.
- `new Date(x)` in a slice breaks this ADR. Review catches it; Bex added a grep to the checklist.
- Nice display ("Tuesday 3 March") is presentation and needs its own formatting code.

## Follow-ups
- MS: tests for month end, year end and leap years in `shared/dates`.
- RL: convert remaining `Date` usages in the books and loans prototypes.
- TO: mention this ADR in the README.
