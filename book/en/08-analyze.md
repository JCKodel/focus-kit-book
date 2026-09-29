# `/analyze`, an existing project

After this chapter you can run `/analyze` on a project that already exists, with code or without, answer its one round of questions, and check the documents it writes against the project before you commit them.

## What changes from `/brainstorm`

`/analyze` is the command for a repository that already has something in it: code, documents, or both.
It runs like `/brainstorm` ([chapter 7](07-brainstorm.md)): a fresh session, a default with every question, "your call" as a valid answer, and the same documents at the end.
What differs is that it reads before it asks, and its file, `analyze/SKILL.md`, has it read this, in this order:

* the README and any documentation already there;
* the manifests, such as `package.json`;
* the folder tree;
* the entry points;
* the tests, and how they run;
* the CI configuration;
* the last fifty commit subjects;
* any rules file already there (`CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.cursorrules`).

What the project does not have, it skips: on a project with no code there are no manifests, entry points or tests to read, and the documents describe what the files say.
From that it infers the stack, how the code is organized, where the business rules live, how errors travel, the verify command and the environments.
Then it asks one round, of four subjects only:

1. The documentation language. Default: the language of the README.
2. The product's purpose and audience in your words, only when no README says it.
3. FOCUS and the git strategy, the [two choices](06-the-documents.md#the-two-choices) of chapter 6. The default of each is what the code already does, and the agent says what that is.
4. The first milestone: its first deliveries, or where to read them from (issues, a TODO file, a roadmap).

Everything else it decides from what it read and marks as observed: you are not asked what the project already answers.
Where what it read contradicts itself, it records an open question in the document that owns the subject, and does not ask you to settle it now; settling it is a delivery of its own.
A rules file already there does not stay beside `AGENTS.md`: its rules move into `AGENTS.md`, and the file keeps the import line and only what applies to that host.
The documents describe what exists, not what should exist.
It shows the diff before it writes, and it changes no code.

### FOCUS on code without an architecture

On code with no clear architecture the default for FOCUS is "neither", because the code does not do it, and FOCUS whole would mean rewriting it.
There is a way between the two, which you give as your answer: the strangler fig, Martin Fowler's name for a gradual replacement of an old system, after a vine that grows around a tree until it stands on its own.[^strangler-fig]
New code grows beside the old: every new feature is a vertical slice in FOCUS, every part a delivery changes moves into one, and the old code goes away one delivery at a time while the project keeps working.
Answer the FOCUS question with that, for example "FOCUS whole, as a strangler fig: new features and every part a delivery touches become vertical slices; the rest stays until then.", and `/analyze` writes it into docs/01 and an ADR, so every later `/propose` and `/apply` follows it.
In the run on CLAHub the agent offered the same shape for the two principles alone: new work moves toward feature folders over time.[^analyze-run]
Part III teaches FOCUS itself.

## Before you run it

The code says what a project does; it rarely says why, for whom, or what was promised.
On a corporate project that knowledge is in proposals, contracts, emails, meeting transcripts, tickets and slides, and what the agent does not read, it has to guess.
Put everything you have about the project in one folder at the root, `context/`, as it is, with no sorting and no summary.
Keep it apart from `docs/`: `context/` is what the agent reads from, and `docs/` is what it writes.
The command does not look for that folder by name, so say it in the same message, `/analyze Read context/ first, whole.`; that sentence is your instruction, not the kit's.

Whether `context/` is committed is your decision.
Committed, every later session can read it, and everything in it stays in the history for everyone with access to the repository.
Listed in `.gitignore`, it stays on your machine, and later sessions see only what the documents took from it.
Read it for what must not be shared before you choose.

The run on CLAHub had no such folder: an open source project keeps its context in the open, in its README and its issues.

## The project

[CLAHub](https://github.com/DamageLabs/clahub) lets an open source project on GitHub ask its contributors to sign a Contributor License Agreement: the owner writes the agreement, a contributor signs it by signing in with GitHub, and every pull request gets a check that says whether all its commit authors have signed.
It is one Next.js application in TypeScript, with its pages, its API and the webhook of its GitHub App in one repository, over a SQLite database through Prisma; it has 11,902 lines of TypeScript code, tests not counted, and 259 tests that pass.[^brownfield-research]
It was chosen among the open source projects measured for this book because it is a real product with a domain of its own, many tests, and open issues written as specs.[^brownfield-research]
This book's fork, `JCKodel/clahub`, freezes it at the tag `book-v1`, the upstream commit that was measured, so the run can be repeated.
Before the run the kit was installed and committed on a branch of the fork, as chapter 5 shows, so `/analyze` started on a clean tree.[^analyze-run]

## The run on CLAHub

The run was answered from a brief with one section per subject of the round, plus the rule for a question the brief does not answer:[^analyze-run]

```markdown
# Brief

## Documentation language
English.

## Purpose and audience
Your call: the README says it.

## Choices
FOCUS: your call. Git: your call.

## First milestone
The three open issues upstream, one delivery each, in this order:
https://github.com/DamageLabs/clahub/issues/270
https://github.com/DamageLabs/clahub/issues/274
https://github.com/DamageLabs/clahub/issues/268

## Rule for a question the brief does not answer
Answer "your call".
```

Open your host at the root of the repository, in a fresh session, and type `/analyze`; I ran it headless in Claude Code and answered with the brief's sections for the subjects asked, word for word.[^analyze-run]
It read the README, the guides already in `docs/`, `package.json`, the CI workflow, the tree, the last fifty commit subjects, the database schema and the code of errors, actions and the CLA check, and then asked its round:[^analyze-run]

```markdown
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
```

The answer was the brief's sections for the subjects asked:[^analyze-run]

```markdown
## Documentation language
English.

## Choices
FOCUS: your call. Git: your call.

## First milestone
The three open issues upstream, one delivery each, in this order:
https://github.com/DamageLabs/clahub/issues/270
https://github.com/DamageLabs/clahub/issues/274
https://github.com/DamageLabs/clahub/issues/268
```

The agent did not ask the purpose, because the README says it, and it told what it found without asking you to confirm it.
It recommended for FOCUS and git what the repository already does, so the brief's "your call" kept both, and it listed the contradictions it will record instead of asking which side is right.

With that answer it wrote the documents, and `git status --short` showed:[^analyze-run]

```
?? AGENTS.md
?? CLAUDE.md
?? docs/00-Product.md
?? docs/01-Architecture.md
?? docs/02-Backend.md
?? docs/03-Domain.md
?? docs/04-Conventions.md
?? docs/05-Process.md
?? docs/06-Queue.md
?? docs/adr/
?? work/
```

These lines hold docs/00 to 06, `AGENTS.md`, `CLAUDE.md` holding the line `@AGENTS.md`, `work/done/.gitkeep`, and an ADR each in `docs/adr/` for the decisions the code already embodies (the rewrite in Next.js, SQLite through Prisma, separate GitHub sign-ins for owners and contributors, checks through the GitHub App, transactions with an audit log, errors as values, repositories identified by number, corporate coverage by email domain) and for the round's choices, FOCUS and git.[^analyze-run]
The excerpts below are quoted at the chapter tag `book-v1-analyze`, as committed.
The brownfield project's chapter tags take a hyphen where the guided project's take a slash (chapter 5) because the fork already holds the tag `book-v1`, the frozen upstream, and git refuses to create a tag `book-v1/analyze` beside it.

docs/01 is where the agent wrote what it inferred.
For the clinic, how the code is organized was a choice made in the conversation; here it is read from the tree.
This is [`docs/01-Architecture.md`](https://github.com/JCKodel/clahub/blob/book-v1-analyze/docs/01-Architecture.md) §How the code is organized:

```markdown
## How the code is organized

The project's own conventions, organized by technical layer (ADR-0009):

* `src/app/`: routes. `(marketing)/` public pages (landing, about, docs,
  privacy, terms, why-cla); `agreements/` dashboard, create, edit and the
  public signing pages `[owner]` and `[owner]/[repo]`; `settings/api-keys`;
  `auth/signin`; `api/` route handlers (`v1/` REST, `badge/`, `health/`,
  `webhooks/github`, `github/` helper lookups, `auth/`).
* `src/components/`: `ui/` shadcn primitives, `agreements/` and
  `settings/` feature components.
* `src/lib/actions/`: server actions, one file per area (agreement,
  signing, signature, exclusion, api-key, audit-log, recheck, contributing),
  plus `result.ts`.
* `src/lib/schemas/`: Zod schemas, shared by forms, actions and the API.
* `src/lib/`: everything else. `cla-check.ts` holds the core rule (author
  classification, check runs, re-check with retry); `github.ts` the App and
  webhook handlers; `access.ts` and `org-membership.ts` access levels;
  `audit.ts`, `api-*.ts`, `rate-limit.ts`, `email.ts`, `export-*.ts`,
  `badge.ts`, `branding.ts`, `templates.ts`, `prisma.ts`.
* `src/middleware.ts`: redirects unauthenticated or non-owner users away
  from owner pages; `/api/v1` authenticates itself.
* `src/generated/prisma/`: generated client, never edited.

Business rules live mostly in `cla-check.ts`, `access.ts` and the server
actions; the actions also do data access directly through `prisma`. There
is no repository layer.
```

Every line names a folder or a file you can open, and the last paragraph says what is missing as plainly as what is there: there is no repository layer, and FOCUS whole would have meant a refactor, so the agent kept the project's own conventions.

The research that chose CLAHub found that its README's setup fails as written: it says to create `.env.local`, and the Prisma configuration reads `.env`.[^brownfield-research]
The run recorded that contradiction as an open question in docs/01, after the review of the next section asked the agent to check the line against the code.
This is the first entry of [`docs/01-Architecture.md`](https://github.com/JCKodel/clahub/blob/book-v1-analyze/docs/01-Architecture.md) §Open questions:

```markdown
## Open questions

* **Which env file the Prisma CLI reads.** README and
  `docs/getting-started.md` say to copy `.env.local.example` to `.env.local`
  and then run `npm run db:push` / `npx prisma db push`. The Prisma CLI reads
  only `.env`, so with `.env.local` alone `DATABASE_URL` is undefined and the
  command fails unless the variable is exported in the shell or also written
  to `.env`. Fix the guides, or make `prisma.config.ts` and `prisma/seed.ts`
  load `.env.local` too?
```

It says what each side says, why the step fails, and both ways out, and it takes neither: fixing the guides or the configuration is a delivery with its own page, and `/analyze` changes no code.

docs/06 is the queue (chapter 9 teaches the marks), and the brief gave its first milestone as the three upstream issues, in order.
This is [`docs/06-Queue.md`](https://github.com/JCKodel/clahub/blob/book-v1-analyze/docs/06-Queue.md):

````markdown
# Queue

## Milestone 1: current signatures, owner emails, personal data

Closes when an owner can require contributors to re-sign after a new CLA
version, with an optional grace period, and PR checks honour it; when the
notification email sent on signing uses the owner's own subject and body,
falling back to the default; and when any user can download their personal
data as one JSON file and delete their account. Source: upstream issues
DamageLabs/clahub #270, #274 and #268, in that order.

```
[ ] resign-on-version-bump       owners can require re-signing when a new CLA version is published, with an optional grace period (#270)
[ ] custom-email-templates       owners customize the subject and body of the new-signature email with variables and a preview (#274)
[ ] gdpr-export-and-deletion     users download their data as JSON and delete their account (#268)
```
````

Since focus-kit's commit `bff8414`, `/analyze` ends the first milestone with one more line, its review, `m1-review` ([chapter 12](12-closing-a-milestone.md)).
This run used the kit at `26e5e1e`, before that rule, so your queue has one line more than the one above.
Each issue is one delivery with a slug for its page, and the paragraph says what is true when the milestone closes; the next section shows that the first version said much less.

## Check it against the code

On a new project you check the documents against what you answered (chapter 7).
On an existing project most of what the agent wrote is marked as observed, so the review is a check of facts:

* every observed statement is true in the code: open the file it names and read it;
* every open question is a contradiction the code really holds;
* nothing describes what should exist instead of what does.

In the run, headless, the agent wrote the documents without showing the diff first, so the whole check came after it.[^analyze-run]
When a statement is wrong, ask the agent in the same session to check it against the code and correct it, and let it write the change ([chapter 6](06-the-documents.md)).

The Local line of docs/01 said that local setup reads `.env.local`.
That is the README's word, taken as a fact, and it was only half true.
The request was:[^analyze-run]

```markdown
docs/01 says local setup uses .env.local. Check that against prisma.config.ts and the README, and correct docs/01; where they disagree, record an open question.
```

The agent read the Prisma configuration, the example environment files and the setup of the end-to-end tests, and rewrote the line; this is the first part of its diff:[^analyze-run]

```diff
--- a/docs/01-Architecture.md
+++ b/docs/01-Architecture.md
@@ -82,9 +82,22 @@
 
 ## Environments
 
-* **Local:** `npm run dev` on port 3000, SQLite file from `DATABASE_URL`,
-  `.env.local`; webhooks need a tunnel (ngrok). E2E reuses the running dev
-  server.
+* **Local:** `npm run dev` on port 3000; webhooks need a tunnel (ngrok).
+  Configuration comes from two files read by different tools:
+  * Next.js (`dev`, `build`, `start`) reads `.env.local` (and `.env`).
+  * The Prisma CLI (`db:push`, `migrate`, `db:seed`, `studio`) reads only
+    `.env`: `prisma.config.ts` and `prisma/seed.ts` load it through
+    `import "dotenv/config"`, which ignores `.env.local`.
+  * `DATABASE_URL` is a path relative to the repository root
+    (`file:./clahub.db` in `.env.local.example`); the app and the Prisma CLI
+    both resolve it from there.
+  * Playwright loads `.env.local`, then `.env.test`, without overriding, so
+    locally the E2E run sees the `DATABASE_URL` of `.env.local`. When no dev
+    server is on port 3000, its global setup force-resets and seeds that
+    database; otherwise it reuses the running server and its data.
+
+  Where README, `docs/getting-started.md` and the code disagree, see the
+  open questions below.
 * **CI (GitHub Actions):** on push and PR to `main`: lint, `tsc --noEmit`,
   unit tests, build; then Playwright E2E against a fresh `test.db`.
 * **Production:** https://www.cla-hub.io. `docs/deployment.md` describes a
```

The second part added the Open questions section quoted above, with the other contradictions it found while checking: a variable the guides call required that no code reads, and a local end-to-end run that can reset the development database; both hold in the code.
The documents read well before the request, and only opening the file behind the statement showed that it was wrong.

The review found a second gap, of input rather than of fact.
`acceptEdits` is a Claude Code permission mode, the setting that decides what the agent does without asking you: in it the agent reads, edits files and runs common file commands, and anything else, such as `gh` or opening a web page, needs your approval.[^claude-code-permission-modes]
It is the least permission the command needs, and the run used it headless, with no one to answer, so every approval it asked for was denied: the host refused the agent both `gh` and the fetch of the issue pages, and it wrote the queue from the issue numbers alone:[^analyze-run]

````markdown
# Queue

## Milestone 1: upstream open issues

Closes when the three issues open upstream at DamageLabs/clahub are
resolved on a branch each, verify green, one page per issue in
`work/done/`. The issue text is read at /propose time; the lines below name
the issue only.

```
[ ] issue-270    resolve upstream issue #270 (https://github.com/DamageLabs/clahub/issues/270)
[ ] issue-274    resolve upstream issue #274 (https://github.com/DamageLabs/clahub/issues/274)
[ ] issue-268    resolve upstream issue #268 (https://github.com/DamageLabs/clahub/issues/268)
```
````

In an interactive session you would see that question and approve `gh issue view` there, and the gap would not reach you unless you denied it.
Headless, the fix was that approval given in advance: it allowed one command, `gh issue view`, for one more turn in the same session, with this request:[^analyze-run]

```markdown
Read the three issues with gh issue view and rewrite the milestone and its lines from them.
```

The agent read the three issues and rewrote the milestone and its lines as shown in the previous section; it changed nothing else.
Its reply also named where the issues clash with the documented rules, such as a deletion of audit logs against the rule that every change is kept, and left them for `/propose` to settle with you.

## Key points

* `/analyze` reads the repository first, code or not (the README and its docs, the manifests, the tree, the entry points, the tests, CI, the last fifty commit subjects, any rules file), and then asks one round of four subjects.
* Put everything you have about the project in `context/` and tell the agent to read it first: what it does not read, it has to guess.
* The default of each choice is what the code already does, and the agent says what that is, so "your call" keeps it; a contradiction becomes an open question for a later delivery.
* On an existing project the review is a check of facts: open the file behind each observed statement.
* A correction is a request in the same session, never an edit by hand; give the agent what it needs to check, a file or a permission, and let it write.

## Exercises

### Exercise 8.1

Clone the fork `JCKodel/clahub` at `book-v1` on a branch of your own, install the kit (chapter 5), commit it (chapter 11 shows how), run `/analyze`, and answer it with the brief of this chapter.
Compare what you get with `book-v1-analyze`: what differs, and is any difference wrong about the code?

### Exercise 8.2

Pick three statements of docs/01 or docs/04 at `book-v1-analyze` and find each in the code.
Which file proves each one?

### Exercise 8.3

Run `/analyze` on a repository of your own.
Which open questions did it record, and which of them would you have missed?

[^strangler-fig]: Martin Fowler, "Strangler Fig", 2024. <https://martinfowler.com/bliki/StranglerFigApplication.html>
[^brownfield-research]: This book's research delivery for the brownfield project, 2026-09-25: the candidates, how each was measured, the choice, and CLAHub's TypeScript code lines (tests excluded) and passing tests at upstream commit 9d1e666e1d30f271aea9640393229a7cbfbd1b62. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/brownfield-research.md>
[^analyze-run]: This book's `/analyze` run on the brownfield project, 2026-09-28, with Claude Code 2.1.283 and the model `claude-opus-5-5`, from `book-v1` to the chapter tag `book-v1-analyze`: the install of the kit, the brief, the commands, every turn's output, the round and its answer, and the corrections. <https://github.com/JCKodel/focus-kit-book/blob/main/work/done/analyze-run/README.md>
[^claude-code-permission-modes]: Anthropic, "Choose a permission mode", Claude Code documentation, accessed 2026-09-29. <https://code.claude.com/docs/en/permission-modes>
