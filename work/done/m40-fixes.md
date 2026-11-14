# m40-fixes

Defined before the author read it: the author's word for this run, relayed by the driver session on 2026-11-14, is "Vamos rodá-la de ponta a ponta automaticamente, sem pausas para concluir o milestone" (run M40 end to end without pauses), and for the review's medium findings "Corrigir em m40-fixes" (fix them in m40-fixes). So each question the documents leave open is answered by the agent's recommendation, marked "decided by the agent", for the author to correct in the review (docs/05 §4, a command that says to decide alone). The page is built before the author read it.

**Objective.** After this delivery a reader of chapters 11, 13 and 15 never meets a line held by `after` told as waiting, in the sentences focus-kit 2026.11.14 reworded, beside the rule that such a line is not waiting; and a reader of chapter 12 on trunk reads a true reason why `/propose` reads pages on their own branch.

**Behaviour.** What the reader can do or explain afterwards, one group per medium finding of `work/done/m40-review.md` (its numbering, M1 and M2):

* M1. In chapters 11, 13 and 15, both editions, no sentence makes a line held by `after` the subject of waiting ("waits on", "waits for", "waits until", "makes it wait", "waiting for", "espera", "a faz esperar", "esperando"): such a line comes after another, needs it, or is not free yet, as docs/05 §4 :143 and :204, §8 :523 and `apply/SKILL.md` :38 now say.
* M1: from chapter 11 alone the reader says that the queue script draws each line under the last line it comes after, and that a milestone's review comes after the lines above it.
* M1: from chapter 13 alone the reader says that `/apply` on a `[>]` line whose `after` is not integrated names the line it needs, and that any stop writes on the page what was built and what the line needs.
* M1: from chapter 15 alone the reader says that the finding lines sit under the review line and go through `/propose`.
* M1, sibling (decided by the agent): chapter 11 :58 says `lend-book`, `[>]`, is ready for `/apply`, as chapter 14 says of `search-catalog`, not that it waits for it; "wait" is the word of a `[?]` line (docs/05 §4 :184).
* M1, kept: "wait" stays for a `[?]` line and its reason, for a command, a build, a commit, a session or a person that waits (`m39-fixes`' kept list), inside the script's output blocks (`waits:`, the tree's word, chapter 13 :213), and in chapter 15 :183 ("As a line it waits its turn"), which m40-review left as weak.
* M2. From chapter 12 :27 alone, a reader on trunk reads that `/propose` reads the page of each delivery in flight in `work/` or on its own branch, since with a branch or a worktree per delivery the main branch's `work/` lacks every page not yet merged: the condition the kit's changelog gives for 2026.11.14 is back, so the reason is true on every Git strategy.
* In the Portuguese edition, the same, with docs/03's terms and the wording chapters 11, 12 and 14 already use ("vem depois de", "precisa de", "livre").

**Contract.** Line numbers en / pt at HEAD `64b67ba`. Each change quotes what it replaces, so a drift is found by the sentence; one sentence per line, no line added or removed; pt follows en. The wording is the agent's (decided by the agent).

* `book/{en,pt}/11-queue-and-milestones.md` en :58 / pt :61.
  * Replaced: "`lend-book` is completely defined and waits for `/apply`" / "`emprestar-livro` está completamente definida e espera o `/apply`".
  * Proposed: "`lend-book` is completely defined and ready for `/apply`" / "`emprestar-livro` está completamente definida e pronta para o `/apply`".
* Same file, en :90 / pt :93.
  * Replaced: "each line under the last line it waits on" / "cada linha sob a última linha que ela espera".
  * Proposed: "each line under the last line it comes after" / "cada linha sob a última linha depois da qual ela vem".
* Same file, en :95 / pt :98.
  * Replaced: "which waits for the lines above it" / "que espera as linhas acima dela".
  * Proposed: "which comes after the lines above it" / "que vem depois das linhas acima dela".
* Same file, en :181 / pt :186.
  * Replaced: "goes above the delivery's line and makes it wait (chapter 14)" / "fica acima da linha da entrega e a faz esperar (capítulo 14)".
  * Proposed: "goes above the delivery's line, which takes it as its `after` (chapter 14)" / "fica acima da linha da entrega, que a recebe no seu `after` (capítulo 14)".
  * Kept: en :89 / pt :92, "`/apply return-book` waits until `lend-book` is integrated", a command that waits.
* `book/{en,pt}/13-apply.md` en :50 / pt :50.
  * Replaced: "it does not start either, says what it waits on, and leaves" / "ele também não começa, diz o que espera, e deixa".
  * Proposed: "it does not start either, names the line it needs, and leaves" / "ele também não começa, nomeia a linha de que ela precisa, e deixa".
* Same file, en :80 / pt :80.
  * Replaced: "what was built and what it waits on" / "o que foi construído e o que ela espera".
  * Proposed: "what was built and what it needs" / "o que foi construído e aquilo de que ela precisa", `apply/SKILL.md` :38's words; it covers both stops, a `[?]` one and one that adds an `after`.
* Same file, en :223 / pt :223.
  * Replaced: "`m1-review`, written `· after all`, waits until `return-book` is defined." / "`m1-review`, escrita `· after all`, espera até `devolver-livro` estar definida."
  * Proposed: "`m1-review`, written `· after all`, is not free until `return-book` is defined." / "`m1-review`, escrita `· after all`, só fica livre quando `devolver-livro` estiver definida." The tree block above (:213, `waits:`) is the script's output and stays.
* `book/{en,pt}/15-closing-a-milestone.md` en :165 / pt :169.
  * Replaced: "go in the same milestone, under the review line, waiting for `/propose`." / "vão para o mesmo marco, sob a linha da revisão, esperando o `/propose`."
  * Proposed: "sit in the same milestone, under the review line, and go through `/propose`." / "ficam no mesmo marco, sob a linha da revisão, e passam pelo `/propose`." (docs/05 §8 :523).
* `book/{en,pt}/12-propose.md` en :27 / pt :27.
  * Replaced: "since the main branch's `work/` lacks every page not yet merged" / "já que o `work/` do branch principal não tem nenhuma página ainda sem merge".
  * Proposed: "since with a branch or a worktree per delivery the main branch's `work/` lacks every page not yet merged" / "já que, com um branch ou um worktree por entrega, o `work/` do branch principal não tem nenhuma página ainda sem merge".
  * Checked, no change: chapter 19 :360, the sibling sentence `ch12-pages-on-branches` changed, gives no reason.
* Sweep: `grep -n -E "wait|esper|aguard"` over `book/en` and `book/pt` at HEAD found no other sentence telling a line held by `after` as waiting in the wording 2026.11.14 displaced; chapter 7 :63 / :64 ("the definition waits for that line's page, the build for its code") is a command's phase that waits, kept as `m39-fixes` kept it; chapter 14 :342 / :344 ("a Milestone 1 review waited on a line the person had dropped") is a dated error told as it happened, kept by the same list.
* No Case A or Case B passage is touched; no number, source, document, ADR or docs/03 row changes.

**Out of scope.**

* m40-review's small findings: listed there, none picked (docs/05 §8).
* Chapter 15 :183 "waits its turn": m40-review marked it weak.
* The kit's own wording (`queue.sh`'s `waits:`, `references/documents.md`): the kit's, for `work/kit-proposals.md`.
* `make book`: the driver session builds the PDFs once for the run.

**Done when.**

* [x] Every change of Contract made in both editions, one sentence per line.
* [x] The M1 sweep finds no sentence of chapters 11, 13 and 15 telling a line held by `after` as waiting.
* [x] Chapter 12 :27 carries the condition, in both editions.
* [x] No em dash; verify green.
* [x] The Delivery review read the delivery, and what it found is fixed or recorded.

## Outcome

Built by /apply on 2026-11-14 on trunk, on the same word of the author relayed by the driver session: every decision is the agent's, taken alone (docs/05 §4), and the page was built before the author read it. The driver session stages, commits and runs `make book` once for the run.

**What changed.** The nine sentences of Contract, both editions, one line each: chapter 11 :58, :90, :95, :181 (pt :61, :93, :98, :186), chapter 13 :50, :80, :223, chapter 15 :165 (pt :169), chapter 12 :27. No line added or removed; no document, ADR or docs/03 row changes.

**Divergence from Contract, from the Delivery review.** Decided by the agent:

* Chapter 13 :50 says "names that line" / "nomeia essa linha" instead of "names the line it needs" / "nomeia a linha de que ela precisa": in pt "ela" could read as the line not yet integrated; "names that line" is chapter 12 :28's wording.
* Chapter 13 :80 says "what the line needs" / "aquilo de que a linha precisa" instead of "what it needs" / "aquilo de que ela precisa": "it" / "ela" could read as the stop.

**Delivery review.** One read-only agent on Opus read the page, `git diff HEAD` of the eight chapters and this line's hunk of docs/06, against docs/04, docs/05 §§4 and 8, `apply/SKILL.md` and the kit's changelog. Must-fix: none. Optional: the two pt ambiguities above, fixed; chapter 14 :342 / :344's dated "waited on", added to the Sweep as kept.

**Proof.** `make verify` green after the last chapter edit, 13 seconds, under the five-minute ceiling. No slow tests exist (docs/05 §5). No PDF built here: `make book` is the driver's.

```commit
docs(m40-fixes): after is never a wait in 11, 13, 15; ch12 condition

- chapters 11, 13, 15: a line held by after is no longer told as waiting
- chapter 12: the branch reason keeps its branch-or-worktree condition
work/done/m40-fixes.md
```
