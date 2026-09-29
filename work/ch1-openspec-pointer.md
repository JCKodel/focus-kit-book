# ch1-openspec-pointer

**Objective.** A reader of chapter 1 can judge the Ninjobs count, 35 OpenSpec changes and 37,228 lines of spec, because the sentence says in a few words what a spec and an OpenSpec change are and points to chapter 3, where OpenSpec is explained.

**Behaviour.**

* In §"Too much process fails too", the Ninjobs sentence, or the one after it, says what the counted things are: OpenSpec is a tool that has the agent write, for each change, a folder of documents, specs among them, that describe what to build before the code.
* The pointer names chapter 3 for what OpenSpec is and keeps chapter 4 for the story of how focus-kit came out of Ninjobs.
* Both editions say the same; the Portuguese uses "spec" and "change" as it does today, since chapter 3 introduces them in those words.
* Finding F1 of the M3 review (`work/done/m3-review-run/findings.md`) is settled.

**Contract.**

* Files: `book/en/01-why-process.md` and `book/pt/01-why-process.md`, §"Too much process fails too" only, lines 62 and 63 today.
* Terms of docs/03: spec, as defined there. No new term.
* Sources: the existing `[^ninjobs]` note; no new note. The gloss agrees with chapter 3's own description of OpenSpec (`book/en/03-spec-driven.md:25`), and a link to chapter 3 is a relative link, `03-spec-driven.md`.
* Cases: Ninjobs, unchanged. Exercises: none; chapter 1 has none.

**Out of scope.**

* The numbers themselves: already sourced by `[^ninjobs]`.
* Explaining Spec Kit or SDD in chapter 1: chapter 3's job.

**Done when.**

* [ ] Both editions changed, same meaning; no other section touched.
* [ ] The sentence stays one reading: what the lines are, then where to learn more.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
