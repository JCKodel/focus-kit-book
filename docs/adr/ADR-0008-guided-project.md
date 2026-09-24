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
