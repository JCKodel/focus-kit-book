# ch8-accept-edits

**Objective.** A reader of chapter 8 knows what `acceptEdits` is, why the book's run was denied `gh` and the issue pages, and that in an interactive session they would be asked instead and could approve.

**Behaviour.**

* In §"Check it against the code", the paragraph that opens "The review found a second gap" says, before the queue it quotes:
  * `acceptEdits` is a Claude Code permission mode: the mode sets what the agent may do without asking; in `acceptEdits` it reads, edits files and runs common file commands, and anything else, such as `gh` or opening a web page, needs your approval;
  * it is the least permission `/analyze` needs, which the run used (kept from today's text);
  * the run was headless, so no one could answer, and every approval it asked for was denied; that is why the queue came from the issue numbers alone. One clause on headless, only as it bears on permissions.
* The sentence after the quoted queue ("The fix allowed one command...") says that in an interactive session you see the question and approve `gh issue view` there, and the gap does not reach you unless you deny it; the run's allowed command for one more turn is the headless form of that approval.
* The Portuguese says the same, with "modo de permissão" for the term.
* Finding F10 of the M3 review is settled.

**Contract.**

* Files: `book/en/08-analyze.md` lines 303-304 and 323; `book/pt/08-analyze.md` lines 306-307 and 326 (today's numbers). Nothing else in the chapter changes; the agent's own words at line 97 ("no way to answer a permission prompt") stay as quoted.
* New term, already in docs/03 after "fresh session": permission mode, `modo de permissão`, identifier `acceptEdits`.
* Terms of docs/03 used: host, command, fresh session, permission mode (new). "Headless" is not added; `headless-runs` owns it.
* New source note, in both editions, after `[^analyze-run]`:
  * en: `[^claude-code-permission-modes]: Anthropic, "Choose a permission mode", Claude Code documentation, accessed <date of /apply>. <https://code.claude.com/docs/en/permission-modes>`
  * pt: `[^claude-code-permission-modes]: Anthropic, "Choose a permission mode", documentação do Claude Code, acesso em <date of /apply>. <https://code.claude.com/docs/en/permission-modes>` (the form of chapter 10's `[^claude-code-plan-mode]`).
  It is cited at the sentence that says what `acceptEdits` allows. Checked on 2026-09-29: the page's table gives `acceptEdits` as "Reads, file edits, and common filesystem commands", and says the same `--permission-mode` flag works with `-p`.
* The run's facts come from `work/done/analyze-run/README.md` (`--permission-mode acceptEdits --permission-prompts none`, turn 3's `--allowedTools "Bash(gh issue view:*)"`), cited by the existing `[^analyze-run]`.
* Cases, exercises: unchanged.

**Out of scope.**

* What headless and `--continue` are in general: `headless-runs`.
* How Copilot and Codex ask for approval: no checked source; the run was Claude Code.
* Line 93's description of the run and line 97's quote: the explanation lives where the gap has consequences.
* Chapter 7's "I ran it headless": `headless-runs`.

**Done when.**

* [x] Both editions changed, same meaning; the reader learns what `acceptEdits` is, why the run was denied, and what an interactive session shows.
* [x] The new note resolves and the link check passes.
* [x] No filler, nothing useful cut; no em dash.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Chapter 8, English: the gap paragraph now opens with what `acceptEdits` is ("a Claude Code permission mode, the setting that decides what the agent does without asking you"), what it allows and what needs approval, cited by the new `[^claude-code-permission-modes]`; the next sentence keeps "the least permission the command needs" and adds that the run was headless, with no one to answer, so every approval it asked for was denied.
* After the quoted queue: "In an interactive session you would see that question and approve `gh issue view` there, and the gap would not reach you unless you denied it." The fix is then "that approval given in advance".
* Portuguese: the same, with "modo de permissão" and "sem interface" for headless, the form chapters 7, 8 and 11 already use.
* The new note sits after `[^analyze-run]` in both editions, accessed 2026-09-29.
* docs/03 took the term permission mode (`modo de permissão`, `acceptEdits`) in this delivery. Nothing dropped, nothing diverged from the plan; lines 93 and 97 unchanged. Finding F10 of the M3 review is settled.
* Proof: `make verify` green, link check included; `make book` builds both editions, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
