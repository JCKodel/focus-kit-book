import { err, ok, type Result } from '../../shared/result.ts';
import type { CalendarDate } from '../../shared/dates.ts';
import type { Librarian } from './librarian.ts';

export type Suspension = {
  readonly reason: string;
  readonly since: CalendarDate;
  readonly by: string;
};

export type Member = {
  readonly id: string;
  readonly name: string;
  readonly email: string;
  readonly suspension?: Suspension;
};

export type MemberError =
  | 'name-required'
  | 'invalid-email'
  | 'reason-required'
  | 'already-suspended'
  | 'not-suspended';

const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export function registerMember(input: { id: string; name: string; email: string }): Result<Member, MemberError> {
  const name = input.name.trim();
  const email = input.email.trim().toLowerCase();
  if (name === '') return err('name-required');
  if (!EMAIL.test(email)) return err('invalid-email');
  return ok({ id: input.id, name, email });
}

export function isSuspended(member: Member): boolean {
  return member.suspension !== undefined;
}

export function suspendMember(
  member: Member,
  by: Librarian,
  reason: string,
  on: CalendarDate,
): Result<Member, MemberError> {
  if (isSuspended(member)) return err('already-suspended');
  if (reason.trim() === '') return err('reason-required');
  return ok({ ...member, suspension: { reason: reason.trim(), since: on, by: by.id } });
}

// Lifts a suspension. Whether the member is allowed to be reinstated (no
// overdue loans left) is a loans concern; see features/loans/suspension.ts.
export function reinstateMember(member: Member): Result<Member, MemberError> {
  if (!isSuspended(member)) return err('not-suspended');
  const { suspension: _, ...rest } = member;
  return ok(rest);
}
