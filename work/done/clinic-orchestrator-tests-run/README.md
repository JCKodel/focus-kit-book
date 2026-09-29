# clinic orchestrator tests run

The guided project's client orchestrators, moved into plain functions that receive their repositories and tested with fake repositories, built with `/propose` and `/apply`, the page and the staged change reviewed by the author and committed by them. Chapter 16 shows it. The delivery that planned and recorded it is `../clinic-orchestrator-tests.md`; the format is the one of `../clinic-milestone-1-run/`, now in docs/05 §5.

* Host: Claude Code, `claude --version` printed `2.1.284 (Claude Code)`; macOS 26 (Darwin 25.6.0), arm64.
* Model: `claude-opus-5-5`, given with `--model` on every turn.
* Kit: focus-kit `e7607c5`, as installed; not updated.
* The clinic's first commit: `c54d011`, "Queue the confirmed findings of the milestone 1 review (docs/06)", tagged `book-v1/closing-a-milestone`; the clinic was on `main`, clean, before the first run.
* The clinic's last commit: `e6653b5906e66ed1f54050891adb0d5efb14c735`, "Move each client hook's events into tested plain functions", pushed, no tag.
* Date: 2026-09-29.

## The commands

Run from the root of the clinic. Common flags, on every turn:

```
--model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose
```

`/propose`, a fresh session: `claude -p "/propose orchestrator-tests"` with the common flags. The brief went next, with `claude -p --continue "<brief>"` and the common flags; the later round of questions was answered with `claude -p --continue "Your call. Say what you chose and why."`. Page review requests went to the same session the same way.

`/apply`, a fresh session: `claude -p "/apply orchestrator-tests"` with the common flags and:

```
--disallowedTools "Bash(npm run dev*)" --allowedTools "Bash(npm *)" "Bash(npx *)" "Bash(node *)" "Bash(mkdir *)" "Bash(cp *)" "Bash(git add *)" "Bash(git status *)" "Bash(git diff *)"
```

Staged review requests went to the `/apply` session with `--continue`, the same flags.

* The turns were started by the book's `/apply` session through its shell, one at a time.
* Every request below was written in English by the book's agent from what the author chose, shown to the author word for word and sent only after the author approved it; the manual check in turn 6 was written after the author reported it had worked.
* Nothing in the clinic was edited by hand. The author ran `npm run dev` for the manual check, which writes only `data/clinic.sqlite`, ignored by git.
* Each turn ended with a result of `success`.
* A note of the host outside the repository appeared in turn 6: the agent wrote a feedback note about the commit message trailer into Claude Code's auto-memory folder for the clinic. It was deleted after the commit, so the next run starts as a reader's would. Its paths read `<host folder of the clinic>` in the turn file.

## orchestrator-tests

`/propose` did not split the line; it put `orchestrator-tests` as the first of milestone 2, as the brief asked.

* `/propose`: turn 1 (`/propose orchestrator-tests`), turn 2 (the brief), turn 3 (the rule). The brief, word for word:

  ```
  Every client orchestrator, each use<Feature>.ts hook, gets unit tests. Move what each event does out of the hook: the calls to repositories and use cases, in their order, and the new state go into plain functions that receive their repositories as a parameter, the real ones by default, and `now` where a use case needs the clock, and return the new state. The hook only holds the state, publishes the in-flight state and publishes what the function returns. The tests pass fake repositories, in Vitest in Node, with no module mock and no new dependency. Server routes do not change. The app behaves exactly as before. Add the line as the first of milestone 2.
  ```

* Page review, turn 4:

  ```
  Four corrections to the page:
  1. Done when has no manual check, unlike the earlier pages with a screen. Add one: the person runs npm run dev, books a time and cancels it from Your appointments, books another and cancels it with the booking code, then signs in at /owner, adds a professional and sets their weekly hours.
  2. Done when says docs/01 lists <name>Events.ts and what stays in the hook, but not the rule this delivery introduces. Add that docs/01 says a client orchestrator's event functions receive their repositories as a parameter, the real ones by default.
  3. The page says no *.e2e.ts is edited, but not what happens to the existing Vitest tests. Add to Done when that every existing Vitest and Playwright test passes without changing what it asserts.
  4. Your edit left the first sentence of milestone 2 in docs/06 on one long line. Wrap the paragraph like the others.
  ```

* `/apply`: turn 5.
* Staged review, turn 6:

  ```
  Two requests:
  1. Finish the delivery yourself: copy work/orchestrator-tests.md to work/done/orchestrator-tests.md with cp, remove the old one with rm, and stage everything with git add -A. The earlier call was denied because of git mv, not because moving the page is forbidden.
  2. The suggested commit message has a Co-Authored-By trailer again. Give it in the docs/05 format, with no trailer and the page on the last line.
  I ran npm run dev, signed in at /owner, added a professional, gave them weekly hours, reloaded and saw the hours kept. Then I opened /, booked a time more than 24 hours away and cancelled it from Your appointments, and booked another and cancelled it with Cancel with a booking code. It all worked. Record it in the page and tick the manual check.
  ```

* Denied calls, two, both in turn 5: a `sed` printing Done when of an earlier page (read another way); a compound call with `git mv` of the page, a dash count, lint and `git add -A`, which left the page in `work/` and asked the author to move it. Turn 6 ran `cp`, `rm` and `git add -A` with no denial. None in `/propose`.
* Diverged: `/propose` asked two rounds of questions before the page, one before the brief and one after it. The `/apply` agent re-exported from the hooks the types the views import, so no view changed; the clinic's page records the rest. The suggested commit message carried a `Co-Authored-By` trailer, corrected by request before the author committed.
* Commit: `e6653b5906e66ed1f54050891adb0d5efb14c735`, "Move each client hook's events into tested plain functions".

## Files

```
README.md                    this file
orchestrator-tests/turn-N.txt every turn, in order: text blocks byte for byte, tool calls as [tool <name>] <path or command>
verify.txt                   the npm run verify output on the clinic's last commit, e6653b5
```

The turn files are derived from each turn's stream. Absolute paths are removed, so paths are relative to the clinic's root; the host's folder for the clinic reads `<host folder of the clinic>`. Session ids are left out. In `verify.txt` the terminal colours are removed and the clinic's folder that Vitest prints became `.`.
