# 4. FOCUS: features, not layers, and the four pieces

After this chapter you can organize code in vertical slices, one folder per feature, and place every file of a feature in one of the four pieces of FOCUS, view, orchestrator, use case or repository, knowing what each forbids.
You can follow one event through them to one new state, and answer "what happens when event X arrives?" with one test.
You can also decide which piece receives a dependency as a parameter, by one question: does its test pass a second implementation?

## The problem

Many projects sort their code by technical layer: a folder of screens, one of controllers, one of services, one of models, one of database access.
Every feature is spread across all of them.
Lending a book in such a library touches a file in `views/`, `controllers/`, `services/`, `models/` and `repositories/`, and a change to how lending works is a change to five folders.

The cost falls on whoever makes the change.
A person has to find the five files and keep them in mind at once; an agent has to open all five folders to learn what lending does, and every file it loads to understand the change fills the context it works in.
The folders say what the code is made of, and nothing about what the program does.

The rules fare no better.
In most applications a business rule lives wherever someone needed it first: part in a screen that hides a button, part in the handler that saves the form, and a copy in a query.
Ask "what happens when a librarian lends this copy to this member?" and nobody can answer by reading one place.
You find out by running the app, clicking, and watching the database.
A person cannot test that answer without the whole app, and an agent asked to change the rule finds two of its three copies and changes those.

FOCUS is this book's name for one way out of both: one folder per feature, and in it four pieces, each with one job, and one direction for everything that flows between them.

## The dependency rule

Layers answered a real problem: rules mixed with screens and SQL cannot be changed, or tested, one without the others.
Robert C. Martin drew the answer in 2012 as concentric circles, with the business rules at the center and the database, the web and the frameworks at the edge, held together by the dependency rule, "*source code dependencies can only point inwards*", so a rule never names a screen, a table or a library.[^martin-clean-2012]
Martin also asked, in 2011, what a project's top-level folders scream, the system or the framework it was built with, and folders named `controllers/` and `models/` scream the framework.[^martin-screaming]
This book keeps the dependency rule and drops the folder per layer, and with it the ceremony of an interface and a mapping at every boundary for code that has one implementation.

## Vertical slices

A vertical slice is one folder that holds everything a feature needs: its screens, its calls to the server, its routes, its rules, its database access and its tests.
Jimmy Bogard named the style in 2018 after years of building systems this way, and gave its rule in one line: "*Minimize coupling between slices, and maximize coupling in a slice.*"[^bogard-vertical-slice]
Code that changes together lives together; code that changes for different reasons lives apart.

The lending library, the example of Part I, is laid out like this:

```text
src/features/loans/          LendView.tsx, lendEvents.ts, rules.ts,
                             repository.server.ts, route.server.ts,
                             rules.test.ts, lendEvents.test.ts,
                             repository.server.test.ts
src/features/loans/return/   returning a copy
src/features/members/        what the library keeps about a member
src/features/catalog/        books and copies
src/lib/result.ts            Result, ok and err
```

`LendView.tsx` is the lending screen; `lendEvents.ts` receives what the screen asks for and answers with the new state; `rules.ts` holds the rules of chapter 3, such as `lend`; `repository.server.ts` reads and writes the database, and `route.server.ts` is the server's address for the loan.
A name ending in `.server.ts` runs only on the server, and client code never imports one.
The tests sit beside the code they test.
Each of these files is one of the four pieces this chapter names further on, and chapter 5 gives each its test.

The top folder screams the library: loans, members, catalog.
A change to how lending works touches `loans/`, and removing loans from the product removes one folder.
Parnas's criterion of 1972 works at this size too: the slice hides its feature's decisions from the rest of the program.

## What one feature is

A feature is one thing the app keeps, named by a term of the project's vocabulary (the loan, the member, the book), or one thing the app does that keeps nothing, named by what it does, such as a `status` check that answers whether the service is up.
Its slice holds every action on it.
Lending and returning both act on the loan: they share its rules, its table and its repository, so they are one slice.
Members and books are other things the library keeps, each with its own table and its own screens, so each has a slice of its own.

A sub-feature is a subfolder.
Returning a copy has its own screen and its own event, and it lives in `loans/return/`, inside the slice whose loan it closes.

A file appears in a slice when it pays its way.
A feature with no rule has no `rules.ts`, and a feature that keeps nothing has no repository.
Keeping nothing does not make it less of a feature: if it has its own route or screen, it has its own slice.

## Where shared code lives

What code is about decides where it lives when two features use it.
Code about one feature stays in that feature's slice, and another slice imports what it needs from there, be it a type, a repository function or a view.
`loans/rules.ts` imports the `Member` type from `members/`, because a member is what that slice keeps; a member's page that lists their loans imports from `loans/`.
Two slices may import from each other.

What belongs to no feature, the shape of a value such as an email address, or plumbing such as `Result`, leaves the slices for `src/lib/`.
It moves there on its second use and not before, the rule of chapter 3, and the file says where its first and second uses are.

## FOCUS, letter by letter

**F, Feature-oriented.** The code is organized in the vertical slices above, and the four pieces of a feature live in its folder, side by side.

**C, Clean.** The pieces are the layers of Martin's Clean Architecture, and they keep its dependency rule.
In his drawing a use case talks to storage through an interface it receives, so a rule can still reach I/O, only through a door with a different name, and its test needs a double behind every door.[^martin-clean-2012]
FOCUS corrects that with the orchestrator, which fetches and saves around the use case, so a use case receives no repository at all: it is a pure function, data in, a `Result` out, and it holds every kind of business rule, a decision such as who may borrow, a validation such as whether a card number is well formed, a format such as how a due date reads to the user.

**U, Unidirectional.** Everything flows one way: an event, the orchestrator, the use cases and repositories it calls, and a new state.
There is no binding, the mechanism some frameworks offer where a field on the screen and a value in memory update each other in both directions.
No state travels back: the view never changes the state it renders, and a use case never calls a repository.
So "what happens when event X arrives?" has one answer, and one test can check it.
That test is the test of a behaviour: "the user wants to sign in with Google" is one event, everything it sets off is one path through the orchestrator, and what comes out is one state, a confirmed sign-in or a failure, so the test reads "given this intention, this state", with nothing to inspect in between.

**S, Scalable.** Every piece is isolated and has its own test, so a new feature adds its own folder and its own tests and changes no other.

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
These are the steps between them:

1. **The view fires the event**, `LendRequested { copyId, memberId }`, and does nothing else.
2. **The orchestrator receives it** and checks it carries both ids; on a server the event is the request, so reading its body is part of receiving it.
3. **The repositories fetch** the member, through `findMember`, and the copy, through `findCopy`.
4. **The use case decides**: `lend` returns a `Loan` due 21 days later, or the refusal `HasOverdueBooks` or `MemberSuspended`.
5. **The repository saves**: `insertLoan` turns the unique index's refusal of a second open loan on the copy into `AlreadyLent`, as [chapter 3](03-simplicity-and-results.md) showed.
6. **The orchestrator publishes the new state**, which the view renders: `Lent` shows the due date, `Refused` "Return your overdue books first.", `Failed` "Could not reach the library's database. Try again."

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
Three more things the code shows:

* **The repositories are a parameter.** The server passes the real ones, bound to its database, and nothing else in the function comes from outside.
* **A test passes fakes.** A fake is a second implementation that answers what the test sets, so the test knows which repositories were called, with what, and what state came out, and the whole flow of a feature is proven with no database and no screen (chapter 5 shows the test).
* **The clock is a value.** `today` is read once, where the event arrives, and handed on as data; neither `lendRequested` nor `lend` reads the clock, so a test of a due date passes the date it wants.

## Dependencies only where a fake exists

A dependency is something a piece of code needs from outside itself to run: the database, the network, the clock, another module.
Martin Fowler named the practice of handing it in from outside in 2004: after long discussion, he wrote, "*we settled on the name Dependency Injection*".[^fowler-injection]
Mark Seemann added where the real parts are assembled: in one place, "*as close as possible to the application's entry point*", which he called the composition root.[^seemann-composition-root]

Injected everywhere, dependencies become their own layer of ceremony: an interface for every class, a container, a parameter nobody varies.
Injecting everywhere solves a real problem in an SDK, whose callers need to replace parts they do not own, and is ceremony inside an application, where each of those interfaces has one implementation for good.
DRY already gives the rule: something with no reason to exist does not exist.
If in an application only the repositories have two implementations, the real one and the fake the tests pass, then only the repositories get an interface, or a parameter; a use case that will always be the one concrete function gets neither.
This book draws that narrower line: a piece receives a dependency as a parameter only where its test passes a second implementation.

`lendRequested(event, today, repositories)` is that line drawn once: the orchestrator receives its repositories because its test passes fakes.
The rest follows from the same test.

* **A server repository receives the database it uses**, `findMember(db, id)`, because its test passes an in-memory database with the real migrations; the server's start code opens the real one and hands it on, and that is the composition root.
* **A use case receives none.** `lend` takes data and returns a value; its test passes data, and there is nothing to swap.
* **A view receives none.** It has one implementation, and a parameter there would exist for ceremony, which KISS rules out.

## The orchestrator elsewhere

The orchestrator has other names in other stacks, and the job is the same.
In Flutter it is a BLoC, a class that receives events and emits states;[^bloc] in .NET it is the Mediator pattern, as in Jimmy Bogard's library MediatR, where each request goes to one handler;[^mediatr] in MVVM it is the view model, and in the MVC of web frameworks the controller is where its job sits; on a server it is the route handler that receives the request and returns the answer; on a React client it is a hook that holds the state and runs the event.
On a client the repositories reach the network, so the orchestrator awaits them; nothing else in it changes.

## When a piece pays its way

Nothing in FOCUS exists for ceremony.
A use case exists when there is a rule, a repository when there is I/O, an orchestrator when an event leads to a new state, and a view when there is a screen.
A feature that shows a list of books with no rule has no use case: the orchestrator asks the repository and publishes what it got.
KISS, YAGNI and DRY decide when a piece is written: when a delivery needs its job, and not before.
On Ninjobs I required every piece on every feature and one field took eight files ([chapter 3](03-simplicity-and-results.md)); the fault was the requirement, and the four pieces are a place for each job, so a feature with fewer jobs has fewer pieces.

## What the team gains

A change touches one folder, and an agent reads one slice.
A delivery on lending names `loans/`, and the agent loads the screen, the event, the rules, the database access and their tests side by side, and nothing about another feature; the dependencies it meets are the ones a test swaps, so the tests show it what to fake and nothing else.
A reviewer sees a delivery's diff inside one folder and knows it touched nothing else, and removing a feature is removing a folder.

"What happens when event X arrives?" is one test: call the orchestrator with the event and fake repositories, and check the state it returns.
Every rule sits in a use case, a pure function, so every rule has a test that needs no setup, and a reviewer or an agent finds the rule in one place.

Client and server share the use cases.
A feature often has a client orchestrator for the screen and a server orchestrator for the request, each with its own repositories, and both call the same rules: the server enforces `lend`, and the client imports `mayBorrow` only to decide what to show, such as greying out "Lend" for a member with an overdue book.
The rule is written once and tested once, and the client's copy of the decision can never disagree with the server's.

None of this has a number: as the prologue says, the book counted no team before and after the practices of Part I.

## Key points

* A vertical slice keeps everything one feature needs in one folder; a feature is one thing the app keeps, or one thing it does that keeps nothing, and code that belongs to no feature moves to `lib/` on its second use.
* FOCUS is Feature-oriented (vertical slices), Clean (the dependency rule, with a use case that receives no repository because the orchestrator fetches and saves), Unidirectional (event, orchestrator, new state, nothing back, so a behaviour is one test) and Scalable (every piece isolated, with its own test).
* The view fires events and renders state, formatting nothing; the orchestrator turns one event into one new state; a use case holds a decision, a validation or a format as a pure function; the repository fetches and saves through a driver, and turns an exception from data into a `Result`.
* A piece receives a dependency only where its test passes a fake: orchestrators and server repositories do, use cases and views do not, and the clock is a value.
* A piece is written when a delivery needs its job, and client and server share the same use cases, so a rule is written and tested once.

[^martin-clean-2012]: Robert C. Martin, "The Clean Architecture", The Clean Code Blog, 2012-08-13, accessed 2026-09-30. <https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html>
[^martin-screaming]: Robert C. Martin, "Screaming Architecture", The Clean Code Blog, 2011-09-30, accessed 2026-09-30. <https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html>
[^bogard-vertical-slice]: Jimmy Bogard, "Vertical Slice Architecture", 2018, accessed 2026-09-30. <https://www.jimmybogard.com/vertical-slice-architecture/>
[^fowler-injection]: Martin Fowler, "Inversion of Control Containers and the Dependency Injection pattern", martinfowler.com, 2004, accessed 2026-09-30. <https://martinfowler.com/articles/injection.html>
[^seemann-composition-root]: Mark Seemann, "Composition Root", 2011-07-28, accessed 2026-09-30. <https://blog.ploeh.dk/2011/07/28/CompositionRoot/>
[^bloc]: Bloc, "Bloc State Management Library", documentation, accessed 2026-09-29. <https://bloclibrary.dev/>
[^mediatr]: Jimmy Bogard, "MediatR", accessed 2026-09-29. <https://github.com/jbogard/MediatR>
