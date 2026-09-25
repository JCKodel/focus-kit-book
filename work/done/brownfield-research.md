# brownfield-research

**Objective.** The author has three to five open-source TypeScript web apps compared on measured, sourced criteria, has picked one, and knows the exact commit that chapter 8 will cite as `JCKodel/<name>` at tag `book-v1`.

**Behaviour.**

* /apply searches GitHub for full-stack TypeScript web apps and records every query it ran and how many results each returned.
* Three to five candidates reach the table. Each one is cloned outside the repository and measured at a recorded upstream commit (SHA and date). Its test suite is run and the app is started on this machine.
* Every number in the table names its source: the tool and its version, the SHA, and the command that was run.
* A project that was looked at and dropped gets one line on the page with the criterion it failed.
* When fewer than three candidates meet every criterion, /apply loosens the criteria in this order and stops as soon as three qualify: (1) the line band widens to 3,000 to 30,000; (2) "full-stack web app" becomes "back end with a local database and tests". License, "no paid service" and "TypeScript" never loosen. The page records what was loosened.
* /apply recommends one candidate in two or three sentences, then asks the author to pick. The author's pick, with its SHA, closes OD-1 in this delivery.
* The agent does not fork, tag or push (docs/05 §5). The fork and the tag are the author's items, done after the commit with the commands below.

**Contract.**

Criteria, how each is measured (ADR-0009, narrowed by this delivery):

| Criterion | Passes when | Measured by |
|---|---|---|
| License | MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause or ISC, in a `LICENSE` file at the root | the file at the SHA |
| Stack | TypeScript is at least 80% of the code lines of programming languages; front end and back end in the same repository; a database that runs locally (SQLite, or Postgres or MySQL in a container) | `cloc` at the SHA |
| Size | 5,000 to 20,000 TypeScript code lines, tests excluded | `cloc --vcs=git`, language TypeScript (`.ts`, `.tsx`), excluding `node_modules/`, `dist/`, `build/`, lockfiles, files under a folder named `generated` or starting with a "generated" header, and test files |
| Tests | a test script exists and runs to completion; the pass and fail counts are recorded (failures do not disqualify, a suite that cannot run does) | the project's own test command, run at the SHA |
| No paid service | installs, starts and passes its tests with no account, API key or paid service; free containers are allowed | the start and test commands, run at the SHA |
| Next deliveries | at least three open issues upstream that each read as one delivery (one page) | the issue URLs, listed |

Test files are `*.test.ts(x)`, `*.spec.ts(x)` and anything under `__tests__/`, `test/`, `tests/` or `e2e/`. Their TypeScript code lines go in their own column.

Comparison table on this page, under "What happened", one row per candidate, with these columns in this order:

```
Candidate (owner/repo, URL) | SHA and date | License | TS code lines | TS test lines | TS share | Front / back / database | Test command and result | Start command | Issues as deliveries (3 URLs) | Notes
```

Above the table: the date of the measurement and the `cloc` and Node versions used. `cloc` runs from a scratch folder or a download and is never installed in the repository.

Files /apply changes after the author picks:

```
work/brownfield-research.md          the table, the recommendation, the pick; then moved to work/done/
docs/adr/ADR-0009-brownfield-by-research.md   an "Amendment" section dated at the pick: stack narrowed to TypeScript full-stack (docs/00 Non-goals, ADR-0008); what was loosened, if anything; the chosen project, upstream URL, SHA, fork JCKodel/<name>, tag book-v1
docs/00-Product.md                   OD-1 closed, pointing to the amendment; the Mechanics line on the brownfield project names it
docs/03-Domain.md                    brownfield project row, Identifier: `JCKodel/<name>@book-v1`
docs/01-Architecture.md              next to the guided project's line: the brownfield code lives in the fork, the book quotes it at `book-v1`, never copies it
docs/06-Queue.md                     brownfield-research [x]
```

`<name>` is the upstream repository's name, unchanged. `book-v1` is the only freeze: the fork's branches may move, the tag does not. Updating chapter 8 means a new tag (`book-v2`) on purpose (ADR-0009).

The author's commands after the commit (written here and in the commit body; the agent never runs them):

```
gh repo fork <owner>/<name> --clone --default-branch-only
git -C <name> tag -a book-v1 <sha> -m "Frozen for One Page at a Time, chapter 8"
git -C <name> push origin book-v1
```

**Out of scope.**

* Chapter 8 and running `/analyze` on the fork: that is the `analyze` delivery.
* Any change inside the fork beyond the tag: the book shows the project as upstream left it.
* Copying upstream issues into the fork: the chapter cites them by upstream URL.
* Stacks other than TypeScript: the book shows TypeScript only (docs/00 Non-goals).
* The guided project: `guided-project-repo` (OD-2).

**Done when.**

* [x] The page lists every search query with its result count, and one line per dropped project with the criterion it failed.
* [x] Three to five candidate rows, each with every column filled, the SHA and date, and the test and start commands actually run.
* [x] Any loosening of the criteria is recorded, in the fixed order.
* [x] Recommendation written; the author's pick recorded with its SHA.
* [x] ADR-0009 amended; docs/00 OD-1 closed; docs/03, docs/01 and docs/06 updated as the contract says.
* [x] `make verify` green; no clone, `cloc` or `node_modules` left inside the repository.

The two Author items stay unchecked when /apply stages. The author ticks them in a follow-up commit, as `pages-and-release` did.

* [ ] Author, after the commit: `JCKodel/<name>` forked; tag `book-v1` on the recorded SHA pushed; the tag URL recorded here.
* [ ] Author: `git -C <name> rev-parse book-v1^{commit}` prints the SHA in the ADR-0009 amendment.

**What happened.**

Searches, with `gh api -X GET search/repositories -f q=<query> -f sort=stars` on 2026-09-25, and the `total_count` each returned:

| Query | Results |
|---|---|
| `language:TypeScript topic:fullstack sqlite license:mit stars:>50` | 2 |
| `language:TypeScript sqlite prisma "web app" stars:>100 pushed:>2025-06-01` | 1 |
| `language:TypeScript topic:self-hosted sqlite stars:>200 pushed:>2025-06-01` | 11 |
| `language:TypeScript topic:self-hosted stars:>300 pushed:>2026-03-01 license:mit` | 85 |
| `language:TypeScript topic:sqlite topic:react stars:>100 pushed:>2026-01-01` | 27 |
| `language:TypeScript topic:prisma topic:sqlite stars:>50 pushed:>2026-01-01` | 6 |
| `language:TypeScript topic:drizzle-orm topic:sqlite stars:>50 pushed:>2026-01-01` | 12 |
| `language:TypeScript topic:express topic:react topic:sqlite stars:>20` | 3 |
| `language:TypeScript topic:vitest topic:sqlite stars:>20 pushed:>2026-01-01` | 0 |
| `language:TypeScript "self-hosted" sqlite vitest in:readme stars:>100 pushed:>2026-03-01` | 47 |
| `language:TypeScript topic:self-hosted sqlite stars:>50 size:500..15000 pushed:>2026-01-01` | 13 |
| `language:TypeScript topic:sqlite topic:fullstack stars:>10` | 3 |
| `language:TypeScript topic:sqlite topic:express stars:>30 pushed:>2025-06-01` | 4 |
| `language:TypeScript topic:react topic:fastify stars:>30 pushed:>2025-06-01` | 20 |

Twelve projects came from the agent's knowledge of the field rather than a query: `epicweb-dev/epic-stack`, `stonith404/pingvin-share`, `chrisvel/tududi`, `chibisafe/chibisafe`, `CorentinTh/enclosed`, `spliit-app/spliit`, `diced/zipline`, `sct/overseerr`, `umami-software/umami`, `ether/etherpad-lite`, `logchimp/logchimp`, `thedevs-network/kutt`.

Dropped after cloning and measuring (TS lines are code lines, tests excluded):

* `Cawlumm/lyftr`: Stack, the back end is Go (TypeScript 70.5%).
* `Kobii-git/rackpad`: Size, 176,413.
* `goniszewski/grimoire`: Size, 40,157.
* `Gsync/jobsync`: Size, 56,786.
* `Manak-hash/LinkBreeze`: Size, 29,850.
* `VityaSchel/lufin`: Next deliveries, a read-only mirror with GitHub issues disabled.
* `lantingzhang1119/cohort-harbor`: Size, 44,086.
* `rocambille/start-express-react`: Size, 2,791 (a starter).
* `dev-xo/remix-saas`: Next deliveries, no open issue.
* `pawelmalak/flame`: Stack, TypeScript 75.6%.
* `Sharkord/sharkord`: Size, 61,602.
* `denho/faved`: Stack, the back end is PHP (TypeScript 74.6%).
* `franklioxygen/MyTube`: Size, 133,930.
* `usekaneo/kaneo`: Size, 118,946.
* `builderz-labs/mission-control`: Size, 88,608.
* `pheralb/slug`: License, GPL-3.0.
* `alan345/AI-Fullstack-SaaS-Boilerplate`: Size, 3,478.
* `chibisafe/chibisafe`: Size, 24,062; and no test script.
* `chrisvel/tududi`: Stack, TypeScript 46.6%.
* `CorentinTh/enclosed`: Stack, no database (a key-value store on files or memory, through `unstorage`).
* `spliit-app/spliit`: not measurable here. In band (14,905) and MIT, but Postgres only, and this machine has no container runtime and no Postgres server.
* `diced/zipline`: Size, 41,546.
* `sct/overseerr`: Size, 58,564; and no test script.
* `umami-software/umami`: Size, 99,984.
* `ether/etherpad-lite`: Size, 44,307.
* `logchimp/logchimp`: Stack, TypeScript 68.6% (the front end is Vue).
* `thedevs-network/kutt`: Stack, JavaScript only.
* `kevincardwell/galley`: Size, 20,040; and Next deliveries, no open issue.
* `kocaemre/recon-deck`: Size, 28,605.
* `h0i5/Foursight`: Tests, no test script; and no database.
* `stonith404/pingvin-share`: Size, 28,240; archived.

Three candidates met every criterion, so nothing was loosened.

Measured on 2026-09-25 with `cloc` 2.10 (`cloc-2.10.pl` from the GitHub release, run from a scratch folder, sha256 `bf59272455172108072a0a106379f7509fd4349bdcfd85203bac038ccd286d83`) and Node 26.10.0 with npm 11.19.1.
Node 24.21.0 and 22.23.3 were downloaded from nodejs.org into the same scratch folder, their `SHASUMS256.txt` checked, for the candidates that need them (see Notes).
Every clone is `git clone --depth 1` of the default branch into that scratch folder.
The three `cloc` commands, run at the clone's root:

```
TS code lines   cloc-2.10.pl --vcs=git --exclude-dir=node_modules,dist,build,generated --include-lang=TypeScript --fullpath --not-match-f='(\.(test|spec)\.tsx?$|(^|/)(__tests__|test|tests|e2e)/)'
TS test lines   the same with --match-f instead of --not-match-f
TS share        cloc-2.10.pl --vcs=git --exclude-dir=node_modules,dist,build,generated; TypeScript over TypeScript + JavaScript + Prisma Schema + Bourne Shell
```

Only files whose first five lines say "generated" count as generated: one, clahub's `prisma.config.ts` (12 lines), added to the exclusion for clahub. Lockfiles are JSON or YAML, outside the TypeScript count.

| Candidate (owner/repo, URL) | SHA and date | License | TS code lines | TS test lines | TS share | Front / back / database | Test command and result | Start command | Issues as deliveries (3 URLs) | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| `DamageLabs/clahub`, <https://github.com/DamageLabs/clahub> | `9d1e666e1d30f271aea9640393229a7cbfbd1b62`, 2026-04-13 | MIT (`LICENSE.md`) | 11,902 | 3,049 | 98.8% | Next.js 16 (App Router) pages and API routes / SQLite through Prisma 7 | `npm ci && npx prisma generate && npm test` (Vitest): 25 files, 259 passed, 0 failed | `.env.local` from `.env.test`'s dummy values, `DATABASE_URL=file:./clahub.db npm run db:push`, `npx next dev -p 3101`: `/api/health` answers 200 with the database healthy | <https://github.com/DamageLabs/clahub/issues/270>, <https://github.com/DamageLabs/clahub/issues/274>, <https://github.com/DamageLabs/clahub/issues/268> | Node 24.21.0: `better-sqlite3` 12.6.2 does not compile on Node 26. The README's `npm run db:push` fails as written: `prisma.config.ts` reads `.env`, the README says `.env.local`. Signing in needs a GitHub App and OAuth app (a free GitHub account); install, tests and start need neither. 17 open issues, most written as specs on 2026-02-13. |
| `bhj/KaraokeEternal`, <https://github.com/bhj/KaraokeEternal> | `b209d4a90aee03420eed5c14d0552b56bd7f89c5`, 2026-02-14 | ISC (`LICENSE`) | 11,227 | 54 | 96.7% | React 18 with Redux / Koa 3 / SQLite through `node:sqlite` | `npm ci && npm test` (Vitest): 1 file, 35 passed, 0 failed | `npx tsx server/main.ts -p 3100` (the `dev` script without watch, on a free port): `/` answers 200, "Karaoke Eternal" | <https://github.com/bhj/KaraokeEternal/issues/91>, <https://github.com/bhj/KaraokeEternal/issues/79>, <https://github.com/bhj/KaraokeEternal/issues/93> | Node 26.10.0 (engines `>=24`). One test file, for the media metadata parser: almost no tests. The server writes its database under the user's application support folder, outside the clone. |
| `epicweb-dev/epic-stack`, <https://github.com/epicweb-dev/epic-stack> | `8473afd804b66dba6a23f317908dc35d1535e90d`, 2026-08-29 | MIT (`LICENSE.md`) | 10,219 | 1,467 | 96.5% | React Router 7 / Express 5 / SQLite through Prisma 6 | `npm ci`, `cp .env.example .env`, `npx prisma generate && npx prisma migrate deploy`, `CI=true npm test` (Vitest): 7 files, 27 passed, 0 failed | `npx prisma generate --sql`, `PORT=3102 npm run dev` (mocks on): `/resources/healthcheck` answers 200, `/` "Epic Notes" | <https://github.com/epicweb-dev/epic-stack/issues/1079>, <https://github.com/epicweb-dev/epic-stack/issues/1061>, <https://github.com/epicweb-dev/epic-stack/issues/1060> | Node 22.23.3 (engines `^22.18.0`). A starter template, not an app: its domain is a demo notes app, and its issues are about the template. `npm run setup` also runs `playwright install`, skipped here. |

**Recommendation.** `DamageLabs/clahub`: a real product with a domain `/analyze` can find (agreements, signatures, repositories), 259 passing tests next to 11,902 lines, and 17 open issues written as specs, three of them one page each.
Its setup bug (`.env` against `.env.local`) is the kind of drift between docs and code the chapter can show `/analyze` catching.
KaraokeEternal has almost no tests, and epic-stack is a template with no domain of its own.

**Pick.** The author picked `DamageLabs/clahub` on 2026-09-25, at `9d1e666e1d30f271aea9640393229a7cbfbd1b62`. OD-1 is closed by the ADR-0009 amendment. The fork is `JCKodel/clahub`, the tag `book-v1`. The author's commands after the commit:

```
gh repo fork DamageLabs/clahub --clone --default-branch-only
git -C clahub tag -a book-v1 9d1e666e1d30f271aea9640393229a7cbfbd1b62 -m "Frozen for One Page at a Time, chapter 8"
git -C clahub push origin book-v1
```

**Proof.** No screen: the proof is the runs recorded in the table, each done at the SHA shown, with the commands shown.

**Divergences and decisions.**

* "One line per dropped project" is read as one line per project cloned and measured. Most search results were set aside from the listing alone (a license GitHub reports as copyleft or unknown, an archive, a library, a desktop or AI-agent tool rather than a web app) and are counted in the query table, not listed one by one.

* Two more Node versions than the one named above the table: the contract names one Node, but clahub's `better-sqlite3` does not build on Node 26, and epic-stack declares Node 22. Each was run on the version its setup accepts, and the row says which.
* Start commands use ports 3100 to 3102, not the projects' default 3000, which another local service already held on this machine.
* The scratch folder, the clones, their `node_modules` and databases, the Node downloads and KaraokeEternal's database under the user's application support folder were deleted after the measurements. Nothing of them was inside the repository.
* No new term or rule. The decision is the ADR-0009 amendment.
