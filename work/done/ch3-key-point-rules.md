# ch3-key-point-rules

**Objective.** A reader who keeps only chapter 3's key points learns what the run showed about rules written once per project: Spec Kit wrote them, in its constitution, and nothing in the chapter shows OpenSpec writing any.

**Behaviour.**

* The third key point credits both tools with the decision written before code in files the agent reads, and credits only Spec Kit with rules written once per project, in its constitution, as §"Some decisions are written once per project" shows.
* No key point says or implies that OpenSpec's once-per-project files hold rules; the key point says nothing of those files that the chapter does not show.
* The clause on asking, settled by ch3-key-point-ask (only OpenSpec asked; Spec Kit, on its default path, asked nothing and wrote its answer under "Assumptions"), keeps its meaning.
* Both editions say the same.
* Finding F3 of the M4.1 review is settled.

**Contract.**

* Files: `book/en/03-spec-driven.md` (line 195 today) and `book/pt/03-spec-driven.md` (line 275 today), that key point only.
* Terms of docs/03: none new. "Constitution" is Spec Kit's name for its file, as the body uses it at line 83 (English) and "constituição" at line 84 (Portuguese).
* Sources: none new; key points carry no notes, and the body's `[^spec-driven-run]` already cites the run's folder, where `openspec/once/` holds what OpenSpec wrote once per project.
* Cases: none. Exercises: unchanged.

**Out of scope.**

* Adding to §"Some decisions are written once per project" what OpenSpec's three once-per-project files hold (`config.yaml`, whose rules and context are only commented examples, and two `.gitkeep` files): the line asks the key point to say only what the section shows, not the section to show more.
* The fifth key point's "documents written once per project" and line 188's "decide once per project": both speak of focus-kit's trade and credit OpenSpec with nothing.
* The table's OpenSpec "once per project" row: it counts files, it claims no rules.
* The chapter's opening sentence: it names what the tools got right without crediting OpenSpec with rules.

**Done when.**

* [x] Both editions changed, same meaning; no other paragraph touched.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author. Left for the batch driver, which builds once at the end of the loop. Done by the driver on 047d672: both editions build.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Revalidated against the tree: the key point was still at line 195 (English) and 275 (Portuguese); the constitution sentence still at lines 83 and 84.
* English now reads "and Spec Kit also wrote rules once per project, in its constitution"; Portuguese "e o Spec Kit também escreveu as regras uma vez por projeto, na sua constituição". The clause on asking is untouched.
* Decision taken alone (batch, no conversation): keep one sentence and add Spec Kit as the subject of the rules clause, rather than splitting the key point in two; it is the smallest change that credits OpenSpec with nothing the section does not show.
* No document changed: no new term, rule or decision.
* `make verify` green. `make book` not run here, by the batch's instruction.
