# ch14-feature-boundary

**Objective.** A reader of chapter 14 can decide what makes one feature in their own code: one thing the app keeps, with every action on it. They can also say why the clinic's appointments slice holds cancelling while weekly hours and professionals have slices of their own.

**Behaviour.**

* §"Vertical slices" states the rule: a feature is one thing the app keeps, named by a term of the project's docs/03 (the appointment, the professional, the weekly hours), and its slice holds every action on it.
* The same place shows the rule on the clinic. Booking and cancelling both act on the appointment, so they share its rules (`rules.ts`), its SQL (`repository.server.ts`), its routes (`route.server.ts`), its calls (`api.ts`) and the list the phone remembers (`remembered.ts`), and they are one slice. Weekly hours and professionals are other things the clinic keeps, each with its own table and screen, so each has a slice.
* The sentence "A change to booking touches this folder, and removing booking removes this folder." (en/14:53, pt/14:53) no longer implies that removing booking would remove cancelling. It speaks of the appointment instead.
* The slice is called "the appointments slice" ("a fatia dos agendamentos" in Portuguese) wherever the book names it, the same as the folder's name.
* The first key point carries the rule. Chapter 14 keeps five key points.
* Exercise 14.3 (absences: a folder of its own or a subfolder of `weeklyHours`) can be answered with the rule. Its text is unchanged.
* Both editions say the same.
* Finding F3 of the M4 review is settled.

**Contract.**

* Files:
  * `book/en/14-errors-and-slices.md`: line 19 ("booking slice"), line 53 (replaced by the rule and its evidence, before the health slice), and the first key point, line 246.
  * `book/pt/14-errors-and-slices.md`: the same places, lines 19, 53 and 246.
  * `book/en/15-four-pieces.md:50`: "in the booking slice" becomes "in the appointments slice".
  * `book/pt/15-four-pieces.md:51`, `book/pt/16-testing-and-agents.md:27`, `:179` and `:329`: "fatia do agendamento" becomes "fatia dos agendamentos".
  * Chapter 16 in English already says "appointments slice" and is not touched.
* Terms of docs/03: none new. The "vertical slice" row's meaning gains the rule: a feature is one thing the app keeps, with every action on it.
* Sources: none new. The files named come from `git ls-tree` at `book-v1/closing-a-milestone`, the listing the section already shows, and the tables and screens come from the clinic's docs/03 and docs/01 at that tag.
* Cases: none. Exercises: unchanged.

**Out of scope.**

* Whether a slice may import another slice's code, such as `slotsOf` importing the repositories of three other slices, and when that code moves to `src/lib/`: that is the later line `slice-imports`.
* Chapter 7's transcript "Code is grouped by feature (book, cancel, weekly hours…)" (en/07:117, pt/07:118): it is a real quoted artifact, and the author chose not to mention it.
* Why cancelling is not a sub-feature subfolder: the rule already answers it, because cancelling acts on the same thing.
* The clinic's own docs/01, which does not define a feature: the clinic repository is not touched.
* The other findings on chapter 14 (`ch14-refusal-io`, `ch14-catch-all`, `pt-health-slice`): each has its own line.

**Done when.**

* [ ] Both editions changed with the same meaning. Chapter 14 opens with its value, with no filler and nothing useful cut.
* [ ] No "booking slice" or "fatia do agendamento" is left in `book/`.
* [ ] The "vertical slice" row of docs/03 updated.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
