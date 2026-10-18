# ch03-literal-type-comment

Draft, from the author's reading of the book on 2026-10-18.

* The refusal example (`type Recusa = "TemLivrosEmAtraso"` and `err("TemLivrosEmAtraso")`, en `HasOverdueBooks`) reads to someone who does not know TypeScript as a magic string written twice, as if `Recusa` should be a constant that `err` returns.
* The code is correct: the type is a string literal type, and the compiler accepts only that exact string in `err`; a typo does not compile.
* The author chose a comment in the code, not prose, to say so.
* Keep the author's layout: declarations and `{ }` blocks apart with blank lines (commit 8507633); within 74 columns.
