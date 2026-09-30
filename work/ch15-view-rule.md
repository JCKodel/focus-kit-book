# ch15-view-rule

**Objective.** A reader of the booking view's excerpt in chapter 15 knows where `tooLateToCancel` comes from: the rule is `cancellationDeadline` in `rules.ts`, the use case the client imports, and the view receives only a boolean. So they can check the excerpt against the view's "Forbids" (business rules, data access) themselves.

**Behaviour.**

* The paragraph after the view's excerpt (en/15:126, pt/15:127) no longer says the view renders only what `state` holds: it names `tooLateToCancel` as the other value the hook returns, next to `state`, which the view only reads.
* Right after it, the text follows `tooLateToCancel` back to the rule, in this order, and says nothing the code does not show:
  * the hook computes it on every render as `tooLateToCancel(state, new Date())`, reading the clock as en/15:58 says the hook does (useBooking.ts:110);
  * the function of that name in `bookingEvents.ts`, the client orchestrator, is true only on the form step when the appointment's cancellation deadline is already before `now` (bookingEvents.ts:107-113);
  * the deadline itself, 24 hours before the start, is `cancellationDeadline` in `rules.ts`, the use case the server's `cancel` also uses (rules.ts:145-149);
  * so the rule is written once, in the use case, and the view holds none: it shows or hides a line of `strings.ts`.
* A short excerpt of bookingEvents.ts:107-113 is printed, byte for byte as the tag has it, with the clinic's comment "Display only: the server does not refuse such a booking.", and one sentence says what that comment means for the reader: the line warns the client, it refuses nothing, and cancelling after the deadline is refused by the server.
* The text ties this to the docs/01 quote already at en/15:66 ("the client imports the same use case only to decide what to show"): `tooLateToCancel` is one such case, in the booking form.
* Both editions say the same.
* Finding F11 of the M4.1 review is settled.

**Contract.**

* Files:
  * `book/en/15-four-pieces.md`: line 126 and the lines added after it, before "**2. The client orchestrator.**" (line 128).
  * `book/pt/15-four-pieces.md`: line 127 and the lines added after it, before "**2. O orquestrador do cliente.**" (line 129).
  * Line numbers are as of this page. `ch15-brief-printed` (around en/15:18) and `ch15-uncaught-pieces` may move these lines; `ch15-shape-cost` edits the key points near the end. Anchor on the text, not the number.
* Sources, the clinic at `book-v1/four-pieces`, `src/features/appointments/`:
  * `useBooking.ts:110`, `tooLateToCancel: tooLateToCancel(state, new Date())`;
  * `bookingEvents.ts:6-10`, the import of `cancellationDeadline` from `./rules.ts`, and `bookingEvents.ts:107-113`, the comment and the function (the excerpt);
  * `rules.ts:145-149`, the comment "24 hours before the appointment starts." and `cancellationDeadline`;
  * `BookingView.tsx:35-49`, where the view takes `tooLateToCancel` from `useBooking()`.
  * The excerpt gets a link to `bookingEvents.ts` at the tag, in the form of the chapter's other links. No note.
* Terms of docs/03: none new. `tooLateToCancel` and `cancellationDeadline` are code identifiers; "use case", "orchestrator" and "view" are the chapter's.
* Cases: none. Exercises: unchanged.

**Out of scope.**

* The view's other unexplained names (`step`, `busy`, `backButton`, `summary`, `errorStrings`): F11 was confirmed narrowed to `tooLateToCancel`, the one that bears on "Forbids".
* Whether comparing the deadline with `now` in `bookingEvents.ts` is "deciding a rule" under the orchestrator's "Forbids": the text states what the code does and adds no ruling; the review raised no finding on it.
* The clinic's code: not touched, no tag moves. Moving the comparison into `rules.ts` would be a clinic line, not this chapter's.
* The printed brief, the uncaught pieces and the key point on when a piece is written: `ch15-brief-printed`, `ch15-uncaught-pieces`, `ch15-shape-cost`.

**Done when.**

* [ ] Both editions changed with the same meaning. Chapter 15 opens with its value, with no filler and nothing useful cut.
* [ ] The excerpt matches `git show book-v1/four-pieces:src/features/appointments/bookingEvents.ts` lines 107-113, byte for byte.
* [ ] `grep -n "tooLateToCancel" book/*/15-four-pieces.md` finds it in the prose of both editions, not only in the view's excerpt.
* [ ] Every number in the new text (the 24 hours) says where it comes from: `rules.ts`'s comment.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
