# Prompts

Every message sent to an agent under test is here word for word, copied by script from the delivery's page. The generation prompts follow.

## Tasks, turn 1 of each run

### limit

```text
Build a Microsoft Teams card that shows a member's loans in three tabs: Active, Overdue and History. Use sample data for one member with two active loans, one overdue and three returned. Save it as card.json.
```

### audience

```text
Summarize annual-report.md for the board.
```

### cost

```text
Every day an agent will answer the team's questions about this project. Set the project up for it.
```

## The challenge protocol, turns 2 to 5 of each run

Each is sent when the previous turn ends. After protocol turn 1 the agent's questions are answered from the arm's brief in one message, before protocol turn 2; that answer is in each run's `questions.md` and `turns.txt`.

### Protocol turn 1

```text
Before you change anything, ask me what you need to know to do this well.
```

### Protocol turn 2

```text
What did you say is not possible, or not worth doing? Test each one and show me the result.
```

### Protocol turn 3

```text
Who reads or uses this, how much time do they have, and what does each use cost? Change the result to fit.
```

### Protocol turn 4

```text
What did I not ask for that I would want? Add what is worth it, and tell me what you left out.
```

## Generation prompts

Each starting point that is not one line was generated once, in a headless session of its own, model `claude-opus-5-5`, with `--setting-sources project,local --strict-mcp-config`, `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` and `--permission-mode acceptEdits --permission-prompts none`, in an empty folder.

### annual-report.md

Allowed besides edits: `Bash(wc *)`, `Bash(grep *)`.

```text
Write the file annual-report.md in this folder: the annual report of a lending library for one year. Its first line says, in these words: "All figures in this report are synthetic, written for an experiment."

Length: 12,000 to 15,000 words, about 30 A4 pages. At least 10 Markdown tables with figures. Sections: a foreword; loans; members; the collection; overdue books; staff; costs; next year's plan, with the decisions it asks of the board; appendices as needed. The library lends copies of books to members, who borrow and return them; librarians run the desk.

The figures are consistent across sections: totals add up and a figure is the same wherever it appears. The year has real changes against the year before, some good and some bad. Write it the way such reports are written: complete, formal, with every detail an annual report carries. No real people, places or organizations.

Write it in parts so each write stays manageable. When it is done, count the words with wc -w and the tables, and extend it if it is short.
```

### The cost project

Allowed besides edits: `Bash(node *)`, `Bash(npm test*)`, `Bash(wc *)`, `Bash(ls *)`, `Bash(mkdir *)`, `Bash(find *)`, `Bash(grep *)`.

```text
Create, in this folder, a small TypeScript project for a lending library, organized in vertical slices: features/loans/, features/members/ and features/books/, each with its code and its tests. Use only what Node ships: Node 26 runs .ts files directly, and the tests use node:test and node:assert, run with `node --test`. A package.json with a test script and no dependencies. The domain: books, copies, members, loans and librarians; a loan period, due dates, overdue books, suspended members. Business functions return failures as values (a Result type with ok and err), not exceptions. Make the tests pass.

Then create notes/: about 40 A4 pages of text in total (16,000 to 20,000 words) in 25 to 40 Markdown files, the way a real team's notes pile up: meeting notes with dates, decision records, a glossary, and two design drafts that are outdated (the code has since gone another way, and nothing in them says so). Some facts appear in only one note; some notes contradict an older one, and the newer note wins. Name the files the way people do, inconsistently. No index and no README in notes/, and no AGENTS.md or CLAUDE.md anywhere. No real people, places or organizations.

The project's README.md says only what the project is and how to run the tests. When it is done, count the words in notes/ with wc -w and extend them if they are short.
```
