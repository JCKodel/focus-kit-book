# 5. A test for each piece

After this chapter you can say which test guards each of the four pieces and what it swaps, only the I/O and what changes between runs, and follow one rule through its tests.
You can also write a fake that fails the test when it is called unexpectedly, and name tests so that a reviewer reads them as the sentences of the rule.
You can keep the tests every delivery runs fast, and say where the slow ones run.
And you know why a test an agent wrote is trusted green only after it was seen red.

## The problem

The reason to have few tests used to be the cost of writing them, and an agent writes one in seconds, so that reason is gone.
The risk moved to the other side: an agent writes tests so easily that it writes too many, the same case five ways, until the suite takes minutes and nobody runs it before saying "done".
An agent also does not mind how long a test takes to run, and when every delivery runs the tests, one slow test makes every delivery wait.
I have seen agents write tests that took 20 minutes to run: 20 minutes on every delivery.
Ask of a test what chapter 3 asks of any step: which broken rule would it catch that no other test catches?

A test that needs the whole application running, a server up, a database seeded, a browser open, takes minutes to start too, and breaks for reasons that have nothing to do with the code it checks.
So it is skipped as well, and a rule that changed last week is found broken by a user.
The four pieces of [chapter 4](04-focus.md) are shaped so that each one can be tested alone, in the time it takes to save a file.

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

Keeping the tests in order, run time included, is your job; the agent will not do it unless you ask.
It is one more reason to keep a rule in a pure use case: its test is a call with data, the fastest test the project has.
End-to-end tests, and any test that needs the application or a network, are written only where they prove something the fast ones cannot.
What every delivery runs is the project's verify command, the command that must pass before a delivery is called done, and you decide what it runs.
A slow test can stay out of it and run in another command, which you run yourself, for example before a milestone closes.
A milestone is a group of deliveries with a paragraph saying what is true when it closes.

## What a fake is

Gerard Meszaros named the objects a test puts in place of real ones "test doubles", after the stunt double of a film, in his book *xUnit Test Patterns* (2007).[^meszaros]
In his names, an in-memory database, a working implementation that takes a shortcut, is a fake, and a repository that answers what the test sets is a stub.
This book calls both fakes, because both replace I/O with a second implementation that answers, and neither asserts how the code under test was written.

A mock does assert that: it checks the calls it was told to expect.
A test that expects `findMember` to be called once with `"m1"`, then `findCopy` with `"c1"`, repeats the orchestrator's code line by line, and fails when you reorder two calls that change nothing the user sees.
Martin Fowler describes this cost in the section "Coupling Tests to Implementations" of his article "Mocks Aren't Stubs".[^fowler-mocks]
A fake lets the test check what matters, the state that comes out, and leaves the code free to change inside.

## Swap only I/O and what changes between runs

The four pieces decide what a test may swap.
Only a repository does I/O, and only the orchestrator receives repositories, so the orchestrator's test swaps them and the repository's test swaps the database file.
Nothing else is swapped: a use case is never faked, because it is pure and fast, and a test that fakes it tests nothing.

The clock is I/O too: `new Date()` answers something different on every call.
In the lending library it is read once, where the request arrives, and passed on as a value, `today`, so a test passes `"2026-10-01"` and needs no fake clock at all.

A random value from `Math.random()`, a new id and a value read from the environment also answer differently from one run to the next, so each is I/O in the same sense.
Each is read once and handed on as a value, as `today` is, so the test passes the value it wants and needs no fake.
If `lend` gave each loan a new id with `crypto.randomUUID()`, its test could not say which loan it expects; the id is made where the request arrives, or by the database when it saves the loan.
A value from the environment, such as a variable, the time zone or the machine's language, is read once where the program starts, so a test does not answer differently on another machine.

There is nothing to swap in the order of a set.
A member's loans read with no `ORDER BY` come back in whatever order the database finds them, so a test that expects the order they were saved in can pass today and fail after the data or an index changes.
The query states the order it promises, or the test compares the loans without order.

A test whose answer depends on any of these passes today and fails tomorrow, or on another machine, on the same code, and then a red test no longer says that a rule broke.

## One rule through its tests

The rule: a member with an overdue book cannot borrow another.
It lives in the use case `lend` of [chapter 4](04-focus.md), and each piece it crosses has a test.

Kent Beck's test-driven development writes the test before the code, in a cycle of three steps: red, the test fails because the code does not exist yet; green, the smallest code that makes it pass; then clean up, with the test still green.[^beck-tdd]
A pure rule is the easiest place to do it, because its test is a call with data: run the first test below before `lend` exists and it is red, write `lend` and it is green.
The page of a delivery lists its behaviours, each one becomes a red test, and the delivery is done when every one of them is green and nothing that was green went red.

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

**The orchestrator.** `lendEvents.test.ts` passes fake repositories to `lendRequested`, the orchestrator of [chapter 4](04-focus.md):

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

## What tests prove, and what they do not

Red and green, the cycle of "One rule through its tests" above, are how an agent's test earns trust.
A test seen red before the code existed, and green after, has proven that it can fail.
A test written after the code, by the agent that wrote the code, may assert what the code does in place of what the rule says, and pass forever.

A green suite still does not prove that the software works.
A test can be wrong and pass.
Unit tests check each piece alone, and the sum of the pieces can fail where no piece does: a field the client sends under one name and the server reads under another passes every unit test on both sides.
That is the job of the few end-to-end tests, and the reason a delivery also carries a proof, the result seen working, before anyone calls it done.

## What the team gains

Every piece has a test that runs without the application, and each test catches a broken rule no other catches, so the suite runs in seconds and an agent runs it on every change, not only before it says "done".
An agent that changes `lend` learns from the name of the failing test which sentence of the rule it broke, before it runs the whole verify.
Because each test was seen red first, "done" is the test runner's output and not the agent's opinion.
And a reviewer checks a delivery by reading test names, which say, before any code, which cases the agent thought of and which it did not.

## Key points

* A use case is tested with data alone, a repository against an in-memory database with the real migrations, an orchestrator with fake repositories, and the view with a few end-to-end tests in a browser, so the run every delivery waits for stays fast.
* A test swaps only I/O and what changes between runs, which it passes in as a value, and expects an order only where the query fixes one, so most tests fake nothing but the repositories.
* A fake answers what the test sets and throws on any call the test did not expect; prefer it to a mock, which repeats the code it tests.
* Each level of test proves what the others do not, and a green suite still proves less than working software: a test can be wrong, and the pieces can fail together, so see a test red before trusting it green.
* A test's name is a sentence of the rule: a reviewer reads the names, and a rule with no sentence has no test.

[^vitest]: Vitest, "Getting Started", documentation, accessed 2026-09-29. <https://vitest.dev/guide/>
[^playwright]: Playwright, "Installation", documentation, accessed 2026-09-29. <https://playwright.dev/docs/intro>
[^vocke-pyramid]: Ham Vocke, "The Practical Test Pyramid", martinfowler.com, 2018. <https://martinfowler.com/articles/practical-test-pyramid.html>
[^meszaros]: Gerard Meszaros, "xUnit Test Patterns: Refactoring Test Code", Addison-Wesley, 2007.
[^fowler-mocks]: Martin Fowler, "Mocks Aren't Stubs", 2007. <https://martinfowler.com/articles/mocksArentStubs.html>
[^beck-tdd]: Kent Beck, "Test-Driven Development: By Example", Addison-Wesley, 2002.
[^cohn]: Mike Cohn, "Succeeding with Agile: Software Development Using Scrum", Addison-Wesley, 2009.
