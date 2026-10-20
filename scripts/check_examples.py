#!/usr/bin/env python3
"""Run chapter 3's database-boundary examples, as the chapter prints them, in both editions.

For each edition, the TypeScript blocks that declare `ok` and `err`, the driver's failure class,
the synchronous boundary and the asynchronous one are read with markdown.py's fence rule,
written in chapter order to a temporary `.mts` file outside the repository, followed by the
cases below, and run by Node's type stripping, so the code under test is the chapter's own.
Each declaration must be in exactly one block; a block that holds several is written once.
A per-edition map names the edition's symbols and fields; the cases are the same for both.
Node 26.12.0 or later is required; there is no silent skip.
Prints one line per finding as `file:line: examples: message`; exits 1 when anything is printed.
"""

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from markdown import line_kinds
from repo_files import ROOT

NODE_MINIMUM = (26, 12, 0)
TIMEOUT_SECONDS = 60
CHAPTER = "03-simplicity-and-results.md"
TYPESCRIPT = {"ts", "typescript"}

# The symbols each edition declares (ch03-query-catch), and the fields of its database failure.
EDITIONS = {
    "en": {
        "symbols": {"ok": "ok", "err": "err", "DriverFailure": "DriverFailure", "query": "query", "queryAsync": "queryAsync"},
        "fields": {"code": "code", "message": "message", "DatabaseFailed": "DatabaseFailed"},
    },
    "pt": {
        "symbols": {"ok": "ok", "err": "err", "DriverFailure": "FalhaDoDriver", "query": "consultar", "queryAsync": "consultarAsync"},
        "fields": {"code": "codigo", "message": "mensagem", "DatabaseFailed": "BancoDeDadosFalhou"},
    },
}

# The cases, the same for both editions. They reach the chapter's code only through
# `subject` and `fields`, which the runner defines from the edition's map.
# Each prints `check-examples<TAB>PASS<TAB>case` or `...<TAB>FAIL<TAB>symbol<TAB>case: detail`, its whitespace
# folded to spaces, then `...<TAB>DONE<TAB>count`; other output of the chapter's code is ignored.
CASES = r"""
const MARK = "check-examples\t";
const outcomes: string[] = [];
const unhandled: unknown[] = [];

process.on("unhandledRejection", (reason) => {
	unhandled.push(reason);
});

function record(symbol: string, name: string, pass: boolean, detail: string) {
	const line = (text: string) => text.replace(/\s+/g, " ");

	outcomes.push(pass ? `${MARK}PASS\t${line(name)}` : `${MARK}FAIL\t${symbol}\t${line(`${name}: ${detail}`)}`);
}

function show(value: unknown): string {
	if (value instanceof Error) return `${value.name}("${value.message}")`;
	if (value instanceof Promise) return "a Promise";
	if (Array.isArray(value)) return `[${value.map(show).join(", ")}]`;
	if (typeof value === "object" && value !== null) {
		return `{ ${Object.entries(value).map(([key, inner]) => `${key}: ${show(inner)}`).join(", ")} }`;
	}

	return typeof value === "string" ? JSON.stringify(value) : String(value);
}

function isDatabaseFailure(result: any, message: string): boolean {
	return result?.ok === false
		&& result.error?.[fields.code] === fields.DatabaseFailed
		&& result.error?.[fields.message] === message;
}

function syncCase(name: string, run: () => unknown, expected: unknown) {
	try {
		const result: any = subject.query(run);

		record("query", name, false, `returned ${show(result)} instead of letting the thrown value pass`);
	} catch (thrown) {
		record("query", name, thrown === expected, `threw ${show(thrown)}, not the same value it was given`);
	}
}

async function asyncCase(name: string, run: () => Promise<unknown>, expected: unknown) {
	try {
		const result: any = await subject.queryAsync(run);

		record("queryAsync", name, false, `resolved to ${show(result)} instead of rejecting with the same reason`);
	} catch (thrown) {
		record("queryAsync", name, thrown === expected, `rejected with ${show(thrown)}, not the same reason`);
	}
}

const loan = { id: "L1" };
const bug = new TypeError("loan is undefined");
const plain = new Error("plain");
const control = { redirect: "/login" };
const odd = new RangeError("out of range");

{
	const result: any = subject.query(() => loan);

	record("query", "a value comes back in ok", result?.ok === true && result.value === loan, `returned ${show(result)}`);
}

try {
	const result: any = subject.query(() => {
		throw new subject.DriverFailure("connection lost");
	});

	record("query", "the driver's failure comes back as err", isDatabaseFailure(result, "connection lost"), `returned ${show(result)}`);
} catch (thrown) {
	record("query", "the driver's failure comes back as err", false, `threw ${show(thrown)}`);
}

syncCase("a TypeError from a bug passes as the same object", () => {
	throw bug;
}, bug);

syncCase("any other Error passes as the same object", () => {
	throw plain;
}, plain);

syncCase("a thrown string passes", () => {
	throw "boom";
}, "boom");

syncCase("a control object passes as the same object", () => {
	throw control;
}, control);

{
	const result: any = await subject.queryAsync(async () => loan);

	record("queryAsync", "an awaited value comes back in ok", result?.ok === true && result.value === loan, `resolved to ${show(result)}`);
}

try {
	const result: any = await subject.queryAsync(() => Promise.reject(new subject.DriverFailure("timeout")));

	record("queryAsync", "the driver's rejection, awaited in try, comes back as err", isDatabaseFailure(result, "timeout"), `resolved to ${show(result)}`);
} catch (thrown) {
	record("queryAsync", "the driver's rejection, awaited in try, comes back as err", false, `rejected with ${show(thrown)}`);
}

await asyncCase("any other rejection rejects with the same reason", () => Promise.reject(odd), odd);
await asyncCase("a rejected control object rejects with the same reason", () => Promise.reject(control), control);

await new Promise((settled) => setTimeout(settled, 0));

record("queryAsync", "no rejection escapes unhandled", unhandled.length === 0, `${unhandled.length} rejection(s) escaped: ${unhandled.map(show).join(", ")}`);

for (const outcome of outcomes) console.log(outcome);

console.log(`${MARK}DONE\t${outcomes.length}`);
"""
# The cases above, each recorded once: a run that records fewer or more is a finding.
CASE_COUNT = 11


def declares(symbol):
    """The pattern of a top-level declaration of symbol, as a function or a class."""
    return re.compile(r"^(?:export\s+)?(?:(?:async\s+)?function\s*\*?\s*|class\s+)" + re.escape(symbol) + r"\b")


def typescript_blocks(text):
    """Return each TypeScript block as (first code line number, its lines), read with markdown.py's fence rule."""
    blocks, current = [], None
    for number, (line, (kind, info)) in enumerate(zip(text.split("\n"), line_kinds(text)), 1):
        if kind == "code":
            if current is not None:
                current[1].append(line)
        elif kind == "fence":
            words = (info or "").split()
            if current is None and words and words[0].lower() in TYPESCRIPT:
                current = (number + 1, [])
            elif current is not None:
                blocks.append(current)
                current = None
            else:
                current = None
    if current is not None:
        blocks.append((current[0], current[1], "unclosed"))
    return blocks


def select(path, blocks, symbols):
    """Return (the blocks to run in chapter order, the line of each symbol's declaration, findings)."""
    chosen, lines, findings = [], {}, []
    for block in blocks:
        if len(block) == 3:
            findings.append(f"{path}:{block[0] - 1}: examples: this TypeScript block is never closed; close its fence")
    if findings:
        return chosen, lines, findings
    for role, symbol in symbols.items():
        pattern = declares(symbol)
        hits = [(block[0] + offset, block) for block in blocks for offset, line in enumerate(block[1]) if pattern.match(line)]
        if not hits:
            findings.append(f"{path}:1: examples: no TypeScript block declares {symbol}; the check needs exactly one")
            continue
        if len(hits) > 1:
            where = ", ".join(str(line) for line, _ in hits)
            for line, _ in hits:
                findings.append(f"{path}:{line}: examples: {symbol} is declared {len(hits)} times, at lines {where}; the check needs exactly one")
            continue
        lines[role] = hits[0][0]
        if hits[0][1] not in chosen:
            chosen.append(hits[0][1])
    chosen.sort(key=lambda block: block[0])
    return chosen, lines, findings


def node_finding():
    """A finding when Node is missing or older than NODE_MINIMUM, else None."""
    node = shutil.which("node")
    minimum = ".".join(map(str, NODE_MINIMUM))
    if node is None:
        return f"Makefile:1: examples: node not found; install Node.js {minimum} or later (see docs/manuals/build-the-book-from-a-clone.md)"
    version = subprocess.run([node, "--version"], capture_output=True, text=True).stdout.strip()
    match = re.fullmatch(r"v(\d+)\.(\d+)\.(\d+)", version)
    if not match or tuple(map(int, match.groups())) < NODE_MINIMUM:
        return f"Makefile:1: examples: node {version or 'of unknown version'} found; Node.js {minimum} or later is required (see docs/manuals/build-the-book-from-a-clone.md)"
    return None


def program(blocks, edition):
    """Return (the chapter module, the Markdown line of each of its lines, the runner).

    The chapter module is the chosen blocks in chapter order and an export of the edition's symbols;
    a line the chapter did not write maps to the chapter line before it, where Node reports a block left open.
    The chapter's blocks export nothing themselves; an `export` there would declare a name twice.
    The runner imports those symbols under the names the cases use: that import is the edition's map.
    """
    source, origin = [], []
    for start, block in blocks:
        for offset, line in enumerate(block):
            source.append(line)
            origin.append(start + offset)
        source.append("")
        origin.append(origin[-1])
    symbols, fields = EDITIONS[edition]["symbols"], EDITIONS[edition]["fields"]
    source.append("export { " + ", ".join(dict.fromkeys(symbols.values())) + " };")
    origin.append(origin[-1])
    runner = [
        "import { " + ", ".join(name if name == role else f"{name} as {role}" for role, name in symbols.items())
        + f' }} from "./chapter-{edition}.mts";',
        "const subject = { " + ", ".join(symbols) + " };",
        "const fields = { " + ", ".join(f"{key}: {value!r}" for key, value in fields.items()) + " };",
    ] + CASES.split("\n")
    return "\n".join(source) + "\n", origin, "\n".join(runner) + "\n"


def run(path, edition, text):
    """Run the edition's examples and return the findings."""
    symbols = EDITIONS[edition]["symbols"]
    chosen, lines, findings = select(path, typescript_blocks(text), symbols)
    if findings:
        return findings
    source, origin, runner = program(chosen, edition)
    with tempfile.TemporaryDirectory(prefix="check-examples-") as folder:
        chapter_path = Path(folder) / f"chapter-{edition}.mts"
        chapter_path.write_text(source, encoding="utf-8")
        runner_path = Path(folder) / f"cases-{edition}.mts"
        runner_path.write_text(runner, encoding="utf-8")
        try:
            done = subprocess.run(
                ["node", "--no-warnings", str(runner_path)],
                capture_output=True, text=True, timeout=TIMEOUT_SECONDS, cwd=folder,
            )
        except subprocess.TimeoutExpired:
            return [f"{path}:{lines['queryAsync']}: examples: the cases did not finish in {TIMEOUT_SECONDS} seconds"]
    mark = "check-examples\t"
    outcomes = [line[len(mark):].split("\t", 2) for line in done.stdout.splitlines() if line.startswith(mark)]
    for outcome in outcomes:
        if outcome[0] == "FAIL":
            symbol = outcome[1] if len(outcome) > 1 else ""
            detail = outcome[2] if len(outcome) > 2 else "failed"
            findings.append(f"{path}:{lines.get(symbol, 1)}: examples: {symbols.get(symbol, symbol)}: {detail}")
    counted = [outcome for outcome in outcomes if outcome[0] == "DONE"]
    recorded = sum(1 for outcome in outcomes if outcome[0] in ("PASS", "FAIL"))
    if done.returncode != 0 or not counted:
        findings.append(crash(path, done, origin, chapter_path.name))
    elif recorded != CASE_COUNT:
        findings.append(f"{path}:1: examples: {recorded} cases ran; {CASE_COUNT} were expected")
    return findings


def crash(path, done, origin, name):
    """A finding for a run that did not finish: at the Markdown line of the first chapter line Node names, or line 1."""
    error = done.stderr
    line = 1
    match = re.search(re.escape(name) + r":(\d+)", error)
    if match and 0 < int(match.group(1)) <= len(origin):
        line = origin[int(match.group(1)) - 1]
    messages = [text.strip() for text in error.splitlines() if re.match(r"\s*\w*(Error|Exception)\b", text)]
    message = messages[0] if messages else (error.strip().splitlines() or [f"node exited {done.returncode}"])[-1]
    return f"{path}:{line}: examples: the examples did not run: {message}"


def main(argv):
    """With no argument, both editions of chapter 3; with paths, those files, each read as the edition of its folder."""
    finding = node_finding()
    if finding:
        print(finding)
        return 1
    paths = [Path(argument) for argument in argv] or [ROOT / "book" / edition / CHAPTER for edition in EDITIONS]
    findings = []
    for path in paths:
        edition = path.parent.name
        shown = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        if edition not in EDITIONS:
            findings.append(f"{shown}:1: examples: no edition named {edition}; the folder must be one of {', '.join(EDITIONS)}")
            continue
        if not path.is_file():
            findings.append(f"{shown}:1: examples: the chapter is missing")
            continue
        findings += run(shown, edition, path.read_text(encoding="utf-8"))
    for finding in findings:
        print(finding)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
