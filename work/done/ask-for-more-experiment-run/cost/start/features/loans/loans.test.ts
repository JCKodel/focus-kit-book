import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import {
  checkOut,
  daysOverdue,
  isOverdue,
  LOAN_PERIOD_DAYS,
  MAX_ACTIVE_LOANS,
  MAX_RENEWALS,
  overdueLoans,
  renewLoan,
  returnCopy,
  type Loan,
} from './loan.ts';
import { applySuspensions, liftSuspension, shouldBeSuspended, SUSPEND_AFTER_DAYS_OVERDUE } from './suspension.ts';
import { addDays } from '../../shared/dates.ts';
import type { Copy } from '../books/book.ts';
import type { Member } from '../members/member.ts';
import type { Librarian } from '../members/librarian.ts';

const librarian: Librarian = { id: 'L1', name: 'Wren Halloway' };
const member: Member = { id: 'M1', name: 'Tobin Vale', email: 'tobin@example.org' };
const suspended: Member = { ...member, suspension: { reason: 'r', since: '2026-01-01', by: 'L1' } };
const copy: Copy = { id: 'C-1', bookId: 'B1', status: 'available' };

function loan(overrides: Partial<Loan> = {}): Loan {
  return {
    id: 'LN1',
    copyId: 'C-1',
    memberId: 'M1',
    issuedBy: 'L1',
    loanedOn: '2026-03-01',
    dueOn: '2026-03-22',
    renewals: 0,
    ...overrides,
  };
}

function checkOutFor(m: Member, c: Copy, loans: Loan[] = [], today = '2026-03-01') {
  return checkOut({ loanId: 'LN9', member: m, copy: c, librarian, loans, today });
}

describe('checkOut', () => {
  it('lends a copy for the loan period and marks it on loan', () => {
    const result = checkOutFor(member, copy);
    assert.ok(result.ok);
    assert.equal(LOAN_PERIOD_DAYS, 21);
    assert.deepEqual(result.value.loan, {
      id: 'LN9',
      copyId: 'C-1',
      memberId: 'M1',
      issuedBy: 'L1',
      loanedOn: '2026-03-01',
      dueOn: '2026-03-22',
      renewals: 0,
    });
    assert.equal(result.value.copy.status, 'on-loan');
  });

  it('computes due dates across month and year ends', () => {
    const result = checkOutFor(member, copy, [], '2026-12-20');
    assert.ok(result.ok);
    assert.equal(result.value.loan.dueOn, '2027-01-10');
  });

  it('refuses a suspended member', () => {
    assert.deepEqual(checkOutFor(suspended, copy), { ok: false, error: 'member-suspended' });
  });

  it('refuses a member who has an overdue loan, even before suspension', () => {
    const late = loan({ id: 'LN0', copyId: 'C-0', dueOn: '2026-02-27' });
    assert.deepEqual(checkOutFor(member, copy, [late]), { ok: false, error: 'member-has-overdue-loans' });
  });

  it('refuses when the member has reached the loan limit', () => {
    const loans = Array.from({ length: MAX_ACTIVE_LOANS }, (_, i) =>
      loan({ id: `LN${i}`, copyId: `C-${i + 10}`, dueOn: '2026-03-15' }),
    );
    assert.deepEqual(checkOutFor(member, copy, loans), { ok: false, error: 'loan-limit-reached' });
  });

  it('returned loans do not count towards the limit', () => {
    const loans = Array.from({ length: MAX_ACTIVE_LOANS }, (_, i) =>
      loan({ id: `LN${i}`, copyId: `C-${i + 10}`, returnedOn: '2026-02-20' }),
    );
    assert.ok(checkOutFor(member, copy, loans).ok);
  });

  it('other members’ loans do not count towards the limit', () => {
    const loans = Array.from({ length: MAX_ACTIVE_LOANS }, (_, i) =>
      loan({ id: `LN${i}`, memberId: 'M2', copyId: `C-${i + 10}` }),
    );
    assert.ok(checkOutFor(member, copy, loans).ok);
  });

  it('refuses a copy that is already on loan', () => {
    assert.deepEqual(checkOutFor(member, { ...copy, status: 'on-loan' }), { ok: false, error: 'copy-not-available' });
  });

  it('refuses a withdrawn copy', () => {
    assert.deepEqual(checkOutFor(member, { ...copy, status: 'withdrawn' }), { ok: false, error: 'copy-withdrawn' });
  });
});

describe('overdue', () => {
  it('is not overdue on the due date', () => {
    assert.equal(isOverdue(loan(), '2026-03-22'), false);
  });

  it('is overdue the day after the due date', () => {
    assert.equal(isOverdue(loan(), '2026-03-23'), true);
    assert.equal(daysOverdue(loan(), '2026-03-23'), 1);
  });

  it('a returned loan is never overdue', () => {
    assert.equal(isOverdue(loan({ returnedOn: '2026-03-30' }), '2026-04-10'), false);
    assert.equal(daysOverdue(loan({ returnedOn: '2026-03-30' }), '2026-04-10'), 0);
  });

  it('lists overdue loans', () => {
    const loans = [loan({ id: 'a' }), loan({ id: 'b', dueOn: '2026-04-30' }), loan({ id: 'c', returnedOn: '2026-03-02' })];
    assert.deepEqual(overdueLoans(loans, '2026-04-01').map((l) => l.id), ['a']);
  });
});

describe('returnCopy', () => {
  const onLoan: Copy = { ...copy, status: 'on-loan' };

  it('closes the loan and makes the copy available', () => {
    const result = returnCopy({ loan: loan(), copy: onLoan, today: '2026-03-10' });
    assert.ok(result.ok);
    assert.equal(result.value.loan.returnedOn, '2026-03-10');
    assert.equal(result.value.copy.status, 'available');
  });

  it('accepts overdue returns', () => {
    assert.ok(returnCopy({ loan: loan(), copy: onLoan, today: '2026-05-01' }).ok);
  });

  it('cannot return twice', () => {
    assert.deepEqual(returnCopy({ loan: loan({ returnedOn: '2026-03-10' }), copy: onLoan, today: '2026-03-11' }), {
      ok: false,
      error: 'already-returned',
    });
  });

  it('the copy must match the loan', () => {
    assert.deepEqual(returnCopy({ loan: loan(), copy: { ...onLoan, id: 'C-2' }, today: '2026-03-10' }), {
      ok: false,
      error: 'copy-mismatch',
    });
  });
});

describe('renewLoan', () => {
  it('extends from the current due date, not from today', () => {
    const result = renewLoan({ loan: loan(), member, today: '2026-03-05' });
    assert.ok(result.ok);
    assert.equal(result.value.dueOn, addDays('2026-03-22', LOAN_PERIOD_DAYS));
    assert.equal(result.value.renewals, 1);
  });

  it('can renew on the due date', () => {
    assert.ok(renewLoan({ loan: loan(), member, today: '2026-03-22' }).ok);
  });

  it('cannot renew an overdue loan', () => {
    assert.deepEqual(renewLoan({ loan: loan(), member, today: '2026-03-23' }), { ok: false, error: 'loan-overdue' });
  });

  it('stops at the renewal limit', () => {
    assert.deepEqual(renewLoan({ loan: loan({ renewals: MAX_RENEWALS }), member, today: '2026-03-05' }), {
      ok: false,
      error: 'renewal-limit-reached',
    });
  });

  it('a suspended member cannot renew', () => {
    assert.deepEqual(renewLoan({ loan: loan(), member: suspended, today: '2026-03-05' }), {
      ok: false,
      error: 'member-suspended',
    });
  });

  it('cannot renew a returned loan', () => {
    assert.deepEqual(renewLoan({ loan: loan({ returnedOn: '2026-03-04' }), member, today: '2026-03-05' }), {
      ok: false,
      error: 'already-returned',
    });
  });
});

describe('suspension of members', () => {
  const due = '2026-03-22';
  const atThreshold = addDays(due, SUSPEND_AFTER_DAYS_OVERDUE);
  const pastThreshold = addDays(due, SUSPEND_AFTER_DAYS_OVERDUE + 1);

  it('is not due at exactly the threshold', () => {
    assert.equal(shouldBeSuspended(member, [loan()], atThreshold), false);
  });

  it('is due one day past the threshold', () => {
    assert.equal(shouldBeSuspended(member, [loan()], pastThreshold), true);
  });

  it('applySuspensions suspends only the members who should be', () => {
    const other: Member = { id: 'M2', name: 'Esra Quill', email: 'esra@example.org' };
    const [m1, m2] = applySuspensions([member, other], [loan()], librarian, pastThreshold);
    assert.ok(m1.suspension);
    assert.equal(m1.suspension.since, pastThreshold);
    assert.equal(m1.suspension.by, 'L1');
    assert.equal(m2, other);
  });

  it('cannot lift a suspension while loans are overdue', () => {
    assert.deepEqual(liftSuspension(suspended, [loan()], '2026-04-30'), {
      ok: false,
      error: 'still-has-overdue-loans',
    });
  });

  it('lifts a suspension once overdue loans are returned', () => {
    const result = liftSuspension(suspended, [loan({ returnedOn: '2026-04-29' })], '2026-04-30');
    assert.deepEqual(result, { ok: true, value: member });
  });
});
