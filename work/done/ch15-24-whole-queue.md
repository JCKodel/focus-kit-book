# ch15-24-whole-queue

**Objective.** After chapter 15 a reader knows that `/apply` reads the whole queue, why that read stays small (a line is one sentence), that `[x]` is its last edit, after the stage, and that the last thing it says is which environment is at which version and the command that updates the others; chapter 24 counts the cost of context with the same facts.

**Behaviour.**

* A reader opening `/apply lend-book` knows from chapter 15 that the session reads the page, `AGENTS.md`, docs/01, docs/04, docs/05 and all of docs/06, and knows why the queue is read whole: to see that the lines its `· after` names are `[x]` before starting, and to name the next free line at the end.
* Failure: a reader who shortens their queue by moving lines into another file, "so `/apply` reads less". Chapter 15 answers: what keeps the read small is each line being one sentence (chapter 13), not reading fewer lines.
* A reader watching `/apply` end sees this order and knows it is the kit's: the `commit` block on the page and in the conversation; the next steps (review the staged diff, commit, merge on a delivery branch, the queue's next line in a fresh session, written as the host invokes it); then, as the very last words, which environment is at which version and the command that updates the others. A session that ends without that last sentence did not end as the kit says, and the reader asks for it.
* A reader checking the queue while `/apply` runs sees `[*]` from its first edit and `[x]` as its last, after the stage; a line marked `[x]` with nothing staged is a session that stopped early.
* Failure: a reader who opens the published site after a session that said "done" and finds it stale. Chapter 15 says the last sentence exists to prevent exactly that.
* A reader of chapter 24 who counts what rides along on every call knows the queue is in the read and that its size is governed by the one-sentence line; the cache-read number of the chapter is unchanged.

**Contract.**

* **Chapter 15, both editions, file name, title and headings kept.**
  1. Opening, third sentence: "and your next steps written out" gains "and, last of all, which environment is at which version".
  2. "What it reads": the sentence "Of docs/06, the queue, it reads only the lines that name its slug and the heading of their milestone." and the one after it ("The queue is the one document it does not read whole: ...") are replaced by: it reads docs/06 whole, to see that the lines its `· after` names are done before it starts, and to name the next free line when it ends; what keeps that read small is the line itself, one sentence and its suffixes (chapter 13), so the queue grows with every delivery and each line costs what one sentence costs. The `[*]` sentence stays and gains "its first edit".
  3. "Green is not done", the bullet on moving the page: "turns the line's mark in docs/06 from `[*]` to `[x]`" moves to the end of the list as its own bullet: the last edit marks the line `[x]` and stages that hunk, after everything else is staged. The parenthesis on `[?]` lines going back by their resume phase drops "and its page is still complete, otherwise to `[ ]`": `resume: apply` goes back to `[>]`, as docs/05 §4 says. The "Its last words" bullet becomes two sentences: the next steps (review the staged diff, commit, merge on a delivery branch, the next line in a fresh session, in the host's form); then the last thing it says, which environment is at which version and the command that updates the others, never silent about it.
  4. "`lend-book`, built": "marks the line `[x]`, and stages only this delivery's paths and its own hunk of docs/06" becomes: stages only this delivery's paths, and, as its last edit, marks the line `[x]` and stages that hunk. The paragraph after the `commit` block is reordered: first the three next steps, then one closing sentence, written for the chapter, in the shape the kit asks: the development database runs this delivery's migration, the staging environment is at the previous delivery, and the command that updates it, `npm run migrate -- staging` (written for the chapter, on the lending library).
  5. "What the team gains": gains one error prevented, in the present: a person who opens a published environment believing it current, after a session that ended without saying it was not; the last sentence of `/apply` prevents it. No number.
  6. Key points: the second point reads "It marks the line `[*]` with its first edit, `[x]` with its last, after the stage, and `[?]`..."; the sixth point reads: its last words are your next steps and, last of all, which environment is at which version and the command that updates the others.
* **Chapter 24, both editions**, "Where the context goes" (the section holding line 63): the sentence "Of the queue, `/apply` reads only the lines that name its slug and their milestone's heading, because what it reads at the start rides along on every call of the session: the queue grows with every delivery, and the build's context does not grow with it." becomes: the queue is in that read, whole, and what it reads at the start rides along on every call of the session; the queue grows with every delivery, so each line holds one sentence (chapter 13), and the read grows by a sentence per delivery, not by a page. Key point: "and `/apply` reading its own queue lines, not the queue, keep small" becomes "and one-sentence queue lines keep small". The 43.1 M figure and every other number stay.
* **Chapter 16, both editions**, one sentence: "A line with `resume: apply` goes back to `[>]` only if its page still answers every section, and otherwise to `[ ]`, with what `/propose` must settle." and the sentence after it become: a line with `resume: apply` goes back to `[>]`; if the answer that freed it changed what its page must say, the person asks `/propose` for the page first, as with any page that no longer holds. (Included here because chapter 15's bullet and chapter 16 say the same rule; one delivery keeps them equal.)
* **Portuguese:** "a última coisa que diz" for the last words; "ambiente" and "versão" as docs/03 has them; `npm run migrate -- staging` stays.
* **Terms:** none new; `environments` slot as docs/05 §5 has it.
* **Sources:** SETUP.md's /apply skill (reads docs/06; `[*]` first edit, `[x]` last after staging; the last thing you say) and docs/05 §2 and §4; the kit's changelog paraphrased with no note, present tense, no version: the queue read whole so `after` and the next line are seen, and the person who opened a published site believing it current.
* **Cases:** Ninjobs, by kind only, as the changelog tells it (a site opened believing it current); no date, no site.
* **Code examples:** the existing `commit` block and next steps, plus the one closing sentence written for the chapter.

**Out of scope.**

* docs/05 §2, §4, §5's Publish policy last sentence and the skills of this repository: `kit-2026-10-16-2`.
* Chapter 13's rule that a line is one sentence: unchanged; chapter 15 points to it.
* Chapter 24's measured numbers and its method: unchanged; only the sentence on what `/apply` reads changes.
* Chapter 11's update report: `ch11-update-2026-10-16-2`.
* A new run measuring the read: the kit's reason is the evidence (ADR-0017).

**Done when.**

* [x] Chapters 15, 16 and 24 changed in both editions, same headings; chapter 15 still opens with its value; no filler and nothing useful cut.
* [x] No sentence in the book says `/apply` reads only its own queue lines, or that `[x]` comes before the stage, or that `resume: apply` may return a line to `[ ]`; `grep -rn "only the lines\|own queue lines\|só as linhas\|suas próprias linhas" book/` finds nothing.
* [x] The order of `/apply`'s ending in chapter 15 matches SETUP.md's /apply skill as `kit-2026-10-16-2` installs it.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* Trunk, no branch: docs/05 §5 Git.
* The read of the whole queue, the mark timing and the last sentence: SETUP.md's /apply skill and docs/05 §4's "a mark changes at once".
* The environment sentence written for the chapter on the lending library, said so: docs/04, Evidence.
* Chapter 16's resume sentence changed here, not in a line of its own: it is the same rule chapter 15's bullet states, and two chapters stating one rule change in one delivery (precedent: `ch13-16-queue-order`).
* The error prevented said in the present with no version: docs/04, the kit as it is.

**Decisions in the review.**

* Chapter 15's example ends with a development and a staging environment, as recommended.

**Built.**

* Chapter 15, both editions: the opening's third sentence ends on "and, last of all, which environment is at which version"; "What it reads" reads docs/06 whole, for `· after` and the next free line, with the one-sentence line (chapter 13), not a shorter queue, as what keeps the read small, and `[*]` as the first edit; "Green is not done" gains its own bullet for the last edit, `[x]` and its hunk staged after everything else, drops "and its page is still complete, otherwise to `[ ]`", and its last-words bullet gives the next steps, then the environments as the last thing said; the example stages its paths, then marks `[x]` as its last edit, gives the three next steps, then closes on the development database, the staging environment and `npm run migrate -- staging`, written for the chapter; the gains name a fourth error, the published site opened believing it current; key points two and six as the Contract says.
* Chapter 16, both editions: `resume: apply` goes back to `[>]`, and a page the answer changed goes to `/propose` first.
* Chapter 24, both editions: the queue is read whole and stays small by its one-sentence lines; the key point says "one-sentence queue lines". No number changed.

**Divergences.**

* Chapter 24: the Contract calls the section "Where the context goes"; its heading is "Why the page and the documents keep sessions small". The sentence at line 63 changed and the heading stayed.
* Chapter 15, "Green is not done": the `[x]` bullet ends the list of edits, before the last-words bullet, not after it, since the words come after the last edit; putting it after them would make the list say the environments are not the last thing.
* Chapter 15, the `[?]` parenthesis: dropping "otherwise to `[ ]`" left `resume: propose` unsaid, so it reads both phases, `[ ]` for `resume: propose` and `[>]` for `resume: apply`, as docs/05 §4 does; and "lines now `[x]`" became "this one, or lines already `[x]`", since this line is marked `[x]` only at the very end.
* Chapter 15, "Done is that whole list": the line `[x]` moved to the end of the list, so no sentence of the chapter puts `[x]` before the stage.
* Chapter 15, the example: after the closing sentence, one line tells the reader to ask for it when a session ends without it, in the shape the chapter already uses for a missing `commit` block (Behaviour, third scenario).
* Chapter 15's gains: the Ninjobs case is the published site opened believing it current, by kind, with no count, date or site.

**Proof.**

* `make verify` green (build, parity, em dash, prose, links, disclosure).
* `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`, given to the author.
* `grep -rn "only the lines\|own queue lines\|só as linhas\|suas próprias linhas" book/` finds nothing; the wider sweep with "próprias linhas da fila", "e mais nada", "does not read whole" and "não lê inteiro" finds nothing about the queue.
* Chapter 15's ending, in order: the `commit` block on the page and in the conversation, the next steps, then the environments and the command that updates the others, as `.claude/skills/apply/SKILL.md` at 2026.10.16.2 says; `[*]` first edit and `[x]` last after staging, as that skill and docs/05 §4 say.

**Decisions.**

* This repository's docs/05 §4 keeps "If scope became undecided, return `[ ]`", a project choice `kit-2026-10-16-2` preserved; the kit's own §4 at `70fc709` has no such sentence, and the book teaches the kit, so chapters 15 and 16 follow the kit and docs/05 stays out of scope as the page says. Not a contradiction between page and document: they describe different things.
* No document, ADR or manual changes: docs/05 §§2, 4 and 5 and the skills already say what the chapters now teach.

```commit
docs(ch15-24-whole-queue): teach the whole queue and the last sentence

- chapter 15: /apply reads docs/06 whole; one-sentence lines keep it small
- chapter 15: `[x]` is the last edit, after the stage
- chapter 15: the last thing said is which environment is at which version
- chapter 16: `resume: apply` goes back to `[>]`
- chapter 24: one-sentence queue lines keep the read small

work/done/ch15-24-whole-queue.md
```
