# Requests

Each request sent to the review's session, word for word, in order.

## Turn 1, the review

```
/code-review high c54d011...e6653b5
```

## Turn 2, the decisions and the lines

```
My decisions on the nine findings:

1. Confirmed. submit publishes a whole state taken from the last rendered state, against docs/01 and the delivery's own choice of an update (current) => State; no click reaches it today, but the code breaks the rule it states.
2. Confirmed. save publishes saveStarted(state).state, a whole state from the render closure, against the same rule.
3. Confirmed. forward and the saving report stay in useWeeklyHours with no test, against the delivery's choice that every event moves so that no logic stays in the hook untested.
4. Confirmed. docs/01 gives one shape for an event with a call, while the booking's next event, the weekly hours' { update, report } and { state, send }, and the remembered list's plain functions are written only in work/done.
5. Confirmed. The update type is declared in seven files and the { state, send } starter twice, with no first occurrence named, against the abstraction rule of AGENTS.md.
6. Confirmed. The shown ref, written during render, exists only so that submit keeps an empty dependency list; it goes with finding 1.
7. Confirmed. WeeklyHoursReport, forward and the four callbacks of HoursSection say the same thing three times, and the comment is copied; it goes with finding 3.
8. Rejected. The delivery recorded the late NotSignedIn on purpose, a person's Cancel cannot land between the report and its update, and the repositories answer with a Result, so nothing rejects short of a bug, which this project lets throw.
9. Rejected. docs/04 tests an orchestrator's events without a DOM, so the hook's run is outside that level; the overwrite itself is finding 1's line.

Fix none of them. For the confirmed findings, write [ ] lines in ../focus-kit-book/docs/06-Queue.md, inside M4.1's block, just before m4.1-review, in this shape:

[ ] clinic-<slug>  <what this project's code does afterwards>, by a recorded run

as clinic-orchestrator-tests is written in M4: a delivery of the book that changes this project, with no chapter and no tag. One line per confirmed finding, except that findings 1 and 6 change the same lines of useBooking.ts, and findings 3 and 7 the same report path: each pair is one line. A finding that a line of this project's milestone 1.1 in docs/06 covers still gets its line, which names that line and what the finding adds; this project's docs/06 is not touched. An M4.1 line that already covers a finding gets no new line, only words if the finding adds something. Add to M4.1's paragraph one clause saying what this project's code does once those lines are done.

Write in English, with no em dash. Edit nothing else, in either repository. Stage with exactly git -C ../focus-kit-book add docs/06-Queue.md, then check with git -C ../focus-kit-book diff --cached and git -C ../focus-kit-book status --short, and say where you put each line and why, and which findings, if any, you found already queued.
```
