# Fearlessly Forward design project

This is an independent Fearlessly Forward project. Keep its source, Git repository and publication separate from Admissions. Do not introduce a build or navigation dependency on the former presentation location.

Use `page-builder/CLAUDE.md`, task commands, `RULES.md` and `registry/` as the source of truth. The separate submodule is pinned at `4cadc21`; the runtime remains Design System 2.1.0. Keep canonical critical CSS complete.

Page source lives at `pages/do-good-now/index.html` and `pages/we-reimagine-learning/index.html`. Shared chrome lives in `shared/`; paths there use `{{ROOT}}`. Images live in `images/shared/` or the page directory. Generated `dist/` is not source.

Run `python3 scripts/build.py` after edits. Use `python3 scripts/build-chrome.py --check` for freshness. This project wrapper uses the unmodified canonical inliner with `SiteChrome`, which stamps native `data-selected` and `aria-current="page"` on desktop and mobile links. Do not patch the submodule or hand-edit generated shared regions.

Building a Do Good Campus selects A Do Good Campus; Learning selects Innovations in Teaching and Learning. Those entries link within this project. The Future of AI keeps its live destination. Home is removed from both desktop and mobile navigation; do not restore it. Preserve one-line desktop labels, mobile wrapping and approved Support Maryland styling. The shared site header uses the user-provided `images/shared/fearlessly-forward-logo.png`, with Fearlessly Forward alt text and a link to https://fearlesslyforward.umd.edu/. Preserve the original image bytes/transparency and aspect ratio. Inline image sizing travels with the native cloned logo slot: width auto, height 48px, object-fit contain; native sticky height limits remain in force.

Preserve all approved copy, photographs, quotes, statistic labels and editorial destinations unless the user supplies a change. Do Good retains seven sections; Learning retains eight. Update preservation manifests in `briefs/` for authorized later content changes.

Hero and ordinary light Pathway remain full bleed. Major sections use native 56/80/120px spacing, intros use 32/40/48px child spacing. Learning's video/caption and program grid remain separate sections. Its caption title stays native 18px bold sentence case, 16px below the iframe. All approved width locks remain unchanged.

The two Pathway helpers stay separate and scoped to `#do-good-month-pathway` and `#learning-pathway`. Retain readiness hooks, duplicate guards and the approved image treatments. Learning's native News Feed keeps three columns, one initial row, load-more and category `802177`. Do not log the public feed token or full HTML/diffs containing it.

Retain the approved `umd-learning-*` house namespace for fidelity; native DS classes are not overrides. Record deviations in this project's `OVERRIDES.md`.

This is the user's publicly shared review site: retain noindex and add no sign-in gate. Publish only to the independent repository, never back under the former project's site. Do not change the production Fearlessly Forward domain.

Do not add Scroll to Top controls on either page; the user requested their removal.
