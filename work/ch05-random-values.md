# ch05-random-values

**Objective.** A reader of chapter 5 can find, besides the clock, every value that changes from one run of a test to the next without anyone meaning it to, a random value, a new id, the order of a set nobody sorted, the environment the test runs in, and keep each one out of the test's answer, so a test fails only when a rule breaks. Both editions. From the author's reading of the book on 2026-10-18: "'Troque só o I/O e o relógio' (pt 05:44) also covers random values, and any value that may change between test runs without anyone meaning it to (ids, the order of a set, the environment). The heading may change if it no longer says what the section holds; same heading in both editions."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *The heading changes, and keeps its verb.* The section will hold more than the clock, so "Swap only I/O and the clock" no longer says what it holds; it becomes "Swap only I/O and what changes between runs" (pt "Troque só o I/O e o que muda entre execuções"), the same heading in both editions, at the same position. The order of a set is the one value under it that is not swapped, and its paragraph says so in its first words: there is nothing to swap, the code fixes the order it promises or the test does not depend on one. A heading with a new verb ("Keep the answer the same on every run") would drop the swap the section's first paragraph teaches. Source: the draft, docs/04 (a heading says what its section holds).
2. *One frame: these values are I/O, as the clock is.* The section already says "The clock is I/O too: `new Date()` answers something different on every call" (en/pt 05:50). The new text extends that sentence's reasoning: a random value, a new id and a value read from the environment answer differently too, so each is read once where the request arrives, or where the program starts, and handed on as a value, as `today` is (pt `hoje`); the test passes the one it wants. Because they are I/O in the chapter's own sense, these occurrences stay true and stay as they are: en/pt 05:19 ("except the I/O and the clock"), the table's use case row (05:25), and docs/03's `unit test` row (docs/03:73), which lists by example what a test may swap. Source: chapter 5 (05:50-51), chapter 4 (04:199, "The clock is a value"), ADR-0016 (the clock is passed as data), docs/03.
3. *The opening and key point 2 follow the heading.* en/pt 05:3's "what it swaps, only the I/O and the clock" names the broader class in the heading's words ("only the I/O and what changes between runs"), and key point 2 (05:159) says it as a rule: a test swaps only I/O and what changes between runs, each passed in as a value, and asserts no order nobody fixed; it keeps "so most tests fake nothing but the repositories". Every chapter opens with what the reader can do, and a key point says what the reader does. Source: ADR-0015, docs/04 §Writing the book (key points), chapter 5's key points.
4. *An id only as a conditional, written for the chapter.* The lending library's code in chapters 3 to 5 generates no id: `Loan` has no type shown with an id, `lend` returns a loan and `insertLoan(loan: Loan)` saves it. So the id example is said as "if": if `lend` gave each loan a new id with `crypto.randomUUID()`, its test could not say which loan it expects; the id is made where the request arrives, as `today` is, or by the database when it saves. It asserts nothing the existing code does. Source: en 04:145-190, chapter 3, docs/04 (code on the lending library, written for the chapter).
5. *The order of a set on the library.* A member's loans read with no `ORDER BY` come back in whatever order the database finds them, so a test that expects them in the order they were saved can pass today and fail after the data or an index changes; the query states the order it promises, or the test compares them without order. Written for the chapter, on the library, as a sentence, not code. Source: docs/04 (lending library), the draft.
6. *The environment in one sentence.* A value read from the environment, a variable, the time zone, the machine's language, is read once where the program starts and handed on, so a test does not answer differently on another machine. No pointer to a later chapter on configuration or deployment. Source: the draft, work/early-no-forward-links.md (no pointer forward in chapters 0 to 7).
7. *The phenomenon described, not named.* No "flaky" or "non-deterministic test": a name would be a new concept, which goes to docs/03 first, and the description, a test that passes today and fails tomorrow on the same code, says it in fewer words for the reader. Source: the propose skill (a new concept enters docs/03 first), docs/04 (teach, do not only show).
8. *No code block, no source, no number.* Prose with library names in backticks; the section stays short, and chapter 5 already shows `today` passed in. No source note: the reader gains nothing to open for this paragraph that the chapter does not already say. Source: docs/04 Evidence and Code bullets (a note only where the reader gains something to open), the author's style (value first, minimal text).
9. *Gain unchanged.* en/pt 05:151's "the suite runs in seconds and an agent runs it on every change" and 05:153's "'done' is the test runner's output" already presume a suite that gives one answer on the same code; the gain is said once. The author can add half a clause in review. Source: docs/04 §Writing the book, **One gain**.
10. No new docs/03 term, no change to docs/00 to docs/05, no new queue line, no split.

**Behaviour.**

* The reader of chapter 5, in either edition, finds the heading "Swap only I/O and what changes between runs" (pt "Troque só o I/O e o que muda entre execuções") where "Swap only I/O and the clock" was, between "What a fake is" and "One rule through its tests".
* Under it, the first paragraph (05:46-48) and the clock paragraph (05:50-51) stay; after them the reader reads:
  * a random value, a new id and a value read from the environment answer differently from one run to the next, as the clock does, so each is I/O in the same sense;
  * each is read once, where the request arrives or the program starts, and handed on as a value, as `today` is, so the test passes the value it wants and needs no fake;
  * the id said as a conditional on the library: if `lend` gave each loan a new id with `crypto.randomUUID()`, its test could not say which loan it expects (decision 4);
  * the environment: a variable, the time zone, the machine's language, read once where the program starts (decision 6);
  * the order of a set, in its own short paragraph, opening with "there is nothing to swap": a member's loans read with no `ORDER BY` come back in any order, so the query states the order it promises, or the test compares without order (decision 5);
  * why it matters, said once: a test whose answer depends on any of these passes today and fails tomorrow on the same code, and a red test no longer says that a rule broke.
* The opening sentence (05:3) says "only the I/O and what changes between runs" (pt "só o I/O e o que muda entre execuções") in place of "only the I/O and the clock"; key point 2 (05:159) says the same rule and that a test asserts no order nobody fixed.
* The Portuguese edition says the same in the same places, with `hoje`, `emprestar` and "caso de uso" as the chapter has them; library and language names stay as they are (`crypto.randomUUID()`, `Math.random()`, `new Date()`, `ORDER BY`), as docs/04 says.
* Checked at apply time:
  * `grep -n "^## " book/en/05-testing-each-piece.md` and the same for pt list the renamed heading at the same position, between the fake section and "One rule through its tests".
  * `grep -n "I/O and the clock" book/en/05-testing-each-piece.md` prints only 05:19; `grep -n "I/O e o relógio" book/pt/05-testing-each-piece.md` prints only 05:19 (decision 2).
  * `grep -n "I/O and the clock" docs/03-Domain.md` is unchanged (decision 2).
* Fails: a heading that differs in meaning between the editions; the order paragraph presented as something to swap or fake; an id example that says the existing code generates one; "flaky" or "non-deterministic" as a term; a pointer to a later chapter (configuration, deployment, chapter 12 or on); a code block, a source note or a number added; the gain or key points other than 2 changed; any change to 05:9-15 and 05:30-31 (`ch05-test-time`) or to 05:60 and 05:147 (`early-no-forward-links`); an em dash; a run narrated.

**Contract.**

* Files: `book/en/05-testing-each-piece.md`, `book/pt/05-testing-each-piece.md`: the opening sentence (05:3), the section heading (05:44) and a new paragraph or two after 05:51, key point 2 (05:159). Nothing else.
* Terms of docs/03: none new; `unit test`, `fake`, `use case`, `repository` as docs/03 has them; docs/03:73 unchanged (decision 2). Sources: none added or removed. Cases: none; no Ninjobs, Case A or Case B passage. Code: none added (decision 8). Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* `ch05-test-time` adds a clause or short sentence to the opening (05:3-5, its decision 6), text after 05:10 and after 05:30-31, and half a clause to key point 1 (05:158); its Fails line already leaves 05:44-51 to this line. This line changes words inside the first opening sentence (05:3) and key point 2 (05:159): adjacent sentences, not the same ones. Whichever lands later finds the sentences by their text, not their line numbers, and keeps the other's words; if `ch05-test-time` adds its clause to the first opening sentence, this line changes only the "only the I/O and the clock" phrase inside it.
* `early-no-forward-links` edits 05:60 and 05:147 and applies last of M18's lines on chapters 0 to 7; this line adds no pointer forward, so its apply-time grep finds nothing new here.
* `pt-identifiers-choice` and `docs04-code-layout` edit docs/04; this line does not touch docs/04. `pt-ninjobs-masculine` edits articles across `book/pt/`; this line adds no Ninjobs mention.
* The other M18 lines touch other chapters, the prologue and docs/04.

**Out of scope.**

* 05:19, the table and docs/03's `unit test` row: they stay true under decision 2.
* A name for the phenomenon in docs/03: decision 7.
* A code example or a source on test non-determinism: decision 8.
* The gain and the other key points: decision 9.
* Chapter 4's "The clock is a value" (04:199): it says what chapter 4 needs; chapter 5 extends it.

**Done when.**

* [ ] Both editions written: the heading, the new paragraphs, the opening phrase and key point 2 as Behaviour says.
* [ ] Behaviour's apply-time greps print what it says.
* [ ] Chapter 5 still opens with its value, keeps its gain said once, no filler and nothing useful cut.
* [ ] Every number sourced: none added.
* [ ] `make verify` green: edition parity, prose rules, width, links, disclosure scan, no em dash.
* [ ] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [ ] `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.
