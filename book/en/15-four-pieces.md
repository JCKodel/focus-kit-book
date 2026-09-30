# The four pieces

After this chapter you can place every file of a feature in one of the four pieces, view, orchestrator, use case and repository, on the client and on the server.
You can follow one event through them to a new state, and decide for a feature which pieces pay their way and which it does without.

## The four pieces

Chapter 6 gave FOCUS in one paragraph, in [the two choices](06-the-documents.md#the-two-choices), from this book's ADR-0016;[^book-adr-0016] this chapter shows its pieces in running code.
Every excerpt below comes from the guided project at its chapter tag [`book-v1/four-pieces`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/four-pieces), the code chapter 12 left plus the clinic's delivery [`orchestrator-tests`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/work/done/orchestrator-tests.md) of milestone 1.1 (that tag's docs/06 still calls it milestone 2; chapter 12 says why), and is quoted as it ran; code nested inside a function is shown without its outer indentation.

`orchestrator-tests` is not a finding of the review: the author put its line in milestone 1.1 because chapter 16 needed client orchestrators with tests.
If you follow the clinic, add that line as the first of the milestone 1.1 that exercise 12.3 wrote, as the clinic's queue has it, and add "every client orchestrator has unit tests" to that milestone's paragraph:

```
[ ] orchestrator-tests   every use<Feature>.ts hook's events move to plain functions with repositories as a parameter, tested in Node
```

Then run `/propose orchestrator-tests`; I ran it headless in Claude Code and answered its first round of questions with the author's brief, word for word, where "milestone 2" is your milestone 1.1:[^clinic-orchestrator-tests-run]

```
Every client orchestrator, each use<Feature>.ts hook, gets unit tests. Move what each event does out of the hook: the calls to repositories and use cases, in their order, and the new state go into plain functions that receive their repositories as a parameter, the real ones by default, and `now` where a use case needs the clock, and return the new state. The hook only holds the state, publishes the in-flight state and publishes what the function returns. The tests pass fake repositories, in Vitest in Node, with no module mock and no new dependency. Server routes do not change. The app behaves exactly as before. Add the line as the first of milestone 2.
```

Every later round was answered with the rule of chapter 10's brief, `Your call. Say what you chose and why.`; then run `/apply orchestrator-tests` before you read on.

The clinic took FOCUS whole in chapter 7, and its [`docs/01-Architecture.md`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/docs/01-Architecture.md), in the section "How the code is organized", gives the four pieces in a table:

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
  <name>Events.ts        client Orchestrator: the hook's state, its initial
                         value, and what each event does, as plain functions
  <name>Events.test.ts
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

On the client, the orchestrator is two files.
`<name>Events.ts` holds what each event does, as plain functions: the calls to repositories and use cases, in order, and the new state.
The hook `use<Feature>.ts` is only the React part: it holds the state, publishes the in-flight state and the answer, reads the clock, and drops a stale answer.
The orchestrator's repositories are `api.ts`, which reaches the network, and, in the appointments slice, `remembered.ts`, which reaches the phone's storage.
The clinic's listing labels only `api.ts` as a repository; this book places `remembered.ts` there too, because it does a repository's job: the section "How data is accessed" of the same docs/01 makes it the only code that touches the phone's storage, and it returns its failure as a `Result`.

On the server, the orchestrator is the route `route.server.ts`, and the repository is `repository.server.ts`, which runs the SQL.

`rules.ts`, the use cases, is imported by both sides, and the clinic's docs/01 says why:

> "*The server enforces every rule. The client imports the same use case only to decide what to show (for example, whether the cancel button appears), so a rule is written once and tested once.*"

The view exists only on the client; on the server, the new state an event leads to is the answer to the request.

## One event, one new state

A client books an appointment: the tap on "Book" is the event, and the screen showing the booking code is the new state.
These are the steps between them.

**1. The view fires the event.** This is the form step of [`src/features/appointments/BookingView.tsx`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/BookingView.tsx):

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

In this step the view reads two values from the hook, `state` and `tooLateToCancel`, and hands every change to the hook, as `typeName`, `typePhone`, `back` or `submit`; the tap on "Book" submits the form, and `submitForm` calls `submit` and does nothing else.

`tooLateToCancel` looks like a business rule in the view, the first thing its "Forbids" names, so follow it back.
The hook computes it on every render as `tooLateToCancel(state, new Date())`, reading the clock as the hook does.
The function of that name is in [`src/features/appointments/bookingEvents.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/bookingEvents.ts), the client orchestrator, and is true only on the form step when the appointment's cancellation deadline is already before `now`:

```ts
// Display only: the server does not refuse such a booking.
export function tooLateToCancel(state: BookingState, now: Date): boolean {
	return (
		state.step.kind === "form" &&
		cancellationDeadline(state.step.startsAt).getTime() < now.getTime()
	);
}
```

The comment is the clinic's: the line warns the client and refuses nothing, the booking still goes through, and it is cancelling after the deadline that the server refuses.
The deadline itself is `cancellationDeadline`, in `rules.ts`: 24 hours before the appointment starts, as its comment says, and the use case `cancel`, which the server's route runs when a client cancels, calls it too.
So the rule is written once, in the use case, and the view holds none: it receives a boolean and shows or hides a line of `strings.ts`.
This is what the clinic's docs/01 means by the client importing the same use case "only to decide what to show", here in the booking form.

**2. The client orchestrator.** Its events are plain functions in [`src/features/appointments/bookingEvents.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/bookingEvents.ts); booking takes two, `submitStarted` and `submit`:

```ts
// Name and phone are checked here to show the message beside the field
// and send nothing; the server checks them again.
export function submitStarted(state: BookingState): {
	state: BookingState;
	send: boolean;
} {
	if (state.step.kind !== "form" || !state.slots) return { state, send: false };
	const name = checkClientName(state.name);
	const phone = checkClientPhone(state.phone);
	const checked = {
		...state,
		nameError: name.ok ? undefined : name.error,
		phoneError: phone.ok ? undefined : phone.error,
	};
	if (!name.ok || !phone.ok) return { state: checked, send: false };
	return { state: { ...checked, busy: true, failed: undefined }, send: true };
}

// `state` is the one `submitStarted` accepted.
export async function submit(
	state: BookingState,
	now: Date,
	repositories = bookingRepositories,
): Promise<BookingOutcome> {
	const { step, slots } = state;
	if (step.kind !== "form" || !slots) return { update: (s) => s };
	const result = await repositories.postAppointment({
		professionalId: step.professional.id,
		startsAt: step.startsAt,
		clientName: state.name,
		clientPhone: state.phone,
	});
	if (result.ok) {
		const booked = result.value;
		// A storage failure leaves the code on screen: nothing else to do.
		repositories.remember(
			{
				bookingCode: booked.bookingCode,
				clientPhone: booked.clientPhone,
				professionalName: booked.professional.name,
				startsAt: booked.startsAt,
				timeZone: slots.timeZone,
			},
			now,
		);
		return {
			update: (s) => ({
				...s,
				step: { kind: "booked", booked, timeZone: slots.timeZone },
				busy: false,
				name: "",
				phone: "",
			}),
		};
	}
	const code = result.error.code;
	if (code === "ProfessionalNotFound") {
		return { next: "loadProfessionals", message: "ProfessionalNotFound" };
	}
	if (code === "SlotTaken") {
		return {
			next: "loadSlots",
			professional: step.professional,
			after: { message: "SlotTaken", date: step.date },
		};
	}
	return { update: (s) => ({ ...s, busy: false, failed: "book" }) };
}
```

`submitStarted` checks name and phone with the use cases `checkClientName` and `checkClientPhone`, only to show a message beside a field, and gives the in-flight state, with `busy` set.
`submit` sends the booking through the repository `postAppointment` and keeps a copy on the phone through the repository `remember`, both reached through `repositories`, with `now` passed in; it returns either an update to the state, the step `booked`, or the next event to run: `loadProfessionals` when the professional is gone, `loadSlots` when the slot was taken.

The `submit` the view calls is the hook's own, which hands the event to `run`, so the hook imports `bookingEvents.ts`'s `submit` as `submitEvent`.
Here are the hook's state, its two refs and `run`, from [`src/features/appointments/useBooking.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/useBooking.ts):

```ts
const [state, setState] = useState<BookingState>(initialBookingState);
// Only the answer to the latest request is shown; Back or another tap
// makes earlier ones stale.
const latest = useRef(0);
// The state last shown: what a booking sends.
const shown = useRef(state);
shown.current = state;

// Any event with a call: its in-flight state, then its answer, which is
// an update or the next event to run.
const run = useCallback(async function run(next: BookingNext) {
	let outcome: Promise<BookingOutcome>;
	if (next.next === "submit") {
		const snapshot = shown.current;
		const started = submitStarted(snapshot);
		setState(started.state);
		if (!started.send) return;
		outcome = submitEvent(snapshot, new Date());
	} else if (next.next === "loadSlots") {
		setState((s) => loadSlotsStarted(s, next.professional));
		outcome = loadSlots(next.professional, next.after);
	} else {
		setState((s) => loadProfessionalsStarted(s, next.message));
		outcome = loadProfessionals();
	}
	const call = ++latest.current;
	const answer = await outcome;
	if (call !== latest.current) return;
	if ("update" in answer) setState(answer.update);
	else await run(answer);
}, []);
```

The hook sets the in-flight state, reads `new Date()` and passes it to `submitEvent`, drops an answer that is not the latest, and publishes the update or runs the next event.
`shown` holds the state last rendered, which the submit branch reads as `snapshot`; `submitStarted` and `submitEvent` both receive that snapshot.
`latest` is a count of requests: each call takes the next number, and an answer whose number is no longer the latest is dropped; `back` also advances `latest`, so an answer that arrives after a tap on "Back" is dropped as well.

**3. The client repository.** This is `postAppointment`, from [`src/features/appointments/api.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/api.ts):

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

**4. The server orchestrator fetches.** The request arrives at [`src/features/appointments/route.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/route.server.ts), whose `slotsOf` reads what a booking is checked against:

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
Each lives in the slice of the thing it reads, and `slotsOf` imports it from there, as the rule of [chapter 14](14-errors-and-slices.md#vertical-slices) says.
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
The route reads the body itself, because the request is the event it receives; a body that cannot be read becomes `BadRequest`, as [chapter 14](14-errors-and-slices.md#exceptions-as-values-in-the-clinic) says.
`drawBookingCode` draws the code at random in the route, because randomness, like the clock, is the orchestrator's to supply, so no use case stops being pure; the clinic's docs/01 says it of the clock: "*Use cases take the current time as a parameter. No use case reads the clock.*"

**6. The use case decides.** This is `book`, from [`src/features/appointments/rules.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/rules.ts):

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

The way back needs no excerpt: the route answers 201, `postAppointment` returns the booking as a value, `submit` returns the update with the step `booked`, the hook publishes it, and the view renders it in its `case "booked"`, with the booking code.

The flow never goes back the wrong way: the view never sets the state, and a use case never calls a repository.
So "what happens when this event arrives?" has one answer, and chapter 16 turns it into a test.

## What the clinic injects

ADR-0016, as amended, gives the rule: a piece receives a dependency only where its test passes a second implementation.[^book-adr-0016]
The clinic follows it on both sides.

The server's orchestrator receives the database, the driver its repositories use, and hands it to each repository function: the route is `appointmentsRoute(db)`, and `slotsOf` and the handler above hand `db` to every repository call, and each repository function receives `db` too, because its own test passes an in-memory database straight in, as [chapter 16](16-testing-and-agents.md#one-rule-five-tests) shows.
The route's test passes `memoryDatabase`, the in-memory SQLite of chapter 14, in place of the file, and the clinic's docs/01 says why the route takes the driver:

> "*Server routes that need the database are functions of it (`clinicRoute(db)`), so Vitest drives them through Hono's `app.request` against an in-memory SQLite (`testDatabase.server.ts`).*"

Vitest is the clinic's test runner, `app.request` sends a request to a route without a network, and `testDatabase.server.ts` holds `memoryDatabase`.

That database is opened before the first request arrives, by the server's start code: `openMigratedDatabase`, in [`src/server/start.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/server/start.server.ts), calls `openDatabase` and `migrate`, and `main.server.ts` hands the database it returns to every route that needs it.
Neither is a piece: no event reaches them, and they run once, at start, to make the driver ready.
They catch where they do I/O, as a repository does, and return a `Result`; `openMigratedDatabase` turns a failure into a message and exit code 1, because a server with no database has nothing to serve.
So the table's "only" holds where events are served: of the four pieces, the repository alone turns an infra exception into a `Result`.

The client's orchestrator receives its repositories, named in `bookingEvents.ts`:

```ts
export type BookingRepositories = {
	fetchProfessionals: typeof fetchProfessionals;
	fetchSlots: typeof fetchSlots;
	postAppointment: typeof postAppointment;
	remember: typeof remember;
};

export const bookingRepositories: BookingRepositories = {
	fetchProfessionals,
	fetchSlots,
	postAppointment,
	remember,
};
```

`submit`, in step 2, takes `repositories = bookingRepositories`, the real ones by default, so the hook passes none.
The event tests pass, in their place, repositories that answer what the test sets.
The clinic's docs/01 says it in the section "How the code is organized":

> "*Its event functions receive their repositories as a parameter, the real ones by default (`<name>Repositories`), and the clock as `now`: no function there reads it.*"

The in-memory SQLite is a fake database and those are fake repositories: a fake is a second implementation that a test passes in place of the real one.
A use case receives no repository (ADR-0016) and a view receives nothing: each has one implementation, so a parameter there would exist for ceremony, which KISS rules out.
`now`, which the route or the hook reads, is passed on as data, a value, not a dependency.
Chapter 16 shows the tests and their fakes.

## When the pieces pay their way

A piece can exist only when it has a job.
A use case exists when there is a rule: the `health` slice of [chapter 14](14-errors-and-slices.md#vertical-slices) has none, so it has no `rules.ts`.
A repository exists when there is I/O, an orchestrator when an event leads to a new state, and a view when there is a screen.

The clinic's [ADR-0002](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/docs/adr/ADR-0002-focus-whole.md), the decision to take FOCUS whole, names the cost in its Consequences: "*A slice has more files than a component that fetches on its own; a file appears only when it pays its way.*"
Its Context names what the clinic buys with it: a product that values "*every rule has a test*", and a rule in a pure function is the cheapest place for one.

A job is needed, and it is not enough: the health slice's client orchestrator has one and still does not pay its way.
Its job is real: `check`, in [`healthEvents.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/health/healthEvents.ts), turns the server's answer into `ok` or `unreachable`.
Its cost, counted with `wc -l` at each tag: at `book-v1/closing-a-milestone` it was one file, `useHealth.ts`, of 20 lines; at `book-v1/four-pieces` it is three, `useHealth.ts` (21), `healthEvents.ts` (16) and `healthEvents.test.ts` (17), 54 lines.
It also brings an update function that ignores the current state, and a `repositories` parameter that only the test uses.
Its gain is already given: the two Vitest cases of `healthEvents.test.ts`, "gives ok" and "gives unreachable", assert what [`HealthView.e2e.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/health/HealthView.e2e.ts) asserts, whose four Playwright tests show "Server: ok" once and "Server: unreachable" twice, on a 500 and on no answer.
The same piece pays in `bookingEvents.ts`, step 2 of [One event, one new state](#one-event-one-new-state): its test "keeps a name typed in flight through a taken slot" proves what no Playwright test at the tag proves.
Alone, `healthEvents.ts` costs more than it gives.
The clinic keeps it because [`orchestrator-tests`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/work/done/orchestrator-tests.md), the delivery that wrote it, chose "*Every event moves*", so every hook has one shape: that shape is what the clinic pays for, not the piece.

Where the code already has its own shape, the pieces can cost more than they give.
On the brownfield project of [chapter 8](08-analyze.md#focus-on-code-without-an-architecture), FOCUS whole meant a large refactor, and the answer was neither.
Between the two stands the kit's middle answer, the two principles alone of [chapter 14](14-errors-and-slices.md#two-principles-that-stand-alone): slices and exceptions as values, with no piece.
KISS, YAGNI and DRY decide, as [chapter 6](06-the-documents.md#the-two-choices) said: a piece is written when a delivery needs its job, and not before.

## Key points

* The view fires events and renders state, the orchestrator turns one event into one new state, a use case holds a rule as a pure function, and the repository is the only piece that fetches and saves.
* A piece is written when its job gives more than it costs, alone or through one shape a delivery chose for every hook, as the clinic keeps `healthEvents.ts`; the "Forbids" column keeps it to that job.
* In the clinic each side has its own orchestrator and repositories, and both import the same use cases: the server enforces a rule, and the client uses it only to decide what to show.
* An event flows one way: the view never sets the state, and a use case never calls a repository.
* A piece receives a dependency only where its test passes a second implementation, a fake: the orchestrator its repositories or the driver they use, and a server repository that driver; a use case and a view receive none, and `now` is passed as data.

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

[^book-adr-0016]: J.C. Ködel, "One Page at a Time", this book's ADR-0016, `docs/adr/ADR-0016-the-books-definition-of-focus.md`, dated 2026-09-28, amended 2026-09-29 and 2026-09-30, in the ADR folder on `main`. <https://github.com/JCKodel/focus-kit-book/tree/main/docs/adr>
[^bloc]: Bloc, "Bloc State Management Library", documentation, accessed 2026-09-29. <https://bloclibrary.dev/>
[^mediatr]: Jimmy Bogard, "MediatR: Simple, unambitious mediator implementation in .NET", accessed 2026-09-29. <https://github.com/jbogard/MediatR>
[^clean-architecture]: Robert C. Martin, "The Clean Architecture", 2012. <https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html>
[^clinic-orchestrator-tests-run]: This book's build of the guided project's orchestrator tests, 2026-09-29, with Claude Code 2.1.284 and the model `claude-opus-5-5`: the brief, every turn, and the `npm run verify` output on the clinic's commit `e6653b5` in `verify.txt`. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/clinic-orchestrator-tests-run/README.md>
