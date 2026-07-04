"""Apply performance optimizations across all HTML pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FONT_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Playfair+Display:ital,wght@0,400;0,500;0,700;1,400"
    "&family=EB+Garamond:ital,wght@0,400;0,500;1,400"
    "&family=Jost:wght@300;400;500&display=swap"
)

FONT_BLOCK = f"""    <link rel='preconnect' href='https://fonts.googleapis.com'>
    <link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>
    <link href='{FONT_URL}' rel='stylesheet' media='print' onload="this.media='all'">
    <noscript><link href='{FONT_URL}' rel='stylesheet'></noscript>"""

FONT_PATTERN = re.compile(
    r"<link rel='preconnect' href='https://fonts\.googleapis\.com'>\s*"
    r"<link\s+href='https://fonts\.googleapis\.com/css2\?[^']+'\s+rel='stylesheet'>",
    re.MULTILINE,
)

SCROLL_REVEAL = re.compile(
    r"\s*<script src='(\.\./|\./)assets/js/scroll-reveal\.js'></script>",
    re.MULTILINE,
)

MAIN_SCRIPT = re.compile(
    r"<script src='((?:\.\./|\./)assets/js/main\.js)'></script>",
)


def wrap_img_with_picture(html: str) -> str:
    """Add WebP source for local asset images."""

    def repl(match: re.Match[str]) -> str:
        tag = match.group(0)
        src_match = re.search(r"src=['\"]([^'\"]+)['\"]", tag)
        if not src_match:
            return tag
        src = src_match.group(1)
        if not re.search(r"assets/images/.+\.(jpe?g|png)$", src, re.I):
            return tag
        webp = re.sub(r"\.(jpe?g|png)$", ".webp", src, flags=re.I)
        if "loading='eager'" in tag or 'loading="eager"' in tag:
            loading = " loading='eager' fetchpriority='high'"
        elif "loading=" in tag:
            loading = re.search(r"loading=['\"][^'\"]+['\"]", tag)
            loading = f" {loading.group(0)}" if loading else " loading='lazy'"
        else:
            loading = " loading='lazy'"
        if "decoding=" not in tag:
            loading += " decoding='async'"
        inner = re.sub(r"\s*loading=['\"][^'\"]+['\"]", "", tag)
        inner = re.sub(r"\s*fetchpriority=['\"][^'\"]+['\"]", "", inner)
        inner = re.sub(r"\s*decoding=['\"][^'\"]+['\"]", "", inner)
        return f"<picture><source srcset='{webp}' type='image/webp'>{inner[:-1]}{loading}></picture>"

    return re.sub(r"<img\b[^>]*src=['\"][^'\"]*assets/images/[^'\"]+['\"][^>]*>", repl, html)


def optimize_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    text = FONT_PATTERN.sub(FONT_BLOCK, text, count=1)
    text = SCROLL_REVEAL.sub("", text)
    text = MAIN_SCRIPT.sub(r"<script src='\1' defer></script>", text)

    if path.name == "index.html" and path.parent == ROOT:
        if "rel='preload' href='./assets/images/meditate.webp'" not in text:
            text = text.replace(
                FONT_BLOCK,
                FONT_BLOCK
                + "\n    <link rel='preload' href='./assets/images/meditate.webp' as='image' type='image/webp' fetchpriority='high'>"
                + "\n    <link rel='preload' href='./assets/images/logo.webp' as='image' type='image/webp'>",
                1,
            )
        text = wrap_img_with_picture(text)
        text = re.sub(
            r"(<picture><source srcset='\./assets/images/yoga\.webp'[^>]*>)"
            r"(<img src='\./assets/images/yoga\.jpg'[^>]*?) loading='eager' fetchpriority='high'",
            r"\1\2 loading='lazy'",
            text,
            count=1,
        )

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    updated = 0
    for path in ROOT.rglob("*.html"):
        if optimize_file(path):
            updated += 1
            print(f"updated {path.relative_to(ROOT)}")
    print(f"\n{updated} files updated")


if __name__ == "__main__":
    main()
