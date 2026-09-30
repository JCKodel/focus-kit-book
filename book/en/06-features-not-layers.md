# Features, not layers

After this chapter you can organize code in vertical slices, one folder per feature, decide what one feature is and where code that two features share belongs.
You can also decide which piece receives a dependency as a parameter and which receives none, by one test: does its test pass a second implementation?

## The problem

Many projects sort their code by technical layer: a folder of screens, one of controllers, one of services, one of models, one of database access.
Every feature is spread across all of them.
Lending a book in such a library touches a file in `views/`, `controllers/`, `services/`, `models/` and `repositories/`, and a change to how lending works is a change to five folders.

The cost falls on whoever makes the change.
A person has to find the five files and keep them in mind at once; an agent has to open all five folders to learn what lending does, and every file it loads to understand the change fills the context it works in (chapter 2).
The folders say what the code is made of, and nothing about what the program does.

## Layers, and what they were for

Layers answered a real problem: rules mixed with screens and SQL cannot be changed, or tested, one without the others.
Robert C. Martin drew the answer in 2012 as concentric circles, with the business rules at the center and the database, the web and the frameworks at the edge, held together by one rule, the dependency rule: "*source code dependencies can only point inwards*".[^martin-clean-2012]
A rule never names a screen, a table or a library, so the outside can change without touching it.
He developed it in the book *Clean Architecture* in 2017.[^martin-clean-2017]

Alistair Cockburn had drawn the same boundary in 2005 as a hexagon, the pattern he called ports and adapters, whose intent is to "*allow an application to equally be driven by users, programs, automated test or batch scripts, and to be developed and tested in isolation from its eventual run-time devices and databases*".[^cockburn-hexagonal]
And Martin himself asked, in 2011, what a project's top-level folders scream: the system, a library or a health care system, or the framework it was built with.[^martin-screaming]
A project whose folders are `controllers/` and `models/` screams its framework.

This book keeps the dependency rule: a rule imports nothing from a screen, a database or a library.
It drops the folder per layer, and with it the ceremony of an interface and a mapping at every boundary for code that has one implementation.

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

`LendView.tsx` is the lending screen; `lendEvents.ts` receives what the screen asks for and answers with the new state; `rules.ts` holds the rules of chapter 5, such as `lend`; `repository.server.ts` reads and writes the database, and `route.server.ts` is the server's address for the loan.
A name ending in `.server.ts` runs only on the server, and client code never imports one.
The tests sit beside the code they test.
Chapter 7 names these four kinds of file as the four pieces, and chapter 8 gives each its test.

The top folder screams the library: loans, members, catalog.
A change to how lending works touches `loans/`, and removing loans from the product removes one folder.
Parnas's criterion of 1972 (chapter 4) works at this size too: the slice hides its feature's decisions from the rest of the program.

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
It moves there on its second use and not before, the rule of chapter 4, and the file says where its first and second uses are.

## Dependencies only where a fake exists

A dependency is something a piece of code needs from outside itself to run: the database, the network, the clock, another module.
Martin Fowler named the practice of handing it in from outside in 2004: after long discussion, he wrote, "*we settled on the name Dependency Injection*".[^fowler-injection]
Mark Seemann added where the real parts are assembled: in one place, "*as close as possible to the application's entry point*", which he called the composition root.[^seemann-composition-root]

Injected everywhere, dependencies become their own layer of ceremony: an interface for every class, a container, a parameter nobody varies.
This book draws a narrower line: a piece receives a dependency as a parameter only where its test passes a second implementation.
That second implementation is a fake: a repository that answers what the test sets, or an in-memory database with the real tables.

The orchestrator of the loans slice receives its repositories:

```ts
export const lendRepositories = { findMember, findCopy, insertLoan };

export async function lendRequested(
	event: LendRequested,
	today: string,
	repositories = lendRepositories,
): Promise<LendState> {
	const member = await repositories.findMember(event.memberId);
	if (!member.ok) return { kind: "Failed", exception: member.error };
	const copy = await repositories.findCopy(event.copyId);
	if (!copy.ok) return { kind: "Failed", exception: copy.error };
	const loan = lend(copy.value, member.value, today);
	if (!loan.ok) return { kind: "Refused", refusal: loan.error };
	const saved = await repositories.insertLoan(loan.value);
	if (saved.ok) return { kind: "Lent", loan: saved.value };
	if (saved.error === "AlreadyLent") return { kind: "Refused", refusal: "AlreadyLent" };
	return { kind: "Failed", exception: saved.error };
}
```

The screen calls `lendRequested(event, today)` and gets the real repositories by default; the test passes fakes in their place.
The rest follows from the same test.

* **An orchestrator receives its repositories**, because its test passes fake ones.
* **A server repository receives the database it uses**, `findMember(db, id)`, because its test passes an in-memory database with the real migrations; the server's start code opens the real one and hands it on, and that is the composition root.
* **A use case receives none.** `lend` takes data and returns a value; its test passes data, and there is nothing to swap.
* **A view receives none.** It has one implementation, and a parameter there would exist for ceremony, which KISS rules out (chapter 4).
* **The clock is passed as a value.** `today` is read once, where the event arrives, and handed on as data; no rule reads the clock, so a test of a due date passes the date it wants.

## What this gives an agent

A delivery on lending names one slice, and the agent reads that folder: the screen, the event, the rules, the database access and their tests, side by side.
It does not search five layers for the parts of one feature, and what it loads into its context is what the change is about.
The dependencies it meets are the ones a test swaps, so the tests show it what to fake and nothing else.

## What the team gains

A change touches one folder, and an agent reads one slice.
A reviewer sees a delivery's diff inside one folder and knows it touched nothing else, and removing a feature is removing a folder.
The book has no measured baseline for this against a layered layout; it states it as a description of the structure, and each reader can check it on the next change in their own code.

## Key points

* Folders per layer spread one feature over five places; a vertical slice keeps everything one feature needs in one folder.
* The dependency rule stays: a rule imports nothing from a screen, a database or a library.
* A feature is one thing the app keeps, named by the vocabulary, or one thing it does that keeps nothing; a sub-feature is a subfolder.
* Shared code stays in the slice it is about and is imported from there; code that belongs to no feature moves to `lib/` on its second use.
* A piece receives a dependency only where its test passes a fake: orchestrators and server repositories do, use cases and views do not, and the clock is a value.

[^martin-clean-2012]: Robert C. Martin, "The Clean Architecture", The Clean Code Blog, 2012-08-13, accessed 2026-09-30. <https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html>
[^martin-clean-2017]: Robert C. Martin, "Clean Architecture: A Craftsman's Guide to Software Structure and Design", Prentice Hall, 2017.
[^cockburn-hexagonal]: Alistair Cockburn, "Hexagonal Architecture", 2005, accessed 2026-09-30. <https://alistair.cockburn.us/hexagonal-architecture/>
[^martin-screaming]: Robert C. Martin, "Screaming Architecture", The Clean Code Blog, 2011-09-30, accessed 2026-09-30. <https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html>
[^bogard-vertical-slice]: Jimmy Bogard, "Vertical Slice Architecture", 2018, accessed 2026-09-30. <https://www.jimmybogard.com/vertical-slice-architecture/>
[^fowler-injection]: Martin Fowler, "Inversion of Control Containers and the Dependency Injection pattern", martinfowler.com, 2004, accessed 2026-09-30. <https://martinfowler.com/articles/injection.html>
[^seemann-composition-root]: Mark Seemann, "Composition Root", 2011-07-28, accessed 2026-09-30. <https://blog.ploeh.dk/2011/07/28/CompositionRoot/>
