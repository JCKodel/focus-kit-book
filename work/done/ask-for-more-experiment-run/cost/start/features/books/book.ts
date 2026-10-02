import { err, ok, type Result } from '../../shared/result.ts';
import type { Librarian } from '../members/librarian.ts';
import type { CalendarDate } from '../../shared/dates.ts';

export type Book = {
  readonly id: string;
  readonly title: string;
  readonly author: string;
  readonly isbn?: string;
};

export type CopyStatus = 'available' | 'on-loan' | 'withdrawn';

export type Copy = {
  readonly id: string;
  readonly bookId: string;
  readonly status: CopyStatus;
  readonly withdrawnBy?: string;
  readonly withdrawnOn?: CalendarDate;
};

export type BookError = 'title-required' | 'author-required' | 'invalid-isbn';
export type CopyError = 'copy-id-required' | 'copy-on-loan' | 'already-withdrawn';

export function createBook(input: {
  id: string;
  title: string;
  author: string;
  isbn?: string;
}): Result<Book, BookError> {
  const title = input.title.trim();
  const author = input.author.trim();
  if (title === '') return err('title-required');
  if (author === '') return err('author-required');
  if (input.isbn === undefined) return ok({ id: input.id, title, author });

  const isbn = input.isbn.replace(/[-\s]/g, '');
  if (!isValidIsbn13(isbn)) return err('invalid-isbn');
  return ok({ id: input.id, title, author, isbn });
}

// Only ISBN-13 is accepted. Hyphens and spaces are stripped before checking.
export function isValidIsbn13(isbn: string): boolean {
  if (!/^\d{13}$/.test(isbn)) return false;
  let sum = 0;
  for (let i = 0; i < 12; i++) {
    sum += Number(isbn[i]) * (i % 2 === 0 ? 1 : 3);
  }
  const check = (10 - (sum % 10)) % 10;
  return check === Number(isbn[12]);
}

export function addCopy(book: Book, copyId: string): Result<Copy, CopyError> {
  const id = copyId.trim();
  if (id === '') return err('copy-id-required');
  return ok({ id, bookId: book.id, status: 'available' });
}

export function withdrawCopy(
  copy: Copy,
  by: Librarian,
  on: CalendarDate,
): Result<Copy, CopyError> {
  if (copy.status === 'withdrawn') return err('already-withdrawn');
  if (copy.status === 'on-loan') return err('copy-on-loan');
  return ok({ ...copy, status: 'withdrawn', withdrawnBy: by.id, withdrawnOn: on });
}

export function availableCopies(copies: readonly Copy[], bookId: string): Copy[] {
  return copies.filter((c) => c.bookId === bookId && c.status === 'available');
}
