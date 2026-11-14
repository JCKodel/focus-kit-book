# ch14-queue-findings

Decided before the author read it: the author's word for this run, relayed by the driver session on 2026-11-13, is "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão", so every question the documents leave open is answered by the agent's recommendation, marked "decided by the agent, the author corrects it in the review" (docs/05 §4, a command that says to decide alone). The page is built before the author reads it.

**Objective.** After chapter 14 the reader, developer or not, can tell a queue line that came from a finding by its `· from <slug>` suffix, say where such a line goes among the planned lines and why every other finding is a note on the page of the delivery that found it and not a line, say that a line delivering a test, a proof tool or a process change enters only on the person's word, and read the `findings:` line and its `⚠️` warning the queue script prints under the milestone.

**Behaviour.** What the reader can do or explain afterwards:

* Say what `· from <slug>` means: the line is a grave finding, a flaw a command discovered in something its delivery did not build or change, and the slug names the delivery that found it; a flaw in what a delivery built is fixed in it and is no finding (chapter 13 owns that).
* Say where the line goes: above the open planned lines only when verify is red or one of them needs it, as `fix-due-date` goes above `my-loans`; otherwise below them, above the review, or under the review once the review ran; so a finding never takes the place of the work the milestone's paragraph asks for.
* Edge: asked "`/propose return-book`, reading `lend-book`'s code, finds that a suspended member can still borrow; verify is green and `return-book` does not need the fix; where does `fix-suspended` go?", answer: below the open planned lines, above `m1-review`, ending `· from return-book`; it is grave (a loan a rule should refuse goes through, which breaks the paragraph's lending on a librarian's usual path) but nothing needs it first.
* Failure: asked "a finding is not grave; should I add it as a `[ ]` line at the end of the milestone so it is not forgotten?", answer no: it is a note on the page of the delivery that found it, under `## For the review`, one line with the file and line and what a person would see; a note is not a line and waits for the next milestone review, which copies it (chapter 15).
* Failure: asked "the agent wants to queue a line for a proof run in parallel and one for test helpers; may it?", answer: only on the person's word, since a line that delivers a test, a proof tool or a change to the process, and is not a grave finding, enters that way alone; without the word it is a note.
* Read the script's two lines on the chapter's five lines: `findings: 1 open of 1 from a finding · 2 planned open` counts the milestone's lines ending `· from <slug>`, how many of them are open, and the open planned lines, the review and the cancelled lines not counted; `⚠️ ahead of planned lines: fix-suspended` names the open finding lines that stand ahead of an open planned line, and the tree's `next:` is then `/propose fix-suspended`, ahead of the planned work; moved below `search-catalog`, above `m1-review`, `fix-suspended` leaves the warning out and `next:` is `/apply return-book`.
* Edge: a finding line an open line names in its `after` or `blocked: after`, as `my-loans` names `fix-due-date`, is not in the warning: it stands above because a planned line needs it.
* Edge: with no line ending `· from <slug>` in the milestone, the script prints no `findings:` line; a closed finding line counts in the total, not in the open ones.
* Say what the warning is for: a look, not a verdict: a finding line ahead of planned work that no open line names is either one verify needs, red, or one that should move below; the person reads it, and since `/apply` runs the script at its end, the drift shows without anyone asking (chapter 13 tells the error it prevents).
* Find in chapter 14 the suffix, the place of the line, the note, the person's word for a test or process line, and the two lines of the script; in the Portuguese edition the same with docs/03's terms: "achado", "achado grave", "nota", "linha planejada" (new row, below), the suffix `· from` and the heading `## For the review` kept as the kit writes them, and the script's output in English.

**Contract.** Two chapter files and one docs/03 row plus one new row. Line numbers en at HEAD `46d5166`, quoted beside each so a drift is found; pt follows en sentence for sentence. The text is the agent's within these changes.

* **ch14** (`book/en/14-queue-states.md`, `book/pt/14-queue-states.md`)
  * C1, opening, second sentence (:4, "mark a line that waits with its reason and the phase to resume, and take it out again; and lay the queue out as a kanban board"; pt :4): one clause after "take it out again": tell a line from a finding by its `· from <slug>`, say where it goes, why every other finding is a note and not a line, and read the `findings:` line the queue script prints. Still three sentences.
  * C2, the script's output, after :137 ("On trunk, a state is one of these: in flight, by the command its mark names; `propose now` or `apply now`, free for that command; `waits:`, with what it waits on; or `blocked:`, with its reason and the command that resumes it."; pt :139, "No trunk, um estado é um destes: ...") and before :138 ("Then come the lines free for `/apply` and for `/propose`"): one sentence: when the milestone holds a line from a finding, two lines may come between the heading and the tree, `findings:` and a warning, read in the new section below. The :153-161 output is unchanged: its milestone holds no finding line, so the script prints neither.
  * C3, the third case of waiting (:177, "the fix becomes a `[ ]` line above it, `fix-due-date`, and `my-loans` waits: `· resume: apply · blocked: after fix-due-date`"; pt :179, `corrigir-devolucao`): the fix line ends `· from my-loans` (pt `· from meus-emprestimos`), as docs/05 §6 :416 writes the prerequisite line. The `[?]` shape stays: `ch14-after-never-waits` (M39) changes it.
  * C4, a new section `## A line from a finding` (pt `## Uma linha de um achado`), after `## Waiting: [?]` (ends :196, "A command that ran past the reason would build on an answer nobody gave."; pt :198) and before `## A session that ended, a delivery cancelled` (:198; pt :200). In this order, from the reader's problem:
    1. The problem: a delivery that finds a flaw outside what it built can turn it into a line, and lines from findings, each reasonable, can stand ahead of the work the paragraph asks for. Chapter 13 tells the error that showed it (`ch13-apply-findings` owns the 32 of 130 lines and the twenty-four in a row); this chapter repeats no number of it, and its sentence must stand alone if chapter 14 lands before chapter 13's text: it says the problem in its own words and adds the pointer as a parenthesis, "(chapter 13 tells where it went wrong)", never a sentence that is only a pointer (docs/04 :41). Chapter 11 already says a grave finding stays in its milestone (ch11 :79, "Two kinds of line stay in the milestone they were found in, even when no clause needs them and the next milestone is already in the queue: a grave finding, a flaw a delivery finds outside what it built, and a finding of the milestone's own review"); not repeated, no pointer needed (docs/04 :43, a pointer back only where the sentence leans on a detail worth reopening).
    2. The suffix: a grave finding becomes a `[ ]` line ending `· from <slug>`, the delivery that found it, as `fix-due-date ... · from my-loans` above (C3). The three tests of grave are chapter 11's words (ch11 :98, "which breaks a clause of the paragraph for a person on its usual path, loses or exposes data, or leaves verify red"), said here in one clause because the place rule needs "verify red", with no pointer.
    3. The place: above the open planned lines only when verify is red or one of them needs it, as `fix-due-date` stands above `my-loans`, which names it in `blocked: after` (:177); otherwise below them, above the review, or under the review once it ran. Reconciles :106 ("A line added later goes in the milestone whose paragraph needs it, never higher in the queue because it is new: its place is its priority"): a finding's place is its priority too, so it goes below the planned work unless verify or a planned line needs it first. A planned line is any line of the milestone that is not from a finding and not the review (C8).
    4. The note: every other finding is a note on the page of the delivery that found it, under the heading `## For the review` above its `commit` block, one line each: the file and line, and what a person would see; a note is not a line, and the next milestone review copies it (chapter 15 grades it; a parenthesis, forward, naming the review the reader has met in chapter 11). A finding nobody can say is grave is a note. One example note written for the chapter, on the library, e.g. "`src/features/catalog/search.ts:41`: a search for a title with an accent finds nothing" (the agent may change it; inline, or a block within 74 columns).
    5. The person's word: a line that delivers a test, a proof tool or a change to the process, and is not a grave finding, enters only on the person's word; without it, it is a note. The evidence, told as the kit's changelog words it, with no project named: in the project of 2026-11-12, a proof run in parallel, a proof split by state and test helpers were queued while its features waited (changelog `## 2026.11.12`, the bullet "A line that delivers a test, a proof tool or a change to the process": "The project above queued a proof run in parallel, a proof split by state and test helpers while its features waited"). Told "in one project, on 2026-11-12", as :71 and :80 tell theirs, with a parenthesis to chapter 13 if that chapter by then tells the same project; the sentence stands without it.
    6. The script: the five lines below, written for the chapter and said so, then the first three lines of the script's output, said to be its first lines (the rest of the tree reads as at :150-166), then the reading: `findings:` counts the finding lines, the open ones and the open planned lines, the review not counted; the warning names `fix-suspended`, which stands ahead of `return-book` and `search-catalog` though neither needs it, and the tree's `next:` is `/propose fix-suspended`, before the planned work; moved below `search-catalog`, above `m1-review`, the warning goes and `next:` is `/apply return-book`. A finding line an open line names in `after` or `blocked: after`, as `my-loans` names `fix-due-date` at :177, is left out of the warning, in prose. The warning is a look, not a verdict: a line verify needs, red, stands ahead and warns too, and the person reads why. `/apply` runs the script at its end (chapter 13, a parenthesis), so the drift shows without anyone asking. No `findings:` line when the milestone has none.

    Input, en, verified by running the installed `queue.sh` with `trunk` on a scratch repository whose docs/06 held these lines under `## Milestone 1: a librarian lends and takes back` (widest row 67 characters):

    ```
    [x] lend-book       the librarian lends a copy, or a rule refuses
    [ ] fix-suspended   a suspended member borrows · from return-book
    [>] return-book     records a return · after lend-book
    [ ] search-catalog  a member searches the catalog
    [ ] m1-review       the milestone against its paragraph · after all
    ```

    Its first three lines of output (its last, `next: /propose fix-suspended`):

    ```
    milestone: Milestone 1: a librarian lends and takes back
    findings: 1 open of 1 from a finding · 2 planned open
    ⚠️ ahead of planned lines: fix-suspended
    ```

    With `fix-suspended` moved between `search-catalog` and `m1-review`: `milestone:`, `findings: 1 open of 1 from a finding · 2 planned open`, then the tree, no warning, and `next: /apply return-book` (verified).

    pt, verified the same way under `## Marco 1: um bibliotecário empresta e recebe de volta` (widest row 74 characters, `emprestar-livro`'s, as chapter 14's pt block at :146 writes it; "empresta" reads as lending, so /apply may word `corrigir-suspenso`'s sentence otherwise, e.g. "suspenso ainda pega livro", 69 characters, rerunning the script):

    ```
    [x] emprestar-livro   o bibliotecário empresta um exemplar ou a regra nega
    [ ] corrigir-suspenso membro suspenso empresta · from devolver-livro
    [>] devolver-livro    registra a devolução · after emprestar-livro
    [ ] buscar-catalogo   um membro busca no catálogo
    [ ] m1-review         o marco contra o parágrafo dele · after all
    ```

    ```
    milestone: Marco 1: um bibliotecário empresta e recebe de volta
    findings: 1 open of 1 from a finding · 2 planned open
    ⚠️ ahead of planned lines: corrigir-suspenso
    ```

    Its last line `next: /propose corrigir-suspenso`; moved between `buscar-catalogo` and `m1-review`, no warning and `next: /apply devolver-livro` (verified). The full output is not shown in either edition: its review row runs past 74 characters.
  * C5, the team gain (:271, "the queue tree draws it from the queue, without a meeting, each line under what it waits on, and ends with the command to run next"; pt :273): one sentence or clause, no number: the tree also says how much of the milestone came from findings and names a finding line standing ahead of planned work, so the drift shows the day it starts; and a finding that is not grave waits on its page for the review instead of entering the queue.
  * C6, key points, still five: key point 3 (:278, "then the lines free for `/apply` and for `/propose`"; pt :280) gains, under the heading, `findings:` and its `⚠️` warning; key point 4 (:279, "`· after` is an order written with the line"; pt :281) gains: a grave finding is a line ending `· from <slug>`, above the open planned lines only when verify is red or one needs it, every other finding a note under `## For the review` on the finding delivery's page; a test, proof tool or process line only on the person's word.
* **docs/03** (`docs/03-Domain.md`)
  * C7, queue tree row (:123, "the current milestone's lines not `[x]`, each under the last line it waits on with its other pending `after` beside it and its state ..."): wrong by omission, since it lists what the tree prints and leaves out two of its lines: after the milestone's heading, `findings:`, how many of its lines came from a finding, how many of those are open and how many planned lines are open, and a `⚠️` line naming the open finding lines ahead of an open planned line, but one an open line names in `after` or `blocked: after` (since focus-kit 2026.11.12). Nothing else of the row changes (M39 owns "every open milestone").
  * C8, a new row after `fixes line` (:38): `planned line | linha planejada | none | A line of a milestone that does not end `· from <slug>` and is not its review, the lines its paragraph's clauses asked for; the queue script counts the open ones, the cancelled left out, and a grave finding goes above them only when verify is red or one of them needs it (docs/05 §4, `queue.sh` :249).` The pt term is the kit's Portuguese changelog's ("linhas planejadas").

Terms of docs/03: finding (achado), note (nota), queue line, mark, queue tree, milestone review, fixes line not needed; new: planned line. Sources: the installed `.agents/skills/propose/scripts/queue.sh` (:12-14, the header; :112, `from <slug>` read only as a suffix with nothing after it; :244-264, the counts, the review and dropped lines left out, the warning, at most three names then "and N more"); the kit's `CHANGELOG.md` and `CHANGELOG.pt.md`, `## 2026.11.12`, the bullets on findings, `queue.sh`'s `findings:` and the person's word; this repository's docs/05 §4 (:117-138) and §3 (:76-77). No source note: the kit is taught as it is (docs/04). Cases: none; the project of the proof run stays unnamed, as the changelog leaves it.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** The Design slot says prototype, no reference, by choice (ADR-0019). But the `⚠️` in C4's output block is the first emoji the book shows (no `⚠`, `🚨` or `✅` in `book/` at HEAD), a kind of content the build has not shown: §5's Proof of a screen asks screenshots of the site in light and dark and of the PDF, in both editions, saved as `work/done/ch14-queue-findings-<what>.png`.

**Out of scope.**

* What /apply does with a flaw in what it built, a note or a `[?]` it cannot fix, its `🚨`/`⚠️`/`✅` last message, and the 32 of 130 lines with the twenty-four in a row: `ch13-apply-findings` (M38), chapter 13.
* The review copying the notes and grading findings, grave, medium on `<milestone>-fixes`, small listed: `ch15-review-grades` (M38), chapter 15.
* A grave finding staying in its milestone and "only through a clause" with its exceptions: chapter 11 (:79, :81, :181), `m35-fixes` in flight; chapter 14 points there.
* `[?]` never on another line, the third case rewritten and `waits`: `ch14-after-never-waits` (M39); `queue.sh` drawing every open milestone and C2's "current milestone": `ch14-queue-every-milestone` (M39); the open lines search: `ch14-open-lines-search` (M39).
* `queue.sh` reading a line only the local file has (2026.11.12's other script change): M39's paragraph ("reading a delivery's own line from its worktree") and its lines.
* The kit's test fixture (`test/fixture/queue/`): the kit's own test, nothing a reader runs.
* `ch14-open-lines-search` (M39), a draft at `work/ch14-open-lines-search.md` with no section chosen yet: whichever lands second places its text without undoing the other's; nothing in this page's C1 to C6 is its.

**Done when.**

* [x] C1 to C6 read as the Contract says in both editions; still three opening sentences and five key points.
* [x] C7 and C8 in docs/03.
* [x] /apply reruns the installed `queue.sh` with `trunk` on the exact five lines of each edition's block, under its heading, and the output block matches the script's first three lines and the text its `next:`; and once with the finding moved below the planned lines, no warning.
* [x] Both editions written; the chapter opens with its value; no filler and nothing useful cut; no number of chapter 13's error repeated; the person's-word evidence as the changelog words it, no project named; no em dash; no run narration; every block within 74 columns.
* [x] The `⚠️` renders: screenshots of the site in light and dark and of the PDF, both editions, as §5's Proof of a screen says for a new kind of content, unless `ch13-apply-findings` already proved it (Decisions); a glyph that does not render is a note, not a change to the build.
* [x] `make verify` green after the last edit, with its time.
* [x] `make book` builds both editions, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent, the author corrects it in the review: one new section after `## Waiting: [?]`, since its third case is already a line from a finding (`fix-due-date`) and the section builds on it; the script's two lines are taught there, on lines that hold findings, and C2 only says they exist, so each thing is said once.
* Decided by the agent, the author corrects it in the review: chapter 14 tells no number of the error of 2026-11-12 and points to chapter 13, which owns it by its queue line; its own evidence is the proof run, the proof split by state and the test helpers queued while features waited, for the person's-word rule, which its queue line names and no sibling does.
* Decided by the agent, the author corrects it in the review: the block's one finding, `fix-suspended · from return-book`, is a flaw in `lend-book`'s code found by `/propose return-book`, so it is a finding of `return-book` (outside what it builds, docs/05 §4 "/propose while it defines included") and grave by the first test; `fix-due-date` keeps its `my-loans` origin from :177 and stays out of the block, since its `[?]` line with its `after` and a sentence does not fit 74 characters, and the exemption it shows is told in prose.
* Decided by the agent, the author corrects it in the review: the output block shows the script's first three lines, said so, because the review's row of the full output runs past 74 columns in both editions; the tree's other lines are taught at :150-166.
* Decided by the agent, the author corrects it in the review: the queue tree row of docs/03 is wrong by omission, since it enumerates the tree's output, and gains the two lines; "planned line" gets a row, being a term the chapter needs and docs/03 lacks, with the pt word from the kit's Portuguese changelog. The finding, note and fixes line rows were checked and say nothing wrong.
* Decided by the agent, the author corrects it in the review: the `⚠️` in a block is a new kind of content, so the render proof of §5 applies, unless `ch13-apply-findings` has already brought `⚠️` into the book and proved it, in which case this delivery owes none. A scratch render of the two output lines with `pandoc/pdf.css` by the local `weasyprint` embedded Apple Color Emoji beside Iosevka Term, so the PDF built on this machine shows it; the site and the EPUB are /apply's to see. If it does not render, the missing glyph is a flaw in the build, which this delivery did not write: a finding, grave only if it breaks a clause of M38's paragraph, which it does not, so a note under `## For the review`, and the chapter keeps the output as the script prints it (docs/04: commands and their output stay as they are).
* Decided by the agent, the author corrects it in the review: the brief of this run limits /propose to this page and its mark, so the docs/03 rows are /apply's (C7, C8), not written before the page as the skill's "add a new concept there first" would have it.
* From the documents: the suffix, the place and the note (docs/05 §4 :117-138), the heading (docs/05 §3 :76-77), the prerequisite line ending `· from <slug>` (docs/05 §6 :416), the script's output (installed `queue.sh`), the kit's names and the script's output kept in English in pt (docs/04), five key points (docs/04).

## Outcome

Built by `/apply` in a subagent on the author's word for this run, "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão", before the author read the page; every decision below was taken by the agent, and the author corrects it in the review. The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

* Drift since `46d5166`: `m36-fixes`, `m37-fixes` and `ch15-review-grades` changed chapter 14's cancelled-review paragraph and docs/03's finding and checker rows; no passage this page edits moved in meaning, each was found by its quoted sentence. Chapter 15's "(chapter 14 shows the note)" and "(chapter 14 shows the suffix)" now hold: the new section shows a note under `## For the review` and the `· from` suffix.
* C1 to C6 written in both editions; the opening still three sentences, five key points. C7 and C8 in docs/03.
* Script proof: the installed `queue.sh` with `trunk`, on a scratch repository holding each edition's five lines under its heading, printed the three lines the blocks show and `next: /propose fix-suspended` (pt `corrigir-suspenso`); with the finding moved between `search-catalog` and `m1-review`, `findings:` unchanged, no warning, `next: /apply return-book` (pt `devolver-livro`).
* Decided by the agent: pt's finding sentence is `membro suspenso pega livro` (the page's suggestion with a subject), since `membro suspenso ainda pega livro` ran the row to 76 columns; widest pt row 74, en 67.
* Decided by the agent: the note example is a block, `## For the review` and one bullet, `src/features/catalog/search.ts:41` (pt `src/features/catalogo/busca.ts:41`), within 74 columns.
* Decided by the agent: the evidence of 2026-11-12 carries no parenthesis to chapter 13, which does not tell that project yet (`ch13-apply-findings` builds after this delivery).
* Render proof of `⚠️` (`ch13-apply-findings` had not brought it in): the site renders it in light and dark in both editions (`work/done/ch14-queue-findings-site-{en,pt}-{light,dark}.png`, the local `site/` served and opened in Chrome, the scheme set by the palette attribute); the PDF embeds Apple Color Emoji but draws the glyph one line up, over the `f` of `findings:`, leaving a gap before `ahead of planned lines` (`work/done/ch14-queue-findings-pdf-{en,pt}.png`, pages 164 and 171). Kept as the script prints it; a note below. The EPUB was not inspected.
* Delivery review (one read-only Opus agent): two must-fix, both handled. The definition of grave lacked docs/05 §4's fourth case, a fix a delivery in flight cannot go on without, which is `fix-due-date`'s case: added in both editions (a case the page's C4.2 did not name). The PDF glyph: recorded as a note. Optional ones fixed: the sentence on no `findings:` line cut as said twice with C2; "a suspended member who borrows is a loan" reworded; the gain sentence split so the tree does not "wait"; pt `precisam`; "the warning goes". Kept: "(chapter 15 grades it)", which the Contract asked for. Not fixed: chapter 11 and docs/03's finding row also give three tests of grave, outside this page (note below).
* `make verify` green after the last edit, 12 seconds. `make book` builds both editions: `output/one-page-at-a-time.pdf`, `output/uma-pagina-de-cada-vez.pdf`.

## For the review

* `pandoc/pdf.css` (PDF build, weasyprint): the `⚠️` in chapter 14's output block is drawn one line up, over the `f` of `findings:`, with an empty gap before `ahead of planned lines`; the site renders it right.
* `book/en/11-queue-and-milestones.md:98` and docs/03's `finding` row: grave lists three tests and leaves out docs/05 §4's "So is a fix a delivery in flight cannot go on without"; a reader of chapter 11 alone would not call `fix-due-date` grave.

```commit
docs(ch14-queue-findings): teach finding lines, notes and findings:

- Chapter 14 teaches the · from suffix, where a grave line goes, the note
- A test, proof tool or process line enters only on the person's word
- queue.sh's findings: line and its warning read on five library lines
- docs/03: queue tree row gains findings:, new planned line row

work/done/ch14-queue-findings.md
```
