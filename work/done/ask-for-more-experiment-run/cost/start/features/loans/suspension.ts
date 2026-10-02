import { err, type Result } from '../../shared/result.ts';
import type { CalendarDate } from '../../shared/dates.ts';
import {
  isSuspended,
  reinstateMember,
  suspendMember,
  type Member,
  type MemberError,
} from '../members/member.ts';
import type { Librarian } from '../members/librarian.ts';
import { activeLoansOf, daysOverdue, isOverdue, type Loan } from './loan.ts';

// A member is suspended once any of their loans is more than this many days
// overdue.
export const SUSPEND_AFTER_DAYS_OVERDUE = 14;

export type SuspensionError = MemberError | 'still-has-overdue-loans';

export function shouldBeSuspended(member: Member, loans: readonly Loan[], today: CalendarDate): boolean {
  return (
    !isSuspended(member) &&
    activeLoansOf(loans, member.id).some((l) => daysOverdue(l, today) > SUSPEND_AFTER_DAYS_OVERDUE)
  );
}

// Suspends every member who should be suspended. Members that are already
// suspended, or have nothing seriously overdue, are returned unchanged.
export function applySuspensions(
  members: readonly Member[],
  loans: readonly Loan[],
  by: Librarian,
  today: CalendarDate,
): Member[] {
  return members.map((member) => {
    if (!shouldBeSuspended(member, loans, today)) return member;
    const result = suspendMember(
      member,
      by,
      `loan more than ${SUSPEND_AFTER_DAYS_OVERDUE} days overdue`,
      today,
    );
    return result.ok ? result.value : member;
  });
}

// Any librarian can lift a suspension, but only once the member has returned
// everything that is overdue.
export function liftSuspension(
  member: Member,
  loans: readonly Loan[],
  today: CalendarDate,
): Result<Member, SuspensionError> {
  if (activeLoansOf(loans, member.id).some((l) => isOverdue(l, today))) {
    return err('still-has-overdue-loans');
  }
  return reinstateMember(member);
}
