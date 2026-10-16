# ch14-18-kit-wording

**Objective.** After chapters 14 and 18 a reader finds the kit's reason for separating deciding from doing quoted as the kit writes it, knows the Contract's three reasons for being exact, the leaked access rule included, and reads the governor's item as "no gate before implementation beyond a complete page".

**Behaviour.**

* A reader who opens the kit's README after chapter 14 finds the sentence the chapter quotes: scope cannot grow during implementation because the person who decided is not in the room. No sentence in the chapter is attributed to a kit file that does not hold it.
* A reader of chapter 14 knows why the Contract must be exact, in three cases: a screen is code rewritten in a session, a column holds data and changing it is a migration, and an access rule that is wrong has already let data out by the time it is noticed; the third is the one no later fix undoes.
* A reader of chapter 18 reads the governor's fifth item as "no gate before implementation beyond a complete page" and knows that the complete page, read by the person before `/apply`, is the one gate the process has.
* Failure: a reader who reads "no gate before implementation" and then chapter 14's "`/apply` refuses an incomplete page" sees a contradiction; the wording closes it.
* Edge: the quotation marks and italics of a quoted kit sentence are kept as chapter 14 uses them today; a paraphrase is not marked as a quotation.

**Contract.**

* **Chapter 14, both editions, file name, title and headings kept.**
  1. §What `/propose` does: "The kit's file for the command gives the reason: '*separating deciding from doing is what keeps scope from growing during implementation*'." becomes "The kit's README gives the reason: '*Scope cannot grow during implementation because the person who decided is not in the room.*'" (pt: the sentence of the kit's README.pt, quoted from it).
  2. §The page, the Contract paragraph: "The kit's reason: '*a wrong screen is fixed in a session, a wrong column is a migration*'" becomes the kit's three clauses, quoted whole, "*a wrong screen is fixed in a session, a wrong column is a migration, and a wrong access rule has already leaked*", and the explaining sentence gains a third clause: an access rule decides who reads what, and a wrong one has let data out before anyone reads the page again.
  3. Nothing else in chapter 14 changes.
* **Chapter 18, both editions:** the bullet "**No gate before implementation:** the person who reads the page before `/apply`, and asks for what is missing." becomes "**No gate before implementation beyond a complete page:** the page is the one gate, read by the person before `/apply`, who asks for what is missing; `/apply` refuses a page that is not complete (chapter 14)." (pt: "Nenhuma barreira antes da implementação além de uma página completa").
* **Portuguese:** the README.pt sentence checked against the kit's README.pt and quoted from it, not translated by the chapter.
* **Terms:** page, Contract, governor, as docs/03 has them; docs/03 unchanged.
* **Sources:** the kit's README and README.pt (the scope sentence), its docs/05 template §3 and §7; paraphrased or quoted with no note, as chapter 14 already does for kit files.
* **Cases:** none. Code examples: none.

**Out of scope.**

* Chapter 14's exploration ending in `/propose` in the same session: `ch13-14-19-line-stops`.
* Chapter 18's retelling of the `[?]` story and its three mentions of the 29 checks: a cut, M15's `method-said-once`.
* The Contract reasons in the book's own docs/05 §3: `kit-2026-10-16-2`.

**Done when.**

* [x] Chapters 14 and 18 changed in both editions, same headings; each opens with its value; no filler and nothing useful cut.
* [x] Each quoted sentence found verbatim in the kit file the chapter names, in both languages.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* The quotation moves to the README because the propose skill at 2026.10.16.2 holds no such sentence and the README does: the kit's files, read for this page; docs/04, every quoted artifact real and saying where it comes from.
* The third reason explained in one clause: docs/04's rule that a rule's reason is the error it prevents, said in the present.
* Chapter 18's item cross-refers to chapter 14's refusal of an incomplete page, which the chapter already teaches: docs/04's pointers rule.

**Decisions in the review.** None.

**Divergences.**

* Chapter 18's item drops the pointer "(chapter 14)" and says the refusal itself, "`/apply` refuses a page that is not complete and points to `/propose`": no chapter teaches that refusal, chapter 14 included, so the Decision above that it "already teaches" it was wrong. The author chose this in the /apply conversation over adding the sentence to chapter 14 or 15. The source is the kit's `/apply` (SETUP.md, "refuse an incomplete proposal and point to /propose").
* Chapter 14's Contract paragraph gains one short sentence after the explaining one, "No later fix undoes the third." (pt: "Nenhuma correção posterior desfaz a terceira."), because Behaviour asks the reader to know that the third reason is the one no later fix undoes, and the clause alone only implies it.

**Omissions.**

* Chapter 14's key point "the Contract is the one exact section, because a wrong column is a migration" stays as it is: the Contract says nothing else in chapter 14 changes, and the point is still true.

**Proof.**

* Each quoted sentence found verbatim in the kit at 2026.10.16.2: the scope sentence in README.md and README.pt.md, in "Deciding and doing in separate sessions"; the Contract's three clauses in SETUP.md's docs/05 template §3; "no gate before implementation beyond a complete page" in its §7. The kit has no Portuguese docs/05 template, so the Portuguese Contract clauses are quoted whole from the one place the kit writes all three in Portuguese, CHANGELOG.pt.md at 2026.10.16.2: "uma tela errada se corrige numa sessão, uma coluna errada é uma migration, e uma regra de acesso errada já vazou"; the chapter's earlier "em uma sessão", its own translation, became the kit's "numa sessão".
* `make verify` green; `make book` built both editions, and the PDFs are `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* Owning documents: none changes. The book's docs/05 §3 and §7 already hold the three reasons and the complete-page gate; docs/03 unchanged.

```commit
docs(ch14-18-kit-wording): quote the kit as it writes it
- ch14: the scope sentence quoted from the kit's README, both editions
- ch14: the Contract's third reason, a wrong access rule has leaked
- ch18: no gate before implementation beyond a complete page
- ch18: /apply refuses a page that is not complete

work/done/ch14-18-kit-wording.md
```
