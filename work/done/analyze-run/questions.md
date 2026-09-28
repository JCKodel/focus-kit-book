# Questions and answers

The round is the agent's message as it ended the turn, whole, then the answer given in the next turn, whole. The answer is sections of `brief.md` word for word. After it come the two corrections the author's review asked for, each the request as sent, whole, and the agent's reply as it ended the turn. The agent used no question form: headless mode offers none, so it asked in text.

## The round: four subjects

Turn 1, the agent:

````markdown
I've read enough to ask my questions. The code already answers most things. One thing to flag first: a command that combined `find` and `xargs cat` needed approval and was denied, because this session has no way to answer a permission prompt. I read the files it covered one at a time instead, so nothing is missing.

**What I found (you don't need to confirm this):**
- **The product:** a Next.js 16 app, a rewrite of the old Rails CLAHub (DamageLabs/clahub, running at cla-hub.io). It uses Prisma 7 with SQLite, Auth.js with separate GitHub sign-in for owners and contributors, and a GitHub App that runs the PR checks. There is also a REST API at `/api/v1`, and it can be self-hosted with Docker.
- **Where the rules live:** the business rules are in `src/lib/cla-check.ts`, the server actions in `src/lib/actions/`, and validation in `src/lib/schemas/`. The code is organized by technical layer, not by feature.
- **How errors travel:** server actions return an `ActionResult` (success or failure as a value). API routes return a structured JSON error through `apiError()`. `requireOwner` is the exception: it throws.
- **Verify command:** `npm run lint && npx tsc --noEmit && npm test && npm run build`, the same checks CI runs. CI also runs the Playwright end-to-end tests.
- **The existing `docs/*.md` files** are user guides, and some of them are shown on the site. The site only shows files from a fixed list, so adding docs/00 to 06 next to them will not publish them.
- **Where the code contradicts itself:** these go into the documents as open questions; I won't ask you to settle them now.
  - `.prettierrc` asks for single quotes, but the code uses double quotes, and CI doesn't check formatting.
  - CONTRIBUTING mentions Biome, which isn't installed.
  - The PRD says no OAuth tokens are stored for contributors. The code stores tokens for owners only, which is consistent, but the PRD also calls for a background job, and re-checking PRs is just a promise nobody waits for.
  - The PRD asks for API and component tests, but those folders are empty.
  - `hono` is a direct dependency that no source file imports.

**Four questions. Each starts with my recommendation:**

1. **Documentation language:** English, since the README is in English. Do you want a different one?

2. **FOCUS:** I recommend **neither**. The documents would describe the current conventions as they are: Next.js App Router, `lib/` organized by layer, and errors returned as values in actions and the API. The other two options are:
   - **the two principles only:** new features go into feature folders, and `throw` is never used for control flow. The layer-based structure stays as it is, and new work moves toward feature folders over time.
   - **FOCUS whole:** View, Orchestrator, Use Case and Repository in separate pieces. That would mean a large refactor.

3. **Git:** I recommend **a branch per delivery**, because that's what the repo already does: `feat/`, `fix/` and similar branches, a PR into `main`, merged by a person. The alternatives are **trunk** or **a worktree per delivery**. In all three, I never commit or merge.

4. **First milestone:** where do its 3 to 8 deliveries come from? Options:
   - **(a)** I draft them from the contradictions above and the PRD items the code doesn't do yet: webhook delivery log, component and API tests, formatting enforcement, background re-check.
   - **(b)** You tell me: GitHub issues, a list, or a goal.
   - The branch name `book` makes me think you may have something specific in mind.

Once you answer, I'll show you the full diff before writing anything.
````

Turn 2, the answer. The brief's sections Documentation language, Choices and First milestone; the section Purpose and audience was not asked, because the agent read the purpose from the README.

````markdown
## Documentation language
English.

## Choices
FOCUS: your call. Git: your call.

## First milestone
The three open issues upstream, one delivery each, in this order:
https://github.com/DamageLabs/clahub/issues/270
https://github.com/DamageLabs/clahub/issues/274
https://github.com/DamageLabs/clahub/issues/268
````

Turn 2, the agent, after writing the documents:

````markdown
I've written the documents; no code changed. I couldn't read the three issues: `gh` and fetching the issue pages both needed approval, and this session had no way to give it. So the queue names each issue by number and link only, and `/propose` will read the issue text.

**Your two "your call" choices:**
- **FOCUS: neither.** The existing layout stays as it is: code grouped by layer under `src/lib`, and errors returned as values (`ActionResult` in actions, `apiError` in the API). Restructuring would touch every file and users would see no difference. This is recorded in ADR-0009.
- **Git: a branch per delivery**, named `<type>/<slug>` from `main`. That matches how the repo already works. This is ADR-0010. I stage and suggest the commit message; you commit, push and merge.

**Files written:** `docs/00-Product.md` to `docs/06-Queue.md`, ten ADRs in `docs/adr/`, `AGENTS.md`, `CLAUDE.md` (just `@AGENTS.md`), and `work/done/.gitkeep`. `GEMINI.md` and `.agents/rules/focus-kit.md` already pointed to `AGENTS.md`, so I left them alone.

**Open questions, recorded in the docs for you to settle later:**
- **Email trust:** the PRD says only verified emails are used to match signers. The code actually matches people by the email on their commits and grants corporate coverage by that email's domain. Anyone can set that email, so this is the one I'd look at first.
- **Background re-check:** after someone signs, the re-check of open PRs runs without anything waiting for it, instead of as a background job as the PRD asks. A serverless host may stop it early.
- **Unbuilt PRD items:** the webhook delivery log and the component/API tests are missing, and no 80% coverage is measured.
- **Formatting:** the Prettier config asks for single quotes but the code uses double quotes, CI doesn't check formatting, and CONTRIBUTING mentions Biome, which isn't installed.
- **Unused dependency:** `hono` is listed as a dependency but no source file imports it.
- **Old planning files:** whether to keep `PRD.md`, `Analysis.md` and `Old-Issues.md` as history now that the new docs exist.

**Queue (`docs/06-Queue.md`), Milestone 1: upstream open issues**
```
[ ] issue-270    resolve upstream issue #270
[ ] issue-274    resolve upstream issue #274
[ ] issue-268    resolve upstream issue #268
```

Next step: in a fresh session, run `/propose issue-270`. If that session also can't fetch GitHub, paste the issue text into it.
````

## Correction 1: the queue from the issues

Turn 3, the author's request, with `--allowedTools "Bash(gh issue view:*)"` added to the command:

````markdown
Read the three issues with gh issue view and rewrite the milestone and its lines from them.
````

Turn 3, the agent:

````markdown
I read the three issues and rewrote Milestone 1 in `docs/06-Queue.md` from them, keeping your order:

```
[ ] resign-on-version-bump       owners can require re-signing when a new CLA version is published, with an optional grace period (#270)
[ ] custom-email-templates       owners customize the subject and body of the new-signature email with variables and a preview (#274)
[ ] gdpr-export-and-deletion     users download their data as JSON and delete their account (#268)
```

The milestone paragraph now says what is true when it closes: re-signing is enforced in PR checks, the signing email uses the owner's own template with the default as fallback, and users can export their data and delete their account.

Some parts of the issues conflict with the documented rules or with each other. These are for `/propose` to settle with you:

- **#268 conflicts with two non-negotiables.** It asks to delete the user's audit logs along with their signatures, but ADR-0005 says every change is kept in the audit log and signatures are revoked, not deleted. It also asks to revoke the user's GitHub token, and only owners have one stored.
- **#274 has two open points.** It suggests Handlebars or Mustache, which would be a new dependency. It also mentions templates for revocation and version-bump emails, but only the new-signature email exists today. That makes it partly depend on #270.
- **#270 needs one choice.** The switch for requiring re-signing could go on the agreement or on each version, and the choice affects how old signatures are treated.

Next step: `/propose resign-on-version-bump` in a fresh session.
````

## Correction 2: the environment file

Turn 4, the author's request:

````markdown
docs/01 says local setup uses .env.local. Check that against prisma.config.ts and the README, and correct docs/01; where they disagree, record an open question.
````

Turn 4, the agent:

````markdown
docs/01 was only half right. The app reads `.env.local`, but Prisma's command-line tool doesn't. I rewrote the Local line in the Environments section of `docs/01-Architecture.md` and added an **Open questions** section at the end of the file. I changed no code or guides.

**What the code does:**
- **The app** (`npm run dev`, `build`, `start`) reads `.env.local`.
- **Prisma's command-line tool** (`db:push`, `migrate`, `db:seed`, `studio`) reads only `.env`. Both `prisma.config.ts` and `prisma/seed.ts` load variables with `import "dotenv/config"`, which ignores `.env.local`.

**Open questions recorded:**
1. **Which file Prisma reads.** The README and `docs/getting-started.md` say to create `.env.local` and then run `db:push`. With only `.env.local`, Prisma never sees `DATABASE_URL`, so that step fails unless the variable is also in `.env` or set in the shell. Either the guides are wrong, or the Prisma config should also load `.env.local`.
2. **`APP_URL` is documented but never read.** The README, both example env files and `docs/configuration.md` list it as required. The code reads `NEXT_PUBLIC_APP_URL` for check-run and CONTRIBUTING.md links, and `NEXTAUTH_URL` for links in emails. So a self-hoster who follows the guides gets check runs that link to `http://localhost:3000`.
3. **Local end-to-end tests can wipe the development database.** Playwright loads `.env.local` before `.env.test`, and the value loaded first wins. Running `npm run test:e2e` with no dev server running therefore resets and reseeds the database named in `.env.local`, not `test.db`.

Question 2 looks like a real bug for anyone self-hosting. If you want it fixed, I'd add it to the queue as its own delivery.
````
