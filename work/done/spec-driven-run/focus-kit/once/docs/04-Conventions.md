# Conventions

## Language
Documentation in English; identifiers in English.

## Naming (observed)
- Types in PascalCase (`Appointment`); functions and fields in camelCase (`book`, `clientName`, `startsAt`).
- A feature file is named after the feature, lowercase, singular: `src/appointment.ts`.
- Functions are verbs of docs/03: `book`.
- Status values are lowercase string literals: `"booked"`.

## Style
Observed: two-space indent, double quotes, semicolons, trailing commas in multi-line literals, `strict` TypeScript. No formatter or linter enforces it; the TypeScript compiler, once `verify` exists, is the only check.

## Tests
- Runner: `node --test` (`npm test`).
- Location: beside the feature, `src/<feature>.test.ts`. None exist yet; `verify` writes the first.
- Level: the module's exported functions, tested through their API. Each Behaviour line of a delivery page is one test. There is no screen, so there are no UI tests.

## Commits
As docs/05 §6. The existing history uses short imperative subjects ("Install", "Starting point").
