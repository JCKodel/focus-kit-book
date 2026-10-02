# Loan Service Design (draft)

**Author:** Rafe Lindqvist
**Date:** 2026-01-21
**Status:** Draft — for review at the next team sync

---

## 1. Purpose

How we will implement lending (checkout, return, renewal, overdue handling and fines) for the Hollowmere Lending Library, using the rules Odile gave at the 2026-01-12 kickoff: 14-day loans, max 3 loans per member, unlimited renewals, fines of 0.20 per day overdue.

The goal: a structure we can grow into without rework, separating outside-world code, rules, and storage.

## 2. Architecture overview

A classic three-layer structure:

```
src/
  controllers/
    LoanController.ts
    MemberController.ts
    BookController.ts
  services/
    LoanService.ts
    FineService.ts
    MemberService.ts
    errors.ts
  repositories/
    LoanRepository.ts
    MemberRepository.ts
    CopyRepository.ts
    inMemory/
  domain/
    Loan.ts
    Member.ts
    Copy.ts
test/
  services/
  repositories/
```

- **Controllers** are entry points (desk actions, later HTTP): they translate input and call services. No business logic.
- **Services** own all business rules, depending on repository *interfaces* injected through the constructor.
- **Repositories** hide storage. We ship only in-memory implementations for now, which the tests also use.
- **Domain** types are plain data shared by all layers.

Dependencies point downwards only: controllers → services → repositories. Every new piece of code has an obvious home.

## 3. Domain types

```ts
// src/domain/Loan.ts
export interface Loan {
  id: string;
  copyId: string;
  memberId: string;
  loanedAt: Date;
  dueAt: Date;
  renewals: number;
  returnedAt: Date | null;
}
```

```ts
// src/domain/Member.ts
export interface Member {
  id: string;
  name: string;
  email: string;
  suspended: boolean;
}
```

```ts
// src/domain/Copy.ts
export type CopyStatus = 'available' | 'on-loan';

export interface Copy {
  id: string;
  bookId: string;
  status: CopyStatus;
}
```

## 4. Dates and times

We use JavaScript `Date` objects throughout, with precise `loanedAt` and `dueAt` instants compared via `getTime()`.

- `dueAt` is checkout plus 14 days, **at 23:59 local time**. "Due on the 4th" means any time on the 4th.

```ts
// src/services/time.ts
export function dueDateFrom(loanedAt: Date, days: number): Date {
  const due = new Date(loanedAt);
  due.setDate(due.getDate() + days);
  due.setHours(23, 59, 0, 0);
  return due;
}
```

Real instants give exact event ordering (a return at 14:02 vs a renewal at 14:05) and let us later show members exact borrow times. A `Clock` lets tests control "now":

```ts
export interface Clock {
  now(): Date;
}
```

## 5. Errors

Rule violations throw typed errors; controllers catch them and turn them into desk messages. `src/services/errors.ts` defines a base `LoanError extends Error` and subclasses `MemberSuspendedError(memberId)`, `LoanLimitReachedError(memberId, limit)` and `CopyNotAvailableError(copyId)`, each with a message such as `Member ${memberId} is suspended`.

A controller can catch `LoanError` once for every lending problem, and still `instanceof`-check specific cases like `MemberSuspendedError` when the desk needs a different message.

## 6. Repositories

```ts
// src/repositories/LoanRepository.ts
export interface LoanRepository {
  findById(id: string): Promise<Loan | undefined>;
  findActiveByMember(memberId: string): Promise<Loan[]>;
  findActiveByCopy(copyId: string): Promise<Loan | undefined>;
  findOverdue(asOf: Date): Promise<Loan[]>;
  save(loan: Loan): Promise<void>;
}

export interface MemberRepository {
  findById(id: string): Promise<Member | undefined>;
  save(member: Member): Promise<void>;
}

export interface CopyRepository {
  findById(id: string): Promise<Copy | undefined>;
  save(copy: Copy): Promise<void>;
}
```

Everything is `async` from the start, so swapping in a real database later won't change service signatures.

## 7. LoanService

```ts
// src/services/LoanService.ts
export class LoanService {
  static readonly LOAN_PERIOD_DAYS = 14;
  static readonly MAX_ACTIVE_LOANS = 3;

  constructor(
    private readonly loans: LoanRepository,
    private readonly members: MemberRepository,
    private readonly copies: CopyRepository,
    private readonly clock: Clock,
    private readonly fines: FineService,
    private readonly ids: () => string,
  ) {}

  async checkOut(memberId: string, copyId: string): Promise<Loan> {
    const member = await this.requireMember(memberId);
    if (member.suspended) throw new MemberSuspendedError(memberId);

    const active = await this.loans.findActiveByMember(memberId);
    if (active.length >= LoanService.MAX_ACTIVE_LOANS) {
      throw new LoanLimitReachedError(memberId, LoanService.MAX_ACTIVE_LOANS);
    }

    const copy = await this.requireCopy(copyId);
    if (copy.status !== 'available') throw new CopyNotAvailableError(copyId);

    const now = this.clock.now();
    const loan: Loan = {
      id: this.ids(),
      copyId,
      memberId,
      loanedAt: now,
      dueAt: dueDateFrom(now, LoanService.LOAN_PERIOD_DAYS),
      renewals: 0,
      returnedAt: null,
    };
    await this.loans.save(loan);
    await this.copies.save({ ...copy, status: 'on-loan' });
    return loan;
  }

  async returnCopy(loanId: string): Promise<{ loan: Loan; fine: number }> {
    const loan = await this.requireLoan(loanId);
    if (loan.returnedAt) throw new LoanError(`Loan ${loanId} already returned`);

    const now = this.clock.now();
    const fine = this.fines.amountFor(loan, now);
    const returned = { ...loan, returnedAt: now };
    await this.loans.save(returned);
    const copy = await this.requireCopy(loan.copyId);
    await this.copies.save({ ...copy, status: 'available' });
    return { loan: returned, fine };
  }

  async renew(loanId: string): Promise<Loan> {
    const loan = await this.requireLoan(loanId);
    if (loan.returnedAt) throw new LoanError(`Loan ${loanId} already returned`);
    const member = await this.requireMember(loan.memberId);
    if (member.suspended) throw new MemberSuspendedError(member.id);

    const renewed = { ...loan, dueAt: this.nextDueDate(loan), renewals: loan.renewals + 1 };
    await this.loans.save(renewed);
    return renewed;
  }

  // requireMember / requireCopy / requireLoan throw LoanError when not found
}
```

- Renewals are unlimited, per Odile; we still count them for reporting.
- Suspended members cannot check out or renew. Returning is never blocked.
- `MemberService` handles suspension; the loan service only reads the flag.

## 8. Fines

Fines accrue **per day** overdue at 0.20 per item. `FineService` computes them on the fly from the loan and the return moment rather than storing a running total, so a rate change only affects future calculations.

```ts
// src/services/FineService.ts
export class FineService {
  static readonly DAILY_RATE = 0.2;
  private static readonly MS_PER_DAY = 24 * 60 * 60 * 1000;

  daysOverdue(loan: Loan, at: Date): number {
    const late = at.getTime() - loan.dueAt.getTime();
    if (late <= 0) return 0;
    return Math.ceil(late / FineService.MS_PER_DAY);
  }

  amountFor(loan: Loan, at: Date): number {
    const days = this.daysOverdue(loan, at);
    return Math.round(days * FineService.DAILY_RATE * 100) / 100;
  }
}
```

The rate moves into configuration, as Juno asked, once the council confirms it. Amounts are rounded to two decimals only at the end. A later nightly job can call `loans.findOverdue(now)` for a "fines owed" desk report.

## 9. Controllers

Thin: each desk action parses input, calls a service, and maps the outcome, with error mapping in one place. `LoanController.checkOut` returns `{ status: 'ok', message: 'Due back <date>' }` on success and `{ status: 'refused', message: e.message }` for a `LoanError`; anything else is a genuine bug and propagates.

## 10. Wiring

`createApp()` builds the in-memory repositories, system clock, services and controllers. Tests use it with a fake clock, so every test run exercises the wiring. No DI container; hand-written constructor injection is enough at this size.

## 11. Testing

- One `node:test`/`node:assert` file per service under `test/services/`, with in-memory repositories and a fake `Clock`.
- A thin smoke test per controller.
- Repository tests check the in-memory implementations behave like a real store (e.g. `findActiveByMember` excludes returned loans).

```ts
test('checkout fails when member already has 3 loans', async () => {
  const svc = makeService({ now: new Date('2026-02-02T10:00:00') });
  for (const c of ['c1', 'c2', 'c3']) await svc.checkOut('m1', c);
  await assert.rejects(() => svc.checkOut('m1', 'c4'), LoanLimitReachedError);
});
```

## 12. Rollout plan

1. Domain types + in-memory repositories (this week)
2. `LoanService.checkOut` / `returnCopy` with tests
3. `FineService` with tests
4. `renew`, then `MemberService` suspension
5. Controllers once Juno has agreed what the desk actions look like

## 13. Open points

- Exact suspension rule — waiting on the session with Wren (26 Jan).
- Lost/damaged copies — `CopyStatus` will grow once we know.
- Where fines get paid and recorded — probably a `Payment` entity later.
