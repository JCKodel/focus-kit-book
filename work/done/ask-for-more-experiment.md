# ask-for-more-experiment

**Objective.** The author knows from one recorded experiment what the challenge protocol adds to an agent's first answer on three lending-library tasks (a limit the agent may call impossible, a reader with little time, a cost paid every day). The book's research numbers are checked against their primary sources. Chapter 25 can cite both, and a reader can check them and repeat the experiment.

**Behaviour.**

* Three arms (limit, audience and cost) each start from a frozen starting point and receive the same task, word for word, in every run.
* Each run is one session. It first records the first answer. It then sends the challenge protocol's four turns, word for word, and records the challenged answer. Every run yields one pair: a first answer and a challenged answer.
* Every question the agent asks is answered from the arm's brief. A question the brief does not answer gets "Use your judgment." Each question and answer is recorded.
* Three runs per arm on the same day, the same model and the same host version.
* The author judges every pair blind. The two answers carry the labels X and Y, drawn at random per pair, and the key stays sealed until the author's scores are recorded. The author scores each answer on the arm's rubric and says which of the two they would send.
* What can be counted is counted: for each answer, tokens by kind, cost and time; in the limit arm, whether the card shows three tabs that switch; in the audience arm, words; in the cost arm, the tokens, cost and correct answers of five fixed questions asked of each setup.
* Every number the research report left unverified is checked against its primary source and recorded as confirmed, corrected or not to be used.
* The author reads the tables and the scores before `ask-for-more-chapter` is proposed. A run where the first answer is already as good as the challenged one is a result and is reported, not dropped.

**Contract.**

Where: the runs happen outside the repository, in `<scratch>/ask-for-more/<arm>/run-<n>/` for `<arm>` in `limit`, `audience`, `cost` and `<n>` in 1 to 3, never in or next to the author's private material. Only the files listed under "Committed" enter the repository. Each run folder is a git repository. The agent's working files are committed after the first answer (`first`) and after the last protocol turn (`challenged`), so both states and their diff are kept.

Starting points, built once by /apply, then copied into each run folder:

* **limit**: a `README.md` with one line, "A lending library's members see their loans in Microsoft Teams." No other file.
* **audience**: `annual-report.md`, the lending library's annual report for one year. About 30 A4 pages (12,000 to 15,000 words), with at least 10 tables, sections on loans, members, the collection, overdue books, staff, costs and next year's plan. It is generated once with the same model, in a session of its own, from the prompt recorded in `prompts.md`. Its figures are synthetic, and the report says so on its first line. The author reads it before the runs.
* **cost**: a lending-library TypeScript project in vertical slices (`features/loans/`, `features/members/`, `features/books/`, with tests). It holds a `notes/` folder of about 40 pages: meeting notes, decisions, a glossary and two outdated design drafts, with no index and no `AGENTS.md`. It is generated once in a session of its own, from the prompt in `prompts.md`. Before the runs, /apply writes `questions.md`: five questions about the project, each with its answer and the file that holds it. The answers are not given to the agent. The author reads both before the runs.

Tasks, the first message of each run, verbatim:

* **limit**: "Build a Microsoft Teams card that shows a member's loans in three tabs: Active, Overdue and History. Use sample data for one member with two active loans, one overdue and three returned. Save it as card.json."
* **audience**: "Summarize annual-report.md for the board."
* **cost**: "Every day an agent will answer the team's questions about this project. Set the project up for it."

Briefs, `<arm>/brief.md`, the facts the person knows but did not say:

* **limit**: the members open the card in Teams on desktop and phone; the library wants it to look like a small app, not a list; any feature that Teams' Adaptive Cards support may be used.
* **audience**: the board has 10 minutes for this item, reads on a phone before the meeting, and decides next year's budget. They want what changed, what it cost and what they must decide. The full report stays available to anyone who asks.
* **cost**: the questions come from developers and the product owner, about 20 a day. Each question opens a fresh session. The notes keep growing. The project pays for every token.

The challenge protocol, turns 2 to 5 of every run, verbatim, each sent when the previous turn ends:

1. "Before you change anything, ask me what you need to know to do this well."
2. "What did you say is not possible, or not worth doing? Test each one and show me the result."
3. "Who reads or uses this, how much time do they have, and what does each use cost? Change the result to fit."
4. "What did I not ask for that I would want? Add what is worth it, and tell me what you left out."

After protocol turn 1 (the run's turn 2) the agent's questions are answered from the brief, in one message, before turn 2 of the protocol is sent. A turn where the agent asks something else is answered the same way and recorded.

Runs: Claude Code headless, model `claude-opus-5-5`. Each run is one session: `claude -p` for the task, then `--resume <session id>` for every later turn, never `--continue`. The flags are `--setting-sources project,local --strict-mcp-config` and `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, in the least permission mode that lets the task finish (recorded), with `--output-format stream-json --verbose` so every turn's usage is kept.

The cost arm's measurement: for each of its six setups (three `first`, three `challenged`), the five questions of `questions.md` are asked one per fresh headless session in a copy of that setup, read-only (`--allowedTools "Read" "Glob" "Grep"`), 30 sessions in all. For each setup: input, output, cache-write and cache-read tokens, cost, and how many of the five answers the author marks correct against `questions.md`.

Blind judging: /apply copies each pair's two answers to `blind/<arm>-<n>/X/` and `blind/<arm>-<n>/Y/`, the side drawn by a random coin per pair. The key goes to `key.md`, which the author does not open until `scores.md` is filled. The rubric, `rubric.md`, scores 1 to 5 per criterion:

* **limit**: does what was asked; looks like a small app; works on the phone. Counted apart: three tabs that switch in the Adaptive Cards Designer with the Microsoft Teams host, yes or no.
* **audience**: a board member can decide in 10 minutes; nothing the decision needs is missing; every figure matches the report.
* **cost**: an agent finds what it needs without reading everything; the setup stays right as the notes grow; it is easy for a person to keep up to date.
* For every pair: "Which would you send, X or Y?"

Counted per answer, from the stream-json usage and the files: input, output, cache-write and cache-read tokens; cost in USD; seconds; for audience, words in the summary (and in any other file it wrote); for limit and audience, the sentences of the first answer that call something not possible, as the author marks them.

Sources check, `sources.md`: one row per number or quotation the research report marks unverified or secondary. At least Skitka, Mosier and Burdick 1999 (41% against 3%, 65%, N=80), Dell'Acqua et al. 2023 working paper against Organization Science 2026 (quality 40% against 30 to 34%, 43% against 17%, "19% less likely" against "19 percentage points"), Randazzo et al. (60%, 14%, 27%, 44%, sample size), Kosmyna et al. 2025 (published since?), Simon's "satisfice" quotation and page, the venues the report could not confirm, and METR 2025's intervals. Each row: the claim, the primary source with its URL or DOI, what it says, and the verdict: confirmed, corrected to, or not to be used.

Committed, `work/done/ask-for-more-experiment-run/`:

```
README.md                  date, claude --version, model id, Node, permission mode, every command and flag, how to repeat, the tables (per arm: first and challenged, per run and total), what diverged
prompts.md                 the three tasks, the protocol, the prompts that generated annual-report.md and the cost project
rubric.md                  the rubric, as above
<arm>/brief.md             the brief
<arm>/start/...            the starting point (the report; the cost project with notes/ and questions.md)
<arm>/run-<n>/turns.txt    every turn: the message sent, the agent's text blocks byte for byte, tool calls as [tool <name>] <relative path or command>
<arm>/run-<n>/first/...    the files after the first answer
<arm>/run-<n>/challenged/...  the files after the last turn
<arm>/run-<n>/questions.md each question the agent asked and the answer given
cost/run-<n>/measure.md    the 5 questions per setup: tokens, cost, the author's correct or not
blind/key.md               the X and Y key, opened after scoring
scores.md                  the author's scores and choices, filled blind, the key applied after
sources.md                 the sources check
```

The files are kept byte for byte, except an absolute path, which is replaced by `<run>` and listed in README.md. Session ids are left out.

Other files changed:

```
docs/06-Queue.md           ask-for-more-experiment [x]
```

The em dash check already skips `work/done/*-run/`. The disclosure scan keeps covering the folder.

**Decided for `ask-for-more-chapter`**, which /propose reads from here:

* Chapter 25 is the book's last chapter, and the prologue gets a seed. No chapter is renumbered.
* The chapter opens with Case A's Teams card. It is paraphrased: the client was disappointed with the look; the agent had said tabs were not possible; asked to test what the card renders, it found more, and the client was pleased. The email is never quoted. Microsoft Teams and Adaptive Cards are named as technology. The text is listed for the author's approval (OD-3).
* The meeting that started this milestone is not used.
* Chapter 2 (context, index) and chapter 23 (cost, cache) hold the technique; chapter 25 points to them.

**Out of scope.**

* Chapter 25 and the prologue seed: `ask-for-more-chapter`.
* Other models and more runs: three pairs per arm, said plainly. Statistics would be a study.
* Rendering in a real Teams tenant: the Adaptive Cards Designer with the Teams host stands in for it, and the README says so.
* Case A's own card and client: nothing private enters the run.
* A judge other than the author: the README says the judge wrote the book.

**Done when.**

* [x] The starting points are generated, read by the author and frozen; `questions.md` is written before the runs.
* [x] Nine runs finished on the same day, with the same model and host version, each with its `first` and `challenged` states committed in the run folder.
* [x] The 30 cost measurement sessions finished, and each answer is marked (by a fresh session, not the author: see What happened).
* [x] `scores.md` was filled before `key.md` was opened (by the blind judge sessions), and the README's tables are counted from the files.
* [x] `sources.md` has a verdict for every row.
* [x] `grep -rE '/Volumes|/Users|/home|/private' work/done/ask-for-more-experiment-run` finds nothing.
* [x] `make verify` is green, disclosure included.
* [ ] The author has read the tables and the scores. The page is moved to `work/done/ask-for-more-experiment.md` with what happened, and docs/06 is marked `[x]`. (Moved and marked; this box ticks when the author has read the tables in the record's README.)

**What happened.**

* The record is `ask-for-more-experiment-run/`; its README has the commands, the tables and what diverged.
* The judge changed. After the runs the author asked the agent to take care of the judging and the marking. Each of the nine pairs was scored blind by a fresh read-only session of `claude-opus-5-5`, the model that wrote the answers, with the key applied after; the 30 measurement answers were marked by one fresh session per question, with the six setups under shuffled letters. "A judge other than the author" was out of scope; the README says plainly who judged.
* Results: the judge would have sent the challenged answer in 9 of 9 pairs; rubric sums, first against challenged, out of 45: limit 31 against 39, audience 36 against 44, cost 24 against 39. The challenged session cost 2.6 to 8 times the first answer (whole session against turn 1: limit 0.82 against 6.59 USD for three runs, audience 1.09 against 3.39, cost 3.04 against 8.00). In the cost arm all 30 answers were correct in both states; per five questions the challenged setup cost 20% and 16% less in runs 1 and 2 and 10% more in run 3.
* Case A's premise did not reproduce: no first answer called tabs impossible, and all six cards switch tabs. The protocol's gain was the look, the phone, the board's ten minutes, and the setup's upkeep and cost, not a limit taken back. `ask-for-more-chapter` must say so if it opens with Case A's card.
* The sentences of the first answers that call something not possible were marked by /apply, not the author.
* "Three tabs that switch" was checked from the JSON (three panels, every toggle target present), not in the Adaptive Cards Designer.
* Permission mode, chosen by the author: `acceptEdits` with `--permission-prompts none`. Every `Bash` call was denied (41), and every write to `.claude/settings.json` (6); `WebFetch` was allowed and the limit runs used it 20 times.
* Protocol turn 4 hit the host's session limit in all nine runs on its first sending; those records were deleted and the turn was sent again to the same sessions the same day, same host version.
* Six runs asked, after protocol turn 2, whether to apply their proposals; each got "Use your judgment." as an extra recorded turn.
* `first/` and `challenged/` keep only the files the agent added or changed; the starting point is kept once in `<arm>/start/`. The audience arm's first answers wrote no file, so its blind sides are told apart by shape; the README says so.
* `sources.md` (42 rows): 29 confirmed, 11 corrected, 2 not to be used. The corrections that matter to chapter 25: Skitka 1999's 65% is the mean share of six wrong recommendations followed, not 65% of participants; Dell'Acqua's quality gain in the published 2026 article is 29.9% to 33.9% (about 32%), and the drop outside the frontier is 19 percentage points; Dell'Acqua 2022 has no "99%" condition; Lee et al.'s p-values are already corrected.
* No ADR: the change of judge is this delivery's, recorded here and in the README.
