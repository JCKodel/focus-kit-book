# Implementation Plan: Client Appointment Cancellation

**Branch**: `001-cancel-appointment` | **Date**: 2026-09-25 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-cancel-appointment/spec.md`

## Summary

A client can cancel their own booked appointment when at least 24 hours remain before it starts.
Later cancellations are refused with a message that names the 24-hour rule, and a cancelled
appointment frees its start time for a new booking. The work adds a `cancel(id, clientName, now?)`
function to `src/appointment.ts`, widens `status` to `"booked" | "cancelled"`, and makes `book`
refuse a start time that already holds a booked appointment. Both functions return a typed
`{ ok: true } | { ok: false, reason, message }` result. Storage stays in memory. There is no screen,
no login and no notification. Tests run with `node --test` directly on TypeScript.

## Technical Context

**Language/Version**: TypeScript 7 (`strict`), ES modules, run on Node.js 26 through native type stripping

**Primary Dependencies**: None at runtime. Dev: `typescript` (already present) and `@types/node` (new, types only; see research R2)

**Storage**: In memory, the module-level `appointments` array. Nothing is persisted

**Testing**: `node --test` (Node's built-in runner and `node:assert/strict`) through `npm test`. Type-check with `tsc --noEmit`

**Target Platform**: Node.js 26+, running in the clinic's local time zone

**Project Type**: Single-module library. The feature is an exported function; no UI, CLI or HTTP

**Performance Goals**: N/A. A single small clinic, and a linear scan of an in-memory array is enough

**Constraints**: Times are the clinic's local time. 24 h means 86,400,000 ms of elapsed time (research R3). Identity is `clientName` only. No notifications

**Scale/Scope**: One module (`src/appointment.ts`) and one test file. Tens to hundreds of appointments

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Check | Pre-research | Post-design |
|-----------|-------|--------------|-------------|
| I. Keep It Simple | No new layers or abstractions. Everything stays in `src/appointment.ts`. Slots are derived, not stored. `now` is a default parameter, not a clock service. No test-only `reset()`. The one new dependency (`@types/node`, dev, types only) is justified in research R2 | ✅ | ✅ |
| II. Strict TypeScript | `strict` stays on. The test file lives under `src/` so it gets type-checked. No `any` or `@ts-ignore`. `erasableSyntaxOnly` guarantees the code runs under type stripping. `npm run typecheck` added for the merge gate | ✅ | ✅ |
| III. Every Rule Has a Test | Every rule (24 h deadline, exact boundary, past start, ownership, already cancelled, not found, slot taken, slot freed, check order) maps to a scenario in [quickstart.md](./quickstart.md) | ✅ | ✅ |
| Tech constraints | TypeScript, ESM, Node, `node --test` through `npm test`. All kept | ✅ | ✅ |

No violations, so Complexity Tracking is empty.

## Project Structure

### Documentation (this feature)

```text
specs/001-cancel-appointment/
├── plan.md                        # This file
├── research.md                    # Phase 0: decisions R1–R8
├── data-model.md                  # Phase 1: Appointment, Slot, Result
├── quickstart.md                  # Phase 1: how to validate + scenario table
├── contracts/
│   └── appointment-module.md      # Phase 1: exported API, messages, check order
├── checklists/requirements.md     # From /speckit-specify
└── tasks.md                       # Phase 2 (/speckit-tasks — not created here)
```

### Source Code (repository root)

```text
src/
├── appointment.ts         # modified: status union, Result types, book() slot check, new cancel()
└── appointment.test.ts    # new: node --test suite covering every rule

package.json               # modified: add "typecheck" script, @types/node devDependency
tsconfig.json              # modified: types ["node"], rewriteRelativeImportExtensions, erasableSyntaxOnly
```

**Structure Decision**: Keep the existing single-module layout. The test file sits next to the
module under `src/`, so the current `tsconfig.json` `include` already type-checks it and
`node --test` finds it with its default `**/*.test.ts` pattern.

## Design Notes

- **Breaking change**: `book` now returns `Result<"slot-taken">` instead of `Appointment`. Nothing
  in the repository calls it, so nothing else needs updating.
- **Check order** in `cancel`: not-found → not-yours → already-cancelled → too-late (research R6).
- **Boundary**: `remaining >= 24h` is accepted, so exactly 24 h passes. On a daylight-saving
  change night, "24 hours" is elapsed time, not the same wall-clock time a day earlier (research R3).

## Complexity Tracking

No constitution violations.
