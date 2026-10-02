# Lending library

A small TypeScript domain model for a lending library: books and their copies, members, librarians and loans, with loan periods, due dates, overdue loans and member suspension.

## Running the tests

Requires Node 26 or later, which runs `.ts` files directly. There are no dependencies to install.

```sh
npm test
```

or, equivalently:

```sh
node --test
```

## Question-answering agent

An agent answers the team's questions about this project, one fresh session per question. Its guide is `CLAUDE.md`, which it loads in full every session, so keep that file short.

When you add a note to `notes/`:

- add its filename to the "Notes index" in `CLAUDE.md`
- if it changes a rule, add a row to "Rules that changed"
- update the "last checked" date

If you skip this, the agent still finds the new note, but it ends its answers with "`CLAUDE.md` is out of date: …" until someone updates the file.

`qa-checks.md` lists questions with known answers, mostly ones where an old note gives the wrong answer. Ask a few after changing `CLAUDE.md` or the rules.
