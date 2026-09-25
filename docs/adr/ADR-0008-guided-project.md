# ADR-0008: the guided project is a TypeScript scheduling app in its own repository

**Date:** 2026-09-24

## Context

The earlier FOCUS manuscript showed code in ten languages and could not keep them consistent.
Every artifact the book shows must be real and checkable.

## Decision

A neighbourhood clinic or salon scheduling app runs through the book, built greenfield with `/brainstorm`.
It has two sides (customer and owner) and real rules (overlapping slots, cancellation, a professional's absence).
It is written in TypeScript, as a React PWA over a local SQLite database, with no paid service.
It lives in its own public repository with a tag per chapter; the book quotes tagged files.
FOCUS examples use the same app.

## Consequences

Readers of other languages follow the ideas, not the syntax.
The name and repository are chosen in `guided-project-repo` (docs/00 OD-2).

## Amendment, 2026-09-25

* The name is `focus-kit-clinic`, the repository `JCKodel/focus-kit-clinic`, public, on `main`.
* A clinic, not a salon: chapter 3's run already used one.
* Licenses as ADR-0003, unchanged: code, scripts and configuration AGPL-3.0-only; `docs/`, `work/` and the README CC BY-SA 4.0; focus-kit's installed command files under focus-kit's terms.
* English only: identifiers, documents and README. The Portuguese edition shows its prose artifacts translated (docs/04 §Evidence); there is no Portuguese copy of the repository.
* The tag rule: `book-v1/start` is the empty starting point, before chapter 5. A chapter that changes the project ends with the annotated tag `book-v1/<chapter-slug>` on the commit it quotes; a chapter that changes nothing has no tag, and its exercises start from the latest earlier tag. A published tag never moves; a second edition tags `book-v2/*`.
