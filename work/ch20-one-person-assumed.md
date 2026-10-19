# ch20-one-person-assumed

**Objective.** After chapter 20 the reader can also say what the kit assumes of the people around a delivery, one person who proposes, uses the delivery, reviews the staged diff and commits, and that on a team whoever commits, or merges the pull request, is that reviewer; and can give a team's board its refresh through a slot of the project's own in docs/05 §5 that `/propose` and `/apply` follow, never by editing the commands' files.

**Behaviour.** What the reader can do or explain after the chapter:

* Asked "who does the kit expect to review a delivery?", the reader answers: the person who commits it; the kit assumes one person who proposes, uses the delivery, reviews the staged diff and commits, and splits those roles no further.
* Asked "on a team with pull requests, who is that reviewer?", the reader answers: whoever merges the pull request, since on a branch the merge is the delivery's one change; a second reviewer before the merge, an agent or a colleague, is the team's practice, which the pull request holds and the kit does not assign.
* Asked "the team wants every mark change pushed to its board; where does that go?", the reader answers: a slot the project adds to docs/05 §5 that names `/propose` and `/apply` and the command that pushes the queue; the commands follow it as they follow the kit's slots; the command files stay the kit's, written by its installation, and nobody edits them.
* The reader can say why such a board shows a mark at once whichever branch the delivery is on: the slot runs inside the command that changed the mark, so the board does not wait for a merge, unlike a board that only reads the main branch's queue (chapter 14).
* Edge: chapter 18's rule stays true beside the new sentence: trunk is for one person; two people work on branches or worktrees, where the merge is the commit the reviewer makes.
* Edge: Case A's sentences stay as they are; nothing says how Case A's customization was wired, and the slot sentence is general, about any project.
* Fails: a sentence that narrates how the kit came to this (skills that listed their slots, command files edited and redone on each update), says "now", or gives a version, date or number for the kit's change; a slot example repeated from chapter 7; any reader who does not read code (out of scope below); one edition changed and not the other.

**Contract.** Files `book/en/20-team-tools.md` and `book/pt/20-team-tools.md`, same changes in both, line numbers as of this page (same in both editions):

* Opening (line 3): one clause added: the reader can say whom the kit assumes reviews and commits on a team, and give a board its refresh through a slot of docs/05 rather than an edit to the commands. Line 4 (the wiki) stays.
* `## The problem` / `## O problema`, line 8 ("One person working on trunk uses the delivery, reviews the staged change and commits it."): becomes the kit's assumption, one person who proposes, uses the delivery, reviews the staged diff and commits it, and the kit splits those roles no further. Lines 9 and 10 stay; they already name what a team adds.
* `## The pull request as the team's review`, after line 32 ("...the person decides what is a finding, and approves the merge."): one sentence: that person, whoever merges, is the reviewer the kit assumes; the merge is the delivery's one change, as the commit is on trunk. No other line of the section changes.
* `## Boards` / `## Quadros`, after line 56 (Case A's commands refreshing the board), before line 57 (the fold): two sentences, general, not about Case A: a project gives its board this refresh with a slot of its own in docs/05 §5 that names `/propose` and `/apply` and the command that pushes the queue, which the commands follow as they follow the kit's slots, with no edit to their files, which are the kit's (a back-pointer to [chapter 7](07-the-documents.md) inside the sentence, where such a slot is shown); and since the slot runs inside the command that changed the mark, the board shows it at once whichever branch the delivery is on. Lines 53 to 58 otherwise byte for byte.
* `## Key points` / `## Pontos-chave`: the pull request bullet (line 81, "The reviewer reads the page...") gains "whoever merges is the reviewer the kit assumes"; the board bullet (line 83) gains "refreshed by a slot of docs/05 that the commands follow, not by an edit to them".
* `## What the team gains`: unchanged; its Case A sentence stays.
* Wording: one sentence per line; Portuguese edition with "slot", "trunk", "branch", "merge", "pull request", "quadro" as the chapter already writes them; `/propose`, `/apply` and docs/05 unchanged in both.
* Terms of docs/03: `slot` (its row already says a project may add one that /propose or /apply follows, with no edit to the skill), `board mirror`, `trunk`. No new term; no docs/03 row.
* Sources: focus-kit README ("The kit assumes one person who proposes, uses the delivery, reviews the staged diff and commits. On a team, whoever commits is that reviewer; the kit does not split the roles further."), docs/05 §5 intro ("The project may add slots of its own; a slot that names /propose or /apply is followed by that command, with no edit to the skill."), docs/03 `slot` and `board mirror`, `work/done/kit-2026-10-19.md`. The kit is named in prose; no footnote, since the reader gains nothing to open (docs/04).
* Cases: Case A, unchanged sentences only. No number added.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* The lending library's Board slot as a quoted block: chapter 7 shows it (`ch07-slots-and-decided`); chapter 20 points back.
* The Git slot letting the agent commit by its word: `ch07-review-git-slots`.
* Where a board that reads the queue sees a mark on trunk or at the merge: chapter 14 (`ch14-where-a-board-sees`), which hands chapter 20 only the mirror refreshed by the commands.
* A person who does not read code (takes part in `/propose`, tests the delivery as its user, asks where things stand or what a page decided): the kit's README says it and M21's paragraph promises it, but no M21 line carries it, this one included; reported to the driver, not written here.
* How Case A's board refresh was wired, and the kit's history of edited command files: before/after, and a private case's detail the documents do not give.
* Issues, question deliveries, the wiki section and every other part of chapter 20: they keep what they say.

**Decisions from the documents.**

* The assumption is the kit's own sentence, from focus-kit's README, which `CHANGELOG.md` 2026.10.19 says the READMEs now state.
* A project slot that names `/propose` or `/apply` is followed with no edit to the skill: docs/05 §5 intro and docs/03 `slot`.
* On a branch the merge is the delivery's one change: the kit's docs/05 template, Git slot ("one commit on trunk, one merge otherwise"), in the installed `references/documents.md` at 2026.10.19; this repository's own slot is trunk.
* Trunk is for one person, not two: docs/03 `trunk` and chapter 18.
* Taught as the kit is today, no version or "now": AGENTS.md and the M21 rule.

**Decisions taken alone.**

* The assumption rewrites line 8 of `## The problem` instead of a new section: that line already describes the one person, and the problem then names what a team adds.
* "Whoever commits is the reviewer" is said for a team on pull requests as "whoever merges", in the pull request section, since the merge is the commit there; the kit's README says "commits".
* The Board slot sentence is general and placed beside Case A's, not attributed to Case A: no document says how Case A's refresh was wired, and saying it would need OD-3 approval.
* Chapter 20 does not quote a slot; it points back to chapter 7, which shows the lending library's.
* The "at once whichever branch" clause is added because chapter 14's page sends the reader here for it.
* The opening gains one clause; no new key point bullet, two existing bullets gain a clause each.

**Done when.**

* [ ] Both editions changed in the same places (opening, line 8, the pull request section's sentence, the Boards sentences, two key points) and nowhere else in chapter 20.
* [ ] The chapter still opens with its value; no filler, nothing useful cut; one sentence per line kept.
* [ ] No version, date, "now", before/after, history of edited command files or narration of a run; no em dash.
* [ ] Case A's existing sentences byte for byte, so no new private text to approve; no number added, so none to source.
* [ ] The back-pointer to chapter 7 sits inside a sentence that says something; no slot block quoted.
* [ ] `make verify` green; `make book` builds both editions, and both PDF paths reported.
* [ ] Delivery review as docs/05 §5 says; only this delivery's paths and its hunk of docs/06 staged; the page moved to `work/done/` and its commit message suggested.
