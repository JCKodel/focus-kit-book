# kit-proposals-ninjobs-phases

**Objective.** After this delivery the author, taking `work/kit-proposals.md` to focus-kit's repository, reads in item 9 what Ninjobs did in each phase, FOCUS required whole until its restart and the two principles kept after it, and the kit's three passages that need it. Found by `m19-review` (work/done/m19-review.md, F1: "Item 9 'Ninjobs took FOCUS whole ... the kit had it under the two principles' is superseded by ch07-ninjobs-focus (whole FOCUS before the restart, two principles after); the pending kit correction lives only in that page's Decisions"; E6: the kit's §3.5 text "FOCUS whole ... Ninjobs chose this" has no phase, and the kit's README says "Ninjobs took it whole").

**Behaviour.**

* Opening `work/kit-proposals.md`, the author finds item 9 under a heading for proposals the kit has not taken yet, separate from the eight that focus-kit 2026.10.18.1 took.
* Item 9 says Ninjobs required FOCUS whole on every feature until its restart on 2026-08-29, and after it kept the two principles, vertical slices and exceptions as values, without the four pieces on every feature; it cites ADR-0016's amendment `ch07-ninjobs-focus` and chapters 4, 6 and 7, which place each phase in its time.
* Item 9 says what 2026.10.18.1 took, the earlier phase with no date, and names the three kit passages to correct: SETUP.md §3.5, whose "FOCUS whole" answer ends "Ninjobs chose this"; README.md, "Ninjobs took it whole."; and README.pt.md, "O Ninjobs adotou inteira."
* Item 9 says the copies the kit installs in this repository follow the next kit version and are not edited here.
* Fails: item 9 still says the kit "had it under the two principles" or cites chapters 3, 4 and 6; it names a local path of the kit's repository or of this machine; items 1 to 8 or the file's opening paragraph change in meaning.

**Contract.** File: `work/kit-proposals.md` only. Items 1 to 8 and the opening paragraph stay. Item 9 leaves the list "Taken to focus-kit 2026.10.18.1, taught by M19 in docs/06:" and goes under a new line after that list, "For the next focus-kit version:", keeping its number, in substance:

    9. **Ninjobs in two phases** (from ch07-ninjobs-focus). Ninjobs required
       FOCUS whole on every feature until its restart on 2026-08-29, and
       after it kept the two principles, vertical slices and exceptions as
       values (ADR-0016's amendment ch07-ninjobs-focus; chapters 4, 6 and
       7). 2026.10.18.1 took the earlier phase alone, with no date: SETUP.md
       §3.5's "FOCUS whole" answer ends "Ninjobs chose this", README.md says
       "Ninjobs took it whole." and README.pt.md "O Ninjobs adotou inteira.";
       the next version says both phases in all three. The copies installed
       here follow it.

/apply may polish the wording within these limits. Sources: ADR-0016's amendment of 2026-10-18 (ch07-ninjobs-focus), work/done/ch07-ninjobs-focus.md's Decisions (the README sentences), work/done/m19-review.md E6 (SETUP.md §3.5). No chapter, no doc and no term of docs/03 changes; no Case A or Case B passage. Ninjobs appears by its process decisions and its restart date, both already published in the book.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.** Editing focus-kit's repository: the file is for the author to take there. The installed copies of the kit's text in this repository (the brainstorm skill's references and their siblings): they change with the next kit update, never by hand. Chapters 4, 6 and 7 and ADR-0016: already say both phases (ch07-ninjobs-focus).

**Decisions taken alone** (no person available, recommended answer taken). (1) Item 9 moves under a new heading instead of staying in the "Taken to 2026.10.18.1" list: what that version took is half of it, and the file's opening says an update milestone teaches what a kit version carries, so a correction the kit has not taken must not read as taught by M19. (2) It keeps the number 9, so m19-review's F1 and this page still point at it. (3) The kit's passages are named by file and section and quoted, never by a path or line number, as docs/04 names the kit's files in plain words.

**Done when.**

* [ ] `work/kit-proposals.md` edited as the Contract says, nothing else; each Behaviour line checked; `grep -n "under the two principles\|chapters 3, 4 and 6" work/kit-proposals.md` prints nothing.
* [ ] No local path in the file or this page; the disclosure scan green.
* [ ] No chapter changed, so no edition and no `make book` apply; no em dash.
* [ ] `make verify` green after the last edit.
* [ ] No delivery review: the author waived it for this round; /apply does not add one.
* [ ] Page archived to `work/done/` and commit message suggested.
