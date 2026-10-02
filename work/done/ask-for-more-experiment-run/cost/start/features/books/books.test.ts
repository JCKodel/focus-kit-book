import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { addCopy, availableCopies, createBook, isValidIsbn13, withdrawCopy, type Book, type Copy } from './book.ts';
import type { Librarian } from '../members/librarian.ts';

const librarian: Librarian = { id: 'L1', name: 'Wren Halloway' };

function book(): Book {
  const result = createBook({ id: 'B1', title: 'The Salt Orchard', author: 'Ines Corvald' });
  assert.ok(result.ok);
  return result.value;
}

describe('createBook', () => {
  it('creates a book with trimmed title and author', () => {
    const result = createBook({ id: 'B1', title: '  The Salt Orchard ', author: ' Ines Corvald' });
    assert.deepEqual(result, { ok: true, value: { id: 'B1', title: 'The Salt Orchard', author: 'Ines Corvald' } });
  });

  it('requires a title', () => {
    assert.deepEqual(createBook({ id: 'B1', title: ' ', author: 'X' }), { ok: false, error: 'title-required' });
  });

  it('requires an author', () => {
    assert.deepEqual(createBook({ id: 'B1', title: 'X', author: '' }), { ok: false, error: 'author-required' });
  });

  it('accepts a valid ISBN-13 with hyphens and stores it without them', () => {
    const result = createBook({ id: 'B1', title: 'X', author: 'Y', isbn: '978-1-234-56789-7' });
    assert.ok(result.ok);
    assert.equal(result.value.isbn, '9781234567897');
  });

  it('rejects an ISBN with a wrong check digit', () => {
    assert.deepEqual(createBook({ id: 'B1', title: 'X', author: 'Y', isbn: '9781234567890' }), {
      ok: false,
      error: 'invalid-isbn',
    });
  });

  it('rejects ISBN-10', () => {
    assert.equal(isValidIsbn13('0306406152'), false);
  });
});

describe('copies', () => {
  it('a new copy is available', () => {
    const result = addCopy(book(), 'C-0001');
    assert.deepEqual(result, { ok: true, value: { id: 'C-0001', bookId: 'B1', status: 'available' } });
  });

  it('a copy needs an id', () => {
    assert.deepEqual(addCopy(book(), '  '), { ok: false, error: 'copy-id-required' });
  });

  it('withdraws an available copy and records who did it', () => {
    const copy: Copy = { id: 'C-0001', bookId: 'B1', status: 'available' };
    const result = withdrawCopy(copy, librarian, '2026-03-01');
    assert.ok(result.ok);
    assert.equal(result.value.status, 'withdrawn');
    assert.equal(result.value.withdrawnBy, 'L1');
    assert.equal(result.value.withdrawnOn, '2026-03-01');
  });

  it('cannot withdraw a copy that is on loan', () => {
    const copy: Copy = { id: 'C-0001', bookId: 'B1', status: 'on-loan' };
    assert.deepEqual(withdrawCopy(copy, librarian, '2026-03-01'), { ok: false, error: 'copy-on-loan' });
  });

  it('cannot withdraw a copy twice', () => {
    const copy: Copy = { id: 'C-0001', bookId: 'B1', status: 'withdrawn' };
    assert.deepEqual(withdrawCopy(copy, librarian, '2026-03-01'), { ok: false, error: 'already-withdrawn' });
  });

  it('lists only available copies of the given book', () => {
    const copies: Copy[] = [
      { id: 'C-1', bookId: 'B1', status: 'available' },
      { id: 'C-2', bookId: 'B1', status: 'on-loan' },
      { id: 'C-3', bookId: 'B1', status: 'withdrawn' },
      { id: 'C-4', bookId: 'B2', status: 'available' },
    ];
    assert.deepEqual(availableCopies(copies, 'B1').map((c) => c.id), ['C-1']);
  });
});
