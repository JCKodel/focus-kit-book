# ch09-key-points

**Objective.** A reader of chapter 9, in either edition, reads key points that name the same cause the gain names, the old process on Ninjobs with a decision in many places and checks blind to the product, and carry no count the gain does not give.

**Decided from the documents.**
1. Both findings hold against the text. L3: `book/en/09-birth-of-focus-kit.md` line 84 (key point 1) says "OpenSpec gave four screens in fifteen days" and that "its checks guarded the form", where the gain at line 79 says "the old process gave Ninjobs four screens in fifteen days, with every decision repeated in many places and checks that never caught a product error". The key point makes the tool the cause; the chapter's own account (§What went wrong, five causes, the third and fourth the author's: the full form required on every feature, 29 checks) makes the process the cause, and the author let complexity grow. L4: line 87 (key point 4) says "six places" while the gain and key point 1 say "many places". Portuguese: the same lines 84 and 87 of `book/pt/09-birth-of-focus-kit.md`.
2. The rule that binds: docs/04 §Numbers that prove, "`## What the team gains` gives the one number that sums the chapter, and each key point carries at most that number", and `plain-numbers` decision 3 and its Divergences, which cut "six places" and "29 checks" from the gain and key point 1 on purpose and left the counts in the story. Key point 4 was missed. The count "six places" is not restored to the gain: the claim is proved by the story (§What went wrong, cause 5), where "six places" stays.
3. Key point 4 keeps the structure ("Each rule of the kit answers a failure: ...") and the order of the six failures, and changes only the first item, from the count to the cause: a decision kept in many places. It is the failure that the rule "One page per delivery" answers in §Each rule and its failure, which names "the six places" and stays as it is.
4. Key point 1 changes its subject and nothing else: "the old process" in place of "OpenSpec", the words the gain uses. "Its checks" now belongs to the process. The chapter's Ninjobs sentence "Ninjobs started with OpenSpec" stays: it says what was used, not what caused the cost.
5. Key points 2, 3 and 5 are not touched: 2 already puts the cause on the author ("I lost KISS and YAGNI by requiring its full form on every feature"); 3's "thirteen days" and 5 carry no count the gain lacks ("thirteen" is the gain's number; "two checks" is in the gain).

**Behaviour.**

* A reader of §Key points reads in point 1: on Ninjobs the old process gave four screens in fifteen days: each decision lived in many places, and its checks guarded the form and never the product. Draft for /apply to polish within these limits (the subject is the process, the cause is the gain's, no count beyond four screens in fifteen days): "On Ninjobs, the old process gave four screens in fifteen days: each decision lived in many places, and its checks guarded the form and never the product." (pt: "No Ninjobs, o processo antigo deu quatro telas em quinze dias: cada decisão morava em muitos lugares, e as verificações do processo guardavam a forma e nunca o produto.")
* A reader of point 4 reads "Each rule of the kit answers a failure: a decision kept in many places, a build that decides as it goes, commands that drift, an outline that mixed plan and reasoning, checks blind to the product, and checks that grew unasked." (pt: "Cada regra do kit responde a uma falha: uma decisão guardada em muitos lugares, uma construção que decide enquanto anda, comandos que divergem, um roteiro que misturava plano e raciocínio, verificações cegas ao produto e verificações que cresceram sem ninguém pedir.")
* Checked, both editions, on the text of §Key points only (from its heading to the first `[^` or the end): `grep -n "OpenSpec\|six places\|seis lugares\|29"` finds nothing; "many places" / "muitos lugares" appears in point 1 and "a decision kept in many places" / "uma decisão guardada em muitos lugares" in point 4.
* The story keeps every count: 29 checks, 37,228 lines, four screens, fifteen days, "Six places for one truth", 91 deliveries, 19 boards, thirteen days. `grep -c "six places\|Six places\|seis lugares\|Seis lugares" book/*/09-birth-of-focus-kit.md` is as before the delivery (the opening of cause 5, "the six places" in §Each rule and its failure).
* A reader comparing the gain and the key points finds the same cause named in both and the same one number, four screens in fifteen days against the opening in thirteen; no key point names a count the gain does not.
* Fails: "six places", "29 checks" or another cut count back in the gain or the key points; OpenSpec or Spec Kit as the subject of a failure in a key point; a key point that names FOCUS or the architecture as the cause; one edition changed and not the other.

**Contract.**

* Files: `book/en/09-birth-of-focus-kit.md`, `book/pt/09-birth-of-focus-kit.md`; no other file.
* Sections and lines (same in both editions): §Key points (pt §Pontos-chave), point 1 (line 84) and point 4 (line 87). The story, the gain (lines 77 to 80) and points 2, 3 and 5 stay as they are.
* Terms of docs/03: none new. Sources: none cited in this chapter's sections (no `[^...]` in the key points); Ninjobs' numbers are the author's own counts, said so by the prologue. Cases: Ninjobs, as today; no Case A or Case B passage. Exercises: none (ADR-0017).
* docs/03, docs/04, docs/05: no change. docs/06: this line `[>]` by the driver, `[*]` when /apply starts, `[x]` by /apply.

**Deliveries in flight on the same chapter (work/).**

* `one-gain-section` (`[>]`, M15, last of the cuts): rewrites every chapter's key points so none restates the gain, as actions, at most five. It will rewrite points 1 and 4 again; this page is not wasted, since it removes a contradiction in the book as it stands and `one-gain-section` must start from points that carry no count the gain lacks. It keeps the gain's one number (docs/04 §Numbers that prove) and does not undo this page.
* `method-said-once` (`[>]`, M15, after `m14-review`): chapter 9 §Where it went (the database lint sentence) and §What the team gains ("no second telling of the four screens in fifteen days beyond the one number, and the 'six places' phrase stays named, not counted"). Same chapter, the gain section I read but do not change; this page agrees with that line (a phrase named, not counted). No line in common: that page works on §Where it went and the gain, this one on §Key points.
* `prologue-and-why`: "Chapter 9's story and chapter 3's count: unchanged"; the two hook numbers leave the prologue and chapters 9 and 19 own them. No conflict.
* `renumber-chapters` (after the merges): chapter 9 becomes chapter 6; links and "chapter N" are moved by its script. This page writes the current number.
* `ch03-restated-rule` (this batch): chapter 3's Ninjobs sentence takes the same cause, "the process I ran on OpenSpec". Different chapter, same direction.

**Out of scope.**

* The story's counts and the gain's wording: `plain-numbers` set them, `method-said-once` and `one-gain-section` shape them later.
* Other chapters that give "six places" or "29 checks" (4, 10, 18): they tell their own story with their own count (`method-said-once` fixes chapter 18's).
* Restoring any number `plain-numbers` cut.
* Making the key points actions rather than restatements: `one-gain-section`.

**Done when.**

* [ ] Both editions changed at points 1 and 4; the grep of Behaviour finds nothing in `book/en` and `book/pt`.
* [ ] Chapter 9 still opens with its value, keeps its gain with its number, no filler and nothing useful cut; the story's counts are as before.
* [ ] Every number still sourced; `make verify` green, disclosure scan included; no em dash.
* [ ] `make book` run; both PDF paths given to the author.
* [ ] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Decisions in the review.** Chosen alone, because the author could not answer; corrections go in the review.

* Point 1's subject becomes "the old process", the gain's own words (the line says the key points "give the cause its gain gives"); the alternative "the process I started with" was rejected as a second name for one thing. Source: the queue line and `m14-review` L3.
* Point 4's "six places" becomes "a decision kept in many places", not a restored count in the gain, because `plain-numbers` cut that count from the summary on purpose and the story proves it (docs/04 §Numbers that prove; `plain-numbers` Divergences). Source: `m14-review` L4.
* No number is restored; nothing is left without its proof.
* Points 2, 3 and 5 are left as they are (decision 5 above).
