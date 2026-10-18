# ch12-review-skill

**Objective.** A reader of chapter 12 §What the team gains learns that on Case A every kind of work, code, questions to the client and handover documents, was reviewed the same way, by reading its page, with no mention of a "review skill" the kit does not have (focus-kit 2026.10.17 installs four skills: brainstorm, analyze, propose, apply); both editions. Found by `m15-review` (work/done/m15-review.md, B26: "en 12:141, pt 12:148: \"one review skill\" that does not exist. Seen.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The clause is reworded, not cut: it keeps the gain's point that one page, read the same way, reviews every kind of work, which is what chapter 21's gain says ("the same queue, the same page and the same review carry code, documents, questions and data rules", en line 90). Cutting the clause would leave the Case A sentence without the gain it proves. Source: the finding B26, chapter 21 §What the team gains, docs/04 §Chapter shape (one gain section per chapter, said once).
2. The new wording names no skill, command or kit artifact: "reviewed the same way, by reading its page". The installed skills are brainstorm, analyze, propose and apply (`.claude/skills/`, focus-kit 2026.10.17), and the book teaches the kit as it is today (the batch's brief). Whether Case A once had something called a review skill does not matter here: the chapter teaches today's kit, and the sentence's point is the page.
3. The sentence does not point to the delivery review or the milestone review. Those are taught by `ch13-delivery-review` (chapter 13) and `ch15-review-by-areas` (chapter 15) in M16; pointing to them from chapter 12 would take their scope and depend on text not yet written. Source: docs/06 M16, the batch's brief.
4. "(chapter 21)" stays as plain text, as it is now; the sentence's other words around it stay byte for byte. Source: chapter 12 as it stands; docs/04 §Chapter pointers is not touched by this finding.
5. Portuguese uses "revisar" and "revisão" as docs/03 does ("review" is "revisão" in its rows); "skill" disappears from the sentence. Source: docs/03.
6. No docs/03 term, no new queue line, no split: two files, one sentence each. Source: docs/03, docs/05 §1.

**Behaviour.**

* A reader of chapter 12 §What the team gains reads, as its third sentence:
  * en: "On Case A, the same page format carried questions to the client and documents for handover, so every kind of work was reviewed the same way, by reading its page (chapter 21)." in place of "On Case A, the same page format carried questions to the client and documents for handover, so one review skill served every kind of work (chapter 21)."
  * pt, §O que o time ganha: "No Caso A, o mesmo formato de página levou perguntas ao cliente e documentos para a passagem do projeto, então todo tipo de trabalho foi revisado do mesmo jeito, lendo a sua página (capítulo 21)." in place of "No Caso A, o mesmo formato de página levou perguntas ao cliente e documentos para a passagem do projeto, então uma única skill de revisão serviu a todo tipo de trabalho (capítulo 21)."
* Checked, both editions: `grep -rn -i "review skill" book/en/` and `grep -rn -i "skill de revisão" book/pt/` find nothing; `grep -n "reviewed the same way, by reading its page" book/en/12-propose.md` and `grep -n "revisado do mesmo jeito, lendo a sua página" book/pt/12-propose.md` find one line each.
* The rest of chapter 12 is unchanged: its other gain sentences, its Key points (which keep "review surface" / "superfície de revisão") and line 22's "in the review" / "na revisão", which mean the person reading the page.
* Fails: one edition changed and not the other; any skill, command or kit artifact named in the new sentence; a pointer to chapter 13 or 15 added; any other line of chapter 12 changed; any other file changed but this page and the line's marks in docs/06; an em dash; a prose rule of docs/04 hit.

**Contract.**

* Files: `book/en/12-propose.md`, `book/pt/12-propose.md`; no other file.
* Section and line: §What the team gains / §O que o time ganha, its third sentence (en line 141, pt line 148 in the working tree of 2026-10-17; the text is the locator, the number a courtesy).
* Terms of docs/03: none new ("review", "revisão", already there). Sources: none added or removed. Cases: Case A, the existing passage reworded; nothing new about it is said (its page format, questions to the client and handover documents are already in the sentence and in chapter 21 §Case A's documents). Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on nearby chapters.** None touches chapter 12: `ch13-delivery-review` is chapter 13, `ch15-review-by-areas` chapter 15, `ch08-09-review-slot` chapters 8 and 9, `batch-propose` chapter 19. No file in common.

**Out of scope.**

* Teaching the delivery review or the milestone review: owned by `ch13-delivery-review` and `ch15-review-by-areas` (decision 3).
* Chapter 20's "the host's own review command" (en line 30): a host's command, not a kit skill, and not this finding.
* Chapter 12's other uses of "review": they mean the person reading the page, which is right.
* Whether Case A had a review skill of its own: the book teaches today's kit (decision 2).

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the results it names.
* [x] Chapter 12 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] The author approves the reworded Case A sentence in both editions (docs/00 OD-3, docs/05 §5 Case A and Case B); `make scan` green. Pending: the author's reading at the end of the batch.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Finding B26 of the M15 review is settled.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

## What happened

**Built.** The third sentence of chapter 12 §What the team gains / §O que o time ganha, reworded in both editions exactly as Behaviour says; no other line changed.

**Case A passage for the author's approval (docs/00 OD-3).** Pending: the author's reading at the end of the batch.

* en, `book/en/12-propose.md`, §What the team gains: "On Case A, the same page format carried questions to the client and documents for handover, so every kind of work was reviewed the same way, by reading its page (chapter 21)."
* pt, `book/pt/12-propose.md`, §O que o time ganha: "No Caso A, o mesmo formato de página levou perguntas ao cliente e documentos para a passagem do projeto, então todo tipo de trabalho foi revisado do mesmo jeito, lendo a sua página (capítulo 21)."

**Proof.** `grep -rn -i "review skill" book/en/` and `grep -rn -i "skill de revisão" book/pt/` find nothing; the two new-wording greps find en line 141 and pt line 148. `make verify` green, `make scan` green, `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Divergences and omissions.** None.

**Decisions in /apply.** None beyond the page's own; the batch had no one to answer.

**Delivery review.** A read-only Opus agent read this delivery's diffs and its docs/06 hunk against this page and docs/04: no findings. Sentences match Behaviour in both editions, nothing else changed, no em dash, no prose rule hit, Case A adds no detail, commit block in docs/05 §6 format.

```commit
docs(ch12-review-skill): name no review skill in chapter 12's gain

- Chapter 12's gain says Case A reviewed every kind of work by its page
- Both editions, one sentence each; no skill, command or pointer added

work/done/ch12-review-skill.md
```
