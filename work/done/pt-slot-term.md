# pt-slot-term

**Objective.** A Portuguese reader of chapter 6 reads invariant 2 and ADR-0005 as the English means them: an appointment lines up with the `slotMinutes` grid, a rule apart from "horário livre" (a free slot) and from the no-overlap rule.

**Behaviour.**

* In chapter 6's Portuguese excerpt of invariant 2, a slot of the grid is "intervalo": "Um agendamento começa em um intervalo: dentro de um dos períodos de trabalho do profissional, na grade de `slotMinutes` contada a partir do início do período, terminando no máximo no fim do período."
* In chapter 6's Portuguese excerpt of ADR-0005's Decision, the same word: "Os horários semanais são cortados em intervalos dessa duração, contados a partir do início de cada período de trabalho."
* Neither excerpt says "horário livre" any more; every other "horário(s) livre(s)" in the Portuguese edition means a free slot and stays (chapters 7, 12, 14 and 16).
* The English edition is unchanged: it already says "slot" for the grid.
* Finding F2 of the M4 review is settled.

**Contract.**

* Files: `book/pt/06-the-documents.md`, the invariant 2 code block (line 221 today) and the ADR-0005 Decision code block (line 235 today), those two sentences only. The blocks keep their line wrapping at about the English width; lines may re-wrap.
* Terms of docs/03: none new. "intervalo" is a translation choice for the clinic's excerpts, recorded here, not a row of docs/03: docs/03 holds the book's own vocabulary, it has no clinic domain term, and the clinic's documents are in English only. "slot" in Portuguese stays what docs/03 fixes, a docs/05 §5 fact, as chapter 6 uses it at lines 77 to 198.
* Sources, cases, exercises: unchanged.

**Out of scope.**

* The clinic's own ambiguity: its docs/03 defines `Slot` as "A free interval of one professional, derived from weekly hours minus booked appointments", while invariant 2 and ADR-0005 use "slot" for the grid. Splitting them is a change to the clinic, not to the book, and is not queued.
* A sentence in chapter 6 explaining grid slot versus free slot: the chapter does not show the clinic's `Slot` row.
* A docs/03 row for "intervalo": see Contract.
* The English edition: nothing to change.
* `ch3-key-point-ask`, in flight: chapter 3 only, no overlap.

**Done when.**

* [x] Both excerpts changed; `grep -n "horário livre\|horários livres" book/pt/06-the-documents.md` finds nothing.
* [x] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author: run once at the end of the M4.1 loop by the driver.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Both sentences changed as written, with no re-wrap: "intervalo" and "intervalos" fit the existing lines. The grep finds nothing in chapter 6; the other "horário(s) livre(s)" of the Portuguese edition stay.
* Line 314 of chapter 6 ("um horário que não está livre", `SlotTaken`) means a free slot and stays.
* `make verify` green. Staging and the commit are left to the driver of the M4.1 loop.
