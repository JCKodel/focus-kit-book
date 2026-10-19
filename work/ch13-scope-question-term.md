# ch13-scope-question-term

**Objective.** After chapter 13 the Portuguese reader meets the same words as in chapters 12, 14 and 19: "questão de escopo" for a scope question and "travado" for a blocked `/apply`.

**Behaviour.**

* Reading chapter 13's "file in `work/`" sentence, the Portuguese reader finds "questão de escopo", as chapter 12 ("uma questão de escopo ainda está sendo conversada") and chapter 14 ("nenhuma questão de escopo está aberta") say it.
* Reading chapter 13's delivery review paragraph, the Portuguese reader finds the partial work of a "`/apply` travado" and, on trunk, "o trabalho travado", the word chapter 13 already uses for its partial message ("Um `/apply` travado escreve uma mensagem parcial") and its Key points ("também quando para travado"), and chapter 19 uses ("um `/apply` travado não coloca nada em stage").
* No sentence of chapter 13 in Portuguese says "pergunta de escopo" or "bloqueado" afterwards.
* The English edition does not change: it already says "scope question" and "blocked" throughout.
* No number, measurement or meaning of the chapter changes.

**Contract.** File: `book/pt/13-apply.md` only. Sentences, located by content:

* "Um arquivo em `work/` não deixa uma página pronta: só o `/propose` marca a linha como `[>]`, quando cada seção está preenchida ou explicitamente inaplicável e nenhuma pergunta de escopo ficou aberta (docs/05 §3)." "pergunta de escopo" becomes "questão de escopo"; the rest stays.
* "Em um branch da entrega onde você fez commit do trabalho parcial que um `/apply` bloqueado colocou em stage, o agente também lê esses commits contra a base do branch: quando a sessão é retomada, uma pasta de trabalho limpa não quer dizer que não há nada a revisar, já que o trabalho até ali pode estar nesses commits, e eles continuam sendo desta revisão." "um `/apply` bloqueado" becomes "um `/apply` travado"; the rest stays.
* "No trunk não há nenhum, já que lá o trabalho bloqueado fica sem commit." "o trabalho bloqueado" becomes "o trabalho travado"; the rest stays.

English counterparts, unchanged: "no scope question is left open", "the partial work a blocked `/apply` staged", "blocked work stays uncommitted there". Source: chapters 12, 14 and 19 in Portuguese, and chapter 13's own lines 249 and 266, which already say "travado". Terms of docs/03: scope question and blocked `/apply` have no Portuguese entry there (its `blocked reason` is "motivo da espera", a different term), so docs/03 does not change; no new term, no private case.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** Chapter 8's "os commits que uma entrega bloqueada já fez" (items list and the paragraph after it): a blocked delivery, not a blocked `/apply`, and it mirrors docs/03's `delivery review` wording. Chapter 17's "qual linha da fila está bloqueada": a queue line, not an `/apply`. Chapter 14's "travada"/"travado" for lines and cards: already the chosen word. Chapter 21's "desbloqueia": another meaning. The English edition: already consistent.

**Decisions taken alone** (no person available, recommended answer taken). (1) "trabalho bloqueado" on line 75 also becomes "travado": it is the work of the same blocked `/apply` the previous sentence names, and chapter 19 pairs "um `/apply` travado" with "o trabalho fica sem commit". (2) Chapters 8 and 17 keep "bloqueada": the queue line names a blocked `/apply` in chapter 13 only, and those passages name a delivery and a queue line; if the author wants one word book-wide, that is a new line. (3) docs/03 is not changed: it holds neither term in Portuguese.

**Done when.**

* [ ] `book/pt/13-apply.md` edited in the three sentences above, nothing else; each Behaviour line checked against it; `grep -n -E "pergunta de escopo|bloquead" book/pt/13-apply.md` prints nothing.
* [ ] `book/en/13-apply.md` unchanged, and the page says why (ADR-0004: English is the source and already says it).
* [ ] The chapter still opens with its value and keeps its evidenced team gain; no filler and nothing useful cut; every number keeps its source; terms follow docs/03; no em dash.
* [ ] No Case A or Case B passage changed or added, so the author's OD-3 approval is inapplicable.
* [ ] `make verify` green after the last edit; `make book` builds both editions and the page gives `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` for the author's review.
* [ ] Delivery review by a read-only Opus agent per docs/05 §5, its candidates answered on this page; page archived and commit message suggested.
