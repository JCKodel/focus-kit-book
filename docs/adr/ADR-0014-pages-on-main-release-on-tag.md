# ADR-0014: the site follows main; PDF and EPUB follow tags

**Date:** 2026-09-24

## Decision

Actions publishes the website on every push to `main`.
Actions builds a GitHub Release with PDF and EPUB in both editions on every `v*` tag.
Only the author pushes and tags, so the author's commit is the publish gate; the agent never publishes.
Unfinished chapters carry a draft marker on the site.
The author uploads the Release files to books.kodel.com.br.

## Consequences

The site is always current; downloadable editions are versions.
