#!/usr/bin/env python3
"""Build the PDF and the EPUB of both editions into output/, with pandoc, weasyprint and pypdf.

The PDF opens on the edition's cover, book/assets/cover-<edition>.pdf (A5, one page), prepended with pypdf;
the EPUB carries book/assets/cover-<edition>.png as its cover image.
Prints the path of each file it writes.
An error prints as `file:line: book: message`, or `Makefile:1: book: message` when it names no file, and exits 1.
"""

import html
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

from markdown import front_matter, mask

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "output"
PANDOC = ROOT / "pandoc"
ASSETS = ROOT / "book" / "assets"
EDITIONS = {
    "en": {"lang": "en", "name": "one-page-at-a-time"},
    "pt": {"lang": "pt-BR", "name": "uma-pagina-de-cada-vez"},
}
# ascii_identifiers: a heading's id drops its accents, as on the site, so one #anchor link works in both.
READ = ["-f", "markdown-tex_math_dollars+ascii_identifiers", "--file-scope", "--toc"]

YAML_FIELD = re.compile(r"^(\s*)(site_author|copyright|draft_banner):\s*(.*)$")
LOCALE = re.compile(r"^(\s*)- locale:\s*(\S+)")
CHAPTER_LINK = re.compile(r"\]\(((?:[0-9]{2}|A[0-9]+)-[^)#\s]+\.md)(\s+\"[^\"]*\")?\)")
PANDOC_PLACE = re.compile(r"\"([^\"]+)\" \(line (\d+), column \d+\)")
CHAPTER_START = re.compile(r"(?=<h1[ >])")
NOTES = re.compile(r'<aside id="footnotes[^"]*" class="footnotes[^"]*"[^>]*>.*?<ol[^>]*>\n?(.*?)</ol>\s*</aside>\n?', re.S)
NOTE_NUMBER = re.compile(r'(<a\s+href="#fn\d+"\s+class="footnote-ref"[^>]*><sup>)\d+(</sup>)')
NOTE_REF = re.compile(r"\[\^([a-z0-9-]+)\](?!:)")
NOTE_DEFINITION = re.compile(r"^\[\^([a-z0-9-]+)\]: ")


class Failed(Exception):
    pass


def unquote(value):
    if value[:1] == "'" and value[-1:] == "'":
        return value[1:-1].replace("''", "'")
    if value[:1] == '"' and value[-1:] == '"':
        return value[1:-1].replace('\\"', '"')
    return value


def site_values():
    """Read site_author, copyright and draft_banner from mkdocs.yml, per edition.

    The standard library has no YAML reader, so this reads the three keys by indentation:
    top level for English, under `- locale: pt` of the i18n plugin for Portuguese.
    """
    values = {"en": {}, "pt": {}}
    locale, indent = None, 0
    for line in (ROOT / "mkdocs.yml").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        depth = len(line) - len(line.lstrip())
        match = LOCALE.match(line)
        if match:
            locale, indent = match.group(2), len(match.group(1))
            continue
        if locale and depth <= indent:
            locale = None
        match = YAML_FIELD.match(line)
        if match:
            target = "en" if locale is None else locale
            if target in values:
                values[target].setdefault(match.group(2), unquote(match.group(3).strip()))
    values["pt"].setdefault("site_author", values["en"].get("site_author"))
    for edition, found in values.items():
        for key in ("site_author", "copyright", "draft_banner"):
            if not found.get(key):
                raise Failed(f"mkdocs.yml:1: book: no {key} for edition {edition}")
    return values


class TextWithURLs(HTMLParser):
    """HTML turned into text, each link followed by its URL in parentheses."""

    def __init__(self):
        super().__init__()
        self.parts, self.hrefs = [], []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.hrefs.append(dict(attrs).get("href"))

    def handle_endtag(self, tag):
        if tag == "a" and self.hrefs:
            href = self.hrefs.pop()
            if href:
                self.parts.append(f" ({href})")

    def handle_data(self, data):
        self.parts.append(data)


def html_to_text(markup):
    parser = TextWithURLs()
    parser.feed(markup)
    parser.close()
    return "".join(parser.parts).strip()


def index_values(edition):
    """Return (title, subtitle) of book/<edition>/index.md: its H1 and its first **...** line."""
    path = Path("book") / edition / "index.md"
    _, body = front_matter((ROOT / path).read_text(encoding="utf-8"))
    title = next((line[2:].strip() for line in body if line.startswith("# ")), None)
    subtitle = next(
        (line.strip()[2:-2] for line in body if re.fullmatch(r"\*\*[^*].*\*\*", line.strip())), None
    )
    if not title or not subtitle:
        raise Failed(f"{path}:1: book: needs an H1 and a **subtitle** line")
    return title, subtitle


def chapters(edition):
    folder = ROOT / "book" / edition
    numbered = sorted(folder.glob("[0-9][0-9]-*.md"))
    appendices = sorted(folder.glob("A[0-9]*-*.md"))
    return numbered + appendices


def anchor(name):
    """The id the H1 of a chapter gets, the target of a link to the chapter without #anchor."""
    return "chapter-" + Path(name).stem


def note_anchor(name, key):
    """The id at the start of a note's text, the target of every later mention of its key."""
    return f"note-{Path(name).stem}-{key}"


def prepare(source, names, banner):
    """Return (lines, source line of each line) of a chapter as pandoc reads it.

    The front matter goes; a draft gets the banner after its H1; the H1 gets the id `anchor`;
    a link to another chapter of the book without #anchor points to that id.
    A note keeps its first mention; every later mention of its key becomes a link to that note,
    showing its number, since pandoc prints one note per mention. Notes number from 1 per chapter.
    """
    text = source.read_text(encoding="utf-8")
    fields, body = front_matter(text)
    first = len(text.splitlines()) - len(body) + 1
    masked = mask("\n".join(body), keep_targets=True)
    lines, where = [], []
    heading_done = False
    notes = {}
    for offset, (line, seen) in enumerate(zip(body, masked)):
        number = first + offset
        # Edits as (start, end, text) on the columns of seen, applied from the right so none shifts another.
        edits = []
        definition = NOTE_DEFINITION.match(seen)
        if definition:
            edits.append((definition.end(), definition.end(), f"[]{{#{note_anchor(source.name, definition.group(1))}}}"))
        for match in NOTE_REF.finditer(seen):
            key = match.group(1)
            if key in notes:
                link = f"[^{notes[key]}^](#{note_anchor(source.name, key)}){{.footnote-ref}}"
                edits.append((match.start(), match.end(), link))
            else:
                notes[key] = len(notes) + 1
        for match in CHAPTER_LINK.finditer(seen):
            if match.group(1) in names:
                edits.append((match.end(1), match.end(1), "#" + anchor(match.group(1))))
        for start, end, new in sorted(edits, reverse=True):
            line = line[:start] + new + line[end:]
        # The mask blanks a code span, so a title that opens with one is checked on the line itself.
        if not heading_done and seen.startswith("# ") and re.match(r"# \S", line):
            heading_done = True
            if not line.rstrip().endswith("}"):
                line = line.rstrip() + " {#" + anchor(source.name) + "}"
            lines.append(line)
            where.append(number)
            if fields.get("status") == "draft":
                for extra in ["", "::: draft-banner", banner, ":::"]:
                    lines.append(extra)
                    where.append(number)
            continue
        lines.append(line)
        where.append(number)
    return lines, where


def notes_at_chapter_end(page):
    """Move the notes of each chapter of pandoc's HTML to the chapter's end, numbered from 1.

    pandoc's --reference-location=section ends the notes at the end of the innermost section,
    an H2, and numbers them through the whole book; the PDF wants them at the end of the chapter.
    """
    end = page.rfind("</body>")
    parts = CHAPTER_START.split(page[:end])
    for index, part in enumerate(parts):
        items = "".join(NOTES.findall(part))
        if not items:
            continue
        numbers = iter(range(1, part.count("footnote-ref") + 1))
        part = NOTE_NUMBER.sub(lambda match: f"{match.group(1)}{next(numbers)}{match.group(2)}", NOTES.sub("", part))
        parts[index] = (
            part + '<aside class="footnotes" role="doc-endnotes">\n<hr />\n<ol>\n' + items + "</ol>\n</aside>\n"
        )
    return "".join(parts) + page[end:]


def run(command, places, cwd=ROOT):
    """Run pandoc or weasyprint; print its warnings as findings, and on failure raise Failed with one finding."""
    done = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    messages = [line.strip() for line in done.stderr.splitlines() if line.strip()]
    if done.returncode != 0:
        message = " ".join(messages) or f"{command[0]} exited with {done.returncode}"
        raise Failed(finding(message, places))
    for message in messages:
        print(finding(message, places))


def finding(message, places):
    """`file:line: book: message` when the message names a chapter, `Makefile:1: book: message` otherwise.

    pandoc names the copy it read; the line becomes the line of the chapter in book/.
    """
    match = PANDOC_PLACE.search(message)
    if match and Path(match.group(1)).name in places:
        source, where = places[Path(match.group(1)).name]
        line = min(int(match.group(2)), len(where))
        number = where[line - 1] if line else 1
        text = (message[:match.start()].rstrip().removesuffix(" at") + message[match.end():]).strip()
        return f"{source}:{number}: book: {text}"
    return f"Makefile:1: book: {message}"


def build(edition, site, work):
    settings = EDITIONS[edition]
    title, subtitle = index_values(edition)
    author = site[edition]["site_author"]
    rights = html_to_text(site[edition]["copyright"])
    sources = chapters(edition)
    names = {source.name for source in sources}
    places = {}
    inputs = []
    for source in sources:
        lines, where = prepare(source, names, site[edition]["draft_banner"])
        copy = work / source.name
        copy.write_text("\n".join(lines) + "\n", encoding="utf-8")
        places[source.name] = (source.relative_to(ROOT), where)
        inputs.append(source.name)
    common = READ + [
        f"--resource-path={ROOT / 'book' / edition}:{ROOT / 'book'}",
        "-M", f"lang={settings['lang']}",
    ]

    front = work / "front.html"
    front.write_text(
        '<section class="title-page">\n'
        f'<h1 class="title">{html.escape(title)}</h1>\n'
        f'<p class="subtitle">{html.escape(subtitle)}</p>\n'
        f'<p class="author">{html.escape(author)}</p>\n'
        "</section>\n"
        f'<section class="rights-page">\n<p>{html.escape(rights)}</p>\n</section>\n',
        encoding="utf-8",
    )
    page = work / "book.html"
    run(
        ["pandoc", *inputs, *common, "--reference-location=section", "-s", "-t", "html5",
         "--css", (PANDOC / "pdf.css").as_uri(),
         "-M", f"pagetitle={title}",
         "--include-before-body", str(front), "-o", str(page)],
        places, work,
    )
    # The return arrow of a note comes with U+FE0E, which no font of the book has.
    text = notes_at_chapter_end(page.read_text(encoding="utf-8")).replace("\ufe0e", "")
    page.write_text(text, encoding="utf-8")
    body = work / "body.pdf"
    run(["weasyprint", "--base-url", str(ROOT / "book" / edition) + "/", str(page), str(body)], places)
    pdf = OUTPUT / f"{settings['name']}.pdf"
    with_cover(edition, body, pdf)

    epub = OUTPUT / f"{settings['name']}.epub"
    run(
        ["pandoc", *inputs, *common, "-t", "epub3",
         "--css", str(PANDOC / "epub.css"),
         "--epub-cover-image", str(cover(edition, "png")),
         "-M", f"title={title}", "-M", f"subtitle={subtitle}",
         "-M", f"author={author}", "-M", f"rights={rights}",
         "-o", str(epub)],
        places, work,
    )
    return [pdf, epub]


def cover(edition, suffix):
    """The edition's cover, book/assets/cover-<edition>.<suffix>; a missing one is a finding at its own path."""
    path = ASSETS / f"cover-{edition}.{suffix}"
    if not path.is_file():
        raise Failed(f"{path.relative_to(ROOT)}:1: book: cover not found")
    return path


def with_cover(edition, body, pdf):
    """Write pdf as the cover's one page followed by every page of body, keeping body's outline."""
    from pypdf import PdfReader, PdfWriter

    front = PdfReader(str(cover(edition, "pdf")))
    if len(front.pages) != 1:
        raise Failed(f"{cover(edition, 'pdf').relative_to(ROOT)}:1: book: the cover must be one page, not {len(front.pages)}")
    writer = PdfWriter()
    writer.append(front, import_outline=False)
    writer.append(PdfReader(str(body)))
    with open(pdf, "wb") as out:
        writer.write(out)


def main():
    for tool in ("pandoc", "weasyprint"):
        if shutil.which(tool) is None:
            print(f"Makefile:1: book: {tool} not found; install it (see README)")
            return 1
    try:
        import pypdf  # noqa: F401
    except ImportError:
        print("Makefile:1: book: pypdf not found; install it (see README)")
        return 1
    try:
        site = site_values()
        OUTPUT.mkdir(exist_ok=True)
        written = []
        for edition in EDITIONS:
            with tempfile.TemporaryDirectory() as work:
                written += build(edition, site, Path(work))
    except Failed as failure:
        print(failure)
        return 1
    for path in written:
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
