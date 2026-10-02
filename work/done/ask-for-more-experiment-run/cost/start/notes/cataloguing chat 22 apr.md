# Cataloguing chat — 22 Apr 2026

Rafe and Wren, in the chat, roughly 14:10–14:50. Rafe tidied it up afterwards and pasted it here because it ended in a decision about ISBNs. Some small talk removed.

---

**Rafe:** quick one. `createBook` currently takes any string as ISBN. Bex wants it validated. What do you actually see on the books at Saltgate?

**Wren:** honestly, everything. New stuff has the 13-digit ones, 978 or 979 at the front. Older books have 10-digit ones. Some have an X at the end. And the donated stuff from the 60s and 70s often has nothing at all.

**Rafe:** how are they written in CardBox?

**Wren:** however whoever typed it felt that day. With hyphens, with spaces, without. I've seen "978-0 14 ..." which is both.

**Rafe:** ok. So stripping hyphens and spaces before checking is a must.

**Wren:** yes please. Nobody's going to retype 11,000 of them.

**Rafe:** and the books with no ISBN at all — they just don't get one?

**Wren:** right. We can't make one up. They still go on the shelf and still get borrowed.

**Rafe:** good, the ISBN is already optional. Title and author are the only required bits.

---

**Rafe:** the bigger question: do we accept ISBN-10 as well as ISBN-13?

**Wren:** what's the difference for you?

**Rafe:** two check digit algorithms, the X thing, and the same book can then be in the catalogue under two different numbers. That last one is what worries me.

**Wren:** ha, yes, that already happens in the sheets. Same book twice.

**Rafe:** every ISBN-10 has an ISBN-13 equivalent (978 prefix, recalculated check digit). So we could only accept 13 and convert the old ones.

**Wren:** convert automatically?

**Rafe:** I'd rather not, for now. Accept 13 only. Old 10-digit books either go in without an ISBN, or someone converts the number by hand when cataloguing. There are free converters; it's a two-minute job per book.

**Wren:** how many old 10-digit books do we have, really... a few hundred maybe. And most of those are the donated ones that I'd enter without an ISBN anyway. Fine by me. Odile won't care as long as the book can still be lent.

**Rafe:** and the check digit gets validated, so a typo gets caught at the desk instead of sitting in the catalogue forever.

**Wren:** that'd be a first.

---

**Wren:** one thing — if the check fails, what does the librarian see?

**Rafe:** `invalid-isbn`. Same error for "wrong length", "has letters" and "check digit wrong". Want them split?

**Wren:** no. "That number's wrong, check it" is all I need.

---

## Outcome (Rafe)

- **Only ISBN-13 is accepted.** ISBN-10 is rejected with `invalid-isbn`.
- Hyphens and spaces are stripped before validation; the book stores the stripped 13 digits.
- The ISBN-13 check digit is validated (weights 1 and 3 alternating, mod 10).
- Old ISBN-10 books: entered **without an ISBN**, or with an ISBN-13 **converted by hand** by whoever catalogues it. No automatic conversion in the model.
- No ISBN is still fine (donations).

## Actions

- [x] RL — `isValidIsbn13` in features/books/book.ts; strip `[-\s]` in `createBook`
- [ ] BA — tests: hyphenated ISBN-13 ok, spaced ok, bad check digit rejected, ISBN-10 rejected, no ISBN ok
- [ ] WH (via JA) — short "how to enter old books" note for the desk
