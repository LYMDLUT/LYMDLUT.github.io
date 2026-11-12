// Theme toggle, scroll progress, and BibTeX actions.

const STORAGE_KEY = "theme";

function applyTheme(theme) {
  document.documentElement.dataset.theme = theme;
  localStorage.setItem(STORAGE_KEY, theme);
}

function setUpThemeToggle() {
  const button = document.querySelector(".theme-toggle");
  if (!button) return;
  button.addEventListener("click", () => {
    applyTheme(document.documentElement.dataset.theme === "dark" ? "light" : "dark");
  });
}

function setUpScrollProgress() {
  const bar = document.querySelector(".progress__bar");
  if (!bar) return;
  const update = () => {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const ratio = scrollable > 0 ? window.scrollY / scrollable : 0;
    bar.style.width = `${Math.min(ratio, 1) * 100}%`;
  };
  addEventListener("scroll", update, { passive: true });
  addEventListener("resize", update);
  update();
}

function setUpBibtex() {
  document.querySelectorAll("[data-bibtex-toggle]").forEach((button) => {
    const card = button.closest(".pub");
    button.addEventListener("click", () => {
      const open = card.classList.toggle("is-open");
      button.setAttribute("aria-expanded", String(open));
    });
  });

  document.querySelectorAll("[data-bibtex-copy]").forEach((button) => {
    const bib = button.closest(".pub").querySelector(".bib");
    button.addEventListener("click", async () => {
      await navigator.clipboard.writeText(bib.textContent.trim());
      const label = button.querySelector(".btn__label") ?? button;
      const original = label.textContent;
      label.textContent = "Copied";
      setTimeout(() => {
        label.textContent = original;
      }, 1400);
    });
  });
}

// A mailto: link does nothing visible when no mail client is configured, so
// copy the address as well and confirm that something happened.
function setUpEmailCopy() {
  const toast = document.querySelector(".toast");
  if (!toast) return;
  let hideTimer;
  document.querySelectorAll("[data-copy-email]").forEach((link) => {
    link.addEventListener("click", async () => {
      await navigator.clipboard.writeText(link.dataset.copyEmail);
      toast.textContent = toast.dataset.label;
      toast.hidden = false;
      clearTimeout(hideTimer);
      hideTimer = setTimeout(() => {
        toast.hidden = true;
      }, 2200);
    });
  });
}

setUpThemeToggle();
setUpScrollProgress();
setUpBibtex();
setUpEmailCopy();
