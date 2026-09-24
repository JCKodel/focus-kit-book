# ADR-0009: the brownfield project is chosen by a research delivery

**Date:** 2026-09-24

## Context

`/analyze` needs an existing codebase to be taught honestly, and a real one convinces more than an invented one.
A live upstream moves, and a chapter built on it would stop being reproducible.

## Decision

`brownfield-research` compares three to five open-source candidates on: permissive license, 5,000 to 20,000 lines, a common stack, existing tests, no paid services, and open issues that make natural next deliveries.
The author picks one (docs/00 OD-1); it is forked and frozen at a tag the book cites.

## Consequences

The chapter stays reproducible; updating it is a deliberate new tag.
