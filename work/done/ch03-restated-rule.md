# ch03-restated-rule

**Objective.** A reader of chapter 3, in either edition, reads that a rule restated is read and changed in every file that restates it (8 of 8 for Spec Kit, 4 of 6 for OpenSpec, one page for focus-kit), and reads the Ninjobs count as the cost of the process the author ran on OpenSpec, the cause chapter 9 gives, not as the tool's.

**Decided from the documents.**
1. Both findings hold against the text. L6: `book/en/03-spec-driven.md` line 64 says Spec Kit restates the rule "in each of its 8 files" and OpenSpec "in 4 of its 6"; line 66 then says "a rule restated in each file is read in each one in review, and when it changes, it changes in each", which is false for OpenSpec's two files that do not restate it. L7: line 77, the first sentence of §What the team gains' Ninjobs passage, says "OpenSpec produced 37,228 lines of spec for four screens", while chapter 9 §How it was and §What went wrong give the cause as the author's process: every feature in its full form, a decision written again in the documents, the specs, the changes and the ADRs, and 29 checks. Portuguese: lines 66 and 77 of `book/pt/03-spec-driven.md`, the same two sentences.
2. The counts stay where line 64 gives them (8 of 8, 4 of 6, 1 page of 82). Line 66 stops repeating a count and says "every file that restates it", which is true of both tools (docs/04 §Numbers that prove; `plain-numbers` cut "8 times" and "8 places" from this very passage on purpose, so the count is not restored).
3. The Ninjobs sentence keeps its number and its method, 37,228 lines under the tool's folder counted with `wc -l`, because that pair is the chapter's gain (`plain-numbers`, decision 5; docs/04 §Chapter shape). Only its subject changes, from the tool to the process the author ran on it. The sentence after it, "The causes were more than the tool", already points to chapter 9; it says whose causes they were.
4. Ninjobs is the author's own process: the cause is the author's choices, never OpenSpec and never FOCUS (docs/00 product question 7 and the book's rule that FOCUS is the answer). So the sentence names neither FOCUS nor the architecture, and says only what chapter 9 says first: the way the author ran the tool.

**Behaviour.**

* A reader of §Where the cost of many places begins reads, after "Spec Kit restates it in each of its 8 files, OpenSpec in 4 of its 6, focus-kit on its one page", that a restated rule is read again in each file that restates it in review and, when it changes, changes in every one of them, or disagrees with itself in the ones that were missed; the sentence says "every file that restates it" (pt "todo arquivo que a repete") and not "each file". Draft for /apply to polish: "The difference is how many other files say it again: a rule restated in a file is read again in that file in review, and when it changes, it changes in every file that restates it, or it disagrees with itself in the ones that were missed." (pt: "A diferença é quantos outros arquivos a dizem de novo: uma regra repetida num arquivo é lida de novo nele na revisão, e quando muda, muda em todo arquivo que a repete, ou se contradiz naqueles que ficaram para trás.")
* Checked: `grep -n "restated in each file\|repetida em cada arquivo" book/*/03-spec-driven.md` finds nothing; the 8 of 8 and 4 of 6 are on line 64 as today and appear once in the section.
* A reader of §What the team gains reads that the process the author ran on OpenSpec, on Ninjobs, produced 37,228 lines of spec for four screens (every line under the tool's folder, counted with `wc -l`), with none of the core flow built. Draft for /apply to polish within these limits: "On Ninjobs, my own product, the process I ran on OpenSpec produced 37,228 lines of spec for four screens (every line under the tool's folder, counted with `wc -l`), and none of the core flow existed yet." (pt: "Na Ninjobs, meu próprio produto, o processo que eu rodei sobre o OpenSpec produziu 37.228 linhas de especificação para quatro telas (toda linha sob a pasta da ferramenta, contada com `wc -l`), e nada do fluxo principal existia ainda.")
* The next sentence says the causes were the author's own way of running the tool as much as the tool, with the pointer to chapter 9 kept and the clause "the count is what a spec costs when it becomes the work" kept. Draft: "The causes were my choices as much as the tool, and [chapter 9](09-birth-of-focus-kit.md) tells them; the count is what a spec costs when it becomes the work." (pt: "As causas foram minhas escolhas tanto quanto a ferramenta, e o [capítulo 9](09-birth-of-focus-kit.md) as conta; a contagem é o que uma especificação custa quando vira o trabalho.")
* Checked: `grep -n "OpenSpec produced\|OpenSpec produziu" book/*/03-spec-driven.md` finds nothing. In chapter 3, no sentence has OpenSpec or Spec Kit as the cause of Ninjobs' cost.
* The gain still ends with the pair: 22,650 lines in 93 finished pages after the move to one page per delivery. "Fifteen days" does not return to chapter 3 (chapter 9 owns it).
* A reader who goes to chapter 9 for the causes finds "the process" and "the old process" there, consistent with chapter 3's "the process I ran".
* Fails: a sentence that restores "8 times", "8 places" or another count line 64 already gives; a sentence that names FOCUS, the architecture or OpenSpec's design as the cause; a number cut or rounded; one edition changed and not the other.

**Contract.**

* Files: `book/en/03-spec-driven.md`, `book/pt/03-spec-driven.md`; no other file.
* Sections and lines (same in both editions): §Where the cost of many places begins, line 66, "The difference is how many other files say it again: ..."; §What the team gains, line 77 (the Ninjobs sentence) and line 78 (the sentence on the causes). Lines of §Where the cost... 63 to 65 (the counts), the Böckeler quotations and every `[^...]` key stay as they are.
* Terms of docs/03: none new. Sources: `[^spec-driven-run]` (the counts) and `[^bockeler-2025]` unchanged, same number of references in both editions. Ninjobs' numbers are the author's own counts, no note (docs/04 Private cases; Ninjobs is public by name). Cases: Ninjobs, as today; no Case A or Case B passage. Exercises: none (ADR-0017).
* docs/03, docs/04, docs/05: no change. docs/06: this line `[>]` by the driver, `[*]` when /apply starts, `[x]` by /apply.

**Deliveries in flight on the same chapter (work/).**

* `ch3-spec-cut` (`[>]`, M15, after `m14-review`): cuts the taxonomy and the second key point of chapter 3. Its Contract says §Where the cost of many places begins and §What the team gains are "unchanged" and its Behaviour reads the Ninjobs count "as today". Same chapter, different sentences, no line in common except that it shifts line numbers and rewrites key point 5 (this page does not touch the key points). It runs after this line, so "as today" means as this page leaves it; /apply of `ch3-spec-cut` finds the passages by their words, not by line. Nothing on that page needs correction.
* `one-gain-section` (`[>]`, M15, last): re-reads every chapter's gain and key points. It will see the Ninjobs sentence this page rewrites; the sentence keeps its one pair, the number it allows.
* `prologue-and-why`: "Chapter 9's story and chapter 3's count: unchanged"; it points to chapters 3 and 9 for Ninjobs, which still hold.
* `renumber-chapters` (after the merges): chapter 3 becomes chapter 2 and chapter 9 becomes chapter 6; the "chapter 9" link in the rewritten sentence is moved by its script, so this page writes the current number.
* `ch09-key-points` (this batch, same driver): changes chapter 9's key points so they give the cause the gain gives; the sentence added here says "the process", the same cause. No common line.

**Out of scope.**

* Chapter 9, whose own key points `ch09-key-points` handles, and any other chapter that names OpenSpec beside the Ninjobs count (chapter 1's pointer, chapter 4): the review named chapter 3.
* The taxonomy cut, the key points and the caveat: `ch3-spec-cut`.
* The counts of the run (756, 180, 82) and their record: `spec-driven-run`, ADR-0017.
* Restoring "fifteen days" or any number `plain-numbers` cut.

**Done when.**

* [x] Both editions changed at the lines of Contract; the two greps of Behaviour find nothing in `book/en` and `book/pt`; the counts are on line 64 as before.
* [x] Chapter 3 still opens with its value, keeps its gain with its number, no filler and nothing useful cut.
* [x] Every number still sourced; every `[^key]` keeps a reference and a definition in both editions.
* [x] `make verify` green, disclosure scan included; no em dash.
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Decisions in the review.** Chosen alone, because the author could not answer; corrections go in the review.

* Line 66 says "every file that restates it" with no count, and the 8 of 8 and 4 of 6 stay on line 64 only (docs/04 §Numbers that prove, `plain-numbers` decision 5); the alternative, repeating both counts in line 66, was rejected as a number said twice.
* The Ninjobs sentence names "the process I ran on OpenSpec" as what produced the lines, and the next sentence says the causes were "my choices as much as the tool"; the alternative "the old process" was rejected because a reader of chapter 3 has not met it (chapter 9 defines it). Source: chapter 9 §What went wrong, and the book's rule that Ninjobs' cost came from the author's process, never FOCUS.
* The Ninjobs pair stays in chapter 3's gain with its method (`plain-numbers`, decision 5).
* No OD-3 approval: no Case A or Case B text changes.

**Decisions in /apply.** Chosen alone, under the batch's rule; corrections go in the review.

* The Ninjobs sentence opens with its subject, "The process I ran on OpenSpec, on Ninjobs, my own product, produced 37,228 lines ..." (pt "O processo que eu rodei sobre o OpenSpec, na Ninjobs, meu próprio produto, produziu 37.228 linhas ..."), not with "On Ninjobs, my own product, the process I ran on OpenSpec produced" as the draft had it. The draft contains "OpenSpec produced" and "OpenSpec produziu", so the page's own check would have found it; the new order is the Behaviour's own ("the process the author ran on OpenSpec, on Ninjobs, produced"), keeps every word, number and method of the draft, and leaves the grep empty.
* The causes sentence keeps the draft, "my choices as much as the tool", rather than dropping the tool: chapter 9 §What went wrong lists the specs and the changes, the tool's files, among the six places, and the sentence names neither OpenSpec's design nor FOCUS as the cause.
* Every other sentence is the draft as written, in both editions.

**What happened.**

* `book/en/03-spec-driven.md` and `book/pt/03-spec-driven.md`, line 66: "a rule restated in a file is read again in that file in review, and when it changes, it changes in every file that restates it" (pt "uma regra repetida num arquivo é lida de novo nele na revisão, e quando muda, muda em todo arquivo que a repete"); the counts stay on line 64 only.
* Lines 77 and 78: the process the author ran on OpenSpec produced the 37,228 lines, and the causes were "my choices as much as the tool", with the pointer to chapter 9 and "the count is what a spec costs when it becomes the work" kept. Line 79's pair, 22,650 lines in 93 pages, unchanged. "Fifteen days" not added.
* No divergence from the Contract; no document changes (docs/03, docs/04, docs/05 untouched); no dependent queue line waits on this one.

**Proof.**

* `grep -n "restated in each file\|repetida em cada arquivo\|OpenSpec produced\|OpenSpec produziu" book/*/03-spec-driven.md` finds nothing; "8 files"/"8 arquivos" and "4 of its 6"/"4 dos seus 6" appear on line 64 of the section only (line 58's "8 files and 756 lines" is the run's count, unchanged).
* `[^spec-driven-run]` and `[^bockeler-2025]` untouched, same references in both editions.
* `make verify` green; `make book` built both editions, and the PDFs are `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

```commit
docs(ch03-restated-rule): a restated rule changes where it is restated
- ch3: a restated rule changes in every file that restates it
- ch3: the Ninjobs lines are the cost of the process the author ran
- ch3: the causes are the author's choices as much as the tool
- both editions

work/done/ch03-restated-rule.md
```
