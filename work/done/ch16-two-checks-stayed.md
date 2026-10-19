# ch16-two-checks-stayed

**Objective.** After chapter 16 the reader reads Ninjobs' restart as chapter 6 tells it: two of the old checks stayed, both guarding privacy, and the rest left; not two new checks in their place. Found by `m19-review` (work/done/m19-review.md, B4: "ch16 says all 29 checks left and two others 'took their place'; ch06:43 says two of the 29 stayed").

**Behaviour.**

* Reading §It works both ways, the reader learns that at Ninjobs' restart all of the old checks but two left, because none of them could name an error in the product it had caught, and that the two which stayed both guard the product's promise of privacy: a proof of what each privacy level may show, and a test of the database access rules.
* The same reader, opening chapter 6's "Of the 29 checks, two stayed, both aimed at the product itself", finds the same two checks and the same story: no chapter says they were new.
* The section still opens on "The question decides what enters, and it decides what stays", and the passage now shows both halves: what left and what stayed.
* Fails: `grep -n -i "took their place\|no lugar delas" book/*/16-the-governor.md` prints anything; chapter 16 says "29" a second time (line 10's "29 checks" stays its only one); one edition changed and not the other; the privacy reason ("where a leak is the error the product cannot afford") cut.
* No number, measurement or other meaning of the chapter changes.

**Contract.** Files: `book/en/16-the-governor.md` and `book/pt/16-the-governor.md`, §It works both ways, the two sentences located by content (they stand after "The question decides what enters, and it decides what stays." / "A pergunta decide o que entra, e decide o que fica."):

* en "On Ninjobs, when I restarted the project, those checks left: none of them could name an error in the product it had caught." becomes, in substance, "On Ninjobs, when I restarted the project, all of those checks but two left: none of them could name an error in the product it had caught."
* en "Two checks took their place, both guarding the product's promise of privacy, where a leak is the error the product cannot afford: a proof of what each privacy level may show, and a test of the database access rules." becomes "The two that stayed both guard the product's promise of privacy, where a leak is the error the product cannot afford: a proof of what each privacy level may show, and a test of the database access rules."
* pt "No Ninjobs, quando eu recomecei o projeto, aquelas verificações saíram: nenhuma delas conseguia nomear um erro no produto que tivesse pegado." becomes "No Ninjobs, quando eu recomecei o projeto, aquelas verificações saíram, menos duas: nenhuma delas conseguia nomear um erro no produto que tivesse pegado."
* pt "Duas verificações ficaram no lugar delas, ambas protegendo a promessa de privacidade do produto, ..." becomes "As duas que ficaram protegem a promessa de privacidade do produto, onde um vazamento é o erro que o produto não pode se permitir: uma prova do que cada nível de privacidade pode mostrar, e um teste das regras de acesso do banco de dados."

/apply may polish the wording within these limits: "two" and no "27" or second "29"; the privacy reason and both checks kept; nothing else in the section changed. Source: chapter 6 §Where it went (§Para onde foi; "Of the 29 checks, two stayed, both aimed at the product itself" / "Das 29 verificações, ficaram duas"), the story's owner. Terms of docs/03: governor (regulador), none new. Cases: Ninjobs by name through its published story, as docs/00 allows; no Case A or Case B passage, so the author's OD-3 approval is inapplicable.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** Line 10's "29 checks that never caught an error in the product": true of all 29, the two kept included, and m15's C2 fixed where the count stands. The gain's "two checks and the governor's question" (en/pt line 87): already reads as the two that stayed. Chapter 6: the owner, already right. Why the two stayed under the governor beyond the privacy reason the text gives: not a finding.

**Decisions taken alone** (no person available, recommended answer taken). (1) "all of those checks but two" and not "27 of those checks": the count stays said once, in line 10 and chapter 6 (docs/04, one fact said once). (2) The "none of them could name an error" clause is not narrowed: it is true of the ones that left and, by line 10, of all 29, so neither reading says the two kept checks caught one. (3) The present tense "guard" / "protegem" for the two kept checks, as chapter 6 tells them still running.

**Done when.**

* [x] Both editions edited in the two sentences above, nothing else; each Behaviour line checked; the Fails grep prints nothing.
* [x] The chapter still opens with its value and keeps its evidenced team gain; no filler and nothing useful cut; every number keeps its source; terms follow docs/03; no em dash.
* [x] No Case A or Case B passage changed or added, so OD-3 is inapplicable.
* [x] `make verify` green after the last edit; `make book` is run once by the batch driver at the end and gives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the author's review.
* [x] No delivery review: the author waived it for this round; /apply does not add one.
* [x] Page archived to `work/done/` and commit message suggested.

**Record.**

* Built: both editions, the two sentences of §It works both ways, worded as the Contract gives them; nothing else in the chapter changed.
* Proof: the Fails grep prints nothing; "29" stays only in line 10's "29 checks" (the other match is a footnote's access date); chapter 6's "two stayed" now reads the same.
* Divergences: none. Omissions: none.
* Delivery review: skipped on the author's word (2026-10-19).
* Decisions: those the page lists; no new one.
* `make verify`: green after the last edit.

```commit
docs(ch16-two-checks-stayed): say two old checks stayed in chapter 16

- en/pt §It works both ways: all of the checks but two left, and the
  two that stayed guard privacy, as chapter 6 tells it
- no new checks took their place; count still said once
```
