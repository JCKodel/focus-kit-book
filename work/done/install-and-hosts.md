# install-and-hosts

**Objective.** After chapter 5 the reader can install focus-kit in a repository with one sentence to the agent, update it by saying the same sentence again, and invoke the four commands in Claude Code, Codex or GitHub Copilot. The reader also knows why the method does not depend on the host.

**Behaviour.**

* The reader can install the kit: open the agent in the repository and say the README's sentence, or download the setup file and point the agent at it. Nothing is installed on the machine.
* The reader can say what the install writes (the four commands, once per host folder, and the pointer files) and what it never touches: `docs/`, `work/`, `AGENTS.md`, `CLAUDE.md`, which belong to the project.
* The reader can update the kit by saying the sentence again, and knows that an update changes only the kit's files.
* The reader can invoke a command with a slug in Claude Code (`/propose <slug>`), Codex (`$propose <slug>`) and Copilot (`/propose`, which asks for the slug), and knows where each host reads its rules and its commands.
* The reader can explain why the hosts are alike enough: each reads a rules file at session start (`AGENTS.md`, directly or through a pointer), each loads a command from a file in the repository, and each hands the command the word typed after it. The method lives in plain files, so switching hosts changes nothing.
* The reader finds any other host in the setup file's table, which the kit keeps current, not the book.

**Contract.**

Chapter 5, `book/en/05-install-and-hosts.md` and `book/pt/05-install-and-hosts.md`:

* Title: "Install, and the hosts" / "Instalar, e os hosts".
* Voice: instruction to the reader as "you"; the run is the author's, told in one clause at most.
* Sections, in order (headings may be reworded; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. Install. The sentence, as the README gives it, with `main`: `Read https://raw.githubusercontent.com/JCKodel/focus-kit/main/SETUP.md and do what it says.` It stays in English in both editions, as focus-kit's `README.pt.md` does. The alternative in one sentence: download `SETUP.md` and point the agent at the file. Then the real run on the guided project (below): context first (the clinic repository at `book-v1/start`, three files), then the agent's report, then the list of what appeared (`git status --short` of the run, grouped as it prints), then one sentence saying what to see: 36 files, the four commands once per skills folder, and small pointer files for the hosts that need them.
  3. What the install never touches, and how to update. Running the file again replaces the kit's files and nothing else; `docs/`, `work/`, `AGENTS.md` and `CLAUDE.md` are the project's. `AGENTS.md` does not exist yet in the clinic: chapter 7 writes it. The same sentence is the update.
  4. How a host finds the commands. Chapter 2's rules file, then per host, each from its vendor documentation:
     * **Claude Code**: `CLAUDE.md` importing `AGENTS.md`; `.claude/skills/<name>/SKILL.md`; `/<name> <slug>`, the slug arriving as `$ARGUMENTS`.
     * **Codex**: `AGENTS.md`; `.agents/skills/<name>/SKILL.md`; `$<name> <slug>`; the `agents/openai.yaml` beside each skill turns off implicit invocation, so a message that says "apply" builds nothing unasked.
     * **GitHub Copilot**: `AGENTS.md`; `.github/prompts/<name>.prompt.md` pointing to the skill; `/<name>`, which asks for the slug.
     * One sentence: Cursor, Gemini CLI, Google Antigravity, Windsurf and others are in the table of `SETUP.md` §1, with the link, and that table, not the book, is kept current. The table is not reproduced (docs/00 non-goal: not a host reference).
  5. Why the method does not depend on the host: the three shared facts of Behaviour, in about three sentences, tied to chapter 2's rules file and fresh session. Every run writes every host's files, so the repository opens ready in any of them.
  6. Key points, at most five.
  7. Exercises (below).
* The run. /apply runs Claude Code non-interactively (`claude -p` with the sentence, permissions enough to fetch and write) inside `../focus-kit-clinic` at `book-v1/start`, and records in `work/done/install-and-hosts-run/`: the exact command, `claude --version`, the agent's full output, and `git status --short` after the run. Paths in those files are relative to the clinic; an absolute path is replaced and the replacement recorded on this page.
* The check of the run. /apply compares every written file with its section of `SETUP.md` at the SHA below, byte for byte (with `<name>` filled), and checks the §4 count of 36. If the install sentence produced a file that differs, the run is redone with the downloaded file. The chapter then shows the download route first and says in one sentence why. The difference is recorded here as a finding for the kit's own repository, which is not changed here.
* The agent's report is evidence of how a tool worded something (docs/04): byte for byte in both editions, followed in Portuguese by its full translation. The chapter shows the report whole if it is short, else the unit that lists the files and the next command. If the raw output holds an em dash, the check's exemption widens from `work/done/spec-driven-run/` to `work/done/*-run/`. This is the second occurrence, and chapter 3's run was the first. The change goes in `scripts/check_em_dash.py`, docs/01 and docs/04.
* Numbers, and only these: 36 files; four commands; the Claude Code version, in its source note only.
* docs/03 terms used: focus-kit, setup file (new, added by this /propose), host, command, rules file, project documents, page, delivery, fresh session, guided project, chapter tag. The Portuguese edition uses the fixed terms.
* Sources (`[^key]`, same keys in both editions):
  * `[^focus-kit-setup]`: focus-kit's `SETUP.md` at `26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b`, the commit the run installed (`main` on 2026-09-25). If `main` moved before /apply, /apply uses the new head and records it.
  * `[^claude-code-skills]`, `[^claude-code-memory]`, `[^codex-skills]`, `[^codex-agents-md]`, `[^copilot-skills]`, `[^copilot-prompt-files]`: the vendor pages `SETUP.md` §1 lists for those hosts, `accessed` on the day of /apply. /apply checks that each page still says what the chapter uses. Where one no longer does, the chapter follows the page and this page records the difference from `SETUP.md`.
  * `[^claude-code-run]`: the run itself, the chapter tag and the Claude Code version.
* Code quoted from the guided project at `https://github.com/JCKodel/focus-kit-clinic/blob/book-v1/install-and-hosts/<path>` (a pointer file, say), never copied from here.
* Cases: none. No OD-3 approval.
* Exercises, on the guided project (answers belong to the `exercise-answers` appendix, not here):
  * 5.1: clone the clinic, check out `book-v1/start` on a branch of your own, install the kit with your host, and compare your file list with `git diff --stat book-v1/start book-v1/install-and-hosts`.
  * 5.2: say the sentence again and read `git status`: what an update changed, and what it left alone.
  * 5.3: find your host's row in `SETUP.md` §1, open its vendor page, and invoke `/propose` (or its equivalent) with a made-up slug. It has no documents yet to read, and what it says shows why chapters 6 and 7 come next.

This is the first chapter that changes the guided project and the first with exercises.

Guided project, `../focus-kit-clinic`: the 36 files of the run, staged by /apply (the install itself does not stage, as `SETUP.md` §1 says). The author's commands, written here and in the commit body, never run by the agent:

```
cd ../focus-kit-clinic
git commit -m "Install focus-kit"
git tag -a book-v1/install-and-hosts -m "One Page at a Time, chapter install-and-hosts"
git push origin main book-v1/install-and-hosts
```

Then the chapter's `make verify` can go green (docs/05 §5 order).

Files:

```
book/en/05-install-and-hosts.md      chapter 5, no status: draft when done
book/pt/05-install-and-hosts.md      chapter 5, no status: draft when done
work/done/install-and-hosts-run/     command, version, output, git status of the run
../focus-kit-clinic/                 36 files staged, not committed
docs/03-Domain.md                    setup file row (written by this /propose)
docs/06-Queue.md                     install-and-hosts [x]
scripts/check_em_dash.py, docs/01, docs/04   only if the run's output holds an em dash
```

**Out of scope.**

* What each command does: chapters 6 to 11. The chapter names them only.
* Reproducing `SETUP.md` §1's table, or any host beyond the three: the table is the kit's, and it changes.
* FOCUS and git as offered, not imposed: one clause at most, pointing to Parts III and IV.
* Running Codex or Copilot: taken from their documentation, as the queue line says.
* Changing focus-kit (a tag, a README fix): another repository, the author decides there.
* `/brainstorm` on the clinic: chapter 7.

**Done when.**

* [x] Run recorded in `work/done/install-and-hosts-run/`, every file matching `SETUP.md` byte for byte, 36 files.
* [x] 36 files staged in `../focus-kit-clinic`; nothing committed there by the agent.
* [x] Both editions written, same headings in the same order, no `status: draft`.
* [x] Opens with its value in at most three sentences; at most five key points; exercises 5.1 to 5.3.
* [x] No filler and nothing useful cut: every sentence read against docs/00 product question 2.
* [x] Every number on the Contract's list, sourced; every vendor page checked on the day.
* [x] The report byte for byte in both editions, translated in Portuguese; no absolute path, no disclosure term.
* [ ] The author commits and pushes the clinic and its tag; then `make verify` green (build, parity, em dash, prose, links including the tag URLs, disclosure).
* [x] `make book` builds; both PDF paths given to the author.
* [x] docs/06 marked `[x]`; page moved to `work/done/install-and-hosts.md` with what happened.

The unticked item is the author's: it ticks when the clinic's commit and tag and this repository's commit are pushed and `make verify` is green.

**What happened.**

* The run. `main` of focus-kit had not moved: the run installed `26e5e1e4c8fcc6e059075a51db8cad5ed2028f2b`. Claude Code `2.1.282`. The install sentence took three attempts, all kept in `work/done/install-and-hosts-run/`:
  1. `acceptEdits` with WebFetch: the fetch tool gave the agent a summary, not the text, and the agent refused to write files it could not copy byte for byte. Its request to `curl` the file was denied.
  2. `acceptEdits` with WebFetch and `curl`: the download worked, and Claude Code refused writes into `.claude/` in that mode.
  3. `bypassPermissions`, inside the clinic only: the run. The chapter turns attempts 1 and 2 into one paragraph telling the reader to approve the download and the write into the host's folder.
  The command also carries `--setting-sources project --strict-mcp-config --no-session-persistence`, so the author's plugins, hooks and MCP servers stay out of the session; a probe first confirmed the session loaded no instruction file, no hook context and no MCP server. Each attempt exited with status 1 after its report.
* The check of the run. All 36 files match their block of `SETUP.md` §3 byte for byte (block lines plus a final newline, `<name>` filled for 3.6 to 3.9), none missing, none extra. The download route was not needed, so the chapter shows the sentence first.
* The report is short and shown whole, byte for byte, in both editions, then translated in Portuguese. It holds no em dash and no absolute path, so nothing was replaced and `scripts/check_em_dash.py`, docs/01 and docs/04 are unchanged. The only change to the raw output: the terminal control sequences Claude Code printed on exit are removed (recorded in the run's README).
* The chapter shows `git status --short` as it printed: untracked folders collapse to seven lines. The chapter says the lines hold 36 files and names `--untracked-files=all`; the one-per-line list is `git-status-staged.txt`. "Seven" is not in the text, to keep the Contract's list of numbers.
* Vendor pages, checked 2026-09-25:
  * Claude Code's memory page now says Claude Code reads `AGENTS.md` on its own, and a `CLAUDE.md` with `@AGENTS.md` is the fallback where it cannot. `SETUP.md` §1 still says "`CLAUDE.md`, which imports `AGENTS.md`". The chapter follows the vendor page. Finding for focus-kit's repository, not changed here: update the Claude Code row of the table.
  * Copilot reading `AGENTS.md` is not on either Copilot page `SETUP.md` §1 lists. It is on GitHub's "Adding repository custom instructions for GitHub Copilot", which the chapter cites as a new key, `[^copilot-instructions]`, beyond the Contract's list.
  * The rest held: `.claude/skills/<name>/SKILL.md`, `/skill-name` and `$ARGUMENTS`; Codex reading `AGENTS.md` before any work, `.agents/skills`, `$` to invoke a skill, `allow_implicit_invocation: false` in `agents/openai.yaml`; Copilot project skills in `.agents/skills`, prompt files in `.github/prompts/`, `/name` that prompts for `${input:...}`. The prompt-file page also says prompt files work only in VS Code, Visual Studio and JetBrains IDEs, which the chapter says in one sentence.
* Added to the chapter beyond the Contract's sections: two sentences introducing the guided project and the chapter tag, since this is the first chapter that uses them (docs/04, context before an excerpt); in Portuguese, one sentence saying what the English install sentence says, and one saying what the prompt file's last line says.
* The run's source note points to `work/done/install-and-hosts-run/README.md` on `main`. It answers only after the author pushes this delivery, like the clinic tag URL.
* Proof. `make verify`: build, parity, em dash and prose green; links red only on the clinic tag URL and the run's README on `main`, in both editions, which answer after the author's push; disclosure green when run alone (`scripts/check_disclosure.py`), and the 36 staged clinic files match no entry of the list. `make book` built both PDFs and EPUBs; its only warnings are the `user-select` ones earlier chapters also print.
* The clinic: 36 files staged, 2049 lines, nothing committed, tagged or pushed by the agent.
* Nothing dropped. No ADR.
