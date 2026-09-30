# ADR-0016: the book's definition of FOCUS

**Date:** 2026-09-28

## Context

The kit describes FOCUS in one paragraph and a table (focus-kit `SETUP.md` §Choices): four pieces, flow in one direction, a Result from every use case, the repository as the only place an infrastructure exception becomes a value.
Parts II and III need more than that, and one word needed fixing: the kit and the field say "errors as values", yet a bug is never a value.
On Ninjobs, FOCUS was required whole on every feature and showing one field took eight files (chapter 4); the architecture was not at fault, the way it was required was: KISS and YAGNI were lost.

## Decision

FOCUS, in this book, is four letters, each with its own value:

* **Feature-oriented.** Vertical slices, with no folder per technology or method (no `controllers/`): one folder holds everything a feature needs, and a sub-feature is a subfolder (`change-password` inside `authentication`).
* **Clean.** The layers of Clean Architecture, with one difference: a use case receives no repository. Use cases are pure, synchronous functions that validate, decide and format. The orchestrator is the only piece with injected dependencies, and those are the repositories: it receives an event, validates the input, asks repositories for data, applies the rules, formats the result, asks repositories to save, and returns a new state. It is BLoC in Flutter and the Mediator pattern in .NET. It asks for persistence; the repository persists. A repository may use a driver, such as a database engine or an ORM, rarely one written for the project.
* **Unidirectional.** Event, orchestration, use cases and repositories, new state: one direction, no binding, no state travelling back. "What happens when event X arrives?" is one test.
* **Scalable.** Every piece is isolated and testable, so the application holds at any size.

Exceptions and errors follow Dart's split (`Exception` and `Error` in `dart:core`): an exception is an expected failure the caller handles, an error is a program failure the programmer should have avoided. Exceptions exist only at I/O, so only repositories have `try`/`catch`, and they return every exception as a value, handled with an exhaustive switch or a union type. Errors are never caught: they reach the developer's screen and analytics, and they are the only thing that does. The book names the principle "exceptions as values" and says once that the field knows it as "errors as values".

Nothing exists for ceremony: a feature with no rule has no use case. DRY, YAGNI and KISS are non-negotiable, and they decide when a piece pays its way.

## Consequences

docs/03 holds every term above. Part III teaches FOCUS from this record; chapter 6 gives it in one paragraph. The kit's three answers (FOCUS whole, the two principles, neither) stand, the second now being vertical slices and exceptions as values. Chapter 14 is renamed accordingly.

## Amendment, 2026-09-29 (four-pieces-injection)

A piece receives a dependency only where there is a second implementation to pass, and in FOCUS that happens only in the orchestrator: the real repository, and the fake a test passes in its place. The server's orchestrator may receive the driver its repositories use, for the same reason: its test passes an in-memory database. A use case receives no repository, and a view or a repository has one implementation, so a parameter there would exist for ceremony. The clinic's client orchestrators, which now take their repositories as a parameter with the real ones by default, are the first case; chapter 15 teaches the rule from them.

## Amendment, 2026-09-30 (ch15-route-io)

The orchestrator receives its event, and on a server the event is the request, so reading the request body is part of receiving it: a body that cannot be read is answered `BadRequest` on the spot, as chapter 14 says. "Only repositories have `try`/`catch`" reads as: only the repository catches an exception from data, and startup code, such as opening the database or running migrations, catches where it does I/O outside the four pieces. Chapters 6 and 15 say it by role: the repository is the only piece that fetches and saves.

## Amendment, 2026-09-30 (ch15-injection-rule)

The criterion of the amendment `four-pieces-injection` stands: a piece receives a dependency only where its test passes a second implementation. Two of its claims do not: "in FOCUS that happens only in the orchestrator" and "a view or a repository has one implementation". A server repository receives the driver it uses, because its test passes an in-memory database. A client repository receives none, because no test passes a second implementation to it. A use case and a view receive none, and the clock is passed as data, a value, not a dependency. The Decision's "The orchestrator is the only piece with injected dependencies" and that amendment are read through this one and are not rewritten. Chapters 6 and 15 state the criterion.
