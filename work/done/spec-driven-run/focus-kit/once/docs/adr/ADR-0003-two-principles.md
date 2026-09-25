# ADR-0003: The two principles of FOCUS, not its four pieces

**2026-09-25 · decided in /analyze.** Context: the module is one file with its type, rule and state together, and there is no screen to separate from rules; the four pieces of FOCUS would add layers that pay nothing yet. Decision: code is organized by feature (vertical slices) and errors travel as values; `throw` is never flow. Consequences: one file per feature in `src/`; a rule that can refuse returns a Result whose shape `book-validation` fixes and docs/01 records; `book()` changes its return type in that delivery.
