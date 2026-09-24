# ADR-0010: trunk

**Date:** 2026-09-24

## Context

A worktree per delivery would let agents write chapters in parallel, but shared files (navigation, glossary, queue) would conflict, and the author reviews every delivery alone.

## Decision

Everything happens on `main`, one delivery at a time.
The agent stages and suggests the message; the author reviews and commits.

## Consequences

The simplest history. Part IV still teaches branches and worktrees, from the other cases.
