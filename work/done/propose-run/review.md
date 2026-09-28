# Review

The author's review of the page as first written, `skeleton-first.md`. It did not run as planned, as a turn of the headless session with `--continue`: the author opened Claude Code in the clinic, interactive, in a fresh session, and typed `/propose skeleton` with the request after the slug, so `/propose` read the documents and the page in `work/` again and worked on that page. The holes were first listed by the agent running this book's `/apply`, from its reading of the page against the clinic's documents; the author checked them and sent them as written. The agent asked two questions with the host's question form, which an interactive session offers, and the author chose an option in each.

## The request

Typed as `/propose skeleton`, a blank line, then this text, whole:

````markdown
1. Import check nobody asked for. The agent added "npm run verify fails when client code imports a *.server.ts file". The clinic's docs/05 §7 says a new check has to name an error that actually happened. The agent only says "without a check the rule relies on memory alone", and it doesn't say which tool would do the check.
2. Icons with no content. The manifest asks for 192 and 512 PNG icons, but nothing says what they show or where they come from, so /apply would invent them.
3. Screenshot baseline. The Visual reference only says "Plain, clean default styling", and a toHaveScreenshot baseline is tied to one machine's fonts. The agent itself admits that.
4. Migration test folder. The migration tests need a migrations folder, but the page ships the real folder empty and doesn't say the runner takes the folder as a parameter.
````

## The questions and the answers

The question form as the agent called it, then the answers the host returned:

````
[tool AskUserQuestion] {
  "questions": [
    {
      "question": "The icons and the manifest's name \"Clinic\" are both placeholders for the clinic's identity, which only exists after clinic-setup (the page already keeps the real name out of the heading for that reason). What should skeleton do with the web manifest?",
      "header": "Icons",
      "multiSelect": false,
      "options": [
        {
          "label": "Drop manifest (Recommended)",
          "description": "Take the manifest and 'Add to home screen' out of skeleton. Add a queue line 'install' in milestone 2, before deploy, when the clinic has a name. Nothing gets invented."
        },
        {
          "label": "Placeholder icon, exact",
          "description": "Keep the manifest. The page states the icon exactly: a white letter C on a solid #2f6f5e square, drawn as a committed SVG, with the 192 and 512 PNGs exported once from it and committed."
        },
        {
          "label": "You supply the icon",
          "description": "Keep the manifest. You put the 192 and 512 PNGs in the repository before /apply, and the page names their paths."
        }
      ]
    },
    {
      "question": "How should the screenshot proof of the page work?",
      "header": "Screenshot",
      "multiSelect": false,
      "options": [
        {
          "label": "Proof file, no baseline (Recommended)",
          "description": "Playwright checks the three states by their text. One screenshot of the 'ok' state at 390x844 is saved to work/done/skeleton-390x844.png for you to look at. verify doesn't compare pixels."
        },
        {
          "label": "Keep toHaveScreenshot",
          "description": "Keep the pixel baseline inside verify. It's tied to this machine's fonts, which is acceptable because there is one developer and no CI, but any font or browser update makes it fail."
        }
      ]
    }
  ]
}

[tool result] Your questions have been answered: "The icons and the manifest's name "Clinic" are both placeholders for the clinic's identity, which only exists after clinic-setup (the page already keeps the real name out of the heading for that reason). What should skeleton do with the web manifest?"="Drop manifest (Recommended)", "How should the screenshot proof of the page work?"="Proof file, no baseline (Recommended)". You can now continue with these answers in mind.
````

## The reply

The agent, after rewriting `work/skeleton.md` and adding a line to docs/06:

````markdown
I rewrote `work/skeleton.md` to fix all four points. The skeleton line in docs/06 was already marked `[>]`.

**How each point was fixed**
1. **Import check:** removed from Behaviour and Done when. Out of scope now says why: under docs/05 §7 a new check has to name an error that actually happened, and none has yet. The rule stays in docs/01 and ADR-0002 until one does.
2. **Icons:** the manifest is out of skeleton, as you chose. I added a line to docs/06 for a new delivery, `install`, in milestone 2 just before `deploy`: the manifest with the clinic's name and icon.
3. **Screenshot:** Playwright checks the three states by their text. A screenshot of the "ok" state is saved once to `work/done/skeleton-390x844.png` as proof, and `npm run verify` no longer compares pixels.
4. **Migration folder:** the Contract now spells out the runner `migrate(db, folder): Result<string[], MigrationFailed>`, including the shape of the error. Its tests use in-memory SQLite, as docs/04 says, plus a temporary folder of fixture files. There's also a test that the real, empty folder applies nothing.

**Choices I made on my own, so check these first**
- **`src/lib/result.ts` is created now.** The runner and the health `api.ts` both return a `Result`, which is the second use that AGENTS.md asks for. The old Out of scope line that postponed it contradicted that, so I removed it.
- **What "plain, clean default styling" means:** `system-ui` font, 16px padding on each side, left-aligned text, browser default colours.
- **Migration files that don't match `NNNN-<name>.sql` are ignored**, and a failed start exits with code 1.
- **Only one test uses a real file:** it checks that the `data/` folder and the SQLite file are created. All other migration tests run in memory.

Read the page and question it. Check that each Behaviour line can be verified, that the Contract is exact, and that Out of scope names everything you assumed was in. Ask for every correction here in this conversation. When the page is right, open a fresh session and type `/apply skeleton`.
````

The change to the page is `skeleton.diff`; the change to the queue is `queue.diff`, which also holds the mark of turn 2.
