# Vela Pre-Seed Deck / Mad Slides

Self-contained pitch deck + lightweight editor, served via GitHub Pages.

**Live:** https://ai-mad-lab.github.io/deck_template/slides.html

## Files
- `slides.html` — the bundled **Mad Slides** app (deck + top toolbar: Edit / Arrange / Present /
  Export / Undo / Redo). This is the editable, shareable build.
- `index.html` — the same bundle without the Mad Slides app shell (plain deck + in-place editor).
- `deck-source.html` — the **un-bundled source of truth** (slides markup + the `text/x-dc` app logic).
  Edit this, then rebuild.
- `bundle.py` — re-encodes `deck-source.html` into the `__bundler/template` script of both bundles
  (JSON-encoded, with every `</` escaped as `</`). The head runtime and the base64 font
  manifest are left untouched.
- `template.html` — legacy un-bundled source (predates Mad Slides); kept for reference only.

## Editing
```
python3 bundle.py extract   # (re)derive deck-source.html from slides.html
# edit deck-source.html
python3 bundle.py build     # regenerate slides.html + index.html
python3 bundle.py verify    # assert the encode round-trips byte-for-byte
```

## Editor
Click **Edit** to edit text in place; click an image to swap it. Edits persist to
`localStorage['deckEdits:' + location.pathname]` as a compact JSON delta and are restored on load.
**Undo/Redo** (⌘Z / ⇧⌘Z, or the toolbar arrows) covers text, image, and structural edits.
Every slide has a gray Claude spark icon; clicking it copies a slide-specific question to paste into Claude.
