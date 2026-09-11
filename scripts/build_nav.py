#!/usr/bin/env python3
"""Stamp shared nav/footer partials into every docs/*.html page.

Usage: python3 scripts/build_nav.py
Run from the repo root (or anywhere — paths are resolved relative to this
file). Rewrites the content between marker comments in every docs/*.html
file (excluding docs/_partials/*) using the current content of
docs/_partials/nav.html and docs/_partials/footer.html.

Re-run this after editing either partial, or after adding a new
docs/*.html page, before committing.
"""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
PARTIALS = DOCS / "_partials"

MARKERS = {
    "NAV": PARTIALS / "nav.html",
    "FOOTER": PARTIALS / "footer.html",
}


def stamp(html: str, name: str, partial_content: str) -> str:
    pattern = re.compile(
        rf"(<!-- {name}:START -->)(.*?)(<!-- {name}:END -->)", re.DOTALL
    )
    if not pattern.search(html):
        return html
    return pattern.sub(
        lambda m: f"{m.group(1)}\n{partial_content.strip()}\n{m.group(3)}", html
    )


def build() -> list[Path]:
    for partial_path in MARKERS.values():
        if not partial_path.exists():
            raise FileNotFoundError(f"missing partial: {partial_path}")
    partial_contents = {name: path.read_text() for name, path in MARKERS.items()}

    changed = []
    for page in sorted(DOCS.glob("*.html")):
        original = page.read_text()
        updated = original
        for name, content in partial_contents.items():
            updated = stamp(updated, name, content)
        if updated != original:
            page.write_text(updated)
            changed.append(page)
    return changed


if __name__ == "__main__":
    changed_files = build()
    for p in changed_files:
        print(f"stamped {p.relative_to(DOCS.parent)}")
    print(f"{len(changed_files)} file(s) updated")
