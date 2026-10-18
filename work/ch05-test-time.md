# ch05-test-time

Draft, from the author's reading of the book on 2026-10-18.

* Agents write tests and do not care how long they run. If a test is slow and every delivery runs everything, every delivery is delayed. The author has seen agents write tests that took 20 minutes to run: 20 minutes on every delivery.
* The person is responsible for keeping the tests in order, time included: an extra reason for pure use cases, which are extremely fast to test; integration or E2E tests only where they make sense, or at the end of a milestone.
* If "milestone" is first named here, a basic gloss: what it is and how the kit generates it (one sentence, per early-no-forward-links).
* The 20 minutes is the author's own observation, on no named project; say it as such.
* A suggestion to the kit itself is in work/kit-proposals.md.
