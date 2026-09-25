---

description: "Task list for Client Appointment Cancellation"
---

# Tasks: Client Appointment Cancellation

**Input**: Design documents from `/specs/001-cancel-appointment/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/appointment-module.md, quickstart.md

**Tests**: Required. Constitution Principle III ("Every Rule Has a Test") and SC-005 require an
automated test for every rule. Each story writes its tests first; they must fail (or fail to
type-check) before the implementation task.

**Organization**: Tasks are grouped by user story. The whole feature touches only
`src/appointment.ts`, `src/appointment.test.ts`, `package.json` and `tsconfig.json`, so almost all
tasks edit the same two files and run in sequence.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)

## Path Conventions

Single project at the repository root: source and tests both live in `src/` (plan.md, research R1).

## Shared test conventions (apply to every test task)

- Import with `import { test } from "node:test";`, `import assert from "node:assert/strict";` and
  `import { book, cancel } from "./appointment.ts";` (the `.ts` extension is required, research R1).
- Every `cancel` call in a test passes a fixed `now` as the third argument (research R4). Use the
  constant `NOW` defined in T005 unless the task says otherwise.
- Every test books at its own start instant, listed in the task, so tests never collide on a slot
  (research R7). Do not add a `reset()` export.
- "Still `booked`" means: after the refused `cancel`, assert that the appointment object returned by
  the original `book` call still has `status === "booked"`. `book` returns the stored object itself
  (not a copy), so this reads the stored state.
- Assert both `reason` and the exact `message` string from contracts/appointment-module.md.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Let `node --test` run TypeScript tests and let `tsc` type-check them

- [ ] T001 In package.json add the script `"typecheck": "tsc --noEmit"` next to the existing `"test": "node --test"` (leave `test` unchanged), add `"@types/node": "^26.0.0"` to `devDependencies`, then run `npm install` so package-lock.json is created/updated (research R2)
- [ ] T002 [P] In tsconfig.json add to `compilerOptions`: `"types": ["node"]`, `"rewriteRelativeImportExtensions": true`, `"erasableSyntaxOnly": true`. Keep `"strict": true` and `"include": ["src"]` unchanged (research R1, R2; constitution Principle II)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Result types, the new `book` return shape, and the test file skeleton that every story builds on

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T003 In src/appointment.ts add the exported types exactly as in contracts/appointment-module.md: `AppointmentStatus = "booked" | "cancelled"`; change `Appointment.status` from `"booked"` to `AppointmentStatus`; add `CancelRefusal = "not-found" | "not-yours" | "already-cancelled" | "too-late"`, `BookRefusal = "slot-taken"`, and `Result<R extends string> = { ok: true; appointment: Appointment } | { ok: false; reason: R; message: string }`. Use `type` aliases only (no `enum`, no `interface`-with-classes; `erasableSyntaxOnly`)
- [ ] T004 In src/appointment.ts change `book(clientName: string, startsAt: Date)` to return `Result<BookRefusal>`: build the appointment as today (`id: appointments.length + 1`, `status: "booked"`), push it, and return `{ ok: true, appointment }` with the same object that was pushed (no copy). Do NOT add the slot-taken check yet; that is T016 (US3)
- [ ] T005 Create src/appointment.test.ts with the imports from "Shared test conventions" (import only `book` for now; `cancel` is added in T006), constants `const HOUR = 60 * 60 * 1000;`, `const DAY = 24 * HOUR;`, `const NOW = new Date(2026, 9, 1, 9, 0, 0);` (local clinic time), a helper `const at = (offsetMs: number): Date => new Date(NOW.getTime() + offsetMs);`, and a helper `function booked(clientName: string, startsAt: Date): Appointment` that calls `book`, asserts `r.ok === true` (use `assert.ok(r.ok)` then narrow with `if (!r.ok) throw new Error("booking refused")`), and returns `r.appointment`. Import `type Appointment` from "./appointment.ts". Add one smoke test: `booked("Smoke", at(30 * DAY))` returns `status === "booked"`
- [ ] T006 Run `npm run typecheck` (0 errors) and `npm test` (smoke test passes) from the repo root

**Checkpoint**: Foundation ready. `book` returns a `Result`, tests run on TypeScript without a build step

---

## Phase 3: User Story 1 - Cancel an appointment in good time (Priority: P1) 🎯 MVP

**Goal**: A client cancels their own booked appointment when 24 h or more remain; the record is kept with `status: "cancelled"`. Refusals for not-found, not-yours and already-cancelled, in that order (contract checks 1–3)

**Independent Test**: Book at `NOW + 3 days`, `cancel(id, sameClient, NOW)` → `ok: true` and status `"cancelled"`

### Tests for User Story 1 ⚠️ (write first, must fail)

- [ ] T007 [US1] In src/appointment.test.ts add `cancel` to the import and add these tests (quickstart scenarios 1, 2, 5, 7, 8):
  - "cancels 3 days ahead" (scenario 1): `a = booked("Ann", at(3 * DAY))`; `r = cancel(a.id, "Ann", NOW)`; assert `r.ok === true`, `r.appointment.status === "cancelled"`, `r.appointment.id === a.id`, and `a.status === "cancelled"` (record kept, FR-005)
  - "accepts exactly 24 hours before" (scenario 2): `booked("Ann", at(DAY))`; cancel with `NOW` → `ok: true`
  - "refuses someone else's appointment" (scenario 5): `booked("Ann", at(5 * DAY))`; `cancel(id, "Bob", NOW)` → `reason: "not-yours"`, message `"You can only cancel your own appointments."`, `a.status` still `"booked"`; also `cancel(id, "ann", NOW)` → `"not-yours"` (comparison is exact and case-sensitive)
  - "refuses an already cancelled appointment" (scenario 7): `booked("Ann", at(4 * DAY))`; cancel once with `NOW` (ok); cancel again → `reason: "already-cancelled"`, message `"This appointment is already cancelled."`, status still `"cancelled"`
  - "refuses an unknown id" (scenario 8): `cancel(Number.MAX_SAFE_INTEGER, "Ann", NOW)` → `reason: "not-found"`, message `"No appointment with that number was found."`

### Implementation for User Story 1

- [ ] T008 [US1] In src/appointment.ts add `export function cancel(id: number, clientName: string, now: Date = new Date()): Result<CancelRefusal>`. Look up with `appointments.find((a) => a.id === id)`, then run the checks in this order, returning on the first failure without changing anything (FR-004): (1) not found → `{ ok: false, reason: "not-found", message: "No appointment with that number was found." }`; (2) `appointment.clientName !== clientName` → `"not-yours"`, `"You can only cancel your own appointments."`; (3) `appointment.status === "cancelled"` → `"already-cancelled"`, `"This appointment is already cancelled."`. Leave a spot after check 3 for the 24-hour check (added in T011, US2). Otherwise set `appointment.status = "cancelled"` on the stored object and return `{ ok: true, appointment }`. No notification or other side effect (research R8)
- [ ] T009 [US1] Run `npm run typecheck` (0 errors) and `npm test`; all US1 tests pass

**Checkpoint**: A client can cancel their own appointment; ownership, existence and double-cancel refusals work

---

## Phase 4: User Story 2 - Late cancellation is refused with a reason (Priority: P1)

**Goal**: Cancellation with less than 24 h remaining (including a past or started appointment) is refused as `too-late` with the 24-hour message, and the appointment stays booked. Ownership and already-cancelled are still reported before too-late

**Independent Test**: Book at `NOW + 23 h 59 min`, `cancel(id, sameClient, NOW)` → `too-late`, message names the 24-hour rule, status still `"booked"`

### Tests for User Story 2 ⚠️ (write first, must fail)

- [ ] T010 [US2] In src/appointment.test.ts add these tests; every `too-late` assertion checks message `"Appointments can only be cancelled at least 24 hours before they start."` and that the appointment is still `"booked"`:
  - "refuses 23 h 59 min before" (scenario 3): `booked("Ann", at(DAY - 60 * 1000))`, cancel with `NOW` → `too-late`
  - "refuses 1 ms under 24 hours" (research R3 boundary): `booked("Ann", at(DAY - 1))`, cancel with `NOW` → `too-late`
  - "refuses a past appointment" (scenario 4): `booked("Ann", at(-HOUR))`, cancel with `NOW` → `too-late`
  - "refuses an appointment starting right now": `booked("Ann", at(2 * HOUR))`, cancel with `now = at(2 * HOUR)` → `too-late`
  - "reports ownership before the deadline" (scenario 6): `booked("Ann", at(HOUR))`, `cancel(id, "Bob", NOW)` → `reason: "not-yours"` (not `"too-late"`), still `"booked"`
  - "reports already-cancelled before the deadline" (research R6): `a = booked("Ann", at(2 * DAY))`, cancel with `NOW` (ok), then `cancel(a.id, "Ann", at(2 * DAY + HOUR))` → `reason: "already-cancelled"` (not `"too-late"`)

### Implementation for User Story 2

- [ ] T011 [US2] In src/appointment.ts add a module constant `const DAY_MS = 24 * 60 * 60 * 1000;` and, in `cancel` after the already-cancelled check and before setting the status, add check (4): `if (appointment.startsAt.getTime() - now.getTime() < DAY_MS)` return `{ ok: false, reason: "too-late", message: "Appointments can only be cancelled at least 24 hours before they start." }`. Exactly 24 h remaining (`=== DAY_MS`) is accepted; negative remaining time is refused (FR-001, FR-002, research R3)
- [ ] T012 [US2] Run `npm run typecheck` (0 errors) and `npm test`; all US1 and US2 tests pass

**Checkpoint**: The 24-hour rule is enforced with a clear message; US1 still passes

---

## Phase 5: User Story 3 - A cancelled appointment's slot can be booked again (Priority: P2)

**Goal**: `book` refuses a start instant that already holds a `"booked"` appointment; a cancelled appointment does not block it (FR-006, FR-007)

**Independent Test**: A books T and cancels in good time; B books T → `ok: true`. A books T'; B books T' → `slot-taken`

### Tests for User Story 3 ⚠️ (write first, must fail)

- [ ] T013 [US3] In src/appointment.test.ts add "refuses a taken slot" (scenario 10): `a = booked("Ann", at(6 * DAY))`; `r = book("Bob", new Date(at(6 * DAY).getTime()))` (a different `Date` object for the same instant) → `ok: false`, `reason: "slot-taken"`, message `"That time is already booked. Please choose another time."`; `a.status` still `"booked"`; then prove nothing was added: `c = booked("Cid", at(6 * DAY + HOUR))` and assert `c.id === a.id + 1` (tests in one file run sequentially)
- [ ] T014 [US3] In src/appointment.test.ts add "a cancelled slot can be booked again" (scenario 9): `a = booked("Ann", at(7 * DAY))`; `cancel(a.id, "Ann", NOW)` is ok; `r = book("Bob", at(7 * DAY))` → `ok: true`, `r.appointment.clientName === "Bob"`, `r.appointment.status === "booked"`, `r.appointment.id !== a.id`, and `a.status` is still `"cancelled"`. Then `book("Cid", at(7 * DAY))` → `slot-taken` (Bob's booking now holds it)
- [ ] T015 [US3] Run `npm test` and confirm "refuses a taken slot" fails because the second booking is accepted ("a cancelled slot can be booked again" may already pass; it guards against over-blocking)

### Implementation for User Story 3

- [ ] T016 [US3] In src/appointment.ts, at the start of `book`, before creating the appointment, return `{ ok: false, reason: "slot-taken", message: "That time is already booked. Please choose another time." }` when `appointments.some((a) => a.status === "booked" && a.startsAt.getTime() === startsAt.getTime())`. Compare with `getTime()`, not `===` on `Date` objects (data-model.md "Slot"). A refused booking pushes nothing
- [ ] T017 [US3] Run `npm run typecheck` (0 errors) and `npm test`; all US1, US2 and US3 tests pass

**Checkpoint**: All user stories work; a freed slot is bookable immediately (SC-003)

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Merge-gate and constitution checks across the whole feature

- [ ] T018 Delete the smoke test added in T005 from src/appointment.test.ts; the story tests now cover `book` (keep the `booked` and `at` helpers)
- [ ] T019 Check src/appointment.ts and src/appointment.test.ts contain no `any`, `@ts-ignore`, `@ts-expect-error` or `enum` (constitution Principle II), and that every quickstart.md scenario 1–10 maps to a named test (constitution Principle III, SC-005)
- [ ] T020 Run the "Try it by hand" snippet from specs/001-cancel-appointment/quickstart.md at the repo root and confirm it prints `{ ok: true, appointment: { ..., status: 'cancelled' } }`
- [ ] T021 Final merge gate: `npm run typecheck` reports 0 errors and `npm test` passes

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies
- **Foundational (Phase 2)**: Depends on Setup (T005 needs `@types/node` and the tsconfig changes). BLOCKS all stories
- **US1 (Phase 3)**: Depends on Foundational
- **US2 (Phase 4)**: Depends on US1, because it adds check 4 to the `cancel` function US1 creates, and its ordering tests use the not-yours / already-cancelled checks from US1
- **US3 (Phase 5)**: Its implementation (T016) depends only on Foundational; its tests (T014) call `cancel`, so the story as a whole depends on US1 (as spec.md states). It does not depend on US2
- **Polish (Phase 6)**: Depends on all stories

### Within Each User Story

- Tests first, confirm they fail, then implement, then run the merge-gate commands
- All tasks in a story edit the same file(s), so they run in order

### Parallel Opportunities

- T001 and T002 (package.json vs tsconfig.json)
- After US1 is done, US2 and US3 could be split between two people (US2 edits `cancel`, US3 edits `book`), but both append tests to src/appointment.test.ts, so expect a trivial merge in that file. With one implementer, run them in order
- There is little else to parallelize: the feature is one module and one test file by design (constitution Principle I)

---

## Parallel Example: Setup

```bash
Task: "T001 Add typecheck script and @types/node to package.json, run npm install"
Task: "T002 Add types, rewriteRelativeImportExtensions, erasableSyntaxOnly to tsconfig.json"
```

## Parallel Example: after US1

```bash
Task: "T010–T012 [US2] 24-hour check in cancel() + tests"
Task: "T013–T017 [US3] slot-taken check in book() + tests"
```

---

## Implementation Strategy

### MVP First (User Stories 1 + 2)

Both US1 and US2 are P1. US1 alone would let late cancellations through, which breaks the
clinic's policy, so the smallest releasable increment is US1 **and** US2:

1. Phase 1: Setup
2. Phase 2: Foundational
3. Phase 3: US1 → validate
4. Phase 4: US2 → validate. **MVP: cancellation with the 24-hour rule**

### Incremental Delivery

1. Setup + Foundational → `book` returns `Result`, tests run
2. US1 → clients can cancel their own appointments
3. US2 → late cancellations refused with a reason (MVP ready)
4. US3 → freed slots bookable again, double-booking refused
5. Polish → merge gate

---

## Notes

- `book` changes from returning `Appointment` to `Result<BookRefusal>` (breaking). Nothing else in the repo calls it (plan.md Design Notes)
- Do not add a clock service, a `reset()` export, a slot table, notifications, or new runtime dependencies (constitution Principle I, research R4, R7, R8)
- Commit after each checkpoint
