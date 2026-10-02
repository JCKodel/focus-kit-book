import { err, ok, type Result } from '../../shared/result.ts';

// Librarians are staff. They are not members and cannot borrow through this
// model; they issue loans, withdraw copies and suspend or reinstate members.
export type Librarian = {
  readonly id: string;
  readonly name: string;
};

export type LibrarianError = 'name-required';

export function createLibrarian(input: { id: string; name: string }): Result<Librarian, LibrarianError> {
  const name = input.name.trim();
  if (name === '') return err('name-required');
  return ok({ id: input.id, name });
}
