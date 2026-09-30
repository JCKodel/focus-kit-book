# pt-skeleton-diff

**Objective.** A Portuguese reader of chapter 10 who relies on the summary of the `skeleton` diff, as the edition invites, places each change in the section the diff puts it and misses none of Behaviour's.

**Behaviour.**

* The summary after the diff (`book/pt/10-propose.md:420` today) says that in Behaviour the server now also creates the `data/` folder, that a failed migration now stops the start with exit code 1, and that the import check and the manifest leave, each as the diff has it (lines 288 to 303 of the chapter).
* The summary no longer puts exit code 1 in the Contract; its Contract clause keeps the rest as today: files outside the pattern ignored, the `migrate(db, folder)` signature, the `MigrationFailed` error with file and message, `Result` in `src/lib/result.ts`.
* Its Visual reference, Out of scope and Done when clauses, and the next paragraph ("Cada buraco fechou..."), are unchanged.
* The English edition is unchanged: the summary exists only in Portuguese, because there the diff stays in English; the English reader reads the diff itself.
* Finding F5 of the M4.1 review is settled.

**Contract.**

* Files: `book/pt/10-propose.md`, line 420 only. `book/en/10-propose.md` unchanged.
* The line becomes, word for word:

  > O diff fica como está no registro, em inglês: no Behaviour, o servidor passa a criar também a pasta `data/`, a migration que falha passa a interromper o início com código de saída 1, e saem a checagem de import e o manifest; no Contract, os arquivos fora do padrão são ignorados, e entram a assinatura `migrate(db, folder)` do executor, o erro `MigrationFailed` com o arquivo e a mensagem, e o `Result` em `src/lib/result.ts`; o Visual reference ganha a fonte `system-ui`, 16px de margem e as cores padrão do navegador; o Out of scope ganha o manifest, que vira a entrega `install`, a checagem de import e a base de pixels; e o Done when troca a base por testes Vitest do executor contra uma pasta temporária e um screenshot salvo uma vez como prova.

* Terms of docs/03: none new. "código de saída" is the chapter's own wording (line 159).
* Sources: none new; the diff is already under `[^propose-run]`. Cases: none. Exercises: unchanged. The guided project: unchanged, no tag.

**Out of scope.**

* The summary's other omissions (Done when's folder-creation test and its test against the real migrations folder, Out of scope losing `src/lib/result.ts`): a summary may leave them out, and the review confirmed only these two errors.
* An English summary of the diff: the English reader has the diff in its own language.
* The other Portuguese lines of M4.2 (`pt-spec-change-terms`): their own delivery.

**Done when.**

* [ ] `book/pt/10-propose.md:420` reads as the Contract gives it; `book/en/10-propose.md` has no change.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
