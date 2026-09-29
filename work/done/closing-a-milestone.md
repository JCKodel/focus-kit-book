# closing-a-milestone

**Objective.** After chapter 12 the reader can close a milestone: check its paragraph on the running product, review everything the milestone built with what the host offers, decide each finding, and turn the confirmed ones into queue lines instead of fixes.

`clinic-milestone-1` was split off from this delivery first: it built and recorded the clinic's milestone 1 that this chapter reviews.

**Behaviour.**

* The reader can say why a milestone needs a review of the whole: each page was read and each staged change reviewed on its own, and nobody looked at what they add up to (the kit's §8, paraphrased).
* The reader checks each sentence of a milestone's paragraph on the running app, end to end, once, and treats a sentence that does not hold as a finding.
* The reader can run `/code-review` on everything a milestone built, knows what their host offers instead when it is not Claude Code, and knows the review fixes nothing.
* The reader decides each finding by conversation with the agent: confirm or reject, with the reason, never trusting a finding blindly nor dismissing it unread.
* The reader asks the agent to turn each confirmed finding into a queue line in the milestone where it belongs, and can say why it is a line and not a fix in the middle of the next milestone.
* The reader can tell, from the Ninjobs story, what happens when a milestone's findings become one delivery instead of lines.

**Contract.**

Chapter 12, `book/en/12-closing-a-milestone.md` and `book/pt/12-closing-a-milestone.md`:

* Title: "Closing a milestone" / "Fechando um marco".
* Voice: instruction to the reader as "you"; the check, the run and the decisions are the author's, in the first person where they are told (docs/04 §Voice).
* Sections, in order (headings may be reworded; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. Why review the whole. The kit's §8 paraphrased: when a milestone closes, review the whole with what the host offers, and each confirmed finding becomes a queue line. Each delivery was right on its own page; the risk of a light process is what they add up to. Short.
  3. Check the paragraph. The clinic's milestone 1 paragraph quoted whole; the author, with `npm run dev`, checks each sentence end to end; the result, one line per sentence, held or not. A sentence that fails is a finding like any other (section 5). Points back to chapter 9: the paragraph is a test a person can check.
  4. Review everything the milestone built. `/code-review high` on the range of milestone 1 (below), run by the agent; why `high`: the breadth suits one look at the whole, and the person's decision filters what is uncertain. One sentence each on what Codex and GitHub Copilot offer to review a whole branch, from their cited documentation, as chapter 5 does. The run on the clinic: the command, and the findings as the run reported them (excerpt), or, if there are none, that the review found nothing and what that does and does not prove.
  5. Decide each finding. For each: the author's decision (confirmed or rejected) and its reason in a sentence, sent to the run's session word for word. The person is the brain: a finding looks right and is not always (chapter 6).
  6. Findings become lines. The request that turns the confirmed findings into lines, the diff of the clinic's docs/06 whole, and why a line and not a fix: a fix in the middle of the next milestone has no page and no review. Then the author's commit and the tag `book-v1/closing-a-milestone`, and one sentence: this tag holds the whole milestone, so the reader can compare their code with it.
  7. When the findings became one delivery (Ninjobs). One story (below).
  8. Key points, at most five, one of them: a finding becomes a line, not a fix.
  9. Exercises (below).
* The range. Milestone 1 of the clinic is `3f0b47c..f16f83b`: `skeleton` through `cancel-appointment`, seven commits, `3f0b47c` the last commit before the milestone. Before the run, /apply checks which target form of `/code-review` in Claude Code 2.1.284 reviews exactly that range, from the command's own description and Claude Code's documentation, never by running a review, and fixes it in the README; if none does, it stops and asks the author.
* Before the first run. The clinic is on `main`, clean, at `f16f83b`, equal to `origin/main`; focus-kit `e7607c5` as installed.
* The run, the mechanism of `clinic-milestone-1` (the first occurrence of these rules for a run of several steps), inside `../focus-kit-clinic`:
  1. The paragraph check, by the author, before the review: `npm run dev`, each sentence of the paragraph checked, the result recorded. Not a run of the agent.
  2. The review, headless: `claude -p "/code-review high <target>"` with `--model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode default --permission-prompts none --output-format stream-json --verbose` and `--allowedTools "Bash(git diff *)" "Bash(git log *)" "Bash(git show *)" "Bash(git status *)" "Bash(npm *)" "Bash(npx *)"`; the review edits nothing, so an edit would be denied. /apply stops and shows the author the findings. A failing paragraph sentence joins them.
  3. The decisions. /apply may give its assessment of each finding; the author decides. The decisions go to the review's session with `--continue`, word for word as the author approves them, in one request, and the same request asks the agent to write each confirmed finding as a `[ ]` line in the clinic's docs/06, in the milestone where it belongs, or in a new milestone with its paragraph if none fits, and to stage; that turn runs with `--permission-mode acceptEdits` and `--allowedTools "Bash(git add *)" "Bash(git status *)" "Bash(git diff *)"`. Corrections to the lines follow with `--continue`, as recorded turns. Nothing in the clinic is edited by hand, and no finding is fixed. A finding may be confirmed and already a line (milestone 2 holds `owner-password`, `sign-in-limit` and `fake-bookings`): no new line; the existing line's description gains words only if the finding adds something; `decisions.md` and the chapter mark it "already queued". If the continued session cannot or will not write the lines, a fresh interactive session in the clinic gets the same request, recorded as a turn, and the chapter says so in one sentence.
  4. The author commits with the kit's message (the clinic's docs/05 §6): imperative subject, one bullet per new or changed line; there is no page in the clinic, so no last line pointing to one. Then the author creates the annotated tag `book-v1/closing-a-milestone` on it, message "One Page at a Time, chapter closing-a-milestone", and pushes both; `make verify` of this book goes green only after that push (docs/05 §5).
  * A denied call is recorded, never retried by another route. Notes the host writes outside the repository are deleted after the run. Session ids are left out of the record. Absolute paths are removed.
  * If no finding is confirmed, the clinic does not change, there is no tag, and the chapter links the milestone's code at `f16f83b` on `main`; the chapter says so.
* Recorded in `work/done/closing-a-milestone-run/`: `README.md` (date, `claude --version`, model, the range and the target form, commands, allowlists, the paragraph check one line per sentence, denied calls, what diverged, the commit's sha and subject), `turn-N.txt` (every turn, text blocks byte for byte, tool calls as `[tool <name>] <relative path or command>`), `findings.md` (the findings as the run reported them, in text or in a tool's input, one block each, byte for byte), `decisions.md` (each request sent, word for word), `queue.diff` (the clinic's docs/06 before and after), `commit-message.txt`.
* Excerpts in the chapter, byte for byte in English, translated in Portuguese with the note of chapter 10: the paragraph (from the clinic's docs/06), the findings (whole if short; otherwise each finding's summary line, the rest reached through the record), the decisions request, `queue.diff`. No code excerpt: the code is reached through the tag.
* Ninjobs, one story, cited as chapter 4 cites it (a private repository, counted by the author): on 2026-08-29 its process wrote the rule that each confirmed finding of a milestone review becomes a queue line; when the milestone closed, the author chose to put all eight findings in one delivery, whose page says in its own words that it does not fit a page and goes against the process on purpose; the page ran to about 880 lines, and in its own check the author found faults its tests had not. The cause is the author's choice. Numbers from Ninjobs: eight findings, the page's line count (`wc -l`), the date; nothing else. None of the findings' content, no level of the review, no file, commit, table or name of infrastructure. The author approves the passage before the chapter is done.
* Numbers, and only these: the Ninjobs ones above; the count of commits and findings in the clinic's run; what the run's output prints and the chapter quotes. The Claude Code version and model in the run's source note only.
* docs/03 terms introduced: milestone review, finding (added by this /propose). Used: milestone, queue, mark, delivery, page, command, host, guided project, chapter tag, fresh session.
* Sources (`[^key]`, same keys in both editions):
  * `[^focus-kit-closing]` (new): `SETUP.md`, the docs/05 template, §8 Closing a milestone, at focus-kit `e7607c58ad38e70e3496518a58d4237612e21ebc`, installed in the clinic.
  * `[^claude-code-review]` (new): Claude Code's documentation of `/code-review`, the page /apply finds and the link check opens.
  * `[^codex-review]`, `[^copilot-review]` (new): their vendors' documentation of reviewing a branch or a pull request.
  * `[^closing-a-milestone-run]` (new): `work/done/closing-a-milestone-run/README.md` on `main`.
  * `[^ninjobs-milestone-review]` (new): Ninjobs, a private repository: the rule in its docs/05 dated 2026-08-29, the page of the delivery that took the eight findings, counted with `wc -l`.
  * `[^clinic-milestone-1-run]` (new): `work/done/clinic-milestone-1-run/README.md`, for the seven deliveries reviewed.
* Exercises, on the clinic, by conversation with the agent, never by hand:
  * 12.1 With your milestone 1 built, check each sentence of its paragraph on your running app, and write down any that does not hold.
  * 12.2 Run `/code-review high` (or your host's review) on the range of your milestone 1, and decide each finding with its reason.
  * 12.3 Ask the agent to turn your confirmed findings into lines, and say for each why it belongs in the milestone the agent chose.
* Documents: docs/03 has the two terms (this /propose). docs/06 line `closing-a-milestone` to `[x]`. docs/00 §Contents already names chapter 12. docs/05 §8 unchanged unless the run shows it needs a word. The page's What happened records the exercise answers for the `exercise-answers` appendix.

**Out of scope.**

* Fixing any finding: the lines wait in the clinic's queue, no chapter builds them now.
* `/code-review ultra` and its billing: the author does not run it here; one sentence at most, if the section on hosts needs it.
* The governor question applied to the findings: chapter 13, `the-governor`.
* Closing a milestone of chapters (this book's M3, docs/05 §8, second paragraph): chapter 23.
* The content of Ninjobs' findings, and the level of its review: infrastructure and a detail the story does not need.
* Updating focus-kit in the clinic: the run uses `e7607c5`.
* Cost or duration numbers: chapter 24.

**Done when.**

* [x] The target form of `/code-review` for the range checked and written in the README before the run.
* [x] The author checked the paragraph on the running app; the README has one line per sentence.
* [x] Run recorded in `work/done/closing-a-milestone-run/` as the Contract says; every denied call in the README; no note of the host left outside the clinic.
* [x] Every finding decided by the author; every request a recorded turn; nothing in the clinic edited by hand, no finding fixed.
* [ ] The author committed and pushed the clinic's docs/06 and the tag `book-v1/closing-a-milestone` (or, with no confirmed finding, the chapter says there is no tag).
* [x] Both editions written, same file name and heading structure, opening with the Objective in at most three sentences.
* [x] No filler and nothing useful cut; every number cites its source; no draft marker.
* [x] Every English excerpt matches its source byte for byte, checked by script; Portuguese translated with the note.
* [x] The author approved the Ninjobs passage.
* [ ] `make verify` green, the disclosure scan included.
* [x] `make book` builds; both PDF paths given to the author.
* [x] docs/06 line `[x]`, page in `work/done/`, staged, commit message suggested.

## What happened

* The target form: Claude Code's documentation names "a ref range such as `main...my-feature`" as a target of `/code-review`, and the command's description in 2.1.284 names "a PR number/branch/path target". The form used is `3f0b47c...f16f83b`: three dots, as the documentation writes it; since `3f0b47c` is an ancestor of `f16f83b`, it is exactly the seven commits. Checked from the documentation before the run, without running a review.
* The paragraph check: every claim held, checked by the author end to end, once, on a clean database, before the review. The clinic's paragraph is one sentence, so the check has one line per claim, four.
* The first start of the review was lost when the book's session that had started it ended; its stream held only the start event, and the clinic was unchanged. The review was started again detached from the book's session (`nohup`), so it could outlive another interruption; the README records both. The later turns were started the same way.
* The review: ten findings, with no denied call. The book's agent checked each against the code and gave its assessment; the author accepted it whole: five confirmed (5, 6, 7, 9, and the duplicated parser of 10), five rejected with their reasons (1, 2, 3, 4, 8, and the query of 10). None was already a line of the clinic's queue. The chapter quotes each finding's summary, since the whole findings are long; the rest is in `findings.md`.
* The lines: the agent put the five in a new milestone 2, "what the review of milestone 1 found", with its paragraph, and renumbered "the owner runs the day" as milestone 3. The page allowed it; the chapter says it. Chapters 7 and 10 speak of the clinic's "milestone 2" as it was at their tags, which stays true there. One call denied in turn 2 (a shell loop over the git history), done as plain commands.
* One correction, turn 3: the suggested commit message had two bullets about the milestone; the corrected one has one bullet per new line, five, with no last line.
* No note of the host: the clinic's auto-memory folder stayed empty.
* The Portuguese edition translates the paragraph, the ten summaries and the decisions request with the note of chapter 10, and gives the new milestone's paragraph in a sentence after the diff, which stays as it ran, as chapter 7 does. It uses chapter 7's "cadastrar" for "register". The prose rule `inflated` refused "de ponta a ponta" (its entry `de ponta`); it became "do começo ao fim".
* The diff of the clinic's queue holds a fenced block, so both editions fence it with four backticks.
* Codex and Copilot are cited from their current pages: OpenAI's "Developer commands" (`/review` and `codex review --base <branch>`; the old `developers.openai.com` addresses redirect to it) and GitHub's "About GitHub Copilot code review".
* Pending, the author's: the clinic's commit, the tag `book-v1/closing-a-milestone` and their push, then this book's commit and push. `make verify` is green up to the link check, which fails only on the link to the tag and on the link to `work/done/closing-a-milestone-run/README.md` on `main`, in both editions; they answer once the clinic's tag and this commit are pushed. The README's commit line reads `COMMIT_SHA` until the author commits in the clinic.
* Proof: `make verify` green up to the link check, as above; the disclosure scan green alone. The English excerpts were compared by script with their sources: the paragraph (the clinic's docs/06), the ten summary lines (`findings.md`), the decisions request (`decisions.md`) and `queue.diff`: all identical. `make book` printed the known warning `Ignored user-select: none`, as in earlier chapters.
* Documents: docs/03 has the two terms, milestone review and finding (written by /propose). docs/05 §8 unchanged: the run followed it as written. docs/06 line `[x]`. No ADR.

Exercise answers, for the `exercise-answers` appendix:

* 12.1: the four claims of the clinic's paragraph held; the reader's own app should hold them too, and any that does not is a finding.
* 12.2: the reader's findings depend on their code; the clinic's are the ten of `findings.md`, decided as in `decisions.md`.
* 12.3: the clinic's lines went to a new milestone, since milestone 1 is closed and "the owner runs the day" is about other work; see `queue.diff`.
