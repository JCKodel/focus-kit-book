# ch14-renewal-example

**Objective.** After chapter 14 the reader, developer or not, can say why `/apply renewal-notice` does not build the line in the chapter's example: first because the line is `[ ]` and `/apply` builds only a `[>]` line, and that `after` would hold it even were it `[>]`; and the Portuguese reader reads a block row that, like the English, names the member the notice warns.

**Behaviour.** What the reader can do or explain after the chapter:

* Read the example's state (`search-catalog` `[x]`, `lend-book` `[*]`, `renew-loan` `[>]`, `renewal-notice` `[ ]`) and say what each command does: `/propose renewal-notice` says it waits on `renew-loan`, leaves the mark as it is, and stops; `/apply renewal-notice` refuses, for its mark first: the line is `[ ]`, not `[>]`, so it refuses to build and points to `/propose`, as chapter 13 says of a `[ ]` or `[~]` line.
* Say that `after` holds `/apply` too: were the line `[>]`, `after` would still hold it until `renew-loan` is `[x]`, whatever the token says (the rule, :92 / :93, unchanged).
* Failure: asked "is `after` why `/apply renewal-notice` stops now?", answer that it is not the first reason: the line has no finished page, so `/apply` points to `/propose`; `after` is the reason `/propose` stops.
* Edge: "The token lets both commands start, and neither does" stays true: neither starts, each for the reason the sentence now gives.
* Edge: "`renewal-notice` is free the moment `renew-loan` is `[x]`" stays true: free is docs/03's `free line`, a line whose `after` lines are all `[x]`, not a line `/apply` may build.
* In the Portuguese edition, read the block row `avisa membro do prazo`, the member and the due date both named, as the English row "warns a member of the due date" names them.

**Contract.** Two files: `book/en/14-queue-states.md` and `book/pt/14-queue-states.md`. Line numbers are at HEAD `ea83160` (chapter 14 last changed in `66344a9`), en / pt. Each change replaces only the quoted words; the rest of each line stays. Each quoted text is found once in its file (`grep -nF`).

* **C1, "The next line, and which run together", the example's reasoning** (:117 / :118):
  * en: ", and `/apply` would do the same." becomes "; `/apply renewal-notice` refuses too, but for its mark first: the line is `[ ]`, not `[>]`, so it refuses to build and points to `/propose` ([chapter 13](13-apply.md)), and were it `[>]`, `after` would still hold it until `renew-loan` is `[x]`."
  * pt: ", e o `/apply` faria o mesmo." becomes "; o `/apply aviso-renovacao` também se recusa, mas primeiro pela marca: a linha está `[ ]`, não `[>]`, então ele se recusa a construir e aponta para o `/propose` ([capítulo 13](13-apply.md)), e se ela estivesse `[>]`, o `after` ainda o seguraria até `renovar-emprestimo` estar `[x]`."
* **C2, same section, the Portuguese block row** (pt :114 only): "avisa o vencimento" becomes "avisa membro do prazo". The row is then 74 columns: `[ ] aviso-renovacao (-A)  ` (26) + `avisa membro do prazo` (21) + ` · after renovar-emprestimo` (27). The English row (:113) stays, 74 columns.

Terms of docs/03 used: `parallel token`, `dependency`, `free line`; none new. Sources: none new; the refusal is docs/05 §2's ("start building only a completely defined `[>]` page") as chapter 13 :40 / :40 teaches it. Cases: none; the example is the lending library's, written for the chapter, as it says.

Sibling sentences checked: chapter 14 :32 ("`/apply` builds it once every line its `after` names is `[x]` and its token lets it") and :106 already say `/apply` needs the page `[>]`; the closing sentence :118 / :119 and the key point :218 / :219 stay true. No other chapter retells this example. `work/done/ch14-after-over-token.md` quotes the old sentence as its Contract; that record says what was built then and is `m29-records-claims`' file, not this line's.

Neighbours: `ch08-other-items-claude-md` touches chapter 8 and `m29-records-claims` touches `work/done/` and docs/03; neither touches chapter 14, so no file is shared.

**States.** Inapplicable: a chapter, no screen.

**Visual reference.** Inapplicable: no figure; the two PDFs of `make book` are the review copy.

**Out of scope.**

* The rule (:92 / :93) and the free-line key point (:218 / :219): correct as written.
* The English block row: it names the member and the due date and keeps to 74 columns.
* The slug `aviso-renovacao`: it appears in the prose, and shortening it is not the finding.
* `work/done/ch14-after-over-token.md` and `work/done/m29-review.md`: records, `m29-records-claims`' and the review's own.

**Done when.**

* [x] C1 and C2 read as the Contract says, each quoted text found once before its edit; the rest of both files unchanged.
* [x] Both editions written, the same reasoning in each, Portuguese names in the Portuguese edition.
* [x] The chapter still opens with its value; no filler and nothing useful cut; no number added; no private case used.
* [x] No em dash in the changed text; no run narration and no commit hash in the chapter.
* [x] The Portuguese block row is 74 columns or fewer (`scripts/check_width.py`).
* [x] `make verify` green after the last edit.
* [x] `make book` builds both editions after the last verify, both PDF paths recorded.

**Decisions from the documents.**

* `/apply` refuses a `[ ]` line and points to `/propose`: docs/05 §2 ("start building only a completely defined `[>]` page") and chapter 13 :40 / :40, whose words C1 echoes ("refuses to build and points to `/propose`" / "se recusa a construir e aponta para o `/propose`").
* `after` holds both commands until the named lines are `[x]`, whatever the token says: docs/05 §4, chapter 14 :92 / :93.
* "Free" in the closing sentence is docs/03's `free line`, so it stays.
* Block width 74 columns: docs/04, "Width of a block".
* Token `(PA)`: the lines above in flight, `ch08-other-items-claude-md` and `m29-records-claims`, are on chapter 8 and on `work/done/` and docs/03; this definition takes nothing from their pages and the build touches only chapter 14's two files; `after` names `m29-review`, `[x]`.

**Decisions taken alone.** The agent chose each of these (the batch's driver asked for recommended answers; correct them in the review).

* The second reason is a counterfactual, "were it `[>]`, `after` would still hold it", not "after holding it once it is", as the queue line words it: in this example `/propose renewal-notice` waits until `renew-loan` is `[x]`, so the line cannot become `[>]` while `renew-loan` is not `[x]`, and `after` would never hold a `[>]` `renewal-notice`. The queue line's sentence becomes "chapter 14's renewal-notice example says /apply refuses the line first because it is `[ ]` and not `[>]`, and that `after` would hold it even were it `[>]`, and the Portuguese block row names the member it warns, within 74 columns; both editions · after m29-review".
* The Portuguese row is "avisa membro do prazo", without the article, rather than "avisa um membro": with the slug, token and `after` fixed, 21 columns are left for the sentence; "avisa um membro do prazo" needs 24 and "avisa o membro do prazo" 23, and "avisa um membro" (15) would drop the due date the English row names, the same kind of loss the review found. A dropped article is style; a dropped noun is meaning.
* "vencimento" becomes "prazo" for width; both render "due date" here.
* C1 links chapter 13, as the section links chapters 9, 12 and 19, since the refusal of a `[ ]` line is taught there.

**Divergences.** One, from the delivery review: C1's opening words "`/apply renewal-notice` refuses too" / "o `/apply aviso-renovacao` também se recusa" became "`/apply renewal-notice` does not start either" / "o `/apply aviso-renovacao` também não começa". "Too" said `/propose` had refused, and it had not: it waits on `renew-loan`, which chapter 13 keeps apart from a refusal (:40 refuses and points to `/propose`; :43 waits and says what it waits on). The rest of C1 and all of C2 are as the Contract words them.

**Decisions taken by /apply.** The review's finding was fixed here rather than queued: it is in the text this delivery wrote, and the fix keeps the sentence's two reasons and its "neither does" opening true. Correct it in the review if the Contract's words were wanted.

**Proof.**

* Before the edits, `grep -nF` found each quoted text once: en :117, pt :118 for C1, pt :114 for C2. After the build, `git diff --stat HEAD` of the two chapter files shows 3 insertions and 3 deletions, en :117 and pt :114, :118, and nothing else.
* Sibling sentences re-read: en :32 ("`/apply` builds it once every line its `after` names is `[x]` and its token lets it") and :106 still hold; the closing sentence en :118 / pt :119 ("free the moment `renew-loan` is `[x]`") stays docs/03's `free line`.
* Block rows measured: en :113 and pt :114 are 74 columns each; `python3 scripts/check_width.py` exit 0.
* `make verify` exit 0 after the last edit to the chapters and again after these records, every check passed, the external link included.
* `make book` exit 0 after the last verify, on HEAD `a4f2cb9` with this delivery's changes and other lanes' uncommitted edits in the tree: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review.** One read-only Opus agent, launched by this /apply over this delivery's paths only (`git diff HEAD` of both chapter 14 files, before the review's fix and these records), against this page and docs/04's width rule; it read chapter 14 :88-122 and chapter 13 :36-44 in both editions, and said it did not call any advisor tool. Its reply, one finding: "`/apply renewal-notice` refuses too" (pt "também se recusa") says `/propose` refused, though it waits on `renew-loan` and leaves the mark, and chapter 13 keeps a refusal (:40) apart from a wait (:43); it suggested "`/apply renewal-notice` does not start either, but for its mark first: …" and "o `/apply aviso-renovacao` também não começa, mas primeiro pela marca: …", the rest as it is, and said it breaks neither the page nor docs/04, since the words were the Contract's own. Everything else checked out: C1 and C2 applied word for word with nothing else changed, the same reasoning in both editions with Portuguese names, the Portuguese correct and the dropped article acceptable in a block row, the pt row 74 columns naming member and due date, no em dash, run narration or commit hash, and the sentence agreeing with chapter 13 :40 and :43, the rule at :92 / :93 and the closing "free the moment" sentence. Fixed as its suggestion words it (Divergences). No new queue line.

```commit
docs(ch14-renewal-example): /apply stops first on the line's mark

- chapter 14's renewal-notice example: /apply does not start
  because the line is [ ], not [>], and after would hold it even so
- the Portuguese block row names the member and the due date
- both editions, within 74 columns

work/done/ch14-renewal-example.md
```
