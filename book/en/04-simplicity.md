# Simplicity is a decision: KISS, YAGNI, DRY

After this chapter you can refuse a piece of code, a document or a check that no delivery needs, and say which principle refuses it and who named it.
You can also tell the duplication that must go from the duplication that should stay, and know the moment a shared version is due: the second concrete occurrence.

## The problem

Software projects rarely die of one hard problem.
They die of many small things, each reasonable when it was added, that together make every change slow: a layer nobody needed, an option nobody used, a rule written in three places that now say three things.
Fred Brooks split the difficulty of software in two in 1987: the essential complexity, which belongs to the problem itself, and the accidental complexity, which the people building it add along the way.[^brooks-silver-bullet]
Nobody can remove the first.
The second is a choice, made one file at a time, and the three principles of this chapter are three ways to refuse it.

An agent makes the choice cheaper to get wrong.
It writes the layer, the option and the third copy in seconds, each one plausible, and each one is then code that someone must read, review and keep true.

## KISS: keep it simple

"Keep it simple, stupid" is credited to Kelly Johnson, the engineer who led Lockheed's Skunk Works, the team that designed the U-2 and the SR-71; the usual account ties it to aircraft that an ordinary mechanic had to repair in the field with ordinary tools.
The rule is about the person who comes next: the design must be simple enough for them, under pressure, without its author in the room.

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

Fowler counted, in 2015, what a presumptive feature costs, and it is four costs.[^fowler-yagni]

1. **Build.** The effort to analyze, program and test it, lost when it turns out nobody needs it.
2. **Delay.** The feature that has value now and waits while the presumptive one is built.
3. **Carry.** Its code "*adds some complexity to the software*", which makes every other feature harder to change and to debug, for as long as it stays.
4. **Repair.** When it is needed after all, the needs have moved, and it must be reworked before it fits.

Even the presumptive feature that turns out to be right pays delay and carry.
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

David Parnas gave the reason in 1972, before the name existed: decompose a system by "*a list of difficult design decisions or design decisions which are likely to change*", so that "*each module is then designed to hide such a decision from the others*".[^parnas-1972]
A decision hidden in one module changes in one module.
A decision copied into three modules changes in three, and one copy is always forgotten.

Sandi Metz named the opposite failure in 2016: "*duplication is far cheaper than the wrong abstraction*".[^metz-wrong-abstraction]
The wrong abstraction is the shared function that two callers used for different reasons; each new caller adds a parameter and a condition, until nobody can change it without breaking someone.
Her remedy is to put the code back into each caller and start again from what each one needs.
DRY and Metz agree: one place for each piece of knowledge, and a shared version only for what is the same knowledge.

## The discipline: abstraction on the second occurrence

The three principles meet in one rule, which this book's process writes into every project: an abstraction is written on the second concrete occurrence, and the delivery that writes it says which was the first.
One copy is no evidence that a shared version is needed: it is a guess, and YAGNI refuses guesses.
Two copies are the error that already happened, and DRY asks for one place.
Naming the first copy makes the move checkable: a reviewer opens both and sees that they are the same knowledge, which is Metz's test.

In the lending library, `Result`, the type that carries either a value or what stopped it (chapter 5), first appears inside the loans feature, as the return type of `lend` in `features/loans/rules.ts`.
It stays there while it has one user.
Then a delivery for members needs a rule that can refuse, and `Result` would be written a second time; that delivery moves it to `src/lib/result.ts`, the folder for code that belongs to no single feature (chapter 6), and says so:

```ts
// First use: features/loans/rules.ts (lend).
// Second use: features/members/rules.ts (register).
export type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };
```

`ok` and `err`, the two functions that build a `Result`, move with it, and both features import them from there.
Had the move come on the first use, it would have been a guess that happened to be right; on the second, it is a fact with two witnesses.

## The same three principles in a process

A process is code too: every document, every check and every step is something a person must read, and someone must keep true when the project moves.
The three principles apply to it unchanged.

* **KISS.** The fewest documents and steps that carry a delivery. A process a new member cannot follow after one reading will be followed by nobody.
* **YAGNI.** A check is a capability built for errors you presume will happen. A check that never catches a real error is a presumptive feature, and it pays build, delay and carry on every delivery that must satisfy it.
* **DRY.** Each fact of the project lives in one document. A decision written in the plan, in the spec, in the ADR and in the code is four places that will disagree, and the agent reads whichever it opens first.

A step enters the process when it names the concrete error it would have caught, and leaves when it names none.
Chapter 17, the governor, turns this into the question every step of the process must answer.

## What the team gains

Less to read, less to review and less to keep true.
Every file, option and check that is not written is one that no person reviews, no agent loads into a session, and no delivery has to satisfy.

On Ninjobs, my own product, I let complexity grow before its process changed.
A delivery had to pass 29 checks, and none of them had ever caught an error in the product: they were costly to satisfy and cheap to get around.[^ninjobs]
A decision lived in six places that could disagree: the documents, the specs, the changes, the ADRs, an outline and the code.[^ninjobs]
And because I required the full layered form of the architecture on every feature, trivial forms included, showing one field on a screen took eight files.[^ninjobs]
The architecture was not at fault; KISS and YAGNI were lost, one reasonable addition at a time.
The process that replaced it kept two checks, each tied to an error it catches, and one place per fact (chapter 9).

## Key points

* Accidental complexity is the part people add; it is a choice, and KISS, YAGNI and DRY are three ways to refuse it.
* KISS: the plainest form that does the job, simple enough for the person who comes next.
* YAGNI: a presumptive capability costs build, delay, carry and repair; it never argues against tests, clear names or other internal quality.
* DRY: one authoritative place for each piece of knowledge; identical lines may be different knowledge, and duplication is cheaper than the wrong abstraction.
* An abstraction is written on the second concrete occurrence, and the delivery says which was the first; in a process, a step enters only when it names the concrete error it would have caught.

[^brooks-silver-bullet]: Frederick P. Brooks Jr., "No Silver Bullet: Essence and Accidents of Software Engineering", IEEE Computer 20(4), 1987.
[^beck-xp]: Kent Beck, "Extreme Programming Explained: Embrace Change", Addison-Wesley, 1999.
[^fowler-yagni]: Martin Fowler, "Yagni", martinfowler.com, 2015-05-26, accessed 2026-09-30. <https://martinfowler.com/bliki/Yagni.html>
[^pragmatic-programmer]: Andrew Hunt and David Thomas, "The Pragmatic Programmer", Addison-Wesley, 1999; 20th anniversary edition, 2019.
[^parnas-1972]: D. L. Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules", Communications of the ACM 15(12), 1972. <https://doi.org/10.1145/361598.361623>
[^metz-wrong-abstraction]: Sandi Metz, "The Wrong Abstraction", 2016-01-20, accessed 2026-09-30. <https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction>
[^ninjobs]: Ninjobs, the author's product, a private repository, read by the author in its ADR-0022 of 2026-08-29, which ended its first process: the 29 checks that had never caught a product error, the six places where a decision could disagree, and the eight files to show one field are that ADR's own causes, paraphrased; the two checks kept in the process that replaced it are counted by the author.
