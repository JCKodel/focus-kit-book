# ch02-gain-less-to-read

**Objective.** A reader of chapter 2 can say, in plain words, why the method writes less: the person has to read everything that is written before the code, attention does not grow with the pile, so the less there is to read, the more attention each part gets. Both editions. From the author's reading of the book on 2026-10-18: chapter 2's gain "does not make explicit that focus-kit's gain is writing less, because the person *has* to read what is written, and the less there is to read, the more attention each part gets. [...] the book describes it well but never says it outright. Write for a reader who will not infer it: say it plainly."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *In the gain section only, at its head.* The new sentences open `## What the team gains` (pt `## O que o time ganha`), before the Ninjobs pair, so the gain is said before its evidence. The body already says "Every one of those files is something a person reviews" (en 02:50) and "read and reviewed in one sitting" (en 02:60); they stay as they are and the gain does not repeat them, it draws the conclusion they leave implicit. Source: docs/04 §Writing the book, **One gain** (the gain said once, in its section), the draft.
2. *The chain in steps, nothing left to infer.* The section says, each in its own short sentence: the person must read everything written before the code, because a decision nobody read is a decision nobody checked; a person's attention does not grow with the pile; so less written is more attention on each part; that is why the method writes one page per feature and not a folder. Source: the draft ("say it plainly"), the author's rule to write for a reader less sharp than average.
3. *No new number, no new source.* The attention claim is reasoning the reader checks against the chapter's own counts, not a measurement; docs/04 §A gain per chapter allows the gain alone, and the section's one pair (37,228 lines of spec for four screens, then 93 pages of 22,650 lines in all) stays its number. A study on review and attention would bring a second number and a source the /propose session did not read. Source: docs/04 (lines on the gain's one number or pair, **A gain per chapter**).
4. *Key points unchanged.* A key point says what the reader does, not what is gained; key point 4 already says the lighter page is paid for with documents. Source: docs/04 §Writing the book, **One gain**.
5. *Opening sentence unchanged.* "Say where the cost of writing one decision in many places begins" (en 02:4) already holds the ability; the gain explains why that cost matters. The author can add a clause to the opening in review if he wants the attention named there too. Source: ADR-0015 (the chapter opens with what the reader can do), en 02:4.
6. *Chapter 3 keeps its own "less to read".* en 03:254 says "Less to read, less to review and less to keep true" about code, files and checks, with its own evidence (29 checks that never caught an error); chapter 2 says the attention cause once, for specs, and chapter 3 is not changed. Source: docs/04 (one fact said once), en 03:254.
7. *Not a quality claim.* The gain is about the person's attention in review, not about which tool builds better software, which en 02:61 says the counts do not show. Source: en 02:61, docs/04 §Evidence.
8. No new docs/03 term, no new queue line, no split.

**Behaviour.**

* The reader of chapter 2, in either edition, reads at the head of the gain section, before the Ninjobs pair:
  * the person has to read everything the tool writes before the code, since what nobody read nobody checked;
  * attention does not grow with the number of lines; the more there is to read, the less each part gets;
  * so writing less is the gain: one page per feature gets read whole and with attention, a folder gets skimmed;
  * this is why focus-kit writes one page, and the rest of the section shows what that meant on Ninjobs.
* The sentence that opens the section today ("One page per feature, instead of one folder per feature, is what the team reads, reviews and keeps true", en 02:65) is kept, merged or reworded by /apply so the section says the gain once, not twice.
* The rest of the section (en 02:66-68, pt 02:66-68), its numbers and its pointer to chapter 6 are unchanged.
* The Portuguese edition says the same in the same place, with the chapter's terms ("página", "entrega", "especificação").
* Fails: a number added without a source; the claim stated as a measured finding or as a claim on software quality; the body's lines 50 or 60 restated; a key point changed; a new mention of Ninjobs; any change outside the gain section of chapter 2 in both editions; an em dash; a run narrated.

**Contract.**

* Files: `book/en/02-spec-driven.md`, `book/pt/02-spec-driven.md`; in each, `## What the team gains` (pt `## O que o time ganha`) only.
* Terms of docs/03: none new; `page` and `delivery` as docs/03 has them. Sources: none added or removed. Cases: Ninjobs as the section already tells it, no new fact; no Case A or Case B passage. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply; no new queue line.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.**

* `early-no-forward-links` edits en/pt 02:20 and 02:59, in the body; gain sections keep their pointers, so en/pt 02:67's link to chapter 6 stays. No shared hunk; it applies after this line (its decision 8).
* `pt-ninjobs-masculine` edits pt 02:66 ("na Ninjobs" to "no Ninjobs"), inside the same section. This delivery adds no Ninjobs mention and leaves pt 02:66-68 as it finds them; whichever lands second reads the other's chapter 2 before editing.
* The other M18 lines touch other chapters, the prologue and docs/04.

**Out of scope.**

* The chapter's body, opening and key points: decisions 1, 4 and 5.
* Chapter 3's "less to read": decision 6.
* A study on review and attention: decision 3.

**Done when.**

* [ ] Both editions written: the gain section as Behaviour says.
* [ ] Chapter 2 still opens with its value, keeps its gain said once, no filler and nothing useful cut.
* [ ] Every number sourced: none added.
* [ ] `make verify` green: edition parity, prose rules, width, disclosure scan, no em dash.
* [ ] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [ ] `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.
