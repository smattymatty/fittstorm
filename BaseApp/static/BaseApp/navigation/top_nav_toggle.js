const navToggle = document.querySelector(".ba-navbar-toggle");
const navItems = document.querySelector(".ba-navbar-items");

// Function to open the menu
function openMenu() {
  navToggle.setAttribute("aria-expanded", "true");
  navItems.style.display = "flex";
}
function resetMenuForLargeScreen() {
  navToggle.setAttribute("aria-expanded", "false");
  navItems.style.display = ""; // Reset to default CSS value
}
// Function to close the menu
function closeMenu() {
  navToggle.setAttribute("aria-expanded", "false");
  navItems.style.display = "none";
}

// Toggle menu when clicking the button
navToggle.addEventListener("mousedown", (event) => {
  event.stopPropagation(); // Prevent this click from immediately closing the menu
  const expanded = navToggle.getAttribute("aria-expanded") === "true" || false;
  if (expanded) {
    closeMenu();
  } else {
    openMenu();
  }
});

// Close menu when clicking outside
document.addEventListener("mousedown", (event) => {
  const isClickInsideMenu = navItems.contains(event.target);
  const isClickOnToggle = navToggle.contains(event.target);

  if (
    !isClickInsideMenu &&
    !isClickOnToggle &&
    navToggle.getAttribute("aria-expanded") === "true"
  ) {
    closeMenu();
  }
});

// Prevent clicks inside the menu from closing it
navItems.addEventListener("mousedown", (event) => {
  event.stopPropagation();
});

// Close menu when pressing Escape
document.addEventListener("keydown", (event) => {
  if (
    event.key === "Escape" &&
    navToggle.getAttribute("aria-expanded") === "true"
  ) {
    closeMenu();
  }
});

// New resize event listener
window.addEventListener("resize", () => {
  if (window.innerWidth > 768) {
    resetMenuForLargeScreen();
  }
});

// Initial check on page load
if (window.innerWidth > 768) {
  resetMenuForLargeScreen();
}
