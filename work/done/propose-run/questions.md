# Questions and answers

The round is the agent's message as it ended the turn, whole, then the answer given in the next turn, whole, then the agent's message as it ended that turn, whole. The answer is the brief's rule, word for word: the agent read the slug from the command, so the section Delivery was not asked, and every question it asked is one the brief does not answer. The agent used no question form: headless mode offers none, so it asked in text.

## The round

Turn 1, the agent:

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

Turn 2, the answer. The brief's section Rule for a question the brief does not answer:

````markdown
Your call. Say what you chose and why.
````

Turn 2, the agent, after writing `work/skeleton.md` and marking the line in docs/06:

````markdown
I wrote the page at `work/skeleton.md` and changed `skeleton` from `[ ]` to `[>]` in docs/06. I staged and committed nothing, and there's no branch because the project works on `main` (ADR-0003).

**What I chose and why:**

1. **First screen: a page that asks the server `GET /api/health` and shows "Server: ok".** The first screenshot then proves both halves of the app work together, not just the client. It also gives the page real loading and error states ("Checking the server", "Server: unreachable") that Playwright can test. The heading says "Clinic" because the clinic's name only exists after `clinic-setup`.
2. **The database and migration runner go in `skeleton`, not `clinic-setup`.** `clinic-setup` is already the heaviest delivery in milestone 1: setup command, owner, sessions, password hashing and sign-in screens. The runner needs one small table of its own, `schema_migration`, which is exact on the page. Each migration runs in its own transaction, so a failed one leaves nothing behind and the server stops with the file's name.
3. **A web manifest and icons, no service worker.** Phones can add the app to the home screen, which is what "PWA" means in docs/01. Booking needs the network anyway, and a service worker would bring cache bugs with nothing gained today.
4. **The screenshot is a Playwright check inside `npm run verify`,** with the reference image committed next to the test. "Screenshot matches" in Done when then becomes something a machine checks. The only cost is that a second machine or a CI server would need its own reference image.

**Smaller calls:**
- **Commands:** `npm run dev` starts the client and the server together.
- **Serving the built client from one process:** left to `deploy`.
- **Settings:** `PORT` defaults to 3000, and `DATABASE_PATH` to `data/clinic.sqlite`, with `data/` kept out of git.
- **Node:** version 24 or later.
- **`Result` type:** stays inside the health feature until a second feature needs it (docs/01).

**One addition you didn't ask for:** `npm run verify` fails when client code imports a `*.server.ts` file. ADR-0002 forbids that import, and without a check the rule relies on memory alone.

**Before `/apply`, read the page and question it:**
- Can each Behaviour line be checked, as a test or by hand?
- Is the Contract exact? The `schema_migration` columns and the `NNNN-<name>.sql` file naming are the parts that would cost a migration to change later.
- Does Out of scope name something you assumed was in, such as offline use or serving the built app from one process?
- Do you disagree with any of the choices above?

Ask for every correction here, in this conversation. When the page is right, open a fresh session and type `/apply skeleton`.

Still open from before: docs/06 lists `absences` for milestone 2, but docs/00 never mentions absences. It needs a decision in docs/00 before anyone proposes that delivery.
````

The page as first written is `skeleton-first.md`. The author's review is in `review.md`.
