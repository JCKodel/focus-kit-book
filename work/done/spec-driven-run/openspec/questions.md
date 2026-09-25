# OpenSpec: questions and answers

In the order asked, in the run that counts (permission mode `auto`). The answers follow the rule of `../brief.md`: the brief when it answers, the tool's default when it offers one, "the simplest option" otherwise.

## 1. `/opsx:propose`, first reply

The tool read the code and stopped before creating the change:

> **The question:** "A cancelled appointment frees its slot" doesn't change anything today, because slots are never held. I see two ways to handle it:
>
> 1. **(Recommended) Make slots real.** `book()` refuses a time that already has a *booked* appointment, and cancelled appointments don't count. This makes "frees its slot" something a test can check (book → cancel → rebook the same time succeeds). It also changes how `book()` behaves, which is outside the cancel feature itself.
> 2. **Keep it narrow.** Cancelling only sets `status: "cancelled"`. "Frees its slot" becomes a promise for later slot logic. `book()` stays as it is, and there's nothing observable to test for it.
>
> **Two smaller points I'll assume unless you say otherwise:**
> - **"Their own":** cancelling takes `(id, clientName, now)`. If `clientName` doesn't match the appointment's client, the cancel is refused with a message. The same goes for an unknown id or an appointment that's already cancelled.
> - **The 24-hour limit:** a cancel exactly 24 hours before the start is allowed. The check measures elapsed hours, so across a daylight-saving change the limit is still 24 real hours, not "same clock time the day before". `now` is a parameter so tests control the time.
>
> Which option do you want for slots, 1 or 2? And are the two assumptions fine?

Answer, with `--continue`:

> 1. The two assumptions: as you assume.

Why: option 1 is the one the tool marked as recommended, and the two assumptions are its own defaults.

## Discarded attempt

A first attempt in `acceptEdits` asked the same question in other words and got the same kind of answer, but the tool's own CLI (`openspec new change`, `status`, `validate`) was denied, so the agent wrote the change by hand without the templates. That is not the documented path; the change was deleted and the run repeated in `auto`, from the same installed state.
