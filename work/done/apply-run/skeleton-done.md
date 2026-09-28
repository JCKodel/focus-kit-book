# skeleton

**Objective.** A developer runs one command and sees the app's first page on
a phone-sized screen, answered by the server, and `npm run verify` proves the
whole project is sound.

**Behaviour.**

* With `npm run dev`, the client and the server start together; opening the
  client at 390×844 shows the heading "Clinic" and the line "Server: ok".
* While the answer is on its way, the page shows "Checking the server".
* When the server does not answer, or answers with an error, the page shows
  "Server: unreachable" instead of a blank page or a crash.
* At start, the server creates the `data/` folder and the SQLite file if they
  are missing, applies every migration not applied yet, in file name order,
  and records each one.
* Starting the server a second time applies no migration.
* A migration that fails is not recorded, leaves the database as it was
  before that file, and stops the start with exit code 1 and a message
  naming the file.
* `npm run verify` runs typecheck, lint, the Vitest tests, the Playwright
  tests and the build, and ends with exit code 0.

**Contract.**

Route, no session needed:

```
GET /api/health
200  { "status": "ok" }
```

Table, created by the migration runner itself before it reads the folder,
not by a migration file:

```sql
CREATE TABLE IF NOT EXISTS schema_migration (
  name       TEXT PRIMARY KEY,  -- the migration's file name, e.g. 0001-clinic.sql
  applied_at TEXT NOT NULL      -- UTC instant, ISO 8601, e.g. 2026-09-28T15:04:05.000Z
);
```

Migrations: files `NNNN-<name>.sql`, four digits, applied in file name order,
each in its own transaction together with its `schema_migration` row. Files
not matching the pattern are ignored. The real folder is
`src/server/migrations/`; this delivery ships it empty.

Migration runner, `src/server/migrate.server.ts`. It takes the folder as a
parameter, so tests pass a temporary folder of fixture files and the server
start passes `src/server/migrations/`:

```ts
function migrate(db: DatabaseSync, folder: string): Result<string[], MigrationFailed>
// ok: the file names applied in this call, in order; [] when none

type MigrationFailed = { code: "MigrationFailed"; file: string; message: string }
// file: the file name that failed; message: the SQLite error text
```

`Result`, in `src/lib/result.ts`, as docs/01 defines it. First use: the
health `api.ts`; second use: `migrate`. That second use is why it moves to
`lib/` in this delivery.

Environment variables of the server:

| Name | Default | Meaning |
|---|---|---|
| `PORT` | `3000` | Port of the Hono server. |
| `DATABASE_PATH` | `data/clinic.sqlite` | The SQLite file; `data/` is ignored by git. |

In development, Vite serves the client and forwards `/api/*` to the server.

Node: `engines` `>=24`.

**States.**

* Empty: not applicable, the page has no list.
* Loading: "Checking the server".
* Error: "Server: unreachable".
* Offline: same as error; there is no service worker.

**Visual reference.** No design file. One client screen at phone width
(390×844). Plain, clean default styling, which here means the `system-ui`
font, 16px padding on each side, the heading and the status line
left-aligned, and no colours beyond the browser defaults. The proof is a
screenshot you look at, not a pixel baseline.

**Out of scope.**

* Web manifest, icons and "Add to home screen": the name and the icon
  belong to the clinic, which exists only after `clinic-setup`; it gets its
  own delivery, `install`.
* Service worker and offline use: booking needs the network; its own
  delivery if ever wanted.
* An automatic check that client code does not import `*.server.ts`: no
  such import has happened yet (docs/05 §7). The rule lives in docs/01 and
  ADR-0002 until one does.
* A `toHaveScreenshot` pixel baseline: without a design file it would only
  freeze whatever was built, and it breaks with the machine's fonts.
* The server serving the built client in one process: `deploy` needs it,
  `deploy` builds it.
* The clinic's real name in the heading: it exists only after
  `clinic-setup`.
* Any business table, sign-in or session: `clinic-setup`.
* CI: one developer, one machine; `npm run verify` is the gate.

**Done when.**

* [x] Vitest tests of `migrate` pass, each against an in-memory SQLite and
      a temporary folder of fixture `.sql` files: applies in file name
      order, records each file, skips applied ones, ignores files not
      matching the pattern, and on a failing file rolls it back, leaves it
      unrecorded and returns `MigrationFailed` naming it.
* [x] One Vitest test, against a temporary directory, shows the server's
      database opening creates the missing folder and SQLite file.
* [x] `migrate` against the real `src/server/migrations/` returns `[]`.
* [x] Playwright tests of the three page states pass at 390×844, asserting
      the texts of Behaviour.
* [x] A screenshot of the "ok" state at 390×844 is saved once, as proof,
      to `work/done/skeleton-390x844.png`; it is not part of `npm run verify`.
* [x] `npm run verify` is green.
* [ ] `npm run dev` leaves client and server running locally, with the
      SQLite file created. The SQLite file exists (`data/clinic.sqlite`,
      created by a server start); the agent's session was not allowed to
      start a long-running process, so the person starts `npm run dev`.
* [x] docs/02 lists `GET /api/health` and `schema_migration`; docs/01 and
      docs/05 name the local command.

## What happened

**Built.** `src/lib/result.ts`; the `health` slice (`route.server.ts`,
`api.ts`, `useHealth.ts`, `HealthView.tsx`, `strings.ts`,
`HealthView.e2e.ts`); the server shell (`main.server.ts`,
`database.server.ts`, `migrate.server.ts`, empty `migrations/`); the app
shell (`src/app/main.tsx`, `src/app/strings.ts`, `index.html`); config for
TypeScript, Biome, Vite and Playwright; `.gitignore`.

**Diverged from the plan, and why.**

* `@hono/node-server` was added next to `hono`: Hono needs an adapter to
  listen on a Node port. It is part of "Node with Hono", recorded in docs/01.
* The server has no build and no runner such as `tsx`: Node `>=24` runs
  `.ts` directly by type stripping. Consequence, in docs/01: imports carry
  `.ts`, and `erasableSyntaxOnly` forbids enums and similar syntax.
* `npm run dev` is `node --watch src/server/main.server.ts & vite`, the
  shell's `&` instead of a tool like `concurrently`, since the page named no
  such tool. Ctrl+C stops both, as they share the terminal's process group.
* `openDatabase` returns `Result<DatabaseSync, DatabaseOpenFailed>` rather
  than throwing, so `throw` is not flow in the server start either. It is
  the third use of `Result` (first: health `api.ts`; second: `migrate`).
* `migrate` also returns `MigrationFailed` when the folder cannot be read or
  `schema_migration` cannot be created. No file was reached then, so `file`
  holds the folder path. The contract names only the per-file case.
* The unreachable state has two Playwright tests (500 answer, aborted
  request), one for each case of Behaviour; the page counted three states.
* The client's error code is `ServerUnreachable`. It is an infrastructure
  code, like `MigrationFailed` and `DatabaseOpenFailed`, so it is not a term
  of docs/03.
* npm installed the current majors: TypeScript 7, Vite 8, Vitest 5,
  Playwright 1.63, Biome 2, React 19, Hono 4.

**Dropped.** Nothing from Behaviour or Contract.

**What the proof found.** The screenshot at 390×844 shows "Clinic" and
"Server: ok" in `system-ui`, left-aligned with 16px on each side, browser
default colours: nothing diverges from the Visual reference. It was taken
by a one-off `page.screenshot` in the "ok" Playwright test, removed after
the run. A manual start with a temporary failing `0001-broken.sql` in
`src/server/migrations/` exited with code 1 and
`Migration 0001-broken.sql failed: no such table: missing`, left only
`schema_migration` (empty) in the database, and the file was removed.

**Decisions.** Playwright files are `*.e2e.ts` next to their view, and
Playwright starts its own server and Vite on ports 3100 and 5174 with a
database in the system temp folder (docs/04). No ADR: every choice sits
inside ADR-0001.
