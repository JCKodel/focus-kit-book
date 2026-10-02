# ask-for-more-experiment run

What a fixed challenge protocol adds to an agent's first answer, on three lending-library tasks: a card with tabs (limit), an annual report summarized for a board (audience), and a project set up for a daily question-answering agent (cost). Each arm ran three times; every run is one session that records the first answer, then sends the protocol's four turns and records the challenged answer. The delivery that planned and recorded it is `../ask-for-more-experiment.md`.

* Date: 2026-10-02, all nine runs and all measurements on that day (UTC 16:26 to about 17:10).
* Host: Claude Code, `claude --version` printed `2.1.287 (Claude Code)` before the first run and again before protocol turn 4; macOS 26.6.2, x86_64; Node v26.10.0.
* Model: `claude-opus-5-5`, given with `--model` on every call: the runs, the generation of the starting points, the measurement sessions and the judges.
* Judge: not the author. The author handed the judging and the marking to the agent; each pair was scored blind by a fresh session of the same model that wrote the answers (see What diverged). The book's author wrote the protocol and the rubric.
* Three pairs per arm, said plainly: this is a recorded experiment, not a study, and has no statistics.

## How it ran

Each run folder, `<run>`, was a fresh copy of `<arm>/start/` (without `questions.md`) made a git repository with one commit, `start`. Every turn was a headless call from `<run>`:

```
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 claude -p "<message>" --model claude-opus-5-5 --setting-sources project,local --strict-mcp-config --output-format stream-json --verbose --permission-mode acceptEdits --permission-prompts none
```

Turn 1 started the session; every later turn added `--resume <the run's session id>`, never `--continue`. A check before the runs, from an empty folder with the same flags, showed the agent no instruction file, no MCP server and no hook of the host's user settings.

1. Turn 1: the arm's task (`prompts.md`). Then the run folder was committed and tagged `first`.
2. Turn 2: protocol turn 1. The agent's questions were answered in turn 3, in one message, from `<arm>/brief.md` only; a question the brief does not answer got "Use your judgment." (`<arm>/run-<n>/questions.md`).
3. Protocol turns 2, 3 and 4 followed, each when the previous turn ended. After protocol turn 2, six agents ended by asking whether to apply what they proposed (limit 1 to 3, audience 1 and 2, cost 2); each got "Use your judgment." as a turn of its own before protocol turn 3. No other turn ended with a question to the person.
4. After the last turn the folder was committed and tagged `challenged`.

Permission mode, chosen by the author before the runs as the least that lets every task finish: `acceptEdits` with `--permission-prompts none`, the same in every run. Under it the host denied every `Bash` call (Bash: 41 calls denied across the nine runs, among them every attempt to validate JSON, count words or run the tests), every write to `.claude/settings.json` (six, in the cost runs) and `WebSearch` (two). `WebFetch` was allowed: the limit runs fetched Microsoft's Teams and Adaptive Cards documentation 20 times (three fetches denied). The audience and cost runs fetched nothing.

The starting points: `limit/start/README.md` is one line. `audience/start/annual-report.md` (14,073 words, 37 tables, figures synthetic and said so on line 1) and the cost project (51 tests passing with `node --test`; `notes/` of 29 files and 19,484 words, with no index and no `AGENTS.md`) were generated once, each in a session of its own, from the prompts in `prompts.md`; `cost/start/questions.md` was written before the runs. The author read them before the runs.

The cost arm's measurement: for each of its six setups (three `first`, three `challenged`), the five questions of `questions.md`, each in its own fresh session in a copy of that setup, read-only:

```
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 claude -p "<question>" --model claude-opus-5-5 --setting-sources project,local --strict-mcp-config --output-format stream-json --verbose --permission-mode default --permission-prompts none --allowedTools "Read" "Glob" "Grep"
```

30 sessions, all finished.

Judging: one script copied each pair's two answers to `X/` and `Y/`, the side drawn by `secrets.randbelow(2)` per pair, and wrote the key to `blind/key.md`; the script printed nothing. An answer is the files the agent added or changed plus its last message of that state, as `answer.md`. One fresh session per pair (same flags as the measurement, read-only) scored X and Y on the arm's rubric and said which it would send; its prompt gave the task, `brief.md`, the criteria and, for audience, the report, for cost, the starting project, and never named the protocol. The key was applied after all nine scores were recorded (`scores.md`). The 30 measurement answers were marked against `questions.md` by one fresh session per question, which saw the six setups' answers under letters shuffled per question.

Counted: tokens and seconds from each turn's `result` event in the stream-json; cost from the same event's `total_cost_usd`, which the host reports for the whole session so far, so the challenged cost is the session's cost at its last turn.

## Results

### Blind scores

Sum of the three criteria, three pairs per arm (at most 45), and how often the judge would send each side:

| Arm | Score, first (of 45) | Score, challenged (of 45) | Sent: first | Sent: challenged |
|---|---|---|---|---|
| limit | 31 | 39 | 0 | 3 |
| audience | 36 | 44 | 0 | 3 |
| cost | 24 | 39 | 0 | 3 |

The judge would have sent the challenged answer in all nine pairs. Per pair, with the judge's sentence, in `scores.md`.

### Tokens, cost and time

`challenged` is the whole session up to its last turn, the first answer included.

| Run | State | Turns | Input | Output | Cache write | Cache read | Cost (USD) | Seconds |
|---|---|---|---|---|---|---|---|---|
| limit-1 | first | 1 | 6 | 8,339 | 11,858 | 49,288 | 0.27 | 68 |
| limit-1 | challenged | 7 | 40 | 59,956 | 134,890 | 1,397,930 | 2.59 | 526 |
| limit-2 | first | 1 | 10 | 6,759 | 10,525 | 79,580 | 0.24 | 59 |
| limit-2 | challenged | 7 | 56 | 36,583 | 83,028 | 1,542,596 | 1.70 | 366 |
| limit-3 | first | 1 | 12 | 9,122 | 13,253 | 101,895 | 0.31 | 74 |
| limit-3 | challenged | 7 | 44 | 50,880 | 127,610 | 1,316,230 | 2.30 | 445 |
| audience-1 | first | 1 | 8 | 2,879 | 37,482 | 81,100 | 0.37 | 31 |
| audience-1 | challenged | 7 | 46 | 20,966 | 61,149 | 1,230,743 | 1.15 | 225 |
| audience-2 | first | 1 | 6 | 2,297 | 37,200 | 65,336 | 0.36 | 24 |
| audience-2 | challenged | 7 | 28 | 31,889 | 70,427 | 759,674 | 1.35 | 304 |
| audience-3 | first | 1 | 6 | 2,200 | 37,200 | 65,336 | 0.35 | 26 |
| audience-3 | challenged | 6 | 26 | 16,134 | 54,547 | 619,912 | 0.88 | 181 |
| cost-1 | first | 1 | 18 | 13,199 | 77,931 | 359,386 | 0.96 | 130 |
| cost-1 | challenged | 6 | 52 | 38,945 | 125,353 | 2,324,007 | 2.49 | 422 |
| cost-2 | first | 1 | 16 | 14,452 | 84,561 | 365,494 | 1.04 | 128 |
| cost-2 | challenged | 7 | 50 | 36,981 | 133,775 | 2,402,582 | 2.60 | 374 |
| cost-3 | first | 1 | 20 | 13,769 | 83,949 | 499,364 | 1.05 | 132 |
| cost-3 | challenged | 6 | 48 | 34,408 | 123,608 | 2,089,095 | 2.90 | 335 |

| Arm | State | Output tokens, 3 runs | Cost (USD), 3 runs | Seconds, 3 runs |
|---|---|---|---|---|
| limit | first | 24,220 | 0.82 | 201 |
| limit | challenged | 147,419 | 6.59 | 1337 |
| audience | first | 7,376 | 1.09 | 81 |
| audience | challenged | 68,989 | 3.39 | 710 |
| cost | first | 41,420 | 3.04 | 390 |
| cost | challenged | 110,334 | 8.00 | 1130 |

### Limit: tabs and what the first answer called impossible

* All six cards have three tabs that switch: three panels, one visible at the start, and `Action.ToggleVisibility` buttons whose every target exists. Checked from `card.json`, not in the Designer (see What diverged).
* No first answer called the tabs, or anything the card shows, not possible. Sentences of the first answers that call something not possible, as /apply marked them: limit 1, two (validation blocked by the session's permissions; the buttons need a bot to do anything); limit 2, none; limit 3, one (validation blocked). Audience: none in any run. Protocol turn 2 turned up, in the limit runs, what Teams does not support (button styles) and what the documentation could not confirm (Badge, ProgressBar, icon names).

### Audience: words

| Run | First: words in the chat answer | Challenged: words per file |
|---|---|---|
| audience-1 | 901 | `board-summary.md` 849 |
| audience-2 | 842 | `board-summary.md` 758, `questions-for-director.md` 209 |
| audience-3 | 853 | `board-summary.md` 671 |

The first answers were text in the chat and wrote no file. Every challenged answer wrote `board-summary.md`, with no tables (for a phone) and the board's decisions first.

### Cost: the five questions per setup

| Setup | Input | Output | Cache write | Cache read | Cost (USD) | Seconds | Correct |
|---|---|---|---|---|---|---|---|
| run-1 first | 26 | 4,746 | 57,216 | 232,274 | 0.599 | 53 | 5 of 5 |
| run-1 challenged | 24 | 3,448 | 45,970 | 200,330 | 0.477 | 39 | 5 of 5 |
| run-2 first | 32 | 5,545 | 54,558 | 308,685 | 0.609 | 60 | 5 of 5 |
| run-2 challenged | 30 | 3,961 | 47,486 | 268,702 | 0.513 | 49 | 5 of 5 |
| run-3 first | 36 | 5,997 | 51,451 | 349,232 | 0.602 | 81 | 5 of 5 |
| run-3 challenged | 44 | 6,537 | 55,516 | 428,373 | 0.661 | 70 | 5 of 5 |

All 30 answers were correct. Per question and the answers byte for byte, in `cost/run-<n>/measure.md`. Every `first` setup is one `CLAUDE.md`, written without asking; every `challenged` setup rewrote it and added a check file the agent can run against new notes (`qa-checks.md` or `AGENT-CHECK.md`).

## What diverged

* The judge is not the author. After the runs the author asked the agent to take care of the judging; the pairs were scored and the measurement answers marked by fresh sessions of the model that wrote the answers. A model judging its own model's answers may share its taste; the scores are the judge's, not a reader's.
* "Three tabs that switch" was checked from the card's JSON, not by rendering each card in the Adaptive Cards Designer with the Microsoft Teams host. No card has a toggle whose target is missing; whether every element renders in Teams was not seen.
* Blindness is partial. In the audience arm the first answers wrote no file, so the side holding only `answer.md` is the first answer. In limit 3 the judge noted that one answer "refers to rounds the person never saw", which marks it as the later one. In the cost arm the challenged side has more files.
* Protocol turn 4 failed in all nine runs on its first sending: the host answered "You've hit your session limit" and no model turn ran. Those records were deleted, and the same message was sent again to the same sessions about 30 minutes later, the same day, with the same host version.
* `first/` and `challenged/` hold only the files the agent added or changed against `start`, not copies of the starting point; no run deleted a file. The report and the cost project are kept once, in `<arm>/start/`.
* The agents saw the run folder's git history: cost 3 found that its first `CLAUDE.md` was in the commit `first` and its revision was not, and cost 2 described the history as one import by "experiment".
* The cost runs started subagents (12 `Agent` calls in all), and so did the session that generated the cost project; `turns.txt` shows each call, not what the subagents did inside.
* The page's premise, from Case A, that an agent calls tabs impossible, did not reproduce: on this model and host the first answer already built switching tabs. What the protocol changed was the look, the phone, the board's time and the cost of each question, as the tables show.

## How to repeat

Copy `<arm>/start/` (without `cost/start/questions.md`) into a fresh folder and `git init` it; send the task of `prompts.md` with the command above, commit, then the four protocol turns with `--resume`, answering any question only from `<arm>/brief.md`; commit. For the cost arm, ask the five questions of `questions.md` read-only in a copy of each state. Put the two answers of a pair behind a coin and score them on `rubric.md` before you look at which is which.

## Files

* `prompts.md`: the tasks, the protocol and the generation prompts. `rubric.md`: the rubric.
* `<arm>/brief.md`, `<arm>/start/`: the brief and the starting point.
* `<arm>/run-<n>/turns.txt`: every turn, the message sent, the agent's text blocks byte for byte and tool calls as `[tool <name>] <relative path or command>`; `questions.md`; `first/`, `challenged/`.
* `cost/run-<n>/measure.md`: the measurement. `blind/key.md`, `scores.md`, `sources.md`: the key, the scores, the sources check.

The files are byte for byte, except absolute paths, replaced by `<run>` (the run folder) in `turns.txt`, `questions.md` and `measure.md`. Session ids are left out.
