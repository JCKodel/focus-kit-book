# ch18-19-only-apply

**Objective.** After chapter 13 a reader knows that code changes only inside `/apply`, and that a change asked anywhere else, however small, becomes a `[ ]` line in the queue and the answer stops there. After chapter 19 they know that `AGENTS.md` makes the agent answer "where are we?" from the queue and the pages, with the next command as their host invokes it, and that there is no status command because the queue already is the status. Both as focus-kit 2026.10.13 says.

**Behaviour.**

* A reader looking at the loan screen of the lending library asks the agent, in an ordinary session, "show the due date as day/month/year". From chapter 13 they expect the agent to add `[ ] due-date-format` under milestone 1, above `m1-review`, say so, and stop, with no file under `src/` changed.
* The same request made during `/propose lend-book` gets the same answer: a new line, and the page unchanged unless the person asks for that line's scope to be part of this page (chapter 14: `/propose` writes no code).
* Failure: a reader whose agent edits `src/loans/` in answer to "just change the label" knows from chapter 13 that this skipped the line, the page and verify. They ask for the line instead, and the edit is reverted before anything is committed.
* Edge: a fix found in the middle of `/apply my-loans` is still the case chapter 16 teaches, a `[ ]` line above it plus `· blocked: after`. Chapter 13 says the rule covers every session, `/apply`'s own included.
* Edge: a correction to a document, such as a line of docs/00 or the queue, is still made by conversation in any session (chapter 13 "Changing the queue", chapter 12). The rule covers code: the app's source, its tests, a migration, configuration.
* A manager in the host at the project's root asks "where are we?". From chapter 19 they expect: the milestone and how many of its lines are done, the lines in flight with their marks, any `[?]` line with its reason, and the next free line with the command to run, `/propose due-date-format` in Claude Code or `$propose due-date-format` in Codex (chapter 11's table).
* Edge: when a line is `[?]`, the answer names its reason and its resume phase, as the line holds them.
* Failure: an agent that answers from what it remembers of the session, offers to keep a status file, or suggests adding a status command. The reader knows from chapter 19 that the queue already is the status, and asks for the file behind the answer, as "The person is the brain" says.
* A reader asked "why does the kit have no status command?" answers: the queue and the pages already hold the status, and a line in `AGENTS.md` tells every session to read them.

**Contract.**

* **Chapter 13, both editions, file name, title and headings kept.**
  1. Opening, second sentence: the reader can also turn a code change asked outside `/apply` into a line.
  2. "Changing the queue", after "No command owns the queue" paragraph's first two sentences: the code has one owner, `/apply`. A change to it asked in any other session, however small, becomes a `[ ]` line, the agent says so, and the answer stops there. Documents still change by conversation. The example is written for the chapter: `[ ] due-date-format   the loan screen shows the due date as day/month/year`, in milestone 1 above `m1-review` (Portuguese: `formato-da-data-de-devolucao`, "a tela do empréstimo mostra a data de devolução como dia/mês/ano"). The section also says a fix found inside `/apply` follows the same rule (chapter 16).
  3. "What the team gains": a sentence from the kit's changelog, entry 2026.10.06.1, paraphrased with no note (docs/04, as the 2026.10.08.3 paragraph beside it). Before the rule, an agent asked for a correction in an ordinary session edited the code directly, with no line in the queue, no page and no verify. Since then a change asked outside `/apply` costs one line, and it gets a page, a proof and the person's commit.
  4. Key points: the "No command owns the queue" point gains "; code changes only inside `/apply`, and a change asked anywhere else becomes a line".
* **Chapter 19, both editions, file name, title and headings kept.**
  1. Opening, first sentence: "what is pending, how it is going and who owes an answer" gains "where it stands and what to run next".
  2. "The questions the team asks": a new first bullet, **Where are we, and what comes next?**, answered by the queue's lines in flight with their marks, the `[?]` lines with their reasons, and the next free line with its command (shown in "The manager's session").
  3. "The manager's session": the rules file also holds a line for this question, so a session asked where things stand answers from the queue and `work/`, with the next command as that host invokes it. There is no status command, because the queue already is the status (the kit's changelog, entry 2026.10.08.1, paraphrased, no note). Then a block written for the chapter on the lending library, said so, about five lines:
     ```text
     Milestone 1, a librarian lends and takes back: 4 of 7 lines done.
     In flight: return-book [*], being built.
     Waiting: none.
     Next free line: due-date-format [ ], no page yet.
     Run: /propose due-date-format (Codex: $propose due-date-format)
     ```
     Portuguese wording and names in the Portuguese edition (`devolver-livro`, `formato-da-data-de-devolucao`).
     The paragraph on changes gains: a change to the code, however small, becomes a line as well (chapter 13), and the session stops there.
  4. Key points: the manager point gains "asked where things stand, it answers from the queue with the next command; there is no status command".
* **Terms:** queue, mark, free line, waiting mark, resume suffix, page, rules file, host, as docs/03 has them; docs/03 unchanged.
* **Sources:** the kit's CHANGELOG, entries 2026.10.06.1 and 2026.10.08.1, named in plain words with no note (docs/04, `ch15-apply-ends` precedent); `AGENTS.md`'s line on where things stand, as the kit's template writes it.
* **Cases:** none new. Case A's paragraph in chapter 19 stays unchanged.
* **Code examples:** the queue line and the "where are we?" answer, written for the chapter on the lending library and said so; Portuguese names in the Portuguese edition.
* **This repository:** docs/05 §2 and `AGENTS.md` already hold both rules (`kit-2026-10-13`); nothing changes there.

**Out of scope.**

* Chapter 18: the author chose chapter 13 for the rule. The governor's examples stay as they are, so the rule is said once.
* Chapter 15 and `/apply`'s next steps: `ch15-apply-ends`, done.
* "Each command names the next one as the host invokes it" for every command: `ch11-update-migrations`.
* Chapter 10's description of `AGENTS.md`'s sections: its lines are not listed there, and chapter 19 is where the question is asked.
* A new run or count: the changelog is the evidence (ADR-0017).

**Done when.**

* [x] Chapters 13 and 19 changed in both editions, same headings; both still open with their value; no filler and nothing useful cut.
* [x] No sentence in the book suggests an agent may change code outside `/apply`, or that the kit has a status command.
* [x] The `due-date-format` line and the "where are we?" block in both editions, Portuguese names in the Portuguese one, said to be written for the chapter.
* [x] Changelog entries 2026.10.06.1 and 2026.10.08.1 paraphrased and checked against the kit's CHANGELOG at 2026.10.13, no note.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* The rule covers code only, and documents still change by conversation in any session. Sources: docs/05 §2 ("Code changes only inside /apply"), and chapter 13's "No command owns the queue", which this book teaches as the kit's.
* Evidence from the kit's changelog, with no Case A passage and no note. Sources: ADR-0017, docs/04, and the `ch15-apply-ends` precedent.
* Two hosts in the next command, Claude Code and Codex, with a pointer to chapter 11's table: the `ch15-apply-ends` precedent.
* The rule goes in chapter 13, not 18 (asked; the author chose).
* A sample answer block in chapter 19 (asked; the author chose).

**Divergences.**

* The Portuguese queue line is `[ ] formato-devolucao   o empréstimo mostra a devolução em dia/mês/ano`, not the Contract's `formato-da-data-de-devolucao` with "a tela do empréstimo mostra a data de devolução como dia/mês/ano": that line is 98 columns and docs/04 keeps a block at 74. The author chose a shorter slug and text in this session; the text was trimmed further than the option offered (78 columns) to fit 70. Chapter 19 uses the same slug.
* The Portuguese "where are we?" block's first line ends "4 de 7 feitas", without "linhas", to stay within 74 columns.
* Chapter 13's paragraph after the new code rule opens "A milestone's paragraph or a line's description changes by conversation too" (pt: "também muda conversando") instead of "the same way", since the rule now stands between it and the conversation it pointed back to.
* Chapter 13 says the failure (an agent that edits the code anyway is asked for the line, the edit reverted) and the `/propose` edge in the text, from Behaviour; the Contract did not list them.
* Chapter 19's code paragraph ends "the answer stops there", the words of chapter 13, rather than "the session stops there".

**Omissions.** None.

**Proof.** `make verify` green. `make book` builds; the author reviews chapters 13 and 19 in `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. The two changelog entries were read in the kit's `CHANGELOG.md` at 2026.10.13, and the line on where things stand in its `SETUP.md` template of `AGENTS.md`. A search of `book/` for "status command", "comando de status" and phrases of an agent editing code on request finds only the new passages; chapter 14's spike stays a conversation that ends in a line, a document or `/propose`, consistent with the rule. Both new blocks fit 74 columns.

**Decisions.** No document or ADR changes: docs/05 §2 and `AGENTS.md` already hold both rules, docs/03 unchanged; no manual changes, nothing done by hand changed. Chapter 15 and 16 pointers are plain text, since each chapter already links them once (docs/04, chapter pointers).

* The queue line until kit-2026-10-16 said: chapter 13: code changes only inside /apply, a fix asked anywhere else becomes a queue line; chapter 19: AGENTS.md answers "where are we?" from the queue, with no status command; both editions.

```commit
docs(ch18-19-only-apply): teach code only in /apply and where are we

- chapter 13: a code change asked outside /apply becomes a [ ] line
- chapter 13: the due-date-format line, changelog 2026.10.06.1 as gain
- chapter 19: "where are we?" answered from the queue, no status command
- chapter 19: a sample answer on the lending library, both hosts
- both editions

work/done/ch18-19-only-apply.md
```
