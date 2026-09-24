---
name: analyze
description: >-
  Document an existing repository. Reads the code, writes docs/00 to 06,
  docs/adr/ and AGENTS.md describing what is there, and asks only what the
  code cannot answer. Writes no code.
---
You are documenting a repository so that every later session can act on it
without rereading it. Read `references/documents.md` first, whole: it says
what each document holds.

## Read

The README and any existing docs; the manifests (package.json, pyproject,
go.mod, *.csproj, pubspec.yaml, Cargo.toml, Gemfile, and the like); the
folder tree two levels deep; the entry points; the tests and how they run;
CI; the last fifty commit subjects; any agent rules file already there
(CLAUDE.md, AGENTS.md, .github/copilot-instructions.md, .cursorrules).

From that, infer the stack, how the code is organized, where business rules
live, how errors travel, what the verify command is, and which environments
exist. What the code says, you do not ask.

## Ask

One round, in the language the person writes in, recommendation first, the
host's question form when it has one:

* the documentation language. Default: the language the README is in;
* what the code cannot say: the product's purpose and audience in the
  person's words, when no README says it;
* the two choices of `references/documents.md` §Choices, FOCUS and git,
  presented in their own words. The default is what the code already does,
  and you say what that is;
* the first milestone: three to eight deliveries, or where to read them
  from (issues, a TODO file, a roadmap).

Everything else you decide from the code and mark as observed. Where the
code contradicts itself, the document records an open question; the person
is not asked to settle it now.

## Write

In the documentation language: docs/00 to 06 describing what exists, not
what should exist; docs/adr/ with the decisions the code already embodies
and the ones this round took, one dated paragraph each; `AGENTS.md` from the
template; `CLAUDE.md` holding the line `@AGENTS.md`; and the folder
`work/done/`. The rules live in `AGENTS.md`: what an existing `CLAUDE.md`,
`.github/copilot-instructions.md` or similar file already says moves into
it, and that file becomes the import line (or, when its host cannot
import, a one-line pointer to `AGENTS.md`), keeping below it only what
applies to that host alone. Show the diff before writing.
The numbers of the documents are fixed; the names after them are in the
documentation language.

Show the queue and stop. The next step is `/propose <slug>` for its first
line, in a fresh session. Change no code.
