#!/usr/bin/env python3
"""Check repository-local links and images in Markdown documentation.

External links are deliberately excluded: network access is not required.
Fragments are not validated because GitHub's generated heading anchors can vary.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))", re.IGNORECASE)
HTML_LINK = re.compile(r"\b(?:href|src)\s*=\s*(['\"])(.*?)\1", re.IGNORECASE)
FENCE = re.compile(r"^\s*([\x60]{3,}|~{3,})")
SKIP_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


def check_reference(source: Path, reference: str, root: Path = ROOT) -> str | None:
    """Return an error message for a missing or escaped local path, else None."""
    reference = html.unescape(reference.strip())
    if not reference or reference.startswith(("#", "//")):
        return None
    parsed = urlsplit(reference)
    if parsed.scheme.lower() in SKIP_SCHEMES:
        return None
    if parsed.scheme or parsed.netloc:
        return None
    relative = unquote(parsed.path)
    if not relative:
        return None
    candidate = ((root / relative.lstrip("/")) if relative.startswith("/")
                 else (source.parent / relative)).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return f"link escapes repository: {reference}"
    if not candidate.exists():
        return f"missing local target: {reference}"
    return None


def references(text: str):
    """Yield (line number, reference) while skipping fenced code samples."""
    marker = None
    for number, line in enumerate(text.splitlines(), 1):
        match = FENCE.match(line)
        if match:
            current = match.group(1)
            if marker is None:
                marker = current
            elif current[0] == marker[0] and len(current) >= len(marker):
                marker = None
            continue
        if marker is not None:
            continue
        for item in MARKDOWN_LINK.finditer(line):
            yield number, (item.group(1) or item.group(2))
        for item in HTML_LINK.finditer(line):
            yield number, item.group(2)


def main() -> int:
    errors = []
    checked = 0
    documents = sorted(ROOT.rglob("*.md"))
    for document in documents:
        if ".git" in document.parts:
            continue
        for line, reference in references(document.read_text(encoding="utf-8")):
            result = check_reference(document, reference)
            checked += 1
            if result:
                errors.append(f"{document.relative_to(ROOT)}:{line}: {result}")
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {len(documents)} Markdown files and {checked} references: "
          f"{len(errors)} broken local links.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
