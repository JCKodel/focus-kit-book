# spec-driven-run

**Objective.** The author knows, from one recorded run, how many files, lines and words SpecKit, OpenSpec and focus-kit write for the same small feature before any code, with the outputs committed so chapter 3 can cite the numbers and a reader can check and repeat them.

**Behaviour.**

* The three tools start from the same minimal TypeScript project and receive the same brief, word for word.
* Each tool runs its own documented path up to the step before implementation, and stops there: no code is written for the feature.
* Every question a tool asks is answered from the brief; the question and the answer are recorded.
* The counts split what the tool installs, what the project writes once, and what the feature writes, so no reader can say setup was hidden or charged to the feature.
* Versions, host, model and date are recorded, and a reader who follows the folder's README gets the same kind of output (not the same bytes: the agent is not deterministic, and the README says so).
* The author reads the table and the outputs before the chapter is proposed.

**Contract.**

Where: the run happens outside the repository, in `<scratch>/weigh-in/<tool>/` for `<tool>` in `speckit`, `openspec`, `focus-kit`, never in or next to a folder of the author's private material. Only the files listed under "Committed" enter the repository.

Starting point, identical in the three folders, created by /apply, then `git init` and one commit "Starting point":

* `package.json`: name `clinic-weigh-in`, `"type": "module"`, TypeScript as the only dev dependency, script `test` running `node --test`.
* `tsconfig.json`: strict, ES2022, module NodeNext.
* `src/appointment.ts`: a type `Appointment` with `id`, `clientName`, `startsAt` (Date) and `status` (`"booked"`); an in-memory list; a function `book(clientName, startsAt)` returning the new appointment. No cancel, no status other than `"booked"`.
* `README.md`: one line, "Appointments for a small clinic."

The brief, saved as `work/done/spec-driven-run/brief.md` and given verbatim:

* Feature: "A client can cancel their own appointment up to 24 hours before it starts. A cancelled appointment frees its slot. A cancellation later than that is refused with a message that says why."
* Answers: storage stays in memory; no screen, the feature is a function in the module; the client is identified by `clientName`, no login; times are the clinic's local time; tests use `node --test`; no notification is sent.
* Principles, for a tool that asks for them: "Keep it simple. TypeScript, strict. Every rule has a test."
* Rule for a question the brief does not answer: take the default the tool offers; with none, answer "the simplest option". Every question and answer goes to `<tool>/questions.md`.

Runs, the same day, host Claude Code headless (`claude -p`, `--continue` to answer a question), the same `--model`, one fresh session per command, the least permission mode that lets the command finish (recorded):

| Tool | Version pinned | Sequence, stopping before implementation |
|---|---|---|
| SpecKit | the latest release tag of `github/spec-kit` that day | `specify init` for Claude Code at that tag → constitution (principles) → specify (feature) → plan (answers) → tasks. The optional commands (clarify, checklist, analyze) are not run. |
| OpenSpec | the latest `@fission-ai/openspec` on npm that day | `openspec init` for Claude Code → the propose command its README recommends at that version (feature and answers). Explore is not run; apply is not run. |
| focus-kit | the SHA of `JCKodel/focus-kit` `main` that day | install by pointing the agent at `https://raw.githubusercontent.com/JCKodel/focus-kit/<sha>/SETUP.md` → `/analyze` (the project has code) → `/propose cancel-appointment` (feature and answers). `/apply` is not run. |

Counted per tool, with `find -type f`, `wc -l` and `wc -w`, three rows:

* **installed**: the templates, scripts and command or skill files the tool puts in the project. Counted, not committed.
* **once per project**: what the project's own setup writes for an agent to read. SpecKit: the constitution. OpenSpec: what `init` writes under `openspec/` outside `changes/`. focus-kit: `docs/`, `docs/adr/`, `AGENTS.md`.
* **per feature**: SpecKit `specs/001-*/`; OpenSpec `openspec/changes/<name>/`; focus-kit `work/cancel-appointment.md`.

Committed, `work/done/spec-driven-run/`:

```
README.md                  date, versions (Claude Code, model id, SpecKit tag, OpenSpec version, focus-kit SHA, Node, uv), permission mode, the count table, how to repeat, one run and why
brief.md                   the brief, verbatim
<tool>/questions.md        each question asked and the answer given, in order
<tool>/once/...            the "once per project" files, paths as the tool wrote them
<tool>/feature/...         the "per feature" files, paths as the tool wrote them
```

Files kept byte for byte, except an absolute path written by a tool, replaced by `<run>` and listed in README.md.

Other files changed:

```
scripts/check_em_dash.py   skips work/done/spec-driven-run/: third-party output kept as evidence, read by no reader of the book
docs/04-Conventions.md     §Tests: that exemption and its reason
docs/06-Queue.md           spec-driven-run [x]
```

The disclosure scan keeps covering the folder.

**Decided for `spec-driven`**, the next delivery, which /propose reads from here: chapter 3 cites this run's per-feature row as its evidence, with the other two rows beside it; Ninjobs stays out (chapter 4's); Böckeler's spec-first, spec-anchored and spec-as-source enter docs/03 in English in both editions, with a translation in parentheses on first use; Kiro and Tessl get one sentence, through Böckeler.

**Out of scope.**

* Implementing the feature: the weight measured is what is written before code.
* The optional commands of each tool: the counted path is the one each README calls the default.
* Several runs or several models: one run, said plainly; statistics would be a study, not a chapter's evidence.
* Kiro and Tessl: not run; Böckeler's article covers them.
* Chapter 3 itself: `spec-driven`.

**Done when.**

* [x] The three runs finished on the same day with the pinned versions, each stopped before implementation.
* [x] `brief.md`, three `questions.md`, the `once/` and `feature/` files and README.md committed as above; the count table has three rows per tool.
* [x] `grep -rE '/Volumes|/Users|/home|/private' work/done/spec-driven-run` finds nothing.
* [x] The em dash exemption in place and in docs/04 §Tests; `make verify` green, disclosure included.
* [x] The author has read the table; the page moved to `work/done/spec-driven-run.md` with what happened; docs/06 marked `[x]`.

**What happened.**

The run, 2026-09-25: SpecKit v1.0.11, OpenSpec 1.13.2, focus-kit `26e5e1e`, Claude Code 2.1.282, model `claude-opus-5-5` (the author's choice; the page named none). The per-feature row: SpecKit 8 files, 756 lines, 6,498 words; OpenSpec 6, 180, 2,201; focus-kit 1, 82, 602. The full table and every setting are in `spec-driven-run/README.md`.

Diverged from the plan:

* Permission mode. Every step started in `acceptEdits`, which was enough only for focus-kit's `/analyze` and `/propose`. SpecKit and OpenSpec run their own scripts and CLI from inside their commands, so they needed `auto`. focus-kit's install needed `bypassPermissions`: `auto` blocked it as possible prompt injection, a web page telling the agent to write files. That finding is a fact about the install path the book recommends, and chapter 3 or 4 can use it. Each attempt that did not count is in the tool's `questions.md`.
* OpenSpec's `openspec` on this machine was 1.9.0; the run put 1.13.2 first on `PATH` so the agent's calls ran the pinned version.
* focus-kit's page is `work/cancel.md`, not `work/cancel-appointment.md`: `/analyze` had already written a queue line `cancel`, and `/propose` recommended it. The author chose to keep the rule (take the tool's default).
* One answer departs from the rule: `/propose` recommended defining `verify` first, which would have ended the run with no page for the feature. The author chose the tool's other option, write the page now with a prerequisite. `focus-kit/questions.md` says so.
* `/propose` also edited `docs/03` and `docs/06` (6 lines added, 3 removed). They are once-per-project files, so the row does not count them; the diff is kept as `focus-kit/propose-docs.diff`, beside `questions.md` so each `feature/` folder holds exactly its row, and the README gives its size.
* `/analyze` also wrote `CLAUDE.md` (the line `@AGENTS.md`) and an empty `work/done/.gitkeep`, outside the page's once row; neither is counted or kept. A `CLAUDE.md` in this repository would load the clinic's `AGENTS.md` into any agent that reads the folder, the next delivery's first of all. The author read the table with them counted (19 files, 278 lines, 2,578 words); without them the row is 17, 277, 2,577.
* SpecKit's `.specify/feature.json` (3 lines, ignored by SpecKit's own `.gitignore`) is not counted. SpecKit created no branch; at v1.0.11 that takes the optional `git` extension.
* Isolation: `--setting-sources project,local --strict-mcp-config` kept the operator's instructions, plugins and MCP servers out; `--bare` needs an API key, and the run used a subscription login.
* The em dash check's one-line description in docs/01 names the exemption too.

The proof: `make verify` green with the disclosure list; the path grep finds nothing; `find | xargs cat | wc -lw` on the committed `once/` and `feature/` folders gives the table's numbers; no tool wrote an absolute path, so nothing was replaced by `<run>`.

Not recorded in the repository: the JSON logs of each step (time, cost, session id) stayed in the scratch folder. The steps that count cost, as Claude Code reported, SpecKit USD 1.59 over 322 s, OpenSpec USD 0.68 over 115 s, focus-kit USD 2.16 over 321 s, of which `/propose` USD 0.54 over 89 s.
