# agent-never-unsure

**Objective.** A reader of chapter 1 can explain that a coding agent answers what is not in its context window with the same assurance as what is, from its training or from invention, rarely saying it does not know, so a confident answer is a hypothesis until the person's judgment checks it against the project. From the author's reading of the book on 2026-10-18: "An agent never says 'I don't know'. It says what it does not know with the same assertiveness as what it knows. [...] A hypothesis is not always true. Human judgment is still the IT professional's main asset."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *Chapter 1, a new section.* The passage goes in chapter 1 as a section of its own, `## What is not in the window` (pt: `## O que não está na janela`), between `## When the window fills` and `## What this changes in your project`. Chapter 1 already teaches that the model sees only its window; what it does with a fact that is not there is the next question, and the one the author marked. Source: the draft, which names chapter 1 first; en 01:3-16 (the model knows only what is sent).
2. *Each chapter keeps its part; nothing said twice.* Chapter 1 says the behaviour and its cause. The prologue keeps the role (en 00:54, "the person interprets, guides and validates, and trusts no one blindly"), chapter 24 keeps the remedy (turn 2, "Test each one and show me the result", en 24:40-45, and the limit an agent claims without testing, en 24:87-90), and chapter 0 keeps the failure "The agent fills gaps with guesses" (en 00:72-74). The new section neither restates the challenge protocol nor redefines the role; it ends on the person's judgment in one sentence. Source: docs/04 §Writing the book (one fact said once), the draft.
3. *No forward pointer in the body.* The section does not send the reader to chapter 24; where it needs the remedy, it says it in a few words ("ask it to test the claim and show the result"). Source: `early-no-forward-links`, the rule the author set for chapters 0 to 7 on 2026-10-18; docs/04 §Chapter pointers.
4. *Evidence.* "Never says 'I don't know'" is the author's observation and is said as his, in the first person, softened to what the book can stand behind ("in my work with agents, I have rarely seen one say it does not know"), since no source proves "never". The cause is sourced: Kalai, Nachum, Vempala and Zhang, "Why Language Models Hallucinate", 2025, <https://arxiv.org/abs/2509.04664>, which argues that training and evaluation reward a guess over admitting uncertainty, as a test taker who guesses scores more than one who leaves the answer blank. /apply quotes the paper from its own text, read at apply time; the /propose session saw only its abstract. Source: docs/04 §Evidence, the prologue's rule on opinion and evidence (en 00:47-49).
5. *Plain words, no new docs/03 term.* The section says what the model does ("answers with the same assurance", "a guess", "a hypothesis") and does not introduce "hallucination" as the book's term: the word appears only in the paper's title in the note. A docs/03 row would name a concept no other chapter uses. Source: docs/03 (no row for it; `sycophancy` is the nearest, and stays chapter 24's), docs/04 §Writing the book (explain the basics for non-developers).
6. *Opening, key point and gain.* The chapter's opening sentence (en 01:4) gains the new ability, so the chapter still opens with everything it teaches; one key point is added. The gain section is unchanged: what the team gains, decisions in files read whole, already covers the practice; the section's lesson is the person's judgment, which the prologue's role carries. Source: ADR-0015, ADR-0017, docs/04 §A gain per chapter.
7. *The three ways an agent answers what it does not know*, from the draft, in this order: it states a guess as fact; it answers from what the model learned in training, which may have nothing to do with this project (an API of another version, a convention of another codebase); rarely, it says, often in passing, that it is not sure and proposes a way to gather evidence for its hypothesis. Source: the draft.
8. No new queue line, no split, no change to chapter 24 or the prologue.

**Behaviour.**

* The reader of chapter 1, in either edition, reads after "When the window fills" a section that says:
  * the model writes the most likely next text, from its window and from what it learned in training, and writes it whether or not the fact was in the window;
  * so it says what it does not know with the same assurance as what it knows, and the author has rarely seen one say "I don't know";
  * the three ways of decision 7;
  * why: training and evaluation reward a guess over "I don't know" (Kalai et al., 2025, quoted, with a footnote);
  * a hypothesis is not always true, and nothing in the answer's tone tells it from a fact; the person's judgment does, by checking it against the project's files or asking the agent to test it and show the result.
* The chapter's opening sentence names the new ability: why the agent's answer sounds as sure when the fact was not in its window.
* A new key point, in both editions: an agent answers what is not in its window with the same assurance as what is, so a confident answer is a hypothesis until the person checks it.
* The Portuguese edition says the same with the same section, the same note and the same key point; the quote from the paper is translated in the text, as the chapter's other quotes are, and the note keeps the English title.
* Fails: a forward pointer to chapter 24 in the body; the challenge protocol restated; "never" stated as the paper's finding instead of the author's observation; "hallucination" used as the book's term in the body; a number added without a source; any change outside chapter 1 of both editions; an em dash; a run narrated.

**Contract.**

* Files: `book/en/01-how-agents-see.md`, `book/pt/01-how-agents-see.md`. In each: the opening sentence (line 4), one new section between `## When the window fills` and `## What this changes in your project`, one key point, one footnote (`[^kalai-2025]`: Adam Tauman Kalai, Ofir Nachum, Santosh S. Vempala and Edwin Zhang, "Why Language Models Hallucinate", 2025. <https://arxiv.org/abs/2509.04664>).
* Terms of docs/03: none new (decision 5). Sources: one added, Kalai et al. 2025. Cases: none; the author's own observation, no Case A or Case B passage. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.** `early-no-forward-links` edits chapters 0 to 7 of both editions, chapter 1 included, to replace forward pointers with a few words; its likely hunks in chapter 1 are en 01:83 and 01:89 (`What this changes in your project`), apart from this delivery's new section, opening sentence and key point. This delivery adds no forward pointer (decision 3), so it follows that delivery's rule in either order; whichever lands second reads the other's chapter 1 before editing. `case-a-why-anonymous` edits the prologue only; `pt-ninjobs-masculine` edits Portuguese uses of Ninjobs, none in chapter 1. The other M18 lines touch chapters 2 to 13 and docs/04.

**Out of scope.**

* Chapter 24 and the prologue: they keep the remedy and the role (decision 2).
* A docs/03 term for hallucination: decision 5.
* A measurement of how often agents say they do not know: the book has no run for it, and the observation is the author's.

**Done when.**

* [x] Both editions written: the section, the opening sentence, the key point and the note, as Behaviour and Contract say.
* [x] The paper quoted from its own text, read at apply time.
* [x] Chapter 1 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: none added.
* [x] No forward pointer in the new section; the protocol not restated.
* [x] `make verify` green: edition parity, prose rules, width, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author: by the batch driver, once at the end of the batch.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block: the page moved and the message below by /apply; the mark, staging and commit by the batch driver.

**Proof.**

* en/pt 01:4 opening sentence gains "why its answer sounds just as sure when a fact was not in the window"; en/pt 01:61-77 the new section `## What is not in the window` (`## O que não está na janela`), between `## When the window fills` and `## What this changes in your project`; one new key point, the fourth; `[^kalai-2025]` added at the end of both editions, as the Contract writes it.
* The paper read at apply time, from its arXiv HTML (v1, 2025-09-04): the abstract says "the training and evaluation procedures reward guessing over acknowledging uncertainty" and "guessing when uncertain improves test performance"; section 1.2 says a binary 0-1 scheme "awards 1 point for a correct answer and none for blanks or IDKs". The chapter quotes the first two and paraphrases the third, each with the note.
* "Hallucinat" appears in chapter 1 only in the note's title, in both editions; no link to chapter 24 in the new section.
* `git diff --stat` on the two paths: 21 insertions, 1 deletion each.
* `make verify`: build, parity, em dash, prose, width and disclosure green; the link check fails only on en/pt 24:159, a web.archive.org URL in chapter 24 that this delivery did not touch, refused by the network from this machine (curl gets no answer either); every other link, the new arXiv one included, passes.

**Divergences.** None from Behaviour. The opening sentence puts the new ability after "why a long session gets worse", in the order the chapter teaches it.

**Decisions taken in /apply.**

* Run in a batch of applies on one tree: the batch driver marks this line in docs/06, runs `make book` once at the end of the batch and gives both PDF paths, and stages and commits this delivery by its paths.
* The body names the authors and the year, not the paper's title, so "hallucination" stays in the note only (decision 5).
* The pt quotes translate "guessing" as "palpite"/"dar um palpite", the word the section already uses for a guess, not "chutar".

**Review.** One read-only agent on Opus read the diff of the two paths against this page and docs/04: nothing breaks the page or docs/04; quotes match the paper. Three suggestions on text this delivery wrote, all applied: the sentence on how most tests score a model takes its own `[^kalai-2025]` marker; the opening sentence says "just as sure" ("igualmente segura"); pt "esteja ou não na janela o fato de que ele precisa" and "a hipótese dele" for the ambiguous "a sua hipótese". No queue line.

```commit
docs(agent-never-unsure): say an agent answers what is not in its window as surely as what is

- Chapter 1, new section "What is not in the window": the model writes the likeliest text whether or not the fact was in the window; three ways an agent answers what it does not know; why, from Kalai et al. 2025; a confident answer is a hypothesis the person checks
- Chapter 1, opening sentence and a new key point say the same; new source note [^kalai-2025]

work/done/agent-never-unsure.md
```
