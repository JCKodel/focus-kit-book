# ch21-counts-once

**Objective.** A reader of chapter 21 meets each count once, finds in its gain the one number that sums the chapter, and learns the pending-deletion story in chapter 13, the chapter that owns it, through a pointer from chapter 21's data rules, in both editions. Found by `m15-review` (work/done/m15-review.md, B5: "21:67-69: the pending-deletion story of 13:188-189 retold. Seen."; B10: "21:59, 87: one fact in two numbers, and a gain with three counts. Seen."; the line numbers were those of the review, before `code-width` moved them by four).

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The gain's one number is Case A's: about 16 of its 73 done lines were questions to people or documents. It sums the chapter's claim, one process for every kind of work, across two of the chapter's kinds of non-code work, and Case A is the chapter's main story. A pair is not used: docs/04 **Numbers that prove** allows a pair only for a comparison (before and after, a result and its cost), and Case A against Ninjobs is neither. Source: docs/04 **Numbers that prove** and **One gain**; the queue line.
2. The one fact said in two numbers ("8 were questions to people and about eight were documents" in §Case A's documents, "about 16 of its 73" in the gain) is said once, in the gain; the body sentence with the split is cut, and the precise count "8 questions" leaves the chapter. The author may want the split back; it would then replace the gain's number, not sit beside it. Source: docs/04 **Numbers that prove** ("one fact said in two numbers" stays at the source).
3. Ninjobs' "six of its 93 finished pages changed only database rules" stays once, in §Data work as deliveries, where it is the evidence that data rules are deliveries, and leaves the gain. Source: docs/04 **Say it where the doubt is born** and **One gain**.
4. The gain's Case B sentence is cut, not reworded without numbers: §Case B tells the story with its counts and the last key point carries the lesson, so a numberless retelling in the gain would tell the story twice. Source: AGENTS.md batch goal (a story told once in the chapter that owns it); docs/04 **One gain**.
5. §Data work keeps what is chapter 21's own: the rule existed, an access rule enforces it in the database itself, and the project's test of the access rules proves it, which is what the section's closing sentence and its key point lean on. What is chapter 13's goes: the first version of the rule, what the build found about a table with no write rule, the refinement and the page recording why. The rule is named once, in its final form (the client cannot write while an account deletion is pending), so no before and after survives. Source: m15-review B5; chapter 13 §What the team gains; docs/04 **Chapter pointers**.
6. The pointer is a link inside that sentence, `[chapter 13](13-apply.md)` / `[capítulo 13](13-apply.md)`, the form chapters 16, 17, 20 and 23 use; it follows a clause that already says something, so it is not a sentence that is only a pointer. Chapter 21's plain "(chapter 20)" elsewhere is untouched. Source: docs/04 **Chapter pointers** and **Teach, do not only show**.
7. Key points are unchanged: they carry no count today. Source: chapter 21 §Key points; docs/04 **One gain**.
8. No docs/03 term, no new queue line, no split: one chapter, four sentences per edition. Source: docs/03 (`team gain` exists); docs/05 §1.

**Behaviour.** In both editions of chapter 21 (`book/en/21-beyond-software.md`, `book/pt/21-beyond-software.md`), after /apply:

* §Case A's documents (pt §Os documentos do Caso A): the sentence "Of Case A's 73 done lines, 8 were questions to people and about eight were documents." (pt "Das 73 linhas concluídas do Caso A, 8 foram perguntas a pessoas e cerca de oito foram documentos.") is gone; the paragraph ends with the question delivery's page and its "(chapter 20)" / "(capítulo 20)" as now.
* §Data work as deliveries (pt §Trabalho com dados como entregas): the two sentences from "One of them was the rule" to "and the page recorded why." (pt from "Uma delas foi a regra" to "e a página registrou por quê.") become one, close to:
  * en: "One of those rules stops the client from writing while an account deletion is pending; it lives in the database itself, as an access rule, and the project's test of the access rules proves it ([chapter 13](13-apply.md) tells what its build found)."
  * pt: "Uma dessas regras impede o cliente de escrever enquanto a exclusão de uma conta está pendente; ela mora no próprio banco de dados, como uma regra de acesso, e o teste das regras de acesso do projeto a prova (o [capítulo 13](13-apply.md) conta o que a construção dela encontrou)."
  The sentences before ("six of its 93 finished pages") and after ("A rule in the database holds for every client ...") stay.
* §What the team gains (pt §O que o time ganha): the first sentence stays; the second and third become one, close to:
  * en: "On Case A, about 16 of its 73 done lines were questions to people or documents, and each went through the same two commands as its code." (built as "as the project's code", review finding 1)
  * pt: "No Caso A, cerca de 16 das suas 73 linhas concluídas foram perguntas a pessoas ou documentos, e cada uma passou pelos mesmos dois comandos que o seu código."
* Checks a person runs, each per edition: `grep -c "73" ` on chapter 21 gives 1, in the gain; `grep -c "93"` gives 1, in §Data work; "six faults" / "seis falhas" and "at least one" / "pelo menos um" appear once each, in §Case B; `grep -c "13-apply.md"` gives 1; "blanket" / "regra geral" and "no write path reachable" / "nenhum caminho de escrita" give 0; heading count and levels equal in both editions and unchanged; key points unchanged.
* Fails: one edition changed and not the other; any count left in two places of the chapter; the gain with more than one number; §Data work losing that the rule is enforced in the database and proven by a test; the first version of the rule or what the build found left in chapter 21; a pointer standing as a sentence of its own; any edit to chapter 13.

**Contract.**

* Files: `book/en/21-beyond-software.md`, `book/pt/21-beyond-software.md`; no other book file. Chapter 13 is read, never edited.
* Sections: §Case A's documents (one sentence cut), §Data work as deliveries (two sentences become one, with the link), §What the team gains (two sentences become one). Headings unchanged.
* Terms of docs/03: none new; `team gain` used as defined. Sources: none added or removed (chapter 21 has no note on these passages; private cases carry none, docs/04). Cases: Case A (gain), Case B (gain sentence cut), Ninjobs (paraphrased, no infrastructure beyond what the chapter already says).
* docs/00 to docs/05: no change. docs/06: this line `[>]` by the driver, `[*]` when /apply starts, `[x]` by /apply. No new queue line.

**Deliveries in flight on the same chapters.**

* `code-width` and `pt-placeholders` (`[x]`): touched chapter 21's code block and pt placeholder; not these sentences.
* `ch13-delivery-review` (`[ ]`): will edit chapter 13. The pointer targets the file, not a heading or a line, so it holds through any rewording of chapter 13's gain; if that delivery moved the pending-deletion story out of chapter 13, the pointer would need the new place, and that delivery's /propose should check it.
* Other sessions' pages and files in the tree are theirs (docs/05 §4). Find passages by their words, not by line numbers.

**Out of scope.**

* Chapter 13: the owner of the story, as it stands.
* The Case A gloss and the list of Case A's documents: the chapter's own evidence, not the finding.
* §Case B's counts and story: said once there already.
* Other chapters' use of the same counts: no finding names them.

**Done when.**

* [x] Both editions changed as Behaviour says; its checks give the results it names.
* [x] Chapter 21 still opens with its value, has its gain, no filler and nothing useful cut.
* [x] Every number still sourced; `make verify` green, parity, width and disclosure scan included; no em dash.
* [x] The author approves the rewritten Case A gain sentence and the cut Case A and Case B sentences, both editions (docs/00 OD-3); the passages are listed under Case A and Case B passages. Pending: the author's reading at the end of the batch.
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Case A and Case B passages, for the author's approval (docs/00 OD-3).**

* Cut, en: "Of Case A's 73 done lines, 8 were questions to people and about eight were documents." pt: "Das 73 linhas concluídas do Caso A, 8 foram perguntas a pessoas e cerca de oito foram documentos."
* Cut, en: "Case B shows what a page would have saved: its analysis had none, and at least one of its six faults reached the next version of the proposal." pt: "O Caso B mostra o que uma página teria poupado: a sua análise não teve nenhuma, e pelo menos uma das suas seis falhas chegou à versão seguinte da proposta."
* New, the gain's sentence quoted in Behaviour, both editions.

**Done.**

* Built: en and pt chapter 21, as Behaviour says (the gain ends "as the project's code" / "que o código do projeto", review finding 1): the Case A split sentence cut in §Case A's documents; the two pending-deletion sentences of §Data work as deliveries made one, with the link to chapter 13; the gain's second and third sentences made one, Case A's count only. Chapter 13 untouched.
* Checks, each edition: "73" 1 (gain), "93" 1 (§Data work), "13-apply.md" 1, "six faults" / "seis falhas" 1 and "at least one" / "pelo menos um" 1 (§Case B), "blanket" / "regra geral" 0, "no write path reachable" / "nenhum caminho de escrita" 0; 9 headings in each, unchanged; key points unchanged.
* Proof: `make verify` green (build, parity, em dash, prose, width, links, disclosure); `make scan` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* Divergences: none. Omissions: none.
* Case A and Case B passages: listed above; the author's approval is pending his reading of the whole book at the end of the batch (docs/00 OD-3), so that Done when item is ticked on that understanding.

**Delivery review.** A read-only agent on Opus read `git diff` and `git diff --cached` of the two chapter files, this page and this line's hunk of docs/06 against this page, docs/04 and AGENTS.md. The three edits match Behaviour in both editions, the checks give the named results, the pointer leans on a clause and chapter 13 is untouched and still holds the story. Nothing breaks the page, docs/04 or this delivery's lines.

1. en/pt gain: "as its code" / "que o seu código" was ambiguous, since questions and documents have no code of their own. Fixed: "as the project's code" / "que o código do projeto".
2. en/pt §Case A's documents: the question-delivery paragraph now carries no Case A number of its own. This is decision 2; left for the author's reading, no change and no queue line.
3. This page: the approval item is ticked while the approval is pending. That is the batch's rule; it says so in the item. No change.
4. en/pt §Case A's documents: the Case A gloss names the platform. The text predates this delivery and is out of scope; the author confirms it in his reading. No change and no queue line.

**Commit.**

```commit
docs(ch21-counts-once): give chapter 21 each count once

- Cut the Case A split sentence; its count lives in the gain
- Make the gain one sentence with Case A's one number
- Point to chapter 13 for the pending-deletion story
- Both editions

work/done/ch21-counts-once.md
```
