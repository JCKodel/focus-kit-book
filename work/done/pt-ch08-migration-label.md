# pt-ch08-migration-label

**Objective.** A reader of the Portuguese chapter 8's key points reads the label of the changelog's migration item, `Migração:`, as the English key point names `Migration:`. Finding R2-6 of `m17-review` (work/done/m17-review.md).

**Decided without the author.** A batch /propose with no question asked; each choice below is the recommended one and names its source.

1. The English key point says "in an item that starts with `Migration:` when the entry has one"; the Portuguese says "num item de migração, quando a entrada tem um", which drops the label the reader looks for. The Portuguese key point takes the label.
2. The label is `Migração:` alone, as the queue line says. The Portuguese reader opens `CHANGELOG.pt.md`, whose migration items start with `Migração:` (the kit's `CHANGELOG.pt.md`), and the chapter's §What an update reports already pairs the two labels once ("`Migration:` (no changelog em português, `Migração:`)"); the key point, like the English one, carries one label.
3. Only the Portuguese edition changes: the English already says it, and this change brings the translation to its source (ADR-0004; docs/04, Languages).
4. Files other slugs touch: `book/pt/08-install-and-hosts.md` is also edited by `ch15-review-range-order`, `ch08-report-item-one` and `untracked-diff-wording`, all far above the key points, in other hunks: stage this delivery's hunk alone if they are in the tree (docs/05 §6). In the batch's order this slug applies after the first two and before `untracked-diff-wording`. /apply finds the key point by its text.
5. No new docs/03 term, no queue line, no `kit:` note.

**Behaviour.**

* A reader of the Portuguese chapter 8, §Pontos-chave, can say which label starts a migration item in the Portuguese changelog: `Migração:`.
* Fails: `grep -n "num item de migração" book/pt/08-install-and-hosts.md` finds a line.
* Edge: the English chapter is unchanged; `git diff book/en/08-install-and-hosts.md` shows no hunk of this delivery.

**Contract.** In `book/pt/08-install-and-hosts.md`, the third key point, "* O changelog do kit, a entrada mais nova primeiro, diz para cada versão o que mudou, o problema que causou a mudança e, num item de migração, quando a entrada tem um, o que mudar nos documentos do projeto.", becomes:

```
* O changelog do kit, a entrada mais nova primeiro, diz para cada versão o que mudou, o problema que causou a mudança e, num item que começa com `Migração:`, quando a entrada tem um, o que mudar nos documentos do projeto.
```

Terms: changelog (changelog), migration (migração), docs/03; no new term.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* The section's sentence that pairs `Migration:` and `Migração:`: right as it is.
* The English edition: decision 3.

**Done when.**

* [x] The Portuguese key point is the Contract's.
* [x] The Behaviour's grep finds nothing.
* [x] No em dash in the new text.
* [x] `make verify` green.
* [x] The delivery review run as docs/05 §5 says, on this delivery's hunk and this page.
* [x] `make book`, and the paths of both PDFs given to the author (docs/05 §5, Proof of a screen).
* [x] Page in `work/done/`, line `[x]`, staged by hunk where the file holds other deliveries' changes (decision 4), commit message in a `commit` block.

Queue line, as it stands in docs/06:

```
[~] pt-ch08-migration-label  the Portuguese chapter 8's key point names the changelog item's `Migração:` label as the English names `Migration:`
```

**Built.** The Portuguese chapter 8, §Pontos-chave: the changelog key point names the item by its label, "num item que começa com `Migração:`", as the English names `Migration:`. The English chapter is unchanged. The Behaviour's grep finds nothing.

**Decisions at apply time.** `make book` is run once by the batch driver at the end of the parallel run; staging is the driver's, from the paths this delivery reports. No Case A or Case B passage.

**Divergences and omissions.** None.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure).

**Delivery review.** One read-only agent on Opus read this delivery's hunk of the Portuguese chapter against this page and docs/04. No findings: the key point matches the Contract, mirrors the English key point with the single label `Migração:`, and the English file has no change.

```commit
docs(pt-ch08-migration-label): name the Migração: label in pt chapter 8

- The Portuguese key point on the changelog names the item's `Migração:` label
- Brings the translation to the English source

work/done/pt-ch08-migration-label.md
```
