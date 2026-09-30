# pt-spec-change-terms

**Objective.** A Portuguese reader who learned "especificação" and "mudança" in chapter 3 meets the same two words in chapters 1, 4 and 13, and never an untranslated "spec", "specs", "change" or "changes" that they cannot be sure is the same thing.

**Behaviour.**

* Chapter 1's key point says "quando escrever a especificação vira o trabalho", not "a spec".
* Chapter 1's Ninjobs source note counts "mudanças pelo arquivo do OpenSpec", not "changes", as its body already says "35 mudanças do OpenSpec".
* Chapter 4 says "uma mudança com proposta, especificações, design e tarefas", "as mudanças" among the six places a decision lived, and "sem pasta de mudança", the form chapter 13 already uses; its Ninjobs source note says "mudanças pelo arquivo do OpenSpec".
* Chapter 13's list of what the process does not have says "Especificação formal" and "Delta de especificação", and a delta is "incorporado às especificações"; its source note says "os dois deltas de especificação".
* The quoted title "Spec Delta", the names Spec Kit and OpenSpec, code, paths and URLs stay as they are: they are what the artifacts print.
* The English edition is unchanged: "spec" and "change" are its terms.
* Finding F1 of the M4.1 review is settled.

**Contract.**

* Files and changes, each quoted phrase the reference, not the line number (today's lines in parentheses):
  * `book/pt/01-why-process.md`: "escrever a spec" → "escrever a especificação" (72); in `[^ninjobs]`, "changes pelo arquivo do OpenSpec" → "mudanças pelo arquivo do OpenSpec" (76).
  * `book/pt/04-birth-of-focus-kit.md`: "uma change com proposta" → "uma mudança com proposta" (9); "as changes, os ADRs" → "as mudanças, os ADRs" (16); "sem pasta de change" → "sem pasta de mudança" (28); in `[^ninjobs]`, "changes pelo arquivo do OpenSpec" → "mudanças pelo arquivo do OpenSpec" (54).
  * `book/pt/13-the-governor.md`: "**Spec formal:**" → "**Especificação formal:**" (48); "**Delta de spec:**" → "**Delta de especificação:**" and "incorporado às specs" → "incorporado às especificações" (49); in `[^spec-driven-run]`, "os dois deltas de spec" → "os dois deltas de especificação" (101).
* Nothing else in those sentences changes; gender and number agreement already fit ("uma mudança", "as mudanças", "a especificação").
* Terms of docs/03: none new. "especificação" is the fixed Portuguese of spec; "mudança", an OpenSpec change, is the word chapter 3 teaches, as in `pt-slot-term` and `pt-health-slice` (the first and second occurrences), a translation choice for another tool's vocabulary stays on the page, not in docs/03.
* Sources, cases, exercises: unchanged; the source notes change one word each, not what they cite.

**Out of scope.**

* "Spec Delta" in quotes (pt/13:49): the title OpenSpec's files print, quoted as the English quotes it.
* URLs and backticked names, such as `.../changes/add-client-cancellation/specs` and `add-client-cancellation`: they are paths.
* English text quoted from a run (pt/05:38, pt/10:439-440): real artifacts, shown as printed.
* "Spec-Driven Development" in the rules file excerpt (pt/02:76): a real artifact, and not what F1 names.
* Chapters other than 1, 4 and 13: the grep of the Portuguese edition finds no other bare "spec" or "change" outside quoted artifacts.
* Chapter 3's key point: `ch3-key-point-rules`, in flight, owns it.
* The English edition and docs/03: nothing to change.

**Done when.**

* [ ] The ten phrases changed as the Contract says, in both body and source notes.
* [ ] `grep -nwiE "changes?|specs?" book/pt/01-why-process.md book/pt/04-birth-of-focus-kit.md book/pt/13-the-governor.md` finds only Spec Kit, "Spec Delta" in quotes, backticked names and URLs.
* [ ] `make verify` green.
* [ ] `make book` run, and both PDF paths given to the author.
* [ ] Page in `work/done/`, `[x]` in docs/06, staged, commit message suggested.
