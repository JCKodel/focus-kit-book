# m36-fixes

Defined before the author read it: the author's word for this run, relayed by the session that runs the queue on the author's behalf on 2026-11-13, is "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão" (close every open line of docs/06 without supervision), and for the reviews "Todas, médios entram" (every medium finding enters the one fixes line). So each question the documents leave open is answered by the agent's recommendation, marked "decided by the agent, the author corrects it in the review" (docs/05 §4, a command that says to decide alone).

**Objective.** After chapters 14 and 15 the reader meets no contradiction in why `after all` leaves out the cancelled lines, and no doubt about which line the person re-decides, in the two places m36-review found: the reason chapter 14 gives agrees with the 27-slug list and with a review that can be dropped, and chapter 15's re-decision attaches to the waiting line, never to the cancelled one.

**Behaviour.** What the reader can do or explain afterwards, one item per medium finding of `work/done/m36-review.md`:

* M1. From chapter 14 alone, say why `after all` leaves out the cancelled lines: a review counting a cancelled line would wait on it, and of the person's ways out, dropping the review loses the test of the milestone's paragraph, and rewriting it turns its `after all` into a list of every other line above it, which is what the error of 2026-10-26 came to.
* M1, failure: asked "can a milestone review ever be dropped, or its `after all` rewritten?", the reader of chapter 14 never answers "no, a review is neither dropped nor rewritten"; and reading :223 and :224 back to back finds no claim one denies, neither "nothing the person could write freed it" beside a list the person wrote.
* M1, edge: the reader still says that after the rule, a cancelled line never keeps the review waiting, and a line whose `after` names the cancelled one does, until the person re-decides it (chapter 14 :225 to :229 unchanged).
* M2. From chapter 15 alone, say that the line the person re-decides is the one whose `after` names a cancelled line, and that the review waits with that line until the person does.
* M2, failure: asked "in chapter 15, what does the person re-decide, `print-card` or `reprint-card`?", in chapter 14's example terms, the reader answers the waiting line, `reprint-card`, never the cancelled one; in the Portuguese edition no feminine pronoun can be read as `a cancelada`.
* In the Portuguese edition, the same, with docs/03's terms (revisão de marco, marco, linha da fila, dependência).

**Contract.** Four chapter files, line numbers en / pt at `4ee7736`, where m36-review read them, the same at HEAD `066b3bf` (`git diff 4ee7736 066b3bf -- book/` is empty). Each change quotes the sentence it replaces so a drift is found; pt follows en sentence for sentence. The text below is the agent's proposal; /apply may word it otherwise within what each item says.

* **M1, ch14** (`book/{en,pt}/14-queue-states.md`), two sentences of `## A session that ended, a delivery cancelled`:
  * :222 / :224, "A milestone's review would have no such way out." / "A revisão de um marco não teria essa saída.": says the short form of the new reason, so the contradiction does not survive one line up. Proposed: "A milestone's review would have no good way out." / "A revisão de um marco não teria uma boa saída."
  * :223 / :225, "A review that named every line above it would name the cancelled one too and wait, as `reprint-card` does, on a line only the person's decision clears; but a review is neither dropped nor rewritten on what exists, so no re-decision of its own would clear it." / "Uma revisão que nomeasse toda linha acima dela nomearia também a cancelada e esperaria, como `reimprimir-cartao` espera, por uma linha que só a decisão da pessoa libera; mas uma revisão não é cancelada nem reescrita sobre o que existe, então nenhuma redecisão dela mesma a liberaria.": the first clause stays word for word (the delivery review of `ch14-15-after-all-dropped` gave it); the clause after the semicolon says what the person's ways out cost a review, without saying they are the only ones and without denying either, since both happened (docs/05 §4 :198 to :201, docs/06 :512's dropped `m20-review`, en :224's list). Proposed: "...; and of the person's ways out, dropping the review loses the test of the milestone's paragraph, and rewriting it on what exists turns its `after all` into a list of every other line above it." / "...; e das saídas da pessoa, cancelar a revisão perde o teste do parágrafo do marco, e reescrevê-la sobre o que existe troca o `after all` dela por uma lista de todas as outras linhas acima dela."
  * :224 / :226, "On 2026-10-26, in one project, a Milestone 1 review waited on a line the person had dropped: the queue script answered `after <slug>, dropped: re-decide`, nothing the person could write freed it, and the review's `after all` was replaced by a list of the other 27 slugs." / "Em 2026-10-26, num projeto, a revisão de um Marco 1 esperou uma linha que a pessoa tinha cancelado: o script de fila respondia `after <slug>, dropped: re-decide`, nada que a pessoa escrevesse a liberava, e o `after all` da revisão foi trocado por uma lista dos outros 27 slugs.": the clause "nothing the person could write freed it" / "nada que a pessoa escrevesse a liberava" goes, since the list was written by the person and freed the review, so beside the new :223 it would contradict the same sentence again; the date, the project unnamed, the script's answer and the 27 slugs stay, as the changelog's `## 2026.10.27.1` has them. Proposed: "On 2026-10-26, in one project, a Milestone 1 review waited on a line the person had dropped: the queue script answered `after <slug>, dropped: re-decide`, and only replacing the review's `after all` with a list of the other 27 slugs freed it." / "Em 2026-10-26, num projeto, a revisão de um Marco 1 esperou uma linha que a pessoa tinha cancelado: o script de fila respondia `after <slug>, dropped: re-decide`, e só trocar o `after all` da revisão por uma lista dos outros 27 slugs a liberou." Under the new :223 it is the second way out, taken. The capital of "Milestone 1" / "Marco 1" stays (m36-review small 8, not picked).
  * :220 / :222 ("is the person's to re-decide") and :225 to :229 / :227 to :231 stay.
* **M2, ch15** (`book/{en,pt}/15-closing-a-milestone.md`) :18 / :18, its last clause, "and a line whose `after` names a cancelled one waits for the person to re-decide it, and the review waits with it." / "e uma linha cujo `after` nomeia uma cancelada espera a pessoa redecidi-la, e a revisão espera com ela.": the line still says it waits, and the line re-decided is named, not a pronoun. Proposed: "and a line whose `after` names a cancelled one waits, and the review with it, until the person re-decides the line that waits." / "e uma linha cujo `after` nomeia uma cancelada espera, e a revisão com ela, até a pessoa redecidir a linha que espera." Every pronoun against every noun of the clause, both editions: "it" / "ela" stands in the gapped "the review [waits] with it" / "a revisão [espera] com ela", so it is the one that waits, the line; the cancelled line does not wait, the review does not wait with itself, and "the person" / "a pessoa" comes after it; "the line that waits" / "a linha que espera" cannot be the cancelled one, which waits for nothing. The rest of :18 stays.
* No pointer added: chapter 15 already points to chapter 14 (:26, :88); chapter 14 needs none here (docs/04, chapter pointers).

Terms of docs/03: milestone review (revisão de marco), milestone (marco), queue line (linha da fila), dependency (dependência, `· after all`). "Cancelled" / "cancelada" and "re-decide" / "redecidir" are the chapters' words, not docs/03 rows (m36-review small 10); no new term; docs/03 unchanged. Sources: docs/05 §4 :198 to :202 (a cancelled line, the line whose `after` names it re-decided, `after all` leaving it out), docs/06 :512 (`m20-review` dropped), the kit's `CHANGELOG.md` `## 2026.10.27.1` for :224, unchanged. No number added. No source note added. Cases: none.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable: no screen, and no new kind of content (prose).

**Out of scope.**

* m36-review's small 6 (R3-2, chapter 14 en :224 / pt :226 never says not to replace `after all` with a list): not met. The new :223 names the list as the review's second way out, which leaves R3-2 no worse, but saying not to write it would be a sentence and a claim no item asks for, a widening.
* m36-review's small 5 (R2-2, "the review waits with it" in chapter 15 :18 when the re-decide line is already `[>]` for the review's `/propose`): not picked; M2 keeps the claim as it was, no worse.
* m36-review's small findings 3, 4 and 7 to 11: not picked by the author's word.
* Chapter 14 en :228 / pt :230, "until the person re-decides it" / "até a pessoa redecidi-la": not in the review's findings; a note below.
* No further line: a fix page opens none (docs/05 §8).

**Overlap with the pages waiting in `work/`.** For their /apply, and for whoever orders the builds:

* `ch14-queue-findings` (`[>]`) edits `book/{en,pt}/14-queue-states.md` at :4, :137, :177, :271, :278 and :279 and inserts a section before :198 / :200; none of those is a sentence this page changes, but if it lands first M1's lines move down by that section's length, so M1 is found by its quoted sentences. Same files: by docs/05 §4 :146 to :149 the two builds do not run at once.
* `ch15-review-grades` (`[>]`) edits `book/{en,pt}/15-closing-a-milestone.md` at :3, :21 and :111 and inserts sections after :112; :18 is not among them and does not move. Same files: the two builds do not run at once.
* `ch14-open-lines-search` (draft) has no section chosen yet; it quotes none of these sentences.
* `ch13-apply-next` (`[>]`) edits chapter 13 only: no overlap.

**Done when.**

* [x] M1 and M2 read as the Contract says in both editions.
* [x] A sweep of `book/` in both editions finds no "neither dropped nor rewritten" nor "não é cancelada nem reescrita", no "no such way out" nor "não teria essa saída", no "nothing the person could write" nor "nada que a pessoa escrevesse" (at `066b3bf` all only in chapter 14), and no "re-decide it" or "redecidi-la" in chapter 15; chapter 14 en :228 / pt :230 keep theirs (the note below).
* [x] Both editions written; no filler and nothing useful cut; no number added; no em dash; no run narration; no pointer added.
* [x] `make verify` green after the last edit, with its time; the disclosure scan green.
* [x] `make book` builds both editions, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent, the author corrects it in the review: M1's reason says what the person's ways out cost a review instead of denying them, since both happened (docs/06 :512 dropped a review; chapter 14 :224 rewrote one as a list), with no "only", and :222's short form changes with it, "no good way out", so no line of the paragraph still says a review has none.
* Decided by the agent, the author corrects it in the review: :224 loses the changelog's clause "nothing the person could write freed it", which beside the new :223 would contradict the list the person wrote; it is inside M1's finding ("against the next sentence"), so no widening, and the sentence keeps every fact of the changelog's entry.
* Decided by the agent, the author corrects it in the review: dropping a review is said to lose "the test of the milestone's paragraph", the review's first job in chapter 15, rather than its code reading, which another review may have done (as `m20-review`'s reason says).
* Decided by the agent, the author corrects it in the review: M2 keeps "waits" for the line and names the re-decided line, "the line that waits" / "a linha que espera", rather than taking chapter 14 :220's "is the person's to re-decide", which would drop the line's own wait and leave "with it" / "com ela" with three feminine candidates in Portuguese.
* Decided by the agent, the author corrects it in the review: R3-2 is not met (Out of scope); the brief allowed it only without widening, and meeting it needs a sentence.
* Decided by the agent, the author corrects it in the review: chapter 14 :228 / :230's "re-decides it" / "redecidi-la", met while defining, is a note and not a third item: the review did not find it, the author's pick names two, and the fixes line is their list.
* From the documents: the two items and that they are one page (`work/done/m36-review.md`, the author's word; docs/05 §8); a review droppable and a cancelled line re-decided (docs/05 §4 :198 to :202); docs/03 unchanged.

## Outcome

Built before the author read it, on the author's word relayed for this run ("Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão"); every decision below was taken by the agent alone, the author corrects it in the review. The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

What changed, both editions, sentence for sentence:

* M1, chapter 14 (en :222 to :224, pt :224 to :226): "A milestone's review would have no good way out." / "A revisão de um marco não teria uma boa saída."; :223 / :225 keeps its first clause word for word and ends "and of the person's ways out, dropping the review loses the test of the milestone's paragraph, and rewriting it on what exists turns its `after all` into a list of every other line above it." / "e das saídas da pessoa, cancelar a revisão perde o teste do parágrafo do marco, e reescrevê-la sobre o que existe troca o `after all` dela por uma lista de todas as outras linhas acima dela."; :224 / :226 ends "`after <slug>, dropped: re-decide`, and the review's `after all` was replaced by a list of the other 27 slugs." / "e o `after all` da revisão foi trocado por uma lista dos outros 27 slugs.", the clause "nothing the person could write freed it" removed. :225 to :229 / :227 to :231 unchanged.
* M2, chapter 15 :18, last clause: "and a line whose `after` names a cancelled one waits, and the review with it, until the person re-decides that line." / "e uma linha cujo `after` nomeia uma cancelada espera, e a revisão com ela, até a pessoa redecidir essa linha."

Divergences from the Contract's proposals, within what each item says (the Contract let /apply word them otherwise):

* Ch14 :224 / :226: the proposal "and only replacing the review's `after all` with a list of the other 27 slugs freed it" became "and the review's `after all` was replaced by a list of the other 27 slugs", the changelog's own clause (`## 2026.10.27.1`). The delivery review found "only" right after a sentence naming two ways out made a reader ask whether dropping would not have freed it too, and the changelog says only that the list replaced it; no fact of the entry is lost but the removed clause.
* Ch15 :18: the proposal "the line that waits" / "a linha que espera" became "that line" / "essa linha". The delivery review found "the line that waits" could strictly be the review, which the same clause says also waits; "that line" takes the clause's subject, the line whose `after` names a cancelled one, and in Portuguese no feminine pronoun is left to read as `a cancelada`.

Proof: the sweep of `book/` finds none of the six removed phrases, and chapter 15 has no "re-decid" or "redecid" but "re-decides that line" / "redecidir essa linha"; chapter 14 en :228 / pt :230 keep theirs (note below). `make verify` green after the last edit, 11 seconds (re-run after this page moved; time in the last line of this section). `make book` built both editions: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

Delivery review: one read-only agent on Opus read the diff of the four chapter files, the paragraphs around each change, this page and docs/04. It found M1 and M2 holding in both editions, every Portuguese pronoun resolved ("reescrevê-la", "dela", "com ela"), no em dash, no run narrated, and "the test of the milestone's paragraph" understood from chapter 14 alone (its queue examples, en :46 and :147, gloss `m1-review` as "the milestone against its paragraph"). Three small candidates in what this delivery changed:

* "only" at ch14 :224 / :226: fixed, above.
* "the line that waits" at ch15 :18: fixed, above.
* Ch14 :223 / :225 gives rewriting as a list as a cost without saying why a list is worse (a line added later is missed, chapter 11 :74): not fixed, decided by the agent: the reviewer judged most readers infer it, and saying it would be a sentence no item asks for.

It confirmed the older flaw of the note below, at ch14 pt :230 / en :228, now more visible since chapter 15 :18 fixed its twin; it stays a note, as the page decided.

Verify after the page moved to `work/done/`: green, 12 seconds; `make book` rebuilt both PDFs from the final text.

## For the review

* `book/pt/14-queue-states.md:230`, "e a revisão espera com ela até a pessoa redecidi-la" (en :228, "until the person re-decides it"): the same ambiguity as m36-review's M2, "-la" readable as `a revisão`, the nearer feminine noun; a person reading Portuguese may think the review is what gets re-decided, the more so once M1 removes :223 / :225's "a review is neither dropped nor rewritten", which told the reader a review is not re-decided. Found by `m36-fixes`' /propose, left as it is.

```commit
docs(m36-fixes): fix M36's two medium findings in chapters 14 and 15

- ch14: a review's two ways out are given with their cost, not denied
- ch14: 2026-10-26 story keeps the 27-slug list, drops the denial
- ch15: the person re-decides the waiting line, never the cancelled one
- both editions, sentence for sentence; verify green

work/done/m36-fixes.md
```
