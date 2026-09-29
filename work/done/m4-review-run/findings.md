### F1. Chapter 3's key point says both tools asked a question before writing, but only OpenSpec did
* Where: `book/en/03-spec-driven.md:195`, `book/pt/03-spec-driven.md:275`
* Question: 2
* What: The key point reads "Spec Kit and OpenSpec got three things right: the decision written before code in files the agent reads, rules written once per project, and a question asked before writing." The body (line 92) says "Spec Kit asked nothing" and wrote its answer under Assumptions. The body's point was the contrast between the two tools.
* Reader: A reader who keeps only the key points learns the opposite of what the run showed about Spec Kit.

### F2. The Portuguese edition translates "slot" as "horário livre" (free slot) in the clinic's invariant and ADR
* Where: `book/pt/06-the-documents.md:221`, `book/pt/06-the-documents.md:235`
* Question: 6
* What: "An appointment starts at a slot" becomes "Um agendamento começa em um horário livre". "Weekly hours are cut into slots" becomes "cortados em horários livres". The English invariant is about lining up with the `slotMinutes` grid. "Free slot" is a separate idea that the milestone paragraph uses ("book a free slot"), and the Portuguese uses the same words for both.
* Reader: A Portuguese reader reads invariant 2 as a rule about slots being free, and cannot tell the grid rule from the no-overlap rule.

### F3. Chapter 14 never says how to draw a feature's boundary, and its own example crosses one
* Where: `book/en/14-errors-and-slices.md:19`, `book/en/14-errors-and-slices.md:53`
* Question: 2
* What: The folder `appointments` is called "the booking slice", yet it holds `CancelView`, `useCancel` and the cancellation rule. `cancel-appointment` was a delivery of its own. Line 53 says "A change to booking touches this folder, and removing booking removes this folder." Taken literally, that would also remove cancelling. The chapter never says why booking and cancelling share one slice while `weeklyHours` and `professionals` get their own.
* Reader: The first clause of M4 is "organize code by feature", but the chapter never says what makes something one feature, so the reader cannot decide it for their own code.

### F4. Chapter 14 defines a refusal as having "no I/O involved", then shows one that comes from the database
* Where: `book/en/14-errors-and-slices.md:84`, `book/en/14-errors-and-slices.md:248`
* Question: 2
* What: The list defines "Refusal: a rule saying no, returned as a value, with no I/O involved". The key point says "a refusal only in a rule". Between them, the chapter's main example `SlotTaken` is a refusal made in the repository when a unique index rejects an insert, which is I/O (lines 129 to 167). The chapter doesn't reconcile the two.
* Reader: The reader gets two rules that clash and cannot classify the chapter's own main example with either of them.

### F5. Chapter 14 says an error is never caught, yet its `query` catches every thrown value, bugs included
* Where: `book/en/14-errors-and-slices.md:85`, `book/en/14-errors-and-slices.md:117`
* Question: 2
* What: "Error: a bug, thrown and never caught". Yet `query` wraps `run()` in `catch (error)` with no filter, so a malformed SQL statement or a `TypeError` in the closure becomes `DatabaseFailed`. The text says only that it "turns the database's exception into a value".
* Reader: Someone following the text cannot see from this code how a bug reaches "your screen" as the chapter promises. They may copy a catch-all that hides bugs as exceptions.

### F6. The Portuguese edition calls the server-check slice "fatia de saúde" (health, as in medical)
* Where: `book/pt/14-errors-and-slices.md:56`
* Question: 6
* What: `health` here is a server health check. Chapter 10 kept "fatia de health". In a clinic app whose documents exclude "qualquer dado de saúde" (any health data, chapter 7), "fatia de saúde" reads as the slice for medical data.
* Reader: A Portuguese reader may think the clinic has a slice for health data, which its own product rules forbid.

### F7. Chapter 15's tag contains an unnamed delivery, and its code is missing from everything the reader built
* Where: `book/en/15-four-pieces.md:9`, `book/en/16-testing-and-agents.md:330`
* Question: 5
* What: The tag is described as "the code chapter 12 left plus the clinic's first delivery of milestone 2". That delivery is never named. Its files (`<name>Events.ts`, `bookingEvents.ts`, `cancelEvents.ts`) are not in chapter 14's 22-file listing. It also matches none of the five milestone 2 lines chapter 12 queued. Chapter 16 mentions it only in passing ("before the event functions existed").
* Reader: A reader who built milestone 1 through exercises 11.4 and 12.3 has no client orchestrator split into event functions. They cannot tell which line of their queue produces it, or why their code differs from the tag.

### F8. Chapter 15's table says only the repository turns an I/O exception into a Result, but its route does it too
* Where: `book/en/15-four-pieces.md:18`, `book/en/15-four-pieces.md:298`
* Question: 2
* What: The table gives the repository as "the only place an infra exception becomes a Result". Chapter 6 (line 108) and key point 1 (line 432) say only the repository does I/O. Yet step 5 shows the route, an orchestrator, doing `c.req.json().catch(() => undefined)`. Chapter 14 (line 209) mentions that routes catch the body without squaring it with this rule, and chapter 15 does not either.
* Reader: The reader cannot tell whether reading a request body in the orchestrator follows FOCUS or breaks the "Forbids" column the chapter tells them to read first.

### F9. The hook excerpt calls `submitEvent`, but the text only ever speaks of `submit`
* Where: `book/en/15-four-pieces.md:207`, `book/en/15-four-pieces.md:223`
* Question: 2
* What: The text says the hook "reads `new Date()` and passes it to `submit`", but the code calls `submitEvent(snapshot, new Date())`. Nothing says that `submitEvent` is `bookingEvents.ts`'s `submit` imported under another name, because the hook has its own `submit`. `shown.current` and `latest.current` are not explained either.
* Reader: Someone following the code from the text cannot connect the event function of step 2 to the call in the hook, at the one step where the two files of the client orchestrator meet.

### F10. Chapter 15 sends code between slices, against chapter 14's rule that shared code moves to `src/lib/`
* Where: `book/en/15-four-pieces.md:291`, `book/en/14-errors-and-slices.md:69`, `book/en/16-testing-and-agents.md:334`
* Question: 2
* What: `slotsOf` "asks four repository functions, from four slices", importing from `professionals`, `clinic` and `weeklyHours`. Chapter 14 said "What two features already share leaves their slices for `src/lib/`", and that a slice holds everything its feature needs. Chapter 16 then calls `professionals/repository.server.ts` "shared code". No chapter says whether one slice may import another slice's repository.
* Reader: The reader is left without a rule for the most common case in organizing by feature: one feature reading another feature's data.

### F11. Chapter 15 says no piece but the orchestrator receives a dependency, yet every repository takes `db`
* Where: `book/en/15-four-pieces.md:413`, `book/en/15-four-pieces.md:436`
* Question: 2
* What: The key point says "no other piece receives a dependency", and line 413 says "Nowhere else is anything passed". Yet `insertAppointment(db, …)`, `findClinic(db)` and every repository function shown take the database driver as a parameter, and line 381 says the orchestrator "hands it to each repository function".
* Reader: The reader cannot state the injection rule in a form that matches the code, so they cannot apply it to their own repositories.

### F12. Chapter 15's "when they pay their way" test is circular and never shows a piece that does not pay
* Where: `book/en/15-four-pieces.md:418`
* Question: 2
* What: The criterion is "A piece exists when it has a job", with its counterpart for each piece (a rule, I/O, an event, a screen). The only cases where something does not pay are the health slice, which has no rule and so no job, and the brownfield project, which is about the whole architecture. No case shows a piece that has a job but costs more than it gives. The chapter's own new split of the client orchestrator into two files never gets its cost weighed.
* Reader: This is the section that carries M4's second half, and the reader leaves with a tautology rather than a way to weigh a piece's cost.

### F13. Chapter 16 defines a unit test as running "one piece", then treats its route test as a test of several pieces
* Where: `book/en/16-testing-and-agents.md:24`, `book/en/16-testing-and-agents.md:176`
* Question: 2
* What: "A test Vitest runs is a unit test: it runs one piece of code". The route test, also run by Vitest, drives the route, the use case `cancel`, the repository and a real SQLite. The chapter itself calls it "one event, one new state" as one test.
* Reader: The reader gets a definition of "unit test" that the chapter's own example breaks, and no line between it and the end-to-end test.

### F14. The text describes a parameterized test as if it were one test with one code
* Where: `book/en/16-testing-and-agents.md:242`
* Question: 2
* What: "In the first test the fake `postCancellation` answers `CancellationTooLate`". The code is an `it.each` over three codes (`AppointmentNotFound`, `CancellationTooLate`, `ServerUnreachable`) with `%s` in its name. Neither `it.each` nor the other two codes is explained.
* Reader: The reader cannot match the prose to the code, and misses that one test covers all three refusals.

### F15. "A slice keeps an agent's reading small" has no baseline, and the chapter's second count cuts against it
* Where: `book/en/16-testing-and-agents.md:359`
* Question: 2
* What: The key point rests on "20 of 95 files for a delivery inside one". The chapter gives nothing to compare it with, such as the same delivery without slices. The other count, `book-appointment` reading 33 of 77 files (43%), is left out of the conclusion.
* Reader: The reader takes a claim as measured that the record only describes, and gets no guide to what "small" means for their own project.

## Paragraph

a reader can organize code by feature: ch14 §Vertical slices · book-v1/closing-a-milestone
with exceptions as values: ch14 §Exceptions as values in the clinic · book-v1/closing-a-milestone
and knows when the four pieces pay their way: ch15 §When the pieces pay their way · book-v1/four-pieces
and when they do not: ch15 §When the pieces pay their way · book-v1/four-pieces
