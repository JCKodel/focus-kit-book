# ch20-21-git-cut

**Objective.** A reader of chapters 20 and 21 meets the decision each chapter serves (one delivery, one step to undo; one folder per agent when their files meet) before the definitions, finds no history or glossary a manual already gives, and reads each thing once; both editions.

**Decided from the documents.**
1. Chapter 20 opens, after §The problem, with the merge table and the rule "one delivery, one step to undo", since that is the decision the kit's Git slot records (docs/05 §5 Git; docs/04 Value first); the definitions follow in the order the table needs them.
2. What *Pro Git* teaches as a glossary (remotes, the `.psd` story, the history of BitKeeper) leaves, with the note kept where a definition the chapter still uses cites it (docs/04, a note only where the reader gains something to open); the one fact the chapter uses from the history, that a branch is only a name and costs nothing, stays as one sentence.
3. Chapter 21 keeps what no manual gives: two sessions in one folder, what is and is not a conflict, the container's one shape, the committed-marker trap, when parallel stops paying; the three sections that define, justify and re-explain a worktree become one (docs/04, Teach, do not report; No filler).
4. The `remote.origin.fetch` configuration goes to a manual of the lending library's docs/05, as chapter 21 already says it does for a real project; the chapter keeps the command and one sentence of warning (docs/05 §5 Manuals: a slot names the command and points to its manual).
5. Line numbers are not cited: `ch21-hidden-folder` (M14) changes chapter 21 before this line; passages are named by section and first words.

**Behaviour.**

* A reader who stops chapter 20 at the end of its second section can already say the rule: a delivery is one commit on trunk or one merge otherwise, and one command takes it back; the table of the four merge forms is on the page before `git merge` is defined.
* A reader who looks for what a remote is finds two sentences in §Commits and the history (clone copies, push sends, pull brings) and no section of its own.
* A reader finds no `logo final final.psd`, no BitKeeper, no 1991; the sentence "a branch is only a name, which is why it costs nothing" stays with its *Pro Git* note.
* A reader of §Trunk and §git-flow finds one paragraph each: what it is, who described it, and what it is in the kit's terms; the five bullets of git-flow become one sentence naming the five branch kinds, and Driessen's 2020 note stays, since it is the reason a web app does not need it.
* A reader of chapter 20's gain reads "one delivery, one step to undo" with the three-line log of §Commits and the history as its evidence, and "a person who never opens the code can follow it" only if that log is shown; the sentence "There is no number for this gain" stays once (and leaves if `one-gain-section` moves it to the prologue).
* A reader of chapter 21 finds one section, §What a worktree is and when it pays, where §What a worktree is, §When a worktree still pays and §How it solves the problem were: what a worktree is (shared history, own files, own `HEAD`, no branch in two folders), the two cases where it pays, and the two agents on `return-book` and `overdue-list`; "Branches alone do not do it" and "A second clone" become two sentences inside it.
* A reader finds "bare repository" defined where `git clone --bare` first appears, in §The life of a worktree, and not before.
* A reader finds the `git config remote.origin.fetch` command with one sentence (a bare clone writes no fetch line, so `git fetch` brings no `origin/main` without it) and the pointer to the manual; the paragraph quoting the git documentation leaves, its note with it.
* A reader finds "One shape for every tool and every person prevents an error" rewritten as the error: a `/propose` running in another tool's folder writes the page where the next `/apply` cannot find it; one sentence.
* A reader of chapter 21's gain reads three sentences: two agents at once, each delivery still one change; the measured 155 seconds against 277 with its costs; the gain holds while the files do not meet and ends at the reviewer's speed. The sentences that repeat §When parallel stops paying leave.
* Fails: a definition cut that a later section uses without it (fast-forward, merge commit, squash, rebase, tag, worktree, bare); a note left without a reference; a Portuguese edition whose sections no longer match the English.

**Contract.**

* **Chapter 20, both editions, same file name and title; headings as follows.** §The problem unchanged. New order: §One delivery, one step to undo (the table of §Four ways to merge's end and the rule, moved up, with the two sentences that follow the table); §Commits and the history (plus two sentences on remotes); §Branches and tags (plus "a branch is only a name"); §Four ways to merge (the four forms, each defined, the table no longer at its end); §Undoing a delivery; §Trunk (one paragraph); §git-flow (one paragraph); §Choosing; §What the team gains; §Key points. §Version control, and why git shrinks to its first two sentences and the one on distribution, placed at the start of §Commits and the history. §Remotes: clone, push and pull is removed. Notes `[^pro-git-about]`, `[^git-flow]` and the others stay where a sentence still cites them; `[^git-clone]` only if a sentence does.
* **Chapter 21, both editions, same file name and title; headings as follows.** §The problem: one folder, two jobs; §Two sessions in one folder; §What is and is not a conflict there; §What a worktree is and when it pays (the three sections merged, bare moved out); §The life of a worktree (bare defined at `git clone --bare`; the fetch configuration as one command and one sentence with the manual's pointer); §Worktrees in the kit (the "one shape" sentence rewritten as the error); §When the branches meet: the conflict; §The trap: committing the markers; §When parallel stops paying; §What the team gains (three sentences); §Key points. The hidden folder and prefix names are whatever `ch21-hidden-folder` wrote.
* **Terms:** worktree, container folder, main worktree, trunk, branch per delivery, as docs/03 has them; no new term.
* **Sources:** notes kept with their sentences; the git documentation quotation on `--bare` leaves with its paragraph; no note added.
* **Cases:** the author's measured run of chapter 21 stays as the gain's number; no private case changes, no OD-3.
* **Code examples:** the command blocks of both chapters stay, except the fetch block, which keeps its two lines and loses the paragraph around it.
* **Checks:** `grep -c "BitKeeper\|logo final" book/*/20-*.md` gives 0; `grep -c "^## " book/en/20-*.md` equals `book/pt/20-*.md`, likewise for 21; the merge table appears before "## Commits" in both editions of chapter 20.

**Out of scope.**

* Chapter 22's pull request, which builds on remotes: unchanged, the two sentences in chapter 20 are what it needs.
* The names `.focus-kit/` and `focus-kit/`: `ch21-hidden-folder`.
* The manual that holds the fetch configuration: the lending library has no repository (ADR-0017); the chapter says the step belongs in `docs/manuals/` of a real project, as it already does.
* The gain's "no number" sentence as a book-wide rule: `one-gain-section`.
* Chapter 20's choice table (§Choosing): kept whole, it is the decision.

**Done when.**

* [ ] Both chapters changed in both editions, headings as Contract; each opens with its value and reaches its decision in its second section; nothing a later section needs is cut.
* [ ] The checks of Contract hold; every note definition keeps a reference; `make verify` green.
* [ ] Word count of chapter 20 and 21 recorded on this page, before and after, as a record and not as a target.
* [ ] `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Decisions in the review.**

* The three-line log is shown in the gain as its evidence, as recommended.
* The `.psd` paragraph is cut entirely, as recommended.
