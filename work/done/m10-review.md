# m10-review

**Objective.** The author knows, clause by clause, whether M10's paragraph holds in the hands of a reader of the book, in both editions, and of a person reading this repository's process; every clause that fails is a `[ ]` line in M10 under this review.

**Decided by the author.**
1. As in `m9-review`, and as docs/05 §8 says: the person tests alone; no fresh session reads the chapters as a reader and no agent proposes findings. The agent prepares, records and writes the lines.

**Behaviour.**

* The author receives both PDFs (`make book`), the page where each passage below starts in each PDF, and the clause table, and tests each clause by reading the passages it names, in English and then in Portuguese; C6 is tested in the repository, not in the PDF.
* For each clause the author answers, in the conversation, `C<n>: holds` or `C<n>: fails, <what the reader does not get>`; a clause that fails in the author's hands is a finding, with nothing to confirm or reject afterwards.
* Each finding becomes one `[ ]` line in M10, under `m10-review`, saying what will be true, never how to fix it; written by the agent from the author's words, shown to the author before it is staged. No M10.1.
* No finding: M10 closes with this delivery; the page says so.
* No file under `book/` and no document but docs/06 and this page is edited by this delivery.

**Contract.**

The clause table, what the author tests (M10's paragraph, quoted: "When this milestone closes, a reader knows the six marks of focus-kit 2026.10.05 (`[ ]`, `[~]`, `[>]`, `[*]`, `[x]`, `[?]`), why each is set at the moment the work changes and not when a command ends, the three cases of `[?]` and its two suffixes, and how a queue read as a kanban shows work while it happens; Case A's Azure Boards delay and its hand-made `[?]` are the evidence, and the book's own queue and process follow the kit."):

| | Clause | Answered by | Passage (en and pt) | How the author tests it |
|---|---|---|---|---|
| C1 | the six marks of focus-kit 2026.10.05 | queue-states | 16 §Six marks; 13 §The marks (lines 30 to 39) and its Key points | Without looking back: can you name the six marks, what each means and who sets it? Does any chapter you read still teach three marks? |
| C2 | each set at the moment the work changes, not when a command ends | queue-states | 16 §At the moment the work changes; 14 lines 24 to 26; 15 lines 21, 39 and 57 | Can you say when `[~]` and `[*]` are set and why that moment and not the end of the command, and where the mark is seen on trunk, on a branch or worktree, and on a board? Do chapters 14 and 15 say the same moments as 16? |
| C3 | the three cases of `[?]` and its two suffixes | queue-states | 16 §Waiting: `[?]` | Can you give the three cases with one example each, write both suffixes, and say who takes a line out of `[?]` and back to which mark? |
| C4 | a queue read as a kanban shows work while it happens | queue-states | 16 §The queue as a kanban board; 22 §Boards; 19 §What the agent already reads (lines 18 to 25) and §The questions the team asks (line 63) | Given a queue, can you draw its six-column board and fold it onto To Do, Doing, Done with `[?]` still visible, and answer "what is blocked, and on what?" from the queue alone? |
| C5 | Case A's Azure Boards delay and its hand-made `[?]` as the evidence | queue-states | 16 §The problem and §What the team gains; 18 §From one project to the kit; 22 lines 65 and 66 | Are the two errors (Doing came late, waiting looked idle) clear, does the gain follow from them, and does no passage read `[?]` as Case A's alone or claim this book found waiting lines of its own? |
| C6 | the book's own queue and process follow the kit | queue-states, context-slot | docs/06's header; docs/05 §2, §4 and §5 Context; `.claude/skills/propose` and `apply`; this line's own `[~]` | Against focus-kit's SETUP.md 2026.10.05: do docs/05 and docs/06's header say the same marks, setters and suffixes, does §5 have the kit's slots, and did this `/propose` mark `m10-review` `[~]` when it started? |

The finding line, in docs/06 under M10:

```
[x] m10-review               the review of M10 as docs/05 §8 says
[ ] <slug>                   <what will be true>
```

docs/06: `m10-review` `[>]` now, `[*]` when /apply starts, `[x]` by /apply; its description stays.

docs/03, docs/05: no change.

**Out of scope.**

* Fixing any finding: each is its own line.
* Chapters other than 13, 14, 15, 16, 18, 19 and 22: M10 changed only those, and the renumbering of 17 to 26 was checked by `queue-states`'s list and the link check.
* Chapter 18's footnote that links the ADR folder and not ADR-0018's file (recorded in `queue-states`): a known divergence, a finding only if the author says C5 fails on it.
* An agent's reading as support: decision 1.
* focus-kit itself: the kit is tested only as the reference C6 compares against.

**Done when.**

* [x] `make book` run; both PDF paths given to the author with the clause table and the page where each passage starts.
* [x] C1 to C6 each answered by the author, recorded under What happened in the author's words.
* [x] Each failed clause a `[ ]` line in M10 under `m10-review`, approved by the author; or the page says there was none.
* [x] No file under `book/` changed.
* [x] `make verify` green, disclosure scan included.
* [x] Page in `work/done/`, `m10-review` `[x]`, staged, commit message suggested.

**What happened.**

* `make book` run; the author got both PDFs, the clause table and the page where each passage starts in each edition (chapter 16 at p. 111 in English and p. 116 in Portuguese).
* The author's answers, in their words (given in Portuguese, rendered here): "All the Cs are fine, except C6, which I did not see (it is currently `[>]`)." Asked how C6 stands, given that `[~]` lived only during `/propose` and was never committed (the diff goes from `[ ]` straight to `[>]`, the end `/propose` is meant to leave), the author answered: "C6: holds".
  * C1: holds. C2: holds. C3: holds. C4: holds. C5: holds. C6: holds.
* No clause failed. The author found two defects of the PDF itself, outside the clause table: "The contents left an orphan line on the second page; the font must be reduced a little more so the contents fit on one page, and the chapter numbers in the contents are much larger than the page numbers"; and a rendering problem in the footnotes, a coloured block behind the note numbers ("I believe every footnote is like that").
* Diverged from the plan: the page foresaw findings only from failed clauses. The author chose to record both defects as `[ ]` lines in M10 under `m10-review`, shown to and approved by the author: `pdf-contents-one-page` and `pdf-footnote-numbers`. M10 closes when both are `[x]`; no M10.1.
* No file under `book/` changed; no ADR.
