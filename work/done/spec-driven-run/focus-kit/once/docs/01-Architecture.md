# Architecture

A TypeScript module where each feature is a function over in-memory data that returns errors as values.

## Stack
- **TypeScript**, `strict`, target ES2022, ES modules (`"type": "module"`, `module: NodeNext`). Observed (ADR-0001).
- **Node.js** runs the code and the tests, stripping types from `.ts` directly (Node 26 on the development machine). Observed.
- **`node --test`** as the test runner rather than a framework: no dependency (ADR-0005).
- No runtime dependency; `typescript` is the only development dependency.

## Organization
The two principles of FOCUS, without its four pieces (ADR-0003):
- **Vertical slices.** One file per feature in `src/`, holding its type, its rules and its state: `src/appointment.ts`. A shared file exists only when a second feature needs it.
- **Errors as values.** A rule that can refuse returns a Result the caller inspects; `throw` is never flow. The Result shape is fixed by the first delivery that needs it (`book-validation`) and recorded here.

Observed today: `book()` validates nothing and cannot fail; it returns the `Appointment` directly.

## Data access
A module-level array in `src/appointment.ts` holds the appointments; its functions read and change it directly. Nothing survives the process (ADR-0002). `id` is `appointments.length + 1`, unique only while nothing is removed from the array.

## Errors
None travel today: no function throws or refuses. From `book-validation` on, refusals are Result values.

## Environments
- **Local:** the only one. Node runs the code and the tests. Nothing is built, published or deployed.

## Removed on purpose
Nothing yet.

## Open questions
- `tsconfig.json` sets `outDir: dist`, but no script compiles and nothing reads `dist`: is `tsc` a check (`--noEmit`) or a build? `verify` decides.
- `module: NodeNext` expects imports ending in `.js`, while Node runs the `.ts` files; a test importing `./appointment.ts` needs `allowImportingTsExtensions` or `rewriteRelativeImportExtensions`. `verify` decides.
- The store is module state shared by every test in a file; how a test starts from empty is decided by `verify`.
- There is no lockfile, and `typescript` is not installed.
