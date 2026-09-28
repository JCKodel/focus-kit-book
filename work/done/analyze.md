# analyze

**Objective.** After chapter 8 the reader can run `/analyze` on an existing project, answer its one round of questions, and check the documents it writes against the code before committing them.

**Behaviour.**

* The reader can say how `/analyze` differs from `/brainstorm`: it reads first (README, existing docs, manifests, the tree, entry points, tests, CI, the last fifty commit subjects, any rules file), it asks one round of four subjects only (documentation language, purpose when no README says it, FOCUS and git, the first milestone), and it describes what exists, not what should exist. It changes no code.
* The reader knows that on an existing project the default of each choice is what the code already does, and that the agent says what that is.
* The reader knows that where the code contradicts itself, `/analyze` records an open question and does not ask the person to settle it now.
* The reader knows that an existing rules file (`CLAUDE.md`, `.github/copilot-instructions.md` and the like) moves into `AGENTS.md`.
* The reader can run `/analyze` on CLAHub at `book-v1` with this chapter's brief and compare what they get with `book-v1/analyze`.
* The reader checks each statement the agent marked as observed against the code, and asks for a correction by conversation, never by editing the file by hand (chapter 6).

**Contract.**

Chapter 8, `book/en/08-analyze.md` and `book/pt/08-analyze.md`:

* Title: "`/analyze`, an existing project" / "`/analyze`, um projeto existente".
* Voice: instruction to the reader as "you"; the run is the author's, one clause at most.
* Sections, in order (headings may be reworded; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. What changes from `/brainstorm`. What it reads, in one list; the four subjects of its round, one line each; observed, not asked; contradictions become open questions; existing rules files move into `AGENTS.md`; it shows the diff before writing and changes no code. Point to chapter 7 for what is the same, with no repetition.
  3. The project. CLAHub in one paragraph: what it does, its stack, its size and tests (numbers below), why it was chosen in one sentence citing `brownfield-research`, and that it is frozen at `book-v1` in the fork. The kit was installed first as chapter 5 shows: one sentence, no retelling.
  4. The run on CLAHub. The brief, shown whole (English in both editions, translated in Portuguese). Then the round of questions and the answers given, from `questions.md`, byte for byte (translated in Portuguese). Then the files it wrote (`git status --short`). Then excerpts quoted at the tag, each with context before and one sentence after: the stack and organization as the agent inferred them (the clinic's docs/01 counterpart), one open question the agent recorded, and docs/06 with the first milestone built from the issues. If the run records the drift `brownfield-research` found (the README says `.env.local`, `prisma.config.ts` reads `.env`), that is the open-question excerpt; if not, the chapter shows the one it did record and does not mention the drift.
  5. Check it against the code. On an existing project the review is a check of facts: every observed statement is true in the code, every open question is real, nothing describes what should exist. If the author's review asked for a fix, show the request and the diff; if not, say how to ask, with no invented example.
  6. Key points, at most five.
  7. Exercises (below).
* The brief, saved as `work/done/analyze-run/brief.md` and given as answers, word for word:

  ```
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

* The fork, before the run. Precondition: the author has done the two open items of `brownfield-research` (`JCKodel/clahub` forked, `book-v1` pushed on `9d1e666e1d30f271aea9640393229a7cbfbd1b62`); /apply checks the tag and stops if it is missing. The fork is worked on in the sibling directory `../clahub`, on a branch `book` created from `book-v1`. /apply installs the kit there from `SETUP.md` at focus-kit `26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b`, the commit chapter 5 installed in the clinic, the same way chapter 5 did, recorded in `work/done/analyze-run/install/`. It stages the install and stops. The author commits it (`git commit -m "Install focus-kit"`) and /apply resumes, so `/analyze` runs on a clean tree.
* The run, the same mechanism as chapter 7's run (the second occurrence; the first is `work/done/spec-driven-run.md`). It uses Claude Code headless (`claude -p "/analyze"`), in `../clahub` on `book`, with `--setting-sources project --strict-mcp-config`, and the least permission mode that lets it finish (recorded). Each answer uses `--continue` and is the text of the brief's section or sections for the subject asked, word for word, or "your call" when no section answers. /apply writes no other words. The record goes in `work/done/analyze-run/`: `brief.md`, the exact commands, `claude --version`, the model, a transcript per turn derived from `--output-format stream-json --verbose` as in chapter 7 (text blocks byte for byte, tool calls by name and relative path, tool errors whole; raw streams stay outside the repository), `questions.md`, and `git status --short` after it. Paths are relative to the fork.
* The author reviews the generated documents before /apply stages them. A correction is a recorded turn to the same session, never an edit by hand.
* Numbers, and only these: four (subjects); fifty (commit subjects it reads); 11,902 TypeScript code lines and 259 passing tests, from `brownfield-research`; three (issues); the Claude Code version and model in the run's source note only.
* docs/03 terms used: command, project documents, rules file, ADR, open decision, slot, verify, queue, milestone, delivery, fresh session, FOCUS, trunk, brownfield project, chapter tag. No new term; "chapter tag" was widened to cover the fork in this `/propose`.
* Sources (`[^key]`, same keys in both editions):
  * `[^focus-kit-analyze]`: the fork's `.claude/skills/analyze/SKILL.md` as installed at `book-v1/analyze`, from focus-kit `26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b`.
  * `[^brownfield-research]`: `work/done/brownfield-research.md` on `main`, for the choice, the size and the tests.
  * `[^analyze-run]`: `work/done/analyze-run/README.md` on `main`, and the chapter tag.
* CLAHub's files are quoted at `https://github.com/JCKodel/clahub/blob/book-v1/analyze/<path>`, never copied here beyond the excerpts.
* Cases: none. No OD-3 approval.
* Exercises, on the brownfield project (answers belong to the `exercise-answers` appendix):
  * 8.1: clone the fork at `book-v1` on a branch of your own, install the kit (chapter 5), run `/analyze` with the brief, and compare with `book-v1/analyze`. What differs, and is any difference wrong about the code?
  * 8.2: pick three statements of `book-v1/analyze`'s docs/01 or docs/04 and find each in the code. Which is the file that proves it?
  * 8.3: run `/analyze` on a repository of your own. Which open questions did it record, and which of them would you have missed?

Brownfield project, `../clahub`: the author's commands, written here and in the commit body. After the install is staged:

```
cd ../clahub
git commit -m "Install focus-kit"
```

After the documents are reviewed and staged:

```
cd ../clahub
git commit -m "Analyze: documents and first milestone"
git tag -a book-v1/analyze -m "One Page at a Time, chapter analyze"
git push origin book book-v1/analyze
```

Then the chapter's `make verify` can go green (docs/05 §5 order).

Files:

```
book/en/08-analyze.md                chapter 8, no status: draft when done
book/pt/08-analyze.md                chapter 8, no status: draft when done
work/done/analyze-run/               brief, install/, commands, version, model, transcripts, questions.md, git status
../clahub/                           on branch book: the kit (first commit), then docs/00 to 06, docs/adr/, AGENTS.md, CLAUDE.md, work/done/.gitkeep, staged
docs/adr/ADR-0009-brownfield-by-research.md   amendment dated at /apply: the fork gets a branch book from book-v1 and the chapter tag book-v1/analyze; book-v1 stays the frozen upstream
docs/05-Process.md                   §5, a "Brownfield project" slot next to "Guided project": ../clahub, branch book, chapter tag, the agent stages and never commits, tags or pushes
docs/01-Architecture.md              the brownfield line: the book quotes the fork at book-v1 and book-v1/analyze
docs/03-Domain.md                    chapter tag widened to the fork (done in this /propose)
docs/06-Queue.md                     analyze [x]
```

**Out of scope.**

* Building any of the three issues: that would be `/propose` and `/apply` on CLAHub, which the book does on the clinic (chapters 10 and 11).
* Fixing CLAHub's code or its README drift: `/analyze` changes no code; the drift, if found, stays an open question.
* How the queue and marks work: chapter 9.
* Running CLAHub or its tests in the chapter: `brownfield-research` did, and its numbers are cited.
* Changing `SETUP.md` or the kit's skills: another repository.
* Copying upstream issues into the fork: the brief cites them by upstream URL.

**Done when.**

* [x] `book-v1` exists on `JCKodel/clahub` at the recorded SHA before the run.
* [x] Kit installed and recorded in `work/done/analyze-run/install/`; the author committed it on `book`.
* [x] Run recorded in `work/done/analyze-run/`; every answer is a brief section word for word or "your call".
* [x] The author reviewed the generated documents; they are staged in `../clahub` and nothing is committed there by the agent.
* [x] ADR-0009 amended; docs/05 and docs/01 updated.
* [x] Both editions written, same headings in the same order, no `status: draft`.
* [x] Opens with its value in at most three sentences; at most five key points; exercises 8.1 to 8.3.
* [x] No filler and nothing useful cut: every sentence read against docs/00 product question 2.
* [x] Every excerpt matches the fork at the tag byte for byte (English), translated in Portuguese with the note; context before, one sentence after.
* [x] Only the Contract's numbers, sourced.
* [ ] The author commits and pushes the fork's branch and tag; then `make verify` green (build, parity, em dash, prose, links including the tag URLs, disclosure).
* [x] `make book` builds; both PDF paths given to the author.
* [x] docs/06 marked `[x]`; page moved to `work/done/analyze.md` with what happened.

The unticked item is the author's: it ticks when the fork's commit and tag and this repository's commit are pushed and `make verify` is green.

**What happened.**

The run, 2026-09-28: Claude Code 2.1.283, model `claude-opus-5-5`, one session of four turns, all in `acceptEdits`, the third with `gh issue view` allowed. Everything is in `analyze-run/README.md`; the install is in `analyze-run/install/`.

Diverged from the plan:

* The install used chapter 5's command unchanged (the raw `SETUP.md` on focus-kit `main`), because `main` was still at `26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b` on the day. Chapter 5's two failed attempts in `acceptEdits` were not repeated; the run went straight to `bypassPermissions`. All 36 files matched `SETUP.md` §3 byte for byte. The author committed it on `book` as `c3512ab`.
* The round asked the four subjects in one message, but not the purpose (the README says it), so the answer was the brief's sections Documentation language, Choices and First milestone, word for word. "Your call" kept the agent's defaults: FOCUS neither, a branch per delivery.
* `/analyze` did not show the diff before writing, although its own round promised to: headless, it wrote and reported. The chapter says so in section 5.
* `acceptEdits` let the command finish, but the host denied `gh issue view` and `WebFetch`, so the first queue named the issues by number only, against the Contract's "docs/06 with the first milestone built from the issues". The author's review chose a correction turn with `--allowedTools "Bash(gh issue view:*)"` and the request "Read the three issues with gh issue view and rewrite the milestone and its lines from them." (`turn-3.diff`).
* The run did not record the `.env` drift: docs/01 repeated the README's `.env.local` as observed. The author's review chose a second correction turn, "docs/01 says local setup uses .env.local. Check that against prisma.config.ts and the README, and correct docs/01; where they disagree, record an open question." (`turn-4.diff`). It corrected the line and recorded the drift and two more contradictions, both checked in the code by /apply (`NEXT_PUBLIC_APP_URL` in `cla-check.ts` and `contributing.ts`; Playwright loads `.env.local` before `.env.test`). So the drift is the open-question excerpt, with its origin stated, and section 5 shows both corrections: the `.env` one with its request and the first hunk of its diff (the second hunk is the section already quoted), the queue one with its request and the queue as first written (the `-` side of `turn-3.diff`), since its new side is the docs/06 excerpt of section 4.
* The fork had no rules file, so "an existing rules file moves into `AGENTS.md`" is taught from the command's text, with no example from the run.
* The organization excerpt is docs/01 §How the code is organized; the open question is the first entry of docs/01 §Open questions, a whole bullet under its heading.
* The transcripts carry the host's denial messages, which hold em dashes; `work/done/*-run/` is already exempt. The agent's `cd <fork>` reads `cd .` after the absolute path was removed. The session id is not recorded.
* `make book` printed "No anchor #brainstorm.md__chapter-07-brainstorm": chapter 8 is the first to link chapter 7, whose title opens with a code span, and `scripts/build_book.py` looked for the H1 on the masked line, where the code span is blank, so it never gave that title its id. Fixed in `prepare()` by checking the line itself; the first title that opens with code was chapter 7's, and no chapter linked to it before.
* Terms: the chapter says "open question", the command's word and the fork's docs/01 heading, for what docs/03 calls an open decision; no new term.
* Numbers: besides the Contract's, the prose holds only chapter and exercise numbers; the quoted artifacts carry their own ("Next.js 16", "Prisma 7", "3 to 8 deliveries", the issue numbers), quoted as written.
* The Portuguese edition translates every prose artifact (the brief, the round, the answer, the excerpts, both requests, the first queue) with a note; `git status` and the diff stay as they ran, and the sentence after the diff gives its content in Portuguese.

After the first staging, the author's review of the chapter asked for four changes, made in both editions:

* The project section links CLAHub's upstream repository at its first mention.
* `/analyze` is not only for code: the opening and section 2 say it works on a repository with code, documents or both, and that it skips what the project does not have. This is the command's own scope ("Document an existing repository"); the run shows the code case only.
* A new section 3, "Before you run it", between "What changes" and "The project": put everything about the project (proposals, contracts, emails, meeting transcripts, tickets, slides) in `context/`, apart from `docs/`, and say it with the command, `/analyze Read context/ first, whole.`, as the reader's instruction, since the kit does not look for that folder. Whether `context/` is committed is the reader's decision; the chapter gives both sides and no recommendation, as the author chose. The CLAHub run had no such folder, and the chapter says so. A key point carries it; the defaults and contradictions key points were merged to stay at five.
* A subsection of section 2, "FOCUS on code without an architecture": the strangler fig, a gradual replacement in vertical slices, given as the reader's answer to the FOCUS question, which `/analyze` records in docs/01 and an ADR. The kit's §Choices does not name it; the run's own round offered the same shape for the two principles. New source `[^strangler-fig]`, Martin Fowler, "Strangler Fig", 2024 (the page's date, 22 August 2024, checked on 2026-09-28). Terms: "vertical slice" / "fatia vertical" from docs/03.

The chapter now has seven H2 sections in each edition instead of the Contract's six, and one H3 inside section 2; parity holds.

The chapter tag is `book-v1-analyze`, not the Contract's `book-v1/analyze`: the author's `git tag -a book-v1/analyze` failed with "cannot lock ref 'refs/tags/book-v1/analyze': 'refs/tags/book-v1' exists", since git stores a tag as a file and `book-v1` cannot also be a folder. Nothing was pushed. `book-v1` is published and cited, so it stays; the author chose the hyphen, and the chapters, the run's README, ADR-0009, docs/05, docs/01 and docs/03 say `book-v1-<chapter-slug>` for the fork. The Contract above keeps its original wording. The fork's commit `be484e9` was already made and is the one the tag goes on.

Dropped: nothing of the Contract.

The proof: build, parity, em dash and prose green; links red only on the `book-v1-analyze` URLs and the run's README on `main`, in both editions, which answer after the author's push; disclosure green (`scripts/check_disclosure.py`), and the 20 staged fork files match no entry of the list. Every English excerpt was inserted by script from its source and then compared with it (the fork's files, `brief.md`, `questions.md`, `git-status.txt`, `turn-4.diff`, the `-` side of `turn-3.diff`): all byte for byte. `make book` built both PDFs and EPUBs; its only warnings are the `user-select` ones earlier chapters also print.

Decisions: no ADR. ADR-0009 amended (branch `book`, chapter tags on the fork, `book-v1` frozen); docs/05 §5 gains the Brownfield project slot; docs/01's brownfield line names the chapter tag URL; docs/03 widened "chapter tag" in `/propose`; no new term.

The author's commands, after reviewing the staged fork files:

```
cd ../clahub
git commit -m "Analyze: documents and first milestone"
git tag -a book-v1-analyze -m "One Page at a Time, chapter analyze"
git push origin book book-v1-analyze
```
