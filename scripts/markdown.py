"""The Markdown reading shared by the scripts: front matter, the kind of each line, the masking of what a reader does not read, and note mentions."""

import re

FIELD = re.compile(r"^([A-Za-z_][\w-]*):\s*(.*?)\s*$")
# A note's key, as pandoc reads a label: any run without whitespace, `^`, `[` or `]`.
NOTE_DEFINITION = re.compile(r"^ {0,3}\[\^([^\]\s^\[]+)\]:")
NOTE_MENTION = re.compile(r"\[\^([^\]\s^\[]+)\]")
# A fenced block opens as CommonMark §4.5 reads a fence at the margin: at most three spaces,
# then a run of three or more backticks whose info string holds no backtick,
# or a run of three or more tildes with any info string;
# group 1 is the run, group 2 the info string.
FENCE_OPENING = re.compile(r" {0,3}(`{3,}(?!.*`)|~{3,})(.*)")


def front_matter(text):
    """Return (fields, body lines): the `key: value` fields of the front matter and the lines after it.

    Without a closed front matter, fields is empty and the body is every line.
    Values lose their surrounding quotes; the body starts at line len(lines) - len(body) + 1.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, lines
    fields = {}
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return fields, lines[i + 1:]
        match = FIELD.match(lines[i])
        if match:
            fields[match.group(1)] = match.group(2).strip("\"'")
    return {}, lines


def closes(line, run):
    """Whether line closes a fenced block opened by run, as CommonMark §4.5 reads it.

    The line is at most three spaces, then a run of run's character at least len(run) long,
    then only spaces or tabs to its end.
    """
    return re.fullmatch(" {0,3}" + re.escape(run[0]) + "{%d,}[ \t]*" % len(run), line) is not None


def blank(text):
    return " " * len(text)


def line_kinds(text):
    """Yield (kind, info) for each line of text.split("\\n"), in order.

    kind is "front" (the front matter, its `---` lines included; unclosed, it runs to the end),
    "fence" (a line that opens or closes a fenced block), "code" (a line inside one) or "text".
    info is the opening's info string for "fence" and "code" ("" on a closing line),
    for "text" whether the line starts inside an HTML comment, and None for "front".
    A fence opens only on a line that does not start inside a comment.
    """
    lines = text.split("\n")
    front = bool(lines) and lines[0].strip() == "---"
    fence, info = None, ""
    comment = False
    for index, line in enumerate(lines):
        if front:
            yield "front", None
            if index > 0 and line.strip() == "---":
                front = False
            continue
        if fence:
            if closes(line, fence):
                fence = None
                yield "fence", ""
            else:
                yield "code", info
            continue
        if not comment:
            opening = FENCE_OPENING.match(line)
            if opening:
                fence, info = opening.group(1), opening.group(2)
                yield "fence", info
                continue
        yield "text", comment
        comment = mask_inline(line, comment, True)[1]


def mask(text, keep_targets):
    """Return the lines of text with front matter, code and HTML comments as spaces.

    With keep_targets False, link and image targets `](…)` are blanked too.
    Line numbers and columns are those of the text.
    """
    out = []
    for line, (kind, info) in zip(text.split("\n"), line_kinds(text)):
        if kind == "text":
            out.append(mask_inline(line, info, keep_targets)[0])
        else:
            out.append(blank(line))
    return out


def target_end(line, i):
    """Given `](` at i, return the index of the `)` that closes the target, or the last index."""
    depth, j = 0, i + 1
    while j < len(line):
        if line[j] == "(":
            depth += 1
        elif line[j] == ")":
            depth -= 1
            if depth == 0:
                break
        j += 1
    return j


def mask_inline(line, comment, keep_targets):
    """Blank inline code, link targets and HTML comments; return (line, still inside a comment)."""
    chars = list(line)
    i = 0
    while i < len(line):
        if comment:
            end = line.find("-->", i)
            stop = len(line) if end < 0 else end + 3
            chars[i:stop] = blank(line[i:stop])
            i = stop
            comment = end < 0
            continue
        if line.startswith("<!--", i):
            comment = True
            continue
        if line[i] == "`":
            run = re.match(r"`+", line[i:]).group(0)
            end = line.find(run, i + len(run))
            if end < 0:
                i += len(run)
                continue
            stop = end + len(run)
            chars[i:stop] = blank(line[i:stop])
            i = stop
            continue
        if line.startswith("](", i):
            j = target_end(line, i)
            if not keep_targets:
                chars[i + 1:j + 1] = blank(line[i + 1:j + 1])
            i = j + 1
            continue
        i += 1
    return "".join(chars), comment


def mentions(line):
    """Return the keys of the notes cited on a masked line, in order; a definition marker at its start is not a citation."""
    definition = NOTE_DEFINITION.match(line)
    if definition:
        line = line[definition.end():]
    return NOTE_MENTION.findall(line)
