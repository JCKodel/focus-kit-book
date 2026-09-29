# The four pieces

After this chapter you can place every file of a feature in one of the four pieces, view, orchestrator, use case and repository, on the client and on the server.
You can follow one event through them to a new state, and decide for a feature which pieces pay their way and which it does without.

## The four pieces

Chapter 6 gave FOCUS in one paragraph, in [the two choices](06-the-documents.md#the-two-choices), from this book's ADR-0016;[^book-adr-0016] this chapter shows its pieces in running code.
Every excerpt below comes from the guided project at its chapter tag [`book-v1/closing-a-milestone`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone), the code chapter 12 left, and is quoted as it ran; code nested inside a function is shown without its outer indentation.

The clinic took FOCUS whole in chapter 7, and its [`docs/01-Architecture.md`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/docs/01-Architecture.md), in the section "How the code is organized", gives the four pieces in a table:

| Piece | Does | Forbids |
|---|---|---|
| View | fires events, renders state | business rules, data access |
| Orchestrator | converts event to state, fetches, calls use cases, publishes state | deciding rules, persisting |
| Use Case | the only place for business rules; pure; takes data, returns a Result | IO, framework, domain exception |
| Repository | fetch and save; the only place an infra exception becomes a Result | business rules |

The same section lists the files of one slice, a folder `features/<feature>/`, with the piece each file plays:

```text
features/<feature>/
  rules.ts               Use Cases: pure, imported by client and server
  rules.test.ts
  route.server.ts        server Orchestrator: a Hono route
  repository.server.ts   server Repository: SQL
  repository.server.test.ts
  api.ts                 client Repository: fetch, network failure becomes a Result
  use<Feature>.ts        client Orchestrator: a React hook publishing one state
  <Feature>View.tsx      View
  strings.ts             every text the user reads in this feature
```

Read the "Forbids" column first: it is what keeps a piece to its job, so a view with a business rule or a repository that decides one breaks the table, whatever it does right.
The table's "domain exception", which a use case may not throw, is what this book calls a refusal, and the clinic's "errors as values" is the book's exceptions as values, both from [chapter 14](14-errors-and-slices.md#exception-refusal-error).
The orchestrator is what Flutter knows as a BLoC[^bloc] and .NET as the Mediator pattern, as in MediatR.[^mediatr]
The Clean of FOCUS is the layers of Clean Architecture[^clean-architecture] with one difference: a use case receives no repository, so a rule cannot reach I/O, even through an interface.[^book-adr-0016]

## Two sides, one set of rules

A clinic slice runs on two sides, the phone's browser and the server, and each side has its own orchestrator and its own repositories.

On the client, the orchestrator is the hook `use<Feature>.ts`.
Its repositories are `api.ts`, which reaches the network, and, in the booking slice, `remembered.ts`, which reaches the phone's storage.
The clinic's listing labels only `api.ts` as a repository; this book places `remembered.ts` there too, because it does a repository's job: the section "How data is accessed" of the same docs/01 makes it the only code that touches the phone's storage, and it returns its failure as a `Result`.

On the server, the orchestrator is the route `route.server.ts`, and the repository is `repository.server.ts`, which runs the SQL.

`rules.ts`, the use cases, is imported by both sides, and the clinic's docs/01 says why:

> "*The server enforces every rule. The client imports the same use case only to decide what to show (for example, whether the cancel button appears), so a rule is written once and tested once.*"

The view exists only on the client; on the server, the new state an event leads to is the answer to the request.

## One event, one new state

A client books an appointment: the tap on "Book" is the event, and the screen showing the booking code is the new state.
These are the steps between them.

**1. The view fires the event.** This is the form step of [`src/features/appointments/BookingView.tsx`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/BookingView.tsx):

```ts
case "form": {
	const timeZone = state.slots?.timeZone ?? "UTC";
	const submitForm = (event: FormEvent) => {
		event.preventDefault();
		submit();
	};
	return (
		<form noValidate onSubmit={submitForm}>
			<p>{summary(step.startsAt, timeZone, step.professional.name)}</p>
			{tooLateToCancel && <p>{strings.tooLateToCancel}</p>}
			<p>
				<label htmlFor="client-name">{strings.name}</label>
				<input
					id="client-name"
					autoComplete="name"
					value={state.name}
					onChange={(event) => typeName(event.target.value)}
					style={field}
				/>
				{state.nameError && (
					<span role="alert">{errorStrings[state.nameError]}</span>
				)}
			</p>
			<p>
				<label htmlFor="client-phone">{strings.phone}</label>
				<input
					id="client-phone"
					type="tel"
					autoComplete="tel"
					value={state.phone}
					onChange={(event) => typePhone(event.target.value)}
					style={field}
				/>
				{state.phoneError && (
					<span role="alert">{errorStrings[state.phoneError]}</span>
				)}
			</p>
			<div style={buttons}>
				<button type="submit" style={action} disabled={busy}>
					{strings.book}
				</button>
				{backButton}
			</div>
		</form>
	);
}
```

The view renders what `state` holds and hands every change to the hook, as `typeName`, `typePhone`, `back` or `submit`; the tap on "Book" submits the form, and `submitForm` calls `submit` and does nothing else.

**2. The client orchestrator.** This is `submit`, from [`src/features/appointments/useBooking.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/useBooking.ts):

```ts
// Name and phone are checked here to show the message beside the field
// and send nothing; the server checks them again.
const submit = useCallback(async () => {
	const { step, slots } = state;
	if (step.kind !== "form" || !slots) return;
	const name = checkClientName(state.name);
	const phone = checkClientPhone(state.phone);
	setState((s) => ({
		...s,
		nameError: name.ok ? undefined : name.error,
		phoneError: phone.ok ? undefined : phone.error,
	}));
	if (!name.ok || !phone.ok) return;

	setState((s) => ({ ...s, busy: true, failed: undefined }));
	const call = ++latest.current;
	const result = await postAppointment({
		professionalId: step.professional.id,
		startsAt: step.startsAt,
		clientName: state.name,
		clientPhone: state.phone,
	});
	if (call !== latest.current) return;
	if (result.ok) {
		const booked = result.value;
		// A storage failure leaves the code on screen: nothing else to do.
		remember(
			{
				bookingCode: booked.bookingCode,
				clientPhone: booked.clientPhone,
				professionalName: booked.professional.name,
				startsAt: booked.startsAt,
				timeZone: slots.timeZone,
			},
			new Date(),
		);
		setState((s) => ({
			...s,
			step: { kind: "booked", booked, timeZone: slots.timeZone },
			busy: false,
			name: "",
			phone: "",
		}));
		return;
	}
	const code = result.error.code;
	if (code === "ProfessionalNotFound") {
		return loadProfessionals("ProfessionalNotFound");
	}
	if (code === "SlotTaken") {
		return loadSlots(step.professional, {
			message: "SlotTaken",
			date: step.date,
		});
	}
	setState((s) => ({ ...s, busy: false, failed: "book" }));
}, [state, loadProfessionals, loadSlots]);
```

It calls the use cases `checkClientName` and `checkClientPhone` only to show a message beside a field, sends the booking through the repository `postAppointment`, keeps a copy on the phone through the repository `remember`, and publishes one new state, the step `booked`.

**3. The client repository.** This is `postAppointment`, from [`src/features/appointments/api.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/api.ts):

```ts
// The client checks name and phone with the same use cases before sending,
// so a 400 would mean the server cannot be relied on: it reads as
// ServerUnreachable, as in weeklyHours/api.ts.
export function postAppointment(
	body: BookingBody,
): Promise<Result<Booked, BookError>> {
	return request<Booked, NotFound | NotFree>(
		"/api/appointments",
		{
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify(body),
		},
		bookedOf,
		{ 404: { code: "ProfessionalNotFound" }, 409: { code: "SlotTaken" } },
	);
}
```

It reaches the network through `request`, from `src/lib/request.ts` in chapter 14, which returns the answer as a `Result`, and it names the two answers it expects as refusals: 404 is `ProfessionalNotFound` and 409 is `SlotTaken`.

**4. The server orchestrator fetches.** The request arrives at [`src/features/appointments/route.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/route.server.ts), whose `slotsOf` reads what a booking is checked against:

```ts
// What both routes read after the body: the active professional, the clinic
// and what the slots are cut from, with `now`; else the answer. Synchronous,
// so no other request of the process runs between this read and the insert.
function slotsOf(
	db: DatabaseSync,
	c: Context,
	professionalId: number | undefined,
	now: Date,
): Result<{ professional: Professional; input: SlotInput }, Response> {
	if (professionalId === undefined) return err(notFound(c));
	const active = findActiveProfessionals(db);
	if (!active.ok) return err(databaseFailed(c));
	const professional = active.value.find((p) => p.id === professionalId);
	if (!professional) return err(notFound(c));
	const clinic = findClinic(db);
	if (!clinic.ok) return err(databaseFailed(c));
	// A professional exists only once the clinic is set up; kept for the types.
	if (!clinic.value) {
		return err(c.json({ error: { code: "ClinicNotSetUp" } }, 500));
	}
	const { timeZone, slotMinutes } = clinic.value;
	const periods = findWorkingPeriods(db, professionalId);
	if (!periods.ok) return err(databaseFailed(c));
	const from = new Date(now.getTime() - slotMinutes * 60 * 1000);
	const booked = findBookedStarts(db, professionalId, from.toISOString());
	if (!booked.ok) return err(databaseFailed(c));
	return ok({
		professional,
		input: {
			periods: periods.value,
			booked: booked.value,
			timeZone,
			slotMinutes,
			now,
		},
	});
}
```

It asks four repository functions, from four slices, for the data: `findActiveProfessionals` from `professionals`, `findClinic` from `clinic`, `findWorkingPeriods` from `weeklyHours` and `findBookedStarts` from `appointments`.
`now` comes in as a parameter, and its `Result` holds either the data or the answer to send, built by `notFound` and `databaseFailed`, two helpers of the same file.

**5. The server orchestrator decides and saves.** This is the handler `.post("/appointments", ...)`, from the same file:

```ts
.post("/appointments", async (c) => {
	const body: unknown = await c.req.json().catch(() => undefined);
	if (!isBookingBody(body)) {
		return c.json({ error: { code: "BadRequest" } }, 400);
	}
	const read = slotsOf(db, c, body.professionalId, new Date());
	if (!read.ok) return read.error;
	const { professional, input } = read.value;
	const booking = book(body, input);
	if (!booking.ok) {
		const code = booking.error;
		return c.json({ error: { code } }, refusalStatus[code]);
	}
	const bookingCode = drawBookingCode();
	const inserted = insertAppointment(db, {
		professionalId: professional.id,
		bookingCode,
		...booking.value,
	});
	if (!inserted.ok) {
		const code = inserted.error.code;
		if (code === "SlotTaken") return c.json({ error: { code } }, 409);
		return databaseFailed(c);
	}
	return c.json(
		{
			bookingCode,
			startsAt: booking.value.startsAt,
			clientPhone: booking.value.clientPhone,
			professional,
		},
		201,
	);
})
```

In order: the body's shape, `slotsOf`, the use case `book`, whose refusal becomes a status through `refusalStatus` from [chapter 14](14-errors-and-slices.md#exceptions-as-values-in-the-clinic), the booking code, the repository `insertAppointment`, whose SQL is in the same section of chapter 14, and the answer 201.
`drawBookingCode` draws the code at random in the route, because randomness, like the clock, is the orchestrator's to supply, so no use case stops being pure; the clinic's docs/01 says it of the clock: "*Use cases take the current time as a parameter. No use case reads the clock.*"

**6. The use case decides.** This is `book`, from [`src/features/appointments/rules.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/rules.ts):

```ts
// The appointment to store, checked in order: name, phone, window, hours,
// taken. `startsAt` comes back as toISOString().
export function book(
	request: BookingRequest,
	input: SlotInput,
): Result<Booking, BookingRefusal> {
	const clientName = checkClientName(request.clientName);
	if (!clientName.ok) return clientName;
	const clientPhone = checkClientPhone(request.clientPhone);
	if (!clientPhone.ok) return clientPhone;

	const start = Date.parse(request.startsAt);
	const now = input.now.getTime();
	// A start that is not a date is in no window.
	if (!(start > now && start <= now + windowMs)) {
		return err("OutsideBookingWindow");
	}
	const startsAt = new Date(start).toISOString();
	if (!freeSlots({ ...input, booked: [] }).includes(startsAt)) {
		return err("OutsideWorkingHours");
	}
	if (!freeSlots(input).includes(startsAt)) return err("SlotTaken");
	return ok({
		startsAt,
		clientName: clientName.value,
		clientPhone: clientPhone.value,
	});
}
```

Data comes in, `now` inside `input`, and a `Result` comes out; it calls `checkClientName`, `checkClientPhone` and `freeSlots`, all in `rules.ts`, and no repository.

The way back needs no excerpt: the route answers 201, `postAppointment` returns the booking as a value, `submit` publishes the step `booked`, and the view renders it in its `case "booked"`, with the booking code.

The flow never goes back the wrong way: the view never sets the state, and a use case never calls a repository.
So "what happens when this event arrives?" has one answer, and chapter 16 turns it into a test.

## What the clinic injects

ADR-0016 says the orchestrator is the only piece with injected dependencies, and that those are the repositories.[^book-adr-0016]
The clinic chose something simpler.

The server's orchestrator receives the database, the driver, and passes it to each repository function: the route is `appointmentsRoute(db)`, and `slotsOf` and the handler above hand `db` to every repository call.
The clinic's docs/01 says why:

> "*Server routes that need the database are functions of it (`clinicRoute(db)`), so Vitest drives them through Hono's `app.request` against an in-memory SQLite (`testDatabase.server.ts`).*"

Vitest is the clinic's test runner, `app.request` sends a request to a route without a network, and `testDatabase.server.ts` holds `memoryDatabase`, from chapter 14.

The client's orchestrator injects nothing: `useBooking.ts` imports `postAppointment` from `api.ts` and `remember` from `remembered.ts`.

This is the clinic's choice, and its reason holds: in a language of plain functions, the one thing its tests swap is the database, so a repository object passed into every orchestrator would be a piece that exists for ceremony, which KISS rules out.
Chapter 16 shows the tests.

## When the pieces pay their way

A piece exists when it has a job.
A use case exists when there is a rule: the `health` slice of [chapter 14](14-errors-and-slices.md#vertical-slices) has none, so it has no `rules.ts`.
A repository exists when there is I/O, an orchestrator when an event leads to a new state, and a view when there is a screen.

The clinic's [ADR-0002](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/docs/adr/ADR-0002-focus-whole.md), the decision to take FOCUS whole, names the cost in its Consequences: "*A slice has more files than a component that fetches on its own; a file appears only when it pays its way.*"
Its Context names what the clinic buys with it: a product that values "*every rule has a test*", and a rule in a pure function is the cheapest place for one.

Where the code already has its own shape, the pieces can cost more than they give.
On the brownfield project of [chapter 8](08-analyze.md#focus-on-code-without-an-architecture), FOCUS whole meant a large refactor, and the answer was neither.
Between the two stands the kit's middle answer, the two principles alone of [chapter 14](14-errors-and-slices.md#two-principles-that-stand-alone): slices and exceptions as values, with no piece.
KISS, YAGNI and DRY decide, as [chapter 6](06-the-documents.md#the-two-choices) said: a piece is written when a delivery needs its job, and not before.

## Key points

* The view fires events and renders state, the orchestrator turns one event into one new state, a use case holds a rule as a pure function, and the repository is the only code that does I/O.
* A piece is written when it has a job, and the "Forbids" column keeps it to that job.
* In the clinic each side has its own orchestrator and repositories, and both import the same use cases: the server enforces a rule, and the client uses it only to decide what to show.
* An event flows one way: the view never sets the state, and a use case never calls a repository.
* The clinic's orchestrators receive the database, or nothing, in place of injected repositories, because the database is the one thing its tests swap.

## Exercises

These exercises use the clinic, by conversation with the agent, never by hand.

### Exercise 15.1

Ask the agent to sort every file of `src/features/professionals/` into the four pieces, client or server, and to name any code that does the job of another piece.
Anything it finds is a candidate for your queue, not a fix now.

### Exercise 15.2

A new rule: a client may hold at most two future appointments.
Ask the agent which files change and which do not, where the server enforces the rule and where the client uses it to decide what to show.
Nothing is built.

### Exercise 15.3

The home page gains a line of help, "Keep your booking code to cancel", written once in `strings.ts` and never edited by the owner.
Ask the agent which of the four pieces this needs, and why each other one does not pay its way.
Nothing is built.

[^book-adr-0016]: J.C. Ködel, "One Page at a Time", this book's ADR-0016, `docs/adr/ADR-0016-the-books-definition-of-focus.md`, dated 2026-09-28, in the ADR folder on `main`. <https://github.com/JCKodel/focus-kit-book/tree/main/docs/adr>
[^bloc]: Bloc, "Bloc State Management Library", documentation, accessed 2026-09-29. <https://bloclibrary.dev/>
[^mediatr]: Jimmy Bogard, "MediatR: Simple, unambitious mediator implementation in .NET", accessed 2026-09-29. <https://github.com/jbogard/MediatR>
[^clean-architecture]: Robert C. Martin, "The Clean Architecture", 2012. <https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html>
