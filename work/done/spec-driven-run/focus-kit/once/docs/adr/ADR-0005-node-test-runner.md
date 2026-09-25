# ADR-0005: Tests run with `node --test`

**2026-09-25 · observed, confirmed by the person.** Context: `npm test` already runs `node --test`, and Node runs TypeScript directly. Decision: tests use Node's built-in runner and `node:assert`, with no test framework. Consequences: no test dependency; tests live beside the feature as `src/<feature>.test.ts`; `verify` writes the first one.
