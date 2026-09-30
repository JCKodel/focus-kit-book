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

* [ ] Both editions changed, same meaning; no other paragraph touched.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
