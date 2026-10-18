# ch03-error-languages

Draft, from the author's reading of the book on 2026-10-18.

* pt 03:164 says "Dart é a única linguagem que eu vi tornar a diferença visível". Dart is not the only one; it is the most explicit by type.
* The distinction: an error is a violated premise, a bug to fix; an exception is a failure the operation foresees, which the caller can handle. Not every exception is transient (a missing file, an invalid JSON); the precise line is recoverable failure versus programming failure.
* What the author brought (to verify against each language's official documentation, with a source per claim, docs/04):
  * Dart: `Error` versus `Exception`, independent; `RangeError`, `StateError`, `TypeError` are `Error`. `on Exception catch` respects the line.
  * Java, Kotlin: `Error` versus `Exception` under `Throwable`, but bugs such as `NullPointerException` and `IllegalArgumentException` are `Exception`.
  * Rust: `Result<T, E>` for recoverable failures, `panic!` for violated premises; its book makes this distinction.
  * Go: `error` versus `panic`, though `panic` is not always a bug.
  * Swift: `throw` for handled failures, traps and `fatalError` for programming failures.
  * C#, JavaScript/TypeScript, C++: no such separation.
* The book says some languages make the separation, and Dart makes it most clearly. No table required; as long as proving it takes (ADR-0015).
* Retry: a transient network failure may justify a retry; a bug must not be hidden by a recovery mechanism. Use it only if the chapter already needs it.
