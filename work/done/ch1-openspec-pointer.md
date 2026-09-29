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

* [x] Both editions changed, same meaning; no other section touched.
* [x] The sentence stays one reading: what the lines are, then where to learn more.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* English: after the Ninjobs sentence, a new one says what OpenSpec writes and points to chapter 3 by a relative link: "OpenSpec is a tool that has the agent write, for each change, a folder of documents, specs among them, that describe what to build before the code; [chapter 3](03-spec-driven.md) explains it." The pointer to chapter 4 stays, and now names "the Ninjobs story", since "that story" would have followed the OpenSpec sentence.
* Diverged, by decision of the author during /apply: the Behaviour line on the Portuguese rested on a wrong premise. Chapter 3 in Portuguese does not say "spec" and "change"; it says "especificações" and "uma pasta por mudança" (`book/pt/03-spec-driven.md:25`), and docs/03 gives "especificação" for spec. The Portuguese count now reads "35 mudanças do OpenSpec" and "37.228 linhas de especificação", and the new sentence uses the same words as chapter 3. The `[^ninjobs]` note, which says "changes pelo arquivo do OpenSpec", was left as it is: the Contract allows no change to it, and there it names the tool's own archive.
* Nothing dropped. No document changed: docs/03 already holds the term.
* Proof: `make verify` green; `make book` builds both editions, and the new sentences read in both PDFs as one reading, the count, what the lines are, then chapter 3 and chapter 4.
