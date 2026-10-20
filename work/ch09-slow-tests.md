# ch09-slow-tests

**Objective.** After chapter 9 a reader knows that `/brainstorm`'s process slots include the slow tests kept out of the verify command, and that `/analyze` infers which tests are slow enough to leave out of it, as the kit's files for the two commands and chapter 7 say.

**Behaviour.**

* A reader who runs `/brainstorm` on the empty lending library repository expects its fifth subject, the process slots, to cover the verify command and the slow tests kept out of it, before the environments; on a project with no code yet, the answer is "none" or "created by the first delivery", as the chapter's "A default with every question" says of what cannot be known yet.
* A reader who reads chapter 7's Verify slot ("the command that verifies a delivery, with the command of any slow tests kept out of it for the milestone review") and then chapter 9's list finds the two agreeing: chapter 9 no longer lists the verify command alone.
* A reader who runs `/analyze` on a repository whose CI runs an end-to-end suite separately expects the agent to infer, beside the verify command and the environments, which tests are slow enough to leave out of verify, and to mark it observed like the rest.
* Failure: a reader reviewing `/brainstorm`'s docs/05 finds the Verify slot naming a command and saying nothing about slow tests. From chapter 5 and chapter 7 they know the slot says the command of the slow tests or that there are none, and ask the agent, in the same session, to add it.
* Edge: a project with no slow test has a Verify slot that says so; chapter 9 adds no new rule for it, chapter 5 :40 already says "or that there are none".

**Contract.**

* **Chapter 9, `book/en/09-starting-a-project.md` and `book/pt/09-starting-a-project.md`; headings unchanged.**
  1. `/brainstorm`'s fifth subject (en :22, pt :22): the first item "the verify command" becomes "the verify command and the slow tests kept out of it"; pt "o comando de verificação" becomes "o comando de verificação e os testes lentos que ficam fora dele". The rest of the sentence is left as it is when this delivery starts.
  2. `/analyze`'s "What it reads" (en :76, pt :76): "the verify command and the environments" becomes "the verify command, which tests are slow enough to leave out of it, and the environments"; pt "o comando de verificação e os ambientes" becomes "o comando de verificação, quais testes são lentos o bastante para ficar fora dele, e os ambientes". The rest of the sentence unchanged.
  3. Nothing else in the chapter changes: the review bullets, "What the team gains" and the Key points do not list the slots one by one, so none goes stale.
* **Neighbouring line on the same file:** `ch07-09-manual-wording` edits chapter 9's same sentence at pt :22 ("a cargo da" in the manuals clause) and comes first in queue order. This delivery touches only the verify clause at the start of that sentence and takes the sentence as that delivery leaves it.
* **Terms:** verify, slot, milestone review, as docs/03 has them; docs/03 unchanged. The Portuguese "testes lentos que ficam fora dele" is chapter 7 pt :46's wording.
* **Sources:** the kit's `brainstorm` skill at 2026.10.19.2 ("verify command and the slow tests kept out of it") and `analyze` skill ("which tests are slow enough to leave out of it"), named in plain words as "the kit's file for the command", no note (docs/04).
* **Cases:** none; no Case A or B, Ninjobs unchanged.
* **Code examples:** none.

**Out of scope.**

* The manuals clause of the same sentence and chapters 7 and 8: `ch07-09-manual-wording`.
* Chapter 7's Verify slot and chapter 5's slow tests: already say it (the review's K2 cites chapter 7 :45 as agreeing).
* :38's "a verify command before any code exists": still true; adding slow tests there is an example, not a correction.
* docs/05, docs/03 and the skills: the finding is the chapter's omission only.

**Done when.**

* [ ] Chapter 9 changed in both editions as the Contract says, same headings; it still opens with its value; no filler and nothing useful cut.
* [ ] No sentence in chapter 9 lists `/brainstorm`'s process slots or `/analyze`'s inferences with the verify command and without the slow tests.
* [ ] No numbers, no history of the kit, no run narrated; no em dash.
* [ ] `make verify` green; `make book` built both PDFs, their paths given to the author.
* [ ] Page in `work/done/`, the commit suggested in a `commit` block; the line's `[x]` and the staging by paths and hunk are the driver's steps.

**Decisions taken from the documents.**

* The wording follows the kit's `brainstorm` skill item 5 and chapter 7 en :45 / pt :46, which the review's K2 names (work/done/m23-review.md).
* Both editions in the same delivery (ADR-0004); the book describes the kit as it is today.

**Decisions taken alone.**

* `/analyze`'s "What it reads" (:76) is included: the same omission against its skill ("which tests are slow enough to leave out of it"), a sibling sentence the review did not cite and no other line owns. The author may drop it in review; the line's wording would then stay as is.
* The queue line's wording is unchanged; it names `/brainstorm` only, and the `/analyze` sentence is recorded here as the sibling.
* :38's example is left as it is (Out of scope).
