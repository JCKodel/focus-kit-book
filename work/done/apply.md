# apply

**Objective.** After chapter 11 the reader can run `/apply` on a reviewed page in a fresh session, follow what it does from the page to a staged change, review that change against the page before committing it, and commit it themselves.

**Behaviour.**

* The reader can say what `/apply` reads (the page, `AGENTS.md`, docs/01, 04 and 05), what it follows literally (the slots of docs/05: verify, environments, proof, publish policy, git), and that the page is the scope: it adds no dependency, layer or tool the page did not name.
* The reader knows what `/apply` does when the page contradicts a document: it stops and says which; the document changes in the same delivery or the page is wrong; it never resolves it silently.
* The reader can say what "done" means in the kit: verify green; the proof taken as docs/05 says, failures included, and each divergence fixed or justified; the page's What happened written; the documents the delivery changed updated; every Done when item ticked; the page in `work/done/`; the mark `[>]` to `[x]`; `git add -A`; the commit message suggested; and the last thing said is which environment is at which version and the command that updates the others.
* The reader can run `/apply skeleton` on the clinic after chapter 10 and compare their staged change with the tag `book-v1/apply`.
* The reader reviews the staged change before committing, with the review questions (below), asks the agent for each correction in the same session, never by hand, and commits it themselves; they know why the agent never commits: the commit is the person's review (Part IV says more).
* The reader knows the commit closes the unit of work of chapter 10: on trunk, the page and its build land in that one commit.

**Contract.**

Chapter 11, `book/en/11-apply.md` and `book/pt/11-apply.md`:

* Title: "`/apply`: build, verify, prove, never commit" / "`/apply`: construir, verificar, provar, nunca fazer commit".
* Voice: instruction to the reader as "you"; the run and the review are the author's, in the first person where they are told (docs/04 §Voice).
* Sections, in order (headings may be reworded; both editions keep the same structure):
  1. Opening, at most three sentences: the Objective.
  2. What it does. From the kit's `apply/SKILL.md` (paraphrased; a sentence quoted only where the wording is the point): what it reads; the page as the scope; the slots followed literally; stop on a contradiction; verify until green; the proof and its divergences; What happened; documents; Done when; `work/done/`; `[x]`; stage and suggest; the environments as the last words. Fresh session in one sentence, pointing to chapter 2 and chapter 10. H3s where a reader would ask a question, as chapter 10 does.
  3. The run on the clinic. Context: the clinic at `3f0b47c` with the reviewed `work/skeleton.md` and docs/06 uncommitted (chapter 10). The command. What the agent did, told in order from the run record, with these excerpts only: the tail of the green `npm run verify` output; the proof screenshot `work/done/skeleton-390x844.png` as an image; the page's What happened section whole; `git status --short` of the staged tree; the suggested commit message whole; the closing line on environments whole. No code excerpt: the code is reached through the tag `book-v1/apply`. If the agent stopped on a contradiction or a failing verify, that is shown too.
  4. Review before you commit. The review questions: is every Done when item ticked and true? Does What happened say what diverged, and would you have decided it otherwise? Did the documents the delivery changed get updated, and only those? Is anything built that the page did not ask for? Do verify and the proof run for you? Then the author's real review of the staged change: each finding, the request sent to the same session by `--continue` (byte for byte), and the diff it made. If the review finds nothing, the section says so and the questions stand alone. Then the author's commit and the tag `book-v1/apply`, and one sentence: the page and its build are in one commit (the unit of work, chapter 10). Why the agent never commits: two or three sentences, pointing to Part IV.
  5. Key points, at most five, one of them: the agent stages, you review and commit.
  6. Exercises (below).
* The run, the mechanism of chapters 7, 8 and 10 (`work/done/brainstorm-run/`, the first occurrence). Claude Code headless, inside `../focus-kit-clinic`, with `--model claude-opus-5-5 --setting-sources project --strict-mcp-config --permission-mode acceptEdits --permission-prompts none --output-format stream-json --verbose` and `--allowedTools "Bash(npm *)" "Bash(npx *)" "Bash(node *)" "Bash(mkdir *)" "Bash(cp *)" "Bash(git add *)" "Bash(git status *)" "Bash(git diff *)"` (the space-wildcard form `claude --help` shows in 2.1.284; the exact list recorded); `git commit`, `git push` and `git tag` are not on it, so a commit would be denied as well as against the kit's instruction. Command: `claude -p "/apply skeleton"`. No brief: the page is the brief. A denied call is recorded; if the run cannot finish, /apply stops and asks the author before any second run.
* The skeleton's Done when item "`npm run dev` leaves client and server running locally" is the author's, not the run's: the agent never starts `npm run dev`, since a server held by a headless turn could block the port and conflict with the author's own. After the run the author starts it, confirms the page and `GET /api/health`, and keeps it running to check the pages during the review. The README and the chapter say so in one sentence.
* Recorded in `work/done/apply-run/`: `README.md` (date, `claude --version`, model, commit, commands, what happened), the transcript of every turn (text blocks byte for byte, tool calls as name and relative path or command), `verify.txt` (the last `npm run verify` output of the run), the proof PNG copied from the clinic, `skeleton-done.md` (the page as the run left it), `review.md` (each request of the author and its turn), `review.diff` (the staged tree before and after the review, if it changed), `git-status-staged.txt`, `commit-message.txt` (as suggested), and `duration.txt` (the run's result event: duration and number of turns, for the record; the chapter cites no cost number).
* The review. /apply stops after the run and shows the author the staged change and the page's What happened. Each request is sent by /apply to the same session with `--continue`, word for word as the author gives it, as a recorded turn; nothing in the clinic is edited by hand. `--continue` this time, so the review keeps the build's reasoning that chapter 10's fresh session lacked; only if the session cannot be continued, a fresh interactive `/apply skeleton` with the request after the slug, recorded as chapter 10's `turn-3.txt`, and the chapter says so. /apply writes the chapter only after the author says the review is over.
* The clinic after it: everything staged by the agent; the author commits with the kit's message (docs/05 §6 of the clinic), then creates the annotated tag `book-v1/apply` on that commit, message "One Page at a Time, chapter apply", and pushes both; `make verify` of this book goes green only after that push (docs/05 §5).
* The image. The screenshot is the book's first raster image: the record's copy stays in `work/done/apply-run/`, the book's copy is `book/assets/11-skeleton-390x844.png` (the same bytes, both kept; the same file in both editions, untranslated, the artifact as it ran, with a sentence in Portuguese giving its text), and its rendering proven by screenshots of the site in light and dark and of the PDF, in both editions, as `work/done/apply-<edition>-<what>.png` (docs/05 §5).
* Numbers, and only these: those the run's own output prints and the chapter quotes (test counts, verify timings as printed). The Claude Code version and model in the run's source note only.
* docs/03 terms used: command, page, delivery, verify, proof, slot, fresh session, unit of work, mark, queue, guided project, chapter tag. No new term.
* Sources (`[^key]`, same keys in both editions):
  * `[^focus-kit-apply]` (new): `SETUP.md` §3.4 at focus-kit `e7607c58ad38e70e3496518a58d4237612e21ebc`, installed in the clinic at `3f0b47c`.
  * `[^apply-run]` (new): `work/done/apply-run/README.md` on `main`.
  * `[^focus-kit-unit-of-work]` (reused from chapter 10).
  * The tag `book-v1/apply` linked where the code is pointed to.
* Cases: the clinic. No Ninjobs, no Case A or B.
* Exercises, on the clinic, by conversation with the agent, never by hand:
  * 11.1 After exercises 10.1 and 10.2, run `/apply skeleton` in a fresh session and compare your staged change with `book-v1/apply`.
  * 11.2 Review your staged change with the questions of section 4, ask the agent for each correction, and commit it yourself.
  * 11.3 For each divergence in your page's What happened, say whether it should have been a question on the page before `/apply`.
* Documents: docs/06 line `apply` keeps its slug and description. docs/00 §Contents already names chapter 11. docs/03 unchanged. docs/05 unchanged unless the image's proof shows the rule needs a word. The page's What happened records the exercise answers for the `exercise-answers` appendix.

**Out of scope.**

* Code excerpts and how the code is organized: Part III (FOCUS) and the tag.
* The git side of "never commit" (branches, merges, the commit as review in depth): Part IV, chapter 19.
* A cost measurement of `/apply`: chapter 10 cites `/usage`; chapter 24 covers cost.
* Changing the kit: this delivery only cites `e7607c5`.
* The next queue line of the clinic (`clinic-setup`): no chapter builds it now.
* The whole-milestone review: chapter 12.

**Done when.**

* [x] Run recorded in `work/done/apply-run/`; the exact allowlist and every denied call, if any, are in the README.
* [x] The author reviewed the staged change; every correction is a recorded turn; nothing in the clinic edited by hand.
* [x] The agent never ran `npm run dev`; the author ran it after the run and confirmed the page and the health route.
* [ ] The author committed and pushed the clinic's commit and the tag `book-v1/apply`.
* [x] Both editions written, same file name and heading structure, opening with the Objective in at most three sentences.
* [x] No filler and nothing useful cut; every number cites its source; no draft marker.
* [x] Every excerpt in the English edition matches its source byte for byte (verify tail, What happened, staged status, commit message, closing line, review requests and diff), checked by script; translated in Portuguese with the note, as chapter 10.
* [x] The image renders: site light and dark and PDF, both editions, screenshots in `work/done/`.
* [ ] `make verify` green.
* [x] `make book` builds; both PDF paths given to the author.
* [x] docs/06 line `[x]`, page in `work/done/`, staged, commit message suggested.

The two unticked items are the author's and wait on one push: the clinic's commit and the tag `book-v1/apply`. `make verify` is red only on the link check, on the three links to the tag (`tree/book-v1/apply` twice and `blob/book-v1/apply/docs/05-Process.md`) and on the link to `work/done/apply-run/README.md` on `main`, in both editions; they answer once the clinic's tag and this commit are pushed.

**What happened.**

The run, 2026-09-28: Claude Code 2.1.284, model `claude-opus-5-5`, one headless session of three turns in `acceptEdits`: the run, then two review turns with `--continue`. Everything is in `apply-run/README.md`.

Diverged from the plan:

* `--disallowedTools "Bash(npm run dev*)"` was added to the command before the run, by the author's decision: `Bash(npm *)` allows `npm run dev`, and the clinic's page lists it in Done when, so the agent would try it. It did, once, and was denied. The README records it beside the exact allowlist.
* Five calls were denied in turn 1, listed in the README: two compound shell commands, a server start with a variable prefix, `npm run dev`, and `git mv`. `acceptEdits` let `mv` and `rm` inside the project through with no approval, which the README says.
* Verify was green the first time; it went red once, on Biome's formatting, after the agent removed the line that took the screenshot, and green again after the fix. The chapter tells it in one sentence and quotes the last, green output.
* The review's findings were listed by the agent running this /apply, as in chapter 10, and the author took all five; they went to the run's session as one request, byte for byte as listed. The agent then asked whether to keep `@hono/node-server`, so a second request, the author's "Keep it", became turn 3. The request was sent through the shell, which dropped its final newline; the README says so.
* In turn 2 the agent wrote two notes into Claude Code's auto-memory folder for the clinic, outside the repository: `--setting-sources project` does not turn auto-memory off. The author had them deleted after turn 3, so the book's next runs on the clinic start as a reader's would. The chapter says it in one sentence; the README records it, and `turn-2.txt` replaces their paths with a placeholder.
* The review changed only the record, not the code: the clinic's page (What happened, one Done when item) and its docs/05 (the local environment: the person starts `npm run dev`). `review.diff` holds both; it compares the staged tree before turn 2 with the staged tree after turn 3.
* The clinic's page keeps the `npm run dev` item unticked, with its reason in What happened; the author started it after the run, confirmed the page and `/api/health`, and kept it running through the review.
* The session id is kept out of the record: the disclosure scan matched it against an entry of the list. The README says the three turns reported the same one.
* `skeleton-done.md` is the page as turn 1 left it; the reviewed page is in the clinic's commit.
* The record adds `turn-1.txt` to `turn-3.txt` as the transcript, and `duration.txt` holds each turn's duration, number of turns and denied calls; the chapter cites none of them.
* The page's Contract names `review.md` with "each request of the author and its turn"; it holds the requests and the replies' text, and the tool calls are in the turn files.

Contradiction found and resolved with the author: docs/04 §Files said images have "no text inside, so one image serves both editions", and this page shows the screenshot, text included, in both editions. The author chose to add a word to docs/04: a screenshot of an artifact of a run is shown as it ran, one PNG for both editions, the same bytes as the record's copy, with the Portuguese edition giving its text in a sentence.

What the proof found: the first screenshots of the site and the PDF showed the white screenshot with no edge. On the light site it merged with the page, and in the PDF it filled a whole page, where it read as a blank page with "Clinic" on it and pushed its caption to the next page. Fixed in the three stylesheets: every PNG gets a thin border and a reduced width (280 pixels on the site, 45% of the text width in the PDF and EPUB); docs/04 states the rule and docs/01 names it in the three files. After the fix the image shows its edge in light and dark and keeps its caption on its page in both PDFs; the proof files are `work/done/apply-<en|pt>-<site-light|site-dark|pdf>.png`, taken with the clinic's Playwright over the built site, served locally, and with `pdftoppm` for page 104 (English) and 112 (Portuguese). The image is the same file in both editions (`book/assets/11-skeleton-390x844.png`, same bytes as `apply-run/skeleton-390x844.png`).

Proof: `make verify` green up to the link check, which fails only on the links above; the disclosure scan green alone. The English excerpts were compared by script with their sources: the verify tail (`verify.txt` lines 14 to 51), What happened (`skeleton-done.md` lines 129 to 176), `git-status-staged.txt`, `commit-message.txt`, the closing line (`turn-1.txt` lines 203 to 205), the request (`review.md` and the file sent) and `review.diff`: all identical. The Portuguese edition translates the prose artifacts (What happened, the commit message, the closing line, the request) with the note; the verify output, the status and the diff stay as they ran, the diff followed by a sentence giving its content in Portuguese. `make book` printed the known warning `Ignored user-select: none`, as in earlier chapters.

Exercise answers, for the `exercise-answers` appendix:

* 11.1: the staged trees will differ in the code and in the versions npm installs on the day; the same shape should hold: the `health` slice, the migration runner in `src/server/`, `Result` in `src/lib/`, the documents updated, the page in `work/done/` with its screenshot, and `skeleton` at `[x]`.
* 11.2: this chapter's review is a model: a dependency the page did not name, a proof held only by a test and missing from What happened, an explanation in the wrong place, a rule of docs/05 that a headless agent cannot keep, and a claim nobody tested.
* 11.3: in this run, `@hono/node-server` should have been a question on the page (the kit forbids an unnamed dependency); how `npm run dev` starts two processes, and how the server runs its TypeScript, were fair choices inside ADR-0001; the versions npm installs are not a page question unless the project pins them.
