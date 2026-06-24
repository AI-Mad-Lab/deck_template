#!/usr/bin/env python3
"""Regenerate the bundled decks from the un-bundled source.

The bundles (slides.html, index.html) embed the deck source as a JSON string
inside <script type="__bundler/template">...</script>. The encoding is:
    json.dumps(source)  then  replace every "</" with "<\\u002F"
so no nested </script> can terminate the inline script early. The head runtime
and the __bundler/manifest (base64 fonts) are left untouched.

Usage:
    python3 bundle.py extract   # write the current source blob -> deck-source.html
    python3 bundle.py build     # encode deck-source.html -> slides.html & index.html
    python3 bundle.py verify    # confirm encode(extract()) == current stored blob
"""
import json
import re
import sys

SRC = "deck-source.html"
BUNDLES = ["slides.html", "index.html"]
TPL_RE = re.compile(r'(<script type="__bundler/template">)(.*?)(</script>)', re.S)


def encode(source: str) -> str:
    return json.dumps(source).replace("</", "<\\u002F")


def stored_blob(path: str) -> str:
    txt = open(path, encoding="utf-8").read()
    return TPL_RE.search(txt).group(2)


def cmd_extract():
    blob = stored_blob("slides.html")
    open(SRC, "w", encoding="utf-8").write(json.loads(blob))
    print(f"wrote {SRC} ({len(json.loads(blob))} bytes)")


def cmd_verify():
    blob = stored_blob("slides.html")
    source = json.loads(blob)
    ok = encode(source) == blob
    print("round-trip byte-identical:", ok)
    if not ok:
        cand = encode(source)
        for i, (a, b) in enumerate(zip(blob, cand)):
            if a != b:
                print("first diff @", i, repr(blob[i - 20:i + 20]), "VS", repr(cand[i - 20:i + 20]))
                break
    return ok


def cmd_build():
    source = open(SRC, encoding="utf-8").read()
    encoded = encode(source)
    for path in BUNDLES:
        txt = open(path, encoding="utf-8").read()
        # function repl is used literally (no backslash/group-ref processing)
        new = TPL_RE.sub(lambda m: m.group(1) + encoded + m.group(3), txt, count=1)
        open(path, "w", encoding="utf-8").write(new)
        print(f"rebuilt {path}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "verify"
    {"extract": cmd_extract, "build": cmd_build, "verify": cmd_verify}[cmd]()
