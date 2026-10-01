# 8. A test for each piece

After this chapter you can say which test guards each of the four pieces and what it swaps, only the I/O and the clock, and follow one rule through its tests.
You can also write a fake that fails the test when it is called unexpectedly, and name tests so that a reviewer reads them as the sentences of the rule.

## The problem

A test that needs the whole application running, a server up, a database seeded, a browser open, takes minutes to start and breaks for reasons that have nothing to do with the code it checks.
So nobody runs it before saying "done", and a rule that changed last week is found broken by a user.
The four pieces of [chapter 7](07-four-pieces.md) are shaped so that each one can be tested alone, in the time it takes to save a file.

## A test for each piece

A unit test calls one piece directly, in the test runner's process, with no server and no browser; it runs the real code that piece calls, except the I/O and the clock.
An end-to-end test drives the running application through its screen, as a user would, across the network to a real server and database.
In TypeScript, Vitest runs unit tests in Node,[^vitest] and Playwright drives a real browser for end-to-end tests.[^playwright]

| Piece | Its test | What it swaps |
|---|---|---|
| Use case | called with data; no setup | nothing: it has no I/O, and the date comes in as a value |
| Repository | against an in-memory database with the project's real migrations | the database file, for the same engine in memory |
| Orchestrator | with fake repositories that answer what the test sets and throw on any call the test did not expect | the repositories |
| View | an end-to-end test in a browser; a few, one per scenario the user sees | nothing |

Most tests are of the first three kinds, and they run in seconds.
End-to-end tests are few because each one is slow and fails for many reasons; Mike Cohn drew the shape as a pyramid, many unit tests at the base and few end-to-end tests at the top,[^cohn] and Ham Vocke's guide on Martin Fowler's site teaches it with code.[^vocke-pyramid]

## What a fake is

Gerard Meszaros named the objects a test puts in place of real ones "test doubles", after the stunt double of a film, in his book *xUnit Test Patterns* (2007).[^meszaros]
Martin Fowler summarized the kinds: a stub answers what the test set, a mock checks the calls it was told to expect, and a fake has a working implementation that takes a shortcut, such as an in-memory database.[^fowler-mocks]

In Meszaros's names, the in-memory database is a fake and a repository that answers what the test sets is a stub.
This book calls both fakes, because both replace I/O with a second implementation that answers, and neither asserts how the code under test was written.

A mock does assert that.
A test that expects `findMember` to be called once with `"m1"`, then `findCopy` with `"c1"`, repeats the orchestrator's code line by line, and fails when you reorder two calls that change nothing the user sees.
Fowler describes the same cost in the section "Coupling Tests to Implementations" of the same article.[^fowler-mocks]
A fake lets the test check what matters, the state that comes out, and leaves the code free to change inside.

## Swap only I/O and the clock

The four pieces decide what a test may swap.
Only a repository does I/O, and only the orchestrator receives repositories, so the orchestrator's test swaps them and the repository's test swaps the database file.
Nothing else is swapped: a use case is never faked, because it is pure and fast, and a test that fakes it tests nothing.

The clock is I/O too: `new Date()` answers something different on every call.
In the lending library it is read once, where the request arrives, and passed on as a value, `today`, so a test passes `"2026-10-01"` and needs no fake clock at all.

## One rule through its tests

The rule: a member with an overdue book cannot borrow another.
It lives in the use case `lend` of [chapter 5](05-rules-and-exceptions.md), and each piece it crosses has a test.

**The use case.** `rules.test.ts` calls `lend` with data:

```ts
describe("lend", () => {
	const copy = { id: "c1", bookId: "b1" };
	const member = { id: "m1", overdue: 0, suspended: false };

	it("refuses a member with an overdue book", () => {
		const result = lend(copy, { ...member, overdue: 1 }, "2026-10-01");
		expect(result).toEqual({ ok: false, error: "HasOverdueBooks" });
	});

	it("lends for 21 days to a member with nothing overdue", () => {
		const result = lend(copy, member, "2026-10-01");
		expect(result.ok && result.value.dueAt).toBe("2026-10-22");
	});
});
```

No database, no server, no mock: the member is an object, the date is a string, and the answer is a value.

**The repository.** `repository.server.test.ts` opens SQLite in memory, runs the same migration files the application runs, and calls `insertLoan` twice for the same copy.
The first returns the loan; the second returns the refusal `AlreadyLent`, because the unique index refused it.
It is the one part of lending that only the database can hold, since two librarians can press "Lend" at the same moment, and it is tested against the real engine and the real schema.

**The orchestrator.** `lendEvents.test.ts` passes fake repositories to `lendRequested`, the orchestrator of [chapter 7](07-four-pieces.md):

```ts
function unexpected(): never {
	throw new Error("not called in this test");
}

function fake(repositories: Partial<LoanRepositories>): LoanRepositories {
	const none = { findMember: unexpected, findCopy: unexpected, insertLoan: unexpected };
	return { ...none, ...repositories };
}

describe("lendRequested", () => {
	it("refuses a member with an overdue book and saves nothing", () => {
		const repositories = fake({
			findMember: () => ok({ id: "m1", overdue: 1, suspended: false }),
			findCopy: () => ok({ id: "c1", bookId: "b1" }),
		});
		const state = lendRequested({ copyId: "c1", memberId: "m1" }, "2026-10-01", repositories);
		expect(state).toEqual({ kind: "Refused", refusal: "HasOverdueBooks" });
	});
});
```

`fake` fills in only the repositories the test sets, and every other one throws.
This test sets no `insertLoan`, so if the orchestrator tried to save a loan for a member with an overdue book, the fake would throw and the test would fail.
It proves the refusal and that nothing was saved, and it asserts no order of calls.

**The view.** One end-to-end test, in a browser, opens the lending screen, lends a copy to a member who has an overdue book, and expects to read "Return your overdue books first."
It proves what none of the others can: that the message reaches the screen.

Each test proves something the others do not: the use case the rule, the repository the race, the orchestrator the flow, the view what the user sees.

## Test names are sentences

A test's name is what a reviewer reads first, so write it as a sentence of the rule:

* `lend refuses a member with an overdue book`
* `lend lends for 21 days to a member with nothing overdue`
* `insertLoan refuses a second open loan of the same copy`
* `lendRequested refuses a member with an overdue book and saves nothing`
* `the lending screen tells a member with an overdue book to return it first`

Read in a row, the names are the rules of lending, and a rule that has no sentence among them has no test.
Names like `test1` or `lend works` tell the reader nothing and hide the rule that is missing.
Kent Beck's *Test-Driven Development: By Example* (2002) writes the test before the code, so the test is the first statement of what the code must do; a name that reads as a sentence keeps it a statement a person can check.[^beck-tdd]

## What tests prove, and what they do not

For years the reason to have few tests was the cost of writing them.
An agent writes a test in seconds, so that reason is gone.
The risk moved to the other side: an agent writes tests so easily that it writes too many, the same case five ways, until the suite takes minutes and nobody runs it before saying "done".
Ask of a test what chapter 4 asks of any step: which broken rule would it catch that no other test catches?

Red and green are how an agent's test earns trust ([chapter 5](05-rules-and-exceptions.md) showed the cycle).
A test seen red before the code existed, and green after, has proven that it can fail.
A test written after the code, by the agent that wrote the code, may assert what the code does in place of what the rule says, and pass forever.

A green suite still does not prove that the software works.
A test can be wrong and pass.
Unit tests check each piece alone, and the sum of the pieces can fail where no piece does: a field the client sends under one name and the server reads under another passes every unit test on both sides.
That is the job of the few end-to-end tests, and the reason a delivery also carries a proof, the result seen working, before anyone calls it done ([chapter 15](15-apply.md)).

## What this gives an agent

An agent that changes `lend` runs the slice's unit tests and knows in seconds whether it broke the rule, before it runs the whole verify of [chapter 15](15-apply.md).
It does not have to start a server or open a browser to find out, so it runs the tests on every change, and a failing test tells it which sentence of the rule it broke.
When it adds a rule, the names of the tests it wrote tell you, before you read any code, which cases it thought of and which it did not.

## What the team gains

Every piece has a test that runs without the application, so an agent checks its own work before it says "done", and a reviewer checks a delivery by reading test names.
This book gives no baseline count of how much sooner a team catches a broken rule this way; the gain is that the check exists and runs in seconds.

## Key points

* A use case is tested with data alone, a repository against an in-memory database with the real migrations, an orchestrator with fake repositories, and the view with a few end-to-end tests in a browser.
* A test swaps only I/O and the clock, and the clock is a value passed in, so most tests fake nothing but the repositories.
* A fake answers what the test sets and throws on any call the test did not expect; prefer it to a mock, which repeats the code it tests.
* Each level of test proves what the others do not, and a green suite still proves less than working software: a test can be wrong, and the pieces can fail together, so see a test red before trusting it green, and keep the proof.
* A test's name is a sentence of the rule: a reviewer reads the names, and a rule with no sentence has no test.

[^vitest]: Vitest, "Getting Started", documentation, accessed 2026-09-29. <https://vitest.dev/guide/>
[^playwright]: Playwright, "Installation", documentation, accessed 2026-09-29. <https://playwright.dev/docs/intro>
[^vocke-pyramid]: Ham Vocke, "The Practical Test Pyramid", martinfowler.com, 2018. <https://martinfowler.com/articles/practical-test-pyramid.html>
[^meszaros]: Gerard Meszaros, "xUnit Test Patterns: Refactoring Test Code", Addison-Wesley, 2007.
[^fowler-mocks]: Martin Fowler, "Mocks Aren't Stubs", 2007. <https://martinfowler.com/articles/mocksArentStubs.html>
[^beck-tdd]: Kent Beck, "Test-Driven Development: By Example", Addison-Wesley, 2002.
[^cohn]: Mike Cohn, "Succeeding with Agile: Software Development Using Scrum", Addison-Wesley, 2009.
