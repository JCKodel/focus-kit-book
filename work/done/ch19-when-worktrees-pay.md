# ch19-when-worktrees-pay

**Objective.** A reader of chapter 19 learns one rule for when deliveries run at once: deliveries whose files do not meet share one folder; deliveries whose files meet run at once only in worktrees, as §What a worktree is and when it pays says with the kit's wording, at the cost of a merge that is a decision about the code; and the measured gain is stated only for the case it measured; both editions. Found by `m15-review` (work/done/m15-review.md, B25: "19:84 against 19:242-268: when a worktree pays, said two ways; :84 follows the kit's wording. Seen.").

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. The side that moves is §When parallel stops paying, the gain and the last key point, not line 84. Line 84 and key point 267 say what the kit says (`.claude/skills/analyze/references/documents.md`, the "a worktree per delivery" strategy: "For parallel work by several people, or by one person whose deliveries touch the same files"), and the example that follows 84 (both deliveries need `src/features/loans/`) depends on it. The book teaches the kit as it is. Source: finding B25, the kit's `references/documents.md`, docs/05 §5 Git slot.
2. Line 241's point stays: across worktrees the merge stops on files both change, and its resolution is a decision about the code. Line 242 stops saying "pair deliveries whose files do not meet" as a rule for both forms; it says one folder needs files that do not meet, worktrees let files meet when the person can make the merge's decision, otherwise order the lines. The condition is said in §What a worktree is (the owner) and applied in §When parallel stops paying, not paraphrased a third way. Source: AGENTS.md (a decision said once), docs/04 chapter shape.
3. The gain does not claim a time for deliveries whose files meet. The measured run (155 s against 277.2 s) was two deliveries whose code files did not meet; only the queue conflicted at the merge (work/done/clinic-worktrees-run/README.md, Merges). So line 260 says what was measured instead of stating a general condition, and adds the merge to what bounds the gain. Source: ADR-0015, docs/04 (every number says where it comes from).
4. Line 254 ("This book ... stays on trunk for those reasons, and its docs/05 lets two sessions work in one folder on free lines that touch different files") stays: it already names different files, so it does not contradict 84. Source: chapter 19 as it stands.
5. Line 4 (the opening), line 72 and key points 264 to 267 stay: each already agrees with 84 (line 72 and 265 offer "give one of them a worktree" for a file both need). Source: chapter 19 as it stands.
6. No docs/03 term, no new queue line, no split: worktree, trunk, merge and free line are already the book's words; two files, three sentences each. Source: docs/03, docs/05 §1.

**Behaviour.**

* A reader of §When parallel stops paying, **Files both change**, reads as its third sentence:
  * en: "So list the files each delivery will touch, from its queue line, docs/01 and the code it names: deliveries whose files do not meet can share one folder; deliveries whose files meet run at once only in worktrees, and only when you can make the merge's decision; otherwise, order them with `· after <slug>`." in place of "So pair deliveries whose files do not meet: read each queue line, docs/01 and the code it names, and list the files each will touch."
  * pt, §Quando o paralelo deixa de compensar, **Arquivos que as duas mudam**: "Então liste os arquivos que cada entrega vai tocar, a partir da sua linha da fila, do docs/01 e do código que ela nomeia: entregas cujos arquivos não se encontram podem dividir uma pasta; entregas cujos arquivos se encontram rodam ao mesmo tempo só em worktrees, e só quando você consegue tomar a decisão do merge; senão, ordene-as com `· after <slug>`." in place of "Então junte entregas cujos arquivos não se encontram: leia cada linha da fila, o docs/01 e o código que ela nomeia, e liste os arquivos que cada uma vai tocar."
* A reader of §What the team gains reads as its last sentence:
  * en: "The measurement is of two deliveries whose code files did not meet; the gain ends at the speed of the person who reviews, commits and merges them." in place of "The gain holds while the deliveries' files do not meet, and it ends at the speed of the person who reviews and commits them."
  * pt, §O que o time ganha: "A medição é de duas entregas cujos arquivos de código não se encontravam; o ganho termina na velocidade da pessoa que as revisa, faz o commit e o merge delas." in place of "O ganho vale enquanto os arquivos das entregas não se encontram, e termina na velocidade da pessoa que as revisa e faz o commit delas."
* A reader of the last key point reads:
  * en: "* Parallel pays while the deliveries' files do not meet, or meet only across worktrees whose merge you can decide, the machine's ports and databases do not collide, the disk holds each worktree's dependencies, and one person can still review each delivery." in place of "* Parallel pays while the deliveries' files do not meet, the machine's ports and databases do not collide, the disk holds each worktree's dependencies, and one person can still review each delivery."
  * pt: "* O paralelo compensa enquanto os arquivos das entregas não se encontram, ou só se encontram entre worktrees cujo merge você consegue decidir, as portas e os bancos de dados da máquina não colidem, o disco comporta as dependências de cada worktree, e uma pessoa ainda consegue revisar cada entrega." in place of "* O paralelo compensa enquanto os arquivos das entregas não se encontram, as portas e os bancos de dados da máquina não colidem, o disco comporta as dependências de cada worktree, e uma pessoa ainda consegue revisar cada entrega."
* Checked, both editions: `grep -n "pair deliveries whose files do not meet\|The gain holds while" book/en/19-worktrees.md` and `grep -n "junte entregas cujos arquivos\|O ganho vale enquanto" book/pt/19-worktrees.md` find nothing; `grep -n "only when you can make the merge's decision" book/en/19-worktrees.md` and `grep -n "só quando você consegue tomar a decisão do merge" book/pt/19-worktrees.md` find one line each.
* Unchanged, both editions: line 84 / §What a worktree is and when it pays (the kit's two cases), key point 267, line 4, line 72, line 254, the measured numbers and the `[^parallel-run]` note.
* Fails: one edition changed and not the other; a time, percentage or other number claimed for deliveries whose files meet; line 84 or key point 267 changed away from the kit's wording; a new statement of when a worktree pays beyond the three sentences above; any other line of chapter 19 or any other file changed but this page and the line's marks in docs/06; an em dash; a prose rule of docs/04 hit; a code block past 74 columns.

**Contract.**

* Files: `book/en/19-worktrees.md`, `book/pt/19-worktrees.md`; no other file.
* Sections and lines (the text is the locator, the number a courtesy, working tree of 2026-10-17): §When parallel stops paying / §Quando o paralelo deixa de compensar, third sentence of **Files both change** (en and pt line 242); §What the team gains / §O que o time ganha, last sentence (line 260); §Key points / §Pontos-chave, last item (line 268).
* Terms of docs/03: none new. Sources: none added or removed; `[^parallel-run]` keeps pointing to the run, whose README says which files each delivery changed. Cases: none (no Case A or Case B passage touched). Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on nearby chapters.** `batch-propose` (M16, draft in work/batch-propose.md) will edit chapter 19, perhaps §When parallel stops paying, and its draft leans on "`/apply` stays parallel only on free lines whose files do not meet, as chapter 19 already teaches", which is the one-folder half of this page's rule and stays true. Run the two one after the other, or stage by hunk; `batch-propose`'s /propose rereads §When parallel stops paying after this lands. `ch17-delivery-time` and `ch18-log-evidence` are other chapters; no file in common.

**Out of scope.**

* The kit's wording of the "worktree per delivery" strategy: a note for the kit, not this book; the book follows it (decision 1).
* Teaching batches of `/propose` or `/apply`: owned by `batch-propose`.
* A measurement of deliveries whose files meet: no run exists, and the book states no gain without one (decision 3).
* Chapter 19's other sections: they already agree with line 84 (decisions 4 and 5).

**Done when.**

* [x] Both editions changed as Behaviour says; its greps give the results it names.
* [x] Chapter 19 says one thing about when a worktree per delivery pays: line 84 and key point 267 state it, 242 and 268 apply it, and nothing contradicts it.
* [x] Chapter 19 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added; the gain's numbers are bound to what was measured.
* [x] `make verify` green.
* [x] `make book` run, and both PDF paths given to the author.
* [x] Finding B25 of the M15 review is settled.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**Proof.** `make verify` green; `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. The Behaviour greps: the old phrases find nothing in either edition; the new phrase finds one line in each.

* Built: en and pt 19-worktrees.md lines 242, 260 and 268, word for word as Behaviour says; nothing else in the chapter changed.
* B25 settled: line 84 and key point 267 state when a worktree per delivery pays, as the kit words it; 242 and 268 apply it; 260 binds the measured gain to the run it measured.
* Divergences: none. Omissions: none.

**Delivery review.** A read-only agent on Opus read `git diff` and `git diff --cached` of the two chapter files and this line's hunk of docs/06 against this page, docs/04 and AGENTS.md. The three sentences match Behaviour word for word in both editions; lines 4, 72, 84, 254 and 267, the numbers and the note are unchanged; the Portuguese means what the English does; no em dash, no number added, no narrated run. Nothing breaks the page, docs/04 or this delivery's lines.

1. en/pt 268: the added clause sits in a list of conditions joined by commas and takes two reads. It breaks no rule and is the Behaviour's text; kept, no change and no queue line.

**Commit.**

```commit
docs(ch19-when-worktrees-pay): say once when a delivery's worktree pays

- One folder for deliveries whose files do not meet
- Files that meet run at once only in worktrees whose merge you decide
- Bind the measured gain to the two deliveries it measured
- Both editions

work/done/ch19-when-worktrees-pay.md
```
