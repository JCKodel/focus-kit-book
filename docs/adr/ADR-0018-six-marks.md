# ADR-0018: six marks

**Date:** 2026-10-05

## Context

Case A mirrored its queue, one way, to a kanban board its project manager followed, and the board showed two errors of the three marks.
A mark changed when a command ended, so a delivery reached Doing only once `/propose` had written its page, while the talk that defined it showed as To Do.
And a line blocked on the client's answers had no mark of its own: five such lines sat in Doing and read as work nobody had started; the project added `[?]` by hand.
This book had rejected `[?]` for itself (ADR-0013), on the ground that none of its lines waits on a person.
The error was not Case A's alone, so focus-kit took both answers in its version 2026.10.05: a mark for each moment the work changes, `[~]` being defined and `[*]` being built, and `[?]` for a line that waits, with its reason at the end of the line.

## Decision

The book follows the kit's six marks, `[ ]`, `[~]`, `[>]`, `[*]`, `[x]`, `[?]`, in its own queue and in docs/05 §4, and installs the kit 2026.10.05 for every host.

## Consequences

Chapter 16, "The queue while it happens", teaches the six marks; chapters 16 to 25 become 17 to 26 (ADR-0017, amendment).
Chapter 18, the governor, tells how a mark moved from one project to the kit; chapter 22 keeps question deliveries as Case A's customization and no longer calls `[?]` Case A's alone.
ADR-0013 is superseded.
