# ch15-review-base

**Objective.** After chapter 15 a reader can name a milestone review's base, the commit of the previous milestone's review, or the project's first commit for a first milestone, and say why: the range from it holds every commit since that review, the fixes of its findings and the next milestone's deliveries in whatever order they landed; and can write the review line that waits on paths not read, `· resume: apply · blocked: <what was read>`, and say what each of the checker's three marks means, seen included; both editions.

**Decided without the author** (batch rule of this run: the recommended answer, no question asked).

1. *Applied after `ch15-range-pointer`.* That M16 fix line edits the same chapter, the sentence on `<base>..HEAD` in "Read the code since the base, by areas" (pt "Leia o código desde a base, por áreas"), and is applied before this line, per the driver. In that section this page touches only the two sentences of decision 2, not `ch15-range-pointer`'s sentence on `<base>..HEAD`; when both are in the tree, chapter 15 is staged by hunk (docs/05 §4). If `ch15-range-pointer` rewrote one of the sentences this page names, this /apply finds them by their text after that change and stops on a conflict (docs/05 §4).
2. *Scope: the base, the waiting line's reason and the seen gloss (driver's decision, folded into this line).* The review line's `[?]` in "Read the code since the base, by areas" shows `· resume: apply` and `· blocked: <what was read>`, as docs/05 §8 writes it; the placeholder is translated in Portuguese, `<o que foi lido>`, as chapter 14 writes `<motivo>` (docs/04 "Evidence"). The checker's sentence glosses seen beside latent and weak, "seen when it is true in the file today", docs/05 §8's "(true in the file today)"; the M17 paragraph names it, and the example block's "seen: true today" already matches. Both sentences sit in the section `ch15-range-pointer` also edits, at other sentences (decision 1).
3. *The reason, in the present.* On trunk the next milestone's deliveries can land before the previous milestone's findings close; a base at the last of those findings would sit after some of the next milestone's work and leave it out of the range. The previous review's commit sits before all of it (docs/05 §8, "so the range holds the fixes of its findings, which get no second review"; docs/04 "The kit as it is": the error it prevents, no history of the kit or of this repository).
4. *The first commit's second use goes.* "and of any later one whose earlier reviews left part of the project unread" no longer matches docs/05 §8, which gives the first commit "for a first milestone": a reading that misses part of its range now makes the review line wait (docs/05 §§4, 8), so no later base needs to reset. The sentence keeps what the first commit does, the whole project read.
5. *"No second review" says where the fixes are read.* One sentence: the finding lines get no review of their own, and the next milestone's review reads them, since its range starts at this review's commit. That is where the reader's doubt on unreviewed fixes is born (docs/04 "Say it where the doubt is born"). The lending library example names `m2-review` and `m1-review`, no hash (ADR-0017).
6. *Opening, gain and the other key points unchanged.* The opening says "the code changed since the milestone's base", still true; key point 2 is the one that names the base and changes. The gain does not depend on which commit is the base (docs/04 "One gain").
7. *No docs/03 change.* The `milestone review` row says "from the commit the page names", still true (`kit-2026-10-18` Out of scope).
8. *Trunk; nothing staged by this definition; the driver sets docs/06's marks.* docs/05 §5 Git, and this batch's instructions.

**Behaviour.**

* Reading "The review is a delivery", a reader finds the base: the commit of the previous milestone's review, or the project's first commit for a first milestone.
* A reader can say why the base is the previous review's commit and not the last commit of the previous milestone: the next milestone's deliveries can land before the previous milestone's findings close, and a range from the previous review's commit holds all of them, the findings' fixes included.
* A reader can say what the first commit does as a base: the review reads the whole project, as a first milestone needs.
* Reading "No second review", a reader can say where the finding lines' fixes are read in the whole: in the next milestone's code reading, whose range starts at this review's commit; on the lending library, `m2-review`'s range starts at `m1-review`'s commit and holds `returned-loan`'s fix.
* Edge: a reader whose review missed part of its range does not restart the next base at the first commit; the line waits (chapter 14) until the rest is read.
* Reading "Read the code since the base, by areas", a reader finds the review line waiting as `[?]` with `· resume: apply` and `· blocked: <what was read>` when the paths read miss some of the range's, and can write it for the lending library (chapter 14 shows one).
* Reading the checker's sentence, a reader can say what each mark means: seen, true in the file today; latent, nothing triggers it today; weak, the claim does not hold as stated.
* Reading key point 2, a reader finds the same base.
* The Portuguese edition reads the same in the same places, with the Contract's words and the lending library's Portuguese slugs.
* Failure: "the commit that closed the previous milestone" (pt "o commit que fechou o marco anterior") left in chapter 15, a commit hash in the text, or one edition changed and not the other.

**Contract.**

* **Chapter 15, both editions** (`book/en/15-closing-a-milestone.md`, `book/pt/15-closing-a-milestone.md`), found by text:
  * In "The review is a delivery" (pt "A revisão é uma entrega"), the sentence "Its page names the commit that closed the previous milestone, or the project's first commit; that commit is the base, and the page lists, by the areas docs/05's Milestone review slot names, the paths the range since it changed." becomes two sentences, one per line:
    "Its page names as the base the commit of the previous milestone's review, or, for a first milestone, the project's first commit, and lists, by the areas docs/05's Milestone review slot names, the paths the range since it changed."
    "The previous review's commit sits before every commit of the next milestone, whose deliveries can land before the previous one's findings close, so the range from it holds all of them, the fixes of those findings included."
    (pt: "A página dela cita como base o commit da revisão do marco anterior, ou, para um primeiro marco, o primeiro commit do projeto, e lista, pelas áreas que o slot Milestone review (revisão de marco) do docs/05 cita, os caminhos que o intervalo desde ele alterou." / "O commit da revisão anterior fica antes de todo commit do marco seguinte, cujas entregas podem entrar antes de os achados do anterior fecharem, então o intervalo a partir dele guarda todos eles, incluídas as correções desses achados.")
  * the sentence "The first commit makes the review read the whole project: it is the base of a first milestone, and of any later one whose earlier reviews left part of the project unread." becomes "The first commit, the base of a first milestone, makes the review read the whole project." (pt "O primeiro commit faz a revisão ler o projeto inteiro: é a base de um primeiro marco, e de qualquer marco posterior cujas revisões anteriores deixaram parte do projeto sem ler." becomes "O primeiro commit, a base de um primeiro marco, faz a revisão ler o projeto inteiro.").
  * In "Read the code since the base, by areas" (pt "Leia o código desde a base, por áreas"), the sentence "When they miss some, the page says which, and the review line waits as `[?]` with `· resume: apply` (chapter 14) until they are read, because ..." becomes "When they miss some, the page says which, and the review line waits as `[?]` with `· resume: apply` and `· blocked: <what was read>` (chapter 14) until they are read, because ..."; the rest of the sentence unchanged (pt "... espera como `[?]` com `· resume: apply` (capítulo 14) até que ..." becomes "... espera como `[?]` com `· resume: apply` e `· blocked: <o que foi lido>` (capítulo 14) até que ...").
  * The checker's sentence, "...: seen, latent when nothing triggers it today, or weak when the claim does not hold as stated." becomes "...: seen when it is true in the file today, latent when nothing triggers it today, or weak when the claim does not hold as stated." (pt "...: visto, latente quando nada o dispara hoje, ou fraco quando a afirmação não se sustenta como foi dita." becomes "...: visto quando é verdadeiro no arquivo hoje, latente quando nada o dispara hoje, ou fraco quando a afirmação não se sustenta como foi dita.").
  * In "No second review" (pt "Nenhuma segunda revisão"), after "Each one passes through its own page, its proof and the person's commit, which is the review." (pt "Cada uma passa pela sua própria página, pela sua prova e pelo commit da pessoa, que é a revisão."), one sentence on its own line:
    "Their code is still read with the whole: the next milestone's review names this review's commit as its base, so on the lending library `m2-review`'s range starts at `m1-review`'s commit and holds `returned-loan`'s fix."
    (pt: "O código delas ainda é lido com o todo: a revisão do marco seguinte cita o commit desta revisão como base, então na biblioteca de empréstimos o intervalo de `m2-review` começa no commit de `m1-review` e guarda a correção de `emprestimo-devolvido`.")
  * key point 2: "its page names the commit that closed the previous milestone, or the project's first commit, writes ..." becomes "its page names as the base the commit of the previous milestone's review, or the project's first commit for a first milestone, writes ..."; the rest of the bullet unchanged (pt "a página dela cita o commit que fechou o marco anterior, ou o primeiro commit do projeto, escreve ..." becomes "a página dela cita como base o commit da revisão do marco anterior, ou o primeiro commit do projeto para um primeiro marco, escreve ...").
  Every other sentence of chapter 15 is unchanged: the rest of "Read the code since the base, by areas", `ch15-range-pointer`'s sentence on `<base>..HEAD` above all, the example candidates, the gain and the other key points.
* **Portuguese words.** milestone review: `revisão de marco`; base: `base`; range: `intervalo`; finding: `achado`; fix: `correção`; checker: `conferente`; seen, latent, weak: `visto`, `latente`, `fraco`; the kit's suffixes `· resume: apply`, `· blocked:` stay, the placeholder `<o que foi lido>` is translated; the lending library's slug `emprestimo-devolvido`, and `m1-review`, `m2-review` in English, as chapter 15 already writes them.
* **Terms of docs/03.** `milestone review`, `finding`, `trunk`, `candidate`, `waiting mark` used as defined. No new term, no docs/03 change (decision 7).
* **Sources.** None added or removed.
* **Cases.** No private case added; the Ninjobs section "When the findings became one delivery" is unchanged. The example is the lending library's milestone already said to be written for the chapter; `m2-review` is named in the text, not shown.
* **docs/06.** None from this page; the driver sets its line's marks.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* The pointer or teaching for `<base>..HEAD`: `ch15-range-pointer`, applied first (decision 1).
* docs/03's `candidate` row, which glosses latent and weak only: M16's `docs03-review-rows` owns its seen gloss.
* Chapter 14's fourth waiting case: `ch14-four-waits`.
* Chapter 8's report of the same migration: `ch08-update-2026-10-18`.
* `work/done/` pages that name the old base: history, not edited.

**Done when.**

* [x] `ch15-range-pointer` is `[x]` before this /apply starts editing chapter 15 (driver's order).
* [x] Both editions written in the places the Contract names, the English first; parity green.
* [x] `grep -n "closed the previous milestone\|any later one" book/en/15-closing-a-milestone.md` and `grep -n "fechou o marco anterior\|qualquer marco posterior" book/pt/15-closing-a-milestone.md` find nothing; "previous milestone's review" (pt "revisão do marco anterior") in the section's sentence and key point 2.
* [x] `grep -c "blocked: <what was read>" book/en/15-closing-a-milestone.md` gives 1 (pt `blocked: <o que foi lido>` 1); `grep -c "seen when it is true in the file today"` gives 1 (pt `visto quando é verdadeiro no arquivo hoje` 1).
* [x] No commit hash in either edition; `m2-review` named once in each.
* [x] Chapter 15 still opens with its value; no filler, nothing useful cut; still five key points.
* [x] The Portuguese uses the Contract's words and no synonym.
* [x] No em dash; `make verify` green (build, parity, em dash, prose, width, links, disclosure).
* [x] The Delivery review ran on this delivery's paths and the files it created (docs/05 §5), and the page records it.
* [x] The author's approval of an anonymized passage: inapplicable, no new Case A or Case B passage.
* [x] `make book` builds; the delivery ends with the paths of both PDFs for the author's review.
* [x] Page moved to `work/done/`, the line `[x]`, chapter 15 staged by hunk if `ch15-range-pointer`'s change is still unstaged in the tree, and this line's hunk of docs/06; the commit message suggested, `docs(ch15-review-base): ...`.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure). "closed the previous milestone", "any later one", "fechou o marco anterior" and "qualquer marco posterior" find nothing; "previous milestone's review" twice in English and "revisão do marco anterior" twice in Portuguese (the section's sentence and key point 2). `blocked: <what was read>`, `blocked: <o que foi lido>`, "seen when it is true in the file today" and "visto quando é verdadeiro no arquivo hoje" once each; `m2-review` once per edition; no commit hash; five key points in each. `ch15-range-pointer` was `[x]` and committed before this /apply, so chapter 15 is staged whole. `make book` builds:

* `output/one-page-at-a-time.pdf`
* `output/uma-pagina-de-cada-vez.pdf`

**Divergences.** None: every string is the Contract's.

**Delivery review** (docs/05 §5, one read-only agent on Opus, on both chapter diffs and this page). Nothing breaks the page, docs/04 or this text: the six edits match the Contract in both editions, `ch15-range-pointer`'s sentence on `<base>..HEAD` is untouched, the new base, the seen gloss and the waiting line match docs/05 §8, the reason is in the present, and the Portuguese uses the Contract's words. Two notes left as they are, since the Contract fixes the wording: "since it" in the base sentence has the first commit as its nearest antecedent and still reads as the base; the first commit's sentence stays after "The reading costs", the order the chapter already had. Chapter 8's quotation of the old docs/05 text belongs to `ch08-update-2026-10-18` and is correct there as a quote.

**Decisions taken in /apply.** None beyond the page's. The `[ ]` line `ch15-waiting-reason` is answered in full by this delivery's waiting line in "Read the code since the base, by areas"; its line is left for the driver, as asked.

```commit
docs(ch15-review-base): base a milestone review on the previous review

- name the base as the previous milestone's review commit, or the
  first commit for a first milestone, and say why
- the review line waits with blocked: <what was read>
- gloss seen; say the next review reads the finding lines' fixes

work/done/ch15-review-base.md
```
