# ADR-0006: No screen; a feature is a function

**2026-09-25 · decided in /analyze.** Context: the product is used by the clinic's staff through code that calls it. Decision: there is no screen; every feature is a function the module exports, taking and returning plain data. Consequences: no UI, no screen proof, no States or Visual reference in delivery pages; tests exercise the exported functions.
