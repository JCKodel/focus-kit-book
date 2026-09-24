# ADR-0002: MkDocs Material for the site, pandoc for PDF and EPUB

**Date:** 2026-09-24

## Context

The website needs two languages, search and diagrams.
The author already builds books with pandoc, weasyprint and mermaid-cli, installed on their machine.
Quarto would build all three outputs with one tool, but its multilingual site support is weaker.

## Decision

MkDocs Material with the static i18n plugin builds the website.
pandoc, weasyprint and mermaid-cli build PDF and EPUB from the same Markdown.
The pipeline is written anew here, without the private server steps of earlier builds.

## Consequences

Two tools read the same source, so the Markdown avoids features only one of them understands.
