# ch04-uncle-bob

**Objective.** A reader who knows Robert C. Martin only as Uncle Bob recognises him the first time the book names him. Both editions. From the author's reading of the book on 2026-10-18: the first time the book names Robert C. Martin, give his nickname, Uncle Bob, in parentheses, because many readers know him only by it.

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *The first mention is chapter 4, line 28, in both editions.* Counted on 2026-10-18 with `grep -rn -i "robert\|uncle bob" book/ README*.md`: Robert C. Martin is named in full only at en 04:28 and pt 04:28 (section "The dependency rule", pt "A regra de dependência"); later he is "Martin" (en/pt 04:29, en 04:90, pt 04:92) and in the two source notes. No earlier chapter, the prologue or a README names him. Source: the count.
2. *Only the first mention.* "Robert C. Martin (Uncle Bob) drew the answer in 2012...", pt "Robert C. Martin (Uncle Bob) desenhou a resposta em 2012..."; the later "Martin" stays, since the reader has just met him, and the source notes keep the author's name as published. Source: the request ("the first time"), docs/04 §Writing the book, Teach, do not only show (a name explained where it first appears).
3. *"Uncle Bob" untranslated in Portuguese.* It is the name Portuguese-speaking developers use for him too, and the request's reason is that readers know him by it; "Tio Bob" would be a name nobody searches for. Plain text in parentheses, no italics or quotes, as the request says. Source: the request, ADR-0004 (same content in both editions).
4. *No new source note.* The nickname is the one his own blog files his posts under: the existing note `[^martin-clean-2012]` on the same sentence links to `https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html`, so the reader already has something to open that shows it. A second note would add nothing to open. Source: docs/04 §Writing the book, Source notes ("a note only where the reader gains something to open").
5. *No further introduction of who he is.* The sentence already says what he drew and when; the request asks for the nickname, not a biography. Source: the request, docs/04 (no filler).
6. No new docs/03 term, no new queue line, no split.

**Behaviour.**

* The reader of chapter 4, in either edition, reads at the first sentence that names him: "Robert C. Martin (Uncle Bob) drew the answer in 2012 as concentric circles, ..." (pt "Robert C. Martin (Uncle Bob) desenhou a resposta em 2012 como círculos concêntricos, ..."); the rest of the sentence and its note are unchanged.
* Checked at apply time:
  * `grep -rn "Uncle Bob" book/` prints exactly two lines, en 04 and pt 04, each the sentence above.
  * `grep -rn "Robert C. Martin" book/ README*.md` shows no full-name mention in the text before those lines (source notes excepted).
  * `git diff book/` shows only the one inserted parenthesis per edition.
* Fails: the nickname at a later mention or in a source note; translated in Portuguese; a new source note; any other change to chapter 4; an em dash.

**Contract.**

* Files: `book/en/04-focus.md`, `book/pt/04-focus.md`; the one sentence that first names Robert C. Martin (line 28 at /propose).
* Terms of docs/03: none new. Sources: none added or removed; `[^martin-clean-2012]` unchanged. Cases: none. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* `ch04-focus-optional` edits chapter 4's opening and its gain section; `ch04-scalable-meaning` edits the S of FOCUS (en 04:100, pt 04:102). Neither touches the dependency rule section; whichever lands later finds line 28 by its text, not its number.
* `early-no-forward-links` lists this line (its "en 04:28") and holds no pointer in that sentence; no shared hunk.
* The other M18 lines touch other chapters, the prologue and docs/04.

**Out of scope.**

* Later mentions of Martin and the source notes: decision 2.
* A biography or a new note: decisions 4 and 5.

**Done when.**

* [x] Both editions written: the sentence as Behaviour says.
* [x] Chapter 4 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: none added.
* [x] `make verify` green: edition parity, prose rules, width, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author: left to the driver, who builds the book once at the end of the batch.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block: the page moved here; the driver marks the line `[x]`, stages and commits.

**Proof.** `grep -rn "Uncle Bob" book/` prints two lines, en 04:28 and pt 04:28, each the sentence of Behaviour. `grep -rn "Robert C. Martin" book/ README*.md` shows the full name only at those two lines and in the two source notes. `git diff -- book/en/04-focus.md book/pt/04-focus.md` shows one hunk per edition, the inserted " (Uncle Bob)" only.

`make verify` green: build, parity, em dash, prose, width, links, disclosure. A first run failed on parity in book/pt/01-how-agents-see.md, a file another session of the batch was editing; the rerun was green.

**Divergences.** None.

**Omissions.** None.

**Decisions taken in /apply.** None beyond the page's.

**Review.** Delivery review by a read-only Opus agent on the diff of both chapter 4 files, against the page and docs/04. No findings: one inserted parenthesis per edition, untranslated in Portuguese, no later mention or source note touched, no new note, no em dash, editions in parity.

```commit
docs(ch04-uncle-bob): name Uncle Bob at Robert C. Martin's first mention

- ch 4, both editions: "Robert C. Martin (Uncle Bob)" in the dependency rule

work/done/ch04-uncle-bob.md
```
