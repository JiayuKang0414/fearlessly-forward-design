# Fearlessly Forward overrides

Native components and canonical critical CSS remain unchanged. Canonical layout, typography and card classes are not custom overrides.

## Scoped Pathway shadow styles

`scripts/do-good-pathway.js` targets only `umd-element-pathway#do-good-month-pathway`; `scripts/learning-pathway.js` targets only `umd-element-pathway#learning-pathway`. Each sets its own `.pathway-container-lock-wrapper` minimum height to zero. Both preserve native readiness hooks and duplicate-style guards. Do Good keeps its 480px maximum photo crop; Learning keeps its original natural image treatment.

These scoped styles remove the standard Pathway's viewport-based `56vh` floor so the rows follow their approved photo and copy without extra blank space. The scripts retain the lifecycle comment, “Reapply after native lazy initialization or a component rerender.” They do not change native typography, padding, section margins or any other Pathway.

## Do Good hero composition

The user requested the snow photograph with the DO GOOD sign exposed. `umd-element-hero#do-good-hero` retains the native small standard variant and uses native left alignment. The original user photo is copied unchanged, with image focal position 70% 70%.

`scripts/do-good-hero.js` installs one scoped shadow style at the native component-ready event and custom-element readiness. At container widths of 768px and above, `.umd-hero-default__text` is limited to `min(480px,40vw)`, and `.umd-hero-default__asset::before` uses a left-to-right black gradient (.75 at the left, .70 at 44%, .15 at 56%, .02 at the right). This separates the copy from the sign and keeps the sign side bright. It does not alter native typography, section spacing or the mobile image-above-text composition. A marked-style guard prevents duplicates and supports rerendering. No other hero is targeted. Browser visual verification remains incomplete.

## Video and shared styles

Learning's `.umd-learning-video` uses a zero-margin figure, responsive 16:9 iframe and a 16px caption gap. Its title uses native 18px bold sentence case; the description uses native rich text. Video and program cards remain separate sections at the native desktop gap.

The shared header uses the user-provided transparent Fearlessly Forward PNG with intrinsic dimensions 754×316. Inline `display:block;width:auto;height:48px;object-fit:contain` preserves its aspect ratio inside the native cloned logo slot; the native sticky maximum height still applies. Its link and accessible label identify the Fearlessly Forward homepage. The previous 284px UMD site-logo sizing rule is removed. `shared/chrome.css` preserves scroll behavior and source/footer credits. The Support Maryland utility row and its alignment/icon/focus styles have been removed at the user’s request. Desktop labels keep inline no-wrap; mobile labels wrap normally. No navigation font, breakpoint or shadow override is added.

The genuine shared page-built classes are `.umd-learning-footer-note` (the presentation credit on both pages), `.umd-learning-source-note` (the small April 2026 editorial note on Do Good) and `.umd-learning-source-note-dark` (that note's dark-band color). These supplementary notes do not replace a native component; their approved small-text, color, spacing and keyboard-focus treatment is retained from the presentation. Learning defines the two source-note helpers through shared CSS but does not render a source-note element. The existing `umd-learning-*` names are preserved for migration fidelity.

## Current-page navigation

`scripts/site_chrome.py` extends the canonical Chrome class only to stamp `data-selected` and `aria-current="page"` by project-relative destination in desktop and mobile menus. `scripts/build-chrome.py` runs the canonical inliner with that class, so generation and freshness checks converge. There is no runtime DOM patch or custom active-state CSS. Neither page reads the other page to obtain chrome.

## Verification

The build checks preserved copy/components, image hashes, asset paths, navigation, themes/classes, critical CSS and chrome freshness. Browser rendering remains unverified because supported initialization fails with `Cannot redefine property: process`.
