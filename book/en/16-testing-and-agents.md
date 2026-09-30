# Testing, and FOCUS with agents

After this chapter you can say which test guards each FOCUS piece and what it swaps, and follow one rule of the clinic through a test at every level, the client orchestrator's test with its fakes included.
You can also say, with the clinic's own record, how a slice and its tests keep an agent's reading small and tell it when it is done.

## A test for each piece

Every excerpt below comes from the guided project at its chapter tag [`book-v1/four-pieces`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/four-pieces), as in chapter 15, and is quoted as it ran; code nested inside a function is shown without its outer indentation.

The clinic's [`docs/04-Conventions.md`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/docs/04-Conventions.md), in its section "Tests", gives its levels in a table:

| Level | Tool | What |
|---|---|---|
| Use case | Vitest | Every rule, with the clock passed as a parameter. No database, no network. |
| Repository | Vitest | Queries against an in memory SQLite with the real migrations. |
| Orchestrator | Vitest | each event with fake repositories and `now`; no DOM, no module mock |
| Screen | Playwright | Each scenario of a page's Behaviour that has a screen, plus the screenshots of docs/05. |

The same section ends with the clinic's rule: "*Every rule has a test. A rule without a test is not done.*"

Vitest runs a test in Node, with no browser.[^vitest]
Playwright drives the app in a real browser, as a user would, by clicking and typing.[^playwright]

A test Vitest runs is a unit test: it runs one piece of code, such as a use case called with its data or a repository against an in-memory database.
A test Playwright runs is an end-to-end test: it drives the running app through the view, the orchestrators, the server and the database.
They are the `.test.ts` and `.e2e.ts` files of the appointments slice in [chapter 14](14-errors-and-slices.md#vertical-slices), each beside the file it tests.

## One rule, five tests

The rule: a client cancels an appointment up to 24 hours before it starts.
It is the clinic's use case `cancel`, which [exercise 14.2](14-errors-and-slices.md#exercises) followed from the rule to the screen; here it is followed through its tests.

**The use case.** This is `describe("cancel", ...)`, from [`src/features/appointments/rules.test.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/rules.test.ts):

```ts
describe("cancel", () => {
	// The deadline of at("08:00") is Monday 28 September, 08:00 UTC.
	const deadline = Date.parse("2026-09-28T08:00:00.000Z");

	it("succeeds one millisecond before and exactly at the deadline", () => {
		for (const now of [deadline - 1, deadline]) {
			expect(cancel(at("08:00"), new Date(now))).toEqual({
				ok: true,
				value: undefined,
			});
		}
	});

	it("is too late one millisecond after the deadline", () => {
		expect(cancel(at("08:00"), new Date(deadline + 1))).toEqual({
			ok: false,
			error: "CancellationTooLate",
		});
	});

	it("is too late for a start already past", () => {
		expect(cancel(at("08:00"), new Date(at("09:00")))).toEqual({
			ok: false,
			error: "CancellationTooLate",
		});
	});
});
```

`at` is a helper of the same file that gives a time on Tuesday 29 September 2026, in UTC, so `at("08:00")` starts at 08:00 and its deadline is 24 hours earlier.
`cancel` receives the start and `now`, and returns a `Result`: `now` is data, so the test tries one millisecond before the deadline, the deadline itself and one millisecond after, with no database and no mock.

**The fake database.** This is `memoryDatabase`, from [`src/server/testDatabase.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/server/testDatabase.server.ts), which [chapter 14](14-errors-and-slices.md#exceptions-as-values-in-the-clinic) showed among the code that catches; the next two tests use it:

```ts
// For Vitest: an in-memory SQLite with the real migrations applied.
export function memoryDatabase(): DatabaseSync {
	const db = new DatabaseSync(":memory:");
	const folder = fileURLToPath(new URL("./migrations/", import.meta.url));
	const migrated = migrate(db, folder);
	if (!migrated.ok) {
		throw new Error(
			`Migration ${migrated.error.file}: ${migrated.error.message}`,
		);
	}
	return db;
}
```

It is the one swap the server needs: the same SQLite engine, in memory, with the same migration files the app runs, so every test starts from an empty database of the real schema.

**The repository.** This is `it("cancels once, keeping the row, and frees the slot", ...)`, from [`src/features/appointments/repository.server.test.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/repository.server.test.ts), where each test gets a fresh `memoryDatabase` with two professionals:

```ts
it("cancels once, keeping the row, and frees the slot", () => {
	insertAppointment(db, appointment);

	expect(cancelAppointment(db, 1)).toEqual({ ok: true, value: true });
	expect(cancelAppointment(db, 1)).toEqual({ ok: true, value: false });

	expect(rows()).toEqual([
		expect.objectContaining({ booking_code: "K7MXQ2", status: "cancelled" }),
	]);
	expect(findBookedStarts(db, 1, "2026-09-29T00:00:00.000Z")).toEqual({
		ok: true,
		value: [],
	});
	expect(
		insertAppointment(db, { ...appointment, bookingCode: "ZZZZZZ" }).ok,
	).toBe(true);
});
```

`appointment` is a booking of the same file and `rows` reads every row of the table.
The test runs the real SQL: the second cancellation changes nothing, the row stays with the status `cancelled`, and the slot takes a new booking.

**The route.** The server orchestrator is tested in [`src/features/appointments/route.server.test.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/route.server.test.ts), which sets up every test this way:

```ts
// Monday 28 September 2026, 01:00 in Lisbon.
const now = new Date("2026-09-28T00:00:00.000Z");

let db: DatabaseSync;
let app: Hono;

function setUpClinic() {
	saveClinicAndOwner(db, {
		name: "Clinica Sol",
		timeZone: "Europe/Lisbon",
		slotMinutes: 30,
		email: "owner@example.com",
		passwordHash: "unused",
	});
}

beforeEach(() => {
	vi.useFakeTimers({ toFake: ["Date"] });
	vi.setSystemTime(now);
	db = memoryDatabase();
	app = new Hono().route("/api", appointmentsRoute(db));
	setUpClinic();
	// 1 works on Tuesdays 09:00 to 11:00; 2 has no hours; 3 is removed.
	insertProfessional(db, "Ana Lima");
	insertProfessional(db, "Rui Lopes");
	insertProfessional(db, "Eva Reis");
	replaceWorkingPeriods(db, 1, [{ weekday: 2, start: "09:00", end: "11:00" }]);
	replaceWorkingPeriods(db, 3, [{ weekday: 2, start: "09:00", end: "11:00" }]);
	setRemovedAt(db, 3, "2026-09-27T10:00:00.000Z");
});

afterEach(() => {
	db.close();
	vi.useRealTimers();
});
```

`vi.useFakeTimers({ toFake: ["Date"] })` replaces only `Date`, so `new Date()` answers whatever `vi.setSystemTime` set, and `afterEach` gives the real clock back.
The route is chapter 15's `appointmentsRoute(db)`, given `memoryDatabase` and mounted in a `Hono` app, and `app.request` sends it a request with no network, as [chapter 15](15-four-pieces.md#what-the-clinic-injects) said.

This is the test of the rule, `it("cancels at the deadline, and answers 409 one millisecond later, keeping it booked", ...)`, inside the file's `describe("POST /api/appointments/cancel", ...)`:

```ts
it("cancels at the deadline, and answers 409 one millisecond later, keeping it booked", async () => {
	const bookingCode = await booked();
	const body = { clientPhone: valid.clientPhone, bookingCode };
	// 24 hours before tuesday[0].
	const deadline = Date.parse("2026-09-28T08:00:00.000Z");

	vi.setSystemTime(deadline + 1);
	await expectError(await postCancel(body), 409, "CancellationTooLate");
	expect(statuses()).toEqual(["booked"]);

	vi.setSystemTime(deadline);
	expect((await postCancel(body)).status).toBe(200);
});
```

`booked` books `tuesday[0]`, 08:00 UTC on Tuesday, through the booking route and answers its code; `valid` is that booking's body, `postCancel` sends a cancellation, `expectError` checks the status and the error code, and `statuses` lists the status of every row.
The clock goes one millisecond past the deadline first: the answer is 409 with `CancellationTooLate`, and the row is still `booked`; then, at the deadline itself, the same request answers 200.

This is [chapter 15](15-four-pieces.md#one-event-one-new-state)'s "one event, one new state" as one test: one request is the event, and the answer and the rows are the new state.
The use case's test passes `now` as data, and the route's test fakes the clock, because the route reads `new Date()` and hands it to `cancel`, as the clinic's docs/01 bullet [chapter 15](15-four-pieces.md#one-event-one-new-state) quoted says: "*Use cases take the current time as a parameter. No use case reads the clock.*"
In the appointments slice, the route and the hooks are the only code that reads `new Date()`, and each hands it on, so every other test passes `now` as data and fakes nothing.

**The client's event.** The client orchestrator's event is `submit`, in `cancelEvents.ts`: it receives what was typed, `now`, and its repositories, `postCancellation` from `api.ts` and `forget` from `remembered.ts`, named in the type `CancelRepositories`, as `BookingRepositories` is in [chapter 15](15-four-pieces.md#what-the-clinic-injects).
Its test, [`src/features/appointments/cancelEvents.test.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/cancelEvents.test.ts), builds the fake repositories with two functions:

```ts
function unexpected(): never {
	throw new Error("not called in this test");
}

function fake(repositories: Partial<CancelRepositories>): CancelRepositories {
	return { postCancellation: unexpected, forget: unexpected, ...repositories };
}
```

`fake` fills in only the repositories a test sets, and any other call throws, so a test fails if the event calls a repository it did not expect.
These are two of its tests under `describe("submitting", ...)`:

```ts
it.each([
	"AppointmentNotFound",
	"CancellationTooLate",
	"ServerUnreachable",
] as const)("keeps what was typed and shows %s", async (code) => {
	const started = submitStarted(typed);
	const update = await submit(
		typed.phone,
		typed.code,
		now,
		fake({ postCancellation: async () => err({ code }) }),
	);

	expect(update(started)).toEqual({
		...typed,
		busy: false,
		message: code,
	});
});

it("forgets the normalized code and shows the cancellation with the fields emptied", async () => {
	const postCancellation = vi.fn(async () => ok(cancelled));
	const forget = vi.fn(() => ok(undefined));

	const update = await submit(
		typed.phone,
		typed.code,
		now,
		fake({ postCancellation, forget }),
	);

	expect(postCancellation).toHaveBeenCalledWith({
		clientPhone: "912 345 678",
		bookingCode: " k7p2qx ",
	});
	expect(forget).toHaveBeenCalledWith("K7P2QX", now);
	expect(update(submitStarted(typed))).toEqual({
		...initialCancelState,
		open: true,
		cancelled,
	});
});
```

`typed` is the form with a phone and the code `" k7p2qx "` typed, `now` a constant date and `cancelled` the server's answer, all constants of the same file.
In the first test the fake `postCancellation` answers `CancellationTooLate`, as the server would, and the test checks the new state, what was typed kept and the refusal named, with no screen.
In the second, `vi.fn` records each call, so the test asserts what was sent, that `forget` got the normalized code `K7P2QX` and `now`, and the new state.
`now` is a constant because `submit` receives it, so nothing is faked but the repositories.

**The screen.** This is `test("an appointment under 24 hours away is refused by the typed form, and shows no Cancel when remembered", ...)`, from [`src/features/appointments/CancelView.e2e.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/CancelView.e2e.ts):

```ts
test("an appointment under 24 hours away is refused by the typed form, and shows no Cancel when remembered", async ({
	page,
}) => {
	const name = tagged("Ana");
	const id = await professionalWith(page, name, allWeek("08:00", "20:00"));
	const [[earliest]] = await slotsByDay(page, id);
	const phone = randomPhone();
	const appointment = await bookThroughApi(page, id, name, earliest, phone);
	await page.goto("/");

	const form = await typeAndSend(page, phone, appointment.bookingCode);

	await expect(form.getByText(tooLate)).toBeVisible();
	await expect(form.getByLabel("Booking code")).toHaveValue(
		appointment.bookingCode,
	);

	await plant(page, [appointment]);
	const item = itemOf(page, appointment);
	await expect(item).toBeVisible();
	await expect(
		item.getByText("Can no longer be cancelled in the app."),
	).toBeVisible();
	await expect(button(item, "Cancel")).toHaveCount(0);
});
```

The helpers are the file's and the slice's: `professionalWith` adds a professional who works `allWeek` from 08:00 to 20:00, `slotsByDay` gives the free times, `bookThroughApi` books the earliest, which is under 24 hours away, `typeAndSend` fills and sends the cancel form, `plant` puts the appointment in the phone's storage and reloads, and `itemOf` finds its line under "Your appointments"; `tooLate` is the 24 hours message.
It runs on the real clock, and in a browser it drives the view and the hook: the typed form shows why it refused and keeps the code, and the remembered line shows no Cancel button.

The use case proves the boundary to the millisecond, and the repository that a cancelled row is kept and its slot freed.
The route proves that the server refuses after the deadline and changes nothing, and the event function that the client keeps what was typed and names the refusal.
The screen proves that the client sees why.

## The client's I/O

`remembered.ts`, the phone's storage, reads and writes `localStorage`, which Node does not have.
This is the setup of [`src/features/appointments/remembered.test.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/features/appointments/remembered.test.ts):

```ts
let stored: Map<string, string>;

beforeEach(() => {
	stored = new Map();
	vi.stubGlobal("localStorage", {
		getItem: (key: string) => stored.get(key) ?? null,
		setItem: (key: string, value: string) => stored.set(key, value),
	});
});

afterEach(() => {
	vi.unstubAllGlobals();
});
```

`vi.stubGlobal` puts a `localStorage` backed by a `Map` in place of the browser's, and `vi.unstubAllGlobals` removes it after each test.

The network goes through one function, `request` in `src/lib/request.ts`, from chapter 14, which every `api.ts` calls.
Its test, [`src/lib/request.test.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/four-pieces/src/lib/request.test.ts), replaces `fetch` the same way, and these are the tests under its `describe("request", ...)`:

* ``gives what `read` accepts from a 2xx body``
* `gives the refusal named for the status`
* `gives ServerUnreachable for a status not named`
* ``gives ServerUnreachable for a body `read` does not accept``
* `gives ServerUnreachable when the network fails`
* `reads no body from a 204`

Each `api.ts` only names which status is which refusal, over `request`, so it has no test of its own, and the end-to-end tests drive it, as they drive the hooks.
On the client, as on the server, a test swaps only the I/O and the clock: the storage, the network and `now`, never a use case.

## How many

The clinic's `npm run verify` at `e6653b5`, the commit the tag `book-v1/four-pieces` points to, ran 33 Vitest files with 323 tests in 1.21 seconds, and 144 Playwright runs in 20.1 seconds.[^clinic-orchestrator-tests-run]
The 144 runs are 91 distinct tests: every test runs at 390×844, and the 53 tests of the three owner screens' files run again at 1280×800, as the clinic's docs/04 says in its section "Tests".
The 91 and the 53 are the lines that start with `test(` in the `.e2e.ts` files at the tag, all seven for the 91 and the owner screens' three for the 53.

## What the slice gives an agent

Chapter 14 said a slice bounds what an agent reads.
The record of the clinic's milestone 1 lets you count it, for the two deliveries of the appointments slice.[^clinic-milestone-1-run]
I counted the distinct paths under `src/` that existed at the delivery's parent commit and whose contents the `/apply` turn read, by a `Read` call or a shell call that prints a file (`cat`, `sed -n`, `head`, `tail`); a `grep` or an `ls` is not a read, a call the record lists as denied read nothing, and the total is what `git ls-tree -r --name-only <parent> src` lists.
These turns ran before the event functions existed, so they count the code of milestone 1, which is what the agent had.

`cancel-appointment` added a feature inside a slice that existed.
Its `/apply` turn read 20 of the 95 files of `src/` at its parent commit, `442f88a`.
15 of the 20 were in `src/features/appointments/`, which had 17, and the other five were code outside the slice that it calls: `src/app/main.tsx`, `src/lib/request.ts`, `src/lib/result.ts`, `src/server/database.server.ts` and the professionals slice's `src/features/professionals/repository.server.ts`.

`book-appointment` started the slice.
Its `/apply` turn read 33 of the 77 files of `src/` at its parent commit, `afc833a`: with no slice of its own yet, it read the other slices, 9 of the 11 files of `src/features/weeklyHours/` among them, and said so:

> "I've studied the `weeklyHours` slice to use as the pattern."

A new slice copies the shape of a sibling slice, and a delivery inside a slice reads that slice and the code outside it that it calls.

Both turns ran the slice's tests alone before the whole verify.
`cancel-appointment` ran `npx vitest run src/features/appointments` and `npx playwright test --project=phone src/features/appointments`, then `npm run verify`.
`book-appointment` ran `npx vitest run src/features/appointments` and `npx playwright test src/features/appointments src/features/clinic`, then `npm run verify`.
The slice's own tests tell the agent in seconds whether it is done with the slice, and verify then tells it that nothing else broke.

Fewer files read is less context, and [chapter 2](02-how-agents-see.md#more-context-less-accuracy) showed that a model's accuracy falls as its context window fills, which is context rot.

Your part is the review.
A test's name is a sentence of the rule, such as "is too late one millisecond after the deadline", so reviewing an agent's staged tests starts by reading their names, as in [chapter 11's review](11-apply.md#review-before-you-commit): a rule with no sentence among them has no test.

## Key points

* Each piece has its test: a use case called with its data and `now`, a repository against an in-memory SQLite with the real migrations, a route through `app.request` with a fake clock, an event function with fake repositories, and the view and the hook in a browser with Playwright.
* A test swaps only I/O and the clock, because of the four pieces only the repositories do I/O, only the orchestrator receives them, and only the orchestrator reads the clock.
* A fake repository answers what the test sets, and any call the test did not expect throws, so the test asserts which repository was called, with what, and the new state.
* One rule followed through every level shows what each level proves that the others do not: the boundary, the row, the server's answer, the client's state, and what the client sees.
* A slice keeps an agent's reading small, 20 of 95 files for a delivery inside one, and its tests, run alone, tell the agent when the slice is done.

## Exercises

These exercises use the clinic, by conversation with the agent, never by hand.

### Exercise 16.1

Ask the agent which tests guard the rule that a client's name has at most 80 characters, at every level, and to run only those.
Compare what it ran with what `npm run verify` runs.

### Exercise 16.2

Take exercise 15.2's rule: a client may hold at most two future appointments.
Ask the agent which test files change, and what each new test asserts, at each level, the booking's event test and its fake included.
Nothing is built.

### Exercise 16.3

In a fresh session, ask the agent which files it would read to add a delivery in which the owner sees the day's appointments, and why.
Compare its list with the slices it names and with the counts of "What the slice gives an agent".
Nothing is built.

[^vitest]: Vitest, "Getting Started", the documentation's guide, accessed 2026-09-29. <https://vitest.dev/guide/>
[^playwright]: Playwright, "Installation", the documentation, accessed 2026-09-29. <https://playwright.dev/docs/intro>
[^clinic-orchestrator-tests-run]: This book's build of the guided project's orchestrator tests, 2026-09-29, with Claude Code 2.1.284 and the model `claude-opus-5-5`: every turn, and the `npm run verify` output on the clinic's commit `e6653b5` in `verify.txt`. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/clinic-orchestrator-tests-run>
[^clinic-milestone-1-run]: This book's build of the guided project's milestone 1, 2026-09-28, with Claude Code 2.1.284 and the model `claude-opus-5-5`: every turn of each delivery, and the denied calls in the README. <https://github.com/JCKodel/focus-kit-book/tree/main/work/done/clinic-milestone-1-run>
