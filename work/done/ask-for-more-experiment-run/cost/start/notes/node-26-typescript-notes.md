# Node 26 + TypeScript — how we run things

_Last edited by Rafe, 2026-02-03. Tamsin reviewed._

Short version: we write `.ts` files and Node 26 runs them directly. No build step, no compiler, no `node_modules`.

## Setup

- Node **26** or newer. `package.json` has `"engines": { "node": ">=26" }` and `"type": "module"`.
- That's it. Clone, `npm test`, done.

## How it works

Node 26 does **type stripping**: loading a `.ts` file, it erases type annotations and runs the rest as plain JavaScript, transforming nothing else. Consequences follow.

### Only erasable syntax

Anything needing TypeScript to *generate* JavaScript is unsupported. For us:

- **No `enum`** — enums produce a runtime object. Use string literal unions:
  ```ts
  export type CopyStatus = 'available' | 'on-loan' | 'withdrawn';
  ```
  Hence every status and error code is a string union. We prefer it — values show up readably in `deepEqual` output.
- **No `namespace`.** Use modules (one file = one module).
- **No constructor parameter properties.** `constructor(private readonly id: string) {}` generates an assignment. We rarely use classes — the domain is plain objects and functions — but if you write one, assign fields explicitly.
- Other non-erasable things (legacy decorators with metadata, `import x = require(...)`) — don't.

### Imports

- **Imports need the `.ts` extension.** `import { ok } from '../../shared/result.ts'`, not `'../../shared/result'` or `.js`. Node resolves exactly as written.
- **Use `import type` for types**, or inline `import { err, ok, type Result } from ...`. Type-only imports are stripped entirely; importing a type as a value makes Node look for a nonexistent runtime export and fail at load.

### No type checking at runtime

- Node does **not** type-check; a type error runs happily.
- **No `tsconfig.json` needed** to run code or tests.
- Editor TypeScript support works without a config for this layout. We might add `tsc --noEmit` in CI later — that would need a tsconfig, but only for checking.
- Upshot: tests keep us honest. Types are documentation the editor checks; tests are what runs.

## Running tests

```
npm test
```

which is just

```
node --test
```

- `node --test` with no arguments finds test files by default patterns, including `*.test.ts`, so `features/loans/loans.test.ts` etc. are picked up automatically.
- One file: `node --test features/loans/loans.test.ts`
- Filter by name: `node --test --test-name-pattern="renew"`
- Watch mode: `node --test --watch`
- Built-in reporter is good enough; `--test-reporter=spec` for the tree view.

Tests use `node:test` (`describe`, `it`) and `node:assert/strict`. Details in `testing conventions.md`.

## No dependencies — decision

Agreed at the 2026-01-26 tech catch-up (TO, RL, MS):

- **Zero runtime and zero dev dependencies.** No `dependencies` or `devDependencies` block in `package.json`.
- Reasons:
  - Nothing to install, audit or upgrade. Small domain model, small library; post-handover maintenance budget is basically zero.
  - Node 26 provides TS execution, a test runner, assertions.
  - Dates are the usual excuse for a library; ADR-003 covers why we don't need one.
- Want a dependency? Bring it to Tamsin first with what it saves. Bar is high.

## Gotchas we hit

- Rafe wrote `enum LoanState` on day one out of habit → `ERR_UNSUPPORTED_TYPESCRIPT_SYNTAX` (or similar) on load. Converted to a union.
- Marek imported `Member` without `type` → runtime "does not provide an export named" error. Fixed with `import type`.
- Forgetting `.ts` on an import → module not found. All of us did this at least once.
- Someone's editor auto-added `.js` extensions. Setting turned off.
