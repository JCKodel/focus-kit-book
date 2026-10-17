# ch26-what-counts

**Objective.** A reader of chapter 26, in either edition, reads for Skitka's wrong recommendations who followed how many of what, and for the cost arm's three runs what each percentage compares, without opening the study or the run's record.

**Decided from the documents.**
1. Both findings hold against the text and against their sources. L9: `book/en/26-asking-for-more.md` line 34 says "When the aid recommended something wrong, on six occasions, all but one participant followed at least one." The noun is gone ("at least one" what), and "participant" does not say which participants (only those with the aid could follow a wrong recommendation). Source: `work/done/ask-for-more-experiment-run/sources.md` row 3, Skitka, Mosier and Burdick 1999, p. 999: "Only one participant made no commission errors", of the participants who had the aid. L10: line 139 says "In every run the challenged setup answered the five questions in 14% to 26% less time, and wrote fewer output tokens in two runs and 9% more in the third." The review said line 152; it is line 139 in both editions. "Every run" and "two runs" do not say which runs (the three of the cost arm, defined at line 113: each run records a first answer and a challenged one), nor what the time is compared with, nor what it counts. Source: the run's `README.md`, §Cost: the five questions per setup: seconds 53 to 39, 60 to 49, 81 to 70 (26%, 18% and 14% less), output tokens 4,746 to 3,448, 5,545 to 3,961, and 5,997 to 6,537 (9% more), each being the sum of the setup's five fresh sessions. The percentages hold.
2. L9 restores the noun and the group, not the 65% average. `plain-numbers` decision 2 cut the average on purpose ("a fact said in two numbers"), and the claim "all but one" still has its proof: it is the number that says how many followed. The sentence is not left without proof. No group size is written: the record gives none for the group with the aid, and a count is not invented (decision 2 of `plain-numbers`: no number rounded or invented).
3. L10 names what the comparison is: in each of the cost arm's three runs, the challenged setup against the first-answer setup of the same run, over the five questions asked in five fresh sessions. The percentages and the "9% more" stay (sourced by the record); the per-run seconds and tokens do not return to the text (docs/04 §Numbers that prove, `plain-numbers`). The sentence before it, "all 30 answers were correct", is not touched.
4. The sentences keep their place in their sections. Skitka's paragraph is in §Why the first answer feels final, the cost arm's paragraph in §What the protocol bought, and what it cost.

**Behaviour.**

* A reader of §Why the first answer feels final reads, after "those with the aid were right 59% of the time against 97% without it", that on six wrong recommendations all but one of the participants who had the aid followed at least one of them. Draft for /apply to polish within these limits (the noun, the group, "all but one", no 65%, no group size): "When the aid recommended something wrong, on six occasions, all but one of the participants who had the aid followed at least one of the wrong recommendations." (pt: "Quando o auxílio recomendou algo errado, em seis ocasiões, todos os participantes que tinham o auxílio, menos um, seguiram ao menos uma das recomendações erradas.")
* A reader of §What the protocol bought, and what it cost reads, after "all 30 answers were correct, first and challenged", what the percentages compare. Draft: "In each of the cost arm's three runs, the five questions took the challenged setup 14% to 26% less time than the first-answer setup of the same run, and its five sessions wrote fewer output tokens in two runs and 9% more in the third." (pt: "Em cada uma das três execuções do braço do custo, as cinco perguntas levaram de 14% a 26% menos tempo na preparação desafiada do que na da primeira resposta da mesma execução, e as suas cinco sessões escreveram menos tokens de saída em duas execuções e 9% mais na terceira.")
* Checked, both editions: `grep -n "In every run\|Em todas as execu" book/*/26-asking-for-more.md` finds nothing; `grep -n "followed at least one\|seguiram ao menos uma" book/*/26-asking-for-more.md` finds the sentence with "of the wrong recommendations" / "das recomendações erradas" after it.
* `grep -nE "65%|3[.,]92|23[.,]1" book/*/26-asking-for-more.md` finds nothing (the cut Skitka values do not return), as `plain-numbers` checked.
* The numbers the sentence keeps are 14%, 26%, two of three runs and 9%; a reader who opens the run's record finds the five-question table (`work/done/ask-for-more-experiment-run/README.md`, §Cost: the five questions per setup) and recomputes them from its seconds and output columns. That record is already the chapter's `[^ask-for-more-run]`, cited at the start of this section; no note is added to the sentence.
* The table, the 1-to-5 scoring, the cost of the protocol (2.9 to 8.8 times, 2.7 to 9.4 times) and the key points are unchanged.
* Fails: a restored 65%, 41%, per-run seconds or tokens; "every run" back without the three runs named; a group size invented for the aid group; one edition changed and not the other.

**Contract.**

* Files: `book/en/26-asking-for-more.md`, `book/pt/26-asking-for-more.md`; no other file.
* Sentences (same line in both editions today): §Why the first answer feels final, line 34; §What the protocol bought, and what it cost, line 139. Nothing else changes.
* Terms of docs/03: none new ("run", "arm", "pair" are used as the chapter defines them at line 113). Sources: `[^skitka-1999]` and `[^ask-for-more-run]` unchanged, same number of references in both editions. Cases: none; no Case A or Case B passage. Exercises: none (ADR-0017).
* docs/03, docs/04, docs/05: no change. docs/06: this line `[>]` by the driver, `[*]` when /apply starts, `[x]` by /apply.

**Deliveries in flight on the same chapter (work/).**

* `ch22-26-team-cut` (`[>]`, M15, after `m14-review`): rewrites chapter 26: the challenge protocol moves before §Why the first answer feels final; Randazzo's paragraph and note leave; §Why the first answer feels final keeps Skitka and Dell'Acqua; §What the protocol bought keeps `[^ask-for-more-run]`, the table, the scoring, and the session-limit story in one sentence; the gain in three sentences. Its Out of scope says "the protocol's text and the experiment's numbers: unchanged". The two sentences this page rewrites travel with their paragraphs and are not named by that page. /apply of `ch22-26-team-cut` finds them by words, not by line (that page says line numbers are not cited), and keeps them as this page leaves them. No conflict; this line runs first.
* `one-gain-section` (`[>]`, M15, last): rewrites the gain and the key points of chapter 26; neither sentence is in them, so no common line. Key point 5 carries "9 of 9" and "3 to 9 times", not the cost arm's percentages.
* `renumber-chapters`: chapter 26 gets a new number; the links to it are moved by its script; this page cites no link to a chapter number inside its two sentences.
* `plain-numbers` (done, M13): cut the 65% and the per-arm seconds on purpose; this page respects it (decisions 2 and 3).

**Out of scope.**

* The other Skitka sentences (59% against 97%, 80 students) and the other studies: they carry what they count.
* The session-limit story, Dell'Acqua and Lee: not named by the findings.
* Restoring the cut average, per-run seconds or tokens (`plain-numbers`).
* Chapter 26's order and its gain and key points: `ch22-26-team-cut`, `one-gain-section`.

**Done when.**

* [x] Both editions changed at line 34 and line 139; the greps of Behaviour hold in `book/en` and `book/pt`.
* [x] Chapter 26 still opens with its value, keeps its gain with its number, no filler and nothing useful cut.
* [x] Every number still sourced; every `[^key]` keeps a reference and a definition in both editions; `make verify` green, disclosure scan included; no em dash.
* [x] `make book` run; both PDF paths given to the author.
* [x] Page in `work/done/`, the line `[x]`, staged by its paths and its hunk of docs/06, commit message in a `commit` block.

**Decisions in the review.** Chosen alone, because the author could not answer; corrections go in the review.

* L9 restores the noun and the group ("of the participants who had the aid", "of the wrong recommendations") and not the 65% average: `plain-numbers` cut it on purpose and "all but one" still proves the claim. If the author wants the size of the effect as a percentage, the average of 65% is the number to restore, with `sources.md` row 3's caution (an error rate per event, not a share of participants).
* L10 compares each run's challenged setup with the first-answer setup of the same run and keeps the percentages, with no per-run values. Source: `plain-numbers` decision 2 and the run's README.
* No new note on the L10 sentence: the same record is cited at the start of the section (docs/04 Evidence: a source note only where the reader gains something to open).
* The review's line 152 is line 139; the finding is the same.

**What /apply did.**

* Both editions, line 34: the Skitka sentence now names the group and the noun: "all but one of the participants who had the aid followed at least one of the wrong recommendations" (pt: "todos os participantes que tinham o auxílio, menos um, seguiram ao menos uma das recomendações erradas"). Line 139: the cost arm's sentence names the three runs and the comparison inside each run. No 65%, no group size, no per-run seconds or tokens.
* Numbers rechecked against the run's README, §Cost: the five questions per setup: seconds 53 to 39, 60 to 49, 81 to 70 are 26%, 18% and 14% less; output tokens fall in runs 1 and 2 and rise from 5,997 to 6,537 (9%) in run 3. Skitka against `sources.md` row 3: "Only one participant made no commission errors".
* Behaviour's greps hold in `book/en` and `book/pt`: "In every run" and "Em todas as execu" find nothing; "followed at least one" and "seguiram ao menos uma" find line 34 with "of the wrong recommendations" and "das recomendações erradas" after them; `65%|3[.,]92|23[.,]1` finds nothing.
* Proof: `make verify` green (build, parity, em dash, prose, links, disclosure); `make book` built `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf`.
* Divergences: none. Omissions: none.

**Decisions in /apply.** Chosen alone, as the batch rules say; corrections go in the review.

* L9 uses the page's drafts word for word, in both editions.
* L10 polishes the draft's "its five sessions" to "the challenged setup's five sessions" (pt: "as suas cinco sessões" to "as cinco sessões da preparação desafiada"): after "the first-answer setup of the same run", "its" could read as that setup or that run.

```commit
docs(ch26-what-counts): chapter 26 says what each of its numbers counts

- Skitka: all but one of those with the aid followed a wrong recommendation
- cost arm: each run's challenged setup against its first-answer setup
- both editions; no cut number returns

work/done/ch26-what-counts.md
```
