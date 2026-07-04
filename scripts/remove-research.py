"""Remove Research section links from all site pages."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NAV_LI = re.compile(
    r"\s*<li><a href='(?:\.\./|\./)research/index\.html'>Research</a></li>\n?",
    re.MULTILINE,
)
MOBILE_LINK = re.compile(
    r"<a href='(?:\.\./|\./)research/index\.html'>Research</a>",
)
FOOTER_LINK = re.compile(
    r"<a\s*\n?\s*href='(?:\.\./|\./)research/index\.html'>Research</a>",
)


def strip_research_links(text: str) -> str:
    text = NAV_LI.sub("", text)
    text = MOBILE_LINK.sub("", text)
    text = FOOTER_LINK.sub("", text)
    return text


def main() -> None:
    updated = 0
    for path in ROOT.rglob("*.html"):
        if path.parts[-2:-1] == ("research",):
            continue
        original = path.read_text(encoding="utf-8")
        text = strip_research_links(original)
        if text != original:
            path.write_text(text, encoding="utf-8")
            updated += 1

    research_dir = ROOT / "research"
    if research_dir.exists():
        shutil.rmtree(research_dir)

    print(f"Removed Research links from {updated} pages.")
    print("Deleted research/ directory.")


if __name__ == "__main__":
    main()
