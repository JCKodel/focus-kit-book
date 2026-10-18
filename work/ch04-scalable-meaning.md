# ch04-scalable-meaning

**Objective.** A reader of chapter 4 knows what the S of FOCUS means by scalable: the project can grow indefinitely without one feature interfering with another, and keeping features and jobs apart is what makes that growth scale. Both editions. From the author's reading of the book on 2026-10-18: "pt 04:102, the S of FOCUS, also says what scalable means: the project can grow indefinitely without one thing interfering with another; separating concepts and features is what makes growth scale."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *One sentence added after the existing one, which stays.* The S paragraph (en 04:100, pt 04:102 at /propose) says how: every piece isolated with its own test, a new feature changes no other. The new sentence, on the next line, says what that buys and names the word: growth without interference. Nothing is cut, since the existing sentence is the mechanism the new one leans on. Source: the draft ("also says"), docs/04 §Writing the book (one sentence per line, no filler).
2. *"Concepts and features" said with the chapter's terms.* Chapters 0 to 4 never use "concept"; what chapter 4 keeps apart is each feature in its folder (F) and each job in its piece (C, the four pieces). The sentence says "each feature keeps to its folder and each job to its piece", which is the author's separation in words the reader has just learned. Source: en 04:88-98, docs/03 (FOCUS row), docs/04 §Writing the book, Teach, do not only show.
3. *"Indefinitely" in both editions.* The author's word, kept as "indefinitely" / "indefinidamente", with no number or size attached, so no source is needed. Source: the draft, docs/04 (every number sourced: none added).
4. *Key points and docs/03 unchanged.* The key point (en 04:244, pt 04:246) already says "Scalable (every piece isolated, with its own test)", and docs/03's FOCUS row says "every piece isolated and testable, whatever the size"; both agree with the new sentence and stay. Source: docs/04 §Writing the book, One gain; docs/03.
5. No new docs/03 term, no new queue line, no split.

**Behaviour.**

* The reader of chapter 4, in English, reads under "FOCUS, letter by letter":
  * "**S, Scalable.** Every piece is isolated and has its own test, so a new feature adds its own folder and its own tests and changes no other." (unchanged)
  * then, on the next line of the same paragraph: "That is what scalable means here: the project can grow indefinitely, feature after feature, and no feature interferes with another, because each feature keeps to its folder and each job to its piece."
* The reader of the Portuguese edition, under "FOCUS, letra por letra":
  * "**S, Scalable (escalável).** Toda peça é isolada e tem o próprio teste, então uma feature nova acrescenta a própria pasta e os próprios testes e não muda nenhuma outra." (unchanged)
  * then: "É isso que escalável quer dizer aqui: o projeto pode crescer indefinidamente, feature após feature, sem que uma feature interfira em outra, porque cada feature fica na sua pasta e cada trabalho na sua peça."
* Checked at apply time:
  * `grep -n "scalable means\|escalável quer dizer" book/*/04-focus.md` prints one line per edition, right after the S line.
  * `git diff book/` shows only the one added line per edition.
* Fails: the existing S sentence changed or cut; the word "concept" introduced; a number or source added; the key point or docs/03 changed; any other change to chapter 4; a sentence that sets FOCUS against what it is not; an em dash.

**Contract.**

* Files: `book/en/04-focus.md`, `book/pt/04-focus.md`; one line added after the S of FOCUS (en 04:100, pt 04:102 at /propose).
* Terms of docs/03: none new; FOCUS, feature, piece as docs/03 has them. Sources: none added or removed. Cases: none. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* `ch04-focus-optional` edits chapter 4's opening (a note box after line 5) and its gain section; `ch04-uncle-bob` edits the sentence at en/pt 04:28, in the dependency rule section. Neither touches "FOCUS, letter by letter".
* `early-no-forward-links` lists this line as holding no pointer of its list; the new sentence names no chapter or command, so its apply-time grep finds nothing here.
* `pt-ninjobs-masculine` changes Ninjobs's article in pt 04; the new sentence has no Ninjobs mention.
* No shared hunk with any of them; the earlier lines shift whichever lands first, so the S line is found by its text, not its number.

**Out of scope.**

* The key point and docs/03's FOCUS row: decision 4.
* The F, C and U paragraphs.

**Done when.**

* [ ] Both editions written: the sentence as Behaviour says.
* [ ] Chapter 4 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [ ] Every number sourced: none added.
* [ ] `make verify` green: edition parity, prose rules, width, disclosure scan, no em dash.
* [ ] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [ ] `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.
