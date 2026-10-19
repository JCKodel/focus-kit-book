# ch20-roles-and-points

**Objective.** After chapters 20 and 23 a reader can say who the reviewer the kit assumes is under both forms of the Git slot, by default the person who reviews the staged diff and commits, or merges, and by the slot's word the person who reviews the commit, or the merge, the agent made; that the kit splits those roles no further and a team's split of them is the team's own practice; and chapter 20 ends with five key points, as docs/04 allows; least change, both editions.

**Behaviour.**

* Reading chapter 20's "The problem", the reader learns that the kit assumes one person who proposes a delivery, uses it and reviews it: by default the staged diff, before committing it; by the Git slot's word, the commit the agent made, after it lands; and that the kit splits those roles no further, how a team splits them being its own practice.
* Reading chapter 20's "The pull request as the team's review", the reader learns that by default whoever merges is the reviewer the kit assumes, the merge being a branch's one change as the commit is on trunk, and that when the Git slot's word lets the agent merge, the reviewer is the person who reviews the merge after it lands.
* Reading chapter 23's "Roles in a team", the reader learns that the kit assumes one person in every role (chapter 20) and that a team, as its own practice, gives each step to whoever owns it; the five role bullets that follow stay.
* Chapter 20's "Key points" has five bullets: the roles bullet holds under both forms; one pull-request bullet carries one delivery and its reviewer under both forms; the issue, board and question-delivery bullets stay as they are.
* Every other sentence of both chapters stays.
* Fails if: a changed sentence is false under either form; the slot's word is extended beyond commit and merge; the text says the kit, or the method, gives the roles to different people; chapter 20 keeps six key points or loses the board or question-delivery bullet's text; chapter 20's board passage (line 60) or its board bullet (line 88) changes; it names a version, a date, a before and after, a host command or this repository's own Git choice; it narrates a run; a title changes.

**Contract.**

The same passages in both editions, `book/en/` and `book/pt/`. Wording is /apply's within the sense below; the Portuguese reuses the phrasing chapters 13 and 23 already use: "por padrão", "pela palavra do slot Git", "a pessoa revisa o commit".

Chapter 20, `20-team-tools.md`:

* §"The problem", line 8 (pt 8): "who proposes a delivery, uses it, reviews the staged diff and commits it, and splits those roles no further" becomes: who proposes a delivery, uses it and reviews it, by default the staged diff before committing it, or, when the Git slot's word lets the agent commit, the commit after it lands; the kit splits those roles no further, and how a team splits them is the team's own practice. No pointer to chapter 23 (docs/04, "Chapter pointers": a pointer forward only names a term not yet taught).
* §"The pull request as the team's review", line 34 (pt 34): "Whoever merges is the reviewer the kit assumes: on a branch the merge is the delivery's one change, as the commit is on trunk." gains "By default" (pt "Por padrão") and one clause: when the Git slot's word lets the agent merge, the reviewer is the person who reviews the merge after it lands.
* §"Key points", lines 84 to 89 (pt 84 to 89), six bullets become five:
  * Line 84: "who proposes, uses, reviews the staged diff and commits" becomes who proposes, uses and reviews, by default the staged diff before committing, or the commit the Git slot's word let the agent make, and a team splits those roles as its own practice; the rest of the bullet stays.
  * Lines 85 and 86 become one bullet: a pull request carries one delivery (branch by slug, page first, build after, one merge with the page, the code and the mark); its reviewer reads the page, then the diff against it; an agent may review first, a person decides; whoever merges is, by default, the reviewer the kit assumes, or, by the Git slot's word, the person who reviews the merge the agent made.
  * Lines 87, 88 and 89 stay.
* Stays: the opening (lines 3 and 4, "who on the team is the reviewer the kit assumes", true under both forms); line 10, "a second person who reviews before the merge", a team's need, not a claim on what the kit assumes; line 33, "the person decides what is a finding, and approves the merge", a code host's approval, which the slot's word does not remove; lines 51 to 62, the board passage (`ch14-20-board-branch`).

Chapter 23, `23-adoption.md`:

* §"Roles in a team", line 58 (pt 58): "The method gives each step to whoever owns it." becomes: the kit assumes one person in every role ([chapter 20](20-team-tools.md)); a team, as its own practice, gives each step to whoever owns it. The pointer back stays under docs/04, "Chapter pointers": chapter 23's roles are a map where the pointers are the content.
* Stays: lines 60 to 66, the role bullets (`ch13-19-commit-by-slot` made them hold under both forms), and the rest of the chapter.

Terms of docs/03 used: slot, trunk; the Git slot's two forms are the kit's slot template as chapter 7 teaches them. No new docs/03 row. No number, footnote, private case or lending library example added. Sources cited: none new.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Chapter 20 line 60, "on any branch the delivery is on", and the board bullet (line 88): `ch14-20-board-branch` (driver).
* The kit README's "whoever commits is that reviewer" (lines 132 to 133): a note for focus-kit, carried by `docs-m21-tidy`.
* Chapter 23's role bullets and Key point: done in `ch13-19-commit-by-slot`.
* Chapters 6, 8, 13, 18 and 19's "by default": `m21-git-slot-default`.
* When a team should pick the slot's form, or how it should split the roles: no repository document gives a rule, and the point is that it is the team's practice.
* docs/03, docs/05, docs/06, AGENTS.md: no edit; the queue line is the driver's.

**Decisions from the documents.**

* The four candidates and their lines: `work/done/m21-review.md`, G6, G7, O9 and O1, confirmed by the author.
* At most five key points: docs/04, chapter skeleton ("Key points ... at most five bullets").
* The slot's word covers commit and merge only, and the person then reviews the commit: the kit's slot template (`.claude/skills/analyze/references/documents.md`, Git), as `work/done/ch13-19-commit-by-slot.md` records.
* "By default" for the person's reading before the commit: the same pattern `m21-git-slot-default` applies to chapters 6, 8, 13, 18 and 19 (docs/06).
* No forward pointer from chapter 20 to chapter 23; a pointer back from chapter 23 to chapter 20: docs/04, "Chapter pointers".
* No before/after, version or date: AGENTS.md, `work/done/kit-as-it-is.md`.

**Decisions taken alone.**

* This page supersedes `ch13-19-commit-by-slot`'s reading that chapter 20 line 8 is "true either way": the author confirmed G6 in `m21-review`.
* Five key points by merging the two pull-request bullets (85 and 86), not by folding the question-delivery bullet (89) into the board bullet (88): bullet 86 changes for G7 anyway, the two describe one pull request, and bullet 88 belongs to `ch14-20-board-branch`.
* The team's practice is said in both chapters, briefly in chapter 20's problem and as the opening of chapter 23's roles, since the finding names both sentences; chapter 23 now attributes the split to the team, not to "the method".
* Lines 10 and 33 of chapter 20 stay, each true under both forms as the Contract says.
* No docs/03 row: no new term enters.

**Done when.**

* Both editions changed in the listed passages, every other sentence the same.
* Chapter 20 opens with its value, as before; no filler, nothing useful cut: the merged key point keeps every clause of the two it replaces.
* Under `## Key points` / `## Pontos-chave` of `20-team-tools.md`, each edition has exactly five `* ` bullets.
* Lines 51 to 62 and 88 of chapter 20 unchanged in both editions (`git diff` shows no hunk there).
* No new number, footnote or case; no em dash.
* `make verify` green.
* `make book` built, both PDF paths given.
