# ch09-second-pair-of-eyes

**Objective.** After chapter 9 a reader starting a project with `/brainstorm` or `/analyze` can answer the one question both commands ask about review, whether a second pair of eyes reads each delivery before it ends and the whole milestone at its close, or keep its stated default knowingly, without knowing the name of any review tool or model; both editions.

**Behaviour.**

* Asked by `/brainstorm`, on the process slots, whether a second pair of eyes reads each delivery and the whole milestone, the reader can answer "your call" and say what that keeps: yes, the host's own review where it has one, else a read-only agent, for each delivery; the kit's readers over docs/01's modules, on the session's model, at a milestone's close.
* The reader can say where the one answer lands: the Delivery review slot ([chapter 13](13-apply.md)) and the Milestone review slot ([chapter 15](15-closing-a-milestone.md)) of docs/05 §5.
* The reader can say why the question names no tool or model: the agent never asks about a tool by name when the question is about what the person wants (the rule chapter 9 already teaches in "A default with every question"); the default carries the tool.
* Asked by `/analyze`, the reader recognises the reviews as one of six subjects in its single round, with a default that also keeps the host's deep review over the range when the project already launches one.
* Edge: the reader who wants no second pair of eyes can say no, and knows that the answer is theirs to give, not a question about tools.
* Fails if: the chapter still asks which model the milestone's readers run on, counts seven `/analyze` subjects, or tells how the kit asked before.

**Contract.**

Chapter `book/en/09-starting-a-project.md` and `book/pt/09-starting-a-project.md`, same passages in both:

* `/brainstorm`, the list of six subjects, item 5 (The process slots): its last clause, today "who reviews a delivery's changes before `/apply` ends, and how the milestone review's code reading splits", becomes the one question: whether a second pair of eyes reads each delivery before it ends and the whole milestone at its close.
* `/brainstorm`, the paragraph after "Each slot it writes in docs/05..." ("Two of those slots say who reviews", three lines): reframed around the one question and its default, yes, which lands in two slots. The Delivery review default stays as written (the host's own review, a skill or a command the agent can run, kept to the delivery's paths since another session may share the folder; otherwise a read-only agent). The Milestone review default is stated as a default, not a question: the kit's readers over docs/01's modules, one reader each, on the session's model; no mention of the host's deep review here, which `/brainstorm`'s default does not name.
* "A default with every question": the sentence "It never asks about a tool by name..." is tied to the review question in one clause (the review question is that rule at work), not restated.
* `/analyze`, "What it asks": "One round, of seven subjects only" becomes six; items 5 and 6 merge into one, "The reviews: whether a second pair of eyes reads each delivery before it ends and the whole milestone at its close", with the default of `.claude/skills/analyze/SKILL.md` §Ask: yes; the host's own review when it can be kept to a delivery's paths, else a read-only agent; and the kit's readers over docs/01's modules on the session's model, or the host's deep review over the range when the project already launches one ([chapter 15](15-closing-a-milestone.md)). The following item renumbers to 6.
* "What the team gains" and "Key points": unchanged unless one clause adds what the reader uses (a person who knows no review tool still answers); /apply decides, and adds nothing if it would repeat the first gain sentence.

Terms of docs/03 used: delivery review, milestone review, slot, milestone; "second pair of eyes" is the kit's plain wording of a question, not a domain term, and enters no table. No new docs/03 row. Sources: the installed `.claude/skills/brainstorm/SKILL.md` (step 5 and the asking rules) and `.claude/skills/analyze/SKILL.md` (§Ask), focus-kit 2026.10.19 (`work/done/kit-2026-10-19.md`). No number, no footnote, no private case, no code example.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* What the host's deep review is and how it differs from the kit's readers: ch15-who-reads teaches it; chapter 9 names the default and points to chapter 15.
* The slow tests in the Verify slot, and the rest of step 5's slot list: already taught; this line changes only the review clause.
* Any before/after: the chapter says what the commands ask today, never what they asked before (ADR-0017, the book is the kit today).
* docs/03, docs/05, docs/06: no change; the slots already say what the kit says (kit-2026-10-19).
* Every other section of chapter 9 (stack, context folder, review before you commit, strangler fig): untouched.

**Decisions from the documents.**

* The question is one, about both reviews, with the default stated: both installed skills at 2026.10.19 (`brainstorm` step 5, `analyze` §Ask).
* The Delivery review default keeps its current wording: the skills did not change it.
* `/analyze` asks six subjects: its §Ask lists six bullets, the reviews one of them.
* The `/analyze` default names the host's deep review "when the project already launches one", and the `/brainstorm` default does not: as each skill says.
* The tie to "never asks about a tool by name": `brainstorm` SKILL.md's asking rules, already taught in the same chapter.

**Decisions taken alone.**

* Items 5 and 6 of the `/analyze` list merge into one item, rather than keeping two items under one question: the skill has one bullet, and the chapter mirrors the skill's list.
* The host's deep review is named in half a clause with a link to chapter 15, and not explained here, to keep the boundary with ch15-who-reads, which runs in parallel.
* No docs/03 row for "second pair of eyes" or "host's deep review": the first is wording, the second already appears in docs/03's `milestone review` and `checker` rows, and ch15-who-reads owns any further term.
* Key points and the gain section are left to /apply's judgment, defaulting to no change.

**Done when.**

* [ ] Both editions written, the same passages changed in each, Portuguese read as Portuguese.
* [ ] The chapter still opens with what the reader can do after it; the review question reads as one question with its default; no filler and nothing useful cut.
* [ ] No sentence asks or says which tool or model the reader picks; no before/after; no narrated run; no em dash.
* [ ] `/analyze` counts six subjects in both editions, numbered 1 to 6.
* [ ] Every link resolves; no number added, so none to source.
* [ ] Delivery review as docs/05 §5 says.
* [ ] `make verify` green; `make book` builds both editions, and the two PDF paths are reported.
* [ ] Only this delivery's paths and its hunks of docs/06 staged; the page moved to `work/done/` and its commit message suggested.
