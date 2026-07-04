"""Resize and compress site images. Generates WebP alongside JPEG/PNG."""
from __future__ import annotations

import os
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMG_DIR = ROOT / "assets" / "images"

# Max width by typical display size on the site
MAX_WIDTH = {
    "logo.png": 560,
    "founder-placeholder.jpg": 800,
}
DEFAULT_MAX = 1400
JPEG_QUALITY = 82
WEBP_QUALITY = 80
MIN_SAVE_BYTES = 8_192


def optimize_image(path: Path) -> None:
    name = path.name
    max_w = MAX_WIDTH.get(name, DEFAULT_MAX)
    suffix = path.suffix.lower()

    with Image.open(path) as img:
        img = img.convert("RGB") if suffix in {".jpg", ".jpeg"} else img
        w, h = img.size
        if w > max_w:
            new_h = round(h * max_w / w)
            img = img.resize((max_w, new_h), Image.Resampling.LANCZOS)

        if suffix in {".jpg", ".jpeg"}:
            tmp = path.with_suffix(path.suffix + ".tmp")
            img.save(tmp, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
            if tmp.stat().st_size < path.stat().st_size - MIN_SAVE_BYTES:
                tmp.replace(path)
            else:
                tmp.unlink(missing_ok=True)

            webp_path = path.with_suffix(".webp")
            img.save(webp_path, "WEBP", quality=WEBP_QUALITY, method=6)
        elif suffix == ".png":
            tmp = path.with_suffix(".png.tmp")
            img.save(tmp, "PNG", optimize=True)
            if tmp.stat().st_size < path.stat().st_size - MIN_SAVE_BYTES:
                tmp.replace(path)
            else:
                tmp.unlink(missing_ok=True)

            webp_path = path.with_suffix(".webp")
            rgb = img.convert("RGBA") if img.mode == "RGBA" else img.convert("RGB")
            rgb.save(webp_path, "WEBP", quality=WEBP_QUALITY, method=6)


def main() -> None:
    exts = {".jpg", ".jpeg", ".png"}
    files = sorted(p for p in IMG_DIR.iterdir() if p.suffix.lower() in exts)
    before = sum(p.stat().st_size for p in files)

    for path in files:
        try:
            optimize_image(path)
            kb = path.stat().st_size / 1024
            webp = path.with_suffix(".webp")
            webp_kb = webp.stat().st_size / 1024 if webp.exists() else 0
            print(f"  {path.name}: {kb:.0f} KB" + (f" + webp {webp_kb:.0f} KB" if webp.exists() else ""))
        except Exception as exc:
            print(f"  SKIP {path.name}: {exc}")

    after = sum(p.stat().st_size for p in files)
    webp_total = sum(p.stat().st_size for p in IMG_DIR.glob("*.webp"))
    print(f"\nJPEG/PNG: {before/1024/1024:.1f} MB -> {after/1024/1024:.1f} MB")
    print(f"WebP total: {webp_total/1024/1024:.1f} MB")


if __name__ == "__main__":
    main()
