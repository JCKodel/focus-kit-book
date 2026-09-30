# Exceptions as values and vertical slices

After this chapter you can organize code by feature, in vertical slices, and return every exception as a value.
You can tell an exception from a refusal and from an error, and you know that both principles work without the four pieces of chapter 15.

## Two principles that stand alone

Vertical slices and exceptions as values need none of the four pieces, the view, the orchestrator, the use case and the repository.
Any structure your stack favors can put each feature in a folder and return exceptions as values: that is the kit's second answer to the architecture, among [the two choices](06-the-documents.md#the-two-choices) of chapter 6, and chapter 15 adds the pieces.
The clinic took FOCUS whole in chapter 7, so its code shows both principles.
Every excerpt below comes from the guided project at its chapter tag [`book-v1/closing-a-milestone`](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone), the annotated tag that marks the code chapter 12 left, and it is quoted as it ran.

## Vertical slices

A vertical slice is one folder that holds everything a feature needs: its screens, its calls to the server, its routes, its rules, its SQL and its tests.[^vertical-slice]
There is no folder per technology or layer, no `controllers/` and no `models/`.
A sub-feature is a subfolder, such as `authentication/change-password/`; the clinic has none yet.

This is the output of `git ls-tree -r --name-only book-v1/closing-a-milestone src/features/appointments`, the [appointments slice](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone/src/features/appointments), 22 files:

```text
src/features/appointments/BookingView.e2e.ts
src/features/appointments/BookingView.tsx
src/features/appointments/CancelView.e2e.ts
src/features/appointments/CancelView.tsx
src/features/appointments/RememberedView.tsx
src/features/appointments/api.ts
src/features/appointments/clinicTime.test.ts
src/features/appointments/clinicTime.ts
src/features/appointments/e2e.server.ts
src/features/appointments/remembered.test.ts
src/features/appointments/remembered.ts
src/features/appointments/repository.server.test.ts
src/features/appointments/repository.server.ts
src/features/appointments/route.server.test.ts
src/features/appointments/route.server.ts
src/features/appointments/rules.test.ts
src/features/appointments/rules.ts
src/features/appointments/strings.ts
src/features/appointments/styles.ts
src/features/appointments/useBooking.ts
src/features/appointments/useCancel.ts
src/features/appointments/useRemembered.ts
```

The three `View.tsx` files are the screens: booking, cancelling with a code, and the appointments the phone remembers.
The three `use*.ts` hooks hold the state each screen shows, and `strings.ts` and `styles.ts` hold its words and its look.
`api.ts` is the client's side of each call to the server; `route.server.ts` is the server's side, the HTTP routes.
`rules.ts` holds the rules (the free slots, a booking, the cancellation deadline), `repository.server.ts` holds the SQL, `clinicTime.ts` reads dates in the clinic's time zone, and `remembered.ts` keeps a copy of each booking on the phone.
A name ending in `.server.ts` runs only on the server, and client code never imports one.
The `.test.ts` files are unit tests, the `.e2e.ts` files drive the screens in a browser, and `e2e.server.ts` holds their shared steps.

A feature is one thing the app keeps, named by a term of the project's docs/03 (the appointment, the professional, the weekly hours), and its slice holds every action on it.
Booking and cancelling both act on the appointment, so they share its rules (`rules.ts`), its SQL (`repository.server.ts`), its routes (`route.server.ts`), its calls (`api.ts`) and the list the phone remembers (`remembered.ts`): they are one slice.
Weekly hours and professionals are other things the clinic keeps, each with its own table and its own screen, so each has a slice of its own, `weeklyHours` and `professionals`.
A change to the appointment touches this folder, and removing the appointment removes this folder.
The slice also bounds what an agent reads for a delivery on booking, which chapter 16 takes up.

The [health slice](https://github.com/JCKodel/focus-kit-clinic/tree/book-v1/closing-a-milestone/src/features/health), the server check of the first milestone, is 6 files:

```text
src/features/health/HealthView.e2e.ts
src/features/health/HealthView.tsx
src/features/health/api.ts
src/features/health/route.server.ts
src/features/health/strings.ts
src/features/health/useHealth.ts
```

It has no `rules.ts`, because it has no rule, and no `repository.server.ts`, because it stores nothing: a file appears in a slice when it pays its way.

What code is about decides where code that two features use lives.
Code about one thing the app keeps stays in that thing's slice, and another slice imports what it needs from there, be it a repository function, a type, a client call or a view; two slices may import from each other.
`findClinic` and `findActiveProfessionals` are each imported by `appointments/route.server.ts` and by `weeklyHours/route.server.ts`, a second use, and they stay in `clinic/` and `professionals/`, because each reads the thing its slice keeps.
What two features share and belongs to no thing the app keeps leaves their slices for `src/lib/`: the shape of a value (`email.ts`, `id.ts`, `name.ts`) or plumbing (`request.ts`, `result.ts`).
`email.ts`, `id.ts`, `name.ts` and `request.ts` each say in a comment where their first and second uses are, such as "First use: health/api.ts (`skeleton`); second use: clinic/api.ts." in `request.ts`; `result.ts` is used by every feature.
That is the rule of the second occurrence from [chapter 13](13-the-governor.md#the-same-question-in-code), applied to folders: code that belongs to no one thing moves to `lib/` on its second use, and not before.

## Exception, refusal, error

Dart splits failures into two classes of `dart:core`.[^dart-core]
An `Exception` is intended to be caught, an expected failure such as a lost connection; an `Error` is a program failure the programmer should have avoided, a bug.[^dart-core]

This book adds a third kind: the refusal, a rule's answer when it says no, such as a phone number with too few digits.
No I/O failed, and no code is wrong; the rule did its job.

So a failure is one of three:

* **Exception:** an expected failure at I/O (the database, the network, the phone's storage), caught where the I/O happens and returned as a value.
* **Refusal:** a rule saying no, checked in code or by a database constraint such as a unique index, and returned as a value; even when the database answers, nothing failed.
* **Error:** a bug, thrown and never caught, so it reaches your screen while you develop and your analytics once the app runs.

The field calls the principle "errors as values", after Go[^go-errors] and Rust,[^rust-result] and chapter 6 said why this book says exception.[^book-adr-0016]
The kit and the clinic still use the field's word, `error`, in the `Result`'s field and in their documents, for what this book calls an exception or a refusal.
The clinic's own docs/03 already calls each of its rule outcomes a refusal, such as `SlotTaken`, "the refusal when a booking asks for a time that is not free".

## Exceptions as values in the clinic

A `Result` holds either the value or what stopped it.
This is [`src/lib/result.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/lib/result.ts), whole:

```ts
export type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };

export function ok<T>(value: T): { ok: true; value: T } {
	return { ok: true, value };
}

export function err<E>(error: E): { ok: false; error: E } {
	return { ok: false, error };
}
```

The caller reads `ok` before it can reach `value` or `error`, and TypeScript narrows the type on that check.

A repository, the code that fetches and saves, runs every SQL statement inside `query`, from [`src/server/database.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/server/database.server.ts):

```ts
export type DatabaseFailed = { code: "DatabaseFailed"; message: string };

// Where a repository's SQLite exception becomes a Result. First use: the
// clinic repository; second use: the session queries.
export function query<T>(run: () => T): Result<T, DatabaseFailed> {
	try {
		return ok(run());
	} catch (error) {
		const message = error instanceof Error ? error.message : String(error);
		return err({ code: "DatabaseFailed", message });
	}
}
```

This is the one `try`/`catch` a repository's SQL runs inside, and it turns the database's exception into a value.

`query` catches every thrown value, not only the database's, so a bug inside `run`, such as a `TypeError` or a malformed statement, becomes `DatabaseFailed` too.
A narrower catch would not tell them apart: SQLite reports a malformed statement with the same code as a missing table or a locked file, `ERR_SQLITE_ERROR`.[^node-sqlite-error]
The definition of an error says what the code aims for; a catch at I/O is where a bug can be caught by accident.
The routes answer `DatabaseFailed` with its code alone and log nothing, so a bug caught there reaches neither your screen nor your analytics.

An exception can also become a refusal.
In [`src/features/appointments/repository.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/repository.server.ts), a booking's insert can fail in two ways:

```ts
export type InsertError = { code: "SlotTaken" } | DatabaseFailed;
```

```ts
// The index appointment_booked_slot is the last guard against a double
// booking (docs/02): its failure is SlotTaken. Any other, a repeated booking
// code included, is DatabaseFailed.
export function insertAppointment(
	db: DatabaseSync,
	appointment: NewAppointment,
): Result<void, InsertError> {
	const inserted = query(() => {
		db.prepare(
			"INSERT INTO appointment (professional_id, starts_at, client_name, client_phone, booking_code) VALUES (?, ?, ?, ?, ?)",
		).run(
			appointment.professionalId,
			appointment.startsAt,
			appointment.clientName,
			appointment.clientPhone,
			appointment.bookingCode,
		);
	});
	if (
		!inserted.ok &&
		inserted.error.message.includes(
			"UNIQUE constraint failed: appointment.professional_id, appointment.starts_at",
		)
	) {
		return err({ code: "SlotTaken" });
	}
	return inserted;
}
```

When two clients book the same time at once, the unique index refuses the second insert, and the repository returns that as the refusal `SlotTaken`; any other failure stays the exception `DatabaseFailed`.
It is the same rule checked twice: the use case `book` refuses a time that is not free first, as [chapter 15](15-four-pieces.md#one-event-one-new-state) shows, and the index is the last guard when two clients book at once.

A refusal from a rule involves no I/O at all.
This is `checkClientPhone`, from [`src/features/appointments/rules.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/rules.ts):

```ts
const phoneCharacters = /^[\d +\-.()]*$/;

// The digits to store: only digits, spaces, +, -, . and brackets typed, and
// 6 to 15 digits.
export function checkClientPhone(
	raw: string,
): Result<string, "InvalidPhoneNumber"> {
	if (!phoneCharacters.test(raw)) return err("InvalidPhoneNumber");
	const digits = raw.replace(/\D/g, "");
	if (digits.length < 6 || digits.length > 15) {
		return err("InvalidPhoneNumber");
	}
	return ok(digits);
}
```

It is a pure function, text in and a value out, so it has nothing to catch.
The clinic calls such a function a use case, a piece chapter 15 teaches.

Every case must be handled, and the compiler can check that.
This is `refusalStatus`, from [`src/features/appointments/route.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/features/appointments/route.server.ts), the HTTP status of each refusal of a booking:

```ts
// The three time refusals share 409: the client shows them alike.
const refusalStatus: Record<BookingRefusal, 400 | 409> = {
	InvalidClientName: 400,
	InvalidPhoneNumber: 400,
	OutsideBookingWindow: 409,
	OutsideWorkingHours: 409,
	SlotTaken: 409,
};
```

A `Record` over `BookingRefusal` must name every member of that type, so a refusal added to the rules without a status fails to compile.

The clinic catches only where I/O happens: `openDatabase` and `query` in `database.server.ts` (`transaction` runs inside `query`), the migration runner in `migrate.server.ts`, `request` in `src/lib/request.ts` for the network on the client, and `remembered.ts` for the phone's storage.
Each route that reads a request body catches too, since the body arrives over the network: a body that cannot be read becomes the answer `BadRequest` on the spot.

The app itself never throws.
Two helpers that only tests run do: `box` in `e2e.server.ts`, when an element is not on screen, and `memoryDatabase`, in [`src/server/testDatabase.server.ts`](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/closing-a-milestone/src/server/testDatabase.server.ts):

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

A migration that fails in a test is a bug, an error, so it is thrown and the test stops there.

## One failure, end to end

The clinic's docs/01, in its section "How errors travel", gives the path a failure takes.
`SlotTaken`, when the index refuses a booking, follows it in five steps, with no `throw` on the way:

1. `insertAppointment` in `repository.server.ts` returns `SlotTaken`.
2. The booking route in `route.server.ts` answers 409 with the body `{ "error": { "code": "SlotTaken" } }`.
3. `postAppointment` in `api.ts` names 409 as `SlotTaken`, and `request` in `src/lib/request.ts` returns it as that refusal.
4. `useBooking.ts`, the hook, reloads the free times and publishes a state whose message is `SlotTaken`.
5. `BookingView.tsx` shows the message `strings.ts` gives that code: "This time is no longer free. Pick another."

`strings.ts` maps every booking failure to a message with a `Record`, as the route does to statuses, so a code with no message also fails to compile.

## Key points

* A feature is one thing the app keeps, with every action on it, and its vertical slice is one folder, with no folder per layer; a change to the feature touches that folder, and removing the feature removes it.
* A file enters a slice when it pays its way; code about one thing the app keeps stays in its slice, which other slices import, and code that belongs to no one thing enters `lib/` on its second use.
* An exception is I/O that failed, a refusal is a rule saying no, in code or in a database constraint, and neither is thrown.
* An error is a bug: never caught, it reaches your screen and your analytics.
* A `Result` handled with a `Record` over its cases fails to compile when a case is forgotten.

## Exercises

These exercises use the clinic, by conversation with the agent, never by hand.

### Exercise 14.1

Ask the agent to list every `try`, `catch` and `throw` in your clinic outside tests, and for each to say what I/O it guards and which value it returns.
Any that guards no I/O is a candidate for your queue, not a fix now.

### Exercise 14.2

Ask the agent to follow `CancellationTooLate` from the rule to the screen, naming each file.
Then say which files would have to change if the rule threw it instead.

### Exercise 14.3

Milestone 2 brings `absences`.
Ask the agent where its files would go, a folder of its own or a subfolder of `weeklyHours`, and which existing files it would touch.
Decide, and say why; nothing is built.

[^vertical-slice]: Jimmy Bogard, "Vertical Slice Architecture", 2018. <https://www.jimmybogard.com/vertical-slice-architecture/>
[^dart-core]: Dart, "Exception class" and "Error class", `dart:core` API reference, accessed 2026-09-29: an `Exception` "*is intended to be caught*"; an `Error` is "*a program failure that the programmer should have avoided*". <https://api.dart.dev/stable/dart-core/Exception-class.html> and <https://api.dart.dev/stable/dart-core/Error-class.html>
[^go-errors]: Rob Pike, "Errors are values", The Go Blog, 2015. <https://go.dev/blog/errors-are-values>
[^rust-result]: The Rust Programming Language, "Recoverable Errors with Result", chapter 9.2, accessed 2026-09-29. <https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html>
[^book-adr-0016]: J.C. Ködel, "One Page at a Time", this book's ADR-0016, `docs/adr/ADR-0016-the-books-definition-of-focus.md`, dated 2026-09-28, in the ADR folder on `main`. <https://github.com/JCKodel/focus-kit-book/tree/main/docs/adr>
[^node-sqlite-error]: Node.js, "Errors", API reference, `ERR_SQLITE_ERROR`, accessed 2026-09-30: "*An error was returned from SQLite.*" <https://nodejs.org/api/errors.html#err_sqlite_error>
