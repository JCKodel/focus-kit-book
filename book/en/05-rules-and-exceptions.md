# Rules as pure functions, exceptions as values

After this chapter you can write a business rule as a pure function that returns a Result, tell an exception from a refusal and from an error in any language, and say why a throw must never steer the program's flow.
You can also keep a library's exceptions out of your domain, so a new library changes one file.

## The problem

A rule that lives inside a screen, a controller or a database call cannot be tested without that screen, controller or database.
A failure that is thrown leaves the function through a door the caller cannot see, and the compiler cannot tell the caller which doors exist.
Both habits make a program that works on the happy path and surprises everyone off it, and an agent that reads such code has no way to know which failures were meant.

## A pure function

A function is pure when the same input always gives the same output and nothing else happens: no read from a database, no write to a file, no clock, no network.
Its test is data in, value out, and it needs no setup.
An impure function needs the world arranged before it runs, and every test pays for that arrangement.

A lending library keeps books and members.
The rule "a member with an overdue book cannot borrow another" is a pure function:

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
Go returns errors as ordinary values, "*errors are values*", and handles them with ordinary code;[^go-errors] Rust puts the recoverable failure in the return type, `Result<T, E>`;[^rust-result] Scott Wlaschin drew the same idea as two tracks, success and failure, that every step of a pipeline rides on.[^wlaschin-rop]
The field calls the principle "errors as values".
This book says "exceptions as values", and the next section says why.

## Exception, refusal, error

A failure is one of three things, and the class name never tells you which.
JavaScript's built-in failures are all an `Error`, and .NET's are all an `Exception`, so the cause decides.
Dart is the one language I have seen make the difference visible: its `dart:core` has an `Exception` class, "*intended to be caught*", and an `Error` class, for "*a program failure that the programmer should have avoided*".[^dart-core]

* **An exception** is an expected failure from outside the program: the database is down, the network dropped, the disk is full.
  No code is wrong.
  It is caught at the boundary with the outside world and returned as a value.
* **A refusal** is a rule saying no: a member with overdue books, a phone number with too few digits, a time already taken.
  Nothing failed; the rule did its job.
  It is returned as a value too, and it is the most common outcome a program handles.
* **An error** is a bug: code that is wrong.
  It is never caught.
  It reaches your screen while you develop and your analytics once the program runs, so that you fix it.

Eric Lippert sorted every thrown value into four kinds in 2008: "fatal", which nobody can handle; "boneheaded", "*your own darn fault*", this book's error; "vexing", thrown by an API that could have returned a value, such as parsing text a user typed; and "exogenous", "*untidy external realities*", this book's exception.[^lippert-vexing]
The refusal is the kind that is missing from that list, because a refusal is never thrown: it is what a rule returns.

That is why this book does not say "errors as values".
An error is a bug, and a bug is never a value: it is a fix.
What travels in a `Result` is an exception or a refusal.

## Why not throw

A throw used to steer the flow, rather than a return, costs four things.

1. **An exit the call site does not show.**
   Joel Spolsky wrote in 2003 that exceptions "*are invisible in the source code*" and "*create too many possible exit points for a function*".[^spolsky-exceptions]
2. **A signature that lies.**
   `function lend(...): Loan` says nothing about the three ways it can fail, so the compiler cannot check that every case is handled.
   `Result<Loan, LendRefusal>` says it in the type, and a `switch` over the refusal that forgets a case fails to compile.
3. **Time.**
   In Stephen Toub's benchmark, 1,000 throws, each caught through ten async frames, took 123.03 ms on .NET 8 and 54.68 ms on .NET 9.[^toub-net9]
   Microsoft's guidance for ASP.NET Core draws the rule: "*Throwing and catching exceptions is slow relative to other code flow patterns. Because of this, exceptions shouldn't be used to control normal program flow.*"[^aspnet-best-practices]
   The Framework Design Guidelines say "*DO NOT use exceptions for the normal flow of control, if possible.*"[^fdg-exception-throwing]
4. **A catch that hides bugs.**
   A catch wide enough to steer the flow also catches the bugs that happen inside it, and they vanish into a message nobody reads.

The refusal is the reason the rule matters most.
Most of what a program handles is a rule saying no, and a program that throws for that has an exit on every rule.

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
Two things bring the bug back to you: a test that runs every database call against a real, in-memory database and checks the value it gets (chapter 8), and a log line that prints the `message` before the program answers.

Two kinds of throw pass the boundary untouched.
A fatal one, such as running out of memory, is handled by no one.
A framework's own control flow, thrown on purpose, must not be caught by you: Next.js's `redirect` "*throws an error so it should be called **outside** the `try` block*",[^nextjs-redirect] and .NET unwinds a cancelled call by throwing, so that the call stack is "*unwound once a cancellation request is observed*".[^dotnet-exceptions]
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

## What the team gains

Every rule is a function a test calls with data, so a rule has a test before it has a screen, and an agent asked to change a rule finds it in one place, with its cases named in its type.
Every failure a caller must handle is in the signature, so a reviewer reads the type and knows what can go wrong, and the compiler refuses a forgotten case.
And the measured cost of steering by throw, twice the time on .NET 9 and more than four times on .NET 8 against a return,[^toub-net9] stays out of the hot path.

## Key points

* A pure function takes data and returns a value, with no I/O and no clock; a business rule written this way is tested with data alone.
* A failure is an exception (from outside, caught at the boundary and returned as a value), a refusal (a rule saying no, returned as a value) or an error (a bug, never caught); the class name tells none of them apart.
* A throw steers no flow: it is an exit the caller cannot see, a signature that lies, a measured cost, and a hiding place for bugs.
* The only `try`/`catch` lives where the program touches the outside world, and it translates the library's exception into the program's value; a new library changes that file alone.
* A `Result` handled with an exhaustive `Record`, `match` or `switch` fails to compile when a case is forgotten.

[^go-errors]: Rob Pike, "Errors are values", The Go Blog, 2015. <https://go.dev/blog/errors-are-values>
[^rust-result]: The Rust Programming Language, "Recoverable Errors with Result", chapter 9.2, accessed 2026-09-29. <https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html>
[^wlaschin-rop]: Scott Wlaschin, "Railway Oriented Programming", F# for Fun and Profit, 2014, accessed 2026-09-30. <https://fsharpforfunandprofit.com/rop/>
[^dart-core]: Dart, "Exception class" and "Error class", `dart:core` API reference, accessed 2026-09-29. <https://api.dart.dev/stable/dart-core/Exception-class.html> and <https://api.dart.dev/stable/dart-core/Error-class.html>
[^lippert-vexing]: Eric Lippert, "Vexing exceptions", Fabulous Adventures in Coding, 2008-09-10, accessed 2026-09-30. <https://ericlippert.com/2008/09/10/vexing-exceptions/>
[^spolsky-exceptions]: Joel Spolsky, "Exceptions", Joel on Software, 2003-10-13, accessed 2026-09-30. <https://www.joelonsoftware.com/2003/10/13/13/>
[^toub-net9]: Stephen Toub, "Performance Improvements in .NET 9", .NET Blog, 2024-09-12, section "VM", benchmark `ExceptionThrowCatch`, accessed 2026-09-30. <https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-9/>
[^aspnet-best-practices]: Microsoft Learn, "ASP.NET Core Best Practices", section "Minimize exceptions", accessed 2026-09-30. <https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices>
[^fdg-exception-throwing]: Krzysztof Cwalina and Brad Abrams, "Exception Throwing", Framework Design Guidelines, 2nd edition, 2008, on Microsoft Learn, accessed 2026-09-30. <https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/exception-throwing>
[^anti-corruption-layer]: Microsoft, "Anti-Corruption Layer pattern", Azure Architecture Center, accessed 2026-09-30. <https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer>
[^nextjs-redirect]: Next.js, "redirect", API reference, accessed 2026-09-30. <https://nextjs.org/docs/app/api-reference/functions/redirect>
[^dotnet-exceptions]: Microsoft Learn, "Best practices for exceptions", .NET, section "Catch cancellation and asynchronous exceptions", accessed 2026-09-30. <https://learn.microsoft.com/en-us/dotnet/standard/exceptions/best-practices-for-exceptions>
