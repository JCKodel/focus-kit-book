# ch15-review-grades

Decided before the author read it: the author's word for this run, relayed by the driver session on 2026-11-13, is "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão", so every question the documents leave open is answered by the agent's recommendation, marked "decided by the agent, the author corrects it in the review" (docs/05 §4, a command that says to decide alone). The page is built before the author reads it.

**Objective.** After chapter 15 the reader can open a milestone review by copying onto its page the notes the range's deliveries left under `## For the review`, have the checker mark them as it marks candidates, and grade every confirmed finding: a grave one a `[ ]` line of its own, the medium ones the person picks on the one `<milestone>-fixes` line, whose page is their list and is not split, the small ones listed on the review's page and a line only when the person picks one; and say why a review grades instead of making every finding a line.

**Behaviour.** What the reader can do or explain afterwards:

* Say where the review's notes come from: a finding a delivery makes outside what it built, and not grave, is a note on that delivery's page under `## For the review` (chapter 14 teaches it); the review opens by copying onto its page the notes of every page its range delivered.
* Say why the checker marks a note as it marks a candidate, seen, latent or weak: a note says what was true when it was written, and a later delivery of the range may have changed the file since.
* Grade a confirmed finding: grave when it breaks a clause of the paragraph for a person on its usual path, loses or exposes data, or leaves verify red; medium when a person meets it in ordinary use while the clause still holds; small when it is a rare case, a latent or weak candidate, or a cost nobody measured.
* Say what each grade becomes: a grave one a `[ ]` line of its own, ending `· from <milestone>-review`, under the review; the medium ones listed first on the review's page, and those the person picks enter one line, `<milestone>-fixes`, each an item of its page, which is their list and is not split, whatever its length; the small ones listed after them, a line only when the person picks one. All these lines sit under the review line and wait for `/propose`; the milestone closes when they are `[x]`.
* Edge: asked "the review confirmed eleven medium findings; should the fixes page be split in two?", answer no: the page is their list and is not split; split, it would be the many lines the grading exists to prevent.
* Edge: asked "a slow test failed in the review; is it a line?", answer: it is a finding, graded like the others; it is a line when grave, and otherwise listed, the person picking.
* Failure: asked "a candidate the checker marked weak; does it become a line?", answer: it is a small one, listed on the page, a line only when the person picks it.
* Failure: asked "the review confirmed a medium finding; can the session fix it right away in the next milestone's delivery?", answer no: never a fix in the middle of the next milestone; it waits on the fixes line, which passes through its own page, proof and commit, with no second review.
* Read the chapter's example: on the lending library, the hand test's failure (a returned copy stays among the member's loans) is grave and becomes `returned-loan`; a note `return-book` left on lending's form is medium; the seen candidate, a cost nobody measured, and the latent and the weak ones are small; with the medium one picked, the milestone ends with `returned-loan` and `m1-fixes` under `m1-review`.
* Say what the team gains: the queue shows as lines the findings that break the milestone's promise and the one list of what a person meets in ordinary use, next to the planned work, while the rest stays listed on the review's page for the person's pick.
* Find all of this in chapter 15 in both editions; in the Portuguese one with docs/03's terms: achado, achado grave, médio, pequeno, nota, linha de correções, conferente, visto, latente, fraco; `## For the review`, `· from` and `<milestone>-fixes` kept as the kit writes them.

**Contract.** Two chapter files and two docs/03 rows. Line numbers are en and pt at `46d5166`, chapter 15's last commit, unchanged at HEAD `4ee7736`; each change quotes the sentence it replaces so a drift is found. pt follows en sentence for sentence. The text is the agent's within these changes.

* **ch15** (`book/en/15-closing-a-milestone.md`, `book/pt/15-closing-a-milestone.md`)
  * C1, opening, first sentence (en :3, "and turn each finding into a `[ ]` line in the same milestone, under the review, even when the next milestone is already in the queue."; pt :3, "e transformar cada achado em uma linha `[ ]` no mesmo marco, sob a revisão, mesmo quando o marco seguinte já está na fila."): becomes: copy onto the review's page the notes the deliveries left, and grade every confirmed finding, a grave one a `[ ]` line of its own, the medium ones you pick on one `<milestone>-fixes` line, the small ones listed, every line under the review even when the next milestone is already in the queue. Still three sentences (docs/04 :127).
  * C2, the slow tests (en :21, "a failing one is a finding, so the milestone does not close while its line is open."; pt :21, "um que falha é um achado, então o marco não fecha enquanto a linha dele estiver aberta."): a failing one is a finding, graded like the others (below).
  * C3, the candidate confirmed (en :111, "A candidate becomes a finding only when the person confirms it, and then it is a finding like the others, a `[ ]` line under the review line."; pt :114): ends "a finding like the others, graded with them (below)".
  * C4, a new section `## The notes the deliveries left` (pt `## As notas que as entregas deixaram`), after `## Read the code since the base` (ends en :112, "A project whose Milestone review slot says none has no code reading, and the hand test still runs."; pt :115) and before C5's section. Short, from the reader's problem:
    1. The problem: deliveries meet flaws outside what they built while the milestone runs, and one that is not grave waits as a note on the page of the delivery that found it, under `## For the review`, one line with the file and line and what a person would see (chapter 14 teaches the note, as a parenthesis; the sentence says it in its own words so it stands if chapter 14's text lands later). The review is where those notes are looked at.
    2. The rule: the review opens by copying onto its page the notes of every page its range delivered, the pages committed between its base and `<review-head>`; a delivery whose page has no notes adds none.
    3. The checker marks each note as it marks a candidate, seen, latent or weak, because a note says what was true when it was written and a later delivery may have changed the file since; the person confirms it as they confirm a candidate.
    4. One example note, written for the chapter and said so: on `return-book`'s page, "`src/features/loans/LendForm.tsx:31`: after a refused loan the form clears the member's card number, and the librarian types it again" (pt: on `devolver-livro`'s page, Portuguese path as the pt chapter writes its paths, e.g. `src/features/emprestimos/FormularioEmprestimo.tsx:31`); `/propose return-book` or its `/apply` found it in lending's form, outside what `return-book` builds. Inline, or a block within 74 columns.
  * C5, a new section `## Grave, medium, small` (pt `## Grave, médio, pequeno`), after C4 and before `## A line, and not a fix` (en :114; pt :117):
    1. The problem, in the present and with no number: findings differ in weight, and a review that made every one a line would fill its milestone with them, each with its own page, proof and commit before the milestone closes, a rare case beside a broken promise, while the next milestone's work waits behind them.
    2. The rule: the review grades every confirmed finding. Grave, in one clause with the three tests (breaks a clause of the paragraph for a person on its usual path, loses or exposes data, or leaves verify red): a `[ ]` line of its own. The others stay listed on the review's page: first the medium ones, met by a person in ordinary use while the clause still holds; then the small ones, a rare case, a latent or weak candidate, a cost nobody measured.
    3. The pick: the person says which medium ones enter the milestone's one line, `<milestone>-fixes`, each an item of its page; that page is their list and is not split, whatever its length, since split it would be the many lines again. A small one becomes a line only when the person picks it. These lines end `· from <milestone>-review`, the delivery that found them (chapter 14 teaches the suffix, a parenthesis), and sit under the review line.
    4. The example, the review's page as it grades the chapter's findings, written for the chapter and said so, after the paragraph names them: the hand test's failure, the note of C4, and the three candidates of en :94-106 (pt :94-108), which it names by file and does not repeat. en, every row within 74 columns (widest 63, counted in characters):

       ```
       Grave
         returned-loan: a returned copy stays among the member's loans
       Medium
         1. LendForm.tsx:31, a note of return-book: a refused loan
            clears the member's card, and the librarian types it again
       Small
         2. myLoans.server.ts:12, seen: my-loans reads the table loan
         3. myLoans.server.ts:14 and repository.server.ts:21, latent
         4. repository.server.ts:18, weak
       ```

       pt the same rows, `Grave`, `Médios`, `Pequenos`, with `emprestimo-devolvido`, `devolver-livro`, `meusEmprestimos.server.ts`, `repositorio.server.ts`, visto, latente, fraco; /apply counts every row in characters and words it within 74.
    5. One sentence each on why: a grave finding is a line of its own because it is a promise broken, and its own page is small enough to read before it is built and to check after; the medium ones share one page because each is a fix a person would want and none breaks the promise; a small one waits for the person because its cost is a guess.
  * C6, `## A line, and not a fix` (en :114-135; pt :117-138):
    * en :116, "Each finding becomes a `[ ]` line in the same milestone, under the review line, waiting for `/propose`." (pt :119, "Cada achado vira uma linha `[ ]` no mesmo marco, sob a linha da revisão, esperando o `/propose`."): becomes: the grave finding and the fixes line, and a small one the person picked, go in the same milestone, under the review line, waiting for `/propose`.
    * en :118, "If the returned copy stayed among the member's loans, the milestone's lines would end this way" (pt :121): with the medium finding picked as well.
    * The block en :120-126 (pt :123-129): its last line becomes the grave line ending `· from m1-review`, and `m1-fixes` follows it. en, widest 68:

      ```
      [x] lend-book      the librarian lends a copy
      [x] return-book    the librarian records a return
      [x] my-loans       a member sees their loans and due dates
      [x] m1-review      the paragraph tested by hand, the code read
      [ ] returned-loan  a returned copy leaves the loans · from m1-review
      [ ] m1-fixes       the review's medium finding · from m1-review
      ```

      pt, widest 73 (the slug column stays at `emprestimo-devolvido`'s width, as the block has it):

      ```
      [x] emprestar-livro      o bibliotecário empresta um exemplar
      [x] devolver-livro       o bibliotecário registra uma devolução
      [x] meus-emprestimos     um membro vê os seus empréstimos e as datas
      [x] m1-review            o parágrafo testado à mão, o código lido
      [ ] emprestimo-devolvido o devolvido sai dos empréstimos · from m1-review
      [ ] m1-fixes             o achado médio da revisão · from m1-review
      ```

    * The rest of the section stands: "Each finding line is a delivery" (en :128) holds for both lines; "returned-loan still goes under m1-review" (en :135) holds, and gains "and so does `m1-fixes`" only if /apply finds the sentence reads as if the grave line were the only one.
  * C7, `## When the findings became one delivery`, its last sentence only (en :155, "Eight lines would have been eight pages, each small enough to read before it was built and to check after."; pt :158, "Oito linhas teriam sido oito páginas, cada uma pequena o bastante para ser lida antes de ser construída e conferida depois."): it teaches every finding as a line, which the grading replaces. Becomes, in the author's voice, without grading the eight: the grades would have given each grave one its own page, small enough to read before it was built and to check after, and only the rest one shared list; my page put all eight on one and graded none. The story's facts (en :146-154: eight findings, three about security, 879 lines, 620 ms to 94 ms, the faults found, "The process was not the cause; my choice was.") stay word for word.
  * C8, the team gain (en :162, "And because each finding becomes a line, the team sees the cost of the milestone's gaps in the queue, next to everything else it plans, instead of in fixes nobody reviewed."; pt :165): because the review grades its findings, the queue shows as lines the ones that break the milestone's promise and one line for what the person picked to fix, next to everything else it plans, and the rest stays listed on the review's page, never in fixes nobody reviewed. No number: the book has none for this gain, and a kit change is taught with none (docs/04 :29-30, :49).
  * C9, key points, still five (docs/04 :133):
    * Key point 3 (en :169, "a clause no delivery answers, one that fails in the person's hands, a slow test that fails, or a candidate the person confirms is a finding."; pt :172): gains that the review opens by copying the notes the range's pages left under `## For the review`, which the checker marks like candidates and the person confirms like them.
    * Key point 4 (en :170, "Each finding becomes a `[ ]` line in the same milestone, under the review line, even when the next milestone already exists, never a fix in the middle of the next milestone; the milestone closes when those lines are `[x]`."; pt :173): the review grades every finding: a grave one a `[ ]` line of its own; the medium ones the person picks on one `<milestone>-fixes` line, whose page is their list and is not split; the small ones listed, a line only when the person picks one; every line ending `· from <milestone>-review` under the review line, even when the next milestone already exists, never a fix in the middle of the next milestone; the milestone closes when those lines are `[x]`.
    * Key point 5 (en :171) stands: "finding lines" still names the lines a finding became.
* **docs/03** (`docs/03-Domain.md`)
  * C10, checker row (:40, "an agent or the review's own session opens each candidate's file and marks it seen, latent or weak (candidate) before the person sees it"): wrong by omission, since §8 has the checker mark each copied note too: "opens each candidate's file, and that of each note the review copied, and marks it seen, latent or weak".
  * C11, finding row (:36, "A review's findings are graded: grave a line each, the medium ones (médios) the person picks on the one fixes line, the small ones (pequenos) listed on its page"): wrong by omission, it leaves out what makes a finding medium or small and that a small one becomes a line on the person's pick: "the medium ones (médios), met in ordinary use while the clause still holds, the person picks on the one fixes line; the small ones (pequenos), a rare case, a latent or weak candidate or a cost nobody measured, listed on its page, a line only when the person picks one".

Terms of docs/03: milestone review, finding (achado, grave, médio, pequeno), note (nota), fixes line (linha de correções), candidate, checker (conferente), seen, latent, weak; none new. Sources: this repository's docs/05 §8 (:489-504) and §4 (:121-131), as the kit writes them, and the kit's `README.md` (:180-187, "a grave finding becomes a line each, the medium ones you pick share one line, and a small one becomes a line only when you pick it, all under the review"), taught as the kit is with no source note (docs/04 :29-30); no number. Cases: Ninjobs, the existing story only, nothing added; no Case A or Case B passage.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable: the Design slot says prototype, no reference, by choice (ADR-0019); the chapter adds blocks of text, a kind of content the build has shown, so no render proof.

**Out of scope.**

* The `· from <slug>` suffix's meaning, where a grave line goes among the planned lines, the note written on a delivery's page, a test or process line only on the person's word, and `queue.sh`'s `findings:`: `ch14-queue-findings` (M38); chapter 15 uses them with a parenthesis to chapter 14.
* What /apply does with a flaw in what it built, a flaw it cannot fix, a finding elsewhere, its last message's marks: `ch13-apply-findings` (M38), chapter 13.
* Chapter 11's summary of the grades (en :97-100), which points here: it already reads right and is `m35-fixes`' recent work; chapter 15 owns the grading and says it whole.
* The author's word for a review taking the clause tests and the confirmation (docs/05 §8 :478-487): not this line's sentence; the word does not cover the pick of medium findings (`kit-2026-11-12`, Left as they were).
* docs/03's candidate row (:39, "a finding only once the person confirms it"): it reads right beside §8, since a latent or weak candidate is listed with the small ones as a candidate, and is not changed.
* `work/m36-review.md`, running in this tree: another session's.

**Done when.**

* [x] C1 to C9 read as the Contract says in both editions; still three opening sentences and five key points.
* [x] C10 and C11 in docs/03.
* [x] Both editions written; the chapter opens with its value; no filler and nothing useful cut; no new number; the Ninjobs facts unchanged; no em dash; no run narration; every block within 74 columns, counted in characters.
* [x] Every sentence that points to chapter 13 or 14 stands without their M38 text, the pointer a parenthesis.
* [x] `make verify` green after the last edit, with its time.
* [x] `make book` builds both editions, under the run's lock, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent, the author corrects it in the review: the Ninjobs section's last sentence (en :155) taught every finding as a line, and the new rule puts the medium ones on one unsplit page, a page away from a story whose lesson was that one page for many findings was the mistake. The eight findings are not graded, since no source says which were grave; the story's facts stay, and only its lesson is rewritten (C7) so that a grave finding having its own page carries the reason, and the author's choice stays the cause.
* Decided by the agent, the author corrects it in the review: no number for the grading. The 21 lines one review of this repository queued (`m14-review`) would prove a kit change by a measure of how it was before, which docs/04 :29-30, the author's word of 2026-10-16 (a kit change taught with no numbers) and `ch15-review-by-areas` item 9 keep out; the problem is said in the present. The queue line, unlike chapter 13's, names no error.
* Decided by the agent, the author corrects it in the review: the reasons the chapter gives are the agent's, from no document: the checker marks a note because the file may have changed since it was written; the fixes page is not split because split it would be the many lines again; C5.5's three reasons for the grades.
* Decided by the agent, the author corrects it in the review: two new sections, notes then grades, placed after the code reading, because the checker that marks the notes is taught there; `## A line, and not a fix` stays for why a finding is a line and not a fix, its block gaining the fixes line.
* Decided by the agent, the author corrects it in the review: in the example the note on the lending form is medium, a librarian meeting it in ordinary use while lending still works; the seen candidate (a slice reading another's table) is small, a cost nobody measured, since no person meets it in use (the chapter's own block says no hand test shows it); the latent and the weak are small by §8's own list; the medium one is picked, so the block shows `m1-fixes`.
* Decided by the agent, the author corrects it in the review: chapter 15 owns the grading and says the three grades whole, chapter 11's two sentences staying as its summary; the note and the suffix are chapter 14's, used here with a parenthesis.
* Decided by the agent, the author corrects it in the review: docs/03's checker and finding rows are wrong by omission and go in scope (C10, C11); the candidate row is right and stays. The brief of this run limits /propose to this page and its mark, so the rows are /apply's.
* From the documents: the copying, the checker on the notes, the grades, the pick, the unsplit page and `· from <milestone>-review` (docs/05 §8 :489-504), grave (§4 :121-124), five key points and three opening sentences (docs/04), 74 columns (docs/04 :44), the kit's names kept in English in pt (docs/04).

## Outcome

Built by /apply on 2026-11-14, before the author read the page, on the author's word for this run ("Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão"). The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

* C1 to C9 in both editions, C10 and C11 in docs/03, as the Contract says; the opening keeps three sentences and the key points five. Since `46d5166` only en :18 / pt :18 had changed (`m36-fixes`), a sentence this delivery does not touch; every passage was found by its quoted sentence.
* Divergence, decided by the agent, the author corrects it in the review: the note's file is `src/features/loans/LendView.tsx:31` (pt `src/features/emprestimos/TelaDeEmprestimo.tsx:31`) and not the page's example `LendForm.tsx`, because chapter 4 already names the lending screen so; the blocks name it `LendView.tsx` / `TelaDeEmprestimo.tsx`.
* Widened within the chapter, decided by the agent: en :134 "And it stays in the milestone whose paragraph it fails" (pt :137) taught every finding line as a failed paragraph, which the fixes line is not; it reads "whose review found it, so a grave one keeps that milestone open until its paragraph holds". C6's "and so does `m1-fixes`" was added, since the sentence read as if the grave line were the only one.
* Blocks counted in characters: en grades 63, en queue 68; pt grades 71, pt queue 73; all within 74.
* Delivery review: one read-only Opus agent over the three paths, this line of docs/06, the page and docs/04. No must-fix. Fixed: the note's example "a screen of another slice" contradicted the example (`LendView.tsx` and `return-book` share `src/features/loans/`), now "a screen another delivery built"; "does not stop the delivery that found it" implied a grave flaw stops a delivery, cut; pt opening and key point 4 rewritten with verbs instead of appositions; the example now says the note was marked seen and confirmed; "a librarian's usual path" became "its usual path"; "the line of a small one"; "the rest one shared list at most"; "cada um como um item", "ficou como nota"; docs/03's checker row "marks each". Kept: "carteirinha" in pt, the natural word for a library card in a lending library's form; "every confirmed finding" in the opening and the grading, as docs/05 §8 says it; the parentheses to chapter 14, which the page requires and whose sentences stand without them (a note below).
* Verify green after the last edit: 10.5 s (11.4 s before the review's fixes), under the five-minute ceiling.
* `make book` built both editions under the run's lock: `/Volumes/Data/Projects/focus-kit-book/output/one-page-at-a-time.pdf` and `/Volumes/Data/Projects/focus-kit-book/output/uma-pagina-de-cada-vez.pdf`.
* No Case A or Case B passage; the Ninjobs facts are unchanged; no number added.

## For the review

* docs/05 §8 :449-455 and :489-491, with chapter 15 en :26 ("a delivery committed before the review's commit is outside the range from it"): a delivery committed after a review's `<review-head>` and before that review's commit is in neither review's range, so its notes are copied by no review and its code read by none; a person would see a note that never reaches a review page.
* chapter 15 en :117 and :138 (pt :120 and :141), "(chapter 14 shows the note)" and "(chapter 14 shows the suffix)": at this commit chapter 14 teaches neither; they hold once `ch14-queue-findings` lands, and each sentence stands without its parenthesis.

```commit
docs(ch15-review-grades): teach review notes and finding grades

- Chapter 15: the review copies the notes the deliveries left
- Grave a line each, medium on one -fixes line, small listed
- Example grades and queue block gain m1-fixes; both editions
- docs/03: checker marks the copied notes, grades defined

work/done/ch15-review-grades.md
```
