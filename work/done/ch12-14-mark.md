# ch12-14-mark

Built before the author read it: the author asked for the whole queue to be run, each page decided alone and built in the same session (docs/05 §4, a command that says to decide alone and to build as well). Every choice the documents leave open is marked "decided by the agent, the author corrects it in the review".

**Objective.** After chapters 12, 13 and 14 the reader, developer or not, knows that every mark of the queue changes through the kit's mark script, one byte, `/propose`'s `[~]` and `[>]`, `/apply`'s `[*]` and its `[x]` staged on its line alone with `stage`, and that any other edit to docs/06 is the host's file edit on the lines it changes, never a program that writes the whole file, because such a program emptied the queue twice.

**Behaviour.** What the reader can do or explain afterwards:

* Say how a mark changes: the agent runs `git -c "alias.fm=!sh .agents/skills/propose/scripts/mark.sh" fm <slug> "<mark>"`, which changes the mark of that slug's one line, one byte (the six marks differ only in the character between the brackets), writes the file beside the queue and renames it over it, and refuses, writing nothing, unless the result keeps the queue's size and differs in at most that byte.
* Say what `stage` adds: the same line changes in the index and nothing else there, so another session's staged lines stay; that is how `/apply` stages its `[x]`, its last edit.
* Say which edits are not the script's: a line added, a suffix such as `· blocked:` or `· dropped:`, a line moved; each is the host's file edit on the lines it changes, never a program that writes the whole file; a line put on hold is two edits, its mark by the script and its suffixes by the file edit.
* Say why, as the error the rule prevents: on 2026-10-18 in one project and on 2026-10-26 in another, a subagent marking its line ran a one-line program that opened the queue for writing, which empties the file, before reading it to change the mark, and the queue was left at zero bytes; both were staging their own hunk of a queue other sessions also edit.
* Failure: asked "may an agent mark its line `[*]` with a one-line script that reads docs/06, replaces the mark and writes the file back?", answer no: the mark goes through the mark script, and a program that writes the whole queue is what emptied it.
* Edge: asked "the line of `return-book` and the line of `overdue-list` sit side by side and the other session already staged its line; how does `/apply return-book` stage its `[x]`?", answer: with the mark script's `stage`, which changes `return-book`'s line in the index and nothing else, so the other line stays staged as it was.
* Find in chapter 12 that `/propose`'s `[~]` and `[>]` go through the script; in chapter 13 the script's line beside the claim script's, `[*]` through it, and `[x]` through it with `stage`; in chapter 14 the rule, what the script does and the error.
* In the Portuguese edition, the same, with docs/03's Portuguese term, "script de marca", as "script de reivindicação" and "script de fila" are.

**Contract.** Six chapter files and one document; line numbers en at HEAD `96a8a1b`; pt follows en sentence for sentence. The text is the agent's within these changes.

* **ch14** (`book/en/14-queue-states.md`, `book/pt/14-queue-states.md`)
  * C1, opening (:3): the reader also says how a mark changes, by the kit's mark script, and why the queue's other edits are made line by line. Still three sentences.
  * C2, a new section `## How a mark changes` (pt `## Como uma marca muda`) after "At the moment the work changes" (:65): the problem, one file every session edits; the error, unnamed projects, both dates, zero bytes, told in prose; the script's line and what it does, one byte, the file written beside and renamed over, the refusal on size and bytes; `stage`, the line alone in the index; every other edit by the host's file edit on its lines; a `[?]` as two edits.
  * C3, the team gain (:236-242): one sentence, no number: a session marking its line never leaves the queue the board reads empty.
  * C4, key point 1 (:246): the mark changed by the mark script, staged on its line alone, any other edit by the host's file edit. Still five key points.
* **ch12** (`12-propose.md`, both editions)
  * C5 (:31, :33): `[~]` and `[>]` set through the kit's mark script, which changes that one mark and nothing else of the file.
  * C6, key point 2 (:195): "marks the line `[~]`" through the mark script. No key point added.
* **ch13** (`13-apply.md`, both editions)
  * C7, after the claim script's paragraph (:32): the mark script, its line, run the same way, `stage` at the end when the line goes into the index; no pointer to chapter 19.
  * C8 (:49): `[*]` through the mark script.
  * C9 (:123): `[x]` with the mark script and `stage`, that line alone in the index, another session's staged lines kept.
  * C10 (:151): the lend-book walk-through's `[x]` the same way.
  * C11, key point 2 (:290): `[*]` and `[x]` through the mark script, `[x]` staged on its line alone.
* **docs/03**: a new row, mark script, script de marca, `propose/scripts/mark.sh` (added by this /propose, as the skill says).

Terms of docs/03: mark, queue line, stage, claim, queue tree; new: mark script. Sources: the kit's `SETUP.md` at 2026.11.12 (§3.8 `propose/scripts/mark.sh`, docs/05 §4's two sentences), the kit's `CHANGELOG.md` 2026.10.26 entry for the error and its two dates; this repository's docs/05 §4. No source note: the kit is taught as it is, and no note points to a file of focus-kit's repository (docs/04). Cases: none; the two projects stay unnamed, as the changelog leaves them.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable: no screen, and no new kind of content (prose, inline code); the Design slot of this repository says prototype, by choice (ADR-0019).

**Out of scope.**

* `mark.sh` refusing a `[~]` on a line that is not `[ ]` and a `[*]` on one that is not `[>]`: `ch12-14-mark-refused`, M35.
* Chapter 19's staging of a line with a patch given to `git apply --cached`: a grave finding of this /propose, its own line `ch19-mark-stage`.
* Chapter 8's install and update: it already counts three scripts and was taught at 2026.11.12 by `ch08-update-2026-10-25`.
* Chapter 12's six key points against docs/04's five: older than this delivery, a note for the review.
* The kit's account of how agents staged their hunk before the script (improvised scripts over the file and the index): a history of a kit change, which docs/04 keeps out; the error is told as the reason of the rule.

**Done when.**

* [x] C1 to C11 read as the Contract says in both editions, with the docs/03 row.
* [x] Both editions written; each chapter opens with its value; no filler and nothing useful cut; every date from the kit's changelog; no em dash; no run narration; no code but the script's line.
* [x] The error told without naming or hinting at a project: the disclosure scan green.
* [x] `make verify` green after the last edit.
* [x] `make book` builds both editions, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent, the author corrects it in the review: the error's source is the kit's public changelog, which names neither project; the chapter tells it as the changelog does, with no project named or hinted, so it draws on no private case and needs no approval under docs/00 OD-3. If either project is Case A or Case B, the author says so in the review.
* Decided by the agent, the author corrects it in the review: the one-line program is told in prose, not quoted: it is Python, and the book's code is TypeScript only (docs/04, ADR-0008).
* Decided by the agent, the author corrects it in the review: the two dates are written in the text, as the line asks, as dates of the error and not of a kit version, with no note (docs/04 "The kit as it is", the precedent of `ch09-design-slot`).
* Decided by the agent, the author corrects it in the review: the rule, what the script does and the error are taught once, in chapter 14, the chapter of marks; chapters 12 and 13 say which marks go through it, chapter 13 giving its line beside the claim script's, with no new pointer to chapter 14 in either.
* Decided by the agent, the author corrects it in the review: the term is a new docs/03 row, mark script, script de marca, as claim and queue tree name the other two scripts, rather than a longer mark row.
* From the documents: the rule (docs/05 §4), the script's behaviour (the kit's `SETUP.md` §3.8), the refusal kept out (`ch12-14-mark-refused`), chapter 19's patch as a grave finding (docs/05 §4: it breaks M34's clause "staged with it on its line alone" for a reader of chapter 19's usual path; no patch staging survives in the kit's `SETUP.md`).

## Outcome

* Built as the Contract says, C1 to C11, in both editions, with the docs/03 row `mark script` / `script de marca` that /propose added; chapter 14 gains the section `## How a mark changes` (pt `## Como uma marca muda`) after "At the moment the work changes"; chapters 12 and 13 say which marks go through the script, chapter 13 giving its line beside the claim script's; no pointer added.
* Diverged: chapter 14 also says what a hunk is where the error names one, since the reader meets the word there before chapter 19; the Portuguese chapter 13 says "índice", docs/03's term, where the first draft said "index".
* Proof: `make verify` green after the last edit, 15 seconds on 2026-11-12, under the five-minute ceiling; `make book` at HEAD `96a8a1b` with this delivery's changes in the tree built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, with their EPUBs. No slow tests: the Verify slot names none.
* Delivery review: one read-only agent on Opus (model set at launch, Explore type) read this page, `AGENTS.md`, docs/04, docs/05 §4, `git diff HEAD` of the six chapter files, docs/03 and this delivery's docs/06 lines, the installed `mark.sh`, the kit's `CHANGELOG.md` and `CHANGELOG.pt.md` 2026.10.26 and chapter 19 :360-378; its report says it consulted the advisor once. Eight candidates:
  * 1, ch14 :71-72: "the read found nothing" and "their own line" glossed the changelog; fixed: the changelog's words, "the write emptied docs/06 before the read", "their own hunk", with the hunk explained.
  * 2, ch14 :70-71: the error a dated story, docs/04 asking for the reason in the present; fixed: the reason first, in the present (a program that opens the file for writing before it reads it empties it), the dates after it, as the line asks.
  * 3, ch14 :76, ch13 :35: "refuses, writing nothing" is false with `stage`, whose index step comes after the queue is written; fixed: "refuses before it writes the queue".
  * 4, ch14 :3: the opening said how, not why; fixed: "since a program that writes the whole queue can empty it".
  * 5, ch13 :35: "one byte" and "the host's own file edit" used before chapter 14 explains them; fixed: both glossed there, with no pointer.
  * 6, ch13 key point 2: "after the stage, with `stage`"; fixed: "once the rest is staged, with `stage`".
  * 7, pt ch12 :33: "o script vira a marca"; fixed: "muda".
  * 8, ch12's six key points: older than this delivery; a note below.
  * Cosmetic: the new queue line's slug column one space off its neighbours, as the file already was; left as it is.
* Verify ran again after the fixes: green.
* Finding of /propose, grave (docs/05 §4): chapter 19 :29, :367-372 and :388 teach `/apply` staging its line of docs/06 with a hand-written patch given to `git apply --cached`, which `mark.sh`'s `stage` replaces, breaking M34's clause "staged with it on its line alone" for a reader of chapter 19's two sessions in one folder; the line `ch19-mark-stage`, `· from ch12-14-mark`, above `m34-review`.

## For the review

* book/en/12-propose.md:194-199 and book/pt/12-propose.md: six key points, docs/04 allows five; a reader sees one bullet more than every other chapter; older than this delivery, which only edited bullet 2.
* work/done/ch12-14-mark.md, Decisions: the two projects of the error are told as the kit's changelog leaves them, unnamed; if either is Case A or Case B, the passage needs the author's approval (docs/00 OD-3).

```commit
docs(ch12-14-mark): teach marks changed by mark.sh, one byte

- ch14: how a mark changes, the queue emptied twice as the error
- ch12, ch13: [~], [>], [*] and the staged [x] through the mark script
- docs/03: the mark script row
- docs/06: ch19-mark-stage, the patch chapter 19 still teaches

work/done/ch12-14-mark.md
```
