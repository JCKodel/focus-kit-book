# case-a-why-anonymous

**Objective.** A reader of the prologue learns why Case A has no owner, client or business on the page: it is a private corporate project, and its name could not be published without authorization. Found by the author's reading of the book on 2026-10-18: "pt 00:107, 'o Caso A sem o seu dono, o seu cliente ou o seu negócio', and its English source, must say why: Case A is a private corporate project, and its name could not be published without authorization."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *One sentence, in place.* The reason joins the sentence that states the omission, en 00:107 and pt 00:107, instead of a new sentence or a note: the reader meets the omission and its reason together, and the prologue grows by one clause (ADR-0015: as long as proving takes, no filler). Source: the author's draft, which names that line; docs/04 (a source note only where the reader gains something to open, never for a private case).
2. *The author's words, and nothing more.* The reason says "a private corporate project" and "its name could not be published without authorization", as the draft does; it does not say who would authorize, why the client wants it private, or any term, place, date or business of Case A. "Corporate" says only what docs/00 already says, that Case A is one of "the author's company projects". Source: the author's draft, docs/00 (Cases), docs/03 §Entities and invariants ("Case A and Case B are never named, dated to a meeting, located, or described by business detail"), ADR-0012.
3. *The wording.* en 00:107 becomes: "Ninjobs appears by name; Case A is a private corporate project, and its name could not be published without authorization, so it appears without its owner, its client or its business." pt 00:107 becomes: "A Ninjobs aparece pelo nome; o Caso A é um projeto corporativo privado, e o seu nome não poderia ser publicado sem autorização, então aparece sem o seu dono, o seu cliente ou o seu negócio." The passage goes to the author for approval (decision 6), who may reword it. Source: the author's draft; docs/04 §Writing the book (one sentence per line, no em dash).
4. *Case B is not touched.* The prologue names Case A only (en 00:106 and 107; Case B appears nowhere in chapter 0), and the draft names Case A only. Source: grep of `book/en/00-product-people-process.md` on 2026-10-18; the draft.
5. *The article before Ninjobs is not this delivery's.* pt 00:107 begins with the article `pt-ninjobs-masculine` changes; this delivery keeps whatever article the line holds at apply time ("A Ninjobs" at /propose) and changes only the Case A clause. Source: `work/pt-ninjobs-masculine.md` (Deliveries in flight).
6. *The author's approval is required.* The changed sentence is a passage drawn from Case A, so it is listed under Behaviour for the author's approval before the delivery is done; it is not inapplicable as in deliveries that only touch the word Ninjobs. Source: docs/00 OD-3, docs/05 §5 (Case A and Case B).
7. No new docs/03 term, no new queue line, no split.

**Behaviour.**

* A reader of the English prologue, at the end of "What the team gains", reads why Case A is anonymous: en 00:107 reads, from "Ninjobs appears by name, and Case A without its owner, its client or its business.", "Ninjobs appears by name; Case A is a private corporate project, and its name could not be published without authorization, so it appears without its owner, its client or its business."
* A reader of the Portuguese prologue reads the same: pt 00:107 reads, from "A Ninjobs aparece pelo nome, e o Caso A sem o seu dono, o seu cliente ou o seu negócio.", "A Ninjobs aparece pelo nome; o Caso A é um projeto corporativo privado, e o seu nome não poderia ser publicado sem autorização, então aparece sem o seu dono, o seu cliente ou o seu negócio." (with the article before Ninjobs as the line holds at apply time, decision 5).
* For the author's approval (docs/00 OD-3): the two sentences above, the only passage drawn from Case A this delivery writes.
* Checked at apply time:
  * `grep -n "could not be published without authorization" book/en/00-product-people-process.md` and `grep -n "não poderia ser publicado sem autorização" book/pt/00-product-people-process.md` print one line each.
  * `git diff book` shows only line 107 of chapter 0 changed in each edition, and in Portuguese no word before "aparece pelo nome" changed.
  * `make scan` green: no listed term.
* Fails: the reason names, dates, locates or describes the business of Case A, or names who would authorize; Case B touched; a sentence added elsewhere; the article before Ninjobs changed by this delivery; one edition changed without the other; an em dash.

**Contract.**

* Files: `book/en/00-product-people-process.md` and `book/pt/00-product-people-process.md`, line 107 only.
* Terms of docs/03: none new. Sources: none added or removed. Cases: Case A, one clause saying it is a private corporate project whose name could not be published without authorization; no new fact about its client, so docs/03 §Entities and invariants's rule holds as it is. Exercises: none (ADR-0017).
* docs/00, docs/01, docs/02, docs/03, docs/04, docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.** `pt-ninjobs-masculine` changes the article before Ninjobs on pt 00:107 and its agreement: whichever lands second edits the line as the first left it; this delivery touches only the Case A clause (decision 5), that one only the article, so the two edits compose. `early-no-forward-links` edits chapters 0 to 7 in both editions to drop pointers to distant chapters; en and pt 00:106 hold "that chapter 17 tells", a line apart from this one, and line 107 holds no pointer, so its edit and this one do not overlap; if it rewrites line 106, this delivery still edits line 107 as it then stands. The other M18 drafts in `work/` (`agent-never-unsure`, `ch02-gain-less-to-read`, `ch03-*`, `ch04-*`, `ch05-*`, `ch07-*`, `ch11-*`, `ch13-teach-the-agent`, `pt-identifiers-choice`, `kit-proposals`) touch other chapters or other lines.

**Out of scope.**

* Case B, and chapter 17's or any other chapter's telling of Case A: decision 4; the draft names the prologue's line only.
* Who would authorize or why the client keeps it private: decision 2, disclosure.
* The article before Ninjobs: `pt-ninjobs-masculine`.

**Done when.**

* [x] en and pt 00:107 read as Behaviour quotes, or as the author rewords them on approval; both editions in the same delivery.
* [x] The prologue still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: no number added.
* [x] The author's approval of the anonymized passage listed under Behaviour (docs/00 OD-3).
* [x] `make verify` green: edition parity, prose rules, width, disclosure scan, no em dash.
* [x] `make book` run; both PDF paths given to the author: by the driver, once at the end of the batch.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block: page moved here; the line's mark, staging and commit are the driver's.

**Divergences.** None from Behaviour or Contract. `make book`, the docs/06 mark and staging are the driver's, by the batch rules.

**Proof.** Both greps print line 107, one line each; `git diff -U0` shows one hunk per edition, `@@ -107 +107 @@`, and in Portuguese "A Ninjobs aparece pelo nome" unchanged; `make verify` exit 0 (build, parity, em dash, prose, width, links, disclosure scan).

**For the author's approval (docs/00 OD-3).** The only passage drawn from Case A this delivery writes, as Behaviour quotes it:

* en 00:107: "Ninjobs appears by name; Case A is a private corporate project, and its name could not be published without authorization, so it appears without its owner, its client or its business."
* pt 00:107: "A Ninjobs aparece pelo nome; o Caso A é um projeto corporativo privado, e o seu nome não poderia ser publicado sem autorização, então aparece sem o seu dono, o seu cliente ou o seu negócio."

**Delivery review.** One read-only reviewer read the diff against this page, docs/04 and docs/03: no findings. Its one suggestion, left for the author's approval and not applied: line 106 already calls Case A "a client project" in "private repositories", so 107's "a private corporate project" describes it twice in a row and repeats "private"; a reader may wonder whether "corporate" means the client's company or the author's. A rewording on approval could drop "private" or say "a client's corporate project".

**Decisions in /apply.** None beyond the page's: the wording is decision 3's, word for word.

```commit
docs(case-a-why-anonymous): the prologue says why Case A is anonymous

- 00:107: Case A is a private corporate project, not named without leave
- both editions

work/done/case-a-why-anonymous.md
```
