import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { isSuspended, registerMember, reinstateMember, suspendMember, type Member } from './member.ts';
import { createLibrarian } from './librarian.ts';

const librarian = { id: 'L1', name: 'Wren Halloway' };
const member: Member = { id: 'M1', name: 'Tobin Vale', email: 'tobin@example.org' };

describe('registerMember', () => {
  it('registers a member with a normalised email', () => {
    const result = registerMember({ id: 'M1', name: ' Tobin Vale ', email: ' Tobin@Example.org ' });
    assert.deepEqual(result, { ok: true, value: member });
  });

  it('requires a name', () => {
    assert.deepEqual(registerMember({ id: 'M1', name: '', email: 'a@b.c' }), { ok: false, error: 'name-required' });
  });

  it('rejects an invalid email', () => {
    assert.deepEqual(registerMember({ id: 'M1', name: 'A', email: 'not-an-email' }), {
      ok: false,
      error: 'invalid-email',
    });
  });

  it('a new member is not suspended', () => {
    assert.equal(isSuspended(member), false);
  });
});

describe('suspension', () => {
  it('suspends a member with a reason, date and librarian', () => {
    const result = suspendMember(member, librarian, 'lost three books', '2026-04-10');
    assert.ok(result.ok);
    assert.equal(isSuspended(result.value), true);
    assert.deepEqual(result.value.suspension, { reason: 'lost three books', since: '2026-04-10', by: 'L1' });
  });

  it('needs a reason', () => {
    assert.deepEqual(suspendMember(member, librarian, '  ', '2026-04-10'), { ok: false, error: 'reason-required' });
  });

  it('cannot suspend twice', () => {
    const once = suspendMember(member, librarian, 'r', '2026-04-10');
    assert.ok(once.ok);
    assert.deepEqual(suspendMember(once.value, librarian, 'r', '2026-04-11'), {
      ok: false,
      error: 'already-suspended',
    });
  });

  it('reinstating removes the suspension', () => {
    const suspended = suspendMember(member, librarian, 'r', '2026-04-10');
    assert.ok(suspended.ok);
    assert.deepEqual(reinstateMember(suspended.value), { ok: true, value: member });
  });

  it('cannot reinstate a member who is not suspended', () => {
    assert.deepEqual(reinstateMember(member), { ok: false, error: 'not-suspended' });
  });
});

describe('createLibrarian', () => {
  it('requires a name', () => {
    assert.deepEqual(createLibrarian({ id: 'L1', name: '' }), { ok: false, error: 'name-required' });
  });

  it('creates a librarian', () => {
    assert.deepEqual(createLibrarian({ id: 'L1', name: 'Wren Halloway' }), { ok: true, value: librarian });
  });
});
