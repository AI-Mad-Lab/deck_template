# Vela Pre-Seed Deck

Self-contained pitch deck, served via GitHub Pages.

**Live:** https://ai-mad-lab.github.io/deck_template/

## Files
- `index.html` — the bundled, self-contained deck (this is what GitHub Pages serves).
- `template.html` — the editable source markup (slides + the `text/x-dc` logic). `index.html` is
  regenerated from this by re-encoding it into the bundle's `__bundler/template` script
  (JSON-encoded, with every `/` escaped as `/`).

Every slide has a gray Claude spark icon at bottom-center; clicking it copies a slide-specific
question to the clipboard to paste into Claude.
