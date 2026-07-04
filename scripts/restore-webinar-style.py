"""Restore standalone webinar landing style (pre site-theme merge)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DL = Path(r"c:\Users\Admin\Downloads\files (1)")

TOPBAR = """
<nav class="webinar-topbar">
  <div class="container">
    <a href="../index.html" class="webinar-topbar__logo">
      <picture>
        <source srcset="../assets/images/logo.webp" type="image/webp">
        <img src="../assets/images/logo.png" width="280" height="80" alt="CureSoulLife — सृजन, साधना और मोक्ष" decoding="async">
      </picture>
    </a>
    <a href="#registration" class="webinar-topbar__cta">Reserve Free Seat</a>
  </div>
</nav>
"""

HERO_PHOTO = """
      <div class="hero__photo">
        <picture>
          <source srcset="../assets/images/founder-placeholder.webp" type="image/webp">
          <img src="../assets/images/founder-placeholder.jpg" alt="Sarvesh Mishra — founder of CureSoulLife" loading="eager" decoding="async">
        </picture>
      </div>"""

GUIDE_PHOTO = """
      <div class="guide__photo">
        <picture>
          <source srcset="../assets/images/founder-placeholder.webp" type="image/webp">
          <img src="../assets/images/founder-placeholder.jpg" alt="Sarvesh Mishra — Life Decoder and Inner Alchemy Architect" loading="lazy" decoding="async">
        </picture>
      </div>"""

HEAD_INDEX = """<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Life Reset™ Masterclass | CureSoulLife</title>
<meta name="description" content="Sarvesh Mishra के साथ Live Online Masterclass — अपनी ज़िंदगी को पहली बार समझिए। 25 July, 6:00 PM. Registration Free.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+Devanagari:wght@500;600;700&family=Noto+Sans+Devanagari:wght@400;500;600;700&family=Jost:wght@500;600;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Noto+Serif+Devanagari:wght@500;600;700&family=Noto+Sans+Devanagari:wght@400;500;600;700&family=Jost:wght@500;600;700&display=swap" rel="stylesheet"></noscript>
<link rel="stylesheet" href="../assets/css/webinar.css">
</head>
<body class="webinar-page">
"""

HEAD_WELCOME = HEAD_INDEX.replace(
    "<title>Life Reset™ Masterclass | CureSoulLife</title>",
    "<title>Welcome To CureSoulLife™</title>",
).replace('<body class="webinar-page">', '<body class="welcome-page webinar-page">')


def patch_index(text: str) -> str:
    body_start = text.find("<!-- ============ HERO")
    content = text[body_start:]
    text = HEAD_INDEX + TOPBAR + "\n" + content

    text = text.replace(
        """        <div class="hero__brand">
          <span class="mark">CureSoulLife™</span>
          <span class="tagline">Heal · Align · Awaken</span>
        </div>""",
        """        <div class="hero__brand">
          <a href="../index.html" style="color:inherit;text-decoration:none;display:flex;align-items:center;gap:12px;">
            <span class="mark">CureSoulLife™</span>
            <span class="tagline">Heal · Align · Awaken</span>
          </a>
        </div>""",
    )

    import re
    text = re.sub(
        r'<div class="hero__photo">\s*<div class="ph-note">.*?</div>\s*</div>',
        HERO_PHOTO.strip(),
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r'<div class="guide__photo">\s*<div class="ph-note">.*?</div>\s*</div>',
        GUIDE_PHOTO.strip(),
        text,
        count=1,
        flags=re.S,
    )
    text = text.replace('<script src="script.js"></script>', '<script src="../assets/js/webinar.js" defer></script>')
    return text


def patch_welcome(text: str) -> str:
    body_start = text.find("<section class=\"welcome-hero\">")
    content = text[body_start:]
    footer_end = content.find("<footer>")
    content = content[:footer_end]
    topbar = TOPBAR.replace('href="#registration"', 'href="index.html#registration"').replace(
        "Reserve Free Seat", "View Masterclass"
    )
    text = HEAD_WELCOME + topbar + "\n" + content
    text += """<footer>
  <div class="container">
    <p style="font-family:var(--serif); font-style:italic; font-size:19px; max-width:520px; margin:0 auto 26px;">"हर परिवर्तन उस क्षण से शुरू होता है जब व्यक्ति स्वयं से ईमानदारी से मिलने का निर्णय लेता है।"</p>
    <div class="mark">Welcome To CureSoulLife™</div>
    <div class="tag">Heal · Align · Awaken</div>
    <div class="support">हम 25 जुलाई को मिलेंगे। Support: <a href="mailto:support@curesoullife.org">support@curesoullife.org</a></div>
  </div>
</footer>
<script src="../assets/js/webinar.js" defer></script>
</body>
</html>
"""
    return text


def patch_css(css: str) -> str:
    extra = """
.hero__photo img,
.guide__photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center top;
}

.webinar-topbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.96);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(8px);
}
.webinar-topbar .container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 12px;
  padding-bottom: 12px;
}
.webinar-topbar__logo {
  display: flex;
  align-items: center;
  line-height: 0;
  text-decoration: none;
}
.webinar-topbar__logo img {
  display: block;
  width: auto;
  height: clamp(2rem, 0.35rem + 3.6vw, 2.75rem);
  max-width: min(220px, 52vw);
  object-fit: contain;
  object-position: left center;
}
.webinar-topbar__cta {
  font-family: var(--label);
  font-size: 13px;
  font-weight: 600;
  padding: 8px 16px;
  border-radius: var(--radius-s);
  border: 1px solid var(--ink);
  background: var(--ink);
  color: #fff;
  text-decoration: none;
  transition: background 0.2s var(--ease), border-color 0.2s var(--ease);
}
.webinar-topbar__cta:hover {
  background: var(--gold);
  border-color: var(--gold);
  color: var(--ink);
}
"""
    if ".webinar-topbar" not in css:
        css = css.rstrip() + "\n" + extra
    return css


def main() -> None:
    index = patch_index((DL / "index.html").read_text(encoding="utf-8"))
    welcome = patch_welcome((DL / "welcome.html").read_text(encoding="utf-8"))
    css = patch_css((ROOT / "assets" / "css" / "webinar.css").read_text(encoding="utf-8"))

    (ROOT / "webinar" / "index.html").write_text(index, encoding="utf-8")
    (ROOT / "webinar" / "welcome.html").write_text(welcome, encoding="utf-8")
    (ROOT / "assets" / "css" / "webinar.css").write_text(css, encoding="utf-8")
    print("Restored standalone webinar style.")


if __name__ == "__main__":
    main()
