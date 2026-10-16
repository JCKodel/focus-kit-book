# ch15-apply-ends

**Objective.** After chapter 15 a reader knows how `/apply` ends, as focus-kit 2026.10.13 says: it stages only its own delivery and leaves everything else in the tree and the index as it found it; it writes the suggested commit message at the end of the page in a fenced block whose info string is `commit`, and shows the same block in the conversation, on the done path and on the blocked one; and its last words are the reader's next steps, each command written out, the next one as their host invokes it.

**Behaviour.**

* A reader whose `/apply lend-book` is done finds, at the end of `work/done/lend-book.md`, one `commit` block, and the same block in the conversation; they paste it into `git commit` without retyping it.
* A reader who commits the next morning, in another window, finds the message on the page, since chapter 15 says the page holds it and the conversation only repeats it.
* Failure: a reader whose agent answers with `git commit -m` lines and no `commit` block on the page knows from chapter 15 that the delivery did not end as the kit says, and asks the agent for the block.
* A reader whose tree holds another session's edit to `src/members/` and its staged hunk of docs/06 while `/apply lend-book` runs knows the staged diff afterwards holds only `lend-book`'s paths and its own hunk of docs/06, that the other entries are untouched, and that `/apply` reports an unrelated entry already staged instead of unstaging it (chapter 21 for two sessions).
* Failure: a reader who sees `git add -A` or `git add .` in their agent's run knows from chapter 15 that `/apply` never stages that way.
* Edge: a reader whose `/apply lend-book` stops on trunk because docs/00 does not say what a suspended member sees finds the line `[?]` with `· resume: apply`, the page in `work/` with what was built and what it waits on, a partial message in a `commit` block on the page and in the conversation that says it is partial and names the blocker, and whose last line is `work/lend-book.md`, and nothing staged: on trunk the work stays uncommitted and out of the index until it is whole.
* Edge: a reader working on a delivery branch knows the same blocked `/apply` may stage the partial work for them to commit on that branch, which stays unmerged until the delivery is complete.
* A reader at the end of `/apply lend-book` reads, in order: review the staged diff (`git diff --staged`); commit with the suggested message (and on a delivery branch, merge it); then the queue's next free line, `return-book`, and its command in a fresh session, `/propose return-book` in Claude Code or `$propose return-book` in Codex (chapter 11's table).
* A reader asked "what does the last line of the message point to?" answers: the page's actual path, `work/done/<slug>.md` when done, `work/<slug>.md` when blocked.

**Contract.**

* **Chapter 15, both editions, file name and title kept; same headings in both.**
  1. Opening: the reader can also say how `/apply` ends: only its delivery staged, the message in a `commit` block on the page and in the conversation, and the next steps written out.
  2. "When the work cannot go on": "and stages what it has (chapter 16)" becomes: it ends the page with a partial message in a `commit` block, shows it in the conversation, and on trunk stages nothing, the work staying uncommitted until it is whole; on a delivery branch the partial work may be staged and committed there, the branch unmerged until the delivery is done (chapter 16 for the mark, chapter 21 for branches).
  3. "Green is not done": the bullet "It stages everything and suggests the commit message..." becomes two: it stages only this delivery's paths and hunks, never `git add -A` or `git add .`, and reports what someone else had already staged without unstaging it; it ends the page with the suggested message in a `commit` block, one block, which a resumed `/apply` replaces, and shows the same block in the conversation. The last bullet becomes the next steps: which environment is at which version and the command that updates the others, then review the staged diff, commit (merge on a branch), and the queue's next line with its command as the host invokes it, in a fresh session. "Done is that whole list" says "only this delivery staged".
  4. "`lend-book`, built": its last paragraph's "stages everything, suggests the message, and ends by saying..." follows item 3, and the section shows the `commit` block that ends `work/done/lend-book.md`, written for the chapter (subject "Lend a copy to a member", up to five bullets, last line `work/done/lend-book.md`), and the next steps with `return-book` as in Behaviour; Portuguese names in the Portuguese edition (`emprestar-livro`, `devolver-livro`, `work/done/emprestar-livro.md`). Line 69's list of tests is `ch14-propose-decides`'s and is not touched here.
  5. "Why it stops at the stage": "It stages everything" becomes "It stages only its delivery".
  6. "Review the staged change": the questions gain "Does the staged diff hold only this delivery, and did the agent report anything already staged?"; the message question names the `commit` block on the page.
  7. "The commit is the human review": when another session works in the same folder, commit one delivery at a time from the index, once `git diff --staged` holds only it (chapter 21); the editor paragraph says where to copy the message from: the `commit` block on the page.
  8. "The message": the format block and its text gain the blocked case: a partial message says it is partial and names the blocker, never implies verify passed, and its last line is `work/<slug>.md`. The format stays the kit's (scope in parentheses when it helps); this book's own `<type>(<slug>)` is docs/05's choice and is not taught here.
  9. "What the team gains": the kit's changelog paraphrased, no note (docs/04): entry 2026.10.06, the message lived only in the chat, an agent answered with `git commit -m` lines, and whoever committed later, in another window or session, had nowhere to start; entry 2026.10.08.2, a message suggested as plain text in a terminal lost the fenced block's highlight and blended into the reply; entry 2026.10.08.1, a person who had just used the kit for the first time knew to commit but had to search the documentation for what came after, and a Codex user was told to run `/propose`, which Codex does not recognize. The Ninjobs paragraph kept.
  10. Key points: the staged-change point says only this delivery; a new point on the `commit` block on the page and in the conversation, also when blocked; the last action is the next steps, written out.
* **Terms:** page, queue, free line, resume suffix, verify, as docs/03 has them; docs/03 unchanged.
* **Sources:** the file of `/apply` and docs/05 §6 of the kit's `SETUP.md`, named in plain words; the kit's CHANGELOG, entries 2026.10.06, 2026.10.07 (stages only its delivery), 2026.10.08.1 and 2026.10.08.2, no note (docs/04).
* **Cases:** Ninjobs's paragraph unchanged; no new private passage.
* **Code examples:** the `commit` block and the next steps for `lend-book`, written for the chapter on the lending library, said so; Portuguese names in the Portuguese edition.
* **Queue:** the line keeps `· after kit-2026-10-13` alone (author's choice); `ch14-propose-decides` is already `[x]` and its list of five tests is in chapter 15.

**Out of scope.**

* Chapter 15's list of tests and the five Behaviour lines: `ch14-propose-decides`.
* "Each command names the next one as the host invokes it" for every command, and the host forms themselves: `ch11-update-migrations`; chapter 15 shows `/apply`'s next steps with two hosts and points to chapter 11's table.
* Two sessions in one tree, hunk-by-hunk staging and `git add -p`: chapter 21, already done (`ch21-one-tree`); chapter 15 points there.
* Chapter 10's "docs/04 ... the format of a commit message", now docs/05 §6's: `ch11-update-migrations`, which teaches the migration of docs/04 and docs/05.
* `docs/manuals/` written or updated by `/apply`: `ch10-12-manuals`.
* Code only inside `/apply`: `ch18-19-only-apply`.
* A new run or count: the changelog is the evidence (ADR-0017).

**Done when.**

* [x] Chapter 15 changed in both editions, same headings; opens with its value; no filler and nothing useful cut.
* [x] No sentence in the book says `/apply` stages everything, or that a blocked `/apply` on trunk stages its work.
* [x] The `commit` block for `lend-book` and the next steps with `return-book` in both editions, Portuguese names in the Portuguese one.
* [x] The changelog entries and the file of `/apply` named in plain words, no note to focus-kit's repository; every number and quote sourced.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* Blocked on trunk stages nothing, against chapter 15's "stages what it has": docs/05 §6 and the kit's §6.
* The kit's message format (scope when it helps) is what the chapter teaches, not this book's `<type>(<slug>)`: the book teaches the kit (docs/00), and docs/05 §6 is this project's filling of the slot.
* The `lend-book` block shown in full beside the abstract format (asked; author chose).
* The next steps with two hosts, Claude Code and Codex, pointing to chapter 11's table (asked; author chose).
* No `· after ch14-propose-decides` (asked; author chose); that delivery finished while this page was written.
* Evidence from the changelog, no Case A passage: ADR-0017 and the ch14 precedent.

**What happened.**

* Chapter 15 changed in both editions along Contract items 1 to 10, same headings: the opening gains how `/apply` ends; the blocked section ends with the partial `commit` block, nothing staged on trunk, staged work on a delivery branch kept unmerged; "Green is not done" stages only the delivery, ends the page with one `commit` block shown in the conversation too, and closes with the next steps.
* "`lend-book`, built" shows the `commit` block that ends `work/done/lend-book.md` (subject "Lend a copy to a member", five bullets) and the next steps with `return-book` in Claude Code and Codex; the Portuguese edition uses `emprestar-livro`, `devolver-livro`, `src/membros/` and `JaEmprestado`.
* "The message" gains the blocked case and the failure of a reply with `git commit -m` lines and no block; "The commit is the human review" says where to copy the message from and to commit one delivery at a time from the index when another session shares the folder.
* "What the team gains" paraphrases the kit's changelog entries 2026.10.06, 2026.10.08.2 and 2026.10.08.1, no note; the Ninjobs paragraph is unchanged.
* No other chapter says `/apply` stages everything or that a blocked `/apply` stages its work on trunk (searched both editions).
* The queue line until kit-2026-10-16 said: chapter 15: the commit message in a `commit` block on the page and in the conversation, also when blocked; /apply stages only its delivery; it ends with the person's next steps in the host's form; both editions.

**Divergences.**

* None from the page. The Behaviour line on another session's `src/members/` edit is taught in "`lend-book`, built", in one sentence pointing to chapter 21.

**Proof.**

* `make verify` green; `make book` builds `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, given to the author for review.
* The first `commit` fence in the book renders in the strict site build and in the PDF like any other code block.

**Decisions.**

* The environments step stays in prose before the numbered next steps in the `lend-book` example, since the library's environments are not the chapter's subject.
* Sources checked against the kit's CHANGELOG (entries 2026.10.06, 2026.10.07, 2026.10.08.1, 2026.10.08.2) and §6 of its `SETUP.md`.

```commit
docs(ch15-apply-ends): teach how /apply ends its delivery

- Stage only this delivery, never git add -A, and report what was staged
- End the page with one commit block, shown in the conversation too
- Partial message when blocked; nothing staged on trunk
- End with the next steps in the host's form, lend-book as the example
- Evidence from the kit's changelog, 2026.10.06 and 2026.10.08.1-2

work/done/ch15-apply-ends.md
```
