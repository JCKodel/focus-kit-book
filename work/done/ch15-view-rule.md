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

* [x] Both editions changed with the same meaning. Chapter 15 opens with its value, with no filler and nothing useful cut.
* [x] The excerpt matches `git show book-v1/four-pieces:src/features/appointments/bookingEvents.ts` lines 107-113, byte for byte.
* [x] `grep -n "tooLateToCancel" book/*/15-four-pieces.md` finds it in the prose of both editions, not only in the view's excerpt.
* [x] Every number in the new text (the 24 hours) says where it comes from: `rules.ts`'s comment.
* [x] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author. Left unticked on purpose: in this batch the driver runs `make book` once at the end of the loop.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* Revalidated against `main` at `ec117c8`: `ch15-brief-printed` and `ch15-uncaught-pieces` had moved the paragraph to en:132 and pt:133, and the hook's clock sentence to en:64; the text was as the page quotes it. The clinic's lines (useBooking.ts:110, bookingEvents.ts:6-10 and 107-113, rules.ts:145-148, BookingView.tsx:35-49) are as the page says.
* The paragraph now says the view reads `state` and `tooLateToCancel`; a new paragraph follows the value back, hook, `bookingEvents.ts` with the excerpt and its link, `rules.ts`, in the page's order.
* Taken alone, since the batch ran without conversation: the page says "the use case the server's `cancel` also uses", but at the tag `cancel` is itself a use case in `rules.ts` (line 152) that calls `cancellationDeadline`, and `route.server.ts:194` runs it. The text says that: "the use case `cancel`, which the server's route runs when a client cancels, calls it too".
* Taken alone: the new paragraph opens by naming the view's "Forbids" ("looks like a business rule in the view"), so the reader knows why the value is followed; the Portuguese glosses the English comment in parentheses, as the chapter glosses "Book".
* "Two values" is scoped to the printed step ("In this step"), since the view also takes `days` from the hook for another step.
* `bookingEvents.ts` is now linked twice, in the new paragraph as the page asks and again at step 2 a few lines below; step 2 is outside this page's files, so it was left for the author to decide.
* The excerpt was checked against the tag by `diff`, in both editions.
* F11 is settled by this delivery; `findings.md` is a run record and is not edited, as done for F9 and F10.
* No document changed: no new term, rule or decision.
