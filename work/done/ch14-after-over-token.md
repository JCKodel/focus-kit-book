# ch14-after-over-token

**Objective.** After chapter 14 the reader, developer or not, can say that `after` holds `/propose` and `/apply` until every line it names is `[x]`, whatever the line's `(PA)` token says, and show it on a library line whose token would let both commands start and whose `after` stops them.

**Behaviour.** What the reader can do or explain after the chapter:

* Say what `after` holds, in docs/05 §4's words as `kit-2026-10-20-5` wrote them: neither `/propose` nor `/apply` starts until every line it names is `[x]`, whatever the token says.
* Read the chapter's new line, `renewal-notice (-A) · after renew-loan`, with `search-catalog` `[x]`, `lend-book` `[*]` and `renew-loan` `[>]`: every line above is `[>]` or beyond, so the `-` lets `/propose` start, and the `A` lets `/apply` run beside them; but `after` names `renew-loan`, `[>]` and not `[x]`, so `/propose renewal-notice` says it waits on `renew-loan`, leaves the mark as it is, and stops, and `/apply` would do the same.
* Failure: asked "the token lets it, so may I run `/propose renewal-notice` now?", answer no: the token speaks of the lines above, `after` of the lines it names, and the token never lifts an `after`.
* Edge: once `renew-loan` is `[x]`, `renewal-notice` is free at that moment, with nothing to clear and no mark to change, as chapter 14 already says of `return-book`; the `· after` stays on the line.
* Edge: the same line as `(PA)` waits all the same; a token with a `P` or an `A` never makes an `after` line free.
* Tell the two waits apart in one sentence: the `-` waits for every line above, `[>]` or beyond before `/propose` and `[x]` before `/apply`; `after` waits for the lines it names, `[x]` for both commands.
* In the Portuguese edition, read the same paragraph and line with Portuguese names: `aviso-renovacao (-A) · after renovar-emprestimo`, `src/features/avisos/`.

**Contract.** Two files: `book/en/14-queue-states.md` and `book/pt/14-queue-states.md`. Line numbers are at HEAD `6c8d56b`, en / pt. Each change replaces only the quoted words; the rest of each sentence stays.

* **C1, "The next line, and which run together", the rule** (:92 / :93):
  * en: "`after` still holds both commands, token or not." becomes "`after` still holds both commands, token or not: neither `/propose` nor `/apply` starts until every line it names is `[x]`, whatever the token says."
  * pt: "O `after` continua valendo para os dois comandos, com token ou sem." becomes "O `after` continua valendo para os dois comandos, com token ou sem: nem o `/propose` nem o `/apply` começa enquanto alguma linha que ele nomeia não está `[x]`, diga o token o que disser."
* **C2, same section, the example**: a new paragraph and a one-line block inserted after the several-slugs sentence (:107 / :108) and before the blank line and "[Chapter 19](19-worktrees.md) shows how two sessions run in one folder" (:109 / :110). The four-line block (:94 to :100 / :95 to :101) and the sentences reasoning from it (:102 to :107 / :103 to :108) stay; the new paragraph is a later state, so no earlier sentence changes.
  * en:

    ````
    `after` is not the token, and the token never lifts it.
    Later, with `search-catalog` `[x]`, `lend-book` still `[*]` and `renew-loan` `[>]`, a line is added below them, written for this chapter like the four above:

    ```
    [ ] renewal-notice (-A)  warns a member of the due date · after renew-loan
    ```

    Its page takes the renewal's rule from `renew-loan`'s, so its `/propose` waits for every line above to be `[>]` or beyond, and they all are; its build lives in `src/features/notices/`, so its `/apply` may run beside them; and it needs renewals that exist, so it was written with `· after renew-loan`.
    The token lets both commands start, and neither does: `after` names `renew-loan`, `[>]` and not `[x]`, so `/propose renewal-notice` says it waits on `renew-loan`, leaves the mark as it is, and stops, and `/apply` would do the same.
    The `-` waits for the lines above, `after` for the lines it names; `renewal-notice` is free the moment `renew-loan` is `[x]`.
    ````

  * pt:

    ````
    O `after` não é o token, e o token nunca o suspende.
    Mais tarde, com `buscar-catalogo` em `[x]`, `emprestar-livro` ainda em `[*]` e `renovar-emprestimo` em `[>]`, uma linha é acrescentada abaixo delas, escrita para este capítulo como as quatro acima:

    ```
    [ ] aviso-renovacao (-A)  avisa o vencimento · after renovar-emprestimo
    ```

    A página dela tira a regra da renovação da de `renovar-emprestimo`, então o `/propose` dela espera toda linha acima estar `[>]` ou além, e todas estão; a construção dela mora em `src/features/avisos/`, então o `/apply` dela pode rodar ao lado delas; e ela precisa de renovações que existam, então foi escrita com `· after renovar-emprestimo`.
    O token deixa os dois comandos começarem, e nenhum começa: o `after` nomeia `renovar-emprestimo`, em `[>]` e não em `[x]`, então `/propose aviso-renovacao` diz que espera `renovar-emprestimo`, deixa a marca como está, e para, e o `/apply` faria o mesmo.
    O `-` espera as linhas acima, o `after` as linhas que ele nomeia; `aviso-renovacao` fica livre no momento em que `renovar-emprestimo` está `[x]`.
    ````

  (The outer fences above only delimit the text on this page; in the chapter the inner block is the only fenced block.)
* **C3, "Key points", the free-line item** (:207 / :208):
  * en: "`after` holding both," becomes "`after` holding both until every line it names is `[x]`, whatever the token says,".
  * pt: "o `after` valendo para os dois," becomes "o `after` valendo para os dois até toda linha que ele nomeia estar `[x]`, diga o token o que disser,".

Terms of docs/03 used: `parallel token`, `dependency`, `free line`; none new. Sources: none new; the rule is docs/05 §4's, and the chapter cites no number here. Cases: none; the example is the lending library's, written for the chapter, as it says.

Chapters 11, 12 and 13 checked for a statement of the rule that reads as the token overriding `after`: none does. Chapter 11 :16 and :87 to :89 describe the token and `after` apart; chapter 12 :27 says `/propose` does not start on an `after` not yet `[x]` "and likewise" on a `-` token, two holds side by side, and :154 and :191 to :192 say "the tokens and `after`" together; chapter 13 :36, :43 and :44 require both, the `after` lines `[x]` and the token letting it build. Chapter 9 :23 describes the token alone. No sibling sentence goes stale, so no other chapter is touched.

Neighbours: `ch08-update-2026-10-20-5`, in flight in M29, touches chapter 8 and nothing of chapter 14; no file is shared. `m29-review` waits on this line by its `after`.

**States.** Inapplicable: a chapter, no screen.

**Visual reference.** Inapplicable: no figure; the two PDFs of `make book` are the review copy.

**Out of scope.**

* Chapter 8: `ch08-update-2026-10-20-5`'s.
* docs/03's `parallel token` row ("`after` holds for both commands, token or not") and `free line` row ("whose `after` lines are all `[x]`"): true as written, the rule unchanged; no row added or edited.
* docs/05 §4: already migrated by `kit-2026-10-20-5`.
* Chapter 14 :89's "so it can be talked through now" and "so it can be built now", and chapter 9 :23 and chapter 11 :16, which describe the token alone: C1, right below :89, now says what `after` holds, and the other chapters point to chapter 14.
* The "a page decided alone says the agent chose" rule of 2026.10.20.5: not this line's sentence; chapter 12 :192 already says "a command told to decide alone has each answer written on the page as the agent's".
* The chapter's opening sentences (:3 to :5): "tell an order written with a line, `· after`" already covers it.

**Done when.**

* [x] C1, C2 and C3 read as the Contract says in both editions, each quoted text found once before its edit; the rest of both files unchanged.
* [x] Both editions written, the same paragraph and line in each, Portuguese names in the Portuguese edition.
* [x] The chapter still opens with its value; no filler and nothing useful cut; no number added, so none to source; no private case used.
* [x] No em dash in the changed text; no run narration and no commit hash in the chapter.
* [x] The new block keeps to 74 columns in both editions.
* [x] `make verify` green after the last edit.
* [x] `make book` builds both editions after the verify that followed the chapters' last edit, one more verify following it (Divergences), both PDF paths recorded.

**Decisions from the documents.**

* The rule's wording is docs/05 §4's as `kit-2026-10-20-5` migrated it ("neither /propose nor /apply starts until every line it names is `[x]`, whatever the token says"; `work/done/kit-2026-10-20-5.md`); the book teaches the kit as it is today, with no before and after.
* The example's reasoning is the record's own (`work/done/kit-2026-10-20-5.md`, the `shout` question): the `-` would let `/propose` wait only for the lines above to be `[>]`, but `after` is not the token, and the line is free once the line it names is `[x]`.
* Free at once when the named line is `[x]`, nothing to clear, the `after` kept: chapter 14 :74 and docs/03 `free line`, unchanged.
* Portuguese slugs and folder translated, `after` and the marks kept: docs/04 :27.
* Token `(PA)`: the one line above in flight, `ch08-update-2026-10-20-5`, is on chapter 8; this definition takes nothing from its page, and the build touches only chapter 14's two files, none of its files; `after` names `kit-2026-10-20-5`, already `[x]`.

**Decisions taken alone.** The agent chose each of these (the batch's driver asked for recommended answers; correct them in the review).

* The example is a lending-library line, `renewal-notice (-A) · after renew-loan`, not the queue line's `shout (-A) · after farewell`: every example in chapter 14 is the library's, written for the chapter (docs/04 :26 and :50), `shout` and `farewell` appear nowhere in the book, and the Portuguese edition would need names for kit test slugs. The shape is the line's: a `(-A)` line whose `after` names a `[>]` line, so the token lets both commands start and `after` alone holds them. The queue line's sentence becomes "chapter 14: `after` holds /propose and /apply until every line it names is `[x]`, whatever the `(PA)` token says, with a library line whose token lets both commands start and whose `after` names a `[>]` line as the example; both editions · after kit-2026-10-20-5".
* The example is a later state in its own paragraph, not a fifth line in the four-line block, so the sentences reasoning from that block, `search-catalog` `[ ]` among them, stay true as written.
* The renewal notice's `-` first comes from its page taking `renew-loan`'s rule, its `A` from a folder of its own, `src/features/notices/`, and its `after` from needing renewals that exist: each letter and the order has a reason the reader can check.
* The line's slug and sentence are short so the block keeps to 74 columns (docs/04, "Width of a block"; `scripts/check_width.py`): 74 in English, 71 in Portuguese.
* The key point is spelled out too (C3), since "`after` holding both" would say less than the section above it.

**Built.** C1 at en :92 / pt :93; C2 after the several-slugs sentence, en :109 to :118 / pt :110 to :119, a blank line before it and the "Chapter 19" / "capítulo 19" line after it; C3 in the free-line key point, en :218 / pt :219. Each quoted text was found once (`grep -cF`) before its edit. `git diff --stat HEAD` on the two files shows 13 insertions and 2 deletions in each, three hunks, and nothing else. The page's line numbers were taken at `6c8d56b`; chapter 14 was last changed in `6e37777`, earlier, and the lines were re-checked before the edit.

**Divergences.**

* C2 is set off by a blank line from the several-slugs sentence, since the Contract calls it "a new paragraph" and does not say whether a blank line precedes it.
* The Portuguese reads "o `/propose` dela espera até toda linha acima estar `[>]` ou além" where the Contract wrote "espera toda linha acima estar", as the delivery review suggested, matching pt :93 and :105.
* The Done when, as defined at `2faeb03`, held no Delivery review item, which docs/05 §5 asks before /apply ends; the review ran as its paragraph records, whether it kept the session's advisor not recorded (Delivery review). Its `make book` item said "after the last verify", while the Proof records the book after the verify that followed the review's fix and one more verify after it; `m29-records-claims` gave the item the Proof's words.

**Omissions.** None.

**Proof.**

* Greps: no em dash in either file; the new block is 74 columns in English and 71 in Portuguese.
* `make verify`: exit 0, all checks passed, after the chapter edits and again after the review's fix; the tree also held another delivery's uncommitted chapter 8, docs/06 and `work/ch08-update-2026-10-20-5.md`.
* `make book`: exit 0, after the verify that followed the review's fix, the chapters' last edit, at HEAD `3c2a050`, in that same tree; both editions built, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` (with their EPUBs).
* `make verify` once more after this page's last edit and its move to `work/done/`: exit 0.

**Delivery review.** One read-only Opus agent (an Explore subagent with model opus), launched by this lane. It read `git diff HEAD` of the two chapter files, this page, AGENTS.md, docs/04, docs/05 §4 and §5, docs/03's `parallel token` and `free line` rows and `work/done/kit-2026-10-20-5.md`; whether it kept the session's advisor, as docs/05 §5 asks, is not recorded, its reply naming none. Its reply, as returned:

> I found no blocking issues. All five checks pass, apart from the minor points listed under optional.
>
> **Blocking findings**
>
> None.
>
> **What I checked**
>
> 1. **Contract text.** I checked each quoted text with a script, in both editions.
>    - **C1:** the old sentence appears once at HEAD. After the edit only the new wording is there, at en:92 and pt:93.
>    - **C2:** the paragraph and block on the page appear exactly once in each file. They sit after the several-slugs sentence, with a blank line before them, and before the "Chapter 19" / "capítulo 19" line.
>    - **C3:** the key-point wording matches, at en:218 and pt:219 in the new files.
>    - **Nothing else changed:** `git diff --stat` shows 3 hunks per file, 13+/2- each, and no other hunk.
> 2. **Reasoning against docs/05 §4 (:103-109).** In the stated state, every line above `renewal-notice` is `[&gt;]` or beyond: `members` `[x]`, `lend-book` `[*]`, `search-catalog` `[x]`, `renew-loan` `[&gt;]`. So the `-` in first place lets `/propose` start. The `A` lets `/apply` run beside them because `src/features/notices/` is a different folder. `after renew-loan` holds both commands because `renew-loan` is `[&gt;]`, not `[x]`. "Free the moment `renew-loan` is `[x]`" matches the free-line definition in docs/03 and chapter 14 :74. The "waits on X, leaves the mark as it is, and stops" wording repeats the chapter's own phrasing at :106, and the reasoning matches the `shout` answer in work/done/kit-2026-10-20-5.md:16.
> 3. **Agreement with the rest of chapter 14.** The new paragraph says "Later", so the four-line block and the sentences that use it (where `search-catalog` is `[ ]`) stay true. :71 ("do not start a line that is not free") and the "(--)" sentence at :103 are consistent with it. The docs/03 rows `parallel token` and `free line` still hold.
> 4. **Portuguese.** It is faithful and uses Portuguese names: `aviso-renovacao`, `renovar-emprestimo`, `src/features/avisos/`. `after` and the marks are kept, as docs/04 requires.
> 5. **docs/04 and AGENTS.md.**
>    - The changed text has no em dash, no run narration and no commit hash.
>    - It adds no number and uses no private case.
>    - Both new passages say the line was "written for this chapter".
>    - The block is 74 columns in English and 71 in Portuguese.
>    - I saw nothing in the prose rules' patterns that would trigger.
>
> **Optional points**
>
> - en:118 and pt:119, "`/apply` would do the same": `renewal-notice` is still `[ ]`, so `/apply` would refuse first because the line isn't `[&gt;]`, before `after` even comes into it. Writing "and `/apply`, once its page is `[&gt;]`, would do the same" would make it exact. This is a hypothetical, as the page's Behaviour has it, so it is not wrong.
> - pt:117, "o `/propose` dela espera toda linha acima estar `[&gt;]`": this reads a little awkwardly. "espera até toda linha acima estar" matches pt:93 and pt:105 and reads more naturally.
> - pt:120, "no momento em que `renovar-emprestimo` está `[x]`": "fica `[x]`" would be more natural.
> - pt:114, "avisa o vencimento" drops "a member", which the English has. The 74-column limit leaves only 3 spare columns, so restoring it would mean cutting something else.
> - docs/04 "Context before an excerpt" says an excerpt is never "a loose line that leans on the lines around it". The one-line block does lean on the four-line queue, but the sentence before it sets it up explicitly. I judge it acceptable.
>
> **What I did not check**
>
> I didn't run `make verify` or `make book`, so the prose, parity and width checks have not actually run. I didn't re-read chapters 9, 11, 12 and 13, where the page says no sentence goes stale. I didn't check the whole of docs/04's prose-rule list against the full chapter, only against the changed lines.

What was done with it: no blocking finding. The second point fixed (Divergences). The first kept: the sentence is the Contract's and the Behaviour's, a hypothetical the agent calls not wrong. The third kept: "está `[x]`" is the chapter's own phrasing for a mark. The fourth kept: the block's width. The fifth kept, as the agent judges. No new queue line.

**Decisions at build.** The agent chose these alone, by the batch rule to take the recommended option: the blank line before C2, and the review's points handled as above.

```commit
docs(ch14-after-over-token): after holds both commands, token or not

- chapter 14: after holds /propose and /apply until its lines are [x]
- the example: renewal-notice (-A) waits on renew-loan; both editions

work/done/ch14-after-over-token.md
```
