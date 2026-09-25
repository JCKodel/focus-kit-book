<!--
Sync Impact Report
- Version change: (template, unversioned) → 1.0.0
- Modified principles:
  - [PRINCIPLE_1_NAME] → I. Keep It Simple
  - [PRINCIPLE_2_NAME] → II. Strict TypeScript
  - [PRINCIPLE_3_NAME] → III. Every Rule Has a Test
- Removed principles: template slots 4 and 5 (user asked to keep it simple; three suffice)
- Added sections: Technology Constraints, Development Workflow, Governance
- Removed sections: none
- Follow-up TODOs: none
-->

# Clinic Weigh-In Constitution

## Core Principles

### I. Keep It Simple

- Build the simplest thing that satisfies the current spec. No speculative features,
  abstractions, or configuration (YAGNI).
- New dependencies MUST be justified in the plan; prefer the Node.js standard library.
- Any added complexity (extra layer, pattern, or package) MUST be recorded with its reason in the
  plan's complexity tracking.

Rationale: a small clinic app is easier to change, review, and trust when there is less of it.

### II. Strict TypeScript

- All source code MUST be TypeScript with `"strict": true` in `tsconfig.json`; strictness MUST NOT
  be relaxed.
- `any`, `@ts-ignore`, and `@ts-expect-error` MUST NOT be used unless a code comment states why
  no typed alternative exists.
- The project MUST type-check with zero errors before merge.

Rationale: the compiler catches whole classes of bugs for free; weakening it gives that away.

### III. Every Rule Has a Test

- Every business rule (e.g. scheduling, availability, cancellation) MUST have at least one
  automated test that fails if the rule is broken.
- A bug fix MUST include a test that reproduces the bug.
- A rule without a test is not done.

Rationale: tests are the executable definition of the rules; untested rules drift silently.

## Technology Constraints

- Language: TypeScript (strict), ES modules, Node.js runtime.
- Tests: Node's built-in test runner (`node --test`, invoked via `npm test`).
- Additional tooling MUST satisfy Principle I.

## Development Workflow

- Each change goes spec → plan → tasks → implementation, as far as its size warrants.
- Merge gate: type-check passes with zero errors and `npm test` passes.
- Reviews MUST confirm each new or changed rule has a matching test.

## Governance

This constitution supersedes other practices where they conflict. Amendments are made by
updating this file with a stated reason and a version bump:

- MAJOR: a principle is removed or redefined incompatibly.
- MINOR: a principle or section is added or materially expanded.
- PATCH: clarifications and wording fixes.

Every plan MUST pass a Constitution Check against these principles, and every review MUST verify
compliance.

**Version**: 1.0.0 | **Ratified**: 2026-09-25 | **Last Amended**: 2026-09-25
