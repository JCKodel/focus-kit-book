# m15-review

**Objective.** The author knows, clause by clause, whether M15's paragraph holds in the hands of a reader of the book, in both editions, and each clause that fails is a `[ ]` line in M15 under this review.

**Decided from the documents.**
1. The person tests alone; the agent prepares the clause table, the PDFs and the page numbers, records the answers and writes the lines (docs/05 §8; `m13-review` decision 1).
2. The review also reads the code as docs/05 §8 says after `kit-2026-10-16-2`: this repository's code is its scripts, and the milestone changed none, so the Milestone review slot's deep review runs against the commit that closed M14 and is expected to report nothing on `scripts/`; a finding there is a line like the others (docs/05 §5 Milestone review; §8 as M14 leaves it).
3. The test of "a reader reaches the method in five chapters" is the contents page of each PDF and the chapter the method starts in; the test of "said once" is the greps of `method-said-once` and `one-gain-section` plus the author's reading; the test of the quick guide is the author following its two columns on paper, with no repository, and finding each pointer's chapter (docs/05 §8, a milestone of chapters is tested by the author reading).
4. Each finding becomes one `[ ]` line under this review, saying what will be true, not how; no M15.1 (docs/05 §8; `m13-review` decision 4).

**Behaviour.**

* The author receives both PDFs (`make book`), the page where each passage below starts in each PDF, the contents page of each, and the clause table, and tests each clause in English and then in Portuguese.
* For each clause the author answers `C<n>: holds` or `C<n>: fails, <what the reader does not get>`; a clause that fails is a finding.
* The author launches the Milestone review slot's command against the commit that closed M14, as docs/05 §8 says, and names each confirmed finding; the agent writes each as a line.
* Each finding becomes one `[ ]` line in M15 under `m15-review`, shown to the author before staging; the author may reword it.
* An answer missing for some clauses: the page records the answers given, the line waits as `[?]` with `· resume: apply · blocked: <clauses> not answered`, and nothing is staged (docs/05 §4, §6).
* No file under `book/` and no document but docs/06 and this page is edited by this delivery.

**Contract.**

The clause table, what the author tests (M15's paragraph, quoted: "When this milestone closes, a reader reaches the method in five chapters instead of nine, every rule of the book is said once in the chapter that owns it with one source per point and one gain section, a reader sees what a five-line delivery costs before being asked to accept one, chapters 20 to 26 keep only what no manual gives, and a chapter after chapter 12 walks a reader from zero to the first delivery on a new project and on an existing one, step by step, with no repository."):

| | Clause | Answered by | Passage | How the author tests it |
|---|---|---|---|---|
| C1 | a reader reaches the method in five chapters instead of nine | `prologue-and-why`, `ch3-spec-cut`, `simplicity-and-results`, `focus-and-slices`, `ch8-testing-trim`, `renumber-chapters` | the contents page of each PDF; the prologue to the chapter before the birth of focus-kit | Does the contents page show five chapters before the method's first chapter? Does each of the five still open with what the reader can do after it, and does the author miss nothing the old nine taught? |
| C2 | every rule of the book is said once in the chapter that owns it, with one source per point | `method-said-once`, `ch20-21-git-cut`, `ch22-26-team-cut`, the five base lines | the six marks (chapter 16 only); the lint story (chapter 18); Case A's rate (chapter 19); "reads as right even when wrong" (chapter 10); chapter 15 §What `/apply` does; chapter 26 §Why the first answer feels final; chapter 5's successor on exceptions; chapter 2 §More context, less accuracy | Reading each passage, does the author find it in one chapter and a pointer elsewhere? Does any point still carry more than one study for the same claim? |
| C3 | one gain section | `one-gain-section` | every chapter's last two sections; the prologue's gain | Does every chapter end with one gain and key points that do not repeat it? Is "no baseline" said only in the prologue? |
| C4 | a reader sees what a five-line delivery costs before being asked to accept one | `small-delivery-example` | chapter 13 §Changing the queue | Can the author, as a reader, say what `due-date-format` cost and what an edit on the spot would have skipped, from the chapter alone? |
| C5 | chapters 20 to 26 keep only what no manual gives | `ch20-21-git-cut`, `ch22-26-team-cut` | chapter 20 §One delivery, one step to undo and §Commits and the history; chapter 21 §What a worktree is and when it pays and §The life of a worktree; chapter 24 §How a team decides; chapter 26 in its new order | Does chapter 20 reach its rule in its second section? Does any passage still teach what *Pro Git* or a vendor's documentation teaches, with no decision of the kit's attached? Is the protocol next to the card's story? |
| C6 | a chapter after chapter 12 walks a reader from zero to the first delivery, new and existing, step by step, with no repository | `quick-guide`, `renumber-chapters` | the quick guide chapter, both columns | Following each column on paper, does the author reach a first commit with no step missing and no repository opened? Does each pointer land on the chapter that teaches the step? |

Passages are named by section; /apply gives the PDF pages from `make book`, since the chapter numbers and lines change inside M15.

The findings' lines, when there are any, in docs/06 under M15 after this line, each `[ ] <slug>  <what will be true>; both editions`.

**Out of scope.**

* A second review of a finding's fix (docs/05 §8).
* Fixing anything in this delivery.
* M14's clauses: `m14-review`.

**Done when.**

* [ ] Both PDFs built; the clause table with PDF pages given to the author; the deep review launched against the commit that closed M14 and its confirmed findings recorded.
* [ ] Every clause answered and recorded on this page; each finding a `[ ]` line under this review, in the author's words.
* [ ] `make verify` green.
* [ ] Page in `work/done/`, line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Decisions in the review.**

* None: the table follows M15's paragraph and docs/05 §8; the author's answers are the review.
