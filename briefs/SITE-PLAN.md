# Site Plan: Fearlessly Forward

- Mode: migrate the two already approved landing pages into an independent project.
- Name/slug: Fearlessly Forward / `fearlessly-forward`.
- Intended repository: `JiayuKang0414/fearlessly-forward-design`.
- Permanent local folder: `/Users/jiayukang/Documents/New project/Fearlessly Forward`.
- Sources: https://fearlesslyforward.umd.edu/we-reimagine-learning and https://fearlesslyforward.umd.edu/do-good-now.
- Tone: image-forward; preserve approved Design System 2.1.0 layouts.
- Chrome: UMD utility bar, logo, four flat nav items, Support Maryland and visual footer.

```text
index.html → pages/do-good-now/
pages/
├── do-good-now/index.html
└── we-reimagine-learning/index.html
```

Home and The Future of AI retain their original live URLs. The migrated entries link within this project and select their own page in both menus. No new homepage or AI prototype is designed.

The scaffold contains a separate pinned page-builder submodule and project-owned `shared/`. Only referenced images are migrated, with identical common images deduplicated. Do Good retains seven sections; Learning retains eight. Preservation manifests record original text, component structure and image bytes.

Public review visibility and noindex metadata are retained from the user's previous sharing authorization; no sign-in gate or production-domain change is introduced.

The independent repository has been created at https://github.com/JiayuKang0414/fearlessly-forward-design. The prepared workflow deploys `main` to the independent GitHub Pages site. Existing review URLs remain until the new deployment is verified, then can redirect.
