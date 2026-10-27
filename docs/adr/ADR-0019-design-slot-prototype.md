# ADR-0019: the Design slot is prototype

**Date:** 2026-10-26

## Context

focus-kit 2026.10.25 adds a Design slot to docs/05 §5: where a screen's reference comes from, and a page with a screen and no reference is not `[>]` unless the slot says prototype.
The book has no screen of its own design: the site's look is MkDocs Material's theme (docs/01), a toolchain delivery that changes what the site shows is proved by screenshots (docs/05 §5, Proof of a screen), and a chapter has no screen.
No document settled which of the slot's forms the book takes.

## Decision

The Design slot reads: prototype, no reference, by choice.
The agent chose it during the kit migration on 2026-10-26, applied directly at the author's request outside /propose and /apply (`kit-2026-10-25`), as the form that keeps how the book already worked; the author may revisit it.

## Consequences

No delivery waits for a reference or a design delivery before `[>]`.
A toolchain delivery that changes the site's look still proves it with the screenshots of Proof of a screen.
Should the book ever design a screen of its own, this ADR is amended and the slot names where the reference is kept.
