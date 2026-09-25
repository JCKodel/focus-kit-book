# Research: Client Appointment Cancellation

**Feature**: [spec.md](./spec.md) | **Plan**: [plan.md](./plan.md) | **Date**: 2026-09-25

The planning input fixed most of the technical context: storage is in memory, the feature is a
function in the module (no screen), the client is identified by `clientName` with no login, times
are the clinic's local time, tests use `node --test`, and no notification is sent. The items below
settle what was still open.

## R1. Running TypeScript tests with `node --test`

- **Decision**: Put the tests in `src/appointment.test.ts` and run them directly with `node --test`.
  Node 26 strips TypeScript types natively, and its default test file patterns include
  `**/*.test.ts`. Relative imports use the `.ts` extension (`./appointment.ts`). Add
  `"rewriteRelativeImportExtensions": true` and `"erasableSyntaxOnly": true` to `tsconfig.json` so
  `tsc` accepts those imports and rejects syntax Node can't strip (such as `enum`).
- **Rationale**: No build step and no test framework. `npm test` stays `node --test` exactly as the
  constitution requires. Because the test file is under `src/`, the existing `"include": ["src"]`
  type-checks it too (Principle II).
- **Alternatives considered**:
  - Compile with `tsc` to `dist/` and then test the JS. This adds a build step before every test
    run and makes stale output possible.
  - Use `tsx` or `ts-node` as a loader. That's a new runtime dependency Node no longer needs
    (Principle I).
  - Put tests in a separate `tests/` directory. Then `tsconfig.json` `include` would have to
    widen, with no benefit for a single module.

## R2. Type-checking the test file

- **Decision**: Add `@types/node` as a devDependency and set `"types": ["node"]` in
  `tsconfig.json`. Add an npm script `"typecheck": "tsc --noEmit"`.
- **Rationale**: The test file imports `node:test` and `node:assert/strict`. Without Node's type
  declarations, `tsc` fails, and the merge gate requires zero type errors. Recent TypeScript
  versions don't load `@types/*` automatically unless `types` lists them, so the entry is explicit.
- **Alternatives considered**: Leave test files out of type-checking. That breaks Principle II
  ("all source code MUST be TypeScript with strict"). This is the only new dependency, and it is
  type declarations only.

## R3. Measuring "24 hours before" in clinic local time

- **Decision**: A cancellation is allowed when `startsAt.getTime() - now.getTime() >= 86_400_000`
  (24 × 60 × 60 × 1000 ms). The comparison is between instants. Both `Date`s are created from the
  clinic's local time, meaning the process runs with the clinic's time zone. No time zone
  conversion happens in the module.
- **Rationale**: The spec asks for "at least 24 hours remain", which is elapsed time. Comparing
  instants is exact at the boundary (exactly 24 h passes, 1 ms less fails) and involves no time
  zone arithmetic. On the two daylight-saving nights a year, "24 elapsed hours" and "same wall-clock
  time yesterday" differ by one hour. Elapsed hours is the literal reading of the rule and the one
  the tests check.
- **Alternatives considered**: Wall-clock subtraction (the same local time one calendar day
  earlier). It needs calendar arithmetic, and the spec doesn't ask for it.

## R4. Controlling "now" in tests

- **Decision**: `cancel(id, clientName, now = new Date())`. The optional last parameter defaults to
  the real clock, so tests pass a fixed `now`.
- **Rationale**: This is the simplest way to test the boundary deterministically (exactly 24 h,
  23 h 59 min, past). No clock abstraction or mocking library is needed.
- **Alternatives considered**: `mock.timers` from `node:test` works, but it is more setup per test
  for the same effect. A clock interface or injected service is speculative (Principle I).

## R5. How success and refusal are reported

- **Decision**: `cancel` and `book` return a discriminated union:
  `{ ok: true; appointment }` or `{ ok: false; reason; message }`. `reason` is a string-literal
  code the tests can check. `message` is the English text shown to the client. Neither function
  throws for an expected refusal.
- **Rationale**: Refusals are normal outcomes. The spec requires each one to carry a reason
  (FR-010), and a union type makes the compiler force callers to handle both branches. Using the
  same shape for `book` (which can now refuse under FR-007) keeps the module consistent.
- **Alternatives considered**:
  - Throw an `Error` subclass per reason. That uses exceptions for expected control flow, callers
    can forget to catch, and the types don't show that a refusal can happen.
  - Keep `book` returning `Appointment` and throw only for a taken slot. That mixes two styles in
    one small module.

## R6. Order of refusal checks

- **Decision**: not found → not yours → already cancelled → too late.
- **Rationale**: The spec requires existence and ownership to be reported first, so a client never
  learns anything about someone else's appointment. "Already cancelled" comes before "too late"
  because it describes the appointment more accurately: a past appointment that was cancelled
  earlier should say it's already cancelled, not that it's too late.

## R7. In-memory storage and test isolation

- **Decision**: Keep the existing module-level `appointments` array. Records are never deleted, so
  `id = appointments.length + 1` stays unique. Tests avoid interfering with each other by using a
  distinct start time per test instead of a reset function.
- **Rationale**: `node --test` runs each test file in its own process, so state doesn't leak
  between files. Within the one test file, distinct start times are enough. A `reset()` export
  would exist only for tests (Principle I).

## R8. Notifications and login

- **Decision**: None. Ownership is a strict equality check between the `clientName` passed to
  `cancel` and the one stored on the appointment. No notification or event is emitted when an
  appointment is cancelled or a slot is freed.
- **Rationale**: The planning input and the spec's Assumptions put both out of scope.
