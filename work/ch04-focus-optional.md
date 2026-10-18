# ch04-focus-optional

**Objective.** A reader of chapter 4 knows from its first lines that FOCUS is a choice the team makes, reads the chapter, above all its gain, to make it, and finds in the gain one more reason that weighs on that choice: one pattern across a company's projects makes moving people between teams cheaper. Both editions. From the author's reading of the book on 2026-10-18: "Chapter 4 opens with a disclaimer: FOCUS gathers the best qualities of the best practices, distilled into a simple, effective architecture, but it is optional. [...] the team should first understand the architecture and the value it delivers, and whether it makes sense. Encourage the reader to read, above all 'What the team gains', and decide whether the team sees the value."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *After the opening, as a note box.* The three "After this chapter you can" sentences (en/pt 04:3-5) stay first and unchanged, since every chapter opens with what the reader can do; the disclaimer follows them, before `## The problem` (pt `## O problema`), as a `> **Note.**` box (pt `> **Nota.**`), one paragraph, one sentence per line. The author called it a disclaimer, and docs/04's note box holds "a warning the reader needs at that point and the section's flow does not carry". If the author prefers a plain paragraph, the content is the same. Source: ADR-0015, docs/04 §Writing the book, **A note box**, the draft.
2. *The kit as it is, not as the draft words it.* The draft says the kit "asks whether to create a new project with FOCUS or migrate an existing one". What the kit asks today, in `/brainstorm` for a new project and in `/analyze` for an existing one, is one question with three answers: FOCUS whole; its two principles only, vertical slices and exceptions as values, in whatever structure the stack favors; or neither, the project's own conventions. On existing code the default is what the code already does, and moving to FOCUS gradually is one way to answer. The kit's own words are "Two things the kit offers and never imposes". The box says that, in a few words. Source: `.claude/skills/brainstorm/references/documents.md` and `.claude/skills/analyze/references/documents.md` §Choices (identical), en 09:19, 81, 100-103, en 07:48-56, docs/04 §Writing the book, **The kit as it is**.
3. *No command and no chapter named in the box.* The reader of chapter 4 has not met `/brainstorm` or `/analyze`, and `early-no-forward-links` removes every forward pointer in chapters 0 to 7 outside the gain sections; the box says "when focus-kit starts a project with the team, new or already written" and names no later chapter. Pointing to this chapter's own `## What the team gains` is not a chapter pointer. Chapter 7's "The two choices" stays as it is: chapter 4 says FOCUS is a choice, chapter 7 says how the kit records it, and the Ninjobs example stays there. Source: work/early-no-forward-links.md, docs/04 §Writing the book, **Chapter pointers**, en 07:48-56.
4. *Optional without undercutting.* The box says first what FOCUS is, in the author's register: the qualities of the practices this book teaches gathered into one simple architecture. Then that it is the team's choice, and that the team makes it after reading the chapter and its gain. It gives no reason to refuse FOCUS, names no cost of it and sets it against nothing. Source: the draft, docs/04's `not-but` rule ("say what it is; do not set it against what it is not"), the author's rule that FOCUS is the solution.
5. *The new gain is the author's reasoning, in his voice.* One or two sentences close `## What the team gains` (pt `## O que o time ganha`), after the shared use cases: when every project of a company follows one pattern, a person who moves to another team finds the folders, the four pieces and the tests where they expect them, so moving people between teams costs less. It is written as the author's reasoning, in the first person the book already uses (en 04 once, chapter 6), with no number, no source and no sentence about a missing number. Source: docs/04 §Writing the book, **A gain per chapter**, docs/06 M18's line, the draft.
6. *No new Ninjobs mention.* en 07:55 already says Ninjobs chose the two principles, and `pt-ninjobs-masculine` rewrites Ninjobs's article in pt 04; the box and the gain add no Ninjobs sentence, so no new fact and no article to agree. Source: docs/03 §Entities and invariants, work/pt-ninjobs-masculine.md.
7. *Key points unchanged.* A key point says what the reader does, not what is gained; the cheaper move between teams is a gain, said once in its section. The author can add a key point on the choice in review if he wants one. Source: docs/04 §Writing the book, **One gain**.
8. No new docs/03 term, no new queue line, no split.

**Behaviour.**

* The reader of chapter 4, in either edition, reads the three opening sentences as they are, then a note box that says:
  * what FOCUS is in one sentence: the qualities of the practices the book teaches, simplicity, exceptions as values and vertical slices, gathered into one simple architecture;
  * that it is the team's choice: focus-kit asks, when it starts a project with the team, new or already written, whether the project uses FOCUS whole, only its two principles (vertical slices and exceptions as values), or neither, and the rest of the method works the same under each answer;
  * that the reader should read the chapter, above all `## What the team gains` (pt `## O que o time ganha`), and decide whether the team sees the value.
* The gain section keeps its four sentences (en 04:236-239 at /propose, pt 04:238-241) and ends with the author's reasoning, in one or two sentences: one pattern across a company's projects means a person moving to another team finds the code laid out as they know it, so moving people between teams costs less.
* The Portuguese edition says the same in the same places, with the chapter's terms ("fatias verticais", "exceções como valores", "peças", "time").
* Checked at apply time:
  * `grep -n "Note\." book/en/04-focus.md` and `grep -n "Nota\." book/pt/04-focus.md` print one line each, after line 5 and before `## The problem` / `## O problema`.
  * `head -5` of each edition's chapter 4 is unchanged by this delivery.
  * `git diff book/` shows changes only in the box and in the gain section of chapter 4, both editions.
* Fails: the box before the opening sentences; a forward pointer to a chapter or a command named in the box; the box describing the kit's question other than as its three answers; a sentence that frames FOCUS as a risk, a cost or a problem, or sets it against what it is not; a number or a source added; a sentence saying the gain has no measured number; a new Ninjobs mention; a key point changed; any change outside the box and the gain section; an em dash; a run narrated.

**Contract.**

* Files: `book/en/04-focus.md`, `book/pt/04-focus.md`; the new note box after the opening and `## What the team gains` (pt `## O que o time ganha`) only.
* Terms of docs/03: none new; `FOCUS` ("The optional architecture"), `vertical slice` and `exceptions as values` as docs/03 has them. Sources: none added or removed. Cases: none. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change; docs/04's note box rule already covers a third use. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* `ch04-uncle-bob` edits the sentence at en/pt 04:28, in "The dependency rule"; `ch04-scalable-meaning` (still a draft) edits the S of FOCUS (en 04:100, pt 04:102). Neither touches the opening or the gain section.
* `early-no-forward-links` lists this line as holding no pointer of its list and edits en 04:54 and 198 (pt 55, 200); it applies last of M18's lines on chapters 0 to 7, and its apply-time grep finds no chapter pointer in this box (decision 3).
* `pt-ninjobs-masculine` changes Ninjobs's article in pt 04; this delivery adds no Ninjobs mention (decision 6).
* No shared hunk with any of them; whichever lands later finds the box and the gain by their text, not their line numbers.

**Out of scope.**

* Chapter 7's "The two choices" and chapter 9's FOCUS question: decision 3.
* The opening sentences and the key points: decisions 1 and 7.
* The link to "chapter 7 ... 07-four-pieces" in the kit's own `references/documents.md`, which answers 404 since the chapters were renumbered: a file of the kit, for the author to take to focus-kit's repository, not this book's.

**Done when.**

* [ ] Both editions written: the note box and the gain sentence as Behaviour says.
* [ ] Chapter 4 still opens with its value, keeps its gain said once, no filler and nothing useful cut.
* [ ] Every number sourced: none added.
* [ ] `make verify` green: edition parity, prose rules, width, disclosure scan, no em dash.
* [ ] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [ ] `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.
