# m12-review

**Objective.** The author knows, clause by clause, whether M12's paragraph holds in the hands of a reader of the book and in this repository, in both editions; every clause that fails is a `[ ]` line in M12 under this review.

**Decided from the documents.**
1. The person tests alone; no fresh session reads the chapters as a reader and no agent proposes findings. The agent prepares, records and writes the lines (docs/05 §8; `m9-review`, `m10-review` and `m11-review` did the same).
2. The paragraph's first clause has two halves: the book teaches the kit, which the chapters answer, and the repository runs on it, which `kit-2026-10-13` answers. The second is tested by opening this repository's documents, not the PDF (docs/05 §8 asks for a hand test of each clause; only a chapter clause is read in the PDF).
3. `ch10-commit-format` and the "where are we?" half of `ch18-19-only-apply` answer no clause of the paragraph: they followed the kit where chapters 10, 12 and 19 had fallen behind it. They are not in the table; a defect the author finds there becomes a line as any defect outside the table does.

**Behaviour.**

* The author receives both PDFs (`make book`), the page where each passage below starts in each PDF, and the clause table, and tests each clause by reading the passages it names, in English and then in Portuguese; C1's second half by opening the files it names.
* For each clause the author answers, in the conversation, `C<n>: holds` or `C<n>: fails, <what the reader does not get>`; a clause that fails in the author's hands is a finding, with nothing to confirm or reject afterwards.
* Each finding becomes one `[ ]` line in M12, under `m12-review`, saying what will be true, never how to fix it; written by the agent from the author's words, shown to the author before it is staged. No M12.1.
* A defect the author finds outside the clause table becomes a line the same way, when the author asks for it.
* An answer missing for some clauses: the page records the answers given, the line waits as `[?]` with `· resume: apply · blocked: <clauses> not answered`, and nothing is staged (docs/05 §4, §6).
* No finding: M12 closes with this delivery; the page says so.
* No file under `book/` and no document but docs/06 and this page is edited by this delivery.

**Contract.**

The clause table, what the author tests (M12's paragraph, quoted: "When this milestone closes, the book teaches focus-kit 2026.10.13 and the repository runs on it: two sessions in one working tree on free lines, the queue's order as its priority and `· after <slug>` as an order, not a block, `/propose` deciding what the documents answer, Behaviour drafted with concrete inputs and failure cases, the commit message in a `commit` block on the page, code changed only inside `/apply`, `/apply` staging only its delivery and naming the next steps, manuals in `docs/manuals/`, and an update that reports migrations instead of rewriting the project's documents; the kit's changelog, paraphrased, is the evidence."):

| | Clause | Answered by | Passage (en lines; pt where they differ) | How the author tests it |
|---|---|---|---|---|
| C1 | the book teaches focus-kit 2026.10.13 and the repository runs on it | `kit-2026-10-13`; every chapter line of M12 | 16, opening (lines 15 and 16); 11 §What an update reports (41 to 76). Repository: docs/05 §2, §3, §4, §5 Manuals and Git, §6; `AGENTS.md`; `docs/manuals/`; docs/06's header | Does the book name the version it follows, once, where the process document is described? Does each rule below stand in this repository's docs/05 and `AGENTS.md` as the chapter teaches it, and can a person follow each manual alone? |
| C2 | two sessions in one working tree on free lines | `ch21-one-tree` | 21 §The problem (6 to 19), §Two sessions in one folder (20 to 55), §What is and is not a conflict there (56 to 73), §When a worktree still pays (74 to 87), §When parallel stops paying (211 to 234); 20 §Choosing (189 to 201); 10 §The two choices (line 56) | Can a reader run two sessions in one folder: what each marks and stages, how the person commits one delivery at a time, the three things that are not a conflict and the two that are, and when a worktree still pays? Do chapters 10 and 20 choose git the same way? |
| C3 | the queue's order as its priority and `· after <slug>` as an order, not a block | `ch13-16-queue-order` | 13 §The line (12 to 27; pt 12 to 29), §Milestone 1 (48 to 65; pt 50 to 67), §Size and order (74 to 88; pt 76 to 90); 16 §The next line, and which run together (56 to 70; pt 57 to 71), §Waiting (71 to 97; pt 72 to 98) | Can a reader say which line is next, when a line with `· after` is free, why `· after` is not `[?]` and `· blocked: after` is, what the resume suffix says, and which lines can run at the same time? |
| C4 | `/propose` deciding what the documents answer | `ch14-propose-decides` | 14, opening; §What `/propose` does (20 to 35); the example page (51 to 100; pt 51 to 107) and the paragraph under it; §Read the page before `/apply` (101 to 126; pt 108 to 133) | Can a reader say what `/propose` decides alone, how the page shows the source of each decision, when it still asks, and where they correct a decision they disagree with? |
| C5 | Behaviour drafted with concrete inputs and failure cases | `ch14-propose-decides` | 14 §The page (36 to 50) and the example's Behaviour; 15 §`lend-book`, built (line 69's list of tests) | Can a reader write one Behaviour line with a concrete input and the result the user sees, name the cases that must fail and the edge in the example, and say who drafts and who corrects? |
| C6 | the commit message in a `commit` block on the page | `ch15-apply-ends` | 15 §When the work cannot go on (37 to 44), §Green is not done (52 to 68), §`lend-book`, built (69 to 105), §The commit is the human review (135 to 155), §The message (156 to 177) | Can a reader find the message on the page and in the conversation, say what a partial message says when blocked, and copy it into the commit? |
| C7 | code changed only inside `/apply` | `ch18-19-only-apply` | 13 opening; §Changing the queue (95 to 118; pt 97 to 120); Key points; 19 §The manager's session (110 to 135), the paragraph on changes | Asked for a small code fix in an ordinary session, does a reader know the agent writes a `[ ]` line and stops, and why? |
| C8 | `/apply` staging only its delivery and naming the next steps | `ch15-apply-ends`; `ch11-update-migrations` | 15 §Green is not done (52 to 68), §Why it stops at the stage (106 to 111), §Review the staged change (112 to 134); 11 §How each host finds the commands (77 to 105) | Can a reader say what `/apply` stages and what it reports of someone else's index, and read its next steps: environments, review, commit, the next line's command as their host invokes it? |
| C9 | manuals in `docs/manuals/` | `ch10-12-manuals`; `kit-2026-10-13` for this repository | 10 §Manuals (69 to 80), §Where a new fact goes (91 to 121); 12 §`/brainstorm` what it writes (49 to 58), §`/analyze` (77 to 97), §Review before you commit (136 to 151); 15 §Green is not done | Can a reader say what a manual holds, who writes it (`/analyze`, `/apply`, not `/brainstorm`), and where a new procedure done by hand goes? |
| C10 | an update that reports migrations instead of rewriting the project's documents | `ch11-update-migrations` | 11 opening; §What the install never touches, and how to update (30 to 40); §What an update reports (41 to 76) | Can a reader say what an update writes and what it only reports, how a migration becomes a delivery, and where the changelog says what changed? |
| C11 | the kit's changelog, paraphrased, is the evidence | every chapter line of M12 | the "What the team gains" sections of 10, 11, 13, 14, 15, 16 and 21 | Does each gain name the changelog entry in plain words, with no note and no quote, and does it read as the error the rule removed? |

Line numbers are those of `book/<edition>/NN-*.md` at the start of this delivery; the PDF pages are given by /apply from `make book`.

The finding line, in docs/06 under M12:

```
[x] m12-review                the review of M12 as docs/05 §8 says
[ ] <slug>                    <what will be true>
```

docs/06: `m12-review` `[>]` now, `[*]` when /apply starts, `[x]` by /apply; its description stays.

docs/03, docs/05: no change.

**Out of scope.**

* Fixing any finding: each is its own line.
* Chapters other than 10, 11, 12, 13, 14, 15, 16, 19, 20 and 21: M12 changed only those, save one sentence of chapter 25 (line 63, "in one folder or in worktrees"), too small to test apart from C2.
* The rest of those chapters: a finding only if the author says a clause fails on it.
* `ch10-commit-format` and chapter 19's "where are we?": decision 3.
* An agent's reading as support: decision 1.

**Done when.**

* [x] `make book` run; both PDF paths given to the author with the clause table and the page where each passage starts in each edition.
* [x] C1 to C11 each answered by the author, recorded under What happened in the author's words.
* [x] Each failed clause a `[ ]` line in M12 under `m12-review`, approved by the author; or the page says there was none.
* [x] No file under `book/` changed.
* [x] `make verify` green, disclosure scan included.
* [x] Page in `work/done/`, `m12-review` `[x]`, staged, commit message suggested in a `commit` block.

**What happened.**

* `make book` run; the author got both PDFs, the clause table and the page where each passage starts in each edition (chapter 21's §Two sessions in one folder at p. 155 in English and p. 164 in Portuguese; chapter 16's §Waiting at p. 122 and p. 129; chapter 14's example page at p. 104 and p. 110; chapter 15's §The message at p. 116 and p. 122; chapter 11's §What an update reports at p. 81 and p. 86).
* The author's answer, in their words: "Tudo ok".
  * C1: holds. C2: holds. C3: holds. C4: holds. C5: holds. C6: holds. C7: holds. C8: holds. C9: holds. C10: holds. C11: holds.
* No clause failed and the author named no defect outside the clause table: no finding, no line added. M12 closes with this delivery; no M12.1.
* Nothing diverged from the plan. No file under `book/` changed; no ADR, no manual, no document but docs/06 and this page.

```commit
docs(m12-review): review M12 clause by clause; no finding

- C1 to C11 tested by the author in both PDFs; all hold
- no finding, M12 closes with this delivery

work/done/m12-review.md
```
