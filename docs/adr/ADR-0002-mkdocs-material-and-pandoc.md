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

## Amendment, 2026-09-25

Mermaid and mermaid-cli are removed from the PDF and EPUB pipeline (delivery `pdf-epub`): the book has no diagram yet, and how diagrams are drawn is decided by the first chapter that has one, on a real diagram.
pandoc and weasyprint build PDF and EPUB, with the fonts of the PDF kept in the repository (`pandoc/fonts/`).

## Amendment, 2026-09-25 (how-agents-see)

The book's first diagram, in chapter 2, decides how diagrams are drawn: SVG written by hand, one file per edition in `book/assets/`, with an opaque light background.
No tool is added: MkDocs, pandoc with weasyprint, and EPUB readers show SVG as they are.
Mermaid is not brought back, since it would put mermaid-cli and a browser into the build; a generator is not added either, since one diagram does not justify it.
