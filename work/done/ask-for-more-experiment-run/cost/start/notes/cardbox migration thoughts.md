# CardBox migration — thoughts

Marek + Juno, started 2026-07-28, conclusion added 2026-08-18.

Context: Odile sent the CardBox column headers + sample rows back in January. With the model fairly settled, Juno asked whether we should plan an import, so that "go live" (whenever) doesn't start from an empty library. Marek volunteered to look at the data since a lot of it is dates.

---

## What's in CardBox (MS)

Three spreadsheets and a box of cards.

**Catalogue sheet** — ~11k rows. Title, author, sometimes an ISBN, sometimes a shelf mark in the ISBN column. Copies are rows, not a separate thing: the same title appears three times with a "copy" column of 1/2/3 — or "a/b", or blank. Some rows are marked "gone", "lost?", "binder", "WD" (withdrawn, we think).

**Members sheet** — ~1,900 active (plus a few hundred lapsed nobody removed). Name, address, phone, *sometimes* email. Card colour. A "notes" column with things like "do not lend art books".

**Loans sheet ("who has what")** — typed up from the cards at end of day, usually. Dates in at least four formats: `14/3/26`, `14.03.2026`, `March 14`, and "Thurs". Loan period was 14 days then, so due dates there are on the old rule. No renewal count — a renewal is a second stamp on the card, maybe a new row, maybe not.

**Cards** — the truth. Not machine-readable.

## What an import would need

- Book vs Copy split from the catalogue sheet. Doable-ish; dedupe by title+author, guess copies.
- Copy ids — CardBox has no barcodes on most stock. Every copy would need a `C-####` id *and* a sticker anyway.
- Members: email is required in our model, missing for maybe a third. Would need to invent placeholders or chase people.
- Loans: parse four date formats, decide which year "Thurs" means, reconcile against the cards, convert old 14-day due dates (keep or recompute?), guess renewals.
- Overdue/suspension state: CardBox doesn't record suspensions at all; it's in Wren's head and a sticky note.

## Juno's take

The catalogue and members would be nice. The loans are the scary bit and also the bit that matters most on day one — if the system says someone has nothing out and they've got five books, the new overdue/limit rules are meaningless.

## Marek's take

Any importer for the loans sheet is a pile of heuristics we'd have to test against data we don't trust, to produce records we'd then have to check by hand against the cards anyway. "If we're checking every row against the cards, we're re-entering them with extra steps."

## Talked to Odile (2026-08-11, JA)

Odile's view: there are roughly 600–700 active loans at any time. The desk could re-enter those over a week or two as people come in, or in a couple of quiet afternoons from the cards. Catalogue and members get re-entered as they're touched anyway — "we've wanted to clean that list for ten years". Wren is up for it, conditional on biscuits.

## Decision — 2026-08-18 (JA, MS, TO agreed; Odile ok'd)

**We are not migrating CardBox data.**

- No importer, no parsing scripts, no mapping tables.
- When a system eventually runs on this model, **the library re-enters active loans by hand** from the cards. Copies and members are created as they're needed (a copy gets its id + sticker the first time it crosses the desk).
- CardBox stays readable as an archive. Nobody deletes the sheets.
- The model doesn't need any "legacy" fields (old card number, CardBox row id). Not adding them.

## Loose ends

- [ ] JA — note for September planning: re-entry needs *some* UI, even a crude one. Ties to the "what's next" discussion.
- [ ] MS — one-page "how to read a CardBox loan card" for whoever does the re-entry (dates especially)
- [ ] TO — glossary: CardBox entry should say we don't import from it
- [ ] Odile — decide whether old 14-day loans on cards get the 21-day rule on re-entry (probably: enter the actual due date from the card)
