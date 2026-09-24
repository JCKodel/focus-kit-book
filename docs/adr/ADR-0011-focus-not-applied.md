# ADR-0011: FOCUS does not apply to this repository

**Date:** 2026-09-24

## Context

The repository holds prose and a few build scripts; there is no product code.

## Decision

Neither FOCUS nor its two principles are applied here.
Scripts follow docs/01 §How errors travel: each check prints `file:line: rule: message` and exits non-zero.

## Consequences

The book presents this repository as the example of the method without the architecture.
