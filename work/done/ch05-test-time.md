# ch05-test-time

**Objective.** A reader of chapter 5 can say why an agent's tests make every delivery wait when nobody watches how long they run, and keep the tests every delivery runs fast: use cases tested with data, the slow tests few and run only where they pay, some outside the per-delivery run, by the person, before a milestone closes. Both editions. From the author's reading of the book on 2026-10-18: "Agents write tests and do not care how long they run. If a test is slow and every delivery runs everything, every delivery is delayed. The author has seen agents write tests that took 20 minutes to run: 20 minutes on every delivery. The person is responsible for keeping the tests in order, time included: an extra reason for pure use cases, which are extremely fast to test; integration or E2E tests only where they make sense, or at the end of a milestone."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *Two places the chapter already holds, no new heading.* The cost (agents do not mind run time; a slow suite delays every delivery; the 20 minutes) joins "The problem", after en/pt 05:10, which already says an agent's tests grow "until the suite takes minutes"; it continues that sentence's thought and does not repeat it. The answer (the person keeps the per-delivery run fast; use cases are the fastest tests; end-to-end tests few and only where they pay; some run outside it) joins "A test for each piece", after en/pt 05:30-31, which already says the first three kinds run in seconds and end-to-end tests are few. The section "What tests prove" (05:138-148) is not touched: `early-no-forward-links` guessed this line would land there, as a courtesy (its Deliveries in flight). Source: the draft, chapter 5 as it stands, docs/04 (one fact said once).
2. *The kit as it is today.* /apply runs the project's verify command until green on every delivery, and that command is whatever the person wrote in docs/05's verify slot when /brainstorm or /analyze set it up; the milestone review (docs/05 §8) runs no tests, the person tests each clause by hand. So the chapter says: every delivery runs what verify runs, so what verify runs is the person's decision; the slow tests that verify leaves out run by another command, run by the person, for example before a milestone closes. It does not say the kit or its review runs them; that suggestion is `work/kit-proposals.md` item 1, not this delivery. Source: `.claude/skills/apply/SKILL.md` ("Run verify until green"), `.claude/skills/brainstorm/SKILL.md` step 5, docs/05 §8, the batch rule (the book is the kit today).
3. *The 20 minutes is the author's own observation, said in the first person, no project named, no source note.* It reads as something the author has seen agents write, not as Ninjobs, Case A or Case B, and it carries no footnote. docs/04's Evidence bullet lists three kinds of source and this is none of them, so it gains one clause: "Every number says where it comes from: a primary publication, a record of this book's runs, for a private case, how the author counted it, or the author's own observation on no named project, said as such in the text with no source note (first: `ch05-test-time`)." The author can strike the clause in review and keep the sentence as its own source (docs/04 Voice, first person). Source: the batch rule, docs/04 Evidence and Voice, AGENTS.md (documents are living).
4. *"Milestone" glossed where chapter 5 first uses it.* Chapters 0 to 4 name it once, en/pt 03:246, inside a caution, without saying what it is; chapter 5 does not name it today. The new sentence gives it a few words with the meaning of docs/03's row: a group of deliveries with a paragraph saying what is true when it closes. No pointer to chapter 11 or 15, kind *b* of `early-no-forward-links` decision 5; Portuguese "marco". The bare mention at 03:246 stays as it is, outside this line's files, and is left to the author. Source: docs/03 (`milestone`), `work/early-no-forward-links.md`, the batch rule.
5. *The chapter's own test words.* The draft's "integration or E2E" becomes the chapter's terms: end-to-end tests (pt "testes ponta a ponta"), and, where needed, a repository test against the real engine; docs/03 and docs/04 have no "integration test". Source: chapter 5 (05:19-28), docs/03.
6. *Opening gains one clause.* The ability is new, so en/pt 05:3-5 add, in a clause or a short sentence, that the reader can keep the tests every delivery runs fast and say where the slow ones go. Source: ADR-0015 (the chapter opens with what the reader can do), docs/05 §3.
7. *Gain unchanged.* en/pt 05:151 already says "the suite runs in seconds and an agent runs it on every change"; the new text explains how that stays true, and the gain is said once. Source: docs/04 §Writing the book, **One gain**.
8. *Key point 1 takes half a clause.* It already lists the four tests; it adds that the end-to-end tests are few and the per-delivery run stays fast. No new key point. Source: docs/04 (a key point says what the reader does), chapter 5's key points.
9. *No new number but the 20 minutes; no new source; no code.* "Seconds" and "minutes" in the chapter stay as they are. Source: docs/04 Evidence.
10. No new docs/03 term (`milestone` exists), no new queue line, no split.

**Behaviour.**

* The reader of chapter 5, in either edition, reads in "The problem", after 05:10:
  * an agent writes tests without minding how long they run;
  * every delivery runs the tests, so a slow test makes every delivery wait;
  * the author has seen agents write tests that took 20 minutes to run, 20 minutes on every delivery, said in the first person and naming no project.
* The reader reads in "A test for each piece", after 05:30-31:
  * keeping the tests in order, run time included, is the person's job, not the agent's;
  * this is one more reason to keep rules in pure use cases: their tests are a call with data and the fastest the project has, with no new measure of time;
  * end-to-end tests, and any test that needs the application or a network, are few and written only where they prove something the fast ones cannot;
  * what every delivery runs is the project's verify command, which the person decides; a slow test can stay out of it and run by another command, by the person, for example before a milestone closes;
  * a milestone is said in a few words where it first appears: a group of deliveries with a paragraph saying what is true when it closes.
* The opening (05:3-5) names the new ability once; key point 1 says the end-to-end tests are few and the per-delivery run stays fast.
* A writer opening docs/04 finds the Evidence bullet as decision 3 quotes.
* The Portuguese edition says the same in the same places, with "entrega", "marco", "teste ponta a ponta", "caso de uso" and "verificação" as the chapter has them.
* Fails: the chapter implies the kit or its milestone review runs the slow tests (that is `work/kit-proposals.md`); the 20 minutes with a footnote, as a measured finding, or tied to Ninjobs, Case A or Case B; "milestone" left without its few words, or glossed with a pointer to a later chapter; "integration test" used; 05:10's "until the suite takes minutes" repeated; a second gain; any change to 05:44-51 (`ch05-random-values`) or 05:138-148 (`early-no-forward-links` edits 05:147); an em dash; a run narrated.

**Contract.**

* Files: `book/en/05-testing-each-piece.md`, `book/pt/05-testing-each-piece.md`: the opening (05:3-5), "The problem" (pt "O problema") after 05:10, "A test for each piece" (pt "Um teste para cada peça") after 05:31, key point 1 (05:158); `docs/04-Conventions.md`: the Evidence bullet (docs/04:23 at /propose).
* Terms of docs/03: none new; `milestone`, `delivery` and `queue` as docs/03 has them. Sources: none added or removed; the 20 minutes is the author's observation (decision 3). Cases: none; no Ninjobs, Case A or Case B passage. Code: none added. Exercises: none (ADR-0017).
* docs/00, docs/01, docs/02, docs/03, docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* `ch05-random-values` edits "Swap only I/O and the clock" (05:44-51) and may rename its heading; this line adds nothing there, and the reason for pure use cases lands at 05:30-31, not at 05:48. No shared hunk.
* `early-no-forward-links` edits 05:60 and 05:147 to drop pointers and applies after this line (its decision 8); this line adds no pointer forward, so its apply-time grep finds nothing new here. Its guess that this line lands near 05:138-148 is superseded by decision 1.
* `pt-identifiers-choice` edits docs/04:28 and 50; this line edits docs/04:23, a hunk apart. `docs04-code-layout` edits docs/04's code rule, another hunk; whichever lands second reads docs/04 as the first left it.
* The other M18 lines touch other chapters, the prologue and other lines of docs/04.

**Out of scope.**

* A kit rule on test time, or the milestone review running tests: `work/kit-proposals.md` item 1 (decision 2).
* The bare "milestone" at 03:246: another chapter, left to the author (decision 4).
* "What tests prove" and the gain: decisions 1 and 7.
* A study or number on test suite time: decision 9.

**Done when.**

* [x] Both editions written: the opening, the two sections and key point 1 as Behaviour says.
* [x] docs/04's Evidence bullet as decision 3 quotes.
* [x] Chapter 5 still opens with its value, keeps its gain said once, no filler and nothing useful cut.
* [x] Every number sourced: the 20 minutes said as the author's own observation.
* [x] `make verify` green: edition parity, prose rules, width, links, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunks of docs/04 and docs/06, commit message in a `commit` block.

**Proof.**

* en/pt 05:5 (opening), 05:11-12 ("The problem"), 05:33-38 ("A test for each piece") and key point 1 read as Behaviour says, with the wordings of Divergences; docs/04:23 as Divergences says.
* `git diff --stat` on the three paths: 23 insertions, 3 deletions; 05:44-51 and 05:138-148 untouched.
* `make verify`: build, parity, em dash, prose, width, links and disclosure green, exit 0.
* `make book`: not run here; the driver builds the book once at the end of the batch and gives both PDF paths.

**Divergences.** Review wordings on text this delivery wrote, kept to the page's intent:

* The new opening sentence sits before "And you know why...", so the opening still ends on that line.
* "every delivery runs the tests, so" became "when every delivery runs the tests,": 05:10 says a slow suite goes unrun, and the new line reads as the case where it runs.
* End-to-end tests "are few" is not said again: 05:31 says it, and docs/04 says a fact once; the new line says they are written only where they prove what the fast ones cannot.
* The milestone gloss is its own sentence; pt "o agente não faz isso se você não pedir"; pt key point 1 "então o que toda entrega roda continua rápido", since "espera" also reads as "expects".
* docs/04's Evidence bullet separates its four sources with semicolons, not the commas decision 3 quotes, so "for a private case, how the author counted it" stays one item.

**Decisions taken in /apply.**

* "Verify" is glossed where it first appears in the chapter as the command that must pass before a delivery is called done, the words of en/pt 00:96-97.
* Run in a batch of applies on one tree: the driver marks this line in docs/06, runs `make book` once at the end of the batch, and stages and commits this delivery by its paths.

**Review.** One read-only agent on Opus read the diff of the three paths against this page and docs/04, with chapters 0 to 5 in both editions: nothing breaks the page; two near-breaks (05:11 against 05:10, "few" said twice) and six wordings, all applied (Divergences).

```commit
docs(ch05-test-time): keep the tests every delivery runs fast

- Chapter 5, The problem: an agent does not mind how long a test runs; the author has seen tests of 20 minutes on every delivery
- Chapter 5, A test for each piece: the person keeps the tests in order; use cases are the fastest tests; slow tests stay out of verify and run by the person, for example before a milestone closes
- Chapter 5, opening and key point 1
- docs/04, Evidence: the author's own observation on no named project, said as such, with no source note

work/done/ch05-test-time.md
```
