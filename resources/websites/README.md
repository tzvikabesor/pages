# Websites

This folder contains all published websites and their source files for GitHub Pages.

## Published Sites

All HTML files live in this folder (`resources/websites/`).

Published sites:
- `index.html` - Landing page linking to all published content
- `sally-brief.html` - System brief for Sally (life coach)
- `castel-gandolfo.html` - Trip guide for Castel Gandolfo

**Live URLs**:
- Main: https://tzvikabesor.github.io/pages/resources/websites/
- Index: https://tzvikabesor.github.io/pages/resources/websites/index.html

## Folder Structure

```
resources/websites/
├── README.md (this file)
├── index.html (landing page)
├── sally-brief.html (published website)
├── sally-brief-source.md (source markdown)
├── castel-gandolfo.html (published website)
└── [future-site]/ (folders for complex sites with assets)
```

## Workflow

1. **Create/edit HTML**: Work directly in `resources/websites/`
2. **Test locally**: Open HTML file in browser
3. **Commit and push**: `git push pages main:main` to deploy

For sites with source files (markdown, etc.):
1. Keep source as `[name]-source.md`
2. Generate HTML as `[name].html`
3. Both live in this folder

## GitHub Pages Setup

- Repository: `tzvikabesor/pages.git`
- Remote: `pages` (separate from `origin`)
- Serves from: `resources/websites/` folder
- Push command: `git push pages main:main`
- `.nojekyll` file in root allows serving from subdirectories
