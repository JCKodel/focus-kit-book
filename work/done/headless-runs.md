# headless-runs

**Objective.** A reader of chapters 7 to 12 knows what the book's headless runs and their `--continue` are, and what they do in their own interactive session instead, so they can follow each run the chapters show.

**Behaviour.**

* In chapter 7, where "headless" first appears (§ after the brief, "Open your host at the root of your repository…"), the text says what a headless run is: Claude Code run from the terminal with `claude -p`, one prompt per call; it prints the answer and exits, with no one to approve anything. Each answer to a round was a new call with `--continue`, which sends it to the most recent conversation in that directory. The book runs headless so every turn is recorded; in an interactive session the reader just types the answer in the same session.
* In chapter 11, where the review list goes "to the run's session with `--continue`", a clause says that is the headless way of typing in the same session, with a pointer to chapter 7; interactively, the reader sends the list in the session where `/apply` ran.
* In chapter 12, where the decisions go "to the review's session with `--continue`", the same clause and pointer; interactively, the reader types the decisions in the review's session.
* Chapters 8 and 10 keep "headless" as it is: after chapter 7 the word is known, and neither shows `--continue` in its text.
* Both editions say the same; the Portuguese keeps "sem interface" for headless, as it does today.
* Finding F14 of the M3 review, as narrowed in its decisions, is settled.

**Contract.**

* Files: `book/en/07-brainstorm.md` and `book/pt/07-brainstorm.md` (line 87 in English, 88 in Portuguese, and the sentences after it if the definition needs its own line); `book/en/11-apply.md` line 252 and `book/pt/11-apply.md` line 258; `book/en/12-closing-a-milestone.md` line 87 and `book/pt/12-closing-a-milestone.md` line 87.
* Terms of docs/03: "headless" (Portuguese "sem interface", identifier `claude -p`), added by this proposal, before the page; chapter 7 is its first use.
* Facts, from the run records: `claude -p` and `--continue` as in `work/done/brainstorm-run/README.md` (lines 16 and 22); `--continue` taking the directory's most recent conversation as in `work/done/m3-review-run/README.md` line 47.
* Sources: one new note in chapter 7, both editions, to Anthropic's Claude Code documentation on running Claude Code headless (the `-p` flag and `--continue`), with its access date; `/apply` opens the page, uses the URL the documentation serves, and the link check proves it. The existing `[^brainstorm-run]`, `[^apply-run]` and `[^closing-a-milestone-run]` are unchanged.
* Cases, exercises: unchanged.
* Queue: the line changes from "Chapters 10 to 12" to "Chapters 7, 11 and 12", since "headless" first appears in chapter 7 and chapter 10 has no `--continue`.

**Out of scope.**

* The M3 review's wrong-session incident with `--continue`: a book-side run, not in any chapter.
* Who the second agent is and how a reader alone would produce its list: F14's decision narrowed the finding; the chapters already name it.
* The full flag list of the runs (`--model`, `--setting-sources`, `--output-format` and the rest): the run records have it, a reader works interactively.
* Chapter 8's permission paragraphs: they already contrast headless with interactive.

**Done when.**

* [x] Chapter 7 says what a headless run is, what `--continue` does, and what the reader does interactively; both editions, same meaning.
* [x] Chapters 11 and 12 say, at `--continue`, that it is the headless way of the same session, point to chapter 7, and say what the reader does interactively; both editions.
* [x] The new note opens, and the link check proves it.
* [x] `make verify` green, the link check included.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Chapter 7 gets three sentences after the line where `/brainstorm` runs headless: what a headless run is, what `--continue` does, and why the book runs headless with what the reader does instead. Both editions cite the new note `[^claude-code-headless]`, Anthropic's page "Run Claude Code programmatically" at `https://code.claude.com/docs/en/headless`, accessed 2026-09-29; the link check opens it.
* That page says `--continue` continues "the most recent conversation" and does not name the directory; the CLI reference page does ("in the current directory"), and so does the M3 review's run record. The sentence keeps "in that directory" under the one note the page asked for, since it states no number and quotes nothing.
* Chapters 11 and 12: the clause and the pointer to chapter 7 went into the sentence with `--continue`, and what followed it ("as it was", "in one request that also asked for the lines") became its own sentence, so no line carries three clauses on semicolons.
* The definition of "headless" in docs/03, added by /propose before this page, is unchanged.
* Proof: `make verify` green, the link check included; `make book` built both PDFs.
* Finding F14 of the M3 review, as narrowed in its decisions, is settled.
