# Proposals for focus-kit

Not a delivery of this repository: suggestions from the author's reading on 2026-10-18, for the author to take to focus-kit's own repository. The book teaches the kit as it is; when a kit version carries one of these, an update milestone teaches it.

1. **Test time** (from ch05-test-time). Agents write tests without minding how long they run; the author has seen a 20-minute suite run on every delivery. The kit could ask /apply to keep the per-delivery test run fast: pure use cases tested in-process, integration and E2E tests run where they pay or at a milestone's review, and a slow test reported, not added silently.
2. **A mark for "if there is time"** (from ch11-queue-grows). Agents tend to add lines, and a milestone of 5 lines may end with 50. Analyse whether a mark such as `[+]`, for an optional improvement a milestone may close without, is worth adding, or whether a later milestone of improvements already does it.
