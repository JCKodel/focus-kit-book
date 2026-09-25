"""The entry syntax shared by the checks: a plain entry, or `re:<pattern>`."""

import re


def compile_entry(entry):
    """Compile one entry, ignoring case; raises re.error on an invalid `re:` entry.

    A plain entry does not match inside a longer word: it gets `(?<!\\w)` in front
    when its first character is a word character, and `(?!\\w)` after when its last one is.
    """
    if entry.startswith("re:"):
        return re.compile(entry[3:], re.IGNORECASE)
    pattern = re.escape(entry)
    if re.match(r"\w", entry[0]):
        pattern = r"(?<!\w)" + pattern
    if re.match(r"\w", entry[-1]):
        pattern = pattern + r"(?!\w)"
    return re.compile(pattern, re.IGNORECASE)
