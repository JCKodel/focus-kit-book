# queue-states

**Objective.** After chapter 16 the reader can read any queue line's state among focus-kit's six marks, say who sets each and at what moment, mark a line that waits with its reason and take it out again, and read the queue as a kanban board that shows work while it happens; the chapters around it and the book's own process follow the kit's 2026.10.05 marks.

**Behaviour.**

* A reader of chapter 16 can say what each of `[ ]`, `[~]`, `[>]`, `[*]`, `[x]`, `[?]` means and who sets it: the conversation that adds the line, /propose when it starts, /propose when the page is written, /apply when it starts, /apply with verify green, any session.
* They can say why a mark changes when the work changes and not when a command ends, from Case A: its board showed a delivery in Doing only after /propose had written the page, and five lines waiting on the client read as work nobody had started.
* They can name the three cases of `[?]` (the person says it is blocked; an answer was asked and not given; another line must be done first, such as a fix found in the middle of /apply), write `· blocked: <reason>` and `· blocked: after <slug>, <slug>`, and say how a line leaves `[?]` and to which mark.
* They know that /propose and /apply on a `[?]` line say what it waits on and go on only when the person says it is resolved.
* They can lay the queue out as a kanban board, a column per mark, and fold it onto a three-column board; and they know where the mark is seen: in the folder of the session that changed it, on `main` only once a branch's delivery lands, at once on a board a command refreshes.
* A reader of chapters 13, 14, 15, 17 (now 18), 18 (now 19) and 21 (now 22) meets the six marks, never three, and never reads `[?]` as Case A's alone or as rejected by this book.
* This book's own queue, docs/05 §4 and installed commands use the six marks: the next /propose here marks `[~]` when it starts.

**Contract.**

Precondition: focus-kit's SETUP.md with the line `Version: 2026.10.05` is committed in the focus-kit repository. If it is not when /apply starts, /apply stops and says so; nothing is built.

Renumbering, both editions, H1 number follows the file:

```
16-closing-a-milestone.md   → 17-closing-a-milestone.md
17-the-governor.md          → 18-the-governor.md
18-project-as-assistant.md  → 19-project-as-assistant.md
19-git-essentials.md        → 20-git-essentials.md
20-worktrees.md             → 21-worktrees.md
21-team-tools.md            → 22-team-tools.md
22-beyond-software.md       → 23-beyond-software.md
23-cost-and-where.md        → 24-cost-and-where.md
24-adoption.md              → 25-adoption.md
25-asking-for-more.md       → 26-asking-for-more.md
```

Every link `](NN-<slug>.md` and every mention "chapter N" / "capítulo N" (N from 16 to 25) moves to the new number in `book/`, docs/00 (Contents and Audience), docs/03, docs/04 and the prologue's parts map ("chapter 25" → 26). `work/done/` and the ADRs keep their old numbers as history; ADR-0017 gains an amendment line: chapters 16 to 25 became 17 to 26 when `queue-states` inserted chapter 16. No `book/assets/` file is numbered 16 to 25.

Files:

```
book/en/16-queue-states.md   new; # 16. The queue while it happens
book/pt/16-queue-states.md   new; # 16. A fila enquanto acontece
book/{en,pt}/13, 14, 15, 18 (governor), 19 (assistant), 22 (team tools)   edited as below
docs/00-Product.md     Contents, Part II gains "16 The queue while it happens"; numbers after it follow
docs/03-Domain.md      done by this page: mark, kanban board, waiting mark, blocked reason; /apply renumbers chapter mentions
docs/05-Process.md     §4 becomes the kit's six-mark text and table; §2's flow names the marks as it goes
docs/06-Queue.md       header line: the six marks and the two suffixes, as the kit's docs/06 header; queue-states [x]
docs/01-Architecture.md, AGENTS.md   the "Do not rebuild" line on `[?]` (ADR-0013) leaves
docs/adr/ADR-0018-six-marks.md       new: context (Case A's two errors), decision (the book follows the kit's six marks and installs the kit 2026.10.05), consequences (chapter 16, chapters 18 and 22 rewritten, ADR-0013 superseded), 2026-10-05
docs/adr/ADR-0013-three-marks.md     amendment: superseded by ADR-0018 on 2026-10-05
host files     the kit's update, as SETUP.md 2026.10.05 says, for every host this repository has
```

Chapter 16, sections in order (pt headings in parentheses):

1. Opening, at most three sentences.
2. `## The problem` (`## O problema`): Case A's board, text below for OD-3.
3. `## Six marks` (`## Seis marcas`): a table, mark · means · set by; a lending-library queue showing all six, `[?]` with both suffixes.
4. `## At the moment the work changes` (`## No momento em que o trabalho muda`): why a mark is set when the work starts or stops; where it is seen: trunk, a branch or worktree (on `main` only after the merge), a board refreshed by the command.
5. `` ## Waiting: `[?]` `` (`` ## Esperando: `[?]` ``): the three cases, a lending-library example each; the suffixes; any mark before `[x]` can wait; leaving it (the person says so, the session that records the answer clears it, /apply clears an `after` when its last line is `[x]`), back to `[>]` or `[ ]`; the commands stop on a `[?]` line.
6. `## The queue as a kanban board` (`## A fila como quadro kanban`): what a kanban board is and where it comes from, one or two sentences with a source note to a primary source; a column per mark; the same queue on a To Do / Doing / Done board, with `[?]` kept visible; chapter 22 shows a mirror to a team's board.
7. `## What the team gains`: a manager reads where every delivery stands without asking; Case A's five idle-looking lines and its late Doing, counted by the author. `## Key points`.

Terms introduced: the six marks, waiting mark, blocked reason, kanban board (docs/03). Sources: focus-kit's SETUP.md 2026.10.05 (source note), the kanban source, `azure-kanban` if quoted. Cases: Case A only.

The Case A passage, as it will read (English; the Portuguese is its translation), for the author's approval (OD-3):

> On Case A, a client project on a low-code platform, the project manager followed the work on an Azure DevOps kanban board that a script filled from the queue, one way: `[ ]` went to To Do, `[>]` to Doing, `[x]` to Done.
> Each mark changed when a command ended.
> So a delivery stayed in To Do for as long as the author and the agent talked its page through, and reached Doing only once `/propose` had written it; and a card in Doing could be a page nobody was building yet.
> Lines blocked on the client's answers had no mark of their own: five of them sat in Doing and read as work nobody had started.
> The project added a fourth mark by hand, `[?]`, for a line waiting on a person.

Then, in the same section: two errors, Doing came late and waiting looked idle; focus-kit 2026.10.05 answers both. No person, project, script or date of Case A appears.

Other chapters (both editions):

* 13: the opening drops "which command changes it"; §The marks keeps one line per mark, six, with its meaning, and sends to chapter 16 for who sets it and when; the key point follows.
* 14: /propose marks `[~]` when it starts and `[>]` when the page is written, or `[?]` when the scope waits; on a `[?]` line it says what it waits on and goes on only when the person says so.
* 15: /apply marks `[*]` when it starts, `[x]` at the end, `[?]` when it stops, and clears an `after` that names only `[x]` lines; "done" keeps the line `[x]`.
* 18, the governor: §The governor decides per project becomes the story of a mark that moved from a project to the kit: Case A's error earned it; the error was not Case A's alone, so the kit took it in 2026.10.05 and this book follows the kit (ADR-0018). The book does not claim it found waiting lines of its own. The key point becomes "an error proven on one project can change the kit"; the footnote cites ADR-0018.
* 19, the assistant: pending is every line not `[x]`; the queue list shows six marks; the assistant answers "what is blocked, and on what?" from the `[?]` lines and their reasons.
* 22, team tools: §Boards maps six marks; §A mark for waiting says the mark became the kit's (chapter 16) and keeps question deliveries as Case A's customization; "the queue on the main branch is always true" says it holds what has landed; key point follows.

**Out of scope.**

* Chapter 21 (worktrees, formerly 20): its rule for a queue conflict, keep both marks, holds with six.
* Question deliveries: still Case A's customization, not the kit's.
* A board mirror for this book: it has no team board.
* Kit changes other than the marks that the reinstall brings (such as a slot docs/05 lacks): /apply lists them on the page; each one that needs a decision becomes a `[ ]` line in M10.
* `work/done/` pages and old ADRs: history, not renumbered.

**Done when.**

* [x] Both editions of chapter 16 written; opens with its value; no filler and nothing useful cut; every number sourced.
* [x] Chapters 13, 14, 15, 18, 19, 22 edited in both editions as above; no chapter teaches three marks or calls `[?]` Case A's alone.
* [x] Renumbering done; the list of every "chapter N" / "capítulo N" (16 to 25) taken before it, written on this page, each mention checked after it.
* [x] docs/00, 01, 03, 05, 06, AGENTS.md, ADR-0013 amendment, ADR-0017 amendment, ADR-0018 as the Contract says.
* [x] Commands installed from SETUP.md 2026.10.05 for every host; the propose and apply files name `[~]` and `[*]`.
* [x] The author approved the Case A passage (OD-3); `make scan` green.
* [x] `make verify` green; `make book`; both PDF paths given to the author.

**What happened.**

* Precondition held: focus-kit's `SETUP.md` says `Version: 2026.10.05`, committed in the kit's repository as `feat: the queue shows work while it happens; [?] marks what waits`.
* Kit installed from that `SETUP.md` for every host: the four `SKILL.md` and two `references/documents.md` in `.claude/skills/`, `.agents/skills/` and `.windsurf/skills/` changed; the Codex, Copilot, Cursor, Gemini and Antigravity files were already byte for byte the same. The propose and apply files name `[~]` and `[*]`.
* Kit changes the reinstall brought besides the marks: the `context/` paragraph in `references/documents.md` (this repo's docs already describe `context/` since its own delivery); the FOCUS link now points at chapter 7 of this book's site; the milestone review and "no review of a review" text, which docs/05 already had. One needs a decision: the kit's docs/05 §5 has a **Context** slot this docs/05 lacks. The author chose to queue it: `context-slot`, a `[ ]` line in M10.
* The author approved the Case A passage as written on this page (OD-3), in this session; chapter 16 uses it verbatim and its Portuguese translation.
* Renumbering: chapters 16 to 25 moved to 17 to 26 with `git mv`, both editions, H1 included; mentions, links and H1s bumped by one script in `book/`, docs/00, docs/03 and docs/04, never in `work/`, `docs/adr/` or docs/06. docs/00's Contents, which has bare numbers, by hand. Every one of the 97 entries below was checked after the move at its new number, and `make verify` (strict build, link check) passed right after it.
* Divergence: chapter 18's footnote cites ADR-0018 by file name and links the repository's `docs/adr/` folder, not the file, because the file is not on GitHub until the author pushes and the link check fails on a 404. A later delivery may point it at the file.
* Decisions taken without an ADR: the three-column fold puts `[~]`, `[>]` and `[*]` in Doing and leaves a `[?]` card in the column it was in, tagged blocked, the same in chapters 16 and 22; the kit's suffix `· blocked:` stays in English in the Portuguese edition, said once where it first appears; the kanban source is Toyota's own history (kanban at every plant in 1963), with Azure Boards for the software board. The six-column board is the mark table, not a drawing, so the chapter brings no new kind of content and no screenshot proof.
* Proof: `make verify` green, `make scan` green, `make book` built both PDFs and EPUBs; chapter 16 checked in the English PDF's text (contents page 111, the table, the queue and the board in place, every block within 74 columns).

**Mentions of chapters 16 to 25 before the renumbering** (file, line, mention; links and H1s moved with them):

* `book/en/00-product-people-process.md`: 41 chapter 25; 47 chapter 17; 51 chapter 18; 58 chapter 18
* `book/en/04-simplicity.md`: 128 Chapter 17
* `book/en/09-birth-of-focus-kit.md`: 43 chapter 17; 68 chapter 17
* `book/en/10-the-documents.md`: 56 Chapters 19 and 20
* `book/en/12-starting-a-project.md`: 132 chapter 18
* `book/en/13-queue-and-milestones.md`: 38 chapter 19; 77 chapter 16; 94 Chapter 18, chapter 21
* `book/en/14-propose.md`: 119 chapter 22
* `book/en/15-apply.md`: 100 chapter 19
* `book/en/16-closing-a-milestone.md`: 1 H1; 19 chapter 21
* `book/en/17-the-governor.md`: 1 H1
* `book/en/18-project-as-assistant.md`: 1 H1; 21 chapter 19
* `book/en/19-git-essentials.md`: 1 H1; 72 Chapter 21; 150 chapter 20; 194 chapter 20, chapter 21
* `book/en/20-worktrees.md`: 1 H1; 13 chapter 19; 144 chapter 19
* `book/en/21-team-tools.md`: 1 H1; 10 chapter 19; 71 chapter 17
* `book/en/22-beyond-software.md`: 1 H1; 59 chapter 21
* `book/en/23-cost-and-where.md`: 1 H1
* `book/en/24-adoption.md`: 1 H1; 21 chapter 23; 24 chapter 17; 63 chapter 20; 66 chapter 16; 67 chapter 18; 78 chapter 16; 80 chapter 23; 100 chapter 22
* `book/en/25-asking-for-more.md`: 1 H1; 9 chapter 18; 105 chapter 23; 136 chapter 23
* `book/pt/00-product-people-process.md`: 41 capítulo 25; 47 capítulo 17; 51 capítulo 18; 58 capítulo 18
* `book/pt/04-simplicity.md`: 129 capítulo 17
* `book/pt/09-birth-of-focus-kit.md`: 43 capítulo 17; 68 capítulo 17
* `book/pt/10-the-documents.md`: 56 capítulos 19 e 20
* `book/pt/12-starting-a-project.md`: 132 capítulo 18
* `book/pt/13-queue-and-milestones.md`: 38 capítulo 19; 77 capítulo 16; 94 capítulo 18, capítulo 21
* `book/pt/14-propose.md`: 119 capítulo 22
* `book/pt/15-apply.md`: 100 capítulo 19
* `book/pt/16-closing-a-milestone.md`: 1 H1; 19 capítulo 21
* `book/pt/17-the-governor.md`: 1 H1
* `book/pt/18-project-as-assistant.md`: 1 H1; 21 capítulo 19
* `book/pt/19-git-essentials.md`: 1 H1; 72 capítulo 21; 150 capítulo 20; 194 capítulo 20, capítulo 21
* `book/pt/20-worktrees.md`: 1 H1; 13 capítulo 19; 144 capítulo 19
* `book/pt/21-team-tools.md`: 1 H1; 10 capítulo 19; 71 capítulo 17
* `book/pt/22-beyond-software.md`: 1 H1; 59 capítulo 21
* `book/pt/23-cost-and-where.md`: 1 H1
* `book/pt/24-adoption.md`: 1 H1; 21 capítulo 23; 24 capítulo 17; 63 capítulo 20; 66 capítulo 16; 67 capítulo 18; 78 capítulo 16; 80 capítulo 23; 100 capítulo 22
* `book/pt/25-asking-for-more.md`: 1 H1; 9 capítulo 18; 105 capítulo 23; 136 capítulo 23
* `docs/03-Domain.md`: 39 chapter 25; 40 chapter 25; 44 chapter 25; 116 chapter 25
* `docs/04-Conventions.md`: 26 chapter 23; 35 chapter 24; 36 chapter 18
