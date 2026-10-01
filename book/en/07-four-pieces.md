# 7. FOCUS: the four pieces

After this chapter you can place any file of a feature in one of four pieces, view, orchestrator, use case or repository, and follow one event through them to one new state.
You can also say what each letter of FOCUS stands for, what it corrects in Clean Architecture, and when a piece is not worth writing.

## The problem

In most applications a business rule lives wherever someone needed it first: part in a screen that hides a button, part in the handler that saves the form, and a copy in a query.
Ask "what happens when a librarian lends this copy to this member?" and nobody can answer by reading one place.
You find out by running the app, clicking, and watching the database.
A person cannot test that answer without the whole app, and an agent asked to change the rule finds two of its three copies and changes those.

FOCUS is this book's name for one way to give that question a single answer: four pieces, each with one job, and one direction for everything that flows between them.

## The acronym, letter by letter

**F, Feature-oriented.** The code is organized in vertical slices: one folder holds everything a feature needs, and there is no folder per technology, no `controllers/` or `services/`.
The four pieces of a feature live in its folder, side by side.

**C, Clean.** The pieces are the layers of Robert C. Martin's Clean Architecture, whose dependency rule says code may point inward, toward the rules, and never outward, toward a screen or a database.[^clean-architecture]
FOCUS keeps that rule with one correction, and the correction is the orchestrator.
In Martin's drawing a use case talks to storage through an interface it receives, so a rule can still reach I/O, only through a door with a different name, and its test needs a double behind every door.
In FOCUS a use case receives no repository at all: it is a pure function, data in, a `Result` out, and it holds every kind of business rule: a decision, such as who may borrow; a validation, such as whether a card number is well formed; a format, such as how a due date reads to the user.
What makes that possible is the orchestrator, the glue between the view, the use cases and the repositories: it decides where the data comes from, which use cases validate and decide, who saves, and how the result is shaped for the view.
It receives its repositories as a parameter, so its test passes doubles in their place and knows which ones were called, with what, and what state came out; the whole flow of a feature is proven with no database and no screen ([chapter 8](08-testing-each-piece.md) shows the test).
Chapter 6 gives the rule behind that choice: a piece receives a dependency only where its test passes a second implementation.

**U, Unidirectional.** Everything flows one way: an event, the orchestrator, the use cases and repositories it calls, and a new state.
There is no binding, the mechanism some frameworks offer where a field on the screen and a value in memory update each other in both directions.
No state travels back: the view never changes the state it renders, and a use case never calls a repository.
So "what happens when event X arrives?" has one answer, and one test can check it.
That test is the test of a behaviour: "the user wants to sign in with Google" is one event, everything it sets off is one path through the orchestrator, and what comes out is one state, a confirmed sign-in or a failure, so the test reads "given this intention, this state", with nothing to inspect in between.
Model-View-Intent (MVI), a pattern of Android apps, draws the same one-way flow with the user's intent as the event.

**S, Scalable.** Every piece is isolated and has its own test, so a new feature adds its own folder and its own tests and changes no other, and the application holds at any size.

## The four pieces

| Piece | Does | Forbids |
|---|---|---|
| View | fires events, renders the state it receives | business rules, data access, formatting |
| Orchestrator | turns one event into one new state: validates and formats through use cases, fetches through repositories, applies the rules through use cases, asks repositories to save, publishes the state | deciding a rule, persisting |
| Use case | the only place for a business rule, be it a decision, a validation or a format; pure: data in, `Result` out | I/O, the framework, exceptions |
| Repository | fetches and saves; the only place an exception from data becomes a `Result` | business rules |

Read the "Forbids" column first: it keeps each piece to its job.
A view that decides who may borrow, or a repository that decides it, breaks the table whatever else it does right.

An event is what happened: a tap on "Lend", or a request arriving at a server.
A state is what the orchestrator publishes after it, whole: on a screen, what the view renders; on a server, the answer to the request.
A view is not only a screen.
The JSON an API answers is a view, and so is the text a command-line tool prints: the view is the output of the computation, input, processing, output, in whatever form leaves the program.
It is dumb on purpose: it does not even format a date; it renders the text the state carries, and the use case that formatted it has a test.

### Drivers and services

A repository does not talk to the disk or the network itself; it uses a driver, the library that speaks to the thing outside.
The usual drivers come from third parties: the client library of a database engine, the program that stores and queries the data, such as SQLite or PostgreSQL; an ORM over it, such as Prisma or Entity Framework; an HTTP client; a cloud vendor's SDK, such as Firebase's.
A project writes a driver only when the thing outside has no library: a client for a payment gateway's API, a reader of the bank's CSV statements, a wrapper around the phone's Bluetooth.
The driver knows the protocol and nothing of the product; the repository knows the product's tables and messages and nothing of the protocol, so a driver can be replaced without a rule noticing.

A service is a helper the four pieces do not name: technical code that is neither a rule nor I/O, such as hashing a password, compressing an image or rendering a PDF.
It is usually called by a repository, before it saves or after it reads, and tested as a function.

## One event, one new state

A librarian lends a copy to a member.
The tap on "Lend" is the event, and the screen that shows the loan, or the reason it was refused, is the new state.
These are the steps between them.

1. **The view fires the event.**
   The lending screen sends `LendRequested { copyId, memberId }` and does nothing else.
2. **The orchestrator receives it.**
   It checks that the event carries both ids; on a server the event is the request, so reading its body is part of receiving it.
3. **The repositories fetch.**
   The orchestrator asks `findMember` for the member and `findCopy` for the copy.
4. **The use case decides.**
   The orchestrator hands both to `lend`, the pure function that returns a `Loan` due 21 days later, or the refusal `HasOverdueBooks` or `MemberSuspended`.
5. **The repository saves.**
   The orchestrator asks `insertLoan` to save the loan; a unique index on the copy refuses a second open loan, and the repository turns that failure into the refusal `AlreadyLent`, as [chapter 5](05-rules-and-exceptions.md) showed.
6. **The orchestrator publishes the new state.**
   `Lent` with the loan, `Refused` with the refusal, or `Failed` with the exception, and the view renders it: the due date, "Return your overdue books first.", or "Could not reach the library's database. Try again."

The state and the repositories the orchestrator needs are types in its file, `lendEvents.ts`:

```ts
type LendRequested = { copyId: string; memberId: string };

type LendState =
	| { kind: "Lent"; loan: Loan }
	| { kind: "Refused"; refusal: LendRefusal | "NotFound" }
	| { kind: "Failed"; exception: DatabaseFailed };

type LoanRepositories = {
	findMember(id: string): Result<Member, "NotFound" | DatabaseFailed>;
	findCopy(id: string): Result<Copy, "NotFound" | DatabaseFailed>;
	insertLoan(loan: Loan): Result<Loan, "AlreadyLent" | DatabaseFailed>;
};
```

The orchestrator itself is steps 3 to 6, in order, once the event has been received and typed:

```ts
function stateOf(error: LendRefusal | "NotFound" | DatabaseFailed): LendState {
	if (typeof error === "string") return { kind: "Refused", refusal: error };
	return { kind: "Failed", exception: error };
}

export function lendRequested(
	event: LendRequested,
	today: string,
	repositories: LoanRepositories,
): LendState {
	const member = repositories.findMember(event.memberId);
	if (!member.ok) return stateOf(member.error);
	const copy = repositories.findCopy(event.copyId);
	if (!copy.ok) return stateOf(copy.error);
	const loan = lend(copy.value, member.value, today);
	if (!loan.ok) return stateOf(loan.error);
	const saved = repositories.insertLoan(loan.value);
	if (!saved.ok) return stateOf(saved.error);
	return { kind: "Lent", loan: saved.value };
}
```

Every line either asks a repository, asks the use case, or turns an answer into the state; none of them decides who may borrow.
The refusals are strings and the exception is an object with a `code`, so `stateOf` tells a `Refused` from a `Failed` with one check.
`today` comes in as a value: the code that receives the request reads the clock once and passes it on, so neither `lendRequested` nor `lend` reads it, and a test passes any date it likes.
`repositories` comes in as a parameter: the server passes the real ones, bound to its database, and a test passes fakes.
The flow never goes back: `lend` never sees a repository, and the view never sees anything but the state.

## The orchestrator elsewhere

The orchestrator has other names in other stacks, and the job is the same.
In Flutter it is a BLoC, a class that receives events and emits states;[^bloc] in .NET it is the Mediator pattern, as in Jimmy Bogard's library MediatR, where each request goes to one handler;[^mediatr] in MVVM it is the view model, and in the MVC of web frameworks the controller is where its job sits; on a server it is the route handler that receives the request and returns the answer; on a React client it is a hook that holds the state and runs the event.
Some find a mediator redundant next to ASP.NET MVC's controllers, since both receive a request and answer it.
I keep both: the controller is infrastructure, replaced the day requests stop arriving over HTTP, and the handler is a piece of software tested on its own, with no web server running.
On a client the repositories reach the network, so the orchestrator awaits them; nothing else in it changes.

A feature often has both: a client orchestrator for the screen and a server orchestrator for the request, each with its own repositories.
They share the same use cases.
The server enforces `lend`, and the client imports `mayBorrow` only to decide what to show, such as greying out "Lend" for a member with an overdue book.
The rule is written once and tested once, and the client's copy of the decision can never disagree with the server's.

## When a piece pays its way

Nothing in FOCUS exists for ceremony.
A use case exists when there is a rule, a repository when there is I/O, an orchestrator when an event leads to a new state, and a view when there is a screen.
A feature that shows a list of books with no rule has no use case: the orchestrator asks the repository and publishes what it got.
KISS, YAGNI and DRY decide when a piece is written: when a delivery needs its job, and not before.

On Ninjobs, I required every piece on every feature, trivial forms included, and showing one field took eight files.
The fault was the requirement, never the architecture: I let complexity grow, and lost KISS and YAGNI on the way ([chapter 9](09-birth-of-focus-kit.md)).
The four pieces are a place for each job, and a feature with fewer jobs has fewer pieces.

## What the team gains

"What happens when event X arrives?" is one test: call the orchestrator with the event and fake repositories, and check the state it returns.
Every rule sits in a use case, a pure function, so every rule has a test that needs no setup, and a reviewer or an agent finds the rule in one place.
No study measures a team with these pieces against the same team without them, and this book gives no baseline.

## Key points

* FOCUS is Feature-oriented (vertical slices), Clean (Clean Architecture's layers, with a use case that receives no repository because the orchestrator fetches and saves), Unidirectional (event, orchestrator, new state, nothing back, so a behaviour is one test) and Scalable (every piece isolated and tested).
* The view, a screen, a JSON answer or a printed line, fires events and renders state, formatting nothing; the orchestrator turns one event into one new state; a use case holds a decision, a validation or a format as a pure function; the repository fetches and saves through a driver, and turns an exception from data into a `Result`.
* The orchestrator receives its repositories as a parameter because its test passes fakes; the clock comes in as a value.
* Client and server have their own orchestrators and repositories and share the same use cases: the server enforces a rule, the client uses it to decide what to show.
* A piece is written when a delivery needs its job: a feature with no rule has no use case.

[^clean-architecture]: Robert C. Martin, "The Clean Architecture", 2012. <https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html>
[^bloc]: Bloc, "Bloc State Management Library", documentation, accessed 2026-09-29. <https://bloclibrary.dev/>
[^mediatr]: Jimmy Bogard, "MediatR", accessed 2026-09-29. <https://github.com/jbogard/MediatR>
