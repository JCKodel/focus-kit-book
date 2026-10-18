# batch-propose

**Objective.** After chapter 19 a reader whose proposes feel slow can run several `/propose` at once, each told to take its own recommendation where it would ask, read on every page the questions it answered alone before the first `/apply`, keep a question only someone else can answer waiting, and say why applies stay parallel only on free lines whose files do not meet and why every commit stays theirs; both editions.

**Decided without the author.**

1. *Home: chapter 19 alone.* The queue line and M16's paragraph name chapter 19 (docs/06); the new section points back to chapter 22 once, and chapter 22 is unchanged. Chapter 12 is not changed either: its question "Do you disagree with a choice the agent made on its own?" already covers what a batch adds to the reading, and running things at once is chapter 19's (docs/04 "Chapter pointers").
2. *Where in chapter 19.* A new section, `## Proposing in a batch` (pt `## Propor em lote`), right before `## When parallel stops paying`, after the worktree and conflict sections, so it holds for one folder and for worktrees alike; the **You.** check of §When parallel stops paying gains one clause pointing back to it, since a batch moves your reading and does not shorten it (docs/04 "Say it where the doubt is born"). The rest of §When parallel stops paying, recently edited by `ch19-when-worktrees-pay`, is unchanged.
3. *Start from the reader's problem.* The section opens on proposes that feel slow and says where that time goes: the person deciding, which chapter 22 shows a token count does not see ("It pays less", the hours of a person). The premise is never that the kit is the problem: what feels slow is the reading and the deciding, and that is what the method keeps (docs/04 "Teach, do not report"; the draft's framing).
4. *What a batch is, as the kit is today.* One session per line, each running `/propose <slug>` and told, in the conversation, to take its recommendation wherever it would ask. The kit's `/propose` already asks with its recommendation first and writes on the page the decisions it took, naming their source (chapter 12), and docs/05 §3 asks that choices made on the person's behalf be explicit; the batch only answers its questions in advance. No batch command, flag or kit rule is invented (docs/04 "The kit as it is").
5. *The list on each page.* Each page lists the questions it answered alone: the question, the answer chosen and why, the document that left it open. The chapter teaches what the list says, not a heading the kit fixes, since docs/05 §3 names none; the example shows one, written for the chapter (docs/04 "Evidence"), and the sentence after it says what to see: the question, the answer and its reason on each item, and that the heading is the project's to name, since docs/05 §3 fixes the page's sections and not this one (docs/04 "Teach, do not only show").
6. *The example.* A short page excerpt on the lending library, the line `overdue-list` chapter 19 already uses (pt `lista-de-atrasos`), with two decisions, said in the text to be written for the chapter; within 74 columns (docs/04 "Width of a block", "Context before an excerpt", "Teach, do not only show").
7. *Questions the person cannot answer.* The recommendation covers only questions the documents leave open and the person running the batch could answer; one that belongs to someone else, a client or the library's director, is never answered on the recommendation: the page goes as far as it can and the line waits as `[?]` with `· resume: propose` (the kit's file for `/propose`; docs/05 §4). The chapter reuses chapter 14's `due-reminder` and its `· blocked: what provider?`, and points to chapter 23's question delivery once; no Case A passage is added.
8. *Pages written at once do not read each other.* `/propose` reads the deliveries in flight in `work/` when it starts (chapter 12), so a page written at the same time is not among them: two pages may settle the same question two ways, or each ask for the same new term in docs/03. You find it by reading the pages side by side, and correct one in its conversation. Another line's mark changing is not a conflict (docs/05 §4, chapter 19); the lines of one batch sit side by side in the queue, so their marks share a hunk, and the check before each commit is the one chapter 19 already teaches, `git diff --cached docs/06-Queue.md` showing only that line.
9. *Applies.* No new rule: applies run at once only on free lines whose files do not meet, and each commit is the person's, one delivery at a time, as chapter 19 teaches (docs/05 §§4, 6).
10. *Agent commits.* Said once, as leaving the method, with what it costs, never taught as a technique (the draft's Out of scope): a commit no longer says a person read the change (chapter 13); in one folder an agent's commit takes what another session staged, or with paths the shared docs/06 whole (chapter 19's trap); reading many committed changes after the fact is the condition of automation bias (chapters 13 and 24); and a wrong delivery that later ones built on reverts with a conflict wherever they changed its lines (chapter 18). The race on git's index lock is left out: it needs a source for a point the section does not need.
11. *Subagents.* Not mentioned. The chapter already opens one session per folder and per command; docs/05 §7 and `ch16-review-agents` admit only the reviews' readers and checker, so a sentence on one session launching an agent per page would either contradict chapter 16 or teach what the kit does not define. The cost of N sessions each reading the documents is the cost chapter 22 already gives one session, so no cost passage either.
12. *Evidence.* This repository's M4.2 run, 14 fix lines proposed and applied in a batch on the recommended answers, is not cited: its applies were committed by the driver, which this section teaches as leaving the method; its review's four findings were rejected to close the milestone, not judged false (work/done/m4.2-review.md); its record is interleaved with the guided project, which no chapter cites (docs/05 §5); and citing it would narrate a run (ADR-0017). The section's claims rest on the kit's own rules and on sources chapters 12, 13, 18, 19, 22 and 24 already give; no source note is added (docs/04 "Source notes").
13. *The gain.* `## What the team gains` keeps its three sentences and its one pair of numbers, and gains one sentence with no number: the agents write the pages while you are away, and each page brings the decisions it took alone listed for your one reading (docs/04 "One gain", "A gain per chapter").
14. *Opening and key points.* The opening gains a third sentence, at most three (docs/04 "Chapter shape"). Key point 5 gains the batch; still five key points (docs/04 "One gain"; `ch16-review-agents` decision 11).
15. *Docs/03.* No new row: "batch" is a plain word for running `/propose` several times, not a concept of the kit. The Portuguese words are fixed on the Contract, one rendering each (docs/04 "Languages").
16. *Trunk, nothing staged by this definition.* docs/05 §5 Git; the driver session sets the marks in docs/06. Chapter 15's files, docs/03, `work/ch07-11-23-review-words.md` and `work/ch16-review-agents.md`, changed in the tree by other sessions, are not this page's (docs/05 §4).

**Behaviour.**

* The opening keeps its two sentences unchanged and gains a third: the reader can also run several `/propose` at once on the agent's recommended answers, read on each page what it decided without them before any `/apply`, and say why every commit stays theirs.
* Reading §Proposing in a batch, a reader can explain:
  * where the time of a slow propose goes: the person deciding, pointing back to chapter 22 once;
  * how to run a batch: one session per line, each `/propose <slug>`, each told to take its own recommendation where it would ask;
  * what each page then lists: every question it answered alone, with the answer chosen, why, and the document that left it open, shown in the example of decision 6, said to be written for the chapter;
  * that the batch moves the decisions to the reading and removes none: every page is read and corrected in its own conversation before the first `/apply`;
  * that a question only someone else can answer waits as `[?]` with `· resume: propose`, with chapter 14's `due-reminder`, and that a question delivery (chapter 23) asks it;
  * that pages written at once do not read each other, so two may settle one question two ways or ask for the same term, found by reading them side by side; and that their neighbouring marks are no conflict, checked with `git diff --cached docs/06-Queue.md` before each commit;
  * that applies stay parallel only on free lines whose files do not meet, and that each commit stays theirs, one delivery at a time;
  * what letting agents commit a batch of applies costs, the four points of decision 10, said as leaving the method.
* §When parallel stops paying: the **You.** check gains one clause pointing to §Proposing in a batch; the other checks and the paragraph on this book stay as they are.
* §What the team gains: its three sentences stay, and the sentence of decision 13 is added.
* Key point 5 gains the batch, the list on each page and the commit that stays the person's; the other four key points are unchanged; still five.
* Edge: a page that answered no question alone says so, or carries no list; the chapter does not ask for an empty one.
* Edge: nothing in either edition names a kit version, a changelog, "since" or "no longer", a host command for batches, a subagent, a model or a commit hash (decisions 4, 11).
* Edge: no run is narrated, M4.2 included: no brief, transcript, diff of a run, `git status` or hash (ADR-0017, decision 12).
* Edge: a pointer back stays only where the sentence leans on that chapter's detail: chapter 22 for where the time goes, chapter 13 for "a commit says a person read the change", chapter 18 for the revert's conflict; chapters 14 and 18 are already linked in chapter 19, so their mentions here name the thing in plain words with no new link, and the other chapters are named without a link where the sentence stands on its own (docs/04 "Chapter pointers").
* Edge: no number is added; `[^parallel-run]` and its pair stay as they are.
* Edge: docs/04's prose rules hold, `not-but` included, in the sentences on what a batch does not remove.
* Failure: a passage implying the kit has a batch command or rule, that a batch removes or shortens the person's review, that a recommendation may answer a client's question, or that an agent's commit is a step of the method contradicts docs/05 §§2, 3, 6 and this page.
* Failure: a passage framing the kit as the problem that a batch solves.
* Failure: one edition changed and not the other.

**Contract.**

* **Files.** `book/en/19-worktrees.md` and `book/pt/19-worktrees.md`, same changes; no other file.
* **Sections touched** (found by text): the opening's second sentence, which stays, and a third after it ("You can also say when it still pays to give each delivery a worktree" / "Você também consegue dizer quando ainda compensa dar a cada entrega um worktree"); a new `## Proposing in a batch` / `## Propor em lote` before `## When parallel stops paying` / `## Quando o paralelo deixa de compensar`; the **You.** check ("The agents work in parallel; your review does not." / "Os agentes trabalham em paralelo; a sua revisão não."); §What the team gains / §O que o time ganha; key point 5 ("Parallel pays while" / its pt).
* **The example**, written for the chapter, en (pt translated, `lista-de-atrasos`, heading `**Decidido sem você.**`), at most 74 columns:

  ```
  **Decided without you.**

  1. Order of the list: most days overdue first. docs/00 does not
     say; recommended, since the librarian calls the oldest loan
     first.
  2. A copy returned today leaves the list at once. docs/00 does not
     say; recommended, so the list never shows a book already back.
  ```

* **Terms of docs/03.** `page`, `free line`, `question delivery`, `trunk`, `conflict`, `automation bias`, used as defined. No new row.
* **Portuguese words.** batch: `lote`; in a batch: `em lote`; recommended answer: `resposta recomendada`; recommendation: `recomendação`; page: `página`; free line: `linha livre`; question delivery: `entrega de pergunta`; automation bias: `viés de automação`; hunk: `hunk`, as chapter 19 keeps it.
* **Sources.** None added; the section leans on chapters 12, 13, 14, 18, 22, 23 and 24 and on this chapter's `[^git-commit]` passage, with links only as the Behaviour edge on pointers says, at most one per target in the chapter (docs/04 "Chapter pointers").
* **Cases.** The lending library only; no Case A, Case B or Ninjobs passage added; M4.2 not cited (decision 12).
* **Numbers.** None added.
* **docs/03**, asked of the driver session: nothing.
* **docs/06**, asked of the driver session: this line's marks only. No new line, no suffix change.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* A batch command, flag or rule in the kit: the book teaches the kit as it is (docs/04).
* Agent commits as a technique: said only as leaving the method (decision 10).
* Subagents that run `/propose`, and how a host runs several sessions: the agents an agent launches are chapter 16's (`ch16-review-agents`), and the host's own way to open sessions is the host's.
* Chapter 12's reading questions and chapter 22's cost sections: unchanged (decision 1).
* The rest of §When parallel stops paying: `ch19-when-worktrees-pay`, done.
* A cost or a time measured for a batch: no record of this book's measures one, and M4.2 does not (decision 12).

**Done when.**

* [x] Both editions written, same sections, parity green; the new heading in both.
* [x] The chapter opens with its value, at most three sentences; no filler, nothing useful cut; still five key points.
* [x] Every Behaviour line reads as written in both editions.
* [x] The example block matches the Contract, says it is written for the chapter, and stays within 74 columns (verify's `width`).
* [x] `grep -n -i -E "2026\.[0-9]|changelog|no longer|subagent|opus|fable|sonnet|m4\.2" book/en/19-worktrees.md` finds nothing; `grep -n -i -E "2026\.[0-9]|changelog|não mais|subagente|opus|fable|sonnet|m4\.2" book/pt/19-worktrees.md` finds nothing.
* [x] The Portuguese uses the Contract's words and no synonym.
* [x] No number added; every number sourced.
* [x] No em dash; `make verify` green, disclosure scan included.
* [x] The Delivery review ran on this delivery's paths as docs/05 §5 says, and the page records it.
* [x] The author's approval of an anonymized passage: inapplicable, no Case A or Case B passage added.
* [x] `make book` builds, and the delivery ends giving the author both PDF paths to review.

**What happened.**

* Built as defined: the opening's third sentence, `## Proposing in a batch` / `## Propor em lote` before §When parallel stops paying, the **You.** clause, one sentence in §What the team gains with no number, and key point 5 widened; still five key points. No divergence from the page, nothing dropped.
* Decided by the agent, no author present (rule of this batch: the recommended option): the **You.** clause says a batch "moves that reading to one sitting and does not shorten it" and points back with "a batch of proposes" in plain words, not a link to the section; the gain sentence opens "Proposes in a batch carry the parallel into definition"; the pt heading of the example is `**Decidido sem você.**` and the librarian "cobra" the oldest loan.
* Links added: chapter 22 and chapter 13, one each; chapters 12, 14, 18, 23 and 24 named in plain words.
* Proof: `make verify` green; `make book` builds; the Done when greps find nothing in either edition.
* Delivery review (docs/05 §5), a read-only agent on Opus over this delivery's staged and unstaged diff against this page and docs/04. One finding broke docs/04 ("Teach, do not only show"): "the trap above" pointed to §The trap: committing the markers, the section right above, instead of the trap of naming paths; fixed to "the trap of naming paths, earlier in this chapter" in both editions. Five suggestions, all on this delivery's own lines, taken: "one at a time" cut (no source says questions come one at a time); "the time is not the agent's" rephrased away from the not-but shape; the question delivery glossed where chapter 19 first names it; pt "uma sentada só" made "uma leitura só"; "the queue's chapter" made "chapter 14". Verify green again after the fixes. No finding left for the queue.

```commit
docs(batch-propose): teach proposing in a batch in chapter 19

- New section on running /propose in a batch on recommended answers
- Each page lists the questions it answered alone; example written
- Others' questions wait as [?]; pages in one batch do not read each other
- Applies stay on free lines; agent commits named as leaving the method
- Opening, You check, gain and key point 5 widened; both editions

work/done/batch-propose.md
```
