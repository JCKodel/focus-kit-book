# clinic milestone 1 run

The guided project's milestone 1, built line by line with `/propose` and `/apply`, each page and each staged change reviewed by the author and committed by them. Chapter 12 reviews this milestone. The delivery that planned and recorded it is `../clinic-milestone-1.md`.

* Host: Claude Code, `claude --version` printed `2.1.284 (Claude Code)`; macOS 26 (Darwin 25.6.0), arm64.
* Model: `claude-opus-5-5`, given with `--model` on every turn.
* Kit: focus-kit `e7607c5`, as installed; not updated.
* The clinic's first commit: `d5b5c03e28ba97836f8188bd6a797e79fe4c85d0`, "Build the skeleton: health page, Hono server, migrations, verify", tagged `book-v1/apply`, committed, tagged and pushed by the author before the first run.
* The clinic's last commit: `f16f83bdfadf7bf5919545aa390c92e6c01d5e3c`, "Let a client cancel an appointment up to 24 hours before it starts", pushed.
* Date: 2026-09-28, every delivery.

## The commands

Run from the root of the clinic. Common flags, on every turn:

```
--model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose
```

`/propose`, a fresh session: `claude -p "/propose <slug>"` with the common flags. Every round of questions was answered with `claude -p --continue "Your call. Say what you chose and why."` and the common flags. Page review requests went to the same session the same way.

`/apply`, a fresh session: `claude -p "/apply <slug>"` with the common flags and:

```
--disallowedTools "Bash(npm run dev*)" --allowedTools "Bash(npm *)" "Bash(npx *)" "Bash(node *)" "Bash(mkdir *)" "Bash(cp *)" "Bash(git add *)" "Bash(git status *)" "Bash(git diff *)"
```

Staged review requests went to the `/apply` session with `--continue`, the same flags.

* The turns were started by the book's `/apply` session through its shell, one at a time, never two in the clinic at once, so each `--continue` reached the session it meant.
* Every request below was written in English by the book's agent from what the author chose, shown to the author word for word and sent only after the author approved it, except the three that record the author's manual check (`professionals` turn 4, `book-appointment` turn 5, `cancel-appointment` turn 4): the author reported the check had worked and chose to have it recorded, and the agent wrote the sentence without showing it first.
* "None" means the author reviewed and asked for nothing; no turn was sent.
* Nothing in the clinic was edited by hand. The author ran `npm run setup` and `npm run dev` for the manual checks, which write only `data/clinic.sqlite`, ignored by git.
* Each turn ended with a result of `success`. The `/apply` turn of `book-appointment` ended while the book's session was detached, so its exit status was not seen; its stream holds the `success` result.
* A note of the host outside the repository appeared once, in `e2e-database-busy` turn 4: the agent wrote a feedback note into Claude Code's auto-memory folder for the clinic. It was deleted after that delivery's commit, so the next run started as a reader's would. Its paths read `<host folder of the clinic>` in the turn file. No other delivery left one; the folder was checked after each.

## clinic-setup

* `/propose`: turn 1, turn 2 (the rule).
* Page review, turn 3:

  ```
  Three corrections to the page:
  1. `EmptyClinicName` also refuses a name over 80 characters, so the name misleads. Rename it `InvalidClinicName`, in the page and in docs/03.
  2. Sign-in with an unknown email answers without running scrypt, so the response time tells whether the email is the owner's, which contradicts "it never says which". When the email does not match, check the password against a fixed hash so both refusals take the same time, and say so in the Contract.
  3. "A session older than 30 days is not live" is only proven by the unit test of `isSessionLive`. Add a route test: a session row whose `expires_at` is in the past answers `401 NotSignedIn` and the row is deleted.
  ```

* `/apply`: turn 4.
* Staged review, turn 5:

  ```
  Two corrections to the staged change:
  1. The fetch-to-Result shape now appears in health/api.ts, clinic/api.ts and signIn/api.ts, and the ServerUnreachable type is declared twice. You moved openMigratedDatabase and testDatabase.server.ts on their second use without the page naming them, so the same rule applies here: move the shared part to src/lib/ now, say in the page which was the first use, and update docs/01.
  2. e2eClinic.ts sits at the repository root, outside the layout of docs/01. Move it next to what uses it and say where in docs/01 or docs/04.
  I ran npm run setup in a terminal (the passwords stay hidden, a refused answer is asked again), then npm run dev, and signed in and out at /owner: it all worked. Record it in the page.
  ```

* Denied calls, five: turn 4, a shell loop printing the source files (read one by one instead); `git rm` of `src/app/strings.ts` with Biome and verify (plain `rm` used); a run of the setup command in a pseudo-terminal with `script` (not proven by the agent; the author checked it by hand); a `sed` ticking Done when (edits used). Turn 5, `git mv` of `e2eClinic.ts` (`mv` used).
* Diverged: the agent could not prove the terminal path of `npm run setup`; the author did. `/propose` added `owner-password` and `sign-in-limit` to milestone 2, where they wait.
* Commit: `75a8a259d52ab5603d222eda682d9d9644104149`, "Set up the clinic and let the owner sign in and out".

## professionals

* `/propose`: turn 1, turn 2 (the rule).
* Page review: none.
* `/apply`: turn 3.
* Staged review, turn 4:

  ```
  I ran npm run dev, signed in at /owner, added, renamed and removed a professional, and reloaded: the list was kept. It all worked. Record it in the page.
  ```

* Denied calls, four, all in turn 3: a shell loop printing the source files; a `sed` renaming test helpers with Biome and typecheck (edits used); `npm run verify` writing its output to a file in `/tmp`; `git mv` of the page (`mv` used).
* Diverged: nothing beyond what the clinic's page records.
* Commit: `4cceb3ab2c2fdb6ff155c7341eed897c0d808e01`, "Let the owner add, rename and remove professionals". The suggested message ended with `work/done/professionals.md`, without "See"; the author kept it.

## weekly-hours

* `/propose`: turn 1, turn 2 (the rule).
* Page review: none.
* `/apply`: turn 3.
* Staged review, turn 4:

  ```
  Two requests:
  1. The flaky sign-in you found (the "session older than 30 days" test writing to the e2e database while the server's connection has no busy timeout) becomes a line in docs/06. Put it where you think it belongs and say where.
  2. The suggested commit message does not follow docs/05: "See work/done/weekly-hours.md" is a bullet and the last line is a Co-Authored-By trailer. Give it again in the docs/05 format, with no trailer and the page on the last line.
  I ran npm run dev, signed in at /owner, set a week with a lunch break for a professional, reloaded and opened "Hours": the week was kept. Record it in the page.
  ```

* Denied calls, five, all in turn 3: two shell loops printing the source files; a loop running Playwright three times; `git mv` of the page (`mv` used); a `sed` ticking Done when (edits used).
* Diverged: the agent found a sign-in failing about once in 300 Playwright tests, from an earlier test and the server's connection having no busy timeout. The author had it queued; the agent put `e2e-database-busy` inside milestone 1, before `book-appointment`, so it was built in this delivery with the same five steps. The first manual check found no "Hours" button because the list was empty after the previous check; the author added a professional and the check held.
* Commit: `064d7a9678fcd1e1fce79b3f3a77b7bf90095e8f`, "Let the owner set each professional's weekly hours".

## e2e-database-busy

The line split from `weekly-hours` into milestone 1.

* `/propose`: turn 1, turn 2 (the rule).
* Page review: none.
* `/apply`: turn 3.
* Staged review, turn 4:

  ```
  Two requests:
  1. Finish the delivery yourself: remove work/e2e-database-busy.md, since the page is already in work/done/, and stage everything with git add -A. The earlier call was denied because of the -C flag, not because staging is forbidden.
  2. The suggested commit message has a Co-Authored-By trailer again. Give it in the docs/05 format, with no trailer and the page on the last line.
  ```

* Denied calls, four, all in turn 3: a `python3` script editing two files (edits used); a `cat >>` appending tests (edits used); `git mv` or `mv` of the page; `git -C . add -A`. The last two left the page in both `work/` and `work/done/` and nothing staged. `git add -A` is on the allowlist; the form with `-C` is not. The author's request asked the agent to finish with the allowed commands; turn 4 ran `rm` and `git add -A` with no denial.
* Diverged: the host note described above.
* Commit: `afc833a9274868e5cb55035f4f52250366f64b05`, "Wait for SQLite locks instead of failing with SQLITE_BUSY".

## book-appointment

* `/propose`: turn 1, turn 2 (the rule).
* Page review, turn 3:

  ```
  Done when has no manual check, unlike the earlier pages with a screen. Add one: the person runs npm run dev, books a time on a phone-sized window, sees the code, reloads and sees it under Your appointments.
  ```

* `/apply`: turn 4.
* Staged review, turn 5:

  ```
  I ran npm run dev, gave a professional weekly hours at /owner, opened / in a 390×844 window, booked a time, saw the booking code, reloaded and saw it under Your appointments. It all worked. Record it in the page.
  ```

* Denied calls, five, all in turn 4: two shell loops printing the source files; a `grep` and `sed` over earlier pages; `npm run verify` writing its output to a file in `/tmp`; `git mv` of the page (`mv` used).
* Diverged: `/propose` added `fake-bookings` to milestone 2, before `deploy`, where it waits.
* Commit: `442f88a1aec2920c0fb9bfd993e7d804226702c9`, "Let a client book a free slot and keep the booking code".

## cancel-appointment

* `/propose`: turn 1, turn 2 (the rule).
* Page review: none.
* `/apply`: turn 3.
* Staged review, turn 4:

  ```
  I ran npm run dev and opened / in a 390×844 window. I booked a time more than 24 hours away, cancelled it from Your appointments and saw the time free again, then booked another and cancelled it with Cancel with a booking code. I also booked the earliest time, under 24 hours away: it showed no Cancel button and "Can no longer be cancelled in the app.", and the typed form refused it with the 24 hours message. It all worked. Record it in the page.
  ```

* Denied calls, two, both in turn 3: a shell loop printing the source files; `rm` of the one-off screenshot file with a `grep` (the file was removed another way).
* Diverged: nothing beyond what the clinic's page records.
* Commit: `f16f83bdfadf7bf5919545aa390c92e6c01d5e3c`, "Let a client cancel an appointment up to 24 hours before it starts".

## The milestone check

The paragraph of milestone 1, checked by the author on the running app with `npm run dev`:

* The owner registers professionals: held (`professionals`, turn 4).
* The owner sets their weekly hours: held (`weekly-hours`, turn 4).
* A client books a free slot: held (`book-appointment`, turn 5).
* A client cancels up to 24 hours before: held (`cancel-appointment`, turn 4, from the list and with the code).
* A client is told why not after that: held (`cancel-appointment`, turn 4, the earliest time under 24 hours away).

The author chose to count the checks made at each delivery rather than repeat them end to end.

## Files

```
README.md          this file
<slug>/turn-N.txt  every turn of that delivery, in order: text blocks byte for byte, tool calls as [tool <name>] <path or command>
verify.txt         the npm run verify output on the clinic's last commit, f16f83b
```

The turn files are derived from each turn's stream. Absolute paths are removed, so paths are relative to the clinic's root; the host's folder for the clinic reads `<host folder of the clinic>`. Session ids are left out. In `verify.txt` the terminal colours are removed and the clinic's folder that Vitest prints became `.`.
