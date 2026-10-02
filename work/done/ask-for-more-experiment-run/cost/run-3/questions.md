# Questions: cost, run 3

Each time the agent asked something, its message (the last text block of that turn, byte for byte) and the answer sent, which uses only the lines of `../brief.md` or "Use your judgment.".

## Asked in turn 2, answered in turn 3

Asked:

    Understood, I won't change anything until you've answered. One thing first: I already created `CLAUDE.md` last turn. It's uncommitted, so it's easy to revise or delete based on what you tell me.

    Here is what I need to know:

    **Where and how the agent runs**
    1. Where do the questions come from: Slack, GitHub issues, a file in the repo, or a person typing into Claude Code? This decides whether I set up a schedule, an integration, or just context.
    2. Will it run unattended, for example as a scheduled cloud agent? If so, it can't approve permission prompts, as happened to me twice here. Should I set up `.claude/settings.json` to allow `npm test` and read-only git commands?
    3. Should the agent be strictly read-only, or may it fix small things it finds, like stale notes or the missing pointer on the 04-08 note?

    **Audience**
    4. Who asks the questions: only the developers, or also Juno, Odile and Wren? That changes the tone. For library staff it should use plain language, with no file paths or error codes unless asked.
    5. Should answers include citations (`loan.ts:39`, the note and its date)? Or should they give a short answer by default, with sources only on request?

    **Keeping it accurate over time**
    6. The current-rules table in `CLAUDE.md` copies values from the code, so it will drift when rules change. Would you rather:
       - (a) keep the table, plus an instruction to always check the code first,
       - (b) drop the numbers and point the agent at the constants and tests, or
       - (c) have the agent flag any drift it notices?
    7. Do new notes keep landing in `notes/` with mixed naming? Should the agent treat any new note as possibly overriding older ones? Or would the team adopt a status line ("Status: current / superseded by X / draft") so the agent doesn't have to infer it?

    **Content I wasn't sure about**
    8. I listed some contradictions within the notes, such as the March retro and the ADR 2 example. Are any of those actually right and my reading wrong?
    9. `rafe-notes-error-handling.md` is referenced but missing. Does it exist somewhere I should know about?
    10. Is there context that lives outside the repo, like the tracker, chat or shared drive, that the agent should know exists, so it can say "check X" instead of "I don't know"?

    **Scope**
    11. Besides answering, should the agent produce anything daily, such as a log of questions asked, a list of gaps it couldn't answer, or suggested doc fixes?

Answered:

    1. The questions come from developers and the product owner, about 20 a day. Each question opens a fresh session.
    2. Each question opens a fresh session. Use your judgment.
    3. Use your judgment.
    4. The questions come from developers and the product owner, about 20 a day.
    5. Use your judgment.
    6. Use your judgment.
    7. The notes keep growing. Use your judgment.
    8. Use your judgment.
    9. Use your judgment.
    10. Use your judgment.
    11. Use your judgment.
