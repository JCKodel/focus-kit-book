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

* [x] Both editions changed; the section says nothing chapter 9 already says, beyond the pointer.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

## What happened

* English: "Between the two commands the line reads `[>]`: the page exists and the build does not; [chapter 9](09-queue-and-milestones.md) says where the page waits." The unit of work sentence is unchanged, and the section ends with "The clinic is on trunk, which is why the run below leaves the page uncommitted." Portuguese says the same.
* Dropped: the sentence on trunk, the waiting page, a branch and one merge, and "Part IV teaches the git side", both already in chapter 9's paragraph, which ends with that pointer to Part IV.
* Nothing else diverged from the plan, no document changed: no new term, no rule, no decision. F12 of the M3 review is settled.
* Proof: `make verify` green, `make book` built both PDFs.
