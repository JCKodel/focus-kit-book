# brainstorm

**Objective.** After chapter 7 the reader can run `/brainstorm` on a new project, answer its questions (or say "your call"), choose a stack by the project's value and by how well the agent knows it, and review the documents it writes before committing them.

**Behaviour.**

* The reader can say what `/brainstorm` asks, in its order: the product, the vocabulary, how it is built (with FOCUS and git), the conventions, the process slots, the first milestone. They can also say what it writes: docs/00 to 06, docs/adr/, `AGENTS.md`, `CLAUDE.md`, `work/done/`. It writes no code.
* The reader knows that "your call" is a valid answer: the command states its default and asks whether it holds, so a person who cannot answer still gets a good document.
* The reader can choose a stack by three questions, in order: what the project needs (its value), how much public code the agent learned from, and whether the agent can check its own work there (types, tests). They can say why the clinic's stack answers them.
* The reader can run `/brainstorm` on the clinic with this chapter's brief and compare what they get with `book-v1/brainstorm`.
* The reader reviews what the command wrote against what they answered, and asks the agent for a correction by conversation, never by editing the file by hand (chapter 6). The person validates; the agent's text reads as right even when it is wrong.

**Contract.**

Chapter 7, `book/en/07-brainstorm.md` and `book/pt/07-brainstorm.md`:

* Title: "`/brainstorm`, a new project" / "`/brainstorm`, um projeto novo" (reworded if the heading renders badly with code).
* Voice: instruction to the reader as "you"; the run is the author's, one clause at most.
* Sections, in order (headings may be reworded; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. What it asks. The six subjects in order, one line each, and the "your call" rule. Say that it writes no code: the first delivery does, with its own page.
  3. Choosing the stack. The three questions of Behaviour, one short paragraph each. The second carries the public measure (below). Ninjobs is one sentence and a link to chapter 4, no retelling. Then the clinic's answer: TypeScript, a React PWA, a small Node server, SQLite in a file, no paid service, one sentence of reason each. Say that the brief gives this stack, so the chapter shows the criteria behind the answer, not a live choice.
  4. The run on the clinic. Context first: the clinic at `book-v1/install-and-hosts`, and the brief (shown whole, English in both editions, translated in Portuguese). Then one round of the agent's questions and the answers given, from `questions.md`, byte for byte, translated in Portuguese. Then the files it wrote (`git status --short`), then three excerpts quoted at the tag: the clinic's docs/00 §Purpose, `AGENTS.md` §Non-negotiables and docs/06 (its first milestone). Each excerpt has context before it and one sentence after it on what to see. These three answer earlier chapters: chapter 5 said chapter 7 writes `AGENTS.md`, and exercise 6.2 compares the reader's hand-written Purpose and non-negotiables with these.
  5. Review before you commit. What to check: every brief answer landed in the document that owns it, each "your call" default is one you accept, every ADR records a decision you took. A fix is asked of the agent in the same session. If the author's review asked for a fix, show it (the request and the diff) as the example. If not, the section says how to ask, with no invented example.
  6. Key points, at most five.
  7. Exercises (below).
* The brief, saved as `work/done/brainstorm-run/brief.md` and given as answers, word for word (the same shape as chapter 3's brief):

  ```
  # Brief

  ## Product
  A scheduling app for one neighbourhood clinic. Clients book and cancel their own appointments with the clinic's professionals from their phones; the owner registers the professionals and their weekly hours.
  Two sides: the client, who has no account and gives a name and a phone number; the owner, who signs in (your call how).
  Rules: a professional cannot have two appointments at the same time. A client can cancel their own appointment up to 24 hours before it starts; a cancelled appointment frees its slot; a later cancellation is refused with a message that says why. Times are the clinic's local time.
  Not: payments, notifications (SMS, email, push), medical records or any health data, more than one clinic.

  ## Stack
  TypeScript, strict. A React PWA that the client and the owner open in the browser, over a small Node server that keeps the data in a SQLite file. No paid service: it runs on a machine at the clinic or on any free host.
  Why: the most public code the agent learned from is in this language and library, and types and tests let it check its own work.

  ## Choices
  FOCUS: FOCUS whole. Git: trunk.

  ## Conventions and process
  English for documents and identifiers. Verify: created by the first delivery. Everything else: your call.

  ## First milestone
  When it closes, the owner can register professionals and their weekly hours, a client can book a free slot, and a client can cancel up to 24 hours before. A professional's absences and the owner's view of the day come in the second milestone.

  ## Principles
  Keep it simple. Every rule has a test. No em dash in any document.

  ## Rule for a question the brief does not answer
  Answer "your call".
  ```

* The run, the same mechanism as chapter 3's run (the first occurrence, `work/done/spec-driven-run.md`). It uses Claude Code headless (`claude -p "/brainstorm"`), inside `../focus-kit-clinic` at `book-v1/install-and-hosts`, with `--setting-sources project --strict-mcp-config` as in chapter 5, and the least permission mode that lets it finish (recorded). There is no `--no-session-persistence`, because each answer is `--continue`. Each answer is the text of the brief's section or sections for the subject asked, word for word, or "your call" when no section answers. /apply writes no other words. If the agent tries the host's question form and headless mode cannot show it, /apply answers the same questions as text and records that. The run is recorded in `work/done/brainstorm-run/`: `brief.md`, the exact commands, `claude --version`, the model, the full output of every turn, `questions.md` (each question and its answer, in order), and `git status --short` after it. Paths are relative to the clinic; a replaced absolute path is recorded here.
* Em dash. If the raw output holds one, the check's exemption widens from `work/done/spec-driven-run/` to `work/done/*-run/` (chapter 3 first, this run the second occurrence), in `scripts/check_em_dash.py`, docs/01 and docs/04. If a generated clinic document holds one despite the brief, /apply asks the agent in the same session to remove it, as a recorded turn. The document is then real as committed, and the fix is a finding for section 5.
* The author reviews the clinic's documents before /apply stages them. A correction the author asks for is made by a recorded turn to the same session, never by hand.
* Numbers, and only these: six (subjects); 24 hours (the brief's rule); the public measure of section 3, sourced; the Claude Code version and model in the run's source note only.
* docs/03 terms used: command, project documents, rules file, ADR, open decision, slot, verify, queue, milestone, delivery, page, fresh session, FOCUS, trunk, guided project, chapter tag. No new term: "brief" is a word of the book's runs, not of the method.
* Sources (`[^key]`, same keys in both editions):
  * `[^focus-kit-brainstorm]`: the clinic's `.claude/skills/brainstorm/SKILL.md` and `references/documents.md` §Choices, as installed at `book-v1/install-and-hosts` (focus-kit `26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b`).
  * `[^octoverse]`: GitHub, "Octoverse", the latest report, for the ranking of languages by contributors on GitHub. /apply fetches it, checks what it says about TypeScript and JavaScript, and cites the figure it finds. If the report does not support "the most public code", the chapter says what it does support and this page records the difference.
  * `[^brainstorm-run]`: the run, `work/done/brainstorm-run/README.md`, and the chapter tag.
* Code and documents of the clinic are quoted at `https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/brainstorm/<path>`, never copied here beyond the excerpts.
* Cases: Ninjobs only as the link to chapter 4. No Case A or B. No OD-3 approval.
* Exercises, on the guided project (answers belong to the `exercise-answers` appendix):
  * 7.1: check out `book-v1/install-and-hosts` on a branch of your own, run `/brainstorm` with the brief, and compare with `book-v1/brainstorm`. What differs, and does any difference break a brief answer?
  * 7.2: take the Purpose and non-negotiables you wrote in exercise 6.2 and compare them with the clinic's. What did the conversation add that you did not write?
  * 7.3: pick a stack for a project of your own by the three questions of section 3, and say which question decided it.

Guided project, `../focus-kit-clinic`: the files the run wrote, staged by /apply after the author's review; nothing committed, tagged or pushed by the agent. The author's commands, written here and in the commit body:

```
cd ../focus-kit-clinic
git commit -m "Brainstorm: documents and first milestone"
git tag -a book-v1/brainstorm -m "One Page at a Time, chapter brainstorm"
git push origin main book-v1/brainstorm
```

Then the chapter's `make verify` can go green (docs/05 §5 order).

Files:

```
book/en/07-brainstorm.md             chapter 7, no status: draft when done
book/pt/07-brainstorm.md             chapter 7, no status: draft when done
work/done/brainstorm-run/            brief, commands, version, model, output, questions.md, git status
../focus-kit-clinic/                 docs/00 to 06, docs/adr/, AGENTS.md, CLAUDE.md, work/done/.gitkeep, staged
docs/adr/ADR-0008-guided-project.md  amendment dated at /apply: a small Node server keeps SQLite in a file, since both sides share the data; the clinic has a docs/02
docs/06-Queue.md                     brainstorm [x]
scripts/check_em_dash.py, docs/01, docs/04   only if the run's output holds an em dash
```

**Out of scope.**

* `/analyze` and the brownfield project: chapter 8.
* How the queue and marks work: chapter 9; here the queue is only shown.
* Writing the first page or any code: chapters 10 and 11.
* FOCUS in detail: Part III. The choice is one sentence pointing there.
* A measured experiment of two stacks: it would be its own `*-run` delivery; one public source is enough here.
* Absences and the owner's view of the day: the clinic's second milestone.
* Changing `SETUP.md` or the kit's skills: another repository.

**Done when.**

* [x] Run recorded in `work/done/brainstorm-run/`; every answer is a brief section word for word or "your call".
* [x] The author reviewed the clinic's documents; the files are staged in `../focus-kit-clinic` and nothing is committed there by the agent.
* [x] ADR-0008 amended.
* [x] Both editions written, same headings in the same order, no `status: draft`.
* [x] Opens with its value in at most three sentences; at most five key points; exercises 7.1 to 7.3.
* [x] No filler and nothing useful cut: every sentence read against docs/00 product question 2.
* [x] Every excerpt matches the clinic at the tag byte for byte (English), translated in Portuguese with the note; context before, one sentence after.
* [x] Only the Contract's numbers, sourced; the Octoverse page checked on the day.
* [ ] The author commits and pushes the clinic and its tag; then `make verify` green (build, parity, em dash, prose, links including the tag URLs, disclosure).
* [x] `make book` builds; both PDF paths given to the author.
* [x] docs/06 marked `[x]`; page moved to `work/done/brainstorm.md` with what happened.

The unticked item is the author's: it ticks when the clinic's commit and tag and this repository's commit are pushed and `make verify` is green.

**What happened.**

The run, 2026-09-28: Claude Code 2.1.283 (chapter 5's run was 2.1.282), model `claude-opus-5-5`, one session of six turns, all in `acceptEdits`. Everything is in `brainstorm-run/README.md`.

Diverged from the plan:

* Subject 6 was never asked. After the round on conventions and process the agent wrote every document, and its milestone 1 held `owner-schedule` and a paragraph where the owner "sees the day's schedule", against the brief. The author's review chose the fix: turn 6 sent the brief's section First milestone, word for word, to the same session. The agent rewrote the paragraph with the brief's sentence and added milestone 2 (`absences`, `owner-schedule`, `deploy`), moving `deploy` there on its own reasoning, which the author accepted. This is the example of section 5, with the request and the diff; `brainstorm-run/questions.md` records it as the round that did not happen.
* No question form: headless mode lists no question tool, so the agent asked in text from the start, and every answer went as text. Four rounds: product; product gaps with vocabulary; how it is built; conventions and process.
* Answer mapping: the product round asked what a good decision looks like, so its answer was Product and Principles; the gaps and vocabulary round, which no section answers, got "your call"; the round on how it is built got Stack and Choices; the conventions and slots round got Conventions and process. No other word was written.
* `acceptEdits` denied two shell commands of turn 5 (the agent's own em dash search and `git status`); the agent wrote `CLAUDE.md` and `work/done/.gitkeep` with its file tool and said the search had not run. /apply ran it: no generated document holds an em dash.
* Em dash: the host's denial message, in `turn-5.txt`, holds one, so the check's exemption widened from `work/done/spec-driven-run/` to `work/done/*-run/` (chapter 3's run the first occurrence, this one the second), in `scripts/check_em_dash.py`, docs/01 and docs/04 §Tests. It also covers `install-and-hosts-run/`, which holds none.
* The recorded output is a transcript per turn derived from `--output-format stream-json --verbose`: the text blocks byte for byte, each tool call as its name and path or command, each tool error whole. The raw streams stayed outside the repository: they carry the clinic's absolute path and the results of the agent's reads, among them a directory listing with the local user name. The absolute path was removed from the tool calls, so every path is relative to the clinic.
* The session id was dropped from the run's README: the disclosure scan matched it.
* The round the chapter shows is the one on how it is built, not the first: it is where the agent reasons from the product's needs to a stack (SvelteKit), and where the brief's answer overrides it, so it teaches section 3's criteria. It is quoted from the section heading on, a whole unit, without the lead sentence that closed the previous round.
* The files are shown by `git status --short` as it printed after turn 5 (four collapsed lines), then named in prose, as chapter 5 did.
* The Portuguese edition shows every prose artifact (the brief, the round, the answers, the three excerpts) translated with a note, as chapter 6 does; the `git status` output and the diff stay as they ran, and the diff's new milestone 2 paragraph is translated in the sentence before it.
* The Octoverse report: the latest on 2026-09-28 is Octoverse 2025 (published 2025-10-28, updated 2026-02-28). It supports that TypeScript was the most used language on GitHub by monthly contributors in August 2025 (2,636,006), ahead of Python and JavaScript; it does not measure how much code there is, or what a model trained on. The chapter says it counts people, not lines of code, and reads it as a ranking; the brief's own "Why" line stays word for word, as given.
* React's reason in section 3 is chapter 4's Ninjobs fact (the agent got the design right in React), not a public measure: Octoverse ranks languages, not libraries.
* Numbers: besides the Contract's, the chapter holds "August 2025" as the date of the Octoverse figure, and the excerpts carry the clinic's own ("30 days"), quoted as written.
* The title keeps the code span; the site navigation and the PDF show it as "/brainstorm, a new project".

Dropped: nothing of the Contract.

The proof: build, parity, em dash and prose green; links red only on the three clinic tag URLs and the run's README on `main`, in both editions, which answer after the author's push; disclosure green (`scripts/check_disclosure.py`), and the 15 staged clinic files match no entry of the list. Every excerpt of the English edition was compared by script with its source (the clinic's files, `questions.md`, `brief.md`, `turn-6.diff`, `git-status.txt`): all byte for byte. `make book` built both PDFs and EPUBs; its only warnings are the `user-select` ones earlier chapters also print.

Decisions: no ADR. ADR-0008 amended (the Node server and the clinic's docs/02); docs/03 unchanged, no new term.

The author's commands, after reviewing the staged clinic files:

```
cd ../focus-kit-clinic
git commit -m "Brainstorm: documents and first milestone"
git tag -a book-v1/brainstorm -m "One Page at a Time, chapter brainstorm"
git push origin main book-v1/brainstorm
```
