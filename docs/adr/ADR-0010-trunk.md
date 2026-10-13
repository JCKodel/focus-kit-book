# ADR-0010: trunk

**Date:** 2026-09-24

## Context

A worktree per delivery would let agents write chapters in parallel, but shared files (navigation, glossary, queue) would conflict, and the author reviews every delivery alone.

## Decision

Everything happens on `main`, one delivery at a time.
The agent stages and suggests the message; the author reviews and commits.

## Consequences

The simplest history. Part IV still teaches branches and worktrees, from the other cases.

## Amendment, 2026-10-13

Since `kit-2026-10-13`, two sessions may work in one tree on free lines that touch different files (docs/05 §4): each stages only its delivery, and the author commits one delivery at a time.
The history stays one commit per delivery, and no worktree is used: two deliveries that need the same files are ordered in the queue with `· after` (`ch21-one-tree`).
