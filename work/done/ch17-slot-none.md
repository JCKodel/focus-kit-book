# ch17-slot-none

**Objective.** After chapter 17 a reader knows that a Milestone review slot of `none` launches no deep review, and that the page still names the base commit, so the clause "or none when the slot says so" is no longer read as the value of `<base>`.

**Behaviour.**

* A reader of chapter 17 §The review is a delivery (the paragraph on the review's page) reads that the page names the commit that closed the previous milestone, or the first commit, and that when docs/05's Milestone review slot names a deep review, such as Claude Code's `/code-review ultra <base>`, the person launches it against that commit, which is `<base>`.
* The same reader reads, in the paragraph on a host with no such review, that the slot says `none` and no deep review is launched, while the hand test still runs and nothing else in the chapter changes.
* Failure: a reader who meets "where `<base>` is that commit, or none when the slot says so" takes `none` for a value of `<base>`, a commit that does not exist; the new sentence has `none` only as the slot's value.
* Edge: the base commit is still named by the page whatever the slot says, as docs/05 §8 has it; only the launching of the review depends on the slot.

**Contract.**

The finding was re-checked, not taken on trust: chapter 17 line 20 (en and pt) ends "where `<base>` is that commit, or none when the slot says so", which attaches "none" to `<base>`, while the kit's slot template (`<the command ... or: none>`, in the installed `analyze` and `brainstorm` references) and the chapter's own later paragraph (line 56 en, 57 pt) make `none` a value of the slot. It holds, as minor.

* **Chapter 17, both editions, file name, title and headings kept.**
  1. §The review is a delivery, the sentence ending "and the person launches against it the deep review that docs/05's Milestone review slot names, such as Claude Code's `/code-review ultra <base>`, where `<base>` is that commit, or none when the slot says so." becomes "Its page names the commit that closed the previous milestone, or the project's first commit for a first milestone; when docs/05's Milestone review slot names a deep review, such as Claude Code's `/code-review ultra <base>`, the person launches it against that commit, which is `<base>`." (pt, line 20: "A página dela cita o commit que fechou o marco anterior, ou o primeiro commit do projeto para um primeiro marco; quando o slot Milestone review (revisão de marco) do docs/05 cita uma revisão profunda do código, como o `/code-review ultra <base>` do Claude Code, a pessoa a lança contra esse commit, que é o `<base>`.")
  2. The paragraph "A project whose host offers no such review writes none in the slot, the hand test still runs, and nothing else in this chapter changes for it." becomes "A project whose host offers no such review writes none in the slot and launches no deep review; the hand test still runs, and nothing else in this chapter changes for it." (pt, line 57: "Um projeto cujo host não oferece uma revisão assim escreve none (nenhuma) no slot e não lança revisão profunda; o teste à mão continua rodando, e nada mais neste capítulo muda para ele.")
  3. Nothing else in chapter 17 changes.
* **Terms:** milestone review, as docs/03 has it; docs/03 unchanged.
* **Sources:** docs/05 §5 (Milestone review) and §8, the book's own copy of the process; the kit's slot template in its docs/05 (`or: none`), paraphrased with no note, as chapter 17 already does for the slot.
* **Cases:** none. Code examples: none; the `Milestone review: /code-review ultra <base>` block stays.

**Overlap with the deliveries in flight (docs/06 M15).**

* `method-said-once` lists chapter 17 as "no cut"; it does not touch these lines.
* `one-gain-section` removes "no baseline" sentences from chapter 17's gain and rewrites its key points; the key point that launches "the deep review docs/05's Milestone review slot names" is not changed here and is its to keep or rewrite.
* `renumber-chapters` moves "chapter 17" and the file links by script; this page adds none.
* `ch16-resume-apply` touches chapters 15 and 16 only; no shared line.
* `quick-guide` points to chapter 17 for "a milestone closes with its review"; no shared line.

**Out of scope.**

* The key point and the gain of chapter 17: `one-gain-section`.
* Whether the review's page names a base commit when the slot is `none`: docs/05 §8 does not say otherwise, and this page keeps the chapter's sentence that the page names it.
* docs/05 §5 and §8 wording: unchanged.

**Done when.**

* [x] Chapter 17 changed in both editions, same headings; it still opens with its value; no filler and nothing useful cut.
* [x] No sentence of chapter 17 in either edition puts `none` as a value of `<base>`; the none case is said once, in the paragraph on a host with no such review, and says no deep review is launched.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions in the review.**

* The sentence is split at the semicolon so that `none` appears only in the later paragraph, which already owns the case: docs/04's No filler and the author's "say once" rule for the book. Chosen alone.
* The base commit stays named by the page whatever the slot says, reading the queue line's "apart from the base commit" and docs/05 §8, which names the commit without conditioning it on the slot. Chosen alone; docs/05 §8.
* "launches no deep review" added to the none paragraph because the queue line asks the chapter to say it. Chosen alone, from the queue line.

**Decisions in /apply.** Chosen alone, under the batch's rule; corrections go in the review.

* The Contract's two sentences are taken as written, in both editions; each was found by its words, at the lines the page names (en 20 and 56, pt 20 and 57).
* No dependent queue line waits on this one; docs/03, docs/04 and docs/05 untouched, as the Contract says.

**What happened.**

* `book/en/17-closing-a-milestone.md` and `book/pt/17-closing-a-milestone.md`, §The review is a delivery: the page names the base commit, and the person launches the deep review against it when the Milestone review slot names one; `none` is no longer read as a value of `<base>`.
* The paragraph on a host with no such review says the slot's none launches no deep review, and the hand test still runs.
* Headings, opening, gain and key points unchanged. No divergence from the Contract.

**Proof.**

* `grep -n "none\|nenhuma" book/*/17-closing-a-milestone.md` shows the slot's none once per edition, in the paragraph on a host with no such review (en 56, pt 57); no sentence attaches it to `<base>`.
* `make verify` green, disclosure scan included; `make book` built both editions, and the PDFs are `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

```commit
docs(ch17-slot-none): chapter 17 says a slot of none launches no review

- ch17: the page names the base commit; the slot's review is launched against it
- ch17: a slot of none launches no deep review, said once
- both editions

work/done/ch17-slot-none.md
```
