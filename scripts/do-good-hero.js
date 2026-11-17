(() => {
  const hero = document.getElementById('do-good-hero');
  if (!hero || !window.customElements) return;

  const installComposition = () => {
    const root = hero.shadowRoot;
    if (!root || root.querySelector('[data-do-good-hero-composition]')) return;

    // Keep the photographed sign clear of copy; shade the text side only.
    const style = document.createElement('style');
    style.setAttribute('data-do-good-hero-composition', '');
    style.textContent = `
      @container (min-width: 768px) {
        :host(#do-good-hero) .umd-hero-default__text {
          width: 100%;
          max-width: min(480px, 40vw);
        }
        :host(#do-good-hero) .umd-hero-default__asset::before {
          background: linear-gradient(90deg,
            rgba(0, 0, 0, .75) 0%,
            rgba(0, 0, 0, .70) 44%,
            rgba(0, 0, 0, .15) 56%,
            rgba(0, 0, 0, .02) 100%);
        }
      }
    `;
    root.appendChild(style);
  };

  // Reapply after native lazy initialization or a component rerender.
  hero.addEventListener('umdComponent:ready', installComposition);
  customElements.whenDefined('umd-element-hero').then(installComposition);
})();
