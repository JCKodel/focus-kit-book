# ch15-first-commit

**Objective.** A reader of chapter 15 can name a milestone review's base for any milestone: the commit that closed the previous milestone, or the project's first commit, which makes the review read the whole project, for a first milestone or for a later one whose earlier reviews left part of the project unread, as docs/05 §8 gives it; both editions. Found by `m15-review` (work/done/m15-review.md, K2: "15:19, both editions: the first commit \"for a first milestone\". Seen."; and its known C7 candidate: "chapter 15 §The review is a delivery gives the first commit only \"for a first milestone\", where docs/05 §8 gives it to any milestone").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The chapter follows docs/05 §8, not the other way round: docs/05 §8 says "names the commit that closed the previous milestone, or the first commit, as the base", with no restriction, and the kit's document is the source the book teaches (the batch's brief: the book teaches the kit as it is today). docs/05 is not changed. Source: docs/05 §8, work/done/m15-review.md decision 2 and K2.
2. The restriction "for a first milestone" is removed and one sentence says when the first commit is the base: a first milestone, and a later one whose earlier reviews left part of the project unread. Only removing the words would leave the reader with two bases and no way to choose; the reason is the one m15-review gave for its own base (decision 2: earlier deep reviews had read only part of the chapters), said in general terms, with no run, commit or milestone of this repository named (ADR-0017, AGENTS.md). Source: docs/05 §8, work/done/m15-review.md decision 2.
3. Scope is the base only. The deep review's command, the range `git diff <base>..HEAD`, the areas, the readers, the checker and the person's word belong to `ch15-review-by-areas` (docs/06 M16), which will rewrite the rest of the same sentence and §Read the whole code once. This page changes the sentence's first clause and adds one sentence after it; the clause from "when docs/05's Milestone review slot" to "which is `<base>`." stays byte for byte, so the two deliveries do not overlap in scope. Source: the batch's brief, docs/06 M16.
4. The key point that already names the base (§Key points, first bullet) gains "or the project's first commit", so the summary does not teach only one base. Its other words stay. Source: docs/04 §Chapter shape (key points summarize the chapter), docs/05 §8.
5. No docs/03 term, no new queue line, no split: two files, two sentences and one key point each. "milestone review" already says "from the commit the page names" (docs/03). Source: docs/03, docs/05 §1.
6. Taken at /apply, from the Delivery review: the new sentence sits after "The agent may say it is time, and never launches it." (pt: "O agente pode dizer que chegou a hora, e nunca a lança."), not right after the base sentence. Placed right after, its "the review" (pt also "a base") became the nearest antecedent of that line's "it" / "a", which then read as the milestone review the agent never launches, against the chapter's own "`/apply` runs it". Moving the new line, rather than rewording the launch line, leaves that line to `ch15-review-by-areas` (decision 3). The pt sentence says "qualquer marco posterior" for "any later one", since "seguinte" reads as the next one only. Source: the Delivery review below, docs/04.

**Behaviour.**

* A reader of chapter 15 §The review is a delivery reads:
  * en, in place of "Its page names the commit that closed the previous milestone, or the project's first commit for a first milestone; when docs/05's Milestone review slot names a deep review, such as Claude Code's `/code-review ultra <base>`, the person launches it against that commit, which is `<base>`.":
    "Its page names the commit that closed the previous milestone, or the project's first commit; when docs/05's Milestone review slot names a deep review, such as Claude Code's `/code-review ultra <base>`, the person launches it against that commit, which is `<base>`.
    The first commit makes the review read the whole project: it is the base of a first milestone, and of any later one whose earlier reviews left part of the project unread."
  * pt, §A revisão é uma entrega (the section holding the same sentence), in place of "A página dela cita o commit que fechou o marco anterior, ou o primeiro commit do projeto para um primeiro marco; quando o slot Milestone review (revisão de marco) do docs/05 cita uma revisão profunda do código, como o `/code-review ultra <base>` do Claude Code, a pessoa a lança contra esse commit, que é o `<base>`.":
    "A página dela cita o commit que fechou o marco anterior, ou o primeiro commit do projeto; quando o slot Milestone review (revisão de marco) do docs/05 cita uma revisão profunda do código, como o `/code-review ultra <base>` do Claude Code, a pessoa a lança contra esse commit, que é o `<base>`.
    O primeiro commit faz a revisão ler o projeto inteiro: é a base de um primeiro marco, e de qualquer marco posterior cujas revisões anteriores deixaram parte do projeto sem ler."
  * Each new sentence is its own line, one sentence per line as the chapter is written, placed after the line that follows the base sentence ("The agent may say it is time, and never launches it." / "O agente pode dizer que chegou a hora, e nunca a lança."), so that line's "it" / "a" still points to the deep review (decision 6).
* A reader of §Key points / §Pontos-chave reads, in the first bullet:
  * en: "its page names the commit that closed the previous milestone, or the project's first commit, writes for each clause" in place of "its page names the commit that closed the previous milestone, writes for each clause".
  * pt: "a página dela cita o commit que fechou o marco anterior, ou o primeiro commit do projeto, escreve para cada cláusula" in place of "a página dela cita o commit que fechou o marco anterior, escreve para cada cláusula".
* Checked, both editions: `grep -c "for a first milestone" book/en/15-closing-a-milestone.md` and `grep -c "para um primeiro marco" book/pt/15-closing-a-milestone.md` give 0; `grep -c "left part of the project unread"` (pt: `"deixaram parte do projeto sem ler"`) gives 1; `grep -c "or the project's first commit"` (pt: `"ou o primeiro commit do projeto"`) gives 2.
* The rest of chapter 15 is unchanged: §Read the whole code once, its deep review example and every other section and key point.
* Fails: one edition changed and not the other; the first commit still tied to a first milestone anywhere in the chapter; the new sentence naming a commit hash, a milestone of this repository or a run; any change to the deep review's command, range, areas, readers or checker (owned by `ch15-review-by-areas`); any other file changed but this page and the line's marks in docs/06; an em dash; a prose rule of docs/04 hit.

**Contract.**

* Files: `book/en/15-closing-a-milestone.md`, `book/pt/15-closing-a-milestone.md`; no other file.
* Sections and lines: §The review is a delivery / §A revisão é uma entrega, the sentence naming the base (line 20 in both editions in the working tree of 2026-10-17), and a new line after the line that follows it (decision 6); §Key points / §Pontos-chave, first bullet (en line 109, pt line 110). The text is the locator, the number a courtesy.
* Terms of docs/03: none new ("milestone review", "revisão de marco", "base" as docs/05 §8 uses it, already there). Sources: none added or removed. Cases: none; no Case A, Case B or Ninjobs passage. Numbers: none added. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on nearby chapters.**

* `ch15-review-by-areas` (`[ ]`, M16): rewrites chapter 15's code reading, including the second half of the same line 20 and §Read the whole code once. Same files, adjacent text, no scope in common (decision 3). Whichever applies second finds its passage by text and keeps the other's change; if it runs first and rewords this sentence, /apply here changes only the base clause as it then stands and adds the new sentence after the sentence that names the base.
* No other line in flight touches chapter 15.

**Out of scope.**

* The deep review's command, the range since the base, the areas, the read-only readers, the paths read, the checker and the person's word: `ch15-review-by-areas` (decision 3).
* docs/05 §8 and docs/03: they already give the first commit to any milestone (decision 1).
* Chapter 11's and chapter 9's mentions of a milestone's review: they name no base.
* §When the findings became one delivery and the gain: they do not name a base.

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the results it names.
* [x] Chapter 15 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] `make verify` green: links, edition parity, disclosure scan, no em dash, prose, width.
* [x] The author's approval of an anonymized passage: inapplicable, the change draws on no Case A or Case B passage (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Proof.**

* The Behaviour greps, both editions: "for a first milestone" / "para um primeiro marco" 0; "left part of the project unread" / "deixaram parte do projeto sem ler" 1; "or the project's first commit" / "ou o primeiro commit do projeto" 2.
* `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* Divergences: none left; the placement of the new line and the pt word "posterior" changed from the first Behaviour text (decision 6), and Behaviour now says so.

**Delivery review.** A read-only agent on Opus read `git diff` and `git diff --cached` of the two chapter files, this page and this line's hunk of docs/06 against this page, docs/04 and docs/05 §8.

1. The new line, right after the base sentence, made the next line's "it" (pt "a") read as the milestone review, which the agent never launches, against the chapter's "`/apply` runs it". Fixed: the new line moved after that line (decision 6).
2. pt "qualquer marco seguinte" read as the next milestone only. Fixed: "qualquer marco posterior".
3. The first key point is a little crowded, nothing wrong. No change.
4. Noted, not this delivery's: the line "The agent may say it is time, and never launches it." differs from docs/05 §8, where the session starts the deep review on the person's word. That line is the person's word, owned by `ch15-review-by-areas` (decision 3, Out of scope), which already rewrites it; no new queue line.

**Commit.**

```commit
docs(ch15-first-commit): give chapter 15's first commit to any milestone

- Name the first commit as a base without tying it to a first milestone
- Say when the first commit is the base: a whole-project read
- Add the first commit to the first key point
- Both editions

work/done/ch15-first-commit.md
```
