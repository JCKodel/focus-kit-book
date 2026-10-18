# ch08-report-item-one

**Objective.** A reader of chapter 8's update report reads in item 1, as in items 2 and 3, the text the migration replaces as well as the text it proposes: "in the three cases below" becomes "in the four cases below"; both editions. Finding R2-4 of `m17-review` (work/done/m17-review.md).

**Decided without the author.** A batch /propose with no question asked; each choice below is the recommended one and names its source.

1. The text replaced is the kit's own: focus-kit 2026.10.18 changed the mark table's `[?]` row from "any session, in the three cases below" to "any session, in the four cases below" (the kit's `SETUP.md`, the `[?]` row; this repository's docs/05 §4 took the same change in `kit-2026-10-18`). The lending library's docs/05 was written from the kit's template, so it held the same words; its pt docs/05 holds them in Portuguese, "nos três casos abaixo", as item 3's pt quotes the library's pt docs/05.
2. Item 1 takes item 3's form, "replace "<old>" with "<new>"" (pt "trocar "<antigo>" por "<novo>""), and keeps its second half, the "after ... add ..." already there. The block is the command's output, written for the chapter (docs/04, The kit as it is; chapter 8 says so before it).
3. Every line of the new item keeps to 74 columns (docs/04, Width of a block): en 66, 68, 63, 56; pt 69, 70, 70, 70, 9. The pt item grows from four lines to five.
4. The sentence after the block, "Item 1 gives a line a fourth case to wait in", needs no change: it already says what the item does.
5. Files other slugs touch, and the order: `book/en/08-install-and-hosts.md` and `book/pt/08-install-and-hosts.md` are also edited by `ch15-review-range-order` (the sentence on item 3), `untracked-diff-wording` (the sentence on item 2) and `pt-ch08-migration-label` (the pt key point on the changelog). Those passages are twenty lines or more below the block, so in other hunks: stage this delivery's hunk alone if they are in the tree (docs/05 §6). In the batch's order this slug applies after `ch15-review-range-order` and before the other two. Line numbers shift as these land; /apply finds the block by its text.
6. No new docs/03 term, no queue line, no `kit:` note: the kit's own migration text is not quoted in the book, and the report block is the chapter's.

**Behaviour.**

* A reader of chapter 8's report can say, from item 1 alone, which words the library's docs/05 §4 had and which it gets: "three cases below" becomes "four cases below", and a fourth case is added after the third.
* The three items read alike: each names the text it replaces or the slot's current reading, then the proposed text.
* Fails: `make verify`'s `width` rule reports a line of the block over 74 columns.
* Fails: `grep -n 'is set "in the four' book/en/08-install-and-hosts.md` or `grep -n 'é posta "nos' book/pt/08-install-and-hosts.md` finds a line.

**Contract.** The block's item 1, as /apply writes it, replacing the four lines of item 1 and nothing else of the block.

`book/en/08-install-and-hosts.md`:

```
1. docs/05, §4 The queue: in the mark table, replace "in the three
   cases below" with "in the four cases below"; after "such as a fix
   found in the middle of an /apply" add ", or when a milestone
   review's code reading missed part of its range (§8)".
```

`book/pt/08-install-and-hosts.md`:

```
1. docs/05, §4 The queue: na tabela de marcas, trocar "nos três casos
   abaixo" por "nos quatro casos abaixo"; depois de "como uma correção
   descoberta no meio de um /apply" acrescentar ", ou quando a leitura
   do código de uma revisão de marco não cobriu parte do seu intervalo
   (§8)".
```

Terms: migration (migração), mark (marca), docs/03; no new term.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* Items 2 and 3 and the block's other lines: they already say what they replace.
* The sentences after the block: decision 4, and the other slugs of decision 5.

**Done when.**

* [x] The block's item 1 is the Contract's, in both editions.
* [x] The Behaviour's greps find nothing, and `width` is green.
* [x] No number, no private case, no em dash, no narrated run in the new text.
* [x] `make verify` green.
* [x] The delivery review run as docs/05 §5 says, on this delivery's hunk of both files and this page.
* [x] `make book`, and the paths of both PDFs given to the author (docs/05 §5, Proof of a screen).
* [x] Page in `work/done/`, line `[x]`, staged by hunk where the files hold other deliveries' changes (decision 5), commit message in a `commit` block.

Queue line, as it stands in docs/06:

```
[~] ch08-report-item-one     chapter 8's report item 1 says what text it replaces, as items 2 and 3 do; both editions
```

**Built.** Chapter 8, §What an update reports, both editions: the report block's item 1 is the Contract's, in the form of item 3 ("replace ... with ...", pt "trocar ... por ..."), with its "after ... add ..." half kept; no other line of the block changed. The lines measure 66, 68, 63 and 56 columns in English and 69, 70, 70, 70 and 9 in Portuguese, as decision 3 says. The Behaviour's greps find nothing; `width` is green.

**Decisions at apply time.** `make book` is run once by the batch driver at the end of the parallel run; staging is the driver's, from the paths this delivery reports. No Case A or Case B passage.

**Divergences and omissions.** None.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure).

**Delivery review.** One read-only agent on Opus read this delivery's hunk of both chapter files against this page and docs/04. No findings: the item matches the Contract in both editions, every line is within 74 columns, it reads like items 2 and 3, and the quoted "three cases below" is what docs/05 §4 held before the kit's 2026.10.18 change.

```commit
docs(ch08-report-item-one): say what text the report's item 1 replaces

- Chapter 8's report item 1 replaces "three cases below" with "four", as item 3 reads
- Both editions

work/done/ch08-report-item-one.md
```
