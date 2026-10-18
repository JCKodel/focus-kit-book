# ch13-four-waits

**Objective.** After chapter 13 a reader can name every case in which `/apply` stops and marks its line `[?]`, the four chapter 14 lists, a milestone review's reading that left part of the milestone's code unread among them; both editions.

**Decided without the author** (batch rule of this run: the recommended answer, no question asked).

1. *Where.* The first sentence of "When the work cannot go on" (pt "Quando o trabalho não consegue seguir"), which lists three cases (`m17-review`, R2-3). The fourth case is added as its last clause; the sentence stays one sentence on one line (docs/04 **One sentence per line**).
2. *Said in words the reader has.* Chapter 13's reader has met the milestone review in chapter 11, which says the session has "the code changed since the milestone's base" read by areas, one read-only agent each; "code reading", "range" and the readers' listed paths are chapter 15's. So the clause says it in chapter 11's words: when `/apply` builds a milestone's review, the reading of the code changed since the milestone's base left part of it unread. The case arises only in a review's `/apply`, so the clause names that condition, as docs/03's `waiting mark` row and docs/05 §4 do ("a milestone review's code reading missed part of its range").
3. *No new pointer.* The next sentence already ends "(chapter 14)", which lists the four cases with their reasons, and chapter 13 already links chapter 15 once, in "The delivery review"; a second pointer to 15 would break docs/04 **Chapter pointers** (once per chapter for each target).
4. *The next sentence stays.* "marks the line `[?]` with that reason at its end (chapter 14)" holds for the fourth case too: its reason, what was read, is chapter 14's to show.
5. *No key point changes.* Key point 2 says `[?]`, "with what it waits on, when it must stop", true for all four.
6. *No docs/03 change.* `waiting mark` already names the four cases.
7. *Trunk; nothing staged by this definition; the driver sets docs/06's marks.* No other line of this batch touches chapter 13 (`untracked-diff-wording` changes chapter 8 and docs/03; chapter 13:65 was found right).

**Behaviour.**

* Reading "When the work cannot go on", a reader finds four cases in which `/apply` stops: an answer nobody has given, another line that must be done first, the person saying the line is blocked, and, in a milestone review, a reading of the code that left part of it unread.
* A reader can say that the fourth case arises only when `/apply` builds a milestone's review, and find in chapter 14, which the next sentence names, its reason and its resume suffix.
* The Portuguese edition reads the same in the same place, with the Contract's words.
* Failure: the sentence split, a case of the three changed or dropped, a pointer added, any other line of chapter 13 changed, or one edition changed and not the other.

**Contract.**

* **Chapter 13, both editions** (`book/en/13-apply.md`, `book/pt/13-apply.md`), found by text, one replacement each in the first sentence of "When the work cannot go on" (pt "Quando o trabalho não consegue seguir"):
  * en "(a fix it found becomes a `[ ]` line above this one), or when you say it is blocked." becomes "(a fix it found becomes a `[ ]` line above this one), when you say it is blocked, or, in a milestone's review, when the reading of the code changed since the milestone's base left part of it unread."
  * pt "(uma correção que ele achou vira uma linha `[ ]` acima desta), ou quando você diz que ela está travada." becomes "(uma correção que ele achou vira uma linha `[ ]` acima desta), quando você diz que ela está travada, ou, na revisão de um marco, quando a leitura do código alterado desde a base do marco deixou parte dele sem ler."
  Every other line of chapter 13 is unchanged.
* **Portuguese words.** milestone review: `revisão de marco` (docs/03), here "a revisão de um marco"; milestone's base: "a base do marco", as chapter 11 writes it; code changed: "código alterado", as chapter 11.
* **Terms of docs/03.** `waiting mark`, `milestone review` used as defined. No new term.
* **Sources.** None added or removed. **Cases.** None.
* **docs/06.** None from this page; the driver sets its line's marks.

**States.** Inapplicable: no screen.

**Visual reference.** Inapplicable: no screen.

**Out of scope.**

* The reason "what was read" and the resume suffix of the fourth case: chapter 14's, named by the next sentence (decision 4).
* docs/05 §4's sentence on the four cases: `docs05-four-cases-sentence`.
* Chapter 13's key points: already true (decision 5).

**Done when.**

* [x] Both editions written in the place the Contract names, the English first; parity green.
* [x] `git diff --numstat book/en/13-apply.md book/pt/13-apply.md` shows one changed line per edition, the first sentence of the section.
* [x] ``grep -c "or, in a milestone's review, when" book/en/13-apply.md`` gives 1, and ``grep -c "ou, na revisão de um marco, quando" book/pt/13-apply.md`` gives 1.
* [x] Chapter 13 still opens with its value; no filler, nothing useful cut; still five key points.
* [x] The Portuguese uses the Contract's words and no synonym.
* [x] No em dash; `make verify` green (build, parity, em dash, prose, width, links, disclosure).
* [x] The Delivery review ran on this delivery's paths and the files it created (docs/05 §5), and the page records it.
* [x] The author's approval of an anonymized passage: inapplicable, no Case A or Case B passage.
* [x] `make book` builds; the delivery ends with the paths of both PDFs for the author's review.
* [x] Page moved to `work/done/`, the line `[x]`, staged by explicit paths and this line's hunk of docs/06; the commit message suggested, `docs(ch13-four-waits): ...`.

**Built.**

* `book/en/13-apply.md:43` and `book/pt/13-apply.md:43`: the first sentence of "When the work cannot go on" (pt "Quando o trabalho não consegue seguir") names the fourth case, word for word as the Contract says; one changed line per edition, nothing else in chapter 13 touched.
* Divergences: none. Omissions: none. Decisions taken in /apply: none beyond the page's.

**Proof.** `make verify` green (build, parity, em dash, prose, width, links, disclosure); both greps of Done when give 1; `git diff --numstat` gives `1 1` per edition; `make book` builds `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

**Delivery review** (docs/05 §5, one read-only agent on Opus, on the two chapter diffs and this line's hunk of docs/06; the delivery created no file). Nothing breaks the page, docs/04 or the text: the four cases agree with chapter 14, docs/03's `waiting mark` and docs/05 §4; the words are chapter 11's; the Portuguese is faithful and uses the Contract's words; no em dash, no new pointer. One optional note, kept as written: "a milestone's review" instead of docs/03's literal "milestone review"; the Contract chose it and the Portuguese "a revisão de um marco" matches it, so no line was added.

```commit
docs(ch13-four-waits): name chapter 13's fourth case of waiting

- Chapter 13's list of when /apply stops adds a milestone review's reading that left part of the code unread
- Both editions, in chapter 11's words

work/done/ch13-four-waits.md
```
