# ch16-reading-count

**Objective.** A reader of chapter 16 can compare the 20 of 95 files that the delivery inside a slice read with what the clinic's other deliveries read, counted the same way. The reader can then say what a slice does to an agent's reading: it bounds where the reading goes, and how much the agent reads depends on what the delivery touches.

**Behaviour.**

* The reader can give the six `/apply` turns of the clinic's milestone 1, each with its count by the chapter's method. `clinic-setup` read 14 of 15 files, `professionals` 26 of 49, `weekly-hours` 25 of 63, `e2e-database-busy` 4 of 77, `book-appointment` 33 of 77 and `cancel-appointment` 20 of 95.
* The reader can say which turns started a slice (`professionals`, `weekly-hours`, `book-appointment`) and which delivery worked inside one (`cancel-appointment`). They can also say that a fix to shared code, `e2e-database-busy`, read fewer files than either kind.
* The reader can say why the chapter no longer says a slice keeps the reading "small". The record has no run of the same delivery without slices. The 4 of 77 also shows that the size of a delivery, not only its slice, decides how much is read.
* The reader can repeat any of the six counts from the record, using the method the chapter already states (en:329, pt:330).
* Both editions say the same.
* Finding F15 of the M4 review is settled (`work/done/m4-review-run/findings.md:85`).

**Contract.**

Sentences are found by their quoted text. The line numbers below are from commit `060d023`. Three other pages are in flight on chapter 16: `ch16-unit-test` (en:24-25, pt:25-26), `ch16-it-each` (en:194,242; pt:195,243) and `slice-imports` (en:334,341; pt:335,343). This page does not touch their lines. The new paragraph goes after the line `slice-imports` rewrites, and it is found by that line's position and not by its wording.

* `book/en/16-testing-and-agents.md` and `book/pt/16-testing-and-agents.md`:
  * Opener, en:4: "how a slice and its tests keep an agent's reading small and tell it when it is done." becomes "how a slice bounds what an agent reads and how its tests tell it when it is done." pt:4: "como uma fatia e os seus testes mantêm pequena a leitura de um agente e dizem a ele quando terminou." becomes "como uma fatia limita o que um agente lê e como os testes dela dizem a ele quando terminou."
  * Section "What the slice gives an agent" (heading and anchor unchanged): a new paragraph after the line "A new slice copies the shape of a sibling slice, ..." (en:341, pt:343, as `slice-imports` leaves it) and before "Both turns ran ...". English proposal for `/apply` to tighten: "The same count over the milestone's other four `/apply` turns gives something to compare with. `clinic-setup`, the first delivery on the skeleton, read 14 of the 15 files. `professionals` read 26 of 49 and `weekly-hours` 25 of 63, each starting its slice, like `book-appointment`'s 33 of 77. `e2e-database-busy`, a fix to how the server opens SQLite, read 4 of 77. The record has no run of the same delivery without slices. What it shows is that a delivery reads about as much as it touches, and that the slice bounds where that reading goes: to the slice itself and the code it calls, or to a sibling slice to copy." Portuguese with the same meaning: "A mesma contagem nos outros quatro turnos de `/apply` do marco dá com o que comparar. `clinic-setup`, a primeira entrega sobre o esqueleto, leu 14 dos 15 arquivos. `professionals` leu 26 de 49 e `weekly-hours` 25 de 63, cada uma começando a sua fatia, como os 33 de 77 de `book-appointment`. `e2e-database-busy`, uma correção de como o servidor abre o SQLite, leu 4 de 77. O registro não tem uma execução da mesma entrega sem fatias. O que ele mostra é que uma entrega lê mais ou menos o quanto toca, e que a fatia limita para onde essa leitura vai: para a própria fatia e o código que ela chama, ou para uma fatia irmã, para copiar." The four new counts carry `[^clinic-milestone-1-run]`, which the chapter already defines (en:385, pt:387). The note does not change.
  * "Both turns ran the slice's tests alone before the whole verify." (en:343) becomes "The two turns of the appointments slice ran the slice's tests alone before the whole verify." pt:345: "Os dois turnos rodaram os testes da fatia sozinhos antes da verificação inteira." becomes "Os dois turnos da fatia do agendamento rodaram os testes da fatia sozinhos antes da verificação inteira." This is needed because the new paragraph has four other turns before it.
  * Key point 5, en:359: "A slice keeps an agent's reading small, 20 of 95 files for a delivery inside one, and its tests, run alone, tell the agent when the slice is done." becomes "A slice bounds where an agent reads: the delivery inside one read 20 of 95 files, the ones that started a slice 25 of 63 to 33 of 77, and a fix to shared code 4 of 77; the slice's tests, run alone, tell the agent when it is done." pt:361 with the same meaning: "Uma fatia limita onde um agente lê: a entrega dentro de uma leu 20 de 95 arquivos, as que começaram uma fatia de 25 de 63 a 33 de 77, e uma correção no código compartilhado 4 de 77; os testes da fatia, rodados sozinhos, dizem ao agente quando terminou." Chapter 16 still has five key points.
  * "Chapter 14 said a slice bounds what an agent reads." (en:327), the counting method (en:329, pt:330), "These turns ran before the event functions existed ..." (en:330, pt:331) and "Fewer files read is less context ..." (en:348, pt:350) all still fit and are not changed.
* How the counts are made, so that `/apply` gets the same numbers. The method is the one en:329 states. Count the distinct paths under `src/` that existed at the parent commit and whose contents the `/apply` turn read, by a `Read` call or by a shell call that prints a file (`cat`, `sed -n`, `head`, `tail`). A `grep` or an `ls` is not a read. A call that the README lists as denied read nothing. The total is `git ls-tree -r --name-only <parent> src` in `../focus-kit-clinic`. Every shell loop that printed source files is denied in the README (`work/done/clinic-milestone-1-run/README.md`, the "Denied calls" line of each delivery), so no loop counts. `weekly-hours`' third loop ran Playwright and printed nothing. The turn files are under `work/done/clinic-milestone-1-run/`:

  | Delivery | `/apply` turn | Parent | Read of `src/` |
  |---|---|---|---|
  | `clinic-setup` | `clinic-setup/turn-4.txt` | `d5b5c03` | 14 of 15 |
  | `professionals` | `professionals/turn-3.txt` | `75a8a25` | 26 of 49 |
  | `weekly-hours` | `weekly-hours/turn-3.txt` | `4cceb3a` | 25 of 63 |
  | `e2e-database-busy` | `e2e-database-busy/turn-3.txt` | `064d7a9` | 4 of 77 |
  | `book-appointment` | `book-appointment/turn-4.txt` | `afc833a` | 33 of 77 |
  | `cancel-appointment` | `cancel-appointment/turn-3.txt` | `442f88a` | 20 of 95 |

  These counts were made when the page was proposed. The same method gives the chapter's 33 of 77 and 20 of 95 exactly. `/apply` recounts all six and records any difference on the page before writing the chapter.
* Terms of docs/03: none new.
* Sources: the milestone 1 run (`work/done/clinic-milestone-1-run/`) and the clinic's history at the six parent commits. The chapter's note `[^clinic-milestone-1-run]` already links the run.
* Cases: none. Ninjobs is not used. Exercises: unchanged.

**Out of scope.**

* The `/apply` turn of `orchestrator-tests` (8 of 100 at `c54d011`). It ran after the event functions existed, which would break en:330.
* A new run of a delivery on a clinic without slices. It would cost a new recorded experiment, and the finding asks for a baseline or a description, not a new run.
* The counts and the wording of en:333-341: `slice-imports` owns lines 334 and 341, and the other lines stay.
* Percentages. The chapter gives counts as "N of M", and so does this page.

**Done when.**

* [ ] The six counts are recounted by the method above and match the table, or the difference is recorded here.
* [ ] Both editions changed with the same meaning. Chapter 16 still opens with its value, with no filler and nothing useful cut, and every number is sourced.
* [ ] `grep -n "reading small\|leitura de um agente" book/*/16-testing-and-agents.md` finds nothing.
* [ ] `grep -n "Both turns ran\|Os dois turnos rodaram" book/*/16-testing-and-agents.md` finds nothing.
* [ ] Chapter 16 has five key points.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
