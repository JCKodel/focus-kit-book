# ch07-review-git-slots

**Objective.** After chapter 7 a reader can say what docs/05's Milestone review slot chooses, who reads the code when a milestone closes (the host's deep review, the kit's readers by area, or no one), and what the Git slot may say about commits: the agent commits only when asked, or, by the slot's word, which counts as the asking, it commits and merges and the person reviews the commit; both editions.

**Behaviour.**

* Reading the ten-slot list, the reader learns that the Milestone review slot says who reads the code of the review that closes a milestone: the host's deep review, which the person launches over the milestone's range, when the host has one that takes the whole range; or the kit's readers, one read-only agent per area the slot names, on the model it names or the session's, with their checker; or no one.
* The reader who has not met either term understands both where they appear: the host's deep review is the host's own review that reads the whole range in one launch; the kit's readers split it by areas, one each.
* Reading the git strategy paragraph, the reader learns that in every strategy the agent stages and commits or merges only when asked, and that the Git slot may instead say the agent commits, and merges, by the slot's word, which counts as the asking, the person then reviewing the commit.
* The list still counts ten slots, and the Verify slot's slow tests kept for the milestone review stay as they are.
* Fails if: the chapter names a host's command, a model or a cloud; points to a later chapter outside the gain section (docs/04, chapters 0 to 7); says when a team should pick the commit-by-slot form, which no document says; names this repository's own choice; tells how the kit or the slot read before; or narrates a run.

**Contract.**

Chapter `book/en/07-the-documents.md` and `book/pt/07-the-documents.md`, the same passages in both:

* §docs/05, the process, the ten-slot list (en line 45, pt line 46): the item "the areas into which the review that closes a milestone splits its code reading and the model its readers and checker run on" (pt "as áreas em que a revisão que fecha um marco divide a leitura do código e o modelo em que os seus leitores e o conferente rodam") becomes one item saying who reads the code when a milestone closes: the host's deep review, the host's own review that reads the whole range in one launch, which the person launches; or the kit's readers, one read-only agent per area, on a model the slot names; or no one. pt: "a revisão profunda do host", "os leitores do kit", "o conferente". One item, so the count stays ten; every other item of the list stays.
* §The two choices, "The git strategy" paragraph, second sentence (en line 81, pt line 82): "reverts in one step" stays; the clause "and the agent never commits or merges on its own; asked, it takes the step the person names" keeps that as the default and gains the slot's other form, from the kit's slot template (`.claude/skills/analyze/references/documents.md`, Git slot): the agent stages, never commits or merges on its own, and asked takes the step the person names; or the Git slot says it commits, and merges, by the slot's word, which counts as the asking, and the person reviews the commit. pt: "pela palavra do slot, que vale como o pedido; a pessoa revisa o commit". /apply may split it into two sentences.
* "The Git slot of docs/05 records the answer, and an ADR records why." (en line 83, pt line 84): stays; the answer now includes which form of commit the slot takes, which the sentence before says.
* Nothing else changes: the opening, the Board slot, the docs/06 paragraph, question 6 ("how a delivery and a milestone are reviewed, git?"), the gain section and the five Key points (key point 2 names the strategies, not the commit form; key point 1 does not list slots one by one).

Terms of docs/03 used: milestone review, checker, slot, trunk; "host's deep review" and "kit's readers" are the wording of docs/05 §5 and §8 and of docs/03's `milestone review` and `checker` rows. No new docs/03 row. No number, no footnote, no private case, no lending library example added.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* The same absolute sentence elsewhere: chapter 6 line 64 (a quoted Ninjobs rule, history, stays), chapter 13 lines 163-165 ("never commits and never merges on its own, whatever the git strategy", and its quote of the kit's flow; another session's file in flight), chapter 19 line 191 ("as in every git strategy"). Not this line's; reported to the driver as a gap no M21 line names (ch18-19-one-index and ch20-one-person-assumed both defer the option to this line, which names chapter 7 only).
* What the host's deep review and the checker do in a review: chapter 15 (`ch15-who-reads`); chapter 7 gives the choice in the slot list only.
* Chapters 11 and 23's "by the areas docs/05 names": `ch11-23-who-reads`.
* This repository's own Milestone review and Git choices: a project's answer, not what the chapter teaches (ADR-0017; `work/ch15-who-reads.md`, Out of scope).
* docs/03, docs/05, docs/06, AGENTS.md: no edit; `kit-2026-10-19` already wrote them.

**Decisions from the documents.**

* The Milestone review slot's three answers and the gloss of the deep review: the kit's slot template (`documents.md`, Milestone review) and docs/05 §8 as `work/done/kit-2026-10-19.md` installed it.
* The commit form "by the slot's word, which is the asking; the person reviews the commit": the kit's slot template (`documents.md`, Git).
* Both terms are glossed where they appear and chapter 15 is not named: they appear in no chapter 0 to 7 yet, and docs/04 ("Teach, do not only show", "Chapter pointers") forbids a forward pointer outside the gain section there.
* No host command, model or cloud named: `work/ch15-who-reads.md` decision 1, chapters 8 and 9.
* No before/after, version or date: AGENTS.md, `work/done/kit-as-it-is.md`.
* The count stays ten: the kit template has ten (`documents.md` §5); `work/done/ch07-slots-and-decided.md`.

**Decisions taken alone.**

* The queue line's "this project's slot keeping commits on request" is read as: the chapter's present sentence is the commits-on-request form and stays as the default, and the change adds the slot's other form. The chapter does not say this book's repository keeps it, since that is a project's answer, not the choice taught. The driver may overrule it if the line meant the lending library's slot.
* The chapter does not say when a team picks the commit-by-slot form: no repository document gives a rule, and the kit's CHANGELOG case is another project's history, a before/after.
* Portuguese "pela palavra do slot, que vale como o pedido".
* The Git slot sentence (line 83) stays unchanged rather than gaining "and how the agent commits".

* /apply: the Milestone review item is one parenthesis of three answers separated by semicolons, so the comma list keeps ten items; it adds "one checker after either", since docs/03's `checker` row has one checker after the area readers or the host's deep review (review finding 2).
* /apply: the deep review's gloss says "reads all of the milestone's changes at once" (pt "lê todas as mudanças do marco de uma vez"), not "the whole range", a term chapters 0 to 7 do not use (review finding 1).
* /apply: the git paragraph keeps the default in its second sentence, adding "by default the agent stages" (pt "coloca em stage", as chapters 6, 8 and 9 say), and the slot's other form is a new third sentence.
* /apply: the Behaviour's "when the host has one that takes the whole range" is implied by "the host's own review" and not written; the Contract does not ask for it.

**Implementation.** `book/en/07-the-documents.md` and `book/pt/07-the-documents.md`: in the docs/05 paragraph, the ten-slot list's milestone item now says who reads the code when a milestone closes; in "The git strategy", the second sentence names the default and one new sentence gives the Git slot's commit-by-its-word form. Nothing else in the chapter changed. No shared file touched.

**Proof.** `make verify` green after the last edit. Both Done when greps find nothing; no em dash. `make book` is the driver's, run once at the end of the batch.

**Delivery review.** A read-only Explore agent on Opus read `git diff HEAD` of both chapter files, this page, AGENTS.md, docs/04, the kit's `documents.md` slots, docs/05 §8 and docs/03's rows. Ten slots counted, both editions parallel, no host command, model, cloud, pointer or before/after. Three findings, all fixed:

1. "the whole range" was a term the reader has not met. Fixed: "all of the milestone's changes".
2. The checker was tied to the kit's readers only. Fixed: "one checker after either".
3. "in one launch, which the person launches" repeated a word. Fixed: "at once, started by the person".

Verify ran again after the fixes: green.

**Divergences.** None from Behaviour or Contract beyond the wording decisions above.

**Done when.**

* [x] Both editions written, the same passages changed in each, Portuguese read as Portuguese.
* [x] The slot list still counts ten and names who reads a milestone's code, both terms glossed in place; the git paragraph gives both commit forms; nothing else in the chapter changed.
* [x] `grep -n -i -E "code-review|ultra|opus|fable|advisor|cloud|no longer|2026\.10|chapter 15|\(chapter 1[0-9]" book/en/07-the-documents.md` and `grep -n -i -E "code-review|ultra|opus|fable|advisor|nuvem|não mais|2026\.10|capítulo 15|\(capítulo 1[0-9]" book/pt/07-the-documents.md` find nothing; no em dash; no narrated run.
* [x] Delivery review as docs/05 §5 says.
* [x] `make verify` green; `make book` builds both editions and both PDF paths are reported (the driver runs `make book` once for the batch).
* [x] Only this delivery's paths and its hunk of docs/06 staged (staging is the driver's); the page moved to `work/done/` and its commit message suggested.

```commit
docs(ch07-review-git-slots): who reads a milestone, commit by slot

- chapter 7's slot list says who reads the code when a milestone closes
- the host's deep review and the kit's readers glossed where they appear
- the git strategy gives the Git slot's other form: commit by its word

work/done/ch07-review-git-slots.md
```
