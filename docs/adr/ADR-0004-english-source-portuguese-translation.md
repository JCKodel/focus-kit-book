# ADR-0004: English is the source, Portuguese the translation; documents in English

**Date:** 2026-09-24

## Context

focus-kit is published in English with a Portuguese README, and the book follows it.
The author talks in Portuguese; contributors may come from anywhere.

## Decision

The English edition is the source; the Portuguese edition (Brazilian) is its translation, and wins nothing when they diverge.
Every delivery that changes one edition changes the other.
The process documents, pages, ADRs and commit messages are in English.

## Consequences

Parity is checked mechanically, by file name and heading structure.
A chapter costs two writings; the terms of docs/03 keep the translation consistent.
