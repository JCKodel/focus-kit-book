# ch10-unit-of-work

**Objective.** A reader of chapter 10 reads, in §"One unit of work", only what chapter 9 did not say: the page and its build are one change that reverts in one step, with a pointer to chapter 9 for where the page waits.

**Behaviour.**

* §"One unit of work" keeps: the line reads `[>]` between the two commands, pointed to chapter 9; the page and its build are one unit of work, as the kit's `references/documents.md` says, one change that reverts in one step; the clinic is on trunk, which is why the run below leaves the page uncommitted.
* It drops the sentence that repeats chapter 9 on trunk, the uncommitted page, a branch and one merge, and its "Part IV teaches the git side", which chapter 9 already says.
* Both editions say the same.
* Finding F12 of the M3 review is settled.

**Contract.**

* Files: `book/en/10-propose.md` and `book/pt/10-propose.md`, §"One unit of work" only, lines 68 to 73 today.
* Terms of docs/03: unit of work, page, trunk. No new term.
* Sources, cases, exercises: unchanged.
* Order: applied after `ch9-what-apply-reads`, so the pointer lands on chapter 9's rewritten paragraph.

**Out of scope.**

* Chapter 9's paragraph: `ch9-what-apply-reads`.

**Done when.**

* [ ] Both editions changed; the section says nothing chapter 9 already says, beyond the pointer.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
