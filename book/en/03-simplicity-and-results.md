# 3. Simplicity and results: KISS, YAGNI, DRY and exceptions as values

After this chapter you can refuse a piece of code, a document or a check that no delivery needs, say which of KISS, YAGNI and DRY refuses it, and know the moment a shared version is due: the second concrete occurrence.
You can write a business rule as a pure function that returns a `Result`, and tell an exception from a refusal and from an error in any language.
You can also keep a library's exceptions at the boundary, so a new library changes one file, and let the compiler refuse a case you forgot to handle.

## What grew on Ninjobs

On Ninjobs, my own product, I let complexity grow, one reasonable addition at a time.
I required the full layered form of the architecture on every feature, trivial forms included, so showing one field on a screen took eight files; every delivery had to pass 29 checks that had never caught an error in the product.
The architecture was not at fault; KISS and YAGNI were lost (chapter 6 tells what went wrong and how the process restarted).

Fred Brooks split the difficulty of software in two in 1987: the essential complexity, which belongs to the problem itself, and the accidental complexity, which the people building it add along the way.[^brooks-silver-bullet]
Nobody can remove the first; the second is a choice, made one file at a time, and the three principles of this chapter are three ways to refuse it.
An agent makes the choice cheaper to get wrong: it writes the layer, the option and the third copy in seconds, each one plausible, and each one is then code that someone must read, review and keep true.

## KISS: keep it simple

"Keep it simple, stupid" is credited to Kelly Johnson, the aircraft engineer who led Lockheed's Skunk Works, whose rule was that what his engineers designed had to be repairable in the field by an average mechanic with a handful of ordinary tools.
The rule is about the person who comes next: the design must be simple enough for them, under pressure, without its author in the room, because a thing that is simple is a thing that can be understood and fixed.

In code, the person who comes next is a colleague, an agent in a fresh session, or you in six months.
KISS asks for the plainest form that does the job: a function before a class, a value before a configuration, one file before three.
The code examples of this book are written for it, in TypeScript, short enough to hold in your head; the ideas hold in any language.
The due date of a loan in the lending library, the example of Part I, is 21 days after the loan:

```ts
const LOAN_DAYS = 21;

function dueDate(today: string): string {
	const due = new Date(today);

	due.setUTCDate(due.getUTCDate() + LOAN_DAYS);

	return due.toISOString().slice(0, 10);
}
```

It takes a date and returns a date, and anyone can read it in one pass.

In a process, KISS asks the same of every step: the fewest documents that hold what the project knows, the fewest commands that carry a delivery, the fewest marks that say where it stands.
A step a newcomer cannot explain after reading it once is a step to question.

## YAGNI: you aren't gonna need it

YAGNI comes from Extreme Programming, the method Kent Beck described in *Extreme Programming Explained* in 1999.[^beck-xp]
Martin Fowler traces the phrase to a conversation on the project where XP took shape: to each capability a colleague said the system would soon need, Beck answered that they were not going to need it.[^fowler-yagni]
The rule: a capability you presume the software will need later is not built now.

A presumptive feature that nobody needs wastes the effort of building it, and one that is needed after all usually has to be reworked, because the needs moved while it waited.
Even the presumptive feature that turns out to be right pays delay and carry: the feature that has value now waits while it is built, and its code "*adds some complexity to the software*" for as long as it stays.[^fowler-yagni]
Suppose someone expects the library to lend for different periods to different kinds of member, and writes it now:

```ts
type MemberCategory = "adult" | "child" | "researcher";

type LoanPolicy = {
	daysFor(category: MemberCategory): number;
	renewals(category: MemberCategory): number;
};
```

The product document names no category and no renewal.
Every reader of `lend` now has to learn a policy the library does not have, every test has to pass one, and when categories do arrive, they will not be these three.
`LOAN_DAYS = 21` is the whole rule until a delivery asks for more.

Fowler draws the limit in the same article: YAGNI "*only applies to capabilities built into the software to support a presumptive feature, it does not apply to effort to make the software easier to modify*".[^fowler-yagni]
A test, a clear name, a rule moved out of a screen into a function of its own: these are internal quality, and YAGNI never argues against them.
YAGNI works only in code that is easy to change, because the promise is that you will add the capability when it is needed, and cheap change is what makes that promise true.

## DRY: one place for each piece of knowledge

Andy Hunt and Dave Thomas named DRY, "don't repeat yourself", in *The Pragmatic Programmer* in 1999: "*Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.*"[^pragmatic-programmer]
The unit is knowledge.
Two identical lines may be two pieces of knowledge, and one piece of knowledge may be written in two lines that look nothing alike.

"A loan lasts 21 days" is one piece of knowledge.
Written as `21` in `dueDate` and again as "Due in 21 days" in the lending screen, it is in two places, and the day the library moves to 14 days one of them will be missed.
The screen imports `LOAN_DAYS`, and the knowledge lives in one place.

"A member's name cannot be empty" and "a book's title cannot be empty" are two pieces of knowledge that happen to read the same today.
Merge them into one `nonEmpty` rule shared by members and books, and the day a title may be empty for an untitled manuscript, the change reaches members too.

Sandi Metz named the opposite failure in 2016: "*duplication is far cheaper than the wrong abstraction*".[^metz-wrong-abstraction]
The wrong abstraction is the shared function that two callers used for different reasons; each new caller adds a parameter and a condition, until nobody can change it without breaking someone.
Her remedy is to put the code back into each caller and start again from what each one needs.
DRY and Metz agree: one place for each piece of knowledge, and a shared version only for what is the same knowledge.

## Abstraction on the second occurrence

The three principles meet in one rule, which this book's process writes into every project: an abstraction is written on the second concrete occurrence, and the delivery that writes it says which was the first.
One copy is no evidence that a shared version is needed: it is a guess, and YAGNI refuses guesses.
Two copies are the error that already happened, and DRY asks for one place.
Naming the first copy makes the move checkable: a reviewer opens both and sees that they are the same knowledge, which is Metz's test.

In the lending library, `Result`, the type that carries either a value or what stopped it (its own section follows), first appears inside the loans feature, as the return type of `lend` in `features/loans/rules.ts`.
It stays there while it has one user.
Then a delivery for members needs a rule that can refuse, and `Result` would be written a second time; that delivery moves it to `src/lib/result.ts`, the folder for code that belongs to no single feature (chapter 4), and says so:

```ts
// First use: features/loans/rules.ts (lend).
// Second use: features/members/rules.ts (register).
export type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };
```

`ok` and `err`, the two functions that build a `Result`, move with it, and both features import them from there.
Had the move come on the first use, it would have been a guess that happened to be right; on the second, it is a fact with two witnesses.

## A pure function

A rule that lives inside a screen, a controller or a database call cannot be tested without that screen, controller or database.
A function is pure when the same input always gives the same output and nothing else happens: no read from a database, no write to a file, no clock, no network.
Its test is data in, value out, and it needs no setup.
An impure function needs the world arranged before it runs, and every test pays for that arrangement.

In the lending library, the rule "a member with an overdue book cannot borrow another" is a pure function:

```ts
type Member = { id: string; overdue: number };

type Refusal = "HasOverdueBooks";

function mayBorrow(member: Member): Result<Member, Refusal> {
	if (member.overdue > 0) return err("HasOverdueBooks");
	return ok(member);
}
```

It reads a member and answers.
Where the member came from, a database or a test, is not its business.
Immutability is the same idea on data: a function that changes its input hides a second output, so `mayBorrow` returns the member it received or a refusal, and changes nothing.

Clean Architecture, as it is usually practised, injects the repositories into the use case that holds the rule, so its test needs a fake for each one; this book keeps `mayBorrow` pure, receiving a member and not a way to fetch one, and leaves fetching and saving to an orchestrator, the function around the rule that chapter 4 builds.

## Result: the value that carries a failure

`Result` is a type that holds either the value or what stopped it:

```ts
type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };

function ok<T>(value: T): Result<T, never> {
	return { ok: true, value };
}

function err<E>(error: E): Result<never, E> {
	return { ok: false, error };
}
```

The caller reads `ok` before it can reach `value` or `error`, and the compiler narrows the type on that check.

The reason to carry a failure in a value, whatever its shape, a union type as here or an enum, is what the compiler does with it: a `switch` over the failure that leaves one case out does not compile.
Every outcome a rule can produce is either handled or a compile error, and that error is the whole value of the construction: the compiler, and not a code review, guarantees that no case was forgotten, on the day the rule is written and on the day a case is added.
The section "Every case handled" shows the check in TypeScript.

The field calls the principle "errors as values", after Go's "*errors are values*";[^go-errors] this book says "exceptions as values", and the next section says why.

## Exception, refusal, error

A failure is one of three things, and the class name never tells you which.
JavaScript's built-in failures are all an `Error`, and .NET's are all an `Exception`, so the cause decides.
Dart is the one language I have seen make the difference visible: its `dart:core` has an `Exception` class, "*intended to be caught*", and an `Error` class, for "*a program failure that the programmer should have avoided*".[^dart-core]

* **An exception** is an expected failure from outside the program: the database is down, the network dropped, the disk is full.
  No code is wrong.
  It is caught at the boundary with the outside world and returned as a value, for two reasons.
  The exception belongs to the domain that threw it: a sign-in library throws its own `AppleSignInException`, and the application's domain has no idea what Apple sign-in is; all it needs to know is that the login failed.
  Translated into a value, `LoginFailed`, the failure speaks the application's language, and, as a member of a type, it enters the exhaustive check: every exception the application can meet is handled, and the compiler proves it.
* **A refusal** is a rule saying no: a member with overdue books, a phone number with too few digits, a time already taken.
  Nothing failed; the rule did its job.
  It is returned as a value too, and it is the most common outcome a program handles.
* **An error** is a bug: code that is wrong.
  It is never caught.
  It reaches your screen while you develop and your analytics once the program runs, so that you fix it.

That is why this book does not say "errors as values".
An error is a bug, and a bug is never a value: it is a fix.
What travels in a `Result` is an exception or a refusal.

## Why not throw

A function returns one value, and its signature says which.
A throw used to steer the flow, in place of a return, costs three things.
It leaves through an exit the call site does not show: the function "returns" something its signature never mentioned, through a path the caller did not write, and every call inside it is one more such door.
It makes the signature lie: `function lend(...): Loan` says nothing about the three ways it can fail, so the compiler cannot check that every case is handled, while `Result<Loan, LendRefusal>` says it in the type, and a `switch` over the refusal that forgets a case fails to compile.
And the catch wide enough to steer the flow also catches the bugs that happen inside it, and they vanish into a message nobody reads.

Most of what a program handles is a rule saying no, so a program that throws for refusals has a hidden exit on every rule, the caller and the agent that reads the code have to know from memory which failures were meant, and every refusal pays for a thrown and caught exception: in Stephen Toub's benchmark, a thousand throws, each caught through ten asynchronous calls, took about an eighth of a second on .NET 8.[^toub-net9]

## Where the catch lives

Exceptions exist only where the program touches the outside world: a database call, a network request, a file, the phone's storage.
So that is the only place a `try`/`catch` lives, and it does one thing: turn the library's exception into the program's value.

```ts
type DatabaseFailed = { code: "DatabaseFailed"; message: string };

function query<T>(run: () => T): Result<T, DatabaseFailed> {
	try {
		return ok(run());
	} catch (thrown) {
		const message = thrown instanceof Error ? thrown.message : String(thrown);
    
		return err({ code: "DatabaseFailed", message });
	}
}
```

Every call to the database runs inside `query`, and nothing past it knows which database library is in use.
Domain-driven design calls such a translator an anti-corruption layer, whose "*core purpose ... is to protect the domain model*";[^anti-corruption-layer] this book takes one step more and translates the exceptions too.
Replace the database library and `query` changes; the rest of the program does not.

The same boundary can turn an exception into a refusal.
When two members borrow the last copy at the same moment, a unique index in the database refuses the second write.
The code that ran the write reads that failure and returns the refusal `AlreadyLent`, since nothing broke: the rule held, in the one place two requests cannot race.
Any other failure of the same write stays `DatabaseFailed`.

A catch this wide also catches a bug thrown inside `run`, and turns it into `DatabaseFailed`.
Two things bring the bug back to you: a test that runs every database call against a real, in-memory database and checks the value it gets (chapter 5), and a log line that prints the `message` before the program answers.

Two kinds of throw pass the boundary untouched, a fatal one, such as running out of memory, and a framework's own control flow, thrown on purpose.
So the rule reads: catch at the boundary with the outside world, translate, and let everything else pass.

## Every case handled

A `Result` pays off when the compiler checks the handling.
In TypeScript a `Record` over the refusal type must name every member:

```ts
type LendRefusal = "HasOverdueBooks" | "AlreadyLent" | "MemberSuspended";

const message: Record<LendRefusal, string> = {
	HasOverdueBooks: "Return your overdue books first.",
	AlreadyLent: "This copy was just lent to someone else.",
	MemberSuspended: "Your membership is suspended.",
};
```

Add a refusal to the rules and forget its message, and the build fails, before any user sees a blank screen.
In Rust and Dart an exhaustive `match` or `switch` does the same; in Go, a linter.

## The same principles in a process

> **Caution.** An agent writes more than code at this speed: it also writes scripts, checks, rules and steps, each one plausible, and a process grows the way code does, one reasonable addition at a time.
> While this book was being written, the agent proposed that every milestone end with a review step, a good idea; the review found errors, which opened a milestone of fixes, whose own review opened a second, and a third was on its way when I stopped it.
> What I should have been doing was reading the chapters and saying what to change.
> On its own, the agent had entered a spiral of checks that checked checks, and one question is what stops it: which concrete error would this step have caught?

Chapter 16, the governor, turns that question into the rule every step of the process must answer: a step enters when it names the concrete error it would have caught, and leaves when it names none.

## What the team gains

Less to read, less to review and less to keep true: every file, option and check that is not written is one that no person reviews, no agent loads into a session and no delivery has to satisfy, while Ninjobs made every delivery pass 29 checks that had never caught an error.
Every rule is a function a test calls with data, so a rule has a test before it has a screen, and an agent asked to change it finds it in one place, with its cases named in its type.
Every failure a caller must handle is in the signature, so a reviewer reads the type and knows what can go wrong, and a forgotten case is a compile error.

## Key points

* Accidental complexity is the part people add; it is a choice, and KISS (the plainest form that does the job), YAGNI (nothing built for a presumed need) and DRY (one place for each piece of knowledge) are three ways to refuse it.
* An abstraction is written on the second concrete occurrence, and the delivery says which was the first; in a process, a step enters only when it names the concrete error it would have caught.
* A business rule is a pure function: data in, a `Result` out, no I/O and no clock; fetching and saving belong to the orchestrator around it.
* A failure is an exception (from outside, caught at the boundary and returned in the domain's own words), a refusal (a rule saying no, returned as a value) or an error (a bug, never caught); a throw steers no flow.
* The value of a `Result` is the exhaustive check: a `Record`, `match` or `switch` that forgets a case fails to compile.

[^brooks-silver-bullet]: Frederick P. Brooks Jr., "No Silver Bullet: Essence and Accidents of Software Engineering", IEEE Computer 20(4), 1987.
[^beck-xp]: Kent Beck, "Extreme Programming Explained: Embrace Change", Addison-Wesley, 1999.
[^fowler-yagni]: Martin Fowler, "Yagni", martinfowler.com, 2015-05-26, accessed 2026-09-30. <https://martinfowler.com/bliki/Yagni.html>
[^pragmatic-programmer]: Andrew Hunt and David Thomas, "The Pragmatic Programmer", Addison-Wesley, 1999; 20th anniversary edition, 2019.
[^metz-wrong-abstraction]: Sandi Metz, "The Wrong Abstraction", 2016-01-20, accessed 2026-09-30. <https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction>
[^go-errors]: Rob Pike, "Errors are values", The Go Blog, 2015. <https://go.dev/blog/errors-are-values>
[^dart-core]: Dart, "Exception class" and "Error class", `dart:core` API reference, accessed 2026-09-29. <https://api.dart.dev/stable/dart-core/Exception-class.html> and <https://api.dart.dev/stable/dart-core/Error-class.html>
[^toub-net9]: Stephen Toub, "Performance Improvements in .NET 9", .NET Blog, 2024-09-12, section "VM", benchmark `ExceptionThrowCatch`, accessed 2026-09-30. <https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-9/>
[^anti-corruption-layer]: Microsoft, "Anti-Corruption Layer pattern", Azure Architecture Center, accessed 2026-09-30. <https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer>
