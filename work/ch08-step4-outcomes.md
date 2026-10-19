# ch08-step4-outcomes

**Objective.** After chapter 8's "What an update reports" a reader knows the update's report gives every item of the setup file's step 4 one of three outcomes, nothing needed, a missing wording proposed, or a recorded project choice, and no sentence of the chapter says the report lists only what the documents lack; both editions, least change.

**Behaviour.**

* Reading the sentence after "Applying the migrations keeps the team's choices", the reader learns the report gives each item one of the three outcomes just described, and still learns it compares the documents with the current templates, never one version of the kit with another.
* Reading the paragraph on the changelog, the reader learns the rerun compares step 4's list and each item is reported, never done, with one of the three outcomes.
* The report excerpt, the three-outcome paragraph, the Key points and every other line read as they do.
* Fails if: any sentence of chapter 8 in either edition still says the report lists only what the documents lack; a sentence other than the two named below changes; the chapter says how it read before or narrates a run; the two editions differ in sense.

**Contract.**

`book/en/08-install-and-hosts.md` and `book/pt/08-install-and-hosts.md`, section "What an update reports" (pt "O que uma atualização relata"), two sentences:

* en line 93, pt line 95: "The report lists only what the documents still lack, or says there is none; it compares the documents with the current templates, never one version of the kit with another." becomes "The report gives each item one of those three outcomes; it compares the documents with the current templates, never one version of the kit with another." (pt "O relatório dá a cada item um desses três resultados; ele compara os documentos com os modelos atuais, nunca uma versão do kit com outra."). Wording is /apply's within that sense.
* en line 109, pt line 111, its last clause only: "each item is reported, never done, and the report lists only what your documents still lack." becomes "each item is reported, never done, with one of the three outcomes." (pt "cada item é relatado, nunca feito, com um dos três resultados."). The rest of the sentence stays.
* Stays: the report excerpt (en 58 to 82), the three-outcome paragraph (en 84 to 88, pt 86 to 90), line 98 ("reports the migrations first, or says there are none", true: migrations come first), the Key points (en 174 already names "a choice the project recorded is reported as that choice"), and every other line.

Line numbers are as of this page, after `m21-git-slot-default`; /apply finds each sentence by its words.

Terms of docs/03 used: migration, project choice, slot; none new. No number added, no source note, no private case. Sources cited: none new.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no visual change.

**Out of scope.**

* Any other chapter, docs/03, docs/06: no edit; the queue line is the driver's.
* O6 and O8 of `work/done/m21-review.md` (the Example slot, the excerpt naming this repository's choices): not confirmed by the author.

**Decisions from the documents.**

* The three outcomes are the kit's: `SETUP.md` step 4 ("report every migration still needed ... A divergence the project decided and recorded ... report it as such, with what the kit says, not as a migration. Each item below is reported, never done"), and the excerpt in the chapter shows all three (`None`, a proposed wording, a project choice).
* Least change: the driver and finding O7 of `work/done/m21-review.md`; the clause about comparing with the current templates stays, since it holds.
* No before/after or version in the text: AGENTS.md, the driver.

**Decisions taken alone.**

* Line 109 (pt 111) is in scope though O7 named only line 93: its last clause repeats the same claim and would contradict the paragraph this delivery fixes.
* "or says there is none" is dropped from line 93: the `None` outcome already covers a document that needs nothing, and line 98 still says the update reports when there are no migrations.
* The new sentence names no extra content of the report (installed version, next command): those are shown in the excerpt and in the following paragraphs, and the sentence is about the items only.

**Done when.**

* [ ] Both editions written, the same two sentences changed in each file, Portuguese read as Portuguese; the chapter opens as it did, no filler and nothing useful cut.
* [ ] `grep -n "only what\|só o que" book/{en,pt}/08-install-and-hosts.md` finds nothing.
* [ ] `git diff` of this delivery touches only those two lines in each chapter 8 file.
* [ ] No em dash; no "no longer", "now", "não mais", "agora" added; no narrated run.
* [ ] Delivery review as docs/05 §5 says.
* [ ] `make verify` green; `make book` builds both editions and both PDF paths are reported (the driver may run it once for the batch).
* [ ] Only this delivery's paths staged; the page moved to `work/done/` and its commit message suggested.
