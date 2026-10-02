# ch25-protocol-findable

**Objective.** A reader of chapter 25 knows, from its opening, what the challenge protocol is and where its four turns are written, and finds them again, word for word, by paging through the chapter, without rereading the section; both editions.

**Decided by the author.**
1. The turns live only in the chapter: no file in the repository, no focus-kit command.
2. The opening says, in one sentence, what the protocol is and where it is written, and says once what a turn is.
3. Key points quotes the four turns word for word.

**Why C3 failed** (the agent's reading, from `m9-review`): the opening names "the four turns of the challenge protocol" about 70 lines before the chapter says what it is; the definition leans on "protocol" and "turn", which the book never explains for a reader who is not a developer; the turns are an ordinary numbered list in the prose, nothing in the PDF sets them apart, and Key points paraphrases them, so the exact words are only in the section.

**Behaviour.**

* A reader of the opening paragraph alone can say what the challenge protocol is (four messages, always the same, sent after an agent's first answer), what a turn is, and under which section the four are written.
* A reader paging through the PDF finds the four turns as a block on night blue under §The challenge protocol, set apart from the prose, and can copy them as they are.
* A reader on the Key points page finds the four turns word for word, the same words as the block.
* Turn 2's "Are you sure?" paragraph, the other turn paragraphs, the experiment, its numbers and the notes read as before.
* The Portuguese edition says the same in the same places, with its translated turns; its sentence that the experiment sent them in English stays.

**Contract.**

Chapter 25, `book/en/25-asking-for-more.md` and `book/pt/25-asking-for-more.md`; the wording below is the English intent, /apply writes the final sentences and the Portuguese.

* **Opening.** One sentence between line 3 ("After this chapter you can...") and line 4 (the experiment's result), in the same paragraph: the challenge protocol is four messages you send, word for word, after an agent's first answer; each message and the agent's reply to it is a turn; the four are written out, ready to copy, under the section "The challenge protocol". Lines 3 and 4 unchanged.
* **§The challenge protocol, first lines.** The definition says "four messages, always the same", not only "four turns"; then one line that introduces the block ("These are the four turns the experiment sent; copy them as they are:"; pt keeps that the experiment sent them in English and these are the same, translated).
* **The block** replaces the numbered list: a `text` code block, no quotation marks, each turn numbered, wrapped with a three-space hanging indent, no line over 74 columns (docs/04, width of a block). English:

  ```text
  1. Before you change anything, ask me what you need to know to do
     this well.
  2. What did you say is not possible, or not worth doing? Test each
     one and show me the result.
  3. Who reads or uses this, how much time do they have, and what does
     each use cost? Change the result to fit.
  4. What did I not ask for that I would want? Add what is worth it,
     and tell me what you left out.
  ```

  Portuguese: the four turns already in `book/pt` at lines 77 to 80, word for word, in the same form.
* **Key points**, the protocol bullet becomes: the challenge protocol is four turns, sent one at a time after the first answer, followed by the four turns quoted word for word, as in the block (inline quotes, numbered 1 to 4 in the sentence).
* Sections, headings, notes, sources, numbers, cases: unchanged. No term added to docs/03 (its "challenge protocol" row already holds; "turn" is a plain word explained once in the chapter).

**Out of scope.**

* The cost in USD and what it means on a fixed subscription: `ch25-cost-for-subscribers`, which also edits this chapter; this delivery leaves line 4, §What the protocol bought, and what it cost, and the cost bullet of Key points as they are.
* A file of the turns in the repository or a focus-kit command: decision 1.
* The prologue: C5 held.
* Defining "turn" in chapter 3, where the word first appears: C3 is chapter 25's finding.
* Any new CSS or a box style: the night-blue code block already exists in the PDF, the site and the EPUB.

**Done when.**

* [x] Opening, section and Key points as Contract, in both editions.
* [x] The block is the turns of the chapter word for word, no line over 74 columns, in both editions.
* [x] No line of §What the agent does not propose, the turn paragraphs, §What the protocol bought, and what it cost, §What the team gains or the notes changed, beyond the Contract.
* [x] Opens with its value, no filler and nothing useful cut; no em dash.
* [x] `make verify` green, disclosure scan included.
* [x] `make book` run; both PDF paths given to the author, with the page where chapter 25 starts.
* [x] Page in `work/done/`, `ch25-protocol-findable` `[x]`, staged, commit message suggested.

## What happened

* As planned, both editions. The opening sentence sits between lines 3 and 4 and points to the section by its title, in quotation marks, with no link; lines 3 and 4 unchanged.
* The section's first sentence keeps "one at a time, each when ... ends" and now says the previous one ends with the agent's reply, so "turn" reads as the chapter defined it.
* Key points numbers the turns as (1) to (4) inside the sentence, separated by semicolons, the quotes the same words as the block.
* The Portuguese block wraps where Portuguese needs it; its longest line is 71 columns, the English 68.
* Proof: `make verify` green; `make book` built; chapter 25 starts on page 166 of the English PDF and 175 of the Portuguese, the block is on pages 170 and 179, set on night blue, no line wrapped.
* No document changed: docs/03's "challenge protocol" row holds, and docs/04's width of a block already covered the block.
