const navbar = document.getElementById("navbar");
window.addEventListener("scroll", () => {
  if (navbar) navbar.classList.toggle("scrolled", window.scrollY > 60);
});

const hamburger = document.getElementById("hamburger");
const mobileMenu = document.getElementById("mobileMenu");

function closeMobileMenu() {
  if (!mobileMenu || !hamburger) return;
  mobileMenu.classList.remove("open");
  mobileMenu.style.display = "none";
  hamburger.classList.remove("active");
  document.body.classList.remove("menu-open");
  hamburger.setAttribute("aria-expanded", "false");
}

if (hamburger && mobileMenu) {
  mobileMenu.style.display = "none";

  hamburger.addEventListener("click", (e) => {
    e.stopPropagation();
    const open = mobileMenu.classList.toggle("open");
    mobileMenu.style.display = open ? "block" : "none";
    hamburger.classList.toggle("active", open);
    document.body.classList.toggle("menu-open", open);
    hamburger.setAttribute("aria-expanded", open ? "true" : "false");
  });

  document.addEventListener("click", (e) => {
    const clickInsideMenu = mobileMenu.contains(e.target);
    const clickOnHamburger = hamburger.contains(e.target);
    if (!clickInsideMenu && !clickOnHamburger && mobileMenu.classList.contains("open")) {
      closeMobileMenu();
    }
  });

  mobileMenu.addEventListener("click", (e) => {
    const clickedLink = e.target.closest("a");
    if (clickedLink) closeMobileMenu();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeMobileMenu();
  });
}

function buildMissingMobileAccordions() {
  const desktopMenu = document.querySelector(".navbar__menu");
  if (!desktopMenu || !mobileMenu) return;

  const mobileInner = mobileMenu.querySelector(".mobile-menu__inner");
  if (!mobileInner) return;

  const desktopDropdowns = Array.from(desktopMenu.children).filter(
    (item) => item.classList && item.classList.contains("has-dropdown")
  );
  const desktopMap = new Map();
  desktopDropdowns.forEach((item) => {
    const topLink = item.querySelector("a");
    const dropdown = item.querySelector(".dropdown");
    const dropdownLinks = dropdown ? dropdown.querySelectorAll("a") : [];
    if (topLink && dropdownLinks.length > 0) {
      desktopMap.set(topLink.textContent.trim().toLowerCase(), Array.from(dropdownLinks));
    }
  });

  ["Practices", "Retreats", "Centers"].forEach((menuName) => {
    const plainLink = Array.from(mobileInner.children).find(
      (node) => node.tagName === "A" && node.textContent.trim().toLowerCase() === menuName.toLowerCase()
    );
    if (!plainLink) return;

    const sourceLinks = desktopMap.get(menuName.toLowerCase());
    if (!sourceLinks || sourceLinks.length === 0) return;

    const wrapper = document.createElement("div");
    wrapper.className = "mobile-accordion";

    const trigger = document.createElement("button");
    trigger.type = "button";
    trigger.className = "accordion-trigger";
    trigger.textContent = menuName;

    const panel = document.createElement("div");
    panel.className = "accordion-panel";

    sourceLinks.forEach((srcLink) => {
      const link = document.createElement("a");
      link.href = srcLink.getAttribute("href") || "#";
      link.textContent = srcLink.textContent || "";
      panel.appendChild(link);
    });

    wrapper.appendChild(trigger);
    wrapper.appendChild(panel);
    plainLink.replaceWith(wrapper);
  });
}

buildMissingMobileAccordions();

document.querySelectorAll(".mobile-menu .accordion-trigger").forEach((btn) => {
  btn.addEventListener("click", () => {
    btn.classList.toggle("open");
    const panel = btn.nextElementSibling;
    panel.style.maxHeight = panel.style.maxHeight ? null : `${panel.scrollHeight}px`;
  });
});

document.querySelectorAll(".schedule .accordion-head").forEach((btn) => {
  btn.addEventListener("click", () => {
    btn.parentElement.classList.toggle("open");
  });
});

function initializeLanguageSwitcher() {
  const languages = [
    { code: "en", label: "English" },
    { code: "hi", label: "Hindi" },
    { code: "vi", label: "Vietnamese" },
    { code: "ur", label: "Urdu" },
    { code: "ar", label: "Arabic" },
  ];

  const switcher = document.createElement("div");
  switcher.className = "language-switcher";
  switcher.innerHTML = `
    <button type="button" class="language-switcher__button" aria-expanded="false" aria-label="Select language">
      Language
    </button>
    <div class="language-switcher__menu" aria-hidden="true">
      ${languages
        .map(
          (lang) =>
            `<button type="button" class="language-switcher__option" data-lang="${lang.code}">${lang.label}</button>`
        )
        .join("")}
    </div>
  `;

  document.body.appendChild(switcher);

  const toggleButton = switcher.querySelector(".language-switcher__button");
  const menu = switcher.querySelector(".language-switcher__menu");
  const options = switcher.querySelectorAll(".language-switcher__option");

  function setOpenState(open) {
    switcher.classList.toggle("open", open);
    toggleButton.setAttribute("aria-expanded", open ? "true" : "false");
    menu.setAttribute("aria-hidden", open ? "false" : "true");
  }

  toggleButton.addEventListener("click", () => {
    const isOpen = switcher.classList.contains("open");
    setOpenState(!isOpen);
  });

  document.addEventListener("click", (event) => {
    if (!switcher.contains(event.target)) setOpenState(false);
  });

  function applyLanguage(langCode) {
    const googleSelect = document.querySelector(".goog-te-combo");
    if (!googleSelect) return;
    googleSelect.value = langCode;
    googleSelect.dispatchEvent(new Event("change"));
    setOpenState(false);
  }

  options.forEach((button) => {
    button.addEventListener("click", () => {
      applyLanguage(button.dataset.lang);
    });
  });

  window.googleTranslateElementInit = function () {
    const container = document.createElement("div");
    container.id = "google_translate_element";
    container.style.display = "none";
    document.body.appendChild(container);

    if (window.google && window.google.translate && window.google.translate.TranslateElement) {
      new window.google.translate.TranslateElement(
        {
          pageLanguage: "en",
          includedLanguages: languages.map((lang) => lang.code).join(","),
          autoDisplay: false,
        },
        "google_translate_element"
      );
    }
  };

  const script = document.createElement("script");
  script.src = "https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit";
  script.async = true;
  document.head.appendChild(script);
}

initializeLanguageSwitcher();
