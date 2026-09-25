# ADR-0008: Every time is the clinic's local time

**2026-09-25 · decided in /analyze.** Context: one clinic in one place. Decision: every time is the clinic's local time; there is no time-zone handling. Consequences: `startsAt` is a `Date`, an absolute instant, so it reads correctly only when the process runs in the clinic's time zone; how the code guarantees that is an open decision in docs/00.
