# ch13-apply-next

Decided before the author read it: the author's word for this run, relayed by the driver session on 2026-11-13, is "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão", so every question the documents leave open is answered by the agent's recommendation, marked "decided by the agent, the author corrects it in the review" (docs/05 §4, a command that says to decide alone). The page is built before the author reads it.

**Objective.** After chapter 13 the reader, developer or not, can say how `/apply` hands the delivery back: it tells them each next step, addressed to them (use what the delivery changed, review the staged diff, commit with the suggested message), then runs the kit's queue script though no one asked and shows its tree, its `next:` command written as their host invokes commands, so they never have to look up what comes after a delivery.

**Behaviour.** What the reader can do or explain afterwards:

* Say the ending in order: the next steps, each told to the person, use what changed as its user would and say in the session what is wrong, review the staged diff, commit with the suggested message (merging, on a delivery branch); then the queue script, run by `/apply` though no one asked, its tree shown and its `next:` written as the host invokes commands; and, last of all, which environment is at which version (already taught, unchanged).
* Say why the steps are addressed to the person, as a reason in the present: a step written as a bare order in the agent's own instructions is the agent's to follow, and a bare "commit" there contradicts its "never commit"; the kit's file words each step "Tell them to ...", so the agent says them and does none of them.
* Say why `/apply` runs the script unasked, as the error it prevents: the script answers whoever asks what may run now, and at the end of `/apply` no one has asked, so an ending that waits to be asked names no next command; on 2026-11-03 a person reported that `/apply` had ended without naming the next command.
* Read the tree `/apply lend-book` ends with, in the chapter's example: `return-book` free for `/propose`, `m1-review` waiting until `return-book` is defined, and `next: /propose return-book`, given as `/propose return-book` in Claude Code or `$propose return-book` in Codex.
* Edge, a session that ends without the tree: asked "`/apply` ended with the commit block and the environments but no queue tree; what do you do?", answer: it did not end as the kit says; ask it for the tree, which it draws by running the queue script.
* Failure, steps read as orders: asked "may `/apply` run `git commit` because its last message says 'commit with the suggested message'?", answer no: that step is told to the person; the agent commits only when the person asks, after their review (the chapter's `## Why it stops at the stage`, unchanged).
* In the Portuguese edition, the same, with docs/03's "árvore da fila", the chapters' own "script de fila" (pt ch14 :135) and "próximos passos" (pt ch13 :128), and "mesmo sem ninguém pedir" as the kit's Portuguese changelog says it.

**Contract.** Two chapter files; line numbers en at HEAD `2673874`, quoted beside each so a drift is found; pt follows en sentence for sentence at the same lines (pt :5, :128, :172 to :177 and :296 checked). The text is the agent's within these changes.

* **ch13** (`book/en/13-apply.md`, `book/pt/13-apply.md`)
  * C1, opening (:5, "your next steps written out and, last of all, which environment is at which version"): one clause, the next steps told to you and the queue tree with the next command. Still three sentences.
  * C2, owner of the rule, the `## Green is not done` bullet (:128, "Its last words are your next steps: use what the delivery changed as its user would, ... and then what may run next: the queue tree, with its free lines offered as one command written as your host invokes it, for a fresh session"): the steps stay the three they are, said as told to you; one sentence on why, in the present, quoting the kit's file in a short phrase ("*Tell them to review the staged diff, then to commit with the suggested message*", pt translated as pt :59 translates its quote) and saying a bare order there would be the agent's own and contradict "never commit"; then `/apply` runs the kit's queue script of chapter 14, though no one asked, and shows its tree with its `next:` written as your host invokes commands, the reason in the present (the script answers whoever asks, and at the end of `/apply` no one has). The free lines offered as one command, "for a fresh session" and "so a person new to the kit does not search the documentation for what comes after" stay, since the kit's file shows the tree as docs/05 §4 says and §4 offers the free lines as one command. Keep the rest of the bullet (the conversation ends with them, the manual, the environments, "never ends silent") as it is. The bullet may split in two at the queue script, the agent's choice. Say "last words", never that the steps open the message.
  * C3, the example (:172 to :177): ":172 Then it gives your next steps:" becomes "tells you"; steps 1 to 3 stay as they are; step 4 ("What may run next, from the queue tree, which ends `next: /propose return-book`: ...") stops being a numbered step and becomes, after the list, the script run though you did not ask, the tree below, and the prose of step 4 kept (`return-book` free for `/propose` since `lend-book` was `[>]`, `m1-review` written `· after all` waiting until `return-book` is defined, the command in a fresh session, `/propose return-book` in Claude Code or `$propose return-book` in Codex, chapter 8's table). Then the error, mirroring :180 and :181: on 2026-11-03 a person reported that `/apply` had ended without naming the next command, and if it ends without the tree, ask it for the tree. The tree, said written for this chapter, is the queue script's real output, run by the agent on a scratch queue of milestone 1 as `lend-book` left it (lines as chapter 11 :49 to :54 with `lend-book` `[x]`; a milestone 2 holding `suspension-end`, which :154 creates, changes nothing, the script drawing the first milestone with a line not `[x]`):

    ```
    milestone: Milestone 1: a librarian lends and takes back
    [ ] return-book · propose now
     └[ ] m1-review · waits: return-book not defined

    free for /apply, in order: none
    free for /propose, in order: return-book
    next: /propose return-book
    ```

    pt, from the same run on pt chapter 11's lines and heading (the script's words stay English, as pt chapter 14's tree has them):

    ```
    milestone: Marco 1: um bibliotecário empresta e recebe de volta
    [ ] devolver-livro · propose now
     └[ ] m1-review · waits: devolver-livro not defined

    free for /apply, in order: none
    free for /propose, in order: devolver-livro
    next: /propose devolver-livro
    ```
  * C4, key point 4 (:296, "its last words are your next steps, using what it built first and what may run next last, the queue tree, each command written out"): a clause, the steps told to you and the queue tree drawn by the script though no one asked, its `next:` written as your host invokes commands. Still five key points.

Terms of docs/03: queue tree, commit block, manual; none new. The queue script (pt "script de fila") has no row of its own: the `queue tree` row names it, and the chapters already say it so (pt chapter 14 :135). docs/03 checked: the `queue tree` row (:123, "/apply ends with it, as apply's says") holds, and the rows `command` (:20), `page` (:25), `commit block` (:125) and `manual` (:126) say nothing this line changes; docs/03 is unchanged. Sources: the installed `.claude/skills/apply/SKILL.md`, its last paragraph ("Then tell the person their next steps, each command written as this host invokes commands. ... Tell them to review the staged diff, then to commit with the suggested message ... Then run the queue script of docs/05 §4, though no one asked, and show its tree as §4 says, its `next:` command written for this host"); the kit's `CHANGELOG.md` and `CHANGELOG.pt.md`, `## 2026.11.03`, for the error and its date; `.agents/skills/propose/scripts/queue.sh` for the tree. No source note: the kit is taught as it is, and no note points to a file of focus-kit's repository (docs/04). Cases: none; the person who reported stays unnamed, as the changelog leaves them.

**States.** Inapplicable: a chapter, no screen.

**Visual reference.** Inapplicable: no screen, and no new kind of content (prose and a code block, as chapter 14 has); the Design slot says prototype, by choice (ADR-0019).

**Out of scope.**

* The last message opening with `🚨`, `⚠️` or `✅`, the delivery fixing its own flaws, a finding a line only when grave (:79, :105 to :107, :152 to :154), tests and verify's ceiling: `ch13-apply-findings` (M38).
* A line waiting on a prerequisite fix and dependent lines resolved at the end (:71 to :72, :124): `ch13-apply-after` (M39).
* How a blocked `/apply` ends beyond what :73 says: the kit's file leaves open whether its next steps and tree follow a blocked ending too, and chapter 13's blocked section is not this line's.
* :43 ("it ends with what may run next, the queue tree"): it holds as it is; C2 owns the rule, and the point is said once.
* Chapter 14's "Asked what may run now": it holds; the script still answers whoever asks, and chapter 14 is another line's (`ch14-15-after-all-dropped`, defined).
* The kit's history behind the error (the sentence the skill had before, the update after which it stopped): docs/04's "The kit as it is" keeps a kit change's history out.

**Done when.**

* [x] C1 to C4 read as the Contract says in both editions; docs/03 unchanged.
* [x] Both editions written; the chapter opens with its value; no filler and nothing useful cut; the date from the kit's changelog; the tree the queue script's real output; no "no longer" or earlier kit version in the text; no em dash; no run narration.
* [x] The error told without naming or hinting at a project or person: the disclosure scan green.
* [x] `make verify` green after the last edit, with its time.
* [x] `make book` builds both editions under the run's lock, both PDF paths recorded.
* [x] Delivery review by one read-only Opus agent, as docs/05 §5 says; only this delivery's paths and its docs/06 line staged; the page in `work/done/` and its commit message suggested.

**Decisions.**

* Decided by the agent, the author corrects it in the review: docs/03 has no wrong row; the `queue tree` row already says "/apply ends with it, as apply's says", and `kit-2026-11-03` left docs/03 as it was; so docs/03 stays out of the delivery, as the brief's scope guard says.
* On the author's word for this run, "Sim, como o changelog": the report of 2026-11-03 is told as the kit's changelog words it, with no project named, no place and no business detail; it is no Case A or Case B passage, so docs/05 §5's Case A and Case B slot asks nothing of this line.
* Decided by the agent, the author corrects it in the review: C2 owns the rule and its reason; the example holds the tree, the error and the check "ask it for the tree", as it already holds the environments' sentence and its Ninjobs evidence (:179 to :181), so the error is told once, where the reader sees what it prevents.
* Decided by the agent, the author corrects it in the review: the bare-sentences reason is taught in the present, with no date and no incident, since the changelog dates none for it and "could drop the whole list" is a possibility, not something that happened.
* Decided by the agent, the author corrects it in the review: the example shows the tree as a code block, the script's real output on the lending library, since the line says "showing its tree" and chapter 14 already teaches how to read one; step 4's prose stays to say what the tree means and how each host types `next:`.
* Decided by the agent, the author corrects it in the review: :43 stays as it is, and so does the blocked ending; both are named in Out of scope.
* From the documents: the rule (installed apply `SKILL.md`, the kit's changelog `## 2026.11.03`), the history kept out (docs/04 "The kit as it is"), five key points (docs/04), the scope kept off M38's and M39's sentences (docs/06, their lines).

## Outcome

Built on 2026-11-14 by /apply on trunk, before the author read it, on the author's word for this run relayed by the driver session: "Precisamos fechar todas as linhas de docs/06-Queue.md sem minha supervisão". The author reads the page and the diff at the end. The author authorized one commit per slug for this run; the driver session commits this delivery with the message below, and never pushes.

Chapter 13 had not changed since `2673874` (`git diff 2673874 HEAD` of both files empty), so the Contract's line numbers held. After the delivery, en and pt stay line for line:

* C1, :5: "your next steps told to you, the queue tree with the next command and, last of all, which environment is at which version" (pt "os seus próximos passos ditos a você, a árvore da fila com o próximo comando"). Still three sentences.
* C2, :128 and :129: the bullet split in two at the queue script, the agent's choice the Contract allowed. :128 keeps the three steps, now "each told to you", with "commit with the suggested message", then the quote "*Tell them to review the staged diff, then to commit with the suggested message*" (pt "*Diga à pessoa que revise o diff em stage e depois faça o commit com a mensagem sugerida*") and the reason in the present; the sentence on the steps ending with the conversation and the manual stays in it. :129: "Then, though no one asked, it runs the kit's queue script and shows its tree (chapter 14)", the free lines as one command for a fresh session, `next:` written the same way, "so a person new to the kit does not search the documentation for what comes after", the reason ("the script answers whoever asks what may run now, and at the end of `/apply` no one has asked"), then the environments sentence, unchanged.
* C3, :172 to :194: "Then it tells you your next steps:" (pt "Depois ele diz a você os seus próximos passos:"), steps 1 to 3 unchanged, step 4 removed; after the list, :179 the script run "though you did not ask" (pt "mesmo sem você pedir"), the tree said written for this chapter, the tree block, step 4's prose kept, :192 "An ending that waits to be asked names no next command: on 2026-11-03 a person reported that `/apply` had ended without naming the next command", :193 "ask it for the tree, which it draws by running the queue script". The environments paragraph follows, unchanged.
* C4, :312: "its last words are your next steps, each told to you, from using what it built to the commit, and then the queue tree, which it draws with the kit's queue script though no one asked, its `next:` written as your host invokes commands". Still five key points.
* docs/03 unchanged, as the Decisions say.

Proof: the tree is the kit's `queue.sh trunk`, the copy installed in `.agents/skills/propose/scripts/`, run on scratch queues outside the repository holding chapter 11's milestone 1 with `lend-book` `[x]` and a milestone 2 with `suspension-end`, en and pt (pt chapter 11's heading and slugs); both outputs are byte for byte the Contract's trees. `make verify` green after the last edit, in 11 seconds (10.8 s, under the five-minute ceiling); the disclosure scan in it green. `make book` under the run's lock built both editions: `output/one-page-at-a-time.pdf` and `output/uma-pagina-de-cada-vez.pdf` (EPUBs beside them).

Divergences and decisions taken in the build, each decided by the agent, the author corrects it in the review:

* The Portuguese example adds one clause the English has not, at pt :179: "e as palavras do script ficam em inglês, como o kit as imprime", since a Portuguese reader meets the script's English words here before chapter 14 says so (pt ch14 :138); docs/04 lets the Portuguese edition say such a thing where the reader first meets it. pt chapter 14 keeps its own sentence; the two say it once per chapter.
* The error is told with the changelog's date and its person unnamed, with "had ended without naming" in place of the changelog's "had stopped ... after an update", which is kit history (docs/04 "The kit as it is").
* The quote's Portuguese follows pt :59's way of translating a quote of the kit's file: the translation alone, in `"*...*"`, no note.

Delivery review: one read-only Opus agent read `git diff HEAD` of both chapters and this line of docs/06, against this page and docs/04, and re-ran the queue script on a scratch copy. It found no blocking fault and reported seven candidates:

1. Key point 4 read the tree as one of the person's steps and lost the commit from the steps. Fixed: "from using what it built to the commit, and then the queue tree ...; both are said in the conversation".
2. :192's "That is the error the unasked run prevents" pointed at nothing (pt awkward too). Fixed: "An ending that waits to be asked names no next command: ..." (pt "Um fim que espera a pergunta não diz o próximo comando: ...").
3. :128's dangling "told to you, the agent says ..." (pt "dito a você" agreeing with nothing). Fixed: "with each step told to you, the agent says them all and takes none" (pt "com cada passo dito a você, o agente os diz e não dá nenhum").
4. :129's two commands read as unrelated. Fixed: "its `next:`, the first free line's command" (pt "o da primeira linha livre").
5. pt :179's extra clause, and "desenhada do marco 1". Kept the clause, as decided above; fixed "desenhada a partir do marco 1".
6. The dated report reads as kit history? Kept: the page's Decisions and the run's word ("Sim, como o changelog") tell it so, as the error, not as a version.
7. docs/06's line says "no longer"; not reader-facing text, left as the line is.

Verify ran again after the fixes, green.

## For the review

* book/en/13-apply.md:181 and book/pt/13-apply.md:181: the example's tree holds while the queue script draws only the first open milestone; once M39's `ch14-queue-every-milestone` teaches it drawing every open milestone, this example's queue (milestone 2 holding `suspension-end`, which :154 creates) would also draw milestone 2 and offer `suspension-end`, so that line's /propose should re-run the script on this example and update the tree here.

```commit
docs(ch13-apply-next): teach /apply's told steps and unasked queue tree

- Chapter 13: the next steps told to the person, with the kit's reason
- Chapter 13: /apply runs the queue script unasked and shows its tree
- Example: the real tree after lend-book, and the report of 2026-11-03
- Opening and key point 4 say the steps and the tree; both editions

work/done/ch13-apply-next.md
```
