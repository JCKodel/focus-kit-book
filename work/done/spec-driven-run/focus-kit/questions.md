# focus-kit: questions and answers

In the order asked. The answers follow the rule of `../brief.md`: the brief when it answers, the tool's default (its recommendation) when it offers one, "the simplest option" otherwise. Two answers of `/propose` depart from that rule; they say so and why.

## 1. `/analyze`, first reply

After reading the repository, the tool asked five questions before writing anything:

> **1. Documentation language.** I recommend **English**, because the README is in English. Identifiers stay in English too.
>
> **2. Product.** The README says what it is but not who it's for. Please tell me in your own words:
> - Who uses it: reception staff, the clinicians, patients booking for themselves, or more than one of these?
> - What form it takes: a library, an API, a CLI or an app with screens?
>
> **3. How the code is organized.** FOCUS offers three options: [FOCUS whole; the two principles only; neither]. [...] I recommend **the two principles only**.
>
> **4. Git.** The options are: [trunk; a branch per delivery; a worktree per delivery]. [...] I recommend **trunk**.
>
> **5. First milestone.** There are no issues, TODO file or roadmap to read from. Please give me 3 to 8 deliveries, or tell me where they're listed. Here is a draft you can accept, edit or replace: [`verify`, `book-validation`, `no-double-booking`, `cancel`, `day-agenda`, `persistence`]

Answer, with `--continue`:

> 1. English. 2. Who uses it: the simplest option. What form it takes: there is no screen: the feature is a function in the module. Storage stays in memory. The client is identified by `clientName`, with no login. Times are the clinic's local time. Tests use `node --test`. No notification is sent. 3. The two principles only. 4. Trunk. 5. Your draft.

Why: 1, 3, 4 and 5 are the tool's recommendations; for 2 the brief answers the form (its "Answers" given verbatim) and not the user, so "the simplest option".

## 2. `/analyze`, second reply

The tool showed every file it would write and asked:

> **Your answers conflict in one place.** You said storage stays in memory, but my draft milestone included `persistence` ("appointments survive a restart"), which would break that. I've left `persistence` out of the queue below [...]. Say so if you want it back [...].
>
> For "who uses it: the simplest option", I wrote a single user: clinic staff booking on a client's behalf. Clients don't use it directly.
>
> Should I write these files? If you want `persistence` back in the queue, say so and I'll also rewrite ADR-0002 and the in-memory rule to match.

Answer, with `--continue`:

> Yes, write them. Persistence stays out.

Why: writing is what the command is for, and leaving `persistence` out is the tool's own choice.

## 3. `/propose cancel-appointment`, first reply

> **1. Slug.** I recommend using the existing queue line, `cancel`, and writing `work/cancel.md`. Otherwise I rename the line in docs/06 to `cancel-appointment`. Which do you want?
>
> **2. Order.** I recommend defining `verify` first (`/propose verify`) and coming back to cancel in queue order, so the Result shape is set by `book-validation` as planned. Or I write the cancel page now and add a prerequisite on the page: `/apply cancel` only after `verify` and `book-validation` are `[x]`. Which do you want?
>
> **3. How staff cancel.** I recommend `cancel(id: number)`, returning a Result: on success, the appointment with `status: "cancelled"`, which stays in memory. [...] Agreed?
>
> **4. Refusals.** I recommend two refusals: the appointment number doesn't exist; the appointment is already cancelled. [...] Which do you want?
>
> **5. Past appointments.** Can staff cancel an appointment whose start time has passed? This touches the open decision "Past bookings" in docs/00, so I won't settle it myself. I recommend leaving it out of scope and allowing it for now, with the page saying so.
>
> **6. Freed time slot.** Does a cancelled appointment free its slot for a new booking? I recommend yes, and that the page says `no-double-booking` ignores cancelled appointments. [...] Agreed?

Answer, with `--continue`, the feature and the answers of the brief first, since this is the first time the tool sees them:

> The feature: A client can cancel their own appointment up to 24 hours before it starts. A cancelled appointment frees its slot. A cancellation later than that is refused with a message that says why. Storage stays in memory. There is no screen: the feature is a function in the module. The client is identified by `clientName`, with no login. Times are the clinic's local time. Tests use `node --test`. No notification is sent.
> 1. cancel. 2. Write the page now, with the prerequisite. 3. As the feature above says; otherwise as you recommend. 4. As you recommend. 5. As you recommend. 6. Yes.

Why:

* 1 is the tool's recommendation, so the page is `work/cancel.md`, not the `work/cancel-appointment.md` the run planned; the author chose to keep the rule.
* 2 departs from the rule: the recommendation, define `verify` first, would end the run with no page for the feature the run exists to measure. The author chose the tool's other option.
* 3 is answered by the brief (a client cancels their own appointment, identified by `clientName`); 4, 5 and 6 are the tool's recommendations, and 6 is also the brief ("frees its slot").

The tool asked nothing more and wrote the page.
