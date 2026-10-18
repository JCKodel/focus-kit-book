# ch13-delivery-review

**Objective.** After chapter 13 a reader can say why an agent that checks its own work misses what it wrote, and how `/apply` closes that gap before it ends: after verify and the proof, it has its delivery's own changes, by their paths, reviewed by a context that did not write them (the host's own review when the agent can run it and keep it to those paths, else a read-only agent), fixes what breaks the page, docs/04 or the delivery's own lines and runs verify again, turns anything else into a `[ ]` line, and records the review on the page; both editions.

**Decided without the author.**

1. *Where the review goes in the chapter.* A new H3, `### The delivery review` (pt `### A revisão da entrega`), inside "What `/apply` does", after "Verify and the proof" and before "Green is not done", because the file of `/apply` orders it so: verify, proof, review, fix and verify again, then record (`.claude/skills/apply/SKILL.md`). Not a bullet of "Green is not done", which lists what is recorded and staged.
2. *Which reviewer the lending library example shows.* A read-only agent, the kit's fallback, since it claims no feature of any host; the general text gives the kit's order, the host's own review first (docs/05 §5's Delivery review slot as `SETUP.md` §3 writes it; changelog 2026.10.17).
3. *Whether to show this book's own slot (a read-only agent on Opus keeping the session's advisor).* No: model and advisor names belong to this repository's choice and to chapter 8 and 9's slot questions, owned by `ch08-09-review-slot`; the chapter teaches the slot's rule, not this project's answer (docs/04 "Context before an excerpt", AGENTS.md scope note of this batch).
4. *Whether to cite the kit's count of rework the milestone review found (21 lines, ten in one build file).* No: it is a measure taken to justify a kit change, which docs/04 "The kit as it is" forbids; the rule's reason is said in the present, as the error it prevents.
5. *What "its own lines" means in "fixes what breaks the page, docs/04 or its own lines".* The lines this delivery changed: a fault in what it wrote is fixed in the delivery that wrote it; a fault in code it did not touch, or a wish the page did not ask for, becomes a `[ ]` line, because the page is the scope (`.claude/skills/apply/SKILL.md`, docs/05 §1, chapter 13's "The page is the scope").
6. *A source for the problem.* Yes, one primary publication, scoped to what it shows: Huang et al., ICLR 2024, whose abstract says language models "struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction" (fetched 2026-10-17). The chapter does not claim it measured code review; the kit's answer adds the two things the writer's own re-read lacks: a context free of the writer's reasoning, and the page and docs/04 as the measure. The chapter holds without the note if /apply finds the URL or the wording changed (docs/04 "Evidence", "Source notes").
7. *Whether to reuse `[^claude-code-subagents]` for "read-only agent".* No: chapter 16 owns subagents and the governor's exception for the reviews' readers (`ch16-review-agents`); chapter 13 says in plain words what the read-only agent is and points to chapter 16 once.
8. *The slot set to none.* Said in one clause: a project whose Delivery review slot says none has no such review, and the person's commit stays the only review (`SETUP.md` §3's slot template, "or: none").
9. *Portuguese term for "read-only agent".* `agente somente leitura`, one rendering in the whole chapter; `revisão da entrega` is docs/03's term, kept distinct from the chapter's `revisão humana` and `Revise a mudança em stage` (docs/04 "Languages").
10. *The gain.* `## What the team gains` keeps its Ninjobs passage and gains one sentence with no number: a fault a delivery wrote is found and fixed in that delivery, by a reader that did not write it, before the person reads the diff (docs/04 "One gain", "A gain per chapter").
11. *Trunk, no branch, nothing staged by this definition.* docs/05 §5 Git; the driver session sets the marks in docs/06 (this batch's instructions).

**Behaviour.**

* The opening's first sentence lists, among what "done" means, a review by a context that did not write the change; the opening stays at three sentences.
* "The problem" gains two sentences: the chapter's own reasoning, that an agent that checks its own work rereads it with the reasoning that wrote it, so what it missed while writing it misses again; and the Huang et al. finding, the abstract's words quoted, with `[^huang-2024]` on the quoted words and not on the chapter's reasoning.
* "What it reads" names, among the slots `/apply` follows literally, how its changes are reviewed before it ends.
* Reading "The delivery review", a reader can explain:
  * when it runs: after verify is green and the proof is done, before the page records what happened;
  * who reviews: a context that did not write the change, inside the same `/apply` session, not a fresh session: the host's own review, as a skill the agent invokes or a command it runs, when it can be kept to the delivery's paths; else a read-only agent, one the session launches with its own context, which reads files and runs `git diff` but edits nothing; docs/05's Delivery review slot names which, and a slot that says none means no such review;
  * what it reads: the delivery's changes, by their paths, and of docs/06 only this line's hunk, against the page and docs/04; the host's review reads them its own way, kept to those paths, and a read-only agent reads their `git diff`; another session's files in the same folder are not this review's (chapter 19);
  * what happens to what it finds: a candidate that breaks the page, docs/04 or a line this delivery wrote is fixed in this session and verify runs again; anything else becomes a `[ ]` line in the queue, because the page is the scope; the reviewer fixes nothing itself;
  * why read-only: the session that built the change knows why it made each choice and makes the fix, so there is one writer;
  * what it is not: it does not replace the person's review and commit, it is one more check before the person reads the diff; and it reads one delivery while it is open, while the milestone review reads across deliveries (chapter 15).
* "Green is not done": the first bullet's record of what happened includes what the review found and what became of each candidate.
* "`lend-book`, built": after the screenshots, a read-only agent reads the diff of the delivery's paths against the page and docs/04, as an illustration written for the chapter and said so. It finds that the first draft of the repository call turns every database failure into `AlreadyLent`, against chapter 3's rule (catch at the boundary, translate the library's exception, let everything else pass), which the library's docs/04 holds: a fault in a line this delivery wrote that no test triggers, fixed to match the unique index's error alone, verify run again; the code the chapter's reader saw in chapters 3 and 4 is the fixed one. It finds that the refusal for a suspended member does not say until when: not on the page, so it becomes the line `suspension-end` (pt `fim-da-suspensao`), placed in the queue where it belongs, so `return-book` stays the next free line. The page records both. The suggested commit message is unchanged.
* "Review the staged change" gains one question, "What did the delivery review find, and was each candidate fixed or lined?", and one sentence in the chapter's pattern: if the page records no review and the slot names one, the delivery did not end as the kit says; ask for it.
* "What the team gains" gains one sentence, no number (decision 10).
* Key point 3 reads that done is the whole list, from the review by a context that did not write the change to the line marked `[x]`; still five key points.
* Edge: nothing in either edition names a kit version, cites the changelog or compares the kit with an earlier one.
* Edge: nothing names Opus, Fable, an advisor or `/code-review`.
* Edge: the passage on what the reviewer catches avoids the `not-but` prose rule (docs/04 §Prose rules), "not only ... but" included.
* Failure: a passage that says the reviewer edits files, runs in a fresh session, reads another session's files, or replaces the commit as the human review contradicts the kit's file of `/apply` and this page.

**Contract.**

* **Files.** `book/en/13-apply.md` and `book/pt/13-apply.md`, same changes; no other chapter.
* **Sections touched** (found by text): the opening; "The problem"; "What it reads"; new H3 "The delivery review" / "A revisão da entrega" between "Verify and the proof" and "Green is not done"; "Green is not done" first bullet; "`lend-book`, built" (pt "`emprestar-livro`, construída"), after the paragraph on the screenshots; "Review the staged change" list and one sentence after it; "What the team gains"; key point 3; the notes at the end of the file.
* **Terms of docs/03.** `delivery review` / `revisão da entrega` (row exists since `kit-2026-10-17`); `milestone review`, `slot`, `host` used as defined. No new term, no docs/03 change.
* **Sources.** One new note, the same key in both editions, cited at the same places:
  `[^huang-2024]: Jie Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet", 2024. <https://arxiv.org/abs/2310.01798>`
  The English quotes the abstract's words in `"*...*"`; the Portuguese gives only their translation. The kit's rule is named in plain words: the file of `/apply` and docs/05's Delivery review slot; no note points to focus-kit's repository (docs/04 "Source notes").
* **Cases.** No private case is added; the existing Ninjobs passages are unchanged.
* **Example names (pt).** `JaEmprestado`, `emprestar-livro`, `src/features/emprestimos/`, `fim-da-suspensao`; `git diff`, `git diff --cached` and `[ ]` stay as they are.
* **docs/06.** None from this page; the driver sets the marks.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* The milestone review by areas, its readers, paths read and checker: `ch15-review-by-areas`.
* Why the governor admits the reviews' readers as its one specialized subagent: `ch16-review-agents`.
* How a project answers the Delivery review slot in `/analyze` and `/brainstorm`, and chapter 8's update report: `ch08-09-review-slot`.
* Devin Desktop and `.agents/skills/`: `ch08-10-devin-desktop`.
* Batches of proposes and parallel applies: `batch-propose`.
* This repository's own slot wording and models: a project choice, not the kit's rule (decision 3).
* A number for the review's effect: forbidden by docs/04 "The kit as it is" (decision 4).

**Done when.**

* [x] Both editions written, same sections and the same note cited the same number of times (parity green).
* [x] The chapter opens with its value, still three sentences; no filler, nothing useful cut; still five key points.
* [x] Every Behaviour line above reads as written in both editions; the example is said to be written for the chapter.
* [x] `[^huang-2024]` opened and its quoted words checked against the abstract; no other new number.
* [x] `grep -n -i "2026\.\|changelog\|no longer\|opus\|fable\|advisor\|code-review" book/en/13-apply.md` finds only the existing "no longer say the truth" of "The problem"; the same grep with the Portuguese words (`não mais`, `changelog`, `opus`, `fable`, `advisor`, `code-review`) finds nothing in `book/pt/13-apply.md`, as it finds nothing today.
* [x] The Portuguese uses `revisão da entrega` and `agente somente leitura` and no synonym.
* [x] No em dash; `make verify` green, disclosure scan included.
* [x] The Delivery review ran on this delivery's paths as docs/05 §5 says, and the page records it.
* [x] `make book` builds, and the delivery ends giving the author both PDF paths to review.

**Proof.**

* Both editions changed in the sections the Contract names, found by their words: the opening (still three sentences), "The problem" (two sentences, the second quoting Huang et al. with `[^huang-2024]`), "What it reads", the new H3 "The delivery review" / "A revisão da entrega" between "Verify and the proof" and "Green is not done", the first bullet of "Green is not done", the lending example after the screenshots, "Review the staged change" (one question and one sentence), "What the team gains" (one sentence, no number) and key point 3; still five key points.
* `[^huang-2024]` opened at <https://arxiv.org/abs/2310.01798> on 2026-10-17: the title and the first author (Jie Huang) match, and the quoted words match the abstract word for word. Cited once per edition, on the quoted words.
* The page's grep finds in `book/en/13-apply.md` only the existing "no longer say the truth" and nothing in `book/pt/13-apply.md`; no em dash in either.
* `make verify` green: build, parity, em dash, prose, width, links and disclosure.
* `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences.**

* The review question reads "was each candidate fixed or turned into a `[ ]` line?" (pt "corrigido ou virou uma linha `[ ]`") in place of "fixed or lined", a word the reader has not met.
* The example says "the repository call chapters 3 and 4 describe is the fixed one" in place of "the code the chapter's reader saw in chapters 3 and 4": chapter 3 never shows `insertLoan`, it describes the call, and chapter 4 shows its signature (delivery review, finding 2).
* The example names chapter 3's sentence "any other failure of the write stays `DatabaseFailed`" as the rule the first draft broke, since chapter 3's "let everything else pass" is about fatal and framework throws (delivery review, finding 3).
* "Done is that whole list" now reads "Done is the review and that whole list", so it agrees with the opening and key point 3, which count the review in done (delivery review, finding 4).
* The pointer to chapter 16 says only that it has more on agents an agent launches, because chapter 16 today lists no specialized subagent and `ch16-review-agents` has not yet written the exception (decision 7).

**Omissions.** None.

**Decisions taken while building.**

* The study is introduced in the text as "a 2024 study of large language models on reasoning tasks, by Jie Huang and colleagues", scoping it to what it measured (decision 6).
* The Portuguese renders "a slot that says none" as "se o slot não nomeia revisor nenhum", since "diz nenhuma" reads badly.

**Review.** A read-only Opus agent read this delivery's `git diff` and `git diff --cached` of both chapters and this line's hunk of docs/06 against this page, docs/04 and the installed apply skill. It found nothing on parity, the quote, the note's format, em dashes, the prose rules, narrated runs or names of kit versions and models, and nine candidates, all fixed in this delivery: (1) the gain sentence read as if the reader fixed the fault, now "found by a reader that did not write it, and fixed in that delivery"; (2) and (3) the example's pointers to chapter 3 and 4, recorded above; (4) "Done is that whole list", recorded above; (5) a "So" that did not follow, dropped, and the sentence now says the reviewer measures the change against the page and docs/04; (7) "candidates" now explained where it appears, "faults it suspects"; (8) the Portuguese "lê através" now "enquanto a revisão de marco lê juntas as entregas do marco"; (9) "narrows the match" now "narrows the catch". Candidate (6), the pointer "(chapter 19)" in the new section, stays: the page's Behaviour names it, and it points to where another session's files in one folder are taught. No candidate became a queue line.

```commit
docs(ch13-delivery-review): teach the delivery review in chapter 13

- /apply has its changes reviewed by a context that did not write them
- The host's own review first, else a read-only agent, or none
- It fixes what breaks the page and lines the rest; lend-book shows it
- Cite Huang et al. on self-correction without external feedback

work/done/ch13-delivery-review.md
```
