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
* At start, the server creates the SQLite file if it is missing, applies
  every migration not applied yet, in file name order, and records each one.
* Starting the server a second time applies no migration.
* A migration that fails is not recorded, leaves the database as it was
  before that file, and stops the start with a message naming the file.
* `npm run verify` runs typecheck, lint, the Vitest tests, the Playwright
  tests and the build, and ends with exit code 0.
* `npm run verify` fails when a file that is not server code imports a
  `*.server.ts` file (ADR-0002).
* The page carries a web manifest, so a phone browser offers "Add to home
  screen" with the name "Clinic" and the app's icon.

**Contract.**

Route, no session needed:

```
GET /api/health
200  { "status": "ok" }
```

Table, created by the migration runner itself before it reads
`src/server/migrations/`, not by a migration file:

```sql
CREATE TABLE IF NOT EXISTS schema_migration (
  name       TEXT PRIMARY KEY,  -- the migration's file name, e.g. 0001-clinic.sql
  applied_at TEXT NOT NULL      -- UTC instant, ISO 8601, e.g. 2026-09-28T15:04:05.000Z
);
```

Migrations: files `src/server/migrations/NNNN-<name>.sql`, four digits, applied
in file name order, each in its own transaction together with its
`schema_migration` row. This delivery ships the folder empty.

Environment variables of the server:

| Name | Default | Meaning |
|---|---|---|
| `PORT` | `3000` | Port of the Hono server. |
| `DATABASE_PATH` | `data/clinic.sqlite` | The SQLite file; `data/` is ignored by git. |

In development, Vite serves the client and forwards `/api/*` to the server.

Web manifest: `name` "Clinic", `short_name` "Clinic", `start_url` "/",
`display` "standalone", icons 192×192 and 512×512 PNG.

Node: `engines` `>=24`.

**States.**

* Empty: not applicable, the page has no list.
* Loading: "Checking the server".
* Error: "Server: unreachable".
* Offline: same as error; there is no service worker.

**Visual reference.** No design file. Plain, clean default styling. One
client screen at phone width (390×844).

**Out of scope.**

* Service worker and offline use: booking needs the network; its own
  delivery if ever wanted.
* The server serving the built client in one process: `deploy` needs it,
  `deploy` builds it.
* The clinic's real name in the heading: it exists only after
  `clinic-setup`.
* Any business table, sign-in or session: `clinic-setup`.
* `src/lib/result.ts`: `Result` lives in the health slice until a second
  feature uses it (docs/01); `clinic-setup` is expected to be that second
  use.
* CI: one developer, one machine; `npm run verify` is the gate.

**Done when.**

* [ ] Repository tests of the migration runner pass against a temporary
      SQLite file: applies in order, records, skips applied ones, rolls back
      and names a failing file.
* [ ] Playwright tests of the three page states pass at 390×844, the "ok"
      state with a `toHaveScreenshot` baseline committed next to the test.
* [ ] `npm run verify` is green, and fails on a deliberate client import of
      a `*.server.ts` file (checked once, then removed).
* [ ] `npm run dev` leaves client and server running locally, with the
      SQLite file created.
* [ ] docs/02 lists `GET /api/health` and `schema_migration`; docs/01 and
      docs/05 name the local command.
