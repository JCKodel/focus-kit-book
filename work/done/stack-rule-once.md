# stack-rule-once

**Objective.** A reader learns how to choose a stack by what the agent knows, with the Flutter lesson that proves it, in one place, chapter 9 §Choosing the stack, and meets it in chapters 6 and 22 only as the story's fact and a pointer, in both editions. Found by `m15-review` (work/done/m15-review.md, A9 and B8: "the stack rule and the Flutter story in 6, 9 and 22. Seen.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. Which chapter owns the rule and its lesson: chapter 9 §Choosing the stack. It holds the three questions, the Octoverse source, and sits where the doubt is born, at `/brainstorm`'s third subject (docs/04 §Say it where the doubt is born; AGENTS.md "a rule said once in the chapter that owns it"). Chapter 6 calls it "one lesson beyond the process", so it is not one of the kit's rules that chapter 6 says it teaches (its line 4). Chapter 22 owns the cost, not the choice. Source: docs/04, chapters 6, 9 and 22 as they stand.
2. What in chapter 6 is not the duplicate and stays: cause 2 of §What went wrong (Material 3, few examples in training, guessed pixel values) and §Where it went's "moved the app from Flutter to React". They are the five causes the decision record named and the restart's narrative, the chapter's one story (the author's rule that a case chapter tells one story: how it was, what went wrong, where it went, chapter 6's own headings; `ch03-opening` leans on §What went wrong staying whole). What goes: §Pick a stack the agent knows well (en 70-74, pt 70-74), which retells the outcome and restates the rule, and key point 4 (en and pt 87), the rule again. Source: chapter 6, the author's rule for case chapters.
3. Where chapter 6 points to chapter 9: inside line 38's sentence, which already says something (the move to React), as a parenthesis; never a sentence that is only a pointer (docs/04 §Teach, do not only show). The outcome "in React the same agent got the design right", now only in the cut section, moves into that sentence so no fact is lost. Source: docs/04.
4. Chapter 9 line 45 stays and takes the one nuance only chapter 6 carried: Flutter could build the product, and what the agent had seen was the limit. That is what separates question 2 from question 1. No pointer back to chapter 6: a reader in order has read it, and docs/04 §Chapter pointers cuts a pointer back that only repeats. Source: docs/04, chapter 6:74.
5. Chapter 22 keeps its own claim, "it does not pay on a stack the agent has seen too little of", the cost of each attempt (tokens and a person's review, no finished screen) and the conclusion that the choice is a cost decision; it drops the retelling of line 78 (pixel values, few examples, screen after screen) and points to chapter 9 once, where the sentence leans on its questions (docs/04 §Chapter pointers: a pointer back that leans on a specific detail). Key point en 106 / pt 107 states chapter 22's claim, not the story, and stays. Source: chapter 22, docs/04.
6. Pointer form: the chapter's own, `(chapter 9)` / `(capítulo 9)`, as chapter 6 writes all its pointers and chapter 22 its line 61; docs/04 §Chapter pointers names no form. Source: docs/04, chapters 6 and 22. In chapter 22 the pointer is part of the sentence, "by the questions of chapter 9" / "pelas perguntas do capítulo 9", as Behaviour writes it, because the sentence leans on those questions.
7. pt chapter 9 line 45's "Na Ninjobs" becomes "No Ninjobs", the form the three chapters use five times, since the line is rewritten anyway. Source: book/pt 6, 9, 22.
8. No docs/03 term (stack is no term of the book's vocabulary) and no split: three chapters, one fact, one page. Source: docs/03, docs/05 §1.
9. At /apply: Behaviour's chapter 22 sentence joins old lines 78 and 79 into one ("that stack was Flutter: each attempt at the design cost tokens..."), while the Contract called line 79 unchanged. Behaviour's text is what the reader reads, so it was followed: line 79's claim stays word for word inside the new line 78, and old line 80 is now line 79. Source: this page.

**Behaviour.**

* A reader of chapter 6 reads the five causes as before, cause 2 whole, and in §Where it went: "On 2026-08-29 I started over, with a process small enough to hold in my head, and moved the app from Flutter to React, where the same agent got the design right (chapter 9 turns that into how to choose a stack)." (pt: "Em 2026-08-29 eu recomecei, com um processo pequeno o bastante para caber na cabeça, e mudei o app de Flutter para React, onde o mesmo agente acertou o design (o capítulo 9 transforma isso em como escolher uma stack).") /apply may polish within these limits: one sentence, the outcome kept, the pointer inside it.
* Chapter 6 has no §Pick a stack the agent knows well (pt §Escolha uma stack que o agente conhece bem); §Each rule and its failure is followed by §What the team gains; its key points are three, the first three as they stand.
* A reader of chapter 9 §Choosing the stack reads at line 45: "On Ninjobs the same agent kept missing the design in Flutter, where it had few examples of a customised design system to learn from, and got it right in React: Flutter could build the product, and what the agent had seen was the limit." (pt: "No Ninjobs, o mesmo agente errava o design no Flutter, onde tinha poucos exemplos de um design system customizado para aprender, e acertava no React: o Flutter conseguiria construir o produto, e o limite era o que o agente tinha visto.") The rest of the section, the Octoverse sentence and its note, and key point 3 stay.
* A reader of chapter 22 §Where an agent pays reads (pt in parentheses):
  * "**It does not pay** on a stack the agent has seen too little of." (unchanged; "**Ele não compensa** numa stack que o agente viu pouco.")
  * "On Ninjobs, before the method, that stack was Flutter: each attempt at the design cost tokens and a person's review, and neither bought a finished screen." ("No Ninjobs, antes do método, essa stack foi o Flutter: cada tentativa no design custou tokens e a revisão de uma pessoa, e nenhum dos dois comprou uma tela pronta.")
  * "Choosing a stack by the questions of chapter 9 is a cost decision as much as a technical one." ("Escolher uma stack pelas perguntas do capítulo 9 é uma decisão de custo tanto quanto técnica.")
* Checked, both editions, on chapters 6, 9 and 22: `grep -n -i "pixel"` finds only chapter 6's cause 2; `grep -n "Material 3"` only chapter 6; `grep -n -i "Choose a stack\|Escolha uma stack"` only chapter 9's key point; `grep -n -i "seen in training\|visto no treinamento"` only chapter 6's cause 2; `grep -c -i flutter` gives 3 lines in chapter 6 (20, 22, 38), 1 in chapter 9, 1 in chapter 22, per edition.
* `grep -rn -i "pick-a-stack\|escolha-uma-stack" book mkdocs.yml` finds nothing before and after (checked at /propose: no link reaches the cut heading).
* Fails: one edition changed and not the other; cause 2 or the move to React cut from chapter 6; a pointer that stands as a sentence of its own; the Octoverse number or note lost from chapter 9; chapter 22 without its cost claim; a pixel, Material 3 or training detail left in chapter 9 or 22 beyond line 45's "few examples"; a second pointer to chapter 9 in chapter 22.

**Contract.**

* Files: `book/en/06-birth-of-focus-kit.md`, `book/pt/06-birth-of-focus-kit.md`, `book/en/09-starting-a-project.md`, `book/pt/09-starting-a-project.md`, `book/en/22-cost-and-where.md`, `book/pt/22-cost-and-where.md`; no other file.
* Sections and lines (same in both editions unless said): chapter 6 §Where it went line 38, §Pick a stack the agent knows well lines 70-75 removed with its blank line, §Key points line 87 removed; chapter 9 §Choosing the stack line 45; chapter 22 §Where an agent pays lines 78 and 80 (line 77, line 79 and key point en 106 / pt 107 unchanged).
* Terms of docs/03: none new. Sources: unchanged; Octoverse stays in chapter 9; no note added or removed. Cases: Ninjobs only, its published facts as today; no Case A or Case B passage. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line `[>]` by the driver, `[*]` when /apply starts, `[x]` by /apply. No new queue line.
* Gains untouched: chapter 6 keeps its gain and three key points; chapter 22's gain is unchanged, so `one-gain-section` is not reopened.

**Deliveries in flight on the same chapters.**

* `line-rule-once` (`[ ]`): chapter 22 line 61, §Why the page and the documents keep sessions small; no line in common.
* `ch03-opening` (`[ ]`): reads chapter 6 §What went wrong, which this page leaves whole.

**Out of scope.**

* Chapter 6's five causes and the rest of §Where it went: the story, told once.
* Chapter 9's three questions, the Octoverse number and its note: the rule as it stands.
* Chapter 22's token table and its other sections: not the finding.
* Chapter 4's BLoC sentence: names Flutter as a stack, not the story.

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the counts it names.
* [x] Chapters 6, 9 and 22 still open with their value, keep their gain, no filler and nothing useful cut.
* [x] Every number still sourced; `make verify` green, disclosure scan included; no em dash.
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Divergences.**

* The training grep, `seen in training\|visto no treinamento`, finds nothing in any of the three chapters, because cause 2 says "had seen few examples of that in training" / "tinha visto poucos exemplos disso no treinamento". `grep -n -i "training\|treinamento"` finds only chapter 6's cause 2 (line 22) in both editions, which is what the check meant.
* `grep -n -i "Choose a stack"` in English also matches chapter 9's opening line 4 ("You can also choose a stack..."), besides key point line 131; it is chapter 9 alone, as the check meant. Portuguese finds only line 131.

**Proof.**

* Greps, both editions, chapters 6, 9 and 22: "pixel" and "Material 3" only in chapter 6 line 22; "Choose a stack" / "Escolha uma stack" only in chapter 9; Flutter on lines 20, 22 and 38 of chapter 6, line 45 of chapter 9, line 78 of chapter 22.
* `grep -rn -i "pick-a-stack\|escolha-uma-stack" book mkdocs.yml` run again at /apply, before and after the edit: no match, so no link reached the removed heading.
* `make verify` green (strict build, parity, em dash, prose, links, disclosure). `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* No Case A or Case B passage touched; Ninjobs only through facts the chapters already published.

**Review.** A read-only Opus agent read this delivery's diff against this page and docs/04. Chapter checks all passed: both editions mean the same, cause 2 and the move to React kept, the pointer inside a sentence, line 45's nuance, one pointer in chapter 22, no em dash, nothing breaking docs/04. Findings: the docs/06 line was still `[*]` and unstaged at review time (it is /apply's last edit, done after the review); decision 6 did not describe chapter 22's pointer form (fixed above); an optional rewording of pt chapter 22 "cada tentativa no design" (kept: it is Behaviour's text and reads correctly). No new queue line.

```commit
docs(stack-rule-once): tell the stack rule once, in chapter 9
- ch 6: drop §Pick a stack and its key point; line 38 keeps the outcome
- ch 6: point to chapter 9 inside the sentence on the move to React
- ch 9: line 45 says Flutter could build it and what the agent saw was the limit
- ch 22: keep the cost claim, drop the retold story, lean on chapter 9
- both editions; pt chapter 9 now "No Ninjobs"
work/done/stack-rule-once.md
```
