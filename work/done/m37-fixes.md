# m37-fixes

Defined before the author read it: the author's word for this run, relayed by the session that runs the queue on the author's behalf on 2026-11-13, is "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão" (close every open line of docs/06 without supervision), and for the reviews "Todas, médios entram" (every medium finding enters the one fixes line). So each question the documents leave open is answered by the agent's recommendation, marked "decided by the agent, the author corrects it in the review" (docs/05 §4, a command that says to decide alone).

**Objective.** After chapter 10 a newcomer following the quick guide expects, at the end of `/apply`, the queue tree with its `next:` drawn after the next steps though nobody asked; and after chapter 14 the reader knows the person re-decides `reprint-card`, the waiting line, never the review.

**Behaviour.** What the reader can do or explain afterwards, one item per medium finding of `work/done/m37-review.md`:

* M2 (the review's numbering, chapter 10). From the quick guide's step 6 alone, say what `/apply` shows at its end: verify green, the page in `work/done/`, its line `[x]`, the delivery staged, the message in a `commit` block, the next steps, starting with using what the delivery changed; and after them, drawn though nobody asked, the queue tree, what may run next, with its `next:`, the first free line's command written as the host invokes it.
* M2, failure: asked "step 6 is done and the session showed a tree I did not ask for; is something wrong?", the reader of chapter 10 answers no, `/apply` draws it unasked; and asked "is the tree one of the next steps I must do?", answers no, it comes after them and tells what may run next.
* M2, edge: step 7's "the environment `/apply`'s last sentence names" stays true: the guide does not say the tree is the last thing `/apply` shows, since the environments are (chapter 13).
* M1 (chapter 14). From chapter 14's cancelled-line passage alone, say that the person re-decides `reprint-card`, the line whose `after` names the cancelled `print-card`, and that the review waits with it until then.
* M1, failure: asked "what does the person re-decide, the review or `reprint-card`?", with :228 and :229 read back to back, the reader answers `reprint-card`, never the review; in the Portuguese edition no feminine pronoun of :230 can be read as `a revisão` or `a árvore da fila`.
* M1, edge: the reader still says that a cancelled line never keeps the review waiting, and that dropped too, `reprint-card` leaves the review's `after all`, rewritten, the review waits for it (en :227 and :229 / pt :229 and :231 unchanged).
* In the Portuguese edition, the same, with docs/03's terms (árvore da fila, revisão de marco, linha da fila) and chapter 13's words for `/apply`'s ending ("próximos passos", "mesmo sem ninguém pedir"), `next:` kept as the script prints it.

**Contract.** Four chapter files, line numbers en / pt at `0e22d1a`, where m37-review read them, the same at HEAD `3616af6` (`git diff 0e22d1a HEAD -- book/` is empty). Each change quotes the sentence it replaces so a drift is found; pt follows en sentence for sentence. The text below is the agent's proposal; /apply may word it otherwise within what each item says.

* **M2, ch10** (`book/{en,pt}/10-quick-guide.md`) :67 / :67, step 6's "You see" line, one clause added after the next steps and nothing else changed:
  * Replaced: "and your next steps, starting with using what the delivery changed; when the delivery is the first after which a person can run the product" / "e os seus próximos passos, começando por usar o que a entrega mudou; quando a entrega é a primeira depois da qual uma pessoa consegue rodar o produto".
  * Proposed: "and your next steps, starting with using what the delivery changed; after them, though you did not ask, the queue tree, what may run next, with its `next:`, the first free line's command written as your host invokes it; when the delivery is the first after which a person can run the product" / "e os seus próximos passos, começando por usar o que a entrega mudou; depois deles, mesmo sem ninguém pedir, a árvore da fila, o que pode rodar em seguida, com o `next:` dela, o comando da primeira linha livre escrito como o seu host o invoca; quando a entrega é a primeira depois da qual uma pessoa consegue rodar o produto".
  * The semicolon ends the steps' series, so the tree attaches to "You see" / "Você vê" and cannot be read as a second step after "starting with" / "começando por". "What may run next" / "o que pode rodar em seguida" is chapter 13 :129's gloss of the tree, so a newcomer who has met the term only in chapter 8 :159 / :160 and chapter 12 :25 still knows what it shows.
  * The order is the installed `.agents/skills/apply/SKILL.md` :79 to :86's: the next steps told, "Then run the queue script of docs/05 §4, though no one asked, and show its tree as §4 says, its `next:` command written for this host", then the environments, "End saying which environment is at which version". The clause names the tree after the steps, not as one of them, and not as last, so step 7 :69's "`/apply`'s last sentence" stays true. "The first free line's command" is chapter 13 :129's own gloss of `next:`, true whether the script draws one milestone or every open one.
  * No pointer added: :68 already points to chapter 13, "What `/apply` does", which owns the why (:129). Key point :126's list of the steps is unchanged: it lists what the reader does, and the tree is something the reader sees.
* **M1, ch14** (`book/{en,pt}/14-queue-states.md`) :228 / :230, the last clause, the re-decided line named instead of a pronoun:
  * Replaced: "and the review waits with it until the person re-decides it." / "e a revisão espera com ela até a pessoa redecidi-la."
  * Proposed: "and the review waits with it until the person re-decides `reprint-card`." / "e a revisão espera com ela até a pessoa redecidir `reimprimir-cartao`."
  * Every pronoun against every noun of the sentence, both editions: "it" / "ela" in "waits with it" / "espera com ela" is the thing that waits, `reprint-card`, the sentence's subject; the review does not wait with itself, the queue tree (pt "a árvore da fila", feminine) prints and does not wait, and "the person" / "a pessoa" comes after it. The re-decided line is now the slug, so no pronoun is left to attach to the review, and :229's "it" / "ela" has `reprint-card` / `reimprimir-cartao` as its nearest noun.
  * :220 / :222 ("is the person's to re-decide") and the script's output `dropped: re-decide` at :224 / :226 and :228 / :230 stay; :229 / :231 stays (Out of scope).

Terms of docs/03: queue tree (árvore da fila), milestone review (revisão de marco), queue line (linha da fila), dependency (dependência). "Cancelled" / "cancelada" and "re-decide" / "redecidir" are the chapters' words; no new term; docs/03 unchanged (its `queue tree` row, :123 at HEAD, already says "/apply ends with it, as apply's says"). Sources: the installed `apply/SKILL.md` :79 to :86 for the order of M2; chapter 13 en / pt :128 to :129 for its words; docs/05 §4 for a cancelled line re-decided. No number added. No source note added. Cases: none.

**States.** Inapplicable: chapters, no screen.

**Visual reference.** Inapplicable: no screen, and no new kind of content (prose).

**Out of scope.**

* m37-review's small 7 (R2-2, ch14 en :229 / pt :231, "rewritten on what exists" / "reescrita" readable as the review): not picked by the author's word. M1 lessens it, since :229's "it" / "ela" now has the slug as its nearest noun, but the fronted participle before "the review" / "a revisão" stays; meeting it needs a rewording no item asks for.
* m37-review's small findings 3 to 6 and 8 to 16: not picked by the author's word.
* What `/apply`'s last message opens with (`🚨`, `⚠️`, `✅`) and what it does with a flaw it built: `ch13-apply-findings` (M38), chapter 13; step 6 does not name the marks.
* The tree drawing every open milestone: `ch14-queue-every-milestone` (M39); M2's wording does not depend on it.
* No further line: a fix page opens none (docs/05 §8).

**Overlap with the pages waiting in `work/`.** For their /apply, and for whoever orders the builds:

* `ch14-queue-findings` (`[>]`) edits `book/{en,pt}/14-queue-states.md` at :4, :137 to :138, :177, :271, :278 and :279 and inserts a section between :196 and :198 / :198 and :200 (its numbers at `46d5166`); none of those is the sentence M1 changes, and M1 is an in-place edit of one clause, so none of its line numbers move if this page lands first. If `ch14-queue-findings` lands first, M1's line moves down by its section's length and is found by the quoted sentence. Same files: by docs/05 §4 the two builds do not run at once.
* `ch14-open-lines-search` (draft) has no section chosen yet; `ch14-after-never-waits` and `ch14-queue-every-milestone` (M39, `[ ]`) have no page; none quotes M1's sentence.
* `ch13-apply-findings` (`[~]`) edits chapter 13 and `ch15-review-grades` (`[*]`) chapter 15 and docs/03: no overlap. No open line touches chapter 10.

**Done when.**

* [x] M1 and M2 read as the Contract says in both editions.
* [x] A sweep of `book/` in both editions finds no "re-decides it" nor "redecidi-la" (at `0e22d1a` only ch14 en :228 / pt :230), and chapter 10's step 6 names the queue tree and `next:` / "árvore da fila" and `next:`; chapter 14's other "re-decide" / "redecidir" and the script's `dropped: re-decide` stay.
* [x] Both editions written; no filler and nothing useful cut; no number added; no em dash; no run narration; no pointer added.
* [x] `make verify` green after the last edit, with its time; the disclosure scan green.
* [x] `make book` builds both editions, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent, the author corrects it in the review: M2 adds one clause to step 6's "You see" line and no step, since the tree is something the reader sees at `/apply`'s end, not something the reader does; the why stays in chapter 13, which step 6 already points to.
* Decided by the agent, the author corrects it in the review: M2 places the tree after the next steps and does not call it the last thing shown, as the installed `apply/SKILL.md` orders them, so step 7's "`/apply`'s last sentence" (the environments) stays true.
* Decided by the agent, the author corrects it in the review: M2 ends the steps' series with a semicolon before the tree, so the tree is not read as a step, and glosses the tree as "what may run next", chapter 13's words, for a newcomer who has met the term only in passing.
* Decided by the agent, the author corrects it in the review: M2 glosses `next:` as "the first free line's command", chapter 13 :129's words, so the guide stays true once `ch14-queue-every-milestone` teaches the tree across every open milestone.
* Decided by the agent, the author corrects it in the review: M1 names the slug, `reprint-card` / `reimprimir-cartao`, rather than chapter 15's "that line" / "essa linha", since here the clause's subject is already the slug and a demonstrative could still be read as the review; "com ela" stays, its only waiting antecedent being the line.
* Decided by the agent, the author corrects it in the review: small 7 (:229 / :231) is not met (Out of scope), lessened by M1; the review allowed meeting it in passing, but its participle needs a rewording that is a third change no pick names.
* From the documents: the two items and that they are one page (`work/done/m37-review.md`, the author's word; docs/05 §8); the order of `/apply`'s ending (installed `apply/SKILL.md` :79 to :86); docs/03 unchanged.

## Outcome

Built before the author read it, on the author's word relayed for this run ("Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão"). The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

* M2, chapter 10 :67 both editions: step 6's "You see" line gains, after the next steps and a semicolon, "after them, though no one asked, the queue tree, what may run next, with its `next:`, the first free line's command written as your host invokes it" / "depois deles, mesmo sem ninguém pedir, a árvore da fila, o que pode rodar em seguida, com o `next:` dela, o comando da primeira linha livre escrito como o seu host o invoca". Nothing else in the step changed; step 7 :69 is untouched.
* M1, chapter 14 en :228 / pt :230: "until the person re-decides it." / "até a pessoa redecidi-la." became "until the person re-decides `reprint-card`." / "até a pessoa redecidir `reimprimir-cartao`."; :227 / :229 and :229 / :231 unchanged.
* Divergence from the Contract: en "though you did not ask" (the page's proposal) became "though no one asked", chapter 13 en :129's own words, so it matches the Portuguese "mesmo sem ninguém pedir" and chapter 13 in both editions; the delivery review noted the mismatch, fixed in this delivery. Decided by the agent, the author corrects it in the review.
* Sweep: no "re-decides it" nor "redecidi-la" left in `book/`; chapter 10's step 6 names the queue tree / árvore da fila and `next:`; chapter 14's other "re-decide" / "redecidir" and `dropped: re-decide` stay.
* Verify: `make verify` green, 12 seconds after the last edit (11 the first run); the disclosure scan green.
* Proof: `make book` built both editions after the last edit: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`. No new kind of content, so no screenshot.
* Delivery review (one read-only Opus agent, docs/05 §5, over the four chapter files and this line's docs/06 hunk): nothing to fix; every Behaviour item holds in both editions, the pt "com ela" can only mean `reimprimir-cartao`, "o `next:` dela" the árvore da fila. One note, the en/pt wording of "unasked", fixed as above, verify and the book run again.
* Out of scope kept: small 7 (en :229 / pt :231) not met; no further line opened.
* Cases: none; no number, no source note, no pointer added; docs/03 unchanged.

```commit
docs(m37-fixes): fix M37's two medium findings in chapters 10 and 14

- ch10 step 6: /apply shows the queue tree and its next: after the steps
- ch14: the person re-decides reprint-card, named, never the review
- both editions; verify green, both PDFs built

work/done/m37-fixes.md
```
