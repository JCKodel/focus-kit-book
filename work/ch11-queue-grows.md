# ch11-queue-grows

**Objective.** A reader of chapter 11 knows that three to eight deliveries is how a first milestone starts, that lines are added while a milestone runs, so it closes larger than it started, and that the person decides which lines enter it and which wait for a later milestone, because an agent tends to add. Both editions. From the author's reading of the book on 2026-10-18: "Chapter 11, 'Tamanho e ordem', reads as if three to eight deliveries were a limit. It is only how a milestone starts. Each delivery or review can add lines; users' tests find problems that, by talking to the agent, become more lines [...]. The queue is a living, dynamic document; the team decides what enters and its priority. [...] Agents tend to add. Without human judgment a milestone can grow without control; a line being added may belong to a future milestone of improvements, not to now."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *Three to eight is the first milestone's rule, and the chapter says only that.* The kit asks three to eight deliveries for the first milestone only (`.claude/skills/brainstorm/SKILL.md` step 6, `.claude/skills/analyze/SKILL.md` "the first milestone"); docs/05 gives no size to any other. en 11:70 (pt 11:73) calls it "a good size for any", which the kit does not say: the sentence becomes that a milestone starts with the lines its paragraph needs, then its review, and that for the first one the kit asks three to eight. It is said as what it is, with no "not a limit" contrast, so docs/04's `not-but` rule holds. Source: the two skill files, docs/05 §4 and §8, docs/04 §Writing the book, **The kit as it is**, docs/04 §Prose rules, `not-but`.
2. *Growth is said as the queue working.* A milestone gains lines while it runs, from three places the chapter already teaches: a fix a delivery finds outside its page becomes a line (en 11:151, pt 11:156), a finding of the review becomes a line under it (en 11:86, pt 11:89), and a problem the person finds trying the product becomes a line by conversation (en 11:91, pt 11:94). The new paragraph gathers them in one place, where the doubt about size is born, and says the milestone closes larger than it started. Source: docs/05 §4 and §8, docs/03's `finding` row, docs/04 §Writing the book, **Say it where the doubt is born**.
3. *The number is this book's own queue, not "5 ending with 50".* "A milestone of 5 lines ending with 50" is the author's impression, not a count, and docs/04's Evidence rule wants every number to say where it comes from; the exemption "how the author counted it" covers a private case only. This repository's docs/06 gives a count the reader can repeat: M15, "The reader's time", holds 42 lines, all `[x]`; its review, `m15-review`, is the 14th, and 28 lines sit under it. The chapter says that, with a source note `[^m15-queue]` to docs/06 in the book's repository, written as chapter 16's `[^m14-review]` is, both editions. M15 is chosen over M14, M16 and M17, which grew the same way, because it is not a kit-update milestone, so the count is not read as a measure of a kit change. No commit hash and no count from the history: the reader counts the file as it is. Source: docs/04 §Writing the book, **Evidence**, **No runs**, and the source notes rule (docs/04 line 140, "a file of this book's repository"), docs/06 §M15, book/en/16-the-governor.md:92.
4. *The person decides, because an agent tends to add.* The paragraph says that an agent asked about a problem tends to answer with a line, each one reasonable, so without a person judging a milestone grows without end; the person decides what enters and where. The test is the one en 11:66 (pt 11:69) already gives, every line serves a sentence of the paragraph: a line that serves none of this milestone's sentences goes to a later milestone, one of improvements if the person wants one. Source: the draft, en 11:66, en 11:91 and 154-157 (the person reorders by conversation, and reads every change to the queue before committing it), AGENTS.md ("Ambiguity → ask"; the agent never commits).
5. *"Intermediate milestones" are taught as a later milestone the person chooses, never a `.1` milestone of findings.* docs/05 §8 and docs/03's `finding` row put every finding under the review line of the same milestone, "never a fix in the middle of the next milestone", and the `.1` milestones of M3 and M4 are history (docs/05 §8, last paragraph; chapter 3's caution, en 03:245-246, tells where they led). The new text names only "a later milestone". Source: docs/05 §8, docs/03.
6. *Chapters 9, 10 and 23 stay as they are.* en/pt 09:22 and 09:85 describe what `/brainstorm` and `/analyze` write for the first milestone; en/pt 10:86 says the backlog is read "into the first milestone"; en/pt 23:74 and 23:112 plan one trial milestone, "start with one milestone ... then decide". Each already reads as a start, and each that points anywhere points to chapter 11, which now carries the rule. Source: the draft's last but one point, the chapters as they are at /propose.
7. *Chapter 3's caution is a different lesson and is not touched or repeated.* It tells an agent adding process steps; this delivery tells an agent adding lines to a queue. The new paragraph names no process step and cites no chapter 3. Source: en 03:244-248, docs/04 §Writing the book, one source per point.
8. *Gain section and other sections unchanged.* The gain stays the queue as the team's board and history, said once; the M15 count is evidence for the size paragraph, not a second gain. §Changing the queue is not edited: it already says lines enter by conversation and the person moves them, and `ch11-agent-runs-propose` edits it. Source: docs/04 §Writing the book, **One gain**, work/ch11-agent-runs-propose.md.
9. *The `[+]` mark is not in the book.* It is a suggestion to the kit, item 2 of work/kit-proposals.md, and the book teaches the kit as it is. Source: the draft, docs/04 **The kit as it is**.
10. No new docs/03 term (the `milestone` row gives no size and needs none), no new queue line, no split.

**Behaviour.**

* The reader of chapter 11, in either edition, reads in `### Size and order` (pt `### Tamanho e ordem`):
  * first, that a milestone starts with the lines its paragraph needs, then its review, and that for the first milestone the kit asks three to eight deliveries; the sentence on the skeleton and the sentence on order follow unchanged;
  * then one new paragraph, one sentence per line, that says:
    * lines are added while a milestone runs, and from where, a few words each and without restating how each works, since the chapter says that where it owns it: a fix a delivery finds outside its page, the review's findings, a problem the person finds trying the product; so a milestone closes larger than it started, and the queue changes with the work;
    * the count from this book's queue: its milestone M15 closed with 42 lines, its review the 14th of them and 28 under it, with `[^m15-queue]` at the claim;
    * an agent tends to add, each line reasonable, and without a person judging a milestone grows without end; the person decides what enters and where: a line that serves no sentence of this milestone's paragraph goes to a later milestone, one of improvements if the person wants one.
  * The paragraph on the order as priority and the paragraph on `· after` follow unchanged.
* The key point that names three to eight (en 11:169, pt 11:174) says the paragraph is a test over the deliveries that make it true, three to eight in the first milestone, the skeleton first, each line after the lines it needs, last the review whose findings become lines under it, and that lines are added while it runs and the person decides which enter now and which wait for a later milestone. No number in the key point.
* The chapter ends with one source note, `[^m15-queue]`: en `J.C. Ködel, "One Page at a Time", docs/06, the queue, milestone M15, accessed <apply date>, in the book's repository. <https://github.com/JCKodel/focus-kit-book/blob/main/docs/06-Queue.md>`; pt translated as pt 16:92 translates its note (`o docs/06, a fila, marco M15, acessado em <data do apply>, no repositório do livro`), same URL. The date is the day /apply recounts the section.
* The Portuguese edition says the same in the same places, with the chapter's terms ("marco", "linha", "entrega", "achado", "revisão", "fila").
* Checked at apply time:
  * `grep -n "three to eight" book/en/*.md` prints only en 09:22, 09:85, 10:86, 23:74, 23:112 and the two rewritten lines of chapter 11; `grep -n "três a oito" book/pt/*.md` prints the same places.
  * `grep -n "good size for any\|bom tamanho para qualquer" book/` prints nothing.
  * The 42, the 14th and the 28 are counted again in docs/06 §M15 at apply time (`[x]` lines of the section, the position of `m15-review`); if the file changed, the chapter says what the file says then.
  * `git diff book/` shows changes only in `### Size and order`, the one key point and the new note of chapter 11, both editions.
* Fails: "a good size for any" kept; a sentence that sets the size against what it is not ("not a limit"), or any `not-but` pattern; "5 ending with 50" or any number without its source; a count taken from git history or a commit hash; a `.1` milestone or "intermediate milestone" taught as the way findings go; the `[+]` mark or any rule the kit does not have; a change to chapters 9, 10 or 23, to §Changing the queue, to the gain section, or to any other key point; an em dash; a run narrated.

**Contract.**

* Files: `book/en/11-queue-and-milestones.md`, `book/pt/11-queue-and-milestones.md`; `### Size and order` (pt `### Tamanho e ordem`), the third key point, and the chapter's notes (one new: `[^m15-queue]`).
* Terms of docs/03: none new; `milestone`, `milestone review` and `finding` as docs/03 has them. Sources: one added, docs/06 of the book's repository, a file the reader can open and count. Cases: none; Ninjobs's 102 at en 11:26 and 11:162 unchanged. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* `ch11-agent-runs-propose` (still a draft) edits the sentence at en 11:103 (pt 11:106), in §Changing the queue; this delivery does not touch that section (decision 8). No shared hunk; whichever lands later finds its text by the text, not the line number.
* `early-no-forward-links` edits chapters 0 to 7 only; chapters 9, 10, 11 and 23 are outside it, and this delivery adds no forward pointer (the note points to a file, not a chapter).
* `pt-ninjobs-masculine` changes Ninjobs's article in pt 11:28 and pt 11:167 (outside `### Tamanho e ordem` and the key points); this delivery adds no Ninjobs mention, so no article to agree.
* No other M18 page edits chapter 11 (`grep -ln "chapter 11\|11-queue\|pt 11:\|en 11:" work/*.md` at /propose: the three above and work/kit-proposals.md, which is not a delivery).

**Out of scope.**

* Chapters 9, 10 and 23: they already say the first or the trial milestone, decision 6.
* §Changing the queue, the gain section, the other key points: decision 8.
* The `[+]` mark for "if there is time": work/kit-proposals.md item 2, for focus-kit's repository (decision 9).
* A count of Ninjobs's milestones: none was counted, and no private number enters without the author's count.

**Done when.**

* [ ] Both editions written: the size sentence, the growth paragraph, the key point and the note as Behaviour says.
* [ ] Chapter 11 still opens with its value, keeps its gain said once, no filler and nothing useful cut.
* [ ] Every number sourced: 42, 14th and 28 from docs/06 §M15, recounted at apply time, with `[^m15-queue]`.
* [ ] `make verify` green: edition parity, prose rules, width, links, disclosure scan, no em dash.
* [ ] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [ ] `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.
