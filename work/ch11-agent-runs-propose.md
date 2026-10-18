# ch11-agent-runs-propose

Draft, from the author's reading of the book on 2026-10-18.

* en 11:102, "the agent cannot run `/propose` on its own, since it is a command the host runs, and a page written without it starts without what `/propose` reads", is not true: Claude Code offers to run /propose from the conversation and runs it itself, without the person typing `/propose`.
* /propose decides what the paragraph says instead, keeping what the kit's flow asks (a fresh session for /propose, docs/05 §2) only as far as it is true in hosts that invoke a command from the conversation.
