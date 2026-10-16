# ch10-12-all-slots

**Objective.** After chapters 10 and 12 a reader can name every slot of docs/05 §5 as the kit fills it today, knows which of them `/brainstorm` asks about and which `/analyze` asks about, and knows what `/analyze` reads before it asks, the context folder and the scripts a person runs by hand included.

**Behaviour.**

* A reader asked to list the slots of docs/05 §5 names nine: documentation language, verify, environments, proof of a screen, publish policy, context, manuals, milestone review and git; chapter 10 lists them where it introduces docs/05.
* A reader who reaches question 6 of "Where a new fact goes" in chapter 10 sees the milestone review's command and whether `context/` is committed among the examples of a slot, beside verify, the environments and git.
* A reader of chapter 10 knows that the Publish policy, whatever it says, ends with /apply's last words saying which environment is at which version (chapter 15 teaches the words themselves).
* A reader of chapter 12 who runs `/brainstorm` is asked, under the process slots, whether `context/` is committed, which manuals exist ("none yet" on a new project) and which deep code review the person will launch at a milestone's close; the chapter's list of subject 5 names them.
* A reader of chapter 12 who runs `/analyze` knows it reads `context/` whole first, when it exists, and any Makefile or script a person runs by hand, and that it asks six subjects in one round: the two new ones are whether `context/` is committed (default: committed when the repository stays with the team, in `.gitignore` when it is delivered or public) and the milestone review (default: the one the host offers, if any).
* Failure: a reader whose `/analyze` asks six subjects and whose chapter says four thinks the kit changed under them; the chapter says six.
* Edge: `/brainstorm` and `/analyze` both create `work/done/` with a `.gitkeep`, so the folder survives a clone; "an empty `work/done/`" is gone.
* Edge: the review checklist of chapter 12 gains nothing: "every slot of docs/05 says what and the command" already covers the new slots.

**Contract.**

* **Chapter 10, both editions, file name, title and headings kept.**
  1. §The seven documents, docs/05: the slot list "the command that verifies a delivery, the environments, how a screen is proved, when anything is published, and the git strategy" becomes the nine slots in the kit's order: the documentation language, the verify command, the environments, how a screen is proved, when anything is published and that /apply's last words say which environment is at which version, whether `context/` is committed, the manuals, the deep code review a person launches when a milestone closes, and the git strategy.
  2. §Where a new fact goes, question 6: the examples become "the verify command, the environments, whether `context/` is committed, the milestone review's command, git".
  3. Key points, first bullet: unchanged (it names no slot).
* **Chapter 12, both editions, file name, title and headings kept.**
  1. §`/brainstorm`, subject 5: "the verify command, the environments, how a screen is proven, when an environment beyond your machine is updated, whether `context/` is committed, the manuals, none yet on a new project, and the deep code review you will launch when a milestone closes".
  2. §What it writes, and where it stops: "an empty `work/done/`" becomes "`work/done/` with a `.gitkeep`, so the folder survives a clone" (pt: "uma `work/done/` com um `.gitkeep`").
  3. §What it reads: the list opens with "`context/`, whole, when it exists: what people said that the code cannot (the section below)" and the CI item becomes "the CI configuration, and any Makefile or script a person runs by hand".
  4. §What it asks: "One round, of four subjects only" becomes six, the list gaining, after FOCUS and git: whether `context/` is committed, with the kit's default; and the milestone review, the deep code review the person will launch at each milestone's close, default the one the host offers, if any. The first milestone stays last.
  5. §What the code cannot say: the sentence "Whether the folder is committed, and what must never be, is a decision of its own (chapter 19)" gains that both commands ask it, with the default above.
  6. Key points, the `/analyze` bullet: "asks one round" stays; nothing added, since the bullet names no count.
* **Portuguese:** slot names as book/pt chapter 10 already has them; "revisão de marco" for milestone review (docs/03); `context/` and `.gitkeep` unchanged.
* **Terms:** slot, manual, milestone review, context folder, as docs/03 has them; docs/03 unchanged.
* **Sources:** the kit's `brainstorm/SKILL.md`, `analyze/SKILL.md` and docs/05 template at 2026.10.16.2, paraphrased with no note (docs/04: the kit as it is).
* **Cases:** none new. Code examples: the milestone block of chapter 12 unchanged.

**Out of scope.**

* The Milestone review slot's use at a milestone's close: `ch17-review-reads-code`.
* /apply's last words themselves: `ch15-24-whole-queue`.
* The context folder's commit decision in chapter 19: unchanged; chapter 12 points there.
* Chapter 12's milestone block duplicated in chapter 13: a cut, M15's `method-said-once`.

**Done when.**

* [x] Chapters 10 and 12 changed in both editions, same headings; each opens with its value; no filler and nothing useful cut.
* [x] The nine slots and the six subjects checked against `70fc709:SETUP.md` §§3.1, 3.2 and the docs/05 template.
* [x] No sentence in the book says `/analyze` asks four subjects or that `work/done/` is created empty.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* Nine slots in the kit's order: the docs/05 template at 2026.10.16.2; the book's own docs/05 §5 adds project slots (disclosure, cases), which are this project's and not taught.
* The Publish policy's last sentence named in chapter 10 as a property of the slot, taught in chapter 15: docs/05 template and the M14 split of lines.
* The context folder enters `/analyze`'s read list although the chapter's context section already says both commands read it: the kit's file lists it first, and the chapter's list says it is the kit's file's list.
* No note: docs/04, a source note only where the reader gains something to open; the kit's files are quoted as the chapter already quotes them.

**Decisions in the review.** None.

**What happened.**

* Chapter 10, both editions: the docs/05 paragraph names the nine slots in the kit's order, and a new line after it says that whatever the publish policy says, `/apply`'s last words say which environment is at which version (chapter 15). Question 6 of "Where a new fact goes" gains `context/` and the milestone review's command. Key points unchanged.
* Chapter 12, both editions: subject 5 of `/brainstorm`, the `.gitkeep` in `work/done/`, `context/` first in `/analyze`'s read list, the CI item with Makefiles and scripts run by hand, six subjects in the round with the two new ones before the first milestone, and the context section's last sentence saying both commands ask it, with the default above. Key points unchanged.
* Divergence: the Publish policy's last sentence became its own line after the slot list instead of a clause inside it, so the list stays nine names a reader can count.
* Divergence: in subject 5, "none yet on a new project" is written as a parenthesis after "the manuals" ("os manuais (nenhum ainda, em um projeto novo)"), so it does not read as a tenth item.
* The kit's text speaks of "this host"; chapter 12 speaks to the reader, so the milestone review's default reads "the one your host offers, if any".
* No other chapter lists the slots of docs/05 §5; nothing outside chapters 10 and 12 needed the change.

**Proof.** `git -C ../focus-kit show 70fc709:SETUP.md`: §3.1 and §3.2 match the installed `brainstorm/SKILL.md` and `analyze/SKILL.md` line for line apart from their fences, and the template's §5 matches `references/documents.md`; the nine slots and six subjects were checked against them. `grep` finds no "four subjects", "quatro assuntos" or empty `work/done/` in the book. `make verify` green. `make book` builds both editions: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the author's review.

```commit
docs(ch10-12-all-slots): name every slot and the six /analyze subjects

- Chapter 10 names the nine slots of docs/05 in the kit's order
- Question 6 adds context/ and the milestone review's command
- /brainstorm subject 5 asks about context/, manuals, milestone review
- /analyze reads context/ and scripts run by hand, asks six subjects
- work/done/ is created with a .gitkeep; both editions

work/done/ch10-12-all-slots.md
```
