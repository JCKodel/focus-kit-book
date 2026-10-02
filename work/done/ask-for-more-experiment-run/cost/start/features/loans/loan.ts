import { err, ok, type Result } from '../../shared/result.ts';
import { addDays, daysBetween, type CalendarDate } from '../../shared/dates.ts';
import type { Copy } from '../books/book.ts';
import { isSuspended, type Member } from '../members/member.ts';
import type { Librarian } from '../members/librarian.ts';

export const LOAN_PERIOD_DAYS = 21;
export const MAX_ACTIVE_LOANS = 5;
export const MAX_RENEWALS = 2;

export type Loan = {
  readonly id: string;
  readonly copyId: string;
  readonly memberId: string;
  readonly issuedBy: string;
  readonly loanedOn: CalendarDate;
  readonly dueOn: CalendarDate;
  readonly renewals: number;
  readonly returnedOn?: CalendarDate;
};

export type LoanError =
  | 'member-suspended'
  | 'member-has-overdue-loans'
  | 'loan-limit-reached'
  | 'copy-withdrawn'
  | 'copy-not-available'
  | 'copy-mismatch'
  | 'already-returned'
  | 'loan-overdue'
  | 'renewal-limit-reached';

export function isActive(loan: Loan): boolean {
  return loan.returnedOn === undefined;
}

// A loan is overdue from the day after its due date. On the due date itself
// it is not overdue.
export function isOverdue(loan: Loan, today: CalendarDate): boolean {
  return isActive(loan) && daysBetween(loan.dueOn, today) > 0;
}

export function daysOverdue(loan: Loan, today: CalendarDate): number {
  return isOverdue(loan, today) ? daysBetween(loan.dueOn, today) : 0;
}

export function overdueLoans(loans: readonly Loan[], today: CalendarDate): Loan[] {
  return loans.filter((l) => isOverdue(l, today));
}

export function activeLoansOf(loans: readonly Loan[], memberId: string): Loan[] {
  return loans.filter((l) => l.memberId === memberId && isActive(l));
}

export function checkOut(input: {
  loanId: string;
  member: Member;
  copy: Copy;
  librarian: Librarian;
  loans: readonly Loan[];
  today: CalendarDate;
}): Result<{ loan: Loan; copy: Copy }, LoanError> {
  const { member, copy, today } = input;
  if (isSuspended(member)) return err('member-suspended');

  const memberLoans = activeLoansOf(input.loans, member.id);
  if (memberLoans.some((l) => isOverdue(l, today))) return err('member-has-overdue-loans');
  if (memberLoans.length >= MAX_ACTIVE_LOANS) return err('loan-limit-reached');

  if (copy.status === 'withdrawn') return err('copy-withdrawn');
  if (copy.status === 'on-loan') return err('copy-not-available');

  const loan: Loan = {
    id: input.loanId,
    copyId: copy.id,
    memberId: member.id,
    issuedBy: input.librarian.id,
    loanedOn: today,
    dueOn: addDays(today, LOAN_PERIOD_DAYS),
    renewals: 0,
  };
  return ok({ loan, copy: { ...copy, status: 'on-loan' } });
}

// Returning is always allowed, also for suspended members and overdue loans.
export function returnCopy(input: {
  loan: Loan;
  copy: Copy;
  today: CalendarDate;
}): Result<{ loan: Loan; copy: Copy }, LoanError> {
  const { loan, copy, today } = input;
  if (!isActive(loan)) return err('already-returned');
  if (loan.copyId !== copy.id) return err('copy-mismatch');
  return ok({
    loan: { ...loan, returnedOn: today },
    copy: { ...copy, status: 'available' },
  });
}

// A renewal adds a full loan period to the current due date, not to today.
export function renewLoan(input: {
  loan: Loan;
  member: Member;
  today: CalendarDate;
}): Result<Loan, LoanError> {
  const { loan, member, today } = input;
  if (!isActive(loan)) return err('already-returned');
  if (isSuspended(member)) return err('member-suspended');
  if (isOverdue(loan, today)) return err('loan-overdue');
  if (loan.renewals >= MAX_RENEWALS) return err('renewal-limit-reached');
  return ok({
    ...loan,
    dueOn: addDays(loan.dueOn, LOAN_PERIOD_DAYS),
    renewals: loan.renewals + 1,
  });
}
