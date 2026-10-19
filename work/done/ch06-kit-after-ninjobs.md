# ch06-kit-after-ninjobs

**Objective.** After chapter 6 a reader can say that Ninjobs' 91 deliveries ran on Ninjobs' own two commands, and that focus-kit, pulled out of them, was planted in Ninjobs on 2026-09-21, after the public opening, so every Ninjobs number the chapter gives comes from before the kit existed; both editions.

**Behaviour.**

* Asked what ran Ninjobs' 91 deliveries, the reader answers: Ninjobs' own `/propose` and `/apply`, the two commands of §Where it went, not the kit's.
* Asked when the kit arrived at Ninjobs, the reader answers: on 2026-09-21, after the opening of 2026-09-10, when the process was pulled out into focus-kit and the kit was planted back in Ninjobs.
* Asked whether the chapter's numbers (four screens, 29 checks, 91 deliveries, 19 boards, thirteen days) measure the kit, the reader answers no: they measure the process the kit was taken from, before the kit existed.
* Edge: the trigger of 2026-09-21, the drift between Ninjobs' command files and its docs/05, still reads as Ninjobs' own commands drifting, which is why the kit's commands hold no fact of the project.
* Fails if: the chapter says or implies the 91 deliveries or the opening ran on focus-kit; adds a number, a date or a source note; names the kit's version, its changelog or why the kit's README now says this; or narrates a run of this repository.

**Contract.**

Chapter `book/en/06-birth-of-focus-kit.md` and `book/pt/06-birth-of-focus-kit.md`, same passages in both:

* §Where it went (pt §Para onde foi):
  * "Two commands did the work: ..." says they were Ninjobs' own: en "Two commands of Ninjobs' own did the work: ...", pt "Dois comandos do próprio Ninjobs faziam o trabalho: ..."; the rest of the sentence stays.
  * The opening sentence, "Ninjobs opened to the public on 2026-09-10, thirteen days after the restart, with 91 one-page deliveries done.", gains that every one ran on those two commands (pt "todas nesses dois comandos" or as Portuguese reads best). The 19 boards sentence stays.
  * The 2026-09-21 paragraph: its first sentence gains "after the opening" and that the kit was then planted in Ninjobs (en "planted the kit back in Ninjobs", pt "plantei o kit de volta no Ninjobs"); one sentence follows saying that the chapter's numbers come from before that day, from the process the kit was taken from, not from the kit. The trigger sentence and "From then on the commands hold no fact of the project ..." stay.
* Opening, §How it was, §What went wrong, §Each rule and its failure, §What the team gains and the key points: unchanged; each stays true (the gain compares the old process with one page per delivery, not with the kit; key point 2 says "the least that held on Ninjobs").

Terms of docs/03 used: case (Ninjobs), delivery, queue, focus-kit; "planted" is the kit README's own word for installing it in a project, said in prose, not a new row. No new docs/03 row.

Sources the /apply checks (none becomes a source note: Ninjobs is a private repository, and the prologue says its numbers were counted by the author, docs/04):

* 91 deliveries at the opening: `work/done/rewrite.md` ("91 deliveries at the opening (its ADR-0026)"), `work/done/ch02-93-moment.md`, the chapter's own line 47; and the kit's `README.md` §Why this shape ("By mid-September 2026: 91 one-page deliveries").
* The deliveries ran on Ninjobs' own two commands: the kit's `README.md` §Why this shape ("Those deliveries ran on Ninjobs' own two commands, the ones this kit was extracted from") and `README.pt.md`; the kit's `CHANGELOG.md`, 2026.10.19 entry.
* Planted on 2026-09-21, after the beta: the kit's `README.md` ("The kit itself was planted in Ninjobs on 2026-09-21, after the beta") and `CHANGELOG.md` 2026.10.19; in this repository, `work/done/birth-of-focus-kit.md` ("adoption on 2026-09-21 (ADR-0026)", Ninjobs' ADR) and `work/done/useful-notes.md` (ADR-0026, dated 2026-09-21, "the adoption of focus-kit").
* The opening on 2026-09-10: the chapter's own line 47; the kit's `README.md` ("a public beta on 2026-09-10").

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* The kit's README and CHANGELOG, and why the kit now says this: the book teaches the kit as it is (docs/04, ADR-0017).
* The README's other Ninjobs figures (46 migrations, about 35k lines, 830 unit and 200 end-to-end tests): not in the line, and the chapter's case is told without them.
* Chapter 16 line 87 ("Ninjobs reached its public opening on a process of one page per delivery, two commands, ...") and chapter 22 line 28 ("built with the method this book teaches"): both say process or method, not kit, and stay true.
* Chapter 4's `[^ninjobs]` note (ADR-0026's date and the adoption): already consistent.
* docs/03, docs/05, docs/06: no change.

**Decisions from the documents.**

* The 91 deliveries ran on Ninjobs' own two commands and the kit was planted on 2026-09-21: the kit's README and CHANGELOG 2026.10.19, with this repository's `work/done/birth-of-focus-kit.md` and `work/done/rewrite.md` (Ninjobs' ADR-0026) for the date and the count.
* No source note: Ninjobs is a private repository, and docs/04 and the prologue (chapter 0 line 106) cover its numbers.
* No version, changelog or before/after in the text: docs/04, ADR-0017, and the driver's rule that the book teaches the kit as it is.
* Ninjobs appears only through its process artifacts and published numbers: AGENTS.md, docs/03.

**Decisions taken alone.**

* "After the beta" is said as "after the opening": the chapter calls 2026-09-10 the public opening and never says beta, and the kit README's "public beta on 2026-09-10" is the same day; no new term enters.
* "Planted the kit back in Ninjobs" and not "in place of its own commands": the sources say the kit was planted, not what it replaced, so the chapter claims no more.
* One sentence names what this means for the chapter's numbers (they come from before the kit): it is the reason the line exists, and without it the two facts stay disconnected. No count of days between the opening and 2026-09-21 is added, since no document states one.
* The edits stay in §Where it went; the gain section and key points are not touched, since none claims the kit ran Ninjobs.

**Done when.**

* [x] Both editions written, the same passages changed in each, Portuguese read as Portuguese, "o Ninjobs" with its masculine article (docs/03).
* [x] The chapter still opens with what the reader can do after it; no filler and nothing useful cut.
* [x] `grep -n -i -E "2026\.10|changelog|readme|no longer|beta" book/en/06-birth-of-focus-kit.md` and `grep -n -i -E "2026\.10|changelog|readme|não mais|beta" book/pt/06-birth-of-focus-kit.md` find nothing; no before/after, no narrated run, no em dash.
* [x] No number or date added; the ones kept (2026-09-10, 2026-09-21, 91) agree with the sources in Contract.
* [x] No private detail of Ninjobs beyond its process artifacts; the disclosure scan green.
* [x] Delivery review as docs/05 §5 says.
* [x] `make verify` green; `make book` and the two PDF paths are the driver's step, run once at the end of the batch.
* [x] Only this delivery's paths and its hunks of docs/06 staged: the driver's step (it owns docs/06 and the index); the page moved to `work/done/` and its commit message suggested.

**Divergences.**

* Contract asked for "Two commands of Ninjobs' own did the work"; the chapter says "Ninjobs' own two commands did the work", the same claim in the kit README's own phrasing, which reads better (review finding 2).
* Contract asked for a sentence saying the numbers come "from the process the kit was taken from, not from the kit"; the chapter says "The numbers in this chapter come from before that day, none of them from the kit." (pt "Os números deste capítulo vêm de antes desse dia, nenhum deles do kit."). The chapter's 37,228 lines of spec, four screens and 29 checks measure the earlier process, not the one the kit was taken from, so the narrower claim is the true one (review finding 1). The Behaviour bullet's grouping of four screens and 29 checks under "the process the kit was taken from" is read the same way: they are not kit numbers.

**Omissions.** None.

**Proof.** Both editions changed in §Where it went / §Para onde foi only: the two commands named as Ninjobs' own, the 91 deliveries said to have run on them, the 2026-09-21 sentence gaining "after the opening" and the planting, and one sentence that no number of the chapter comes from the kit. The Done when greps find nothing in either edition. `make verify` green after the last edit. Sources checked: the kit's `README.md` §Why this shape (lines 163-169) and `README.pt.md`; `work/done/rewrite.md`, `work/done/birth-of-focus-kit.md`.

**Review.** One read-only Opus agent read `git diff HEAD` of the two chapter files and this page against the page and docs/04. Findings: (1) "from the process the kit was taken from" is not true of every chapter number: fixed as in Divergences; (2) "Two commands of Ninjobs' own" awkward: fixed; (3) pt "todas nesses dois comandos" elliptical: now "todas feitas com esses dois comandos"; (4) optional, move the numbers sentence to the end of the paragraph: not taken, the Contract places it after the first sentence and the trigger still reads as Ninjobs' own commands drifting.

**Decisions taken alone during /apply.**

* Took review findings 1 to 3 and declined 4, as Review says.
* Portuguese wording: "Dois comandos do próprio Ninjobs faziam o trabalho", "todas feitas com esses dois comandos", "depois da abertura", "plantei o kit de volta no Ninjobs".

```commit
docs(ch06-kit-after-ninjobs): Ninjobs ran on its own commands

- chapter 6: the two commands and the 91 deliveries were Ninjobs' own
- the kit was planted in Ninjobs on 2026-09-21, after the opening
- no number in the chapter comes from the kit; both editions

work/done/ch06-kit-after-ninjobs.md
```
