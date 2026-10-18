# ch03-error-languages

**Objective.** A reader of chapter 3 can explain that several languages separate a program's bug from a failure the caller handles, each with its own mechanism, that most do not, and that Dart makes the separation most explicitly, in the names of its two root types; the sentence "Dart is the one language I have seen make the difference visible" (en 03:163, pt 03:164) is gone. Both editions. From the author's reading of the book on 2026-10-18: "Dart is not the only one; it is the most explicit by type. [...] The book says some languages make the separation, and Dart makes it most clearly."

**Decided without the author.** The batch had no one to answer; each choice is the recommended one.

1. *In place, one paragraph.* The change is the section `## Exception, refusal, error` (pt `## Exceção, recusa, erro`), its two opening lines and the Dart sentence (en 03:161 to 163, pt 03:162 to 164 at /propose); the three bullets and the closing lines stay. A few sentences, no table: the line says "some languages", and a list of five proves it. Source: the draft ("No table required; as long as proving it takes"), ADR-0015.
2. *The first sentence changes too.* "A failure is one of three things, and the class name never tells you which" contradicts a paragraph that then shows a class name telling. It becomes: in most languages the type does not tell you which. Source: the Rust book, chapter 9: "Most languages don't distinguish between these two kinds of errors and handle both in the same way, using mechanisms such as exceptions."
3. *The languages kept, each with what its official documentation says:*
   * Rust: `Result<T, E>` for recoverable failures, `panic!` for unrecoverable ones, which "are always symptoms of bugs"; its guidelines panic when "some assumption, guarantee, contract, or invariant has been broken". Sources: <https://doc.rust-lang.org/book/ch09-00-error-handling.html>, <https://doc.rust-lang.org/book/ch09-03-to-panic-or-not-to-panic.html>.
   * Swift: `throws` for "recoverable errors at runtime"; assertions and preconditions "aren't used for recoverable or expected errors", "there's no way to catch a failed assertion", and force unwrapping a `nil` stands for "a programmer error or corrupted state", "effectively, a shorter spelling of `fatalError`". Sources, for the reader: <https://docs.swift.org/swift-book/documentation/the-swift-programming-language/errorhandling/> and <https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Assertions-and-Preconditions>; the rendered site needs JavaScript, so /apply verifies the words in the book's source, <https://raw.githubusercontent.com/swiftlang/swift-book/main/TSPL.docc/LanguageGuide/TheBasics.md> and `.../ErrorHandling.md`.
   * Go: an `error` returned to the caller is "the usual way to report an error"; `panic` is for when "the program simply cannot continue" or "something impossible has happened", and the runtime panics on bugs such as "indexing a slice out of bounds"; "real library functions should avoid `panic`". Source: Effective Go, sections Errors, Panic and Recover, <https://go.dev/doc/effective_go>. The note says "Effective Go" plainly; the page says it was written for Go's 2009 release and is not actively updated, so the chapter leans on it for nothing current.
   * Java: the line is drawn, but not by name. `Error` marks "serious problems that a reasonable application should not try to catch"; the tutorial says runtime exceptions "represent problems that are the result of a programming problem", which the caller "cannot reasonably be expected to recover from"; yet `NullPointerException` extends `RuntimeException`, which extends `Exception`, so a catch of `Exception` also catches the bug. Sources: <https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Error.html>, <https://docs.oracle.com/javase/tutorial/essential/exceptions/runtime.html>, <https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html>.
   * Dart: as the chapter already quotes, plus that its `Error` subclasses include `RangeError`, `StateError` and `TypeError`, and its `Error` page names the line in the book's terms: a failure the caller must catch is "an *exception* rather than an error". Source: the existing `[^dart-core]`.
4. *Dropped, with reason.* Kotlin: its documentation says only that it "treats all exceptions as unchecked", which shows no separation, and the line is about languages that separate. C++: no official source fetched, and the chapter never names it. `IllegalArgumentException` and Dart's `on Exception catch`: not verified, and `NullPointerException` and the root types already prove the point. Source: the batch rule (drop what cannot be sourced), ADR-0015.
5. *"Most explicitly" means by name, and is the author's.* Dart alone puts the book's line in the names of its two root types, `Exception` and `Error`, and defines it in its API reference in the book's own terms; Rust, Swift and Go draw the same line by mechanism (`Result` or `throws` or a returned `error`, against `panic!`, a trap or `panic`), and Java by compile-time checking at a type whose name does not say so (Java also has `Error` and `Exception` under `Throwable`, but they mark another split; /apply writes "Dart alone names the book's line in its root types", never "Dart alone has these names"). The sentence stays in the first person, as the current one is, softened to what can be stood behind ("the most explicit I know"). Source: the draft; work/agent-never-unsure.md decision 4 (an observation said as the author's).
6. *The book's words stay the book's.* Each language calls "error" what this book calls an exception (Rust's "recoverable errors", Go's `error`, Swift's "recoverable errors"). The paragraph names each language's mechanism, not its word; a quote that says "error" for a handled failure is attributed to its language and followed by the book's term. Error stays a bug, as docs/03's rows `exception`, `refusal`, `error` define, and "recoverable error" is never used as the book's term. Source: docs/03.
7. *The exception bullet gains one example.* The draft notes that not every exception is transient. The bullet already says "an expected failure from outside the program", and docs/03's row names "a missing record"; its three examples, though, all read as transient. It gains one that is not: a file that is not there (Rust's own example of a recoverable failure). "An invalid JSON" is not added: it can be an exception or a refusal, and the chapter would have to say which. Source: the draft, the Rust book chapter 9, docs/03.
8. *JavaScript and .NET get their notes.* The sentence "JavaScript's built-in failures are all an `Error`, and .NET's are all an `Exception`" stays and, now that the paragraph sources every language, carries notes: MDN says `Error` objects "are thrown when runtime errors occur" and serve "as a base object for user-defined exceptions", <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error>; Microsoft Learn says `System.Exception` "serves as the base class for all exceptions", <https://learn.microsoft.com/en-us/dotnet/api/system.exception>. Source: docs/04 (every quoted claim carries a note).
9. *Retry stays out.* Neither edition of chapter 3 mentions a retry, and the draft says to use it only if the chapter already needs it. Source: the draft.
10. *Opening, key point and gain unchanged.* The chapter's opening sentence and the key point at en 03:263 already say the three kinds of failure; which languages separate them is support for that, not a new ability. Line 241 (Rust and Dart's exhaustive `match` or `switch`) stays. Source: ADR-0015, ADR-0017.
11. No new docs/03 term, no new queue line, no split.

**Behaviour.**

* The reader of chapter 3, in either edition, reads at the start of "Exception, refusal, error":
  * that a failure is one of three things and in most languages the type does not tell which (Rust book quoted, with its note);
  * that JavaScript's built-in failures are all an `Error` and .NET's all an `Exception` (each with its note);
  * that some languages do separate a bug from a failure the caller handles, each in its own way: Rust (`Result` against `panic!`), Swift (`throws` against assertions, preconditions and `fatalError`), Go (a returned `error` against `panic`), and Java, whose line runs through `RuntimeException`, so `NullPointerException` is still an `Exception`;
  * that Dart is the most explicit the author knows, because the line is in its two root types' names, and the existing quotes on `Exception` and `Error`, with `RangeError`, `StateError` and `TypeError` named as `Error`.
* The exception bullet lists a missing file among its examples; the refusal and error bullets are unchanged.
* The Portuguese edition says the same with the same notes; quotes are translated in the text and the notes keep the English titles (docs/04).
* Checked at apply time:
  * `grep -n "the one language\|a única linguagem" book/*/03-simplicity-and-results.md` prints nothing.
  * `grep -n -i "kotlin\|c++" book/*/03-simplicity-and-results.md` prints nothing.
  * `grep -n -i "recoverable error\|erro recuperável" book/*/03-simplicity-and-results.md` prints only lines inside a quotation, attributed to Rust or Swift.
  * Each quoted phrase is found in the source the note points to, read at apply time.
* Fails: Dart still called the only language; a language named without a note to its official documentation; Kotlin or C++ named; "error" used for a handled failure outside a quotation; a table; a retry passage; a pointer to a later chapter; any change outside the section's opening lines, the exception bullet's examples and the notes; the editions differing; an em dash.

**Contract.**

* Files: `book/en/03-simplicity-and-results.md`, `book/pt/03-simplicity-and-results.md`. In each: the section's first lines (en 03:161 to 163, pt 03:162 to 164 at /propose), the exception bullet's examples (en 03:165, pt 03:166), and the notes at the end of the file.
* Notes, in the chapter's existing format (`Author or publisher, "Title", site, accessed <apply date>. <url>`): `[^rust-book-errors]` (both Rust pages), `[^swift-book-errors]` (The Basics and Error Handling, docs.swift.org URLs), `[^effective-go]`, `[^java-errors]` (the Error and NullPointerException API pages and the tutorial page), `[^mdn-error]`, `[^dotnet-exception]`; `[^dart-core]` reused. The URLs are the ones decisions 3 and 8 list.
* Terms of docs/03: none new; `exception`, `refusal`, `error` used as their rows define (decision 6). Cases: none. Exercises: none (ADR-0017).
* docs/00 to docs/05: no change. docs/06: this line's marks only, set by the driver and by /apply.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Deliveries in flight on the same files.** Chapter 3 is edited by three other M18 lines; none touches this section, and no line order is needed.

* `ch03-literal-type-comment`: the refusal example's code block (en near 03:120 to 150), a comment inside the code.
* `pt-identifiers-choice`: pt 03:25 and docs/04, Portuguese only.
* `early-no-forward-links`: chapter 3's forward pointers at en 03:11, 98, 133, 220 and 250, none between 159 and 182; it applies last of M18's lines on chapters 0 to 7. This delivery adds no chapter pointer, so its rule holds in either order.
* `pt-ninjobs-masculine`: pt 03:7's heading.
* Whichever lands second reads chapter 3 as the first left it; the line numbers here are a courtesy counted on 2026-10-18. `m18-review` reads all of them after.

**Out of scope.**

* Kotlin, C++, `IllegalArgumentException`, `on Exception catch`: decision 4.
* A table of languages: decision 1.
* Retry: decision 9.
* The refusal and error bullets, the "Why not throw" section, line 241 and the key point: decision 10.
* `work/done/`: the record, not rewritten.

**Done when.**

* [x] Both editions written: the opening lines, the language sentences, the exception example and the notes, as Behaviour and Contract say.
* [x] Every quoted phrase checked against its source at apply time; the Swift words checked in the book's source repository, the note pointing to docs.swift.org.
* [x] Behaviour's apply-time checks give what they name.
* [x] Chapter 3 still opens with its value, keeps its gain, no filler and nothing useful cut.
* [x] Every number sourced: none added.
* [x] `make verify` green: edition parity, prose rules, width, links, disclosure scan, no em dash.
* [x] The author's approval of an anonymized passage: inapplicable, no private case (docs/00 OD-3).
* [x] `make book` run; both PDF paths given to the author: by the batch driver, once at the end of the batch.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block: the page moved and the message below by /apply; the mark, staging and commit by the batch driver.

**Proof.**

* en 03:164 to 175, pt 03:165 to 176: the section's opening now says most languages' types do not tell (Rust book quoted), JavaScript and .NET with their notes, then one sentence each for Rust, Swift, Go, Java (two) and Dart (two); the exception bullet adds "a file is not there" ("um arquivo não está lá"). Six new notes at the end of both editions, `[^dart-core]` reused. `git diff --stat` on the two paths: 20 insertions, 5 deletions each.
* Every quoted phrase found at apply time, 2026-10-18, in its source: the two Rust book pages; Swift's `TheBasics.md` and `ErrorHandling.md` in swiftlang/swift-book; Effective Go (its "not actively updated" banner read too); Oracle's `Error` and `NullPointerException` pages (`java.lang.RuntimeException` in its hierarchy) and the tutorial page; MDN "Error"; Microsoft Learn "Exception Class"; Dart's `Error` page ("we consider the thrown object an exception rather than an error"; `StateError` and `TypeError` among its implementers, `RangeError` through `ArgumentError`).
* Behaviour's greps: "the one language" and "a única linguagem" print nothing; "kotlin" and "c++" print nothing; "recoverable error" prints en 03:169 and 03:170, pt 03:171, each inside a quotation attributed to Rust or Swift.
* `make verify` green: build, parity, em dash, prose, width, links, disclosure.

**Divergences.**

* The Rust quote "unrecoverable errors are always symptoms of bugs" is quoted whole, with its subject, so that "recoverable error" appears only inside a quotation, as Behaviour's grep asks.
* The Rust page title "To panic! or Not to panic!" is written with `panic!` in code, as the Rust book sets it, because the prose check reads a bare "!" as an exclamation.
* The Java tutorial's title joins "Unchecked Exceptions" and "The Controversy" with an em dash; the note writes it with a colon, by the no-em-dash rule.
* The .NET note carries no quote in the text: the sentence says only that .NET's failures are all an `Exception`, which the page's "the base class for all exceptions" supports (the page's wording is "The Exception class is the base class for all exceptions", not "serves as").

**Decisions taken in /apply.**

* Run in a batch of applies on one tree: the batch driver marks this line in docs/06, runs `make book` once at the end of the batch and gives both PDF paths, and stages and commits this delivery by its paths.
* Swift's force unwrap and its "programmer error or corrupted state" are left out: the sentence names assertions, preconditions and `fatalError`, and one quote proves the line.
* Go's "real library functions should avoid `panic`" is left out: the two quotes on `error` and `panic` already prove the line.
* The six new notes follow `[^dart-core]` at the end of the file, in no particular order; the PDF and EPUB number notes by first citation.

**Review.** One read-only agent on Opus read the diff of the two paths against this page, docs/03 and docs/04, and fetched the sources: nothing breaks the page or docs/04; every quote matches. Of four optional suggestions, two applied: pt "interrompe" instead of the verb "para", which read as the preposition (03:170, 03:171), and "um slice" (03:172). Not applied: a book term after the opening Rust quote (the sentence before it already names the two kinds as a bug and a failure the caller handles), and decision 5's wording "Dart alone names" (Behaviour asks for "the most explicit the author knows"). No queue line.

```commit
docs(ch03-error-languages): say which languages separate a bug from a handled failure

- Chapter 3, "Exception, refusal, error": most languages' types do not tell which; Rust, Swift, Go and Java separate the bug by their own mechanisms, and Dart most explicitly, in its root types' names
- The exception bullet adds a missing file; six new source notes, JavaScript and .NET included

work/done/ch03-error-languages.md
```
