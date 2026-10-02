# Glossary

Shared vocabulary for the Hollowmere Lending Library model. Started by Bex in February because "book" meant three different things. Everyone edits; initial your additions.

Rule of thumb: words in test names belong here, with the same meaning. If code and this page disagree, the code wins.

Last tidy-up: TO, early September.

---

## Catalogue

**Book**
A title in the catalogue: title, author, optionally an ISBN. The *idea* of the thing: "Do we have *The Salt Orchard*?" is about a book. Title and author are required (`title-required`, `author-required`). Lives in `features/books`. (BA)

**Copy**
A physical item on a shelf at Saltgate. One book can have many copies. Copies get lent, withdrawn and returned — never books. Each copy has a status (see below). When Odile says "the book is out" that nearly always means a copy. (BA, after the January discovery session)

**Copy id / barcode**
The identifier on a copy, like `C-0001`. Librarians say "barcode" (the sticker number); same thing. Required when adding a copy (`copy-id-required`). Not CardBox card numbers, a different scheme. (RL; barcode note added by Wren via JA)

**Available**
Copy status: on the shelf (or should be) and can be checked out. A newly added copy is available. `availableCopies` lists a book's available copies. (BA)

**On loan**
Copy status (`on-loan` in code): lent to a member under an active loan. Can't be lent again (`copy-not-available`) or withdrawn (`copy-on-loan`) until it comes back. (BA)

**Withdrawn**
Copy status: out of circulation for good — damaged, lost, worn out, weeded. A librarian withdraws it; we record who and when. Can't be lent (`copy-withdrawn`) or withdrawn twice (`already-withdrawn`). No "un-withdraw"; if one turns up, add it as a new copy. (RL)

## People

**Member**
Someone registered to borrow: name and email (normalised to lower case; `invalid-email` if it doesn't look like one). May have a suspension. Children are members too, same rules — different colour card in CardBox, nothing different here. (BA)

**Librarian**
Library staff, modelled as just an id and a name. Librarians issue loans (`issuedBy` on the loan), withdraw copies, and suspend or reinstate members. Separate from members; see `librarians-vs-members.md`. (TO)

**Head librarian**
Odile Fenwick. Our client; decides how lending works at Saltgate. The model has *no* head-librarian role — any librarian can do anything a librarian can. Odile confirmed explicitly, not wanting to be a reinstatement bottleneck. (JA)

## Lending

**Loan**
The record of one copy lent to one member: copy id, member id, issuing librarian, date lent (`loanedOn`), due date (`dueOn`), renewal count, and date returned (`returnedOn`, empty while out). One loan = one copy. Five books at the desk = five loans. (RL)

**Active loan**
A loan not yet returned (`returnedOn` not set). Only active loans count towards the loan limit or can be overdue. Returned loans stay as history. (RL)

**Checkout**
Lending a copy to a member, i.e. creating a loan (`checkOut`). Refused, in this order, if: the member is suspended (`member-suspended`); has any overdue loan (`member-has-overdue-loans`); already has 5 active loans (`loan-limit-reached`); the copy is withdrawn (`copy-withdrawn`); or already on loan (`copy-not-available`). On success the copy becomes on loan. (RL; overdue rule added after the 16 June meeting — TO)

**Loan period**
21 days, for the due date at checkout and for renewals. Was 14 in CardBox days; changed in spring after Odile and Wren agreed three weeks matched what people actually did. Constant `LOAN_PERIOD_DAYS`. (MS)

**Loan limit**
At most 5 active loans per member (`MAX_ACTIVE_LOANS`). Other members' loans and returned loans don't count. (RL)

**Due date**
The calendar day a loan should be back by (`dueOn`): checkout date + loan period. A plain calendar date, see *Dates* below. (MS)

**Overdue**
An active loan whose due date has passed. Can't be renewed (`loan-overdue`), blocks new checkouts for that member, and can lead to suspension. A returned loan is never overdue, however late it came back. (MS)

**Days overdue**
How many days past the due date an active loan is; 0 if not overdue (or returned). The number the suspension rule looks at. (MS)

**Renewal**
Extending an active loan by another loan period without the copy coming back. Max 2 per loan (`renewal-limit-reached`). Not allowed when the loan is overdue (`loan-overdue`) or the member suspended (`member-suspended`). (RL)

**Return**
The copy comes back: the loan gets a `returnedOn` date and the copy becomes available. Always allowed — late, suspended, whatever. We want the books back. Only failures: returning twice (`already-returned`) or scanning the wrong copy (`copy-mismatch`). (BA)

## Suspension

**Suspension**
A block on a member: can't check out or renew, can still return. Recorded with a reason, date (`since`), and the librarian who did it (`by`). A member is suspended once any loan is **more than 14 days** overdue — 14 exactly is not enough, 15 is. Not automatic; a librarian runs `applySuspensions` (in practice Wren, Monday mornings), which suspends everyone who qualifies and records that librarian. A librarian can also suspend by hand with a reason (e.g. lost several books). (TO, MS)

**Reinstatement / lifting a suspension**
Removing a suspension (`liftSuspension`, using `reinstateMember` underneath). Any librarian can do it, but only once the member has nothing overdue; otherwise `still-has-overdue-loans`. Lifting for someone not suspended gives `not-suspended`. "Lifting" and "reinstating" are the same; Odile says reinstating, the code says both. (BA)

**Fines**
There aren't any. "Likely" at kickoff, dropped when the council decided against them. Listed so nobody adds them back. (JA)

## Code words

**Result**
How every operation reports success or failure: `{ ok: true, value }` or `{ ok: false, error }`, built with `ok()` and `err()` from `shared/result.ts`. Business failures (limit reached, member suspended…) are *never* thrown — they're ordinary return values. Exceptions are for actual bugs. (TO)

**Error code**
The `error` in a failed Result. Always a kebab-case string literal, e.g. `loan-limit-reached`, written so a librarian could read it out loud and roughly understand it. (TO)

**Slice**
A folder under `features/` owning one area end to end: `books`, `members`, `loans`, with code and tests together. Non-library shared bits live in `shared/` (`result.ts`, `dates.ts`). Suspension logic sits in `loans` because it depends on loans; the member record just holds the suspension. (TO)

**Dates / calendar date**
`"YYYY-MM-DD"` strings. No times, no time zones; arithmetic in UTC so a day is always a day. Helpers: `addDays`, `daysBetween`, `isCalendarDate`. (MS — "please do not put a `Date` object in a loan")

## Places and old things

**Saltgate branch**
The Hollowmere branch we're building this for; so far the only one in scope. Where the clanking radiator is. (JA)

**CardBox**
The library's current system: paper loan cards plus three spreadsheets (catalogue, members, "who has what"). The cards are the truth, the spreadsheets are a rumour (Odile). We don't import from it — see `cardbox migration thoughts.md`. (JA)
