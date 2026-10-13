# Publish the site

## What it does and when

Puts the book's website, both editions, at https://jckodel.github.io/focus-kit-book/ as `main` reads now.
It happens on every push to `main`: there is no separate publish command.
Push when a delivery has been committed and you want readers to see it.
A chapter not yet done carries `status: draft` and shows a banner, so `main` can be published at any time.

## What must be in place

* Push rights to `JCKodel/focus-kit-book`.
* Once per repository: Settings, Pages, Source set to "GitHub Actions" (not "Deploy from a branch").
* The secret `DISCLOSURE_DENYLIST` set in the repository, because the job `pages` runs only after the job `verify` is green, and `verify` fails without the list (`set-up-the-disclosure-list.md`).
* Locally, `make verify` green on the commit you push, so the job `verify` does not stop the publish.

## Steps

1. On `main`, with the delivery committed: `make verify`.
2. `git push origin main`.
3. Open https://github.com/JCKodel/focus-kit-book/actions and follow the run of the workflow `verify`: the job `verify` first, then `pages`.

## How to tell it worked

The job `pages` ends green and its step `deploy` shows the site's address.
The site shows the change; a new chapter appears in the navigation of both editions, the Portuguese one under `pt/`.
A browser may show the old page for a few minutes; reload without the cache.

## How to undo it

Pages keeps no older version to roll back to.
Revert the commit that brought the change, `git revert <commit>`, and push `main`: the job `pages` publishes the reverted state.

## What breaks if a step is skipped

* Source left as "Deploy from a branch": the job `pages` fails at its deploy step and the site stays as it was.
* Secret missing or `make verify` red: the job `verify` fails, `pages` never starts, and the site stays as it was.
* Pushing a branch other than `main`: `verify` runs, `pages` does not; nothing is published.
