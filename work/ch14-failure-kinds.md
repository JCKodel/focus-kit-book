# ch14-failure-kinds

**Objective.** A reader of chapter 14 can say, in any language, what an error is (a bug, fixed and never handled) and what an exception is (a failure from outside the program, handled where it happens), and can explain why an exception must not steer the program's flow. They can also turn a library's exception into their own domain's value at the boundary, so the rest of the app has no exceptions at all.

**Behaviour.**

* The reader can tell an error from an exception by its cause, not by its class name. JavaScript calls every failure `Error` and .NET calls every one `Exception`, so the name tells them nothing.
* The reader knows where the split comes from. Dart names it in two classes, `Exception` and `Error`, and the author credits it, in the first person: in forty years of programming, it is the one language that made the difference visible. The explanation stands without Dart, and no Dart code is shown.
* The reader can place any thrown value in Lippert's four kinds: fatal, boneheaded, vexing and exogenous. They can map them to the book's words: boneheaded is an error; exogenous is an exception; vexing is an exception an API's design makes, turned into a value on the spot or avoided with a `Try` form; fatal is caught by nobody.
* The reader can give four reasons not to use exceptions for control flow, each with its source:
  * A `throw` is an exit invisible at the call site.
  * The signature does not say what can fail, so the compiler cannot check that every case is handled, as the `Record` over `BookingRefusal` does.
  * A throw costs more than a return.
  * A catch wide enough to steer the flow also catches bugs, the risk `query` already shows.
* The reader can say why an exception belongs to the domain that throws it. A sign-in through Apple whose SDK throws `AppleAuthException` returns `AuthFailure`, because the app must not know Apple exists. This example is prose only, with no code.
* The reader sees the same move in the clinic's real code. SQLite's failure becomes `DatabaseFailed` or `SlotTaken` in the repository. No rule, hook, screen or `api.ts` imports `node:sqlite`. The text of SQLite's `UNIQUE` failure is read in one file only.
* The reader can answer "is every exception outside I/O a bug?" Almost:
  * A vexing exception from parsing comes from text that came from I/O, so it sits at the same boundary.
  * A fatal one is handled by no one.
  * A framework's own control flow is thrown on purpose and must pass untouched: Next.js `redirect()` and `notFound()`, .NET cancellation.
  * The rule the reader leaves with: catch at the boundary with the outside world, and let everything else pass.
* Both editions say the same.

**Contract.**

Sentences are found by their quoted text. The line numbers below are from commit `4404d12`.

* `book/en/14-errors-and-slices.md`:
  * Opening, lines 3-4: the second sentence also promises the two new abilities: why a thrown exception must not steer the flow, and keeping a library's exceptions out of the domain.
  * Section "Exception, refusal, error" (lines 76-92; heading and anchor unchanged), rewritten in this order:
    1. Error and exception, defined by cause. The class-name trap in JS and .NET. The Dart credit in the first person, one or two sentences, with the `dart-core` note kept. No Java aside: Java's `Error` is Lippert's fatal kind, not the book's error, and the audience reads React and .NET.
    2. Lippert's four kinds mapped to error and exception. The names stay in English, in quotes, with his one-line definitions quoted.
    3. The refusal, as today (lines 81-82 and its bullet).
    4. The three-bullet list, as today, with the exception bullet saying "at the boundary with the outside world (I/O, and the parsing of what it brings)".
    5. The field's "errors as values" paragraph (lines 90-92), unchanged.
  * New section "Why not throw" after it, before "Exceptions as values in the clinic": the four reasons of Behaviour. The cost is given as measured, dated and without "orders of magnitude": 1,000 throw/catch through 10 async frames took 123.03 ms on .NET 8 and 54.68 ms on .NET 9. It cites the ASP.NET Core "Minimize exceptions" sentence and the Framework Design Guidelines "DO NOT use exceptions for the normal flow of control, if possible".
  * New section "The boundary" after "Exceptions as values in the clinic" (after line 238), before "One failure, end to end". It holds, in order:
    * the Apple example, in prose;
    * the anti-corruption layer, whose purpose is "to protect the domain model", with the extension to exceptions stated as the book's own step;
    * the clinic's evidence, the `git grep` facts of Behaviour, at `book-v1/closing-a-milestone`. Routes import only the type `DatabaseSync` to pass the handle, and the text says so;
    * the answer on exceptions outside I/O (vexing, fatal, framework) and the rule "catch at the boundary, let the rest pass".
  * Key points: points 3 and 4 (the exception/refusal point and "An error is a bug...") become the three below, as proposals for `/apply` to tighten. The refusal clause stays whole, as `ch14-refusal-io` settled it. Points 1, 2 and 5 are unchanged.
    * "An error is a bug, fixed and never caught; an exception is a failure from outside the program, caught at the boundary and returned as a value; a refusal is a rule saying no, in code or in a database constraint; the class name tells none of them apart." Portuguese: "Um erro é um bug, corrigido e nunca capturado; uma exceção é uma falha de fora do programa, capturada na fronteira e devolvida como valor; uma recusa é uma regra dizendo não, no código ou numa restrição do banco; o nome da classe não distingue nenhum deles."
    * "A throw is an exit the caller cannot see and the compiler cannot check, so it never steers the flow." Portuguese: "Um throw é uma saída que quem chama não vê e o compilador não verifica, então nunca conduz o fluxo."
    * "A library's exception belongs to the library: the code at the boundary turns it into the domain's value, and the rest of the app throws nothing." Portuguese: "A exceção de uma biblioteca pertence à biblioteca: o código na fronteira a transforma no valor do domínio, e o resto do app não lança nada."
  * Exercise 14.1 gains one clause: also name every exception type from a library that reaches code outside the place that does its I/O.
* `book/en/06-the-documents.md:108`: the parenthesis "(Dart splits its `Exception` and `Error` classes the same way)" becomes a credit of origin, such as "a split the author learned from Dart". The note `dart-error-exception` stays.
* `book/pt/`: the same changes in 14 and 06. Lippert's names stay in English, glossed once. "Fronteira" is used for boundary.
* New notes, all accessed 2026-09-30:
  * Eric Lippert, "Vexing exceptions", 2008-09-10, <https://ericlippert.com/2008/09/10/vexing-exceptions/>.
  * Joel Spolsky, "Exceptions", 2003-10-13, <https://www.joelonsoftware.com/2003/10/13/13/>, quoting "*They are invisible in the source code.*" and "*They create too many possible exit points for a function.*"
  * Microsoft Learn, ASP.NET Core best practices, "Minimize exceptions", <https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices>.
  * Krzysztof Cwalina, Framework Design Guidelines, "Exception Throwing", <https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/exception-throwing>.
  * Stephen Toub, "Performance Improvements in .NET 9", 2024-09-12, benchmark `ExceptionThrowCatch`, <https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-9/>.
  * Oracle, Java SE 21 `Error` and `Exception` javadoc.
  * Next.js, `redirect`: "*`redirect` throws an error so it should be called **outside** the `try` block*", <https://nextjs.org/docs/app/api-reference/functions/redirect>.
  * Microsoft Learn, "Best practices for exceptions", cancellation section, <https://learn.microsoft.com/en-us/dotnet/standard/exceptions/best-practices-for-exceptions>.
  * Azure Architecture Center, "Anti-Corruption Layer pattern", <https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer>.

  Every quote is re-read on the live page by `/apply`. Bloch's *Effective Java* is not cited, because its item number was not verified.
* Terms of docs/03: none new. Error, exception and refusal keep the book's meanings. Lippert's names are quoted, not terms.
* Cases: none. Ninjobs is not used. Code shown: only the clinic's, at `book-v1/closing-a-milestone`.

**Out of scope.**

* The clinic's code and its tag: the book only. Routes importing `DatabaseSync` are described, not changed.
* `query`'s catch-all (lines 132-135): settled by `ch14-catch-all`. The new sections link to it and do not repeat it.
* Code examples in .NET, React or Apple's SDK: ADR-0008 and "every artifact shown is real".
* Chapter 15's pieces and the repository row of docs/03: already say that only the repository catches an exception from data.
* A slice importing another slice's code: `slice-imports`, in flight.

**Done when.**

* [ ] Both editions changed with the same meaning. Chapter 14 opens with its value, with no filler and nothing useful cut.
* [ ] No Dart code, and Dart appears in chapter 14 only as the credit of origin.
* [ ] Every quote was re-read on its live page, and the benchmark numbers name their source and date.
* [ ] The clinic's `git grep` claims were re-run at `book-v1/closing-a-milestone`.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
