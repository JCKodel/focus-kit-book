# ADR-0004: Trunk-based work

**2026-09-25 · decided in /analyze.** Context: the history is two commits on `main`, and one person reviews every delivery. Decision: everything happens on `main`, one delivery at a time; the agent stages and suggests the message, the person commits. Consequences: no branches or worktrees to manage; two deliveries are never built at the same time.
