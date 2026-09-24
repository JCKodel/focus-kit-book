# ADR-0001: a website and PDF/EPUB from one source, no wiki

**Date:** 2026-09-24

## Context

The book could live as a GitHub wiki in the focus-kit repository, as a GitHub Pages site, as a PDF, or several of these.
A wiki is a second git repository with no pull requests, no build and no PDF.
Two copies of the same text drift: in Case A, the per-host copies of the commands drifted apart within days.

## Decision

This repository is the only source.
It builds a website on GitHub Pages and PDF and EPUB files, free, published on books.kodel.com.br.
focus-kit's README links to the website; there is no wiki, neither written by hand nor mirrored.

## Consequences

One text to maintain and review.
Readers of the focus-kit repository reach the book through one link.
