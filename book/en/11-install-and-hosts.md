# 11. Install, and the hosts

After this chapter you can install focus-kit in a repository with one sentence to your coding agent, update it with the same sentence, knowing what the update writes and what it only reports to you, and invoke its commands in the host you use.
You can also say why the method does not depend on the host.

## The problem

A method tied to one tool lasts as long as the team keeps that tool, and a team rarely agrees on one.
One person works in Claude Code, another in Copilot inside their editor, a third tries Codex, and each host, the program that runs the coding agent, looks for its rules and its commands in folders of its own.
The kit has to open ready in all of them, and install without asking anyone to install anything.

## Install

Open your coding agent at the root of the repository and say:

```
Read https://github.com/JCKodel/focus-kit/blob/main/SETUP.md and follow its section 1.
```

That file is the kit's setup file: one file of instructions that the agent reads and turns into the kit's files, the four commands and a few small pointer files for the hosts that need them.
Nothing is installed on your machine; the agent writes files into the repository, and that is all.
Your host may ask before it downloads the file and before it writes into its own folder inside the repository, `.claude/` in Claude Code: approve both.

The setup file tells the agent to copy every file byte for byte.
Some hosts fetch a web page through a tool that hands the agent a summary of the page instead of its text; if yours does, ask the agent to download the file and read it whole.

The install does not stage or commit.
You read what it wrote and commit it yourself, as with every change the agent makes (chapter 15).

## What the install never touches, and how to update

The setup file writes the kit's files and nothing else.
`docs/`, `work/`, `AGENTS.md` and `CLAUDE.md` belong to the project: the commands write them, starting with `/brainstorm` or `/analyze` (chapter 12), and the setup file never touches them.
A `GEMINI.md` that already holds the project's own text keeps it; the kit only adds one line at its top.

To update the kit, say the same sentence again.
The agent writes the kit's files as the setup file holds them now, and the change you review is the kit's alone, with nothing of your project in it.
It replaces a file only when that file is one the kit shipped, in this version or an earlier one.
A command of your own in a host's folder, or an edit you made by hand to one of the kit's files, `.claude/skills/apply/SKILL.md` say, stops the update before it writes any file: the agent shows the diff against the kit's file, and you decide whether to keep yours or replace it.

## What an update reports

docs/04, docs/05, docs/06 and `AGENTS.md` belong to the project: the team wrote its rules there, its choices with them, such as the verify command or working on trunk, and its queue.
When a new kit version changes what those files should hold, the setup file does not write it.
It compares the files with its own templates and reports each migration, a change your documents still need: the path, the section or the line, and the wording it proposes, in the project's documentation language.
A migration may name a rule, a queue line or a slot.
Your choices stay: a docs/05 whose §5 says "trunk, one session at a time" sees the wording for two sessions in one folder proposed, and keeps its own until the team accepts the change.

Here is the report of the update from 2026.10.13 to 2026.10.16 on the lending library, written for this chapter:

```
Installed: focus-kit 2026.10.16, in every SKILL.md.
Pending process migrations: 6.

1. docs/05, §2 The flow: after "the answer stops there", add
   "or, when the person wants it defined now, the conversation
   continues as /propose <slug> in the same session".
2. docs/05, §4 The queue: add "A line is the mark, the slug, one
   sentence and its suffixes; what happened goes on the page."
3. docs/05, §5 This project: open it with "A slot says what and the
   command, in a few lines." In the Manuals slot, add "and a proof
   /apply runs on another machine".
4. AGENTS.md, Non-negotiables, the "One delivery" line: add the
   clause of item 1.
5. docs/06, Milestone 1, the line members carries history. Shorten
   it to "the librarian registers, suspends and reinstates members"
   and move "suspended members keep their loans, as the librarian
   decided" to work/done/members.md, which lacks it.
6. docs/05, §5 Environments: the slot holds the steps to publish the
   app. Keep its command and point to docs/manuals/publish-the-app.md,
   which takes the steps.

docs/ and AGENTS.md were not changed.
```

Items 5 and 6 change no rule.
The line `members` still says what that delivery was, and the slot still names its command; each loses only what a session would read for nothing every time, the reason [chapter 13](13-queue-and-milestones.md) gives for a short line and [chapter 10](10-the-documents.md) for a short slot.
The decision stays on the page in `work/done/`, where the report sends it.

The report keeps two facts apart.
The `metadata.version` in each `SKILL.md` says which kit is installed.
The process is what docs/04, docs/05 and `AGENTS.md` say, because that is what every command reads, so an updated kit whose migrations are not applied still runs the old process.
The update is done when the migrations are applied, and the method applies them as it applies any change: a queue line, defined with `/propose` and built with `/apply`, so the change to your rules or your queue gets a page, verify and your review.

On a documented project the update reports the migrations first, or says there are none.
It never asks you to run `/brainstorm` or `/analyze` again: those write a project's documents from nothing, and yours exist.
A version that asks nothing of your documents reports no migration: 2026.10.08.2 only made `/apply` show its commit message in the conversation too, so the commands changed and nothing else did.
2026.10.15 reports none either: it changed how a worktree per delivery is laid out, and a docs/05 whose Git slot names no folder for it already means the new layout.

To know why a migration exists, read the kit's changelog, `CHANGELOG.md` in its repository, `CHANGELOG.pt.md` in Portuguese.
It has one entry per version, newest first; the version is the `Version:` line of `SETUP.md`, the same value as the `metadata.version` in each `SKILL.md`.
Each entry says what changed and the problem that caused it, and an item that starts with `Migration:` names what to change in the project's documents.
The entry for 2026.10.16 says, in its `Migration:` item, that the report lists the queue lines that carry history and the slots that narrate steps or output, with the shorter wording: items 5 and 6 of the report above.

## How each host finds the commands

A host needs two things from the repository: the rules file, `AGENTS.md`, and the commands, each with the slug you type after it, the name of the delivery in `work/<slug>.md` (chapter 14).
The setup file writes what every host below needs:

| Host | Reads the rules from | Reads the commands from | You type |
|---|---|---|---|
| Claude Code | `CLAUDE.md`, which imports `AGENTS.md` | `.claude/skills/` | `/propose <slug>` |
| Codex | `AGENTS.md` | `.agents/skills/` | `$propose <slug>` |
| GitHub Copilot | `AGENTS.md` | `.agents/skills/`, through a prompt file in `.github/prompts/` | `/propose`, and it asks for the slug |
| Cursor | `AGENTS.md` | `.agents/skills/`, through a command file in `.cursor/commands/` | `/propose` |
| Gemini CLI | `AGENTS.md`, through `GEMINI.md` | `.agents/skills/`, through a command file in `.gemini/commands/` | `/propose <slug>` |
| Google Antigravity | `AGENTS.md`, through a rule in `.agents/rules/` | `.agents/skills/` | `/propose <slug>` |
| Windsurf | `AGENTS.md` | `.windsurf/skills/` | `@propose <slug>` |

Each command is a skill, a folder with a `SKILL.md` file of instructions the host loads when you invoke it.[^claude-code-skills][^codex-skills][^copilot-skills]
Claude Code reads `CLAUDE.md` at the start of a session, and a line `@AGENTS.md` in it imports the rules file.[^claude-code-memory]
Codex and Copilot read `AGENTS.md` on their own.[^codex-agents-md][^copilot-instructions]
Copilot's slash command comes from a prompt file that only tells the agent to read the skill and follow it, and asks you for the slug when you type the command.[^copilot-prompt-files]
Codex may run a skill on its own when a message matches its description; a small file beside each skill turns that off, so a message that happens to say "apply" builds nothing you did not ask for.[^codex-skills]
For Cursor, the vendor's documentation does not say whether a slug typed after a command reaches it, so name the delivery in your message if it does not.

Every command ends by naming the next one, written as the host running it invokes it, the table's last column.
The setup file names `/brainstorm` or `/analyze`, `/propose` names `/apply` with the page's slug, and `/apply` names the queue's next line.
On the lending library, after `/propose lend-book`, Claude Code tells you to run `/apply lend-book` in a fresh session, and Codex tells you to run `$apply lend-book`.
The kit's files are the same in both; the form follows the host that runs them.

The kit's setup file keeps this table current, with the vendor page each row was read from, and adds a host only with its documentation in hand; other hosts that read `AGENTS.md` can still run a command when you ask for its skill in words.

## Why the method does not depend on the host

The hosts differ in folders and in the character that starts a command, and they share three facts.
Each reads a rules file at the start of a session, `AGENTS.md` directly or through a pointer.
Each reads the files you point it at.
Each can write files.

The method needs nothing more.
It lives in plain files: the rules file, the project documents a fresh session reads, the pages in `work/` and the commands, which only say which documents to read and what never to do.
The setup file writes every host's files, whichever host runs it, so the repository opens ready in any of them, and a person who switches hosts finds the same documents, the same queue and the same commands.

## What the team gains

One repository opens ready in any host, so each person keeps the host they prefer and the team still shares one process, and switching hosts changes nothing in the project.
There is no number for this gain: it is a property of plain files.

An update never rewrites the rules the team wrote.
In the kit's changelog, from 2026.10.07, the version that brought the migration report, to 2026.10.16, six of the eight versions ask for a change in the project's documents, and 2026.10.08.2 and 2026.10.15 are the two that do not.
Each of those six reached a project as a list of what to change and where, with the team's own rules still in place.
The shorter lines and slots of 2026.10.16 pay on every delivery, because a session reads them each time: the entry records a project where each `/apply` read about 180KB of documents before its first edit, a queue of 80KB whose lines reached 4.7KB and an Environments slot of about 120 lines.

And the next command arrives in the form your host recognizes.
The changelog's entry 2026.10.08.1 records why: a Codex user was told to run `/propose`, which Codex does not recognize, since Codex invokes skills with `$`.

## Key points

* One sentence to your agent installs focus-kit, and the same sentence updates it; nothing is installed on your machine, nothing is staged or committed, and a kit file you changed stops the update before it writes.
* The setup file writes only the kit's files and never touches `docs/`, `work/`, `AGENTS.md` or `CLAUDE.md`; a change docs/04, docs/05, docs/06 or `AGENTS.md` needs, a rule, a queue line or a slot, comes as a migration in its report, and until the team applies it as a delivery the process is the old one.
* The kit's changelog, newest first, says for each version what changed, the problem that caused it, and in a `Migration:` item what to change in the project's documents.
* Each host finds the rules and the commands in its own folders: Claude Code runs a command as `/propose <slug>`, Codex as `$propose <slug>`, Copilot as `/propose`, which asks for the slug, Windsurf as `@propose <slug>`; every command names the next one in that form.
* Every host reads a rules file at the start, reads the files you point it at and writes files, and the method needs nothing more.

[^claude-code-memory]: Anthropic, "How Claude remembers your project", Claude Code documentation, accessed 2026-09-30. <https://code.claude.com/docs/en/memory>
[^claude-code-skills]: Anthropic, "Extend Claude with skills", Claude Code documentation, accessed 2026-09-30. <https://code.claude.com/docs/en/skills>
[^codex-agents-md]: OpenAI, "Custom instructions with AGENTS.md", Codex documentation, accessed 2026-09-30. <https://developers.openai.com/codex/guides/agents-md>
[^codex-skills]: OpenAI, "Build skills", Codex documentation, accessed 2026-09-30. <https://developers.openai.com/codex/skills>
[^copilot-instructions]: GitHub, "Adding repository custom instructions for GitHub Copilot", GitHub Docs, accessed 2026-09-30. <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
[^copilot-skills]: GitHub, "About agent skills", GitHub Docs, accessed 2026-09-30. <https://docs.github.com/en/copilot/concepts/agents/about-agent-skills>
[^copilot-prompt-files]: GitHub, "Your first prompt file", GitHub Docs, accessed 2026-09-30. <https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file>
