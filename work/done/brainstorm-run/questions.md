# Questions and answers

Each round is the agent's message as it ended the turn, whole, then the answer given in the next turn, whole. Every answer is a section of `brief.md` word for word, or "your call". The agent used no question form: headless mode offers none, so it asked in text.

## Round 1: the product (subject 1)

Turn 1, the agent:

````markdown
Your README already tells me a lot: a scheduling app for a neighbourhood clinic, with a customer side and an owner side. I'll use that as the starting point and propose defaults. Tell me where they're wrong, or say "your call" and I'll keep them.

## 1. The product

**My draft, in one sentence:** *A web app where a small neighbourhood clinic's patients book, move and cancel their own appointments, and the clinic's owner sets their availability and sees the day's schedule.*

I need four answers to write docs/00:

1. **What kind of clinic, and how big is it?** My default: one location, a few practitioners (1 to 5), each offering a small list of services with fixed durations (for example "consultation, 30 min"). Does that fit, or is it a single practitioner, or several locations?

2. **How does a patient get in?** My default: they sign in with just an email (a magic link, no password). The clinic only needs a name and a phone number to call them back. The other option is to let people book as guests with no account, which is easier for them but makes cancelling and spotting no-shows harder.

3. **What is it *not*?** My proposed non-goals:
   - no payments or deposits
   - no medical records, diagnoses or clinical notes (we store only schedule data, which keeps us out of health-data regulations)
   - no insurance or billing
   - no video consultations
   - no marketplace of clinics: the app serves exactly one clinic

   Should anything come off this list, or go on it?

4. **What does a good decision look like here?** My default values, in order: **simple for the patient** (booking in under a minute on a phone), **trustworthy schedule** (never a double booking, never a slot the owner didn't open), **little work for the owner**, **privacy**, **cheap to run**. When two of them conflict, the one higher on the list wins. Does the order hold?
````

Turn 2, the answer. The brief's sections Product and Principles.

````markdown
## Product
A scheduling app for one neighbourhood clinic. Clients book and cancel their own appointments with the clinic's professionals from their phones; the owner registers the professionals and their weekly hours.
Two sides: the client, who has no account and gives a name and a phone number; the owner, who signs in (your call how).
Rules: a professional cannot have two appointments at the same time. A client can cancel their own appointment up to 24 hours before it starts; a cancelled appointment frees its slot; a later cancellation is refused with a message that says why. Times are the clinic's local time.
Not: payments, notifications (SMS, email, push), medical records or any health data, more than one clinic.

## Principles
Keep it simple. Every rule has a test. No em dash in any document.
````

## Round 2: the product's gaps and the vocabulary (subjects 1 and 2)

Turn 2, the agent:

````markdown
That covers docs/00 almost whole. I'm keeping "keep it simple" and "every rule has a test" as values, and "no em dash" as a non-negotiable. For owner sign-in, my call: **one owner account, email and password**, handled by whatever the stack provides, with no sign-up screen. There's one owner per clinic, so the account is created once at setup.

Three gaps are left in the product, and each one changes the vocabulary, so I'm handling both subjects in this round.

## 1. Product gaps

1. **How does a client with no account prove an appointment is theirs when cancelling?** With no notifications, the proof has to appear on screen at booking time. My default: after booking, the client sees a **short booking code** (6 characters) and the device remembers it. To cancel, they enter phone number + code, or tap the appointment the device remembers. Is that OK?

2. **How long is an appointment?** My default: **one fixed length for the whole clinic, 30 minutes**, set by the owner. Weekly hours are cut into slots of that length. The alternatives are a length per professional or per service. Both add a concept, and you said "keep it simple".

3. **How far ahead can clients book?** My default: from the next slot that hasn't started yet up to **30 days ahead**, with no limit on how many appointments one phone number holds.

I'll also record two things as **open decisions**, which no delivery may settle by assumption: what happens to future appointments when the owner removes a professional or changes their hours (my default for now: those appointments stay), and whether the owner can cancel a client's appointment.

## 2. Vocabulary (docs/03)

Here's my draft. Correct any word that isn't how you'd say it:

| Term | In code | Meaning |
|---|---|---|
| Clinic | `Clinic` | The one clinic the app serves; holds the time zone and slot length |
| Owner | `Owner` | The person who runs the clinic and signs in |
| Professional | `Professional` | Someone clients book with |
| Weekly hours | `WeeklyHours` | A professional's recurring availability |
| Working period | `WorkingPeriod` | One weekday + start + end inside the weekly hours |
| Slot length | `slotMinutes` | The fixed length of every appointment |
| Slot | `Slot` | A free interval of one professional, derived from weekly hours minus appointments; never stored |
| Client | `Client` | Whoever books: name + phone, no account |
| Appointment | `Appointment` | One client, one professional, one start time |
| Status | `AppointmentStatus` | `booked` or `cancelled` |
| Booking code | `bookingCode` | The code that proves an appointment belongs to the client |
| Book | `book` | Create an appointment in a free slot |
| Cancel | `cancel` | Mark an appointment cancelled, which frees its slot |
| Cancellation deadline | `cancellationDeadline` | 24 hours before the start; after it, cancel is refused |
| Clinic time | `clinicTimeZone` | All times are shown and reasoned in this zone |
| Slot taken | `SlotTaken` | The refusal when two bookings race for one slot |
| Too late to cancel | `CancellationTooLate` | The refusal after the deadline, with its message |

**4.** Is **"client"** the right word, rather than "patient"? I'm keeping yours because "patient" hints at health data, which is a non-goal.
````

Turn 3, the answer. No section of the brief answers these questions, so the rule of its last section applies.

````markdown
your call
````

## Round 3: how it is built, FOCUS and git (subject 3)

Turn 3, the agent:

````markdown
Everything stays as I drafted it: booking code, 30-minute clinic-wide slots, 30 days ahead, "client", and the two open decisions.

## 3. How it is built (docs/01)

What the product needs from the stack:
- a phone-first web page for clients, with no install and no account
- a sign-in for one owner
- a **server that holds the rules**, because a phone can't be trusted to enforce the 24-hour deadline or stop double bookings
- rules that are easy to test, since every rule has a test

**1. Stack. My recommendation: one TypeScript web app (SvelteKit) with a SQLite database, on one small server.**
- It's one language and one project, and the rules run on the server as plain functions that Vitest tests in milliseconds.
- A double booking is impossible at the database level: slots are aligned, so a unique index on (professional, start) over booked appointments settles any race.
- The owner's sign-in is a hashed password plus a session cookie, about a page of code.
- The data is one file, and a backup is a copy of that file.

The alternative is a thin page over a hosted backend service (Postgres plus built-in sign-in). You get hosting and auth for free, but the rules would live in SQL functions and be tested in a second language. That's a worse fit for "every rule has a test" and "keep it simple". Does the recommendation hold?

**2. How the code is organized.** The kit offers FOCUS, an architecture in four pieces where data flows one way:
- the **screen** only shows state and reports what the user did
- an **orchestrator** turns what the user did into the next state
- **use cases** hold every business rule as pure functions that take data and return a result or a refusal
- a **repository** is the only code that talks to the database

Code is grouped by feature (book, cancel, weekly hours…), not by layer, and errors are returned as values instead of thrown.

You can take it whole, take only the two principles (feature folders + errors as values), or take neither. **My recommendation: FOCUS whole.** It maps onto SvelteKit with no extra machinery: the page is the screen, the page's server file is the orchestrator, `rules.ts` holds the use cases and `repository.ts` holds the queries. It also puts the 24-hour rule and the slot rule in pure functions, which is where "every rule has a test" is cheapest.

**3. Git.** In every option the agent never commits or merges; it stages and suggests the message. You can work on the main branch one delivery at a time and review and commit after each. Or each delivery gets its own branch that you merge. Or each delivery gets its own branch in a separate folder, so several agents can build at once. **My recommendation: the main branch**, since you're one person working through one delivery at a time.
````

Turn 4, the answer. The brief's sections Stack and Choices.

````markdown
## Stack
TypeScript, strict. A React PWA that the client and the owner open in the browser, over a small Node server that keeps the data in a SQLite file. No paid service: it runs on a machine at the clinic or on any free host.
Why: the most public code the agent learned from is in this language and library, and types and tests let it check its own work.

## Choices
FOCUS: FOCUS whole. Git: trunk.
````

## Round 4: the conventions and the process slots (subjects 4 and 5)

Turn 4, the agent:

````markdown
FOCUS whole and trunk it is. Here are the smaller choices I'll make within your stack, unless you object:

- **Vite** builds the React PWA.
- **Hono** runs the Node server. It's small and TypeScript-first, and it runs anywhere Node runs.
- **`node:sqlite`**, the SQLite driver built into Node, reads and writes the database. It needs no native package, so any free host can run it.
- The **owner's password** is hashed with `node:crypto` (scrypt), and the session travels in an httpOnly cookie. No auth library.
- **FOCUS in this stack:**
  - the React component is the View
  - a hook per feature is the client's Orchestrator
  - a Hono route is the server's Orchestrator
  - the Repository is SQL on the server, and on the client a `fetch` wrapper that turns network failures into values
- **The use cases live in a shared folder that both sides import.** The server enforces the 24-hour rule, and the client uses the same function to decide whether to show the cancel button. That's one function in one place with one test, not a copy.

## 4. Conventions and 5. Process

Defaults, in one block:

- **Languages:** documentation in English, identifiers in English.
- **Style:** Biome formats and lints in one tool, with TypeScript `strict`.
- **Tests:** Vitest, with each `x.test.ts` next to the file it tests.
  - Every use case has unit tests: pure, no database, a fixed clock.
  - Repositories are tested against an in-memory SQLite.
  - Screens are tested end to end with Playwright.
- **Commits:** imperative subject up to 72 characters, scope in parentheses when it helps, and a last line pointing to `work/done/<slug>.md`.
- **Verify:** `npm run verify`, which runs typecheck + lint + tests + build. It's created by the first delivery.
- **Proof of a screen:** Playwright screenshots of the client side at phone width (390×844) and of the owner side at phone and desktop width (1280×800), with no design file; the page's Behaviour section is the reference.
- **Publish policy:** the agent never deploys. You update any environment beyond your own machine.

Three questions this round:

1. **What language are the screens in?** This is the text clients read, not the code. My default: English, with every user-facing string in one file per feature so a translation is a later delivery, not a rewrite.
2. **Environments:** my default is that milestone 1 runs only locally (`npm run dev`), and "production" (a machine at the clinic or a free host) is a delivery of its own at the end of the milestone. Should it be deployed earlier than that?
3. **Is there a visual design** (a sketch, a Figma file, a brand colour), or is plain, clean default styling fine for now?
````

Turn 5, the answer. The brief's section Conventions and process.

````markdown
## Conventions and process
English for documents and identifiers. Verify: created by the first delivery. Everything else: your call.
````

## No round 5: the first milestone

Turn 5 wrote the documents without asking about the first milestone, subject 6 of the command, so the brief's section First milestone was never given as an answer. The queue it wrote put the owner's view of the day in milestone 1, which the brief puts in the second. The author's review chose the fix: give that section, word for word, as turn 6, in the same session.

Turn 6, the answer. The brief's section First milestone.

````markdown
## First milestone
When it closes, the owner can register professionals and their weekly hours, a client can book a free slot, and a client can cancel up to 24 hours before. A professional's absences and the owner's view of the day come in the second milestone.
````

The agent's reply is `turn-6.txt`; the change it made is `turn-6.diff`.
