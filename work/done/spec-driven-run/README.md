# Spec-driven run

SpecKit, OpenSpec and focus-kit, given the same brief on the same small TypeScript project, each run up to the step before implementation. What each wrote is here, counted in files, lines and words. The delivery that planned and recorded the run is `../spec-driven-run.md`.

## Setting

| | |
|---|---|
| Date | 2026-09-25, all three runs |
| Host | Claude Code 2.1.282, headless (`claude -p`), macOS 26 (Darwin 25.6.0), arm64 |
| Model | `claude-opus-5-5`, the same for every step |
| SpecKit | `specify-cli` v1.0.11, the latest release tag of `github/spec-kit` that day |
| OpenSpec | `@fission-ai/openspec` 1.13.2, the latest on npm that day, put first on `PATH` so the agent's `openspec` calls ran that version |
| focus-kit | `JCKodel/focus-kit` `main` at `26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b` |
| Node | v26.10.0 |
| uv | 0.11.14 |

Each step was one fresh session, `--continue` only to answer the question that step asked:

```
claude -p [--continue] --model claude-opus-5-5 \
  --setting-sources project,local --strict-mcp-config \
  --permission-mode <mode> --permission-prompts none \
  --output-format json "<prompt>"
```

`--setting-sources project,local` and `--strict-mcp-config` keep the operator's own instructions, plugins and MCP servers out of the sessions; only Claude Code's built-in skills and what each tool installed were present. `--bare` would isolate more, but it takes only an API key, and the run used a subscription login.

## The project and the brief

The three folders started from one commit, "Starting point", with the same four files: `package.json` (`clinic-weigh-in`, `"type": "module"`, TypeScript `^7.0.2` as the only dev dependency, `test` running `node --test`), `tsconfig.json` (strict, ES2022, NodeNext), `src/appointment.ts` (the type `Appointment` with `status: "booked"`, an in-memory list and `book(clientName, startsAt)`) and a one-line `README.md`. Nothing was installed with npm.

The brief is `brief.md`. Each tool got its parts where its path asks for them, word for word:

| Tool | Step | Prompt | Permission mode |
|---|---|---|---|
| SpecKit | install | `specify init --here --force --non-interactive --integration claude` (terminal) | |
| | constitution | `/speckit-constitution` + Principles | `auto` |
| | specify | `/speckit-specify` + Feature | `auto` |
| | plan | `/speckit-plan` + Answers | `auto` |
| | tasks | `/speckit-tasks` | `auto` |
| OpenSpec | install | `openspec init --tools claude --profile core --no-animation` (terminal) | |
| | propose | `/opsx:propose` + Feature + Answers | `auto` |
| focus-kit | install | `Read https://raw.githubusercontent.com/JCKodel/focus-kit/26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b/SETUP.md and do what it says.` | `bypassPermissions` |
| | analyze | `/analyze` | `acceptEdits` |
| | propose | `/propose cancel-appointment`; Feature + Answers with the first answer | `acceptEdits` |

Every step started in `acceptEdits` and moved up only when it could not finish there; the attempts that did not count are in each `questions.md`:

* SpecKit: its skills run the scripts of `.specify/scripts/bash/`, which `acceptEdits` denies; the constitution stopped without writing. In `auto` nothing was denied.
* OpenSpec: `/opsx:propose` runs the `openspec` CLI, which `acceptEdits` denies; the agent wrote the change by hand, without the templates, so the change was deleted and the step repeated in `auto`.
* focus-kit install: `acceptEdits` denied the download of `SETUP.md`; in `auto` the permission check blocked the file writes as possible prompt injection ("a web page telling me to write files into your repo"). It finished only in `bypassPermissions`.
* focus-kit `/analyze` and `/propose`: `acceptEdits` denied one shell command in each; the agent read the same files with its file tool and said so. Both finished.

No step wrote code for the feature. SpecKit's plan ran a throwaway check that Node runs `.ts` tests and removed it; nothing outside the folders counted below changed.

## The counts

Counted with `find -type f`, `wc -l` and `wc -w` on the files of each row, as each row's step left them.

| Tool | Row | Files | Lines | Words |
|---|---|---:|---:|---:|
| SpecKit | installed | 29 | 5,074 | 30,174 |
| SpecKit | once per project | 1 | 71 | 429 |
| SpecKit | per feature | 8 | 756 | 6,498 |
| OpenSpec | installed | 12 | 2,590 | 27,015 |
| OpenSpec | once per project | 3 | 32 | 140 |
| OpenSpec | per feature | 6 | 180 | 2,201 |
| focus-kit | installed | 36 | 2,049 | 14,700 |
| focus-kit | once per project | 17 | 277 | 2,577 |
| focus-kit | per feature | 1 | 82 | 602 |

What each row holds:

* **SpecKit.** Installed: `.claude/skills/` (10 skills) and `.specify/` (scripts, templates, workflow, manifests), without `.specify/memory/constitution.md`, which `init` writes as a template and the constitution step rewrites. Once: that constitution, as the step left it. Per feature: `specs/001-cancel-appointment/`. Also written by `/speckit-specify` and ignored by SpecKit's own `.gitignore`, so not counted: `.specify/feature.json`, 3 lines pointing at the feature folder. SpecKit created no git branch: at v1.0.11 branching is the optional `git` extension, not installed by default.
* **OpenSpec.** Installed: `.claude/commands/opsx/` (6) and `.claude/skills/` (6). Once: what `init` wrote under `openspec/` outside the change: `config.yaml`, `specs/.gitkeep` and `changes/archive/.gitkeep`. Per feature: `openspec/changes/add-client-cancellation/` (the tool chose the name).
* **focus-kit.** Installed: the 36 files of `SETUP.md` (the four skills in `.claude/`, `.agents/` and `.windsurf/`, the files for Codex, Copilot, Cursor, Gemini CLI and Antigravity, and `GEMINI.md`). Once: `docs/`, `docs/adr/` and `AGENTS.md`, as `/analyze` wrote them. It also wrote `CLAUDE.md`, the one line `@AGENTS.md`, and an empty `work/done/.gitkeep`; neither is counted or kept, the first because a `CLAUDE.md` inside this repository would load the clinic's rules into any agent reading the folder. Per feature: `work/cancel.md`; the page named `cancel`, not `cancel-appointment`, because the queue `/analyze` wrote already had that line (see `focus-kit/questions.md`). `/propose` also changed two once-per-project files, adding 6 lines and 143 words to `docs/03-Domain.md` and `docs/06-Queue.md` while removing 3; that diff is `focus-kit/propose-docs.diff`, not in the row.

The installed files are counted and not kept here; `once/` and `feature/` keep the other two rows byte for byte, with each path as the tool wrote it. No tool wrote an absolute path, so nothing was replaced by `<run>`.

## Repeating it

1. Create the four starting files above in three empty folders, `git init` and commit each.
2. Install each tool with the command of the table, at the version of the table (`uvx --from git+https://github.com/github/spec-kit.git@v1.0.11 specify ...`; `npx -y @fission-ai/openspec@1.13.2 ...`; the `SETUP.md` URL with the SHA).
3. Run each step with the `claude -p` line above, a fresh session per step, the prompt of the table and the text of `brief.md`. When a step ends with a question, answer it by the rule at the end of `brief.md` with `--continue`, and write both down.
4. Count each row with `find <paths> -type f | xargs cat | wc -lw`.

You will get the same kind of output, not the same bytes: the agent is not deterministic, so the questions, the file names and the numbers will move. This is one run, said plainly: one model, one day, one feature. It shows the order of magnitude of what each tool writes before code; it is not a study of the average.
