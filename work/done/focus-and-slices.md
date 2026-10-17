# focus-and-slices

**Objective.** After this chapter a reader can organize code in vertical slices, name the four pieces of FOCUS and what each forbids, pass a dependency only where a test passes a fake, and answer "what happens when event X arrives?" with one test, in one chapter where the lending orchestrator is shown once.

**Behaviour.**

* A reader opens on the pain of chapter 6 (a change to lending is a change to five folders; an agent loads five folders to learn one feature) and reaches the slice, then the four pieces, then the one event one new state walk, then dependencies only where a fake exists, in that order; no section repeats a point another made.
* A reader sees the `lendRequested` orchestrator once, in the "One event, one new state" section, and the "Dependencies only where a fake exists" section refers to it by name and shows only its signature line.
* A reader finds the dependency rule with one attribution (Martin, 2012) and screaming architecture with one sentence; Cockburn and the 2017 book are gone.
* Failure: a reader looking for ".NET world... SOLID", "Some find a mediator redundant... I keep both", or Model-View-Intent does not find them.
* A reader finds the C of FOCUS in at most three sentences: the layers are Clean Architecture's, the correction is the orchestrator, and the use case receives no repository; the walk-through section carries the rest.
* A reader finds the steps of the walk-through as the code and six one-line captions, not as prose that the code then repeats.
* A reader finds the client and server sharing use cases in the gain section, since it is the gain the review found outside it.
* Edge: the Ninjobs sentence "I required every piece on every feature... eight files" is said in the merged chapter 4 (`simplicity-and-results` opens with it) and here appears as half a sentence with a pointer, in "When a piece pays its way".
* Edge: "S, Scalable" keeps one sentence and no claim beyond isolation and a test per piece; the book gives no evidence for more, and the key point says the same.
* Edge: one gain section and five key points for the whole chapter; the "What this gives an agent" section is folded into the gain.

**Contract.**

* **One file, both editions:** `06-focus.md` (pt same name), H1 "6. FOCUS: features, not layers, and the four pieces" (pt: "6. FOCUS: funcionalidades, não camadas, e as quatro peças"); `07-four-pieces.md` removed with `git rm` in both editions.
* **Sections, in order:**
  1. Opening, three sentences.
  2. `## The problem`: chapter 6's problem section, plus chapter 7's second paragraph (a rule lives wherever someone needed it first; nobody answers by reading one place).
  3. `## Vertical slices`, `## What one feature is`, `## Where shared code lives`: chapter 6's sections unchanged, preceded by a four-sentence `## The dependency rule` taken from "Layers, and what they were for": the problem layers answered, Martin's dependency rule with `[^martin-clean-2012]`, the screaming-folders sentence with `[^martin-screaming]`, and the sentence that this book keeps the rule and drops the folder per layer. `[^martin-clean-2017]` and `[^cockburn-hexagonal]` removed.
  4. `## FOCUS, letter by letter`: chapter 7's section with C cut to three sentences (the pointer to chapter 6 removed, since it is this chapter), U without the MVI sentence, S as one sentence.
  5. `## The four pieces` and `### Drivers and services`: unchanged.
  6. `## One event, one new state`: chapter 7's section with the six numbered steps reduced to one line each, the types block and the orchestrator block kept as they are, and the "Three things the code shows" bullets of chapter 6 (`lendRepositories` as the parameter, the fake, the clock as a value) placed after the block, once.
  7. `## Dependencies only where a fake exists`: chapter 6's section, minus the ".NET world" and SOLID paragraph, minus the second copy of the orchestrator; keeps `[^fowler-injection]` and `[^seemann-composition-root]`, the line "a piece receives a dependency as a parameter only where its test passes a second implementation", and the signature `lendRequested(event, repositories = lendRepositories, today)` as its only code.
  8. `## The orchestrator elsewhere`: the names in other stacks, one paragraph, `[^bloc]` and `[^mediatr]` kept; the mediator-versus-controller debate cut; the client-and-server paragraph moved to the gain.
  9. `## When a piece pays its way`: chapter 7's section; the Ninjobs sentence shortened to half a sentence with a pointer to chapter 4.
  10. `## What the team gains`: a change touches one folder and an agent reads one slice; "what happens when event X arrives?" is one test; client and server share use cases, so the client's decision cannot disagree with the server's. No number; the baseline sentence is the prologue's.
  11. `## Key points`: five, merged from both lists.
* **Cuts, by first words:** "He developed it in the book Clean Architecture"; "Alistair Cockburn had drawn"; "The .NET world shows the habit"; "Model-View-Intent (MVI)"; "Some find a mediator redundant... I keep both"; chapter 6's full orchestrator block (lines 98 to 117); chapter 7's step prose where the code shows it; both "What this gives an agent" sections; chapter 7's "No study measures a team..." sentence.
* **Notes removed:** `[^martin-clean-2017]`, `[^cockburn-hexagonal]`, `[^clean-architecture]` (chapter 7's duplicate of `[^martin-clean-2012]`, merged into one key). Kept: `[^martin-clean-2012]`, `[^martin-screaming]`, `[^bogard-vertical-slice]`, `[^fowler-injection]`, `[^seemann-composition-root]`, `[^bloc]`, `[^mediatr]`.
* **Pointers:** every `](07-four-pieces.md)` and "chapter 7" in `book/`, docs/00 (Contents, Audience), docs/03 (FOCUS, orchestrator, use case, repository, view rows), docs/04 (the orchestrator example in §Say it where the doubt is born) and ADR-0016 (an amendment line only) resolves to chapter 6 or the merged file; chapter 12's "chapter 6 and chapter 7" becomes "chapter 6". The list on this page.
* **Terms:** FOCUS, feature, slice, orchestrator, use case, repository, view, driver, service, fake, as docs/03 has them; ADR-0016 (the book's definition of FOCUS) is unchanged in substance.
* **Code:** the two blocks of chapter 7 and the signature line; Portuguese names in the pt edition as today.
* **Cases:** Ninjobs, half a sentence with a pointer.

**Out of scope.**

* The tests of the four pieces: chapter 8.
* `Result`, the boundary and the exhaustive switch: chapter 4 after `simplicity-and-results`.
* Renumbering 8 to 26: `renumber-chapters`.

**Done when.**

* [x] One chapter in both editions, `07-four-pieces.md` gone from both, same headings; opens with the problem; the orchestrator shown once; one source per point; no filler and nothing useful cut (every rule of the two chapters is in the merged one or named as cut above).
* [x] No link to `07-four-pieces.md` and no "chapter 7"/"capítulo 7" that means the old chapter left in `book/`, docs/00, docs/03, docs/04; ADR-0016 amended with one line; the list on this page.
* [x] Parity of notes green; the Portuguese code keeps its Portuguese names.
* [x] `make verify` green; `make book` builds and both PDF paths are given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, the commit suggested in a `commit` block.

**Decisions taken from the documents.**

* The orchestrator is shown once, in the walk-through: docs/04 §Context before an excerpt wants an artifact to be a whole unit, and DRY as chapter 4 applies it.
* The client-and-server gain moves to the gain section: docs/04 §Say it where the doubt is born cuts the other way too, a gain the body states and the gain section omits is misplaced.
* The chapter keeps the name FOCUS in its title because ADR-0006 names the method by the kit and ADR-0016 defines FOCUS as the book's; the slice is the F.

**Decisions in the review.**

* The file is `06-focus.md`, as recommended.

**Decisions taken alone in /apply** (batch rule: no questions).

* The Portuguese H1 is "6. FOCUS: features, não camadas, e as quatro peças", not the Contract's "funcionalidades": docs/03's `feature` row says the Portuguese edition says "feature", never "funcionalidade", and the book had no use of it.
* The orchestrator kept is chapter 7's synchronous block, unchanged, with `repositories: LoanRepositories` required and no default, because chapter 8's test calls it as `lendRequested(event, today, repositories)`. The Contract's signature `lendRequested(event, repositories = lendRepositories, today)` matched neither block, so the dependencies section shows `lendRequested(event, today, repositories)`, and `lendRepositories` appears nowhere.
* The bullets after the block are three: the repositories as a parameter, a test passing fakes (with the definition of a fake and the whole flow proven with no database and no screen, which C no longer carries), and the clock as a value. Chapter 7's "The flow never goes back" sentence is cut, since U says it. In the dependencies section, chapter 6's orchestrator and clock bullets became the lead sentence and the walk-through's bullet; the server repository, use case and view bullets stay.
* `[^martin-clean-2012]` is cited twice: at the dependency rule and at C's claim about Martin's drawing, a claim from that source.
* The gain keeps one sentence saying it has no number, with the prologue as its reason, since docs/04 §A gain per chapter asks for that sentence until `one-gain-section`.
* F is one sentence pointing to the slices above, since its two sentences restated `## Vertical slices`; after the .NET cut, "The habit solves" became "Injecting everywhere solves", which had lost its antecedent.
* The Ninjobs half sentence keeps "the fault was the requirement", pointing to chapter 4, which tells it whole.
* docs/04 §Say it where the doubt is born keeps its history: "first: the orchestrator of chapter 7, now chapter 6 after `focus-and-slices`"; docs/04 §Chapter shape's H1 example becomes chapter 6's.

**What happened.**

* `book/{en,pt}/06-features-not-layers.md` moved to `06-focus.md` and rewritten to the Contract's eleven parts; `book/{en,pt}/07-four-pieces.md` removed. Same 13 H2 headings and one H3 in both editions.
* Cut as the page names: "He developed it in the book", Cockburn's hexagon, the .NET and SOLID paragraph, MVI, the mediator-versus-controller debate, chapter 6's orchestrator block, chapter 7's step prose, both "What this gives an agent" sections (their agent sentences are in the gain), "No study measures a team", S's "holds at any size". Notes removed: `[^martin-clean-2017]`, `[^cockburn-hexagonal]`, `[^clean-architecture]`.
* Pointers resolved, both editions: chapter 4 "the function around the rule that chapter 7 builds" to chapter 6; chapter 8's two links to `07-four-pieces.md` to `06-focus.md`, chapter 6; chapter 9 "the four pieces of chapter 7" to chapter 6; chapter 10 "the architecture of chapter 7: ... vertical slices (chapter 6)" to "the architecture of chapter 6: ... vertical slices"; chapter 12 "chapter 6 and chapter 7" (two links) to one link to chapter 6. docs/00 Contents: entries 6 and 7 become "6 FOCUS: features, not layers, and the four pieces"; Audience names no chapter 6 or 7, unchanged; OD-4's quote of the kit's pointer untouched, as `od4-kit-pointer` says. docs/03: no FOCUS, orchestrator, use case, repository or view row names a chapter, so nothing changed. The READMEs, both `index.md`, `mkdocs.yml`, `scripts/` and `pandoc/` name no chapter title or file of these two. docs/04: the two lines above. ADR-0016: one amendment.
* Left as they are: docs/04 §Tests and ADR-0008, whose "chapter 7" is the `/brainstorm` chapter before `rewrite`; the comment in `pandoc/pdf.css`, a generic example; the kit's installed skill copies, which the author repoints with the kit.
* Chapter numbers 8 to 26 are left for `renumber-chapters`; with this line `[x]`, every line its `after` names is done, and it keeps its `[>]`.

**Proof.**

* `grep -rn "07-four-pieces|06-features-not-layers|[Cc]hapter 7|[Cc]apítulo 7" book docs/00-Product.md docs/03-Domain.md docs/04-Conventions.md` finds only OD-4's quote and the two docs/04 history lines named above.
* Citations per edition, en and pt equal: `[^martin-clean-2012]` 2, `[^martin-screaming]` 1, `[^bogard-vertical-slice]` 1, `[^fowler-injection]` 1, `[^seemann-composition-root]` 1, `[^bloc]` 1, `[^mediatr]` 1.
* The Portuguese code keeps its names (`emprestimoPedido`, `RepositoriosDeEmprestimo`, `estadoDe`, `buscarMembro`).
* `make verify` green; `make book` built both editions, and the PDFs are `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.

```commit
docs(focus-and-slices): chapters 6 and 7 become one chapter, FOCUS

- ch6: slices, the four letters and the four pieces in one chapter
- ch6: the orchestrator shown once; client and server in the gain
- ch7 removed; every pointer to it now names chapter 6
- docs/00 contents, docs/04 examples and ADR-0016 follow
- both editions

work/done/focus-and-slices.md
```
