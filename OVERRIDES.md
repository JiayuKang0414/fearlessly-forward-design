# Fearlessly Forward overrides

Native components and canonical critical CSS remain unchanged. Canonical layout, typography and card classes are not custom overrides.

## Scoped Pathway shadow styles

`scripts/do-good-pathway.js` targets only `umd-element-pathway#do-good-month-pathway`; `scripts/learning-pathway.js` targets only `umd-element-pathway#learning-pathway`. Each sets its own `.pathway-container-lock-wrapper` minimum height to zero. Both preserve native readiness hooks and duplicate-style guards. Do Good keeps its 480px maximum photo crop; Learning keeps its original natural image treatment.

These scoped styles remove the standard Pathway's viewport-based `56vh` floor so the rows follow their approved photo and copy without extra blank space. The scripts retain the lifecycle comment, “Reapply after native lazy initialization or a component rerender.” They do not change native typography, padding, section margins or any other Pathway.

## Do Good hero settings restored

At the user’s request, the Do Good hero is restored to the native small standard centered layout, default text width and native gradient. The snow photograph and focal position 70% 70% are retained. The page-specific hero composition script and its shadow injection are removed.

## Video and shared styles

Learning's `.umd-learning-video` uses a zero-margin figure, responsive 16:9 iframe and a 16px caption gap. Its title uses native 18px bold sentence case; the description uses native rich text. Video and program cards remain separate sections at the native desktop gap.

The shared header uses the user-provided FF-black.svg, stored as `images/shared/fearlessly-forward-logo.svg`, with viewBox 0 0 160 67. The SVG is copied unchanged and used directly as a vector image. Inline `display:block;width:auto;height:48px;object-fit:contain` preserves its aspect ratio inside the native cloned logo slot; the native sticky maximum height still applies. Its link and accessible label identify the Fearlessly Forward homepage. The previous 284px UMD site-logo sizing rule is removed. `shared/chrome.css` preserves scroll behavior and source/footer credits. The Support Maryland utility row and its alignment/icon/focus styles have been removed at the user’s request. Desktop labels keep inline no-wrap; mobile labels wrap normally. No navigation font, breakpoint or shadow override is added.

The genuine shared page-built classes are `.umd-learning-footer-note` (the presentation credit on both pages), `.umd-learning-source-note` (the small April 2026 editorial note on Do Good) and `.umd-learning-source-note-dark` (that note's dark-band color). These supplementary notes do not replace a native component; their approved small-text, color, spacing and keyboard-focus treatment is retained from the presentation. Learning defines the two source-note helpers through shared CSS but does not render a source-note element. The existing `umd-learning-*` names are preserved for migration fidelity.

## Do Good, Now news feed

The former static eight-card snapshot is replaced with the native dynamic `umd-feed-news`. Original source category 10461, four columns and two rows provide eight current articles from Maryland Today. The existing wide intro, 1600px lock and native spacing remain. The original public client configuration is used without a page-built fetcher, shadow style or proxy. Its token is excluded from this document. `briefs/do-good-news-source.json` records the source and validated configuration; the preservation manifest records static copy and the feed component, not fetched article text.

## Pines Image Expand quote

At the user's request, the former standalone light Pines quote uses the native full-bleed Image Expand layout. Its content slot is constrained to 480px and left-aligned with canonical utility classes; the featured quote uses `data-theme="dark"` and `data-visual-transparent="true"`, with default size for the long quotation. The user's original Maryland Day WebP provides the image. Native animation, overlay, typography and landing spacing remain; no new CSS, script or shadow override is added. All quotation and attribution text is preserved.

## Closing-statement component comparison

At the user's request, the We are united in purpose Image Expand is replaced by three native examples with identical approved copy: centered Section Intro with a red separator, Brand Chevron Promo, and standard white Pathway with the existing Do Good sculpture photo. Each has its own native landing section and unique heading/anchor IDs. Section Intro supplies its own centered width; Chevron Promo and Pathway remain full-bleed. The Chevron's `data-animation="false"` starts its native animation on entering view. The new Pathway uses a direct paragraph in its text slot and does not reuse the Do Good Month spacing helper. No new styles, shadow injections, runtime scripts, labels or calls to action are added. This comparison increases Do Good from seven to nine sections.

## Support promo and edge-to-edge action cards

Support remains a default gold native Banner Promo above Apply, Join, Connect and Cheer, with its original donation URL and official Giving copy recorded in `briefs/support-promo-source.json`. The Support banner retains its native 1600px larger lock. At the user's request the action grid fills the viewport horizontally: the nav sits directly in its section after removal of the larger-lock wrapper. No horizontal spacing class is applied, since even the full lock includes responsive gutters. The main and section already span the page, so no new width rule, 100vw breakout, negative margin or custom script is needed. The action cards match the user's reference markup: `umd-layout-grid-columns-four umd-animation-grid` on the nav and `size-large` on each image Overlay Card. Native 2.1.0 CSS supplies four touching columns from 1024px, two from 650px, and the large card height. The existing canonical grid-animation script handles entry motion. The reference's masonry-grid ID does not refer to the separate two-column staggered Masonry utility.

The former `opportunities-masonry-styles` block, 420/480px host heights, normal lock and staggered grid class are removed. No custom CSS or runtime script is added. Card content, imagery, destinations and CTA-icon treatment are preserved, along with native landing spacing. Learning, Support and the shared Simple Footer remain unchanged.

## Shared Simple Footer

At the user's request, both pages use `umd-element-footer data-display="simple"` instead of the Visual variant. The background image slot is removed. The existing local white UMD logo, its homepage link and the presentation source-credit links remain. The native default dark theme and internal layout apply without new CSS or JavaScript. `shared/footer.html` supplies both pages through the canonical chrome inliner.

## Current-page navigation

`scripts/site_chrome.py` extends the canonical Chrome class only to stamp `data-selected` and `aria-current="page"` by project-relative destination in desktop and mobile menus. `scripts/build-chrome.py` runs the canonical inliner with that class, so generation and freshness checks converge. There is no runtime DOM patch or custom active-state CSS. Neither page reads the other page to obtain chrome.

## Verification

The build checks preserved copy/components, image hashes, asset paths, navigation, themes/classes, critical CSS and chrome freshness. Browser rendering remains unverified because supported initialization fails with `Cannot redefine property: process`.
