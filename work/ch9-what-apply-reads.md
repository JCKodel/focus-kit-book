# ch9-what-apply-reads

**Objective.** A reader of chapter 9 knows what a fresh session running `/apply` relies on to find the page: the file `work/<slug>.md` in the working tree, committed or not.

**Behaviour.**

* In §"The queue" (the paragraph after the marks), the sentence that begins "It is how a fresh session running `/apply` knows the page exists" is rewritten with no pronoun: `/apply` is given the slug and reads `work/<slug>.md` from the working tree, so it finds the page whether or not the page was committed.
* The paragraph keeps what it says about trunk and a branch, and ends with the pointer to Part IV.
* Both editions say the same.
* Finding F11 of the M3 review is settled.

**Contract.**

* Files: `book/en/09-queue-and-milestones.md` and `book/pt/09-queue-and-milestones.md`, lines 35 and 36 today.
* What the text claims matches the kit: `apply/SKILL.md` opens with "Implement `work/$ARGUMENTS.md`". No quote of it is needed.
* Terms of docs/03: page, fresh session, trunk. No new term.
* Sources, cases, exercises: unchanged.

**Out of scope.**

* Chapter 10's §"One unit of work", which repeats this paragraph: `ch10-unit-of-work`, applied after this one.

**Done when.**

* [ ] Both editions changed, same meaning; no "It" whose antecedent is unclear.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
