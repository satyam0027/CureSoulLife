"""Retheme webinar pages to match main site."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NAV = """    <nav class='navbar' id='navbar'>
        <div class='navbar__inner container'><a href='../index.html' class='navbar__logo'><picture><source srcset='../assets/images/logo.webp' type='image/webp'><img
                    src='../assets/images/logo.png' width='280' height='80'
                    alt='CureSoulLife — सृजन, साधना और मोक्ष' loading='eager' fetchpriority='high' decoding='async'></picture></a>
            <ul class='navbar__menu'>
                <li><a href='../index.html'>Home</a></li>
                <li class='has-dropdown'><a href='../about/index.html'>About</a>
                    <div class='dropdown'><a href='../about/index.html'>About CureSoulLife</a><a
                            href='../about/mission.html'>Mission</a><a href='../about/vision.html'>Vision</a><a
                            href='../about/philosophy.html'>Philosophy</a><a href='../about/the-movement.html'>The
                            Movement</a><a href='../about/core-values.html'>Core Values</a></div>
                </li>
                <li class='has-dropdown'><a href='../framework/index.html'>Framework</a>
                    <div class='dropdown'><a href='../framework/index.html'>Overview</a><a
                            href='../framework/five-dimensions.html'>Five Dimensions</a><a
                            href='../framework/human-suffering.html'>Human Suffering</a><a
                            href='../framework/life-purpose.html'>Life Purpose</a><a
                            href='../framework/methodology.html'>Methodology</a></div>
                </li>
                <li class='has-dropdown'><a href='../knowledge/index.html'>Knowledge</a>
                    <div class='dropdown'><a href='../knowledge/spiritual-wisdom.html'>Spiritual Wisdom</a><a
                            href='../knowledge/human-psychology.html'>Human Psychology</a><a
                            href='../knowledge/astrology-destiny.html'>Astrology &amp; Destiny</a><a
                            href='../knowledge/philosophy-of-life.html'>Philosophy of Life</a><a
                            href='../knowledge/tantra-energy.html'>Tantra &amp; Energy</a><a
                            href='../knowledge/case-studies.html'>Case Studies</a></div>
                </li>
                <li class='has-dropdown'><a href='../practices/index.html'>Practices</a>
                    <div class='dropdown'><a href='../practices/yoga.html'>Yoga</a><a
                            href='../practices/meditation.html'>Meditation</a><a
                            href='../practices/breathwork.html'>Breathwork</a><a
                            href='../practices/energy-practices.html'>Energy Practices</a><a
                            href='../practices/detoxification.html'>Detoxification</a></div>
                </li>
                <li class='has-dropdown'><a href='../retreats/index.html'>Retreats</a>
                    <div class='dropdown'><a href='../retreats/consciousness-retreat.html'>Consciousness Retreat</a><a
                            href='../retreats/youth-transformation.html'>Youth Transformation</a><a
                            href='../retreats/women-awakening.html'>Women Awakening</a><a
                            href='../retreats/corporate-leadership.html'>Corporate Leadership</a><a
                            href='../retreats/silence-retreat.html'>Silence Retreat</a><a
                            href='../retreats/index.html'>View All Retreats -&gt;</a></div>
                </li>
                <li class='has-dropdown'><a href='../centers/index.html'>Centers</a>
                    <div class='dropdown'><a href='../centers/india.html'>India</a><a
                            href='../centers/dubai.html'>Dubai</a><a href='../centers/vietnam.html'>Vietnam</a><a
                            href='../centers/uae.html'>UAE</a><a href='../centers/upcoming.html'>Upcoming Centers</a>
                    </div>
                </li>
                <li><a href='../research/index.html'>Research</a></li>
                <li><a href='../community/index.html'>Community</a></li>
                <li><a href='index.html'>Webinars</a></li>
                <li><a href='../join/index.html'>Join</a></li>
            </ul>
            <div class='navbar__end'><a href='#registration' class='btn btn--primary btn--sm navbar__book'>Reserve Free Seat</a><button
                type='button'
                class='navbar__hamburger' id='hamburger'
                aria-label='Open menu' aria-expanded='false' aria-controls='mobileMenu'><span></span><span></span><span></span></button>
            </div>
        </div>
        <div class='mobile-menu' id='mobileMenu' role='dialog' aria-label='Site navigation'>
            <div class='mobile-menu__inner'>
                <a href='../index.html'>Home</a>
                <div class='mobile-accordion'><button class='accordion-trigger'>About</button>
                    <div class='accordion-panel'><a href='../about/index.html'>About CureSoulLife</a><a
                            href='../about/mission.html'>Mission</a><a href='../about/vision.html'>Vision</a><a
                            href='../about/philosophy.html'>Philosophy</a><a href='../about/the-movement.html'>The
                            Movement</a><a href='../about/core-values.html'>Core Values</a></div>
                </div>
                <div class='mobile-accordion'><button class='accordion-trigger'>Framework</button>
                    <div class='accordion-panel'><a href='../framework/index.html'>Overview</a><a
                            href='../framework/five-dimensions.html'>Five Dimensions</a><a
                            href='../framework/human-suffering.html'>Human Suffering</a><a
                            href='../framework/life-purpose.html'>Life Purpose</a><a
                            href='../framework/methodology.html'>Methodology</a></div>
                </div>
                <div class='mobile-accordion'><button type='button' class='accordion-trigger'>Knowledge</button>
                    <div class='accordion-panel'><a href='../knowledge/index.html'>Overview</a><a
                            href='../knowledge/spiritual-wisdom.html'>Spiritual Wisdom</a><a
                            href='../knowledge/human-psychology.html'>Human Psychology</a><a
                            href='../knowledge/astrology-destiny.html'>Astrology &amp; Destiny</a><a
                            href='../knowledge/philosophy-of-life.html'>Philosophy of Life</a><a
                            href='../knowledge/tantra-energy.html'>Tantra &amp; Energy</a><a
                            href='../knowledge/case-studies.html'>Case Studies</a></div>
                </div><a href='../practices/index.html'>Practices</a><a href='../retreats/index.html'>Retreats</a><a
                    href='../centers/index.html'>Centers</a><a href='../research/index.html'>Research</a><a
                    href='../community/index.html'>Community</a><a href='index.html'>Webinars</a><a
                    href='../join/index.html'>Join</a>
            </div>
        </div>
    </nav>
    <main class='webinar-landing'>"""

FOOTER = """    </main>
    <footer class='footer'>
        <div class='footer__watermark' aria-hidden='true'><svg viewBox='0 0 100 80' xmlns='http://www.w3.org/2000/svg'
                fill='none' stroke='currentColor' stroke-width='1'>
                <path d='M50 70 C50 50 40 30 50 10 C60 30 50 50 50 70Z' />
                <path d='M50 60 C40 50 20 45 15 30 C30 35 45 50 50 60Z' />
                <path d='M50 55 C35 50 18 35 25 15 C35 30 45 48 50 55Z' />
                <path d='M50 60 C60 50 80 45 85 30 C70 35 55 50 50 60Z' />
                <path d='M50 55 C65 50 82 35 75 15 C65 30 55 48 50 55Z' />
                <line x1='50' y1='70' x2='50' y2='78' />
                <path d='M30 75 Q50 72 70 75' stroke-linecap='round' />
            </svg></div>
        <div class='container'>
            <div class='footer__top'>
                <div class='footer__brand'><picture><source srcset='../assets/images/logo.webp' type='image/webp'><img src='../assets/images/logo.png' alt='CureSoulLife'
                        style='filter: brightness(0) invert(1) opacity(0.92);' loading='lazy' decoding='async'></picture>
                    <p class='footer__tagline'>सृजन, साधना और मोक्ष</p>
                    <p>A global institution for human consciousness and transformation.</p>
                </div>
                <div class='footer__col'>
                    <h5>Know Us</h5><a href='../about/index.html'>About</a><a href='../founder/index.html'>Founder</a><a
                        href='../about/mission.html'>Mission</a><a href='../about/philosophy.html'>Philosophy</a><a
                        href='../research/index.html'>Research</a>
                </div>
                <div class='footer__col'>
                    <h5>Explore</h5><a href='../framework/index.html'>Framework</a><a
                        href='../knowledge/index.html'>Knowledge Hub</a><a
                        href='../science-consciousness/index.html'>Science &amp; Consciousness</a><a
                        href='../practices/index.html'>Inner Practices</a>
                </div>
                <div class='footer__col'>
                    <h5>Programs</h5><a href='index.html'>Webinars</a><a href='../retreats/index.html'>All Retreats</a><a
                        href='../centers/index.html'>Global Centers</a><a href='../community/index.html'>Community</a><a
                        href='../global-initiatives/index.html'>Initiatives</a>
                </div>
                <div class='footer__col'>
                    <h5>Connect</h5><a href='../join/index.html'>Join the Movement</a><a
                        href='../contact.html'>Contact</a><a href='../media-press.html'>Media &amp; Press</a><a
                        href='../join/volunteer.html'>Volunteer</a><a href='../join/partner-with-us.html'>Partner With
                        Us</a>
                </div>
            </div>
            <div class='footer__divider'></div>
            <div class='footer__bottom'>
                <p>&copy; 2026 CureSoulLife.org — सृजन, साधना और मोक्ष</p>
                <div class='footer__legal'><a href='../privacy-policy.html'>Privacy Policy</a><a
                        href='../terms-of-use.html'>Terms of Use</a><a href='../media-press.html'>Media &amp; Press</a>
                </div>
            </div>
        </div>
    </footer>
    <script src='../assets/js/main.js' defer></script>
    <script src='../assets/js/webinar.js' defer></script>"""

HEAD = """<!DOCTYPE html>
<html lang='hi'>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1.0, viewport-fit=cover'>
<meta name='color-scheme' content='light'>
<title>Life Reset™ Masterclass | CureSoulLife</title>
<meta name='description' content='Sarvesh Mishra के साथ Live Online Masterclass — अपनी ज़िंदगी को पहली बार समझिए। 25 July, 6:00 PM. Registration Free.'>
<link rel='preconnect' href='https://fonts.googleapis.com'>
<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>
<link href='https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,700;1,400&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Jost:wght@300;400;500&display=swap' rel='stylesheet' media='print' onload="this.media='all'">
<noscript><link href='https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,700;1,400&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Jost:wght@300;400;500&display=swap' rel='stylesheet'></noscript>
<link rel='stylesheet' href='../assets/css/global.css'>
<link rel='stylesheet' href='../assets/css/components.css'>
<link rel='stylesheet' href='../assets/css/animations.css'>
<link rel='stylesheet' href='../assets/css/webinar.css'>
</head>
<body>"""


def patch_index() -> None:
    path = ROOT / "webinar" / "index.html"
    text = path.read_text(encoding="utf-8")

    # Strip old head/body start through topbar
    start = text.find("<!-- ============ HERO")
    hero_on = text[start:]

    text = HEAD + "\n" + NAV + "\n" + hero_on

    text = text.replace("<header class=\"hero\">", "<section class=\"hero reveal\">")
    text = text.replace("</header>", "</section>", 1)

    replacements = [
        ('<section class="problem" id="problem">', '<section class="section--paper problem reveal" id="problem">'),
        ('<section id="big-idea">', '<section class="section--sand reveal" id="big-idea">'),
        ('<section class="assessment" id="assessment">', '<section class="section--void-soft assessment reveal" id="assessment">'),
        ('<section id="experience">', '<section class="section--paper reveal" id="experience">'),
        ('<section id="guide">', '<section class="section--sand reveal" id="guide">'),
        ('<section id="why-different">', '<section class="section--paper reveal" id="why-different">'),
        ('<section id="faq">', '<section class="section--sand reveal" id="faq">'),
        ('<section id="testimonials">', '<section class="section--void-soft reveal" id="testimonials">'),
        ('<section class="registration" id="registration">', '<section class="section--void registration reveal" id="registration">'),
        ('class="eyebrow"', 'class="label"'),
        ('class="btn btn--block"', 'class="btn btn--primary btn--block"'),
        ('class="btn btn-start"', 'class="btn btn--primary btn-start"'),
        ('class="btn btn-next"', 'class="btn btn--primary btn-next"'),
        ('class="btn">', 'class="btn btn--primary">'),
        ('class="btn" ', 'class="btn btn--primary" '),
        ('style="color:var(--ink-soft);', 'style="color:var(--earth-300);'),
        ('style="color:var(--ink-soft)"', 'style="color:var(--earth-300)"'),
        ('color:var(--gold-deep)', 'color:var(--gold-500)'),
        ('style=\'margin-top:26px;\'', 'style=\'margin-top:1.5rem;\''),
    ]
    for old, new in replacements:
        text = text.replace(old, new)

    # Replace old footer and scripts
    footer_start = text.find("<footer>")
    if footer_start != -1:
        text = text[:footer_start] + FOOTER + "\n</body>\n</html>\n"

    path.write_text(text, encoding="utf-8")
    print("patched index.html")


def patch_welcome() -> None:
    path = ROOT / "webinar" / "welcome.html"
    text = path.read_text(encoding="utf-8")
    start = text.find("<section class=\"welcome-hero\">")
    body = text[start:]
    footer_start = body.find("<footer>")
    body = body[:footer_start]

    welcome_nav = NAV.replace("href='#registration'", "href='index.html#registration'").replace(
        "Reserve Free Seat", "View Masterclass"
    )

    head = HEAD.replace("Life Reset™ Masterclass", "Welcome — Life Reset™").replace(
        "Sarvesh Mishra", "CureSoulLife"
    )

    text = head + "\n" + welcome_nav.replace(
        "class='webinar-landing'>", "class='webinar-landing webinar-welcome'>"
    ) + "\n" + body + FOOTER + "\n</body>\n</html>\n"

    text = text.replace('class="eyebrow"', 'class="label"')
    text = text.replace('class="btn btn--ghost"', 'class="btn btn--outline-light"')
    path.write_text(text, encoding="utf-8")
    print("patched welcome.html")


if __name__ == "__main__":
    patch_index()
    patch_welcome()
