# ch08-update-other-edits

**Objective.** After chapter 8 the reader knows that applying an update's migrations can need an edit no report item names, when a migration's wording contradicts a sentence the report does not check, and sees it on the book's own update to 2026.10.20.3, where docs/05 §7 was edited beside §2 and §4; so "the update is done when the migrations are applied" holds of the chapter's own example. Finding C1 of `work/done/m27-review.md`.

**Behaviour.**

* Given chapter 8's section "What an update reports", the reader still reads each item with one of three outcomes and every item reported, never done (en 81 to 85, 90, 109 unchanged), and then learns that applying the migrations can take an edit no item names: a sentence the report does not check can contradict the wording a migration proposes, and the line that applies the migrations edits it too.
* The example is the book's: at 2026.10.20.3, docs/05 §7 admitted no specialized subagent beyond the reviews' readers and checker, which the §4 paragraph the report proposed, on a command typed with several slugs, contradicted; the line that applied §2 and §4 edited §7 as well, and §7 now admits a command's one subagent per slug with the reviews' readers and checker (`work/done/kit-2026-10-20-3.md`, "The project's other dispositions"; docs/05 :370 to :371 as committed).
* "The update is done when the migrations are applied" stays, and the new sentence follows it in the same paragraph, so "applied" covers that edit.
* Edge: the excerpt (en 58 to 79, pt 58 to 80) does not change: the report held no §7 item, step 4's §7 item matched, and its "other items" line, which names §§6 to 8, stays true (C1).
* Edge: chapter 8 does not teach a command's subagents; the sentence names §7's clause and the §4 paragraph only, as chapters 12 to 18 teach them.
* Fails: a §7 or provenance item in the excerpt; "Applied:" in the excerpt; a comparison of kit versions ("the template's §7 changed though step 4's item did not", "gained", "since"); a count of edits, files or lines; a record line number, commit hash or narrated run in the chapter; §7 quoted as chapter 16 :67 reads today instead of as docs/05 :370 to :371 reads; one edition changed without the other; an em dash. /apply removes it before verify.

**Contract.** Both editions, `book/en/08-install-and-hosts.md` and `book/pt/08-install-and-hosts.md`, same change; English is the source (ADR-0004). Line numbers as the files are now (HEAD `0534b1f`).

* en 93, after "...so the change to your rules or your queue gets a page, verify and your review.", a new line in the same paragraph:

  "Applying them can need an edit no item names, when a migration's wording contradicts a sentence the report does not check: on the book's repository at 2026.10.20.3, docs/05 §7 admitted no specialized subagent beyond the reviews' readers and checker, which the §4 paragraph the report proposed, on a command typed with several slugs, contradicted, so the line that applied §2 and §4 edited §7 too, and §7 now admits a command's one subagent per slug with the reviews' readers and checker."

* pt 94, after "...para que a mudança nas suas regras ou na sua fila tenha uma página, verificação e a sua revisão.", a new line in the same paragraph:

  "Aplicá-las pode pedir uma edição que nenhum item cita, quando o texto de uma migração contradiz uma frase que o relatório não confere: no repositório do livro, na 2026.10.20.3, o docs/05 §7 não admitia nenhum subagente especializado além dos leitores e do conferente das revisões, o que o parágrafo do §4 que o relatório propôs, sobre um comando digitado com vários slugs, contradizia, então a linha que aplicou o §2 e o §4 editou o §7 também, e o §7 hoje admite o subagente por slug de um comando junto com os leitores e o conferente das revisões."

* Nothing else in chapter 8 changes: en 81 to 85 / pt 82 to 86, en 88 and 90 / pt 89 and 91, en 109 / pt 110 stay true of the report's items.
* Neighbouring lines on the same files: none in M27 (`ch12-13-19-several-slugs-paths` touches chapters 12, 13 and 19, `ch16-subagent-account` chapter 16, `m27-records-claims` record pages). M28's `ch08-update-2026-10-20-4` and `ch08-copilot-cli` touch chapter 8 after this line; the first replaces the update example and should keep or restate this sentence's claim.

Sources: the record named in prose, `work/done/kit-2026-10-20-3.md`, read as committed at `0534b1f` ("The project's other dispositions", its §7 bullet; Migration report, the §§6 and 7 item); docs/05 :370 to :371. No source note (as `ch08-update-2026-10-20-3` decided). `m27-records-claims` edits that record's review and build lines, not its §7 facts.

**States.** Inapplicable: prose, no screen.

**Visual reference.** Inapplicable: existing chapter layout.

**Out of scope.** The excerpt and its "other items" line; chapter 16's list and its subagent account (`ch16-subagent-account`); chapters 12, 13 and 19 (`ch12-13-19-several-slugs-paths`); the record pages (`m27-records-claims`); docs/05, docs/03, docs/06.

**Decisions from the documents.**

* The fix is prose after en 93 / pt 94 and not the excerpt: C1 says the excerpt's "other items" line stays true, and `ch08-update-2026-10-20-3` kept §7 out of the excerpt because the report held no §7 item.
* §7 is quoted as docs/05 :370 to :371 reads now; chapter 16 :67's older wording is `ch16-subagent-account`'s.
* Portuguese: "conferente" for checker and "subagente", as chapter 16 pt :67 and chapter 8 pt :64 write them.
* No version comparison and no count: the book is the kit today; the sentence speaks of the book's docs/05, naming the version the chapter already names.
* Token `(PA)`: every line above in M27 that this definition reads from is `[x]` (the record is committed; `m27-records-claims` is `[ ]` and changes none of the facts used here); the build touches only chapter 8's two files, which no line above or in flight touches. `(PA)` holds.

**Decisions taken alone.** The agent chose each of these.

* The sentence follows en 93 / pt 94 rather than en 88 / pt 89, so "applied" in "the update is done when the migrations are applied" is the word it qualifies.
* The sentence states the mechanism (a migration's wording contradicting a sentence the report does not check) and not the /apply stop rule of chapter 13; no link to chapter 13 or 16, to keep chapter 8 off subagents.
* The queue line's wording stays.

**Done when.**

* [x] Both editions of chapter 8 hold the Contract's sentence after en 93 / pt 94, the Portuguese with Portuguese wording; nothing else in either file changed.
* [x] The sentence checked against `work/done/kit-2026-10-20-3.md` (its §7 disposition) and docs/05 :370 to :371.
* [x] No version comparison, count, record line number, commit hash or em dash in the new sentence (grep).
* [x] `make verify` green after the last edit; `make book` builds both editions, with both PDF paths.
* [x] Delivery review as docs/05 §5 says, recording what its agent read and whether it kept the session's advisor. No private case, so OD-3 approval is inapplicable.

**Built.** The Contract's sentence is the new en :94 and pt :95, in the paragraph of en :93 / pt :94; `git diff --stat HEAD` on the two files shows one insertion each and nothing else. The facts match the record as committed (`work/done/kit-2026-10-20-3.md`, "The project's other dispositions", its §7 bullet, and the Migration report's §§6 and 7 item) and docs/05 :370 to :371, which read "no subagent beyond a command's one per slug (§4) and the reviews' readers and checker".

**Divergences.** The Portuguese reads "na versão 2026.10.20.3" where the Contract wrote "na 2026.10.20.3", as the delivery review suggested, so the version is named as chapter 8 pt names it elsewhere ("o focus-kit 2026.10.20.3"). The page's line numbers were taken at HEAD `0534b1f`; chapter 8 and docs/05 had not changed since, re-checked before the edit.

**Omissions.** None.

**Proof.**

* Greps on the new lines: no em dash in either file; none of "Applied:", "gained", "since" (pt "Aplicado:", "ganhou", "desde"), a hash-like token or a `:NN` line number in the new sentence.
* `make verify`: exit 0, all checks passed, after the last chapter edit and again after the page's last edit before this line.
* `make book`: exit 0, after the last verify; both editions built, `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` (with their EPUBs).

**Delivery review.** One read-only Opus agent (an Explore subagent with model opus); it did not keep the session's advisor, since a subagent opened this way has none. It read `git diff HEAD` of the two chapter files, this page, docs/04, AGENTS.md, `work/done/kit-2026-10-20-3.md` as committed and docs/05 §7. Its reply, as returned:

> I found no blocking findings. The delivery matches its page, docs/04, AGENTS.md and the sources.
>
> **What checks out:**
> - **Contract text:** The new sentence matches the Contract word for word in both editions, at book/en/08-install-and-hosts.md:94 and book/pt/08-install-and-hosts.md:95. A fixed-string whole-line grep finds each sentence exactly once, in its own edition.
> - **Placement:** Each sentence sits in the same paragraph right after "The update is done when..." (en :93) and "A atualização termina quando..." (pt :94).
> - **Nothing else changed:** The diff stat shows one insertion per file and nothing else, so the excerpt (en 58 to 79, pt 58 to 80) is untouched. There is no §7 or provenance item and no "Applied:".
> - **Facts:** They agree with the committed record. Its other-dispositions §7 bullet is at work/done/kit-2026-10-20-3.md:117, the §§6 and 7 item at :109, and the record's §7 bullet at :48 quotes the old wording. §7 is quoted as docs/05:370 to :371 reads ("no subagent beyond a command's one per slug (§4) and the reviews' readers and checker"), not as chapter 16 :67 reads.
> - **Fails list:** No em dash in either file. The new sentence has no version comparison ("gained", "since", "changed though"), no count, no record line number, no commit hash and no narrated run.
> - **Parity:** Both editions changed. "conferente" and "subagente" follow pt :64 as the page decided.
>
> **Minor wording points (optional):** Both are wording points in the Contract itself, not departures by the delivery. A fix would change the page and both lines together.
> 1. **book/pt/08-install-and-hosts.md:95, "na 2026.10.20.3":** This leaves "versão" unstated. Elsewhere chapter 8 pt writes "o focus-kit 2026.10.20.3" (:46, :56). Suggested fix: "na versão 2026.10.20.3" or "no focus-kit 2026.10.20.3".
> 2. **book/pt/08-install-and-hosts.md:95, "o subagente por slug de um comando":** This drops the English "one" ("a command's one subagent per slug"). It is still natural and faithful, since "o ... por slug" carries the singular. Suggested fix, only if exact parity is wanted: "o único subagente por slug de um comando".
>
> **Not checked:** I did not run `make verify` or `make book`; the page's Done when still lists both. All 2026-10-20-3 record line numbers above refer to the copy committed at HEAD.

What was done with it: point 1 fixed (Divergences); point 2 left as it is, since the agent itself calls it natural and faithful and "o subagente por slug" already says one per slug. No new queue line.

**Decisions at build.** Taken alone, by the batch rule to take the recommended option: the review's point 1 fixed and point 2 kept, as above.

```commit
docs(ch08-update-other-edits): migrations can need other edits

- chapter 8: applying migrations can edit a sentence no item names
- the book's example: docs/05 §7 edited beside §2 and §4

work/done/ch08-update-other-edits.md
```
