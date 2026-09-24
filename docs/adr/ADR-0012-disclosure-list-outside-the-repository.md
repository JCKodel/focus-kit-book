# ADR-0012: the disclosure list lives outside the repository

**Date:** 2026-09-24

## Context

The book draws on private projects.
A scan needs the list of terms that must not appear, but that list is itself made of those terms, so committing it would publish them.

## Decision

The list is a local file, `~/.config/focus-kit-book/denylist.txt`, or the path in `FKB_DENYLIST`.
In Actions its content comes from the secret `DISCLOSURE_DENYLIST`.
`make verify` fails when a listed term appears anywhere in the repository.
Private case sources are never linked, named or pathed in this repository, its pages or its commits.

## Consequences

A contributor without the list runs every check but the scan; Actions runs it on every push.
Anonymization is still judged by the author (docs/00 OD-3); the scan only catches what is listed.
