# Fearlessly Forward

Independent UMD design project with its own Git repository, shared chrome, images, page-builder submodule and deployment workflow.

| Page | Project route | Selected navigation |
| --- | --- | --- |
| Building a Do Good Campus | `pages/do-good-now/` | A Do Good Campus |
| We Reimagine Learning | `pages/we-reimagine-learning/` | Innovations in Teaching and Learning |

The root redirects to Do Good for review. Home and The Future of AI retain their original live-site URLs. The two migrated pages link directly to each other, using project-relative URLs and independent desktop/mobile selection.

## Build and preview

```sh
git submodule update --init page-builder
python3 scripts/build.py
python3 -m http.server 4173 --directory dist
```

Open http://localhost:4173. UMD bundles/fonts, live news and YouTube require an internet connection. The page-builder is pinned at `4cadc21`; the runtime remains Design System 2.1.0.

Edit page content in `pages/`; edit shared regions in `shared/`, then build. `scripts/build-chrome.py` runs the canonical inliner with project-owned current-page selection. `briefs/` records approved text/component and image hashes; update those records when the user authorizes later content changes. Never print feed tokens or full Learning HTML in logs.

The build retains Do Good's seven sections and Learning's eight sections, three-column News Feed, 18px caption title and 120px desktop video-to-program gap. Only referenced images are migrated. The publication artifact contains only required pages, assets and runtime scripts; no fixtures, Git files or design-system source are published.

## Publication status

The local project and Pages workflow are ready. Intended repository: `JiayuKang0414/fearlessly-forward-design`. It has not been created: the current session has no GitHub repository-creation credential. After creating that empty repository, add its SSH origin and push `main`; select GitHub Actions as the Pages source.

The user's existing public review behavior is retained: no new login gate, with noindex metadata. No production UMD domain is changed. Existing review URLs remain until the new deployment is verified; they can then become redirects.

Copy, components, section order, local assets, navigation, native spacing classes, themes, class names, canonical CSS and shared-chrome freshness are checked. Browser visual/interaction verification remains incomplete because supported initialization fails with `Cannot redefine property: process`.
