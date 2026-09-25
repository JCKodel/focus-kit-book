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

## Amendment, 2026-09-25

* The stack is narrowed to a TypeScript full-stack web app: TypeScript at least 80% of the code, front end and back end in one repository, a database that runs locally (docs/00 Non-goals, ADR-0008). Size is 5,000 to 20,000 TypeScript code lines, tests excluded.
* Nothing was loosened: three candidates met every criterion (delivery `brownfield-research`).
* The chosen project is CLAHub, upstream <https://github.com/DamageLabs/clahub>, at `9d1e666e1d30f271aea9640393229a7cbfbd1b62` (2026-04-13).
* The fork is `JCKodel/clahub`; the tag `book-v1` on that SHA is the only freeze. The fork's branches may move; the tag does not.
