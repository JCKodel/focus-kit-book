# ch14-keepless-feature

**Objective.** A reader of chapter 14 can place a feature in a slice, whether it is one thing the app keeps, or one thing the app does that keeps nothing, such as the clinic's server check, and can say where the code of either lives.

**Behaviour.**

* The reader can say what a feature is in two cases: one thing the app keeps, named by a term of the project's docs/03 (the appointment, the professional, the weekly hours), or one thing the app does that keeps nothing, named by what it does (the health slice, the server check). In both, its slice holds every action on it.
* The reader, shown the health slice, can say why it is a feature and not code for `src/lib/`: it is one thing the app does, with its own route, call, hook and screen, and it has no `repository.server.ts` because it keeps nothing, not because it is less of a feature.
* The reader can apply the placement rule to a feature that keeps nothing: code about one feature stays in its slice, and only what two features share that belongs to no one feature moves to `src/lib/` on its second use. The rule no longer reads as if a check's own code, having no kept thing, had to go to `lib/`.
* The reader can give an example of their own of a feature that keeps nothing (a check, a report), without the chapter adding a new example from the clinic.
* Both editions say the same.

**Contract.**

Sentences are found by their quoted text. The line numbers below are from commit `cad46ef`, the same in both editions.

* `book/en/14-errors-and-slices.md`, section "Vertical slices" (heading and anchor unchanged):
  * Line 54, "A feature is one thing the app keeps, named by a term of the project's docs/03 (the appointment, the professional, the weekly hours), and its slice holds every action on it." gains the second case. Proposal for `/apply` to tighten: "A feature is one thing the app keeps, named by a term of the project's docs/03 (the appointment, the professional, the weekly hours), or one thing the app does that keeps nothing, named by what it does (the server check of `health`); its slice holds every action on it."
  * Lines 55 to 58 (booking and cancelling share the appointment; weekly hours and professionals; a change touches this folder; what an agent reads) unchanged.
  * Line 71, "It has no `rules.ts`, because it has no rule, and no `repository.server.ts`, because it stores nothing: a file appears in a slice when it pays its way." gains, before or after it, one short sentence saying the health slice is the second kind of feature: it keeps nothing and is still a slice. In English, "because it stores nothing" becomes "because it keeps nothing", one verb for one idea (the Portuguese already says "não guarda nada"). No new code block, no new listing.
  * Line 74, "Code about one thing the app keeps stays in that thing's slice" becomes "Code about one feature stays in that feature's slice"; the rest of the sentence unchanged.
  * Line 75 (`findClinic`, `findActiveProfessionals`, "because each reads the thing its slice keeps") unchanged: both slices keep a thing.
  * Line 76, "belongs to no thing the app keeps" becomes "belongs to no one feature".
  * Line 78, "code that belongs to no one thing" becomes "code that belongs to no one feature".
* Key points, `book/en/14-errors-and-slices.md`:
  * Line 297: "A feature is one thing the app keeps, with every action on it" becomes "A feature is one thing the app keeps, or one thing it does that keeps nothing, with every action on it"; the rest unchanged.
  * Line 298: "code about one thing the app keeps stays in its slice" becomes "code about one feature stays in its slice", and "belongs to no one thing" becomes "belongs to no one feature".
  * The other key points unchanged.
* `book/pt/14-errors-and-slices.md`: the same changes at lines 54, 71, 74, 76, 78, 297 and 298. Proposal for line 54: "Uma funcionalidade é uma coisa que o app guarda, nomeada por um termo do docs/03 do projeto (o agendamento, o profissional, os horários semanais), ou uma coisa que o app faz sem guardar nada, nomeada pelo que faz (a verificação do servidor de `health`); a fatia dela guarda toda ação sobre ela." "Code about one feature" is "O código sobre uma funcionalidade"; "no one feature" is "nenhuma funcionalidade".
* Terms of docs/03: none new. The vertical slice row (docs/03 line 54) changes its definition of a feature the same way, in the same delivery, by `/apply`: "a feature is one thing the app keeps, or one thing it does that keeps nothing, with every action on it", and "code about one thing the app keeps stays in its slice" becomes "code about one feature stays in its slice", and "belongs to no one thing" becomes "belongs to no one feature".
* Sources: none new. The health slice's link and listing at `book-v1/closing-a-milestone` stay as they are; `/apply` re-runs `git ls-tree` there and confirms the 6 files and that no `repository.server.ts` exists.
* Cases: none. Ninjobs is not used. Exercises: unchanged.

**Out of scope.**

* The clinic's code and its tags: the book only, and health stays as it is.
* Chapter 15's health passage (lines 442 to 454, the orchestrator that does not pay its way): owned by `ch15-shape-cost`.
* Chapter 14's `query`, "Why not throw" and "The boundary": owned by `ch14-swallowed-bug`, `ch14-library-types` and `ch15-uncaught-pieces`, in flight at the same time; this page touches only lines 54 to 78 and key points 1 and 2.
* A name or docs/03 term for a feature that keeps nothing: one example in the clinic does not earn one (abstraction on the second occurrence).
* `signIn`, named by an action yet keeping the owner's session: the chapter does not mention it, and it is not this line's finding.
* The clinic's own docs/03 having no term for health: its docs are the clinic's, not the book's.

**Done when.**

* [x] Both editions changed with the same meaning; chapter 14 opens with its value, with no filler and nothing useful cut.
* [x] No sentence of chapter 14 still defines a feature, or the placement rule, only by "one thing the app keeps".
* [x] docs/03's vertical slice row says the same as the chapter.
* [x] The health slice's listing was re-run at `book-v1/closing-a-milestone`.
* [x] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author. Left to the batch driver, which builds once at the end of the loop.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Revalidated against the current tree: the earlier M4.2 deliveries moved none of the quoted lines; all were still at 54, 71, 74, 76, 78, 297 and 298 in both editions, and the docs/03 row at line 54.
* `git ls-tree` at `book-v1/closing-a-milestone` lists the same 6 files under `src/features/health/`, with no `repository.server.ts`.
* Line 54 took the proposal as written, in both editions.
* Line 71: the new sentence goes after it, "Keeping nothing does not make it less of a feature: it has its own route, call, hook and screen, and so its own slice." (pt: "Não guardar nada não a torna menos funcionalidade: ela tem a sua rota, a sua chamada, o seu hook e a sua tela, e por isso a sua fatia."). After, not before, so the file list and its missing files are read first. Chosen alone in the batch, the agent's recommendation.
* "stores nothing" became "keeps nothing" in English; the Portuguese already said "não guarda nada".
* docs/03's vertical slice row changed as the page says.
* The first `make verify` failed only on a timeout of an external link in chapter 10 (code.claude.com), unrelated; the second run was green.
* Nothing dropped; no ADR.
