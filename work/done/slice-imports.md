# slice-imports

**Objective.** A reader of chapters 14 to 16 can decide where code that two features use should live. Code about one thing the app keeps stays in that thing's slice, and any other slice imports it from there. Code that belongs to no thing the app keeps, such as the shape of a value or plumbing, moves to `src/lib/` on its second use. The reader can then explain why `slotsOf` imports from three other slices.

**Behaviour.**

* In chapter 14, §"Vertical slices" gives the rule in the paragraph on `lib/` (en/14:69-71 and pt/14:69-71 today). The second use says when code moves. The rule says where it goes:
  * Code about one thing the app keeps stays in that thing's slice, and another slice imports what it needs from there. This covers a repository function, a type, a client call or a view. Imports may run both ways between two slices.
  * `src/lib/` holds what two features share that belongs to no thing the app keeps. That is either the shape of a value (`email.ts`, `id.ts`, `name.ts`) or plumbing (`request.ts`, `result.ts`).
* The same paragraph shows the rule working in the clinic. `findClinic` and `findActiveProfessionals` are each imported by two routes, `appointments/route.server.ts` and `weeklyHours/route.server.ts`, so each has a second use. They stay in `clinic/` and `professionals/`, because each reads the thing its slice keeps.
* The rule builds on the definition of one feature from ch14-feature-boundary: "one thing the app keeps, with every action on it". The chapter's text points back to that definition rather than repeating it.
* Chapter 14's second key point carries the rule: "A file enters a slice when it pays its way; code about one thing the app keeps stays in its slice, which other slices import, and code that belongs to no one thing enters `lib/` on its second use." In Portuguese: "Um arquivo entra em uma fatia quando se paga; o código sobre uma coisa que o app guarda fica na fatia dela, que as outras fatias importam, e o código que não pertence a nenhuma coisa entra em `lib/` no segundo uso." Chapter 14 still has five key points.
* In chapter 15, one sentence after "It asks four repository functions, from four slices, ..." (en/15:291, pt/15:292) says that each function lives in the slice of the thing it reads. `slotsOf` imports it from there, as chapter 14's rule says. The sentence links to that section.
* In chapter 16, en/16:334 and pt/16:335 stop calling `professionals/repository.server.ts` "shared code". The five files are called code outside the slice that the delivery calls: the shells, `lib/`, and another slice's repository. The same change applies to en/16:341 and pt/16:343. The counts, the paths and the quote do not change.
* Both editions say the same.
* This settles finding F10 of the M4 review.

**Contract.**

* Files:
  * `book/en/14-errors-and-slices.md`: the `lib/` paragraph ("What two features already share leaves their slices for `src/lib/`." up to "and not before.") and key point 2 ("A file enters a slice when it pays its way, ..."). Both are found by their content, because ch14-feature-boundary adds lines above them first.
  * `book/pt/14-errors-and-slices.md`: the same places ("O que duas funcionalidades já compartilham ..." and "Um arquivo entra em uma fatia quando se paga, ...").
  * `book/en/15-four-pieces.md`: one sentence after line 291. `book/pt/15-four-pieces.md`: one sentence after line 292.
  * `book/en/16-testing-and-agents.md`: lines 334 and 341. `book/pt/16-testing-and-agents.md`: lines 335 and 343.
* Terms of docs/03: none new. The "vertical slice" row already carries the rule from ch14-feature-boundary: a feature is one thing the app keeps, with every action on it. This delivery adds the rest of the rule to that row's meaning: code about that thing stays in its slice and other slices import it, and `lib/` holds what two features share that belongs to no one thing, on its second use.
* Sources: none new. The imports and the "First use / second use" comments come from `git grep` at `book-v1/four-pieces` and `book-v1/closing-a-milestone`, which give the same result at both tags. The chapters link to those tags already.
* First occurrence: ch14-feature-boundary, which gave the definition of one feature that this rule builds on.
* Cases: none. Exercises: unchanged.

**Out of scope.**

* The clinic's docs/01:55 and :88 contradict its own code in the same way. The clinic repository is not touched, and the tags never move.
* Whether a subfolder feature (`features/<name>/<sub-feature>/`) imports its parent's code. The clinic has no subfolder feature, so there is no example to show.
* Chapter 15's injection rule and "Nowhere else is anything passed": the later line `ch15-injection-rule`.
* The rest of chapter 16: the unit-test definition belongs to `ch16-unit-test`. The pages in flight on chapters 14 and 15 keep the lines they own.

**Done when.**

* [x] ch14-feature-boundary is applied first.
* [x] Both editions changed with the same meaning. Chapter 14 opens with its value, with no filler and nothing useful cut.
* [x] Chapter 14 has five key points.
* [x] `grep -n "shared code it calls\|código compartilhado que ela chama" book/*/16-testing-and-agents.md` finds nothing.
* [x] The "vertical slice" row of docs/03 updated.
* [x] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author: run once at the end of the M4.1 loop by the driver.
* [x] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.

**What happened.**

* §"Vertical slices" opens the `lib/` paragraph with the rule: what code is about decides where code two features use lives. Code about one thing the app keeps stays in its slice and other slices import it; `findClinic` and `findActiveProfessionals`, each imported by `appointments/route.server.ts` and `weeklyHours/route.server.ts`, stay in `clinic/` and `professionals/`. What belongs to no thing goes to `src/lib/`, as the shape of a value or plumbing. The closing sentence on chapter 13's rule now says it is code that belongs to no one thing that moves to `lib/` on its second use. The text reuses "one thing the app keeps" from the definition a few paragraphs above instead of restating it.
* Checked with `git grep` at `book-v1/four-pieces` and `book-v1/closing-a-milestone`: the same imports at both tags.
* Key point 2 carries the rule, in the words the page gave; chapter 14 keeps five key points. The "vertical slice" row of docs/03 gains the rest of the rule.
* Chapter 15 adds one sentence after the four repository functions, linking to §"Vertical slices" of chapter 14.
* Chapter 16: the five files are "code outside the slice that it calls", and the professionals repository is named as the professionals slice's; line 341 says "the code outside it that it calls". Choice taken: the page's "the shells" is not a term the book uses, so the sentence keeps the paths in their order and names only the other slice's repository, rather than introducing a new word. Counts, paths and quote unchanged.
* Portuguese: "plumbing" is "encanamento".
* Finding F10 of the M4 review is settled.
