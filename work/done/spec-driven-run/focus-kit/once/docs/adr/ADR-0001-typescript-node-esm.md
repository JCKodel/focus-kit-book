# ADR-0001: TypeScript on Node, ES modules

**2026-09-25 · observed.** Context: the repository starts with `package.json` declaring `"type": "module"` and `tsconfig.json` with `strict`, target ES2022 and `module: NodeNext`. Decision: the module is written in strict TypeScript as ES modules and run by Node. Consequences: types are checked by the TypeScript compiler, not by Node, which only strips them; imports follow NodeNext resolution, whose interplay with running `.ts` directly is settled by `verify` (docs/01, Open questions).
