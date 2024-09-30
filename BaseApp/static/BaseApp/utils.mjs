export function scrollToTopAddClassThenRemove(
  targetElement,
  className,
  scrollDuration = 500,
  delay = 1000,
  offsetValue = 0,
  offsetUnit = "px" // 'px' or 'rem'
) {
  // Convert offset to pixels if necessary
  let offset = offsetValue;
  if (offsetUnit === "rem") {
    const remInPixels = parseFloat(
      getComputedStyle(document.documentElement).fontSize
    );
    offset = offsetValue * remInPixels;
  }

  // Smoothly scroll to the target position over scrollDuration milliseconds
  const startY = window.scrollY;
  const targetY = offset; // We want to scroll to position 'offset' from the top
  const distance = startY - targetY;
  const startTime = performance.now();

  function scrollStep(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / scrollDuration, 1);
    const easeInOutCubic =
      progress < 0.5
        ? 4 * progress * progress * progress
        : 1 - Math.pow(-2 * progress + 2, 3) / 2;

    const newY = startY - distance * easeInOutCubic;
    window.scrollTo(0, newY);

    if (elapsed < scrollDuration) {
      window.requestAnimationFrame(scrollStep);
    }
  }

  window.requestAnimationFrame(scrollStep);

  // Add the class to the target element
  targetElement.classList.add(className);

  // Remove the class after the specified delay
  setTimeout(() => {
    targetElement.classList.remove(className);
  }, delay);
}
