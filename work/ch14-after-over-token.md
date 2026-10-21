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

* [ ] C1, C2 and C3 read as the Contract says in both editions, each quoted text found once before its edit; the rest of both files unchanged.
* [ ] Both editions written, the same paragraph and line in each, Portuguese names in the Portuguese edition.
* [ ] The chapter still opens with its value; no filler and nothing useful cut; no number added, so none to source; no private case used.
* [ ] No em dash in the changed text; no run narration and no commit hash in the chapter.
* [ ] The new block keeps to 74 columns in both editions.
* [ ] `make verify` green after the last edit.
* [ ] `make book` builds both editions after the last verify, both PDF paths recorded.

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
