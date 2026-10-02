marek — dates scratch notes
===========================

(working notes, not a spec. ADR-003 is the actual decision.)

---

### 20 Feb — the DST thing

Reproduced the prototype bug. Our clocks go forward on the last Sunday of March. Building dates in local time:

```
new Date(2026, 2, 28)  // Sat 28 Mar, local midnight
new Date(2026, 2, 30)  // Mon 30 Mar, local midnight
(b - a) / 86400000     // 1.9583333…
```

Two calendar days, 47 hours. `Math.floor` → 1: the prototype's "13-day loan" bug. Autumn goes the other way: 49 hours → 2.04, floor fine, ceil not. Whatever rounding you pick, local time is wrong one way or the other.

Also `new Date('2026-03-28')` (date-only ISO) parses as **UTC**, but `new Date('2026-03-28T00:00')` as **local**. Same-looking input, different instant. Lovely.

Conclusion: never local time. Always parse as `YYYY-MM-DDT00:00:00Z` explicitly.

---

### 23 Feb — why Math.round in daysBetween

With everything at UTC midnight, differences are exact multiples of 86 400 000 ms (no DST in UTC; JS ignores leap seconds), so `/ MS_PER_DAY` should already be an integer.

Kept `Math.round` anyway:
- belt and braces: a sneaked-in non-midnight value gives the *nearest* day, the least surprising answer
- `floor` is wrong for negatives (−0.0001 → −1)
- `trunc` would silently hide off-by-a-few-hours errors in one direction

Rafe: does round hide bugs? Possibly, but a non-midnight value only reaches `toUtcMs` by bypassing `isCalendarDate` — the real bug.

Negative results are deliberate: `daysBetween('2026-03-10', '2026-03-01') === -9`. Callers compare with `> 0` etc.

---

### 24 Feb — validating: isCalendarDate

Regex alone isn't enough: `/^\d{4}-\d{2}-\d{2}$/` accepts `2026-02-30` and `2026-13-01`.

`Date.parse('2026-02-30T00:00:00Z')` doesn't fail either — it rolls over to 2 March. So:

1. matches the pattern
2. `Date.parse` isn't NaN
3. round-trip: `new Date(ms).toISOString().slice(0, 10) === value`

Step 3 catches rollover. If the date "moved", it didn't exist.

Cases to test:
- `2026-02-30` → false
- `2026-04-31` → false
- `2026-13-01` → false
- `2026-1-5` → false (no padding)
- `2026-01-05 ` → false (trailing space; trimming is the caller's job)
- `20260105` → false
- `2026-01-05` → true

---

### 25 Feb — leap years

- 2026, 2027 not leap; 2028 is.
- `isCalendarDate('2026-02-29')` → false, `isCalendarDate('2028-02-29')` → true
- 2100 is *not* leap (div by 100, not 400); 2000 was. Irrelevant for loans but cheap: `2100-02-29` → false.
- `addDays('2028-02-28', 1)` → `2028-02-29`; `addDays('2028-02-28', 2)` → `2028-03-01`
- `daysBetween('2028-02-01', '2028-03-01')` → 29

---

### 10 Mar — month & year ends

Loan period is 21 days after the March meeting, so updated examples:

- `addDays('2026-12-20', 21)` → `2027-01-10` (year end). In loans.test.ts as "computes due dates across month and year ends".
- `addDays('2026-01-31', 1)` → `2026-02-01`
- `addDays('2026-03-31', 21)` → `2026-04-21`
- across the March clock change: `addDays('2026-03-20', 21)` → `2026-04-10`. Passes in any TZ since nothing touches local time; ran it with `TZ` at +13:00 and −03:30.

---

### 12 Mar — things I keep having to explain

- "Why not `new Date()` in the function?" — then it depends on the clock and every test fakes time. `today` is a parameter; tests pick any day.
- "Can I compare dates with `<`?" — yes, for valid `YYYY-MM-DD` strings lexical order is date order. Prefer `daysBetween` when you need a count.
- "What about year 10000?" — no.

---

### todo / ideas
- [ ] branded `CalendarDate` type? Skipped in ADR, revisit if a bad string gets in
- [ ] `compareDates` helper? String compare works (fixed-width) — probably unneeded
- [ ] display formatting ("Tuesday 3 March") lives outside the domain, not my problem yet
- [x] run date tests under odd TZ values
