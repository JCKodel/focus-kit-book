# `/propose`, one page

After this chapter you can run `/propose` on a queue line, answer its questions, and read the page it writes as the record of what the agent understood and of what `/apply` will build.
You can cover the page's holes by conversation before `/apply`, and split a delivery that does not fit one page.

## What it does

Every piece of work in a focus-kit project is a delivery: the smallest change that has value, what other methods call a task or a work item.
The queue, docs/06, lists the deliveries in order, one line each ([chapter 9](09-queue-and-milestones.md)).
`/propose` takes one line and turns it into a page, `work/<slug>.md`: what the delivery must do, what it must not do, and how you will know it is done.[^focus-kit-propose]
The page fits on one page so that a person can review it, before the build and after it: once `/apply` has built it, the same page also records what happened, what diverged and what was decided, as the clinic's [docs/05 §3](https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/brainstorm/docs/05-Process.md) defines it.
If it does not fit one page, the scope has not been understood yet, and it is two deliveries (the last section of this chapter).

### Where the slug comes from

A slug is the delivery's name, in lowercase words joined by hyphens, such as `skeleton` or `book-appointment`.
It is written once, in the queue line, and from then on it names everything about the delivery: the page `work/<slug>.md`, the argument of `/propose <slug>` and of `/apply <slug>`, and the last line of the commit that closes it, `work/done/<slug>.md`.
The first lines come from `/brainstorm` or `/analyze`, which write the first milestone ([chapter 7](07-brainstorm.md), [chapter 8](08-analyze.md)); later lines come from a conversation or from a milestone's review ([chapter 9](09-queue-and-milestones.md)).
If you type `/propose` with no slug, it asks you for one.[^focus-kit-propose]

### When the line does not exist

You can also type `/propose` with a slug the queue does not have yet.
It defines the delivery the same way, adds its line to the queue where it belongs, and tells you it did.[^focus-kit-propose]
A new idea therefore reaches the queue and its page in one conversation; you still check, in the diff of docs/06, the milestone and the place where the line landed.

### How it knows what to do

It reads before it asks.[^focus-kit-propose]
The line's one-line description is where it starts; the project documents give it the rest:

* docs/00, the product: who it serves, its rules, what it is not.
* docs/03, the vocabulary: the words the page must use, each with its name in code.
* docs/05, the process: the project's slots (the verify command, how a screen is proven, the git strategy) and the format of the page.
* docs/06, the queue: what comes before and after this line.
* `work/`: the deliveries in flight, so the new page does not collide with one of them.
* docs/01, the architecture: where the change lives in the code.

Then it asks, only where there is more than one reading and no document closes it: its assessment first, in prose, and its recommendation first in every question, so "your call" is a valid answer, as with `/brainstorm` ([chapter 7](07-brainstorm.md)).
It writes the page in the format of docs/05 §3 and turns the line's mark from `[ ]` to `[>]`; a new term goes into docs/03 first, then onto the page.[^focus-kit-propose]

### Why not do it all in one step

`/propose` never writes, edits or generates code, a migration, a test or configuration, and the kit says why: "*separating deciding from doing is what keeps scope from growing during implementation*".[^focus-kit-propose]
An agent that plans and builds in one breath takes its decisions in the middle of the build, where you do not see them; the page puts every decision where you can read it before any code exists.
`/apply` then starts in a fresh session ([chapter 2](02-how-agents-see.md)), with a clean context, and the page is all it takes from this conversation, so the page has to hold everything the build needs.
And the order is the cheap one: a hole found on the page costs a turn of conversation, a hole found in the build costs another `/apply` (the numbers are in "Read the page before `/apply`").

### How you correct the page

You ask the agent, in the same conversation, and it writes the fix: on the page, and in any document the fix touches.[^focus-kit-propose]
You do not edit the page by hand ([chapter 6](06-the-documents.md)): the agent knows which document owns each fact, so a fix that touches the vocabulary or the queue lands there too, and the conversation keeps the reason for the change.
"Read the page before `/apply`", below, shows a real review, with the request and the diff.

### Why not your host's plan mode

Hosts have their own way to plan before editing: in Claude Code it is plan mode, where "*Claude reads files and proposes a plan but makes no edits until you approve*".[^claude-code-plan-mode]
Plan mode works inside one session, for the change at hand.
The page works for the project: a file in the repository, in the format docs/05 fixes, written from the project documents and in their words, marked in the queue, read by a fresh session to build it, and kept in `work/done/` with what happened, in the same commit as the build.
Use plan mode inside a session if it helps you; the page is what outlives the session.

### The Contract, the one exact section

One section of the page must be exact, the Contract: the data, the schema, the API, the shapes of the messages.
The kit gives the reason: "*a wrong screen is fixed in a session, a wrong column is a migration*".[^focus-kit-propose]
A screen is code you rewrite; a column holds data, and changing it means a migration that carries the data already there.

### One unit of work

Between the two commands the line reads `[>]`: the page exists and the build does not ([chapter 9](09-queue-and-milestones.md)).
The page and its build are one unit of work: one change that reverts in one step.[^focus-kit-unit-of-work]
On trunk they land in one commit, so the page waits uncommitted in the working tree between `/propose` and `/apply`; on a branch or a worktree, the branch may carry several commits, and the delivery reaches the main branch in one merge.
Part IV teaches the git side; the clinic is on trunk, which is why the run below leaves it uncommitted.

## The run on the clinic

The run started from the clinic after `book-v1/brainstorm`, at commit [`3f0b47c`](https://github.com/JCKodel/focus-kit-clinic/commit/3f0b47c1868e69970eefadb4f4a34bdcbada67b2), "Update focus-kit to e7607c5": the kit updated as chapter 5 teaches, in a commit of its own, so the update reverts in one step.
In that version the kit's `/propose` ends by asking you to read the page before `/apply`, and the run shows it.[^focus-kit-propose]
The delivery was the queue's first line, `skeleton`: the empty PWA and server in one project, `npm run verify`, and the first screenshot.
The brief names the line and gives the rule for everything else:[^propose-run]

```markdown
# Brief

## Delivery
The first line of the queue: skeleton.

## Rule for a question the brief does not answer
Your call. Say what you chose and why.
```

Open your host at the root of the project, in a fresh session, and type `/propose skeleton`; I ran it headless in Claude Code and answered with the brief's rule.[^propose-run]
The agent read the documents and asked:[^propose-run]

````markdown
I've read docs/00 to 06, the ADRs and `work/` (only `done/`, which is empty). Git is trunk (ADR-0003), so the page will go on `main` with no branch.

**My read of `skeleton`:** this delivery adds no business rule. It builds the frame every later delivery relies on: one TypeScript project with a Vite React client and a Hono server, Biome, Vitest, Playwright, `npm run verify` and a local run command. It also creates the empty `src/features/`, `src/app/`, `src/server/` and `src/lib/` layout from docs/01, and saves the first screenshot at 390×844. The risk is scope creep: anything that belongs to `clinic-setup` (tables, sign-in) or to a later offline story shouldn't slip in here. The docs leave four points open that change the page.

**1. What does the first screen show?** I recommend a single client page that fetches `GET /api/health` and shows "Server: ok", or a clear message if the server can't be reached. The screenshot then proves the whole path: client, proxy, server, JSON and the `Result` error path. The heading would be a neutral "Clinic", because the clinic's name doesn't exist until `clinic-setup`. The simpler option is a static page with no server call, but then nothing tests the server half until `clinic-setup`.

**2. Where do the database and the migration runner go?** I recommend putting them in `skeleton`: it opens the SQLite file through `node:sqlite` and applies the SQL files in `src/server/migrations/` in order at startup, with a repository test. That means one exact contract item, a bookkeeping table `schema_migration (name TEXT PRIMARY KEY, applied_at TEXT NOT NULL)`, and no business table. `clinic-setup` is already the heaviest line in milestone 1 (setup command, owner, sessions, scrypt, sign-in screens), so moving this out makes it lighter. The other option is to leave all of it to `clinic-setup`, which creates the first real table.

**3. How much PWA?** I recommend a web manifest and one icon, and no service worker. Booking needs the network anyway, and a service worker brings cache bugs with no product benefit today. Offline behaviour would be its own delivery if you ever want it. The other option is a full service worker now, using `vite-plugin-pwa`.

**4. What counts as screenshot proof?** I recommend a Playwright `toHaveScreenshot` assertion whose baseline PNG is committed next to the test and runs inside `npm run verify`. "Screenshot matches" then becomes a mechanical check, which is what "Done when" asks for. The downside is that baselines depend on the machine's fonts; that is fine for one developer and would matter only if CI arrived. The other option is to save the PNGs as proof files without checking them against a baseline.

**Choices I'd make on my own unless you object:**
- **Node:** version 24 or later declared in `engines` (you have 26).
- **Commands:** `npm run dev` runs Vite and the server together, with Vite forwarding `/api` to the server. Having the server serve the built client in one process is left to `deploy`.
- **`lib/result.ts`:** not created yet. It moves to `lib/` on its second use, as docs/01 says, so the health slice would keep its `Result` locally.
- **SQLite file:** `data/clinic.sqlite`, with `data/` in `.gitignore`.

**Separate from `skeleton`, noticed in passing:** docs/06 milestone 2 includes `absences`, but docs/00 says nothing about absences (not in Mechanics, Rules or Open decisions), and docs/03 has no term for them. Before `/propose absences`, docs/00 needs a line on it. I'm not changing it now.

Answer 1 to 4 (a plain "yes" takes all my recommendations) and I'll write `work/skeleton.md` and mark the line `[>]` in docs/06.
````

The brief answers none of these, so the answer was its rule, word for word:[^propose-run]

```markdown
Your call. Say what you chose and why.
```

The agent wrote the page, marked the line `[>]`, said what it chose and why, and ended its reply with the kit's new ending:[^propose-run]

```markdown
**Before `/apply`, read the page and question it:**
- Can each Behaviour line be checked, as a test or by hand?
- Is the Contract exact? The `schema_migration` columns and the `NNNN-<name>.sql` file naming are the parts that would cost a migration to change later.
- Does Out of scope name something you assumed was in, such as offline use or serving the built app from one process?
- Do you disagree with any of the choices above?

Ask for every correction here, in this conversation. When the page is right, open a fresh session and type `/apply skeleton`.
```

This is the page as it first wrote it, `work/skeleton.md`:[^propose-run]

````markdown
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
````

Every recommendation of the round is on the page as a decision, and the page reads as finished: that is what the next section questions.

## Read the page before `/apply`

The page is the record of what the agent understood, and it is what `/apply` will build: a fresh session reads the page and nothing of this conversation.
It is written to be read by a person, interpreted and completed, not generated and applied in the same breath.[^focus-kit-propose]
Read it before `/apply`, and cover every hole by asking the agent, never by editing the page by hand ([chapter 6](06-the-documents.md)): the agent writes the fix where it belongs, on the page and in any document it touches.

The cost decides when to read it.
A hole found on the page costs one turn of conversation; a hole found after `/apply` costs another `/apply`, the most expensive command.[^focus-kit-propose]
In my own usage, as Claude Code's `/usage` reported it, `/apply` took 32% and `/propose` 16% over the last 24 hours, and 47% and 14% over the last 7 days.[^claude-usage]
The figures are approximate and cover all my projects together, but the ratio is what matters: `/apply` costs from twice to more than three times what `/propose` does.

Ask the page these questions:

* Can each Behaviour line become a test or a check?
* Is the Contract exact, or "none" on purpose?
* Does Out of scope name what you assumed was in?
* Is Done when mechanical, a list a machine or a person can tick?
* Did the agent decide something you would have decided otherwise? Read its "your call" choices first.

The first page of `skeleton` read well, and that is the trap: an agent's text reads as right even when it is wrong, and you are the one who validates it ([chapter 6](06-the-documents.md)).
I had a second agent read it against the clinic's documents, the one running this book's `/apply`; it listed the holes it found, and I checked each one against the documents and sent the list as it was.[^propose-run]
The kit asks for every correction in the same conversation; I sent them in a fresh session instead, typing `/propose skeleton` with the list after the slug.
It worked because `/propose` reads `work/` first and found the page; what that session did not have was the first conversation's reasoning behind each recommendation.
The request, whole:[^propose-run]

```markdown
1. Import check nobody asked for. The agent added "npm run verify fails when client code imports a *.server.ts file". The clinic's docs/05 §7 says a new check has to name an error that actually happened. The agent only says "without a check the rule relies on memory alone", and it doesn't say which tool would do the check.
2. Icons with no content. The manifest asks for 192 and 512 PNG icons, but nothing says what they show or where they come from, so /apply would invent them.
3. Screenshot baseline. The Visual reference only says "Plain, clean default styling", and a toHaveScreenshot baseline is tied to one machine's fonts. The agent itself admits that.
4. Migration test folder. The migration tests need a migrations folder, but the page ships the real folder empty and doesn't say the runner takes the folder as a parameter.
```

The first hole is a rule of the clinic's own docs/05, "What this process does not have": a new check enters only when it names an error that happened.
The agent asked me about the manifest and about the screenshot, each with its options and its recommendation first, and I took both recommendations, "Drop manifest (Recommended)" and "Proof file, no baseline (Recommended)".[^propose-run]
It also took a choice on its own and said so: the migration runner and the health page both return a `Result`, so it moved `Result` to `src/lib/result.ts` in this delivery, as docs/01 asks on its second use.
This is the diff from the first page to the reviewed one:[^propose-run]

````diff
--- a/work/skeleton.md
+++ b/work/skeleton.md
@@ -11,17 +11,15 @@
 * While the answer is on its way, the page shows "Checking the server".
 * When the server does not answer, or answers with an error, the page shows
   "Server: unreachable" instead of a blank page or a crash.
-* At start, the server creates the SQLite file if it is missing, applies
-  every migration not applied yet, in file name order, and records each one.
+* At start, the server creates the `data/` folder and the SQLite file if they
+  are missing, applies every migration not applied yet, in file name order,
+  and records each one.
 * Starting the server a second time applies no migration.
 * A migration that fails is not recorded, leaves the database as it was
-  before that file, and stops the start with a message naming the file.
+  before that file, and stops the start with exit code 1 and a message
+  naming the file.
 * `npm run verify` runs typecheck, lint, the Vitest tests, the Playwright
   tests and the build, and ends with exit code 0.
-* `npm run verify` fails when a file that is not server code imports a
-  `*.server.ts` file (ADR-0002).
-* The page carries a web manifest, so a phone browser offers "Add to home
-  screen" with the name "Clinic" and the app's icon.
 
 **Contract.**
 
@@ -32,8 +30,8 @@
 200  { "status": "ok" }
 ```
 
-Table, created by the migration runner itself before it reads
-`src/server/migrations/`, not by a migration file:
+Table, created by the migration runner itself before it reads the folder,
+not by a migration file:
 
 ```sql
 CREATE TABLE IF NOT EXISTS schema_migration (
@@ -42,10 +40,27 @@
 );
 ```
 
-Migrations: files `src/server/migrations/NNNN-<name>.sql`, four digits, applied
-in file name order, each in its own transaction together with its
-`schema_migration` row. This delivery ships the folder empty.
+Migrations: files `NNNN-<name>.sql`, four digits, applied in file name order,
+each in its own transaction together with its `schema_migration` row. Files
+not matching the pattern are ignored. The real folder is
+`src/server/migrations/`; this delivery ships it empty.
 
+Migration runner, `src/server/migrate.server.ts`. It takes the folder as a
+parameter, so tests pass a temporary folder of fixture files and the server
+start passes `src/server/migrations/`:
+
+```ts
+function migrate(db: DatabaseSync, folder: string): Result<string[], MigrationFailed>
+// ok: the file names applied in this call, in order; [] when none
+
+type MigrationFailed = { code: "MigrationFailed"; file: string; message: string }
+// file: the file name that failed; message: the SQLite error text
+```
+
+`Result`, in `src/lib/result.ts`, as docs/01 defines it. First use: the
+health `api.ts`; second use: `migrate`. That second use is why it moves to
+`lib/` in this delivery.
+
 Environment variables of the server:
 
 | Name | Default | Meaning |
@@ -55,9 +70,6 @@
 
 In development, Vite serves the client and forwards `/api/*` to the server.
 
-Web manifest: `name` "Clinic", `short_name` "Clinic", `start_url` "/",
-`display` "standalone", icons 192×192 and 512×512 PNG.
-
 Node: `engines` `>=24`.
 
 **States.**
@@ -67,32 +79,46 @@
 * Error: "Server: unreachable".
 * Offline: same as error; there is no service worker.
 
-**Visual reference.** No design file. Plain, clean default styling. One
-client screen at phone width (390×844).
+**Visual reference.** No design file. One client screen at phone width
+(390×844). Plain, clean default styling, which here means the `system-ui`
+font, 16px padding on each side, the heading and the status line
+left-aligned, and no colours beyond the browser defaults. The proof is a
+screenshot you look at, not a pixel baseline.
 
 **Out of scope.**
 
+* Web manifest, icons and "Add to home screen": the name and the icon
+  belong to the clinic, which exists only after `clinic-setup`; it gets its
+  own delivery, `install`.
 * Service worker and offline use: booking needs the network; its own
   delivery if ever wanted.
+* An automatic check that client code does not import `*.server.ts`: no
+  such import has happened yet (docs/05 §7). The rule lives in docs/01 and
+  ADR-0002 until one does.
+* A `toHaveScreenshot` pixel baseline: without a design file it would only
+  freeze whatever was built, and it breaks with the machine's fonts.
 * The server serving the built client in one process: `deploy` needs it,
   `deploy` builds it.
 * The clinic's real name in the heading: it exists only after
   `clinic-setup`.
 * Any business table, sign-in or session: `clinic-setup`.
-* `src/lib/result.ts`: `Result` lives in the health slice until a second
-  feature uses it (docs/01); `clinic-setup` is expected to be that second
-  use.
 * CI: one developer, one machine; `npm run verify` is the gate.
 
 **Done when.**
 
-* [ ] Repository tests of the migration runner pass against a temporary
-      SQLite file: applies in order, records, skips applied ones, rolls back
-      and names a failing file.
-* [ ] Playwright tests of the three page states pass at 390×844, the "ok"
-      state with a `toHaveScreenshot` baseline committed next to the test.
-* [ ] `npm run verify` is green, and fails on a deliberate client import of
-      a `*.server.ts` file (checked once, then removed).
+* [ ] Vitest tests of `migrate` pass, each against an in-memory SQLite and
+      a temporary folder of fixture `.sql` files: applies in file name
+      order, records each file, skips applied ones, ignores files not
+      matching the pattern, and on a failing file rolls it back, leaves it
+      unrecorded and returns `MigrationFailed` naming it.
+* [ ] One Vitest test, against a temporary directory, shows the server's
+      database opening creates the missing folder and SQLite file.
+* [ ] `migrate` against the real `src/server/migrations/` returns `[]`.
+* [ ] Playwright tests of the three page states pass at 390×844, asserting
+      the texts of Behaviour.
+* [ ] A screenshot of the "ok" state at 390×844 is saved once, as proof,
+      to `work/done/skeleton-390x844.png`; it is not part of `npm run verify`.
+* [ ] `npm run verify` is green.
 * [ ] `npm run dev` leaves client and server running locally, with the
       SQLite file created.
 * [ ] docs/02 lists `GET /api/health` and `schema_migration`; docs/01 and
````

Each hole closed where `/apply` would have had to guess: the import check and the manifest left, with their reasons in Out of scope; the runner got an exact signature and error in the Contract; and Done when traded the pixel baseline for tests `/apply` can run and a screenshot you look at.

## When it does not fit

A scope that does not fit one page is two deliveries: `/propose` says so, proposes the split and writes only the first page, and the second becomes a line in the queue, where it belongs ([chapter 9](09-queue-and-milestones.md)).[^focus-kit-propose]
This book split one on chapter 3, which compares Spec Kit, OpenSpec and focus-kit by what each writes for the same feature.
The measured run of the tools, with its brief, its pinned versions and its counts, would not fit on the chapter's page, so it became a delivery of its own, `spec-driven-run`.
This is the diff of this book's docs/06 in its commit:[^book-spec-driven-run]

````diff
diff --git a/docs/06-Queue.md b/docs/06-Queue.md
index 2216d99..0f6ead6 100644
--- a/docs/06-Queue.md
+++ b/docs/06-Queue.md
@@ -25,6 +25,7 @@ When this milestone closes, a reader who has never followed a process knows why
 
 ```
 [x] how-agents-see         Chapter 2: statelessness, context window, context rot, fresh sessions, from primary sources
+[x] spec-driven-run        SpecKit, OpenSpec and focus-kit run on the same feature and brief; files, lines and words counted and committed for chapter 3
 [ ] spec-driven            Chapter 3: SDD, what SpecKit and OpenSpec got right and where they weighed too much
 [ ] birth-of-focus-kit     Chapter 4: the Ninjobs restart, and the kit that grew and became one file again
 ```
````

The new line sits before `spec-driven`, the chapter that needs its numbers, already `[x]` because its page and its build landed in one commit.
The review of `skeleton` did the same on a small scale: the manifest left the page and became the line `install` in the clinic's milestone 2, before `deploy`, at `[ ]`.[^propose-run]

## Key points

* `/propose <slug>` turns one queue line into one page: it reads the documents and `work/`, asks only where no document closes a reading, recommendation first, and writes the page and the mark `[>]`, never code, migration, test or configuration; a slug the queue lacks gets its line.
* The Contract is the one exact section: a wrong screen is fixed in a session, a wrong column is a migration.
* Read the page before `/apply`: it is what the agent understood and what will be built; cover each hole by asking the agent, never by hand, because a hole on the page costs a turn and after `/apply` it costs another `/apply`.
* The page and its build are one unit of work that reverts in one step: one commit on trunk, so the page waits uncommitted; one merge of the branch otherwise.
* A scope that does not fit one page is two deliveries: the first gets the page, the second a line where it belongs.

## Exercises

These exercises use the clinic, by conversation with the agent, never by hand.

### Exercise 10.1

Check out `book-v1/brainstorm` on a branch of your own, update the kit as in chapter 5, run `/propose skeleton` with the brief of this chapter, and compare your page with the one in this chapter.
Which differences are the agent's "your call" choices?

### Exercise 10.2

Review your page with the questions of "Read the page before `/apply`" before any `/apply`.
Ask the agent to cover each hole, and read the diff.

### Exercise 10.3

Ask `/propose` for `book-appointment` and `cancel-appointment` as one delivery.
Does it propose a split, and where does the second line go?

[^focus-kit-propose]: J.C. Ködel, "focus-kit", `SETUP.md` §3.3, the file of `/propose`, at commit e7607c58ad38e70e3496518a58d4237612e21ebc, installed in the guided project at commit 3f0b47c. https://github.com/JCKodel/focus-kit/blob/e7607c58ad38e70e3496518a58d4237612e21ebc/SETUP.md
[^focus-kit-unit-of-work]: J.C. Ködel, "focus-kit", `SETUP.md` §Choices, the git answers, at commit e7607c58ad38e70e3496518a58d4237612e21ebc: a delivery's page and build are one change that reverts in one step. https://github.com/JCKodel/focus-kit/blob/e7607c58ad38e70e3496518a58d4237612e21ebc/SETUP.md
[^propose-run]: This book's `/propose` run on the guided project, 2026-09-28, with Claude Code 2.1.283 and the model `claude-opus-5-5`, from commit 3f0b47c: the brief, the commands, every turn's output, the questions and the answer, the first page, the review and its diff. https://github.com/JCKodel/focus-kit-book/blob/main/work/done/propose-run/README.md
[^claude-usage]: Claude Code `/usage`, read by the author on 2026-09-28, local sessions on one machine, all projects together; `work/done/propose-run/usage.txt`. The tool calls its figures approximate; the author read it in three projects and got the same figures, so it is not a measure of one project. https://github.com/JCKodel/focus-kit-book/blob/main/work/done/propose-run/usage.txt
[^book-spec-driven-run]: J.C. Ködel, "One Page at a Time", commit 53109f372125e8aeda200bb2e5bbd1ad7bcc5d61, which recorded chapter 3's run as a delivery of its own. https://github.com/JCKodel/focus-kit-book/commit/53109f372125e8aeda200bb2e5bbd1ad7bcc5d61
[^claude-code-plan-mode]: Anthropic, "Common workflows", Claude Code documentation, section "Plan before editing", accessed 2026-09-28. https://code.claude.com/docs/en/common-workflows#plan-before-editing
