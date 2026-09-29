# ch15-submit-event

**Objective.** A reader following the booking from the event functions into the hook knows that the hook's `submitEvent` is `bookingEvents.ts`'s `submit` imported under another name. They also know what `shown` and `latest` hold, so they can follow the code where the two files of the client orchestrator meet.

**Behaviour.**

* The sentence before the hook's excerpt (en/15:195, pt/15:196) says the hook has a `submit` of its own, the one the view calls. For that reason it imports `bookingEvents.ts`'s `submit` as `submitEvent`.
* The hook's excerpt now starts at the hook's state and its two refs, useBooking.ts:30-36 at the tag, with the clinic's own comments. It runs on through `run`, as it does today. The code is the same in both editions, byte for byte as the tag has it, and without the outer indentation, as en/15:9 says.
* The summary after the excerpt (en/15:223, pt/15:224) says the hook passes `new Date()` to `submitEvent`, not to `submit`.
* The prose says what `shown` holds: the state last rendered, which the submit branch reads as `snapshot`. `submitStarted` and `submitEvent` both receive that snapshot. The text describes the ref without judging it and says nothing about a later change.
* The prose says what `latest` holds: a count of requests. Each call takes the next number, and an answer whose number is no longer the latest is dropped. One clause says that `back` also advances `latest`, so an answer that arrives after Back is dropped as well.
* Every bare `submit` left in chapter 15 reads unambiguously as either the hook's or the event's. en/15:371 and pt/15:372 ("`submit` returns the update with the step `booked`") mean the event's `submit`, and they read correctly once the alias is named.
* Both editions say the same.
* Finding F9 of the M4 review is settled.

**Contract.**

* Files:
  * `book/en/15-four-pieces.md`: line 195, the excerpt at 197-221, and line 223.
  * `book/pt/15-four-pieces.md`: line 196, the excerpt at 198-222, and line 224.
  * Line numbers are as of this page. `ch15-event-delivery` and `ch15-route-io`, both in flight, edit chapter 15 above these lines.
* Sources: the clinic at `book-v1/four-pieces`, file `src/features/appointments/useBooking.ts`:
  * line 18, `submit as submitEvent`;
  * lines 30-36, `state`, `latest` and `shown`, with their comments;
  * line 82, `back`'s `latest.current++`;
  * line 94, the hook's `submit`.
  * The link the excerpt already has stays. No new link and no note.
* Terms of docs/03: none new. `submitEvent`, `shown` and `latest` are code identifiers.
* Cases: none. Exercises: unchanged.

**Out of scope.**

* Replacing `shown`, and the in-flight state applied as an update. That is the later clinic line `clinic-booking-submit`. It changes useBooking only on the clinic's main branch. `book-v1/four-pieces` never moves (docs/05), so this text stays true after that line lands, and the two deliveries can land in either order. Explaining the new code belongs to whichever chapter next tags the clinic.
* `back`'s body. One clause in the prose covers it, and no excerpt is added.
* en/15:9 and the delivery that added the event functions. They belong to `ch15-event-delivery`, which is in flight and names this slug in its Out of scope.
* The route's body read. It belongs to `ch15-route-io`, which is in flight and names this slug in its Out of scope.
* Slice imports, the injection rule and the cost of a piece. Those are the later lines `slice-imports`, `ch15-injection-rule` and `ch15-piece-cost`.
* The clinic. It is not touched, and no tag moves.

**Done when.**

* [ ] Both editions changed with the same meaning. Chapter 15 opens with its value, with no filler and nothing useful cut.
* [ ] The excerpt matches `git show book-v1/four-pieces:src/features/appointments/useBooking.ts` lines 30 onward, byte for byte after removing the outer indentation.
* [ ] `grep -n "passes it to \`submit\`\|o passa a \`submit\`" book/*/15-four-pieces.md` finds nothing.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
