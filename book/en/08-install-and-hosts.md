# 8. Install, and the hosts

After this chapter you can install focus-kit in a repository with one sentence to your coding agent, update it with the same sentence, knowing what the update writes and what it only reports to you, and invoke its commands in the host you use.
You can also say why the method does not depend on the host.

## The problem

A method tied to one tool lasts as long as the team keeps that tool, and a team rarely agrees on one.
One person works in Claude Code, another in Copilot inside their editor, a third tries Codex, and each host, the program that runs the coding agent, looks for its rules and its commands in folders of its own.
The kit has to open ready in all of them, and install without asking anyone to install anything.

## Install

Open your coding agent at the root of the repository and say:

```
Read https://raw.githubusercontent.com/JCKodel/focus-kit/main/SETUP.md
and do what it says.
```

The address is the file itself, not the page GitHub draws around it, so the agent gets the whole text.
That file is the kit's setup file: one file of instructions that the agent reads and turns into the kit's files, the four commands and a few small pointer files for the hosts that need them.
Nothing is installed on your machine; the agent writes files into the repository, and that is all.
Your host may ask before it downloads the file and before it writes into its own folder inside the repository, `.claude/` in Claude Code: approve both.

The setup file tells the agent to copy every file byte for byte.
Some hosts fetch a web page through a tool that hands the agent a summary of the page instead of its text; if yours does, ask the agent to download the file and read it whole.

The install does not stage or commit.
You read what it wrote and commit it yourself, as with every change the agent makes (chapter 13).

## What the install never touches, and how to update

The setup file writes the kit's files and nothing else.
`docs/`, `work/`, `AGENTS.md` and `CLAUDE.md` belong to the project: the commands write them, starting with `/brainstorm` or `/analyze` (chapter 9), and the setup file never touches them.
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

Here is the report of an update on the lending library, written for this chapter:

```
Installed: focus-kit 2026.10.18, in every SKILL.md.
Pending process migrations: 3.

1. docs/05, §4 The queue: in the mark table, [?] is set "in the four
   cases below"; after "such as a fix found in the middle of an
   /apply" add ", or when a milestone review's code reading missed
   part of its range (§8)".
2. docs/05, §5 Delivery review: the slot reads git diff. Proposed:
   "Delivery review: a read-only agent on the session's model reads
   git diff of the delivery's paths and the files the delivery
   created, which no diff shows until they are staged, against its
   page and docs/04."
3. docs/05, §8 Closing a milestone: replace "Its page names the
   commit that closed the previous milestone, or the first commit, as
   the base," with "Its page names as the base the commit of the
   previous milestone's review, so the range holds the fixes of its
   findings, which get no second review, or the first commit for a
   first milestone,"; "marks it seen," with "marks it seen (true in
   the file today),"; and "with · resume: apply (§4)" with "with
   · resume: apply and · blocked: <what was read> (§4)".

docs/ and AGENTS.md were not changed.
```

Every item changes a rule.
Item 1 gives a line a fourth case to wait in, a milestone review whose code reading missed part of its range ([chapter 14](14-queue-states.md)), so a reading that covered less than its range shows in the queue instead of passing as done.
Item 2 has the delivery review read the files the delivery created as well as its `git diff`: a new file is untracked, one git does not hold yet, so `git diff` shows nothing of it until it is staged, and `/apply` stages after the review.
Item 3 names as the base the commit of the previous milestone's review, so the range holds every commit after that review: the fixes of its findings, and the next milestone's deliveries that landed after it ([chapter 15](15-closing-a-milestone.md)); it also says what seen means, and has the waiting line say what the readers read.
A Delivery review slot that names the host's own review gets no item 2: the report proposes the created files only where the slot reads `git diff`, so the team's choice of reviewer stays.

The kit's version is the `metadata.version` in each `SKILL.md`; the process is what docs/04, docs/05 and `AGENTS.md` say, because every command reads them, so an updated kit whose migrations are not applied still runs the old process.
The update is done when the migrations are applied, as any change is: a queue line, defined with `/propose` and built with `/apply`, so the change to your rules or your queue gets a page, verify and your review.

On a documented project the update reports the migrations first, or says there are none.
It never asks you to run `/brainstorm` or `/analyze` again: those write a project's documents from nothing, and yours exist.
A version that asks nothing of your documents reports no migration: a version that changes only the commands, such as `/apply` showing its commit message in the conversation too, changes nothing else.
A docs/05 whose Git slot chose a worktree per delivery and names no folder gets a migration only when the project already works in a container, the folder [chapter 19](19-worktrees.md) lays out with the checkout and a hidden folder for the history and the worktrees, and that hidden folder holds `repo.git/`.
The report then proposes writing in that folder's name and the prefix the delivery branches already use, so nothing moves.
With no container yet, the slot means the kit's default, which that chapter names, and the report proposes nothing.

To know why a migration exists, read the kit's changelog, `CHANGELOG.md` in its repository, `CHANGELOG.pt.md` in Portuguese.
It has one entry per version, newest first; the version is the `Version:` line of `SETUP.md`, the same value as the `metadata.version` in each `SKILL.md`.
Each entry says what changed and the problem that caused it, and an entry may carry an item that starts with `Migration:`, naming what to change in the project's documents.
What a rerun compares is the setup file's own step, which names the sections of docs/05, the slots and the lines of `AGENTS.md` it checks; the report lists only what your documents still lack, on the lending library the three items above.

## How each host finds the commands

A host needs two things from the repository: the rules file, `AGENTS.md`, and the commands, each with the slug you type after it, the name of the delivery in `work/<slug>.md` (chapter 12).
The setup file writes what every host below needs:

| Host | Reads the rules from | Reads the commands from | You type |
|---|---|---|---|
| Claude Code | `CLAUDE.md`, which imports `AGENTS.md` | `.claude/skills/` | `/propose <slug>` |
| Codex | `AGENTS.md` | `.agents/skills/` | `$propose <slug>` |
| GitHub Copilot | `AGENTS.md` | `.agents/skills/`, through a prompt file in `.github/prompts/` | `/propose`, and it asks for the slug |
| Cursor | `AGENTS.md` | `.agents/skills/`, through a command file in `.cursor/commands/` | `/propose` |
| Gemini CLI | `AGENTS.md`, through `GEMINI.md` | `.agents/skills/`, through a command file in `.gemini/commands/` | `/propose <slug>` |
| Google Antigravity | `AGENTS.md`, through a rule in `.agents/rules/` | `.agents/skills/` | `/propose <slug>` |
| Devin Desktop, formerly Windsurf | `AGENTS.md` | `.agents/skills/` | `/propose` |
| OpenCode, Zed | `AGENTS.md` | `.agents/skills/` | by asking for the skill |

Each command is a skill, a folder with a `SKILL.md` file of instructions the host loads when you invoke it.[^claude-code-skills][^codex-skills][^copilot-skills]
Claude Code reads `CLAUDE.md` at the start of a session, and a line `@AGENTS.md` in it imports the rules file.[^claude-code-memory]
Codex, Copilot and Devin Desktop, formerly Windsurf, read `AGENTS.md` on their own.[^codex-agents-md][^copilot-instructions][^devin-rules]
Copilot's slash command comes from a prompt file that only tells the agent to read the skill and follow it, and asks you for the slug when you type the command.[^copilot-prompt-files]
Codex may run a skill on its own when a message matches its description; a small file beside each skill turns that off, so a message that happens to say "apply" builds nothing you did not ask for.[^codex-skills]
For Cursor and Devin Desktop, neither vendor's documentation says whether a slug typed after a command reaches it, so name the delivery in your message if it does not.
Devin Desktop also reads `.windsurf/skills/`, the folder of its former name;[^devin-skills] the setup file writes nothing there and, on an update, removes the kit's own files from it, so the host never finds an older copy of a command beside the current one in `.agents/skills/`, and a file of yours there is reported and left.

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

An update never rewrites the rules the team wrote.
A version that asks for a change in the project's documents reaches the project as a list of what to change and where, with the team's own rules still in place, and the team applies it as it applies any change.

And the next command arrives in the form your host recognizes, because a host may not recognize another's form: Codex does not recognize `/propose`, since Codex invokes skills with `$`.

## Key points

* One sentence to your agent installs focus-kit, and the same sentence updates it; nothing is installed on your machine, nothing is staged or committed, and a kit file you changed stops the update before it writes.
* The setup file writes only the kit's files and never touches `docs/`, `work/`, `AGENTS.md` or `CLAUDE.md`; a change docs/04, docs/05, docs/06 or `AGENTS.md` needs, a rule, a queue line or a slot, comes as a migration in its report, and until the team applies it as a delivery the process is the old one.
* The kit's changelog, newest first, says for each version what changed, the problem that caused it, and, in an item that starts with `Migration:` when the entry has one, what to change in the project's documents.
* Each host finds the rules and the commands in its own folders: Claude Code runs a command as `/propose <slug>`, Codex as `$propose <slug>`, Copilot as `/propose`, which asks for the slug, Devin Desktop as `/propose`; every command names the next one in that form.
* Every host reads a rules file at the start, reads the files you point it at and writes files, and the method needs nothing more.

[^claude-code-memory]: Anthropic, "How Claude remembers your project", Claude Code documentation, accessed 2026-09-30. <https://code.claude.com/docs/en/memory>
[^claude-code-skills]: Anthropic, "Extend Claude with skills", Claude Code documentation, accessed 2026-09-30. <https://code.claude.com/docs/en/skills>
[^codex-agents-md]: OpenAI, "Custom instructions with AGENTS.md", Codex documentation, accessed 2026-09-30. <https://developers.openai.com/codex/guides/agents-md>
[^codex-skills]: OpenAI, "Build skills", Codex documentation, accessed 2026-09-30. <https://developers.openai.com/codex/skills>
[^copilot-instructions]: GitHub, "Adding repository custom instructions for GitHub Copilot", GitHub Docs, accessed 2026-09-30. <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
[^copilot-skills]: GitHub, "About agent skills", GitHub Docs, accessed 2026-09-30. <https://docs.github.com/en/copilot/concepts/agents/about-agent-skills>
[^copilot-prompt-files]: GitHub, "Your first prompt file", GitHub Docs, accessed 2026-09-30. <https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file>
[^devin-skills]: Cognition, "Skills Overview", Devin Docs, accessed 2026-10-17. <https://docs.devin.ai/cli/extensibility/skills/overview>
[^devin-rules]: Cognition, "Rules & AGENTS.md", Devin Docs, accessed 2026-10-17. <https://docs.devin.ai/cli/extensibility/rules>
