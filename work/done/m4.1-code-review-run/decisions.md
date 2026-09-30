# Requests

Each request sent to the review's session, word for word, in order.

## Turn 1, the review

```
/code-review high a3e2470...6edc9ad
```

## Turn 2, the decisions and the lines

```
My decisions on the seven findings:

1. Confirmed. The time inputs stay enabled while a save is in flight, so a time typed meanwhile is shown but not sent, and a successful save closes the editor and drops it without a word.
2. Confirmed. The name and phone fields stay enabled while a booking is in flight, so the form can show details that were not booked; one change settles it with finding 1.
3. Rejected. The late reload after ProfessionalNotFound on the editor's first load is code M4 added, with the same behaviour before M4.1 in hoursRefused, so it is outside this review's range.
4. Confirmed. WeeklyHoursAnswer.report now allows "saving", which only the hook reports, so a load or save that answered it would leave the section busy for good.
5. Rejected. docs/01's shape 4 writes the check's answer onto the current state on purpose, and no click reaches a current state without the refused period, since the update is published in the same event.
6. Rejected. The M4.1 line asked for one tested professionals event, and splitting it moves the branch from the answer's type to the report without removing it; docs/01 records the shape as 7.
7. Rejected. docs/01 names retryOf and what it returns under shape 5, the only shape that uses it.

Fix none of them. For the confirmed findings, write [ ] lines in ../focus-kit-book/docs/06-Queue.md, inside M4.2's block, just before m4.2-review, in this shape:

[ ] clinic-<slug>  <what this project's code does afterwards>, by a recorded run

aligned as the lines around it. Findings 1 and 2 are settled by one change and share one line; finding 4 gets its own. A finding that a line of this project's milestone 1.1 in docs/06 covers still gets its line, which names that line and what the finding adds; this project's docs/06 is not touched. An M4.2 line that already covers a finding gets no new line, only words if the finding adds something. Add to M4.2's paragraph one clause saying what this project's code does once those lines are done.

Write in English, with no em dash. Edit nothing else, in either repository. Stage with exactly git -C ../focus-kit-book add docs/06-Queue.md, then check with git -C ../focus-kit-book diff --cached and git -C ../focus-kit-book status --short, and say where you put each line and why, and which findings, if any, you found already queued.
```

## Turn 3, a correction

```
In clinic-hours-answer, say that load answers only a refusal or nothing and save only "saved", "failed" or a refusal; edit nothing else, stage and check as before.
```
