# ch07-rag-and-numbers

**Objective.** A reader of chapter 7 can say in a few words what retrieval-augmented generation (RAG) is, with a source to open, why focus-kit's documents work as a retrieval made for the project, which the author holds to be their main value, and that every focus-kit project gives each document the same number, so docs/06 is the queue in any of them. Both editions. From the author's reading of the book on 2026-10-18: "Introduce RAG (retrieval-augmented generation) in a few words, and how focus-kit's documents end up as a retrieval made for the project: in the author's view, their main value. Every focus-kit project gives each document the same number: docs/06 is always the queue (what to do, being done, done), in any project. RAG's definition with a source (docs/04)."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *Where the text goes.* The RAG sentences and the numbers sentence go in `## One place per fact` (pt `## Um lugar para cada fato`), where the chapter first says what the places are and that their numbers are fixed (en 07:14-17, pt 07:14-18): docs/04's "Say it where the doubt is born" puts what a thing is for where it is introduced. No new section: the point is two short paragraphs, and the section already holds both of its subjects. Source: docs/04 §Writing the book, **Say it where the doubt is born**, en 07:16.
2. *Said as it is: retrieval by name.* RAG, as Lewis et al. defined it in 2020, gives a model, with each question, passages a retriever found in a body of text the model was not trained on; in the paper the retriever is a neural network searching a dense vector index of Wikipedia. focus-kit builds no index: the agent reads `AGENTS.md`, which names where each kind of fact lives, and opens the document the command cites when it needs it, with its own tools. That is retrieval in RAG's broad sense, the text the model answers from found and brought in at the moment of the question, from a body of text the project wrote for that use; the chapter says it so, positively, and does not claim the kit is RAG in the paper's sense. Anthropic calls this way of loading context "just in time", by "lightweight identifiers (file paths...)" loaded "at runtime using tools", and that article supports the sentence. Source: the paper's abstract (arXiv 2005.11401, read on 2026-10-18: "the non-parametric memory is a dense vector index of Wikipedia"; its first page lists the authors' institutions as Facebook AI Research, University College London and New York University), Anthropic's "Effective context engineering for AI agents" (read on 2026-10-18), the kit's `references/documents.md` of `/brainstorm` and `/analyze`, en 07:14-17, en 01:77-89.
3. *"Their main value" is the author's, in the first person.* One sentence in the section of decision 1 says it as his view ("For me, this is the documents' main value: ..."), in the first person the book already uses for the author (docs/04 **Voice**; chapter 7 already does, en 07:132). The gain section gains one sentence, also in his voice, that sums it: every session and every person retrieves the same fact from the same place, in every focus-kit project. No number and no sentence about a missing number. Source: the draft, docs/04 **A gain per chapter** and **One gain**, work/ch04-focus-optional.md decision 5 (same shape).
4. *The numbers, the kit as it is.* The kit's description of the documents, the same file in `/brainstorm` and `/analyze` (`references/documents.md`), says: "The numbers are fixed, because the four commands cite them; the name after the number is in the documentation language". So in every focus-kit project docs/00 is the product and docs/06 the queue, whatever the file is called after the number. The chapter already says the numbers are fixed (en 07:16); this delivery adds the consequence the author named: a person or an agent who opens another focus-kit project finds the queue, what to do, what is being done and what is done, at docs/06, and each other fact at its same number. The file is named in plain words, no note (docs/04, Source notes). Source: the kit file, docs/04 **The kit as it is**.
5. *docs/03 gains a row.* RAG is a concept the book defines with a source, as `context window`, `context rot`, `compaction`, `automation bias` and `sycophancy` are; docs/03 says a new concept enters there first, in both languages. One row, after `compaction` (the context group): Behaviour quotes it. Leaving it out is defensible (the chapter mentions RAG once), and the author can say so in review. Source: docs/03's header, docs/05 §3 (a chapter's Contract lists the docs/03 terms it introduces), the skill of `/propose`.
6. *Portuguese words fixed here.* "geração aumentada por recuperação (RAG)" on first use, then "RAG" in both editions; "recuperação" for retrieval; "o agente busca pelo nome" for retrieval by name. The Portuguese edition translates any quotation and keeps the original in the note. Source: docs/03's header, docs/04 §Writing the book, Source notes.
7. *Two notes.* `[^lewis-rag-2020]` is new. Chapter 1's `[^anthropic-context-2025]` is reused with the same key and the same definition line: notes number per chapter (`scripts/build_book.py`: `prepare` starts its `notes` anew for each chapter and `note_anchor` takes the file's name), so the key in a second file is a note of its own; it is the first key in two chapters, and `make verify` green is the check. A quotation from either source, if /apply writes one, is a fragment it reads again in the source that day. Source: docs/04 Source notes, `scripts/build_book.py`.
8. *No pointer forward, no Ninjobs.* The new sentences name no chapter after 7 (the rule `early-no-forward-links` sets for chapters 0 to 7) and no Ninjobs fact, so they need no article for `pt-ninjobs-masculine` to agree. They lean on chapter 1's context window without a pointer: a reader in order has just read it. Source: work/early-no-forward-links.md, work/pt-ninjobs-masculine.md, docs/04 **Chapter pointers**.
9. *Key points.* The first bullet (en 07:148, pt 07:149) ends "with numbers fixed because the commands cite them"; it gains "the same in every project", three words. RAG gets no key point: a key point says what the reader does, and the gain is said once. Source: docs/04 **One gain**.
10. No new queue line, no split.

**Behaviour.**

* The reader of chapter 7, in either edition, reads in `## One place per fact` (pt `## Um lugar para cada fato`), after the sentence on fixed numbers and their names (en 07:16, pt 07:16-17), two short paragraphs:
  * what RAG is, in two or three sentences: a model is given, with each question, text a retriever found in a body of writing it was not trained on, and answers from it; the term and the method come from a 2020 paper by researchers at Facebook AI Research (Lewis et al.), whose retriever searched an index of Wikipedia; one source note;
  * that focus-kit's documents work as a retrieval made for the project: the body of text is the project's own documents, written for that use, one place per fact; the agent finds what it needs by name, `AGENTS.md` and the commands telling it which document holds which fact, and reads it when it needs it, which Anthropic calls loading context "just in time" (its note); no index is built, said only as what the agent does, never as a contrast;
  * the author's view, in the first person, that this is the documents' main value;
  * the consequence of line 16's fixed numbers, its cause not said again: every focus-kit project gives each document the same number, as the kit's description of the documents (the phrase en 07:93 already uses for that file) writes them, so docs/06 is the queue, what to do, what is being done, what is done, in any focus-kit project, and so is every other number, whatever the name after it.
* `## What the team gains` (pt `## O que o time ganha`) keeps its three sentences and gains one, in the author's voice: every session and every person retrieves a fact from the same place, and in another focus-kit project from the same number.
* The first key point ends "with numbers fixed because the commands cite them, the same in every project" (pt the same in Portuguese).
* docs/03 gains, after the `compaction` row: `| retrieval-augmented generation (RAG) | geração aumentada por recuperação (RAG) | none | Giving a model, with each question, text a retriever found in a body of writing it was not trained on, so it answers from that text (Lewis et al., 2020); focus-kit's documents work as such a body, made for the project and read by name. |`
* Source notes, at the end of chapter 7, both editions, the title in English in both:
  * `[^lewis-rag-2020]: Patrick Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", 2020. <https://arxiv.org/abs/2005.11401>`
  * `[^anthropic-context-2025]:` as chapter 1 writes it.
* Checked at apply time:
  * `grep -n "RAG\|retriev" book/en/07-the-documents.md` and `grep -n "RAG\|recupera" book/pt/07-the-documents.md` print lines only in the two paragraphs, the gain section and the notes.
  * `grep -n "lewis-rag-2020\|anthropic-context-2025" book/{en,pt}/07-the-documents.md` prints a call and a definition of each, in each edition.
  * `grep -nE "[Cc]hapters? ([89]|[1-9][0-9])|[Cc]apítulos? ([89]|[1-9][0-9])" ` over the new sentences prints nothing.
  * `git diff book/` shows only chapter 7, in the places above.
* Fails: a sentence saying or implying the kit builds an index, embeddings, a vector store or a database of the documents; a sentence that sets the documents against RAG ("not ... but"); "main value" said as a fact and not as the author's view; RAG without its note; a quotation not read in the source on the day; a number added; a forward pointer; a Ninjobs or Case A or Case B mention; the numbers said as a rule of this book's repository instead of the kit's; any change outside chapter 7 and docs/03's new row; the editions differing; an em dash; a run narrated.

**Contract.**

* Files: `book/en/07-the-documents.md`, `book/pt/07-the-documents.md` (the section `One place per fact`, the gain section, the first key point, the notes); `docs/03-Domain.md`, one new row after `compaction`.
* Terms of docs/03: `retrieval-augmented generation (RAG)` new (decision 5); `project documents`, `rules file`, `context window` as their rows have them. Sources: Lewis et al. 2020, new; Anthropic 2025, chapter 1's. Cases: none. Exercises: none (ADR-0017).
* docs/00, docs/01, docs/02, docs/04, docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* `early-no-forward-links` edits en 07:15 and 17 (pt 07:15 and 18), the lines on either side of where this delivery adds its paragraphs, and 07:35, 36, 41, 59, 61, 83, 89; it applies last of M18's lines on chapters 0 to 7 and finds its pointers by text. Not the same lines (docs/05 §4), though git may show one hunk: each session stages only its own lines. This delivery adds no pointer for it to remove (decision 8).
* `ch07-talk-not-edit` (a draft) edits `## Living documents`, pt 07:133 and its English source: no shared section.
* `pt-ninjobs-masculine` changes Ninjobs's article in pt 07:10, 56 and 144 and docs/03's `case` row: this delivery adds no Ninjobs mention, and its docs/03 row is a hunk apart.
* Whichever lands later finds the section, the gain and the key point by their text, not their line numbers.

**Out of scope.**

* Building or recommending a vector index or embedding search for a project: not what the kit does (decision 2).
* Chapter 1, which already teaches the context window and cites Anthropic: unchanged.
* Renaming the documents, or the Portuguese edition's extra sentence on folder names (pt 07:17): not this line's.
* The other sections of chapter 7: other deliveries' or unchanged.

**Done when.**

* [x] Both editions written: the two paragraphs, the gain sentence, the key point's words and the two notes, as Behaviour says.
* [x] docs/03's row added as Behaviour quotes, with the one word change Divergences gives.
* [x] Chapter 7 still opens with its value, keeps its gain said once, no filler and nothing useful cut.
* [x] Every number sourced: none added; the definition of RAG carries its note.
* [x] `make verify` green: edition parity, prose rules, width, links, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author: left to the driver, who builds the book once at the end of the batch.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunks of docs/03 and docs/06, commit message in a `commit` block: the driver marks and stages (batch rules).

**Divergences.** The delivery review's suggestions are applied on the driver's word (batch rule 5). The text keeps the page's intent and differs from the Behaviour's exact words as follows:

* "a body of writing it was not trained on" becomes "a body of writing kept outside the model" in en, in pt ("guardado fora do modelo") and in the docs/03 row. The paper sets the retrieved text apart from what the model's weights hold; it does not say the model never saw that text (its BART was very likely pretrained on text that included Wikipedia).
* en "work as a retrieval made for the project" becomes "work as retrieval made for the project".
* "as the kit's description of the documents writes them" becomes "numbers them" (pt "os numera"), and pt "a descrição dos documentos no kit" becomes "do kit".
* pt "O agente busca pelo nome" becomes "O agente busca o que precisa pelo nome", matching the English. Decision 6's phrase stays inside it.
* pt "cada outro número" becomes "cada um dos outros números", and the gain sentence gets the comma before "em outro projeto".
* The two paragraphs follow the section's last sentence (en 07:17, pt 07:18), so line 17 is not split from line 16. They open with one sentence that leans on chapter 1's window, with no pointer (decision 8).
* Not applied: moving the numbers paragraph before the RAG one, because Behaviour lists RAG first. "Sob demanda" for "just in time" was not used; the pt keeps "na hora certa".

**Proof.**

* The `grep` for "RAG" and "retriev" (pt "recupera") prints en 07:20-22 and 155, and pt 07:21-23 and 156: the paragraphs and the gain line only.
* The `grep` for the two keys prints 4 lines per edition: one call and one definition of each.
* There are no chapter numbers in the new sentences, and `git diff` shows only chapter 7 and the docs/03 row.
* The quotations were read in their sources on 2026-10-18. The arXiv abstract says "dense vector index of Wikipedia, accessed with a pre-trained neural retriever". Anthropic writes "just in time" for loading "lightweight identifiers (file paths...)" "at runtime using tools".
* `make verify` passes build, parity, em dash, prose, width, links and disclosure, with exit 0. The first run failed only on chapter 24's web.archive.org link, which was refused; it passed on the rerun.

**Review.** A read-only Opus reviewer that did not write the change read the diff against this page and docs/04. Nothing breaks the page or docs/04, the text matches Behaviour, and no Fails pattern appears. Its accuracy point and its wording suggestions are applied as Divergences says. There is no new queue line.

**Decisions.** The batch driver owns docs/06, the staging and the commit, and runs `make book`.

```commit
docs(ch07-rag-and-numbers): say the documents work as retrieval, numbered alike in every project

- Chapter 7, both editions: what RAG is (Lewis et al., 2020, note), the documents as retrieval made for the project, read by name just in time (Anthropic, note), the author's view that this is their main value; every focus-kit project gives each document the same number, so docs/06 is always the queue; one gain sentence; the first key point adds "the same in every project"
- docs/03: retrieval-augmented generation (RAG) row after compaction

book/en/07-the-documents.md
book/pt/07-the-documents.md
docs/03-Domain.md
docs/06-Queue.md
work/done/ch07-rag-and-numbers.md
```
