# ch15-brief-printed

**Objective.** A reader following the guided project can run the clinic's `orchestrator-tests` from chapter 15 alone: the chapter prints, word for word, the author's brief that answers `/propose`'s first round of questions and the rule that answers every later round, as chapters 7, 8 and 10 print theirs, so building the code `book-v1/four-pieces` holds needs no trip to the run record.

**Behaviour.**

* The reader finds the brief printed in chapter 15, right where the chapter tells them to run `/propose orchestrator-tests`, and can send it without opening any note.
* The reader knows what to send in each round, as the run did: the brief answers the first round of questions (turn 2 of the record), and `Your call. Say what you chose and why.` answers every later round (turn 3).
* The reader knows that the brief's "milestone 2" is their milestone 1.1, as the chapter already says.
* The note `[^clinic-orchestrator-tests-run]` stays, as the source of the printed brief, and names the brief among what the record holds.
* Both editions say the same; the Portuguese one prints the brief translated, saying the original is in English, as chapters 7, 8 and 10 do.
* Finding F9 of the M4.1 review is settled (`work/done/m4.1-review-run/findings.md:49`).

**Contract.**

Sentences are found by their quoted text. `ch15-uncaught-pieces`, `ch15-view-rule` and `ch15-shape-cost` edit other sections of chapter 15 at the same time and may move its lines; the line numbers below are from commit `cad46ef`.

* `book/en/15-four-pieces.md`, section "The four pieces" (heading and anchor unchanged), the sentence "Then run `/propose orchestrator-tests`, answer its questions with the author's brief,[^clinic-orchestrator-tests-run] where "milestone 2" is your milestone 1.1, and run `/apply orchestrator-tests` before you read on." (en:18, pt:18) becomes, as a proposal for `/apply` to tighten:
  * "Then run `/propose orchestrator-tests`; I ran it headless in Claude Code and answered its first round of questions with the author's brief, word for word, where "milestone 2" is your milestone 1.1:[^clinic-orchestrator-tests-run]"
  * a fenced block with no language tag, holding the brief exactly as `work/done/clinic-orchestrator-tests-run/README.md:43` has it:

    ```
    Every client orchestrator, each use<Feature>.ts hook, gets unit tests. Move what each event does out of the hook: the calls to repositories and use cases, in their order, and the new state go into plain functions that receive their repositories as a parameter, the real ones by default, and `now` where a use case needs the clock, and return the new state. The hook only holds the state, publishes the in-flight state and publishes what the function returns. The tests pass fake repositories, in Vitest in Node, with no module mock and no new dependency. Server routes do not change. The app behaves exactly as before. Add the line as the first of milestone 2.
    ```

  * "Every later round was answered with the rule of chapter 10's brief, `Your call. Say what you chose and why.`; then run `/apply orchestrator-tests` before you read on."
* `book/pt/15-four-pieces.md`, the same place (pt:18), the same three parts. Proposal:
  * "Depois rode `/propose orchestrator-tests`; eu o rodei sem interface no Claude Code e respondi à primeira rodada de perguntas com o briefing do autor, em que "marco 2" é o seu marco 1.1; o original está em inglês, e aqui vai traduzido:[^clinic-orchestrator-tests-run]"
  * the brief translated in a fenced block with no language tag, identifiers (`use<Feature>.ts`, `now`, Vitest, Node) unchanged: "Todo orquestrador do cliente, cada hook use<Feature>.ts, ganha testes unitários. Tire do hook o que cada evento faz: as chamadas a repositórios e casos de uso, na ordem delas, e o novo estado vão para funções simples que recebem os seus repositórios como parâmetro, os reais por padrão, e `now` onde um caso de uso precisa do relógio, e devolvem o novo estado. O hook só guarda o estado, publica o estado em andamento e publica o que a função devolve. Os testes passam repositórios falsos, no Vitest em Node, sem mock de módulo e sem dependência nova. As rotas do servidor não mudam. O app se comporta exatamente como antes. Adicione a linha como a primeira do marco 2."
  * "Toda rodada seguinte foi respondida com a regra do briefing do capítulo 10, `Your call. Diga o que escolheu e por quê.`; depois rode `/apply orchestrator-tests` antes de seguir a leitura."
* The note `[^clinic-orchestrator-tests-run]` (en:495, pt:496): "every turn" becomes "the brief, every turn" ("o briefing, cada turno"); the rest unchanged.
* Terms of docs/03: none new, none changed. "brief" is not a docs/03 term; it is used as the plain word chapters 7, 8 and 10 already use.
* Sources: `work/done/clinic-orchestrator-tests-run/README.md` (the brief at :43, the rounds at :20 and :40). No new note.
* Cases: none. Exercises: unchanged.

**Out of scope.**

* The author's page review (turn 4) and staged review (turn 6) of the run: the chapter asks the reader only for `/propose` and `/apply`, and F9 names the brief alone; the record keeps them.
* The clinic and the run record: nothing reruns; `work/done/clinic-orchestrator-tests*.md` record what happened and are not edited.
* Chapter 15's catches, the view's rule and the key point on a piece's cost: `ch15-uncaught-pieces`, `ch15-view-rule` and `ch15-shape-cost`, proposed at the same time.
* Chapters 7, 8 and 10: they already print their briefs and are the first occurrences; not edited.

**Done when.**

* [ ] Both editions changed with the same meaning; chapter 15 still opens with its value, with no filler and nothing useful cut.
* [ ] The English brief in chapter 15 is byte for byte the one in `work/done/clinic-orchestrator-tests-run/README.md`.
* [ ] No "answer its questions with the author's brief" or "responda às perguntas dele com o briefing do autor" left in `book/`.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
