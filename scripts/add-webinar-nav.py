"""Add Webinars link to site navigation across all HTML pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DESKTOP_ROOT = (
    "<li><a href='./community/index.html'>Community</a></li>\n"
    "                <li><a href='./webinar/index.html'>Webinars</a></li>\n"
    "                <li><a href='./join/index.html'>Join</a></li>"
)
DESKTOP_SUB = (
    "<li><a href='../community/index.html'>Community</a></li>\n"
    "                <li><a href='../webinar/index.html'>Webinars</a></li>\n"
    "                <li><a href='../join/index.html'>Join</a></li>"
)

MOBILE_ROOT = (
    "<a href='./community/index.html'>Community</a><a href='./webinar/index.html'>Webinars</a><a\n"
    "                    href='./join/index.html'>Join</a>"
)
MOBILE_SUB = (
    "<a href='../community/index.html'>Community</a><a href='../webinar/index.html'>Webinars</a><a\n"
    "                    href='../join/index.html'>Join</a>"
)


def update_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    rel = path.relative_to(ROOT)
    depth = len(rel.parents) - 1 if rel.name != "index.html" or rel.parent != Path(".") else 0

    if "webinar/index.html" in text:
        return False

    if depth == 0 or (rel.parent == Path(".") and rel.name != "index.html"):
        text = text.replace(
            "<li><a href='./community/index.html'>Community</a></li>\n"
            "                <li><a href='./join/index.html'>Join</a></li>",
            DESKTOP_ROOT,
        )
        text = text.replace(
            "<a href='./community/index.html'>Community</a><a\n"
            "                    href='./join/index.html'>Join</a>",
            MOBILE_ROOT,
        )
        text = text.replace(
            "<a href='./community/index.html'>Community</a><a href='./join/index.html'>Join</a>",
            "<a href='./community/index.html'>Community</a><a href='./webinar/index.html'>Webinars</a><a href='./join/index.html'>Join</a>",
        )
    else:
        text = text.replace(
            "<li><a href='../community/index.html'>Community</a></li>\n"
            "                <li><a href='../join/index.html'>Join</a></li>",
            DESKTOP_SUB,
        )
        text = text.replace(
            "<a href='../community/index.html'>Community</a><a\n"
            "                    href='../join/index.html'>Join</a>",
            MOBILE_SUB,
        )
        text = text.replace(
            "<a href='../community/index.html'>Community</a><a href='../join/index.html'>Join</a>",
            "<a href='../community/index.html'>Community</a><a href='../webinar/index.html'>Webinars</a><a href='../join/index.html'>Join</a>",
        )

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    count = 0
    for path in ROOT.rglob("*.html"):
        if path.parts[-2:] == ("webinar", "index.html") or path.parts[-2:] == ("webinar", "welcome.html"):
            continue
        if update_file(path):
            count += 1
            print(path.relative_to(ROOT))
    print(f"\nUpdated {count} files")


if __name__ == "__main__":
    main()
