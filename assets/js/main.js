const navbar = document.getElementById("navbar");
window.addEventListener("scroll", () => {
  if (navbar) navbar.classList.toggle("scrolled", window.scrollY > 60);
});

const hamburger = document.getElementById("hamburger");
const mobileMenu = document.getElementById("mobileMenu");

function closeMobileMenu() {
  if (!mobileMenu || !hamburger) return;
  mobileMenu.classList.remove("open");
  hamburger.classList.remove("active");
  document.body.classList.remove("menu-open");
  hamburger.setAttribute("aria-expanded", "false");
}

if (hamburger && mobileMenu) {
  hamburger.addEventListener("click", (e) => {
    e.stopPropagation();
    const open = mobileMenu.classList.toggle("open");
    hamburger.classList.toggle("active", open);
    document.body.classList.toggle("menu-open", open);
    hamburger.setAttribute("aria-expanded", open ? "true" : "false");
  });

  mobileMenu.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      closeMobileMenu();
    });
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeMobileMenu();
  });
}

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
