# ch3-key-point-ask

**Objective.** A reader who keeps only chapter 3's key points learns what the run showed about asking: OpenSpec asked a question before writing, and Spec Kit, on its default path, asked nothing and wrote its answer as an assumption.

**Behaviour.**

* The third key point credits both tools with two things, the decision written before code in files the agent reads and rules written once per project, and credits only OpenSpec with a question asked before writing.
* The same key point, or the next clause, says that Spec Kit asked nothing on its default path and wrote its answer under "Assumptions", as §"What they got right" says.
* No key point says or implies that Spec Kit asked a question in the run.
* Both editions say the same.
* Finding F1 of the M4 review is settled.

**Contract.**

* Files: `book/en/03-spec-driven.md` (line 195 today) and `book/pt/03-spec-driven.md` (line 275 today), that key point only.
* Terms of docs/03: none new. The Portuguese keeps "Assumptions" with "(suposições)", as its body does at line 94.
* Sources: none new; key points carry no notes, and the body's `[^spec-driven-run]` and `[^spec-kit]` already cite the run and the optional clarification step.
* Cases: none. Exercises: unchanged.

**Out of scope.**

* The body of §"What they got right", its bold line "The tool asks before it writes." and the chapter's opening sentence: the body already draws the contrast; the finding is the key point.
* Whether OpenSpec's once-per-project files hold rules as Spec Kit's constitution does: not a finding of the M4 review.
* Naming Spec Kit's optional `/speckit-clarify` in the key point: the body says it; the key point says only what the run did.

**Done when.**

* [x] Both editions changed, same meaning; no other paragraph touched.
* [x] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author: run once at the end of the M4.1 loop by the driver.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* The third key point now credits both tools with the decision written before code and the rules written once per project, and only OpenSpec with the question; the same bullet says Spec Kit, on its default path, asked nothing and wrote its answer under "Assumptions". Nothing diverged from the page.
* The Portuguese keeps "Assumptions" with "(suposições)", as its body does.
* Finding F1 of the M4 review is settled.
