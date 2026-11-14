#!/usr/bin/env python3
"""Screenshot a DENT benchmark pair (without vs. with) at phone and desktop widths.

Usage:
  python benchmark/screenshot.py WITHOUT_index.html WITH_index.html --out benchmark/results/<run-name>

Requires: pip install playwright && python -m playwright install chromium
Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from pathlib import Path
import argparse
import shutil
import sys

WIDTHS = {390: 844, 1440: 900}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("without", type=Path, help="index.html built WITHOUT DENT")
    ap.add_argument("with_", metavar="with", type=Path, help="index.html built WITH DENT")
    ap.add_argument("--out", type=Path, required=True, help="output folder")
    args = ap.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright is missing: pip install playwright && python -m playwright install chromium")
        return 1

    for f in (args.without, args.with_):
        if not f.is_file():
            print(f"error: {f} not found")
            return 1

    args.out.mkdir(parents=True, exist_ok=True)
    runs = {"without": args.without.resolve(), "with": args.with_.resolve()}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for label, html in runs.items():
            (args.out / label).mkdir(exist_ok=True)
            shutil.copy2(html, args.out / label / "index.html")
            for width, height in WIDTHS.items():
                page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
                page.goto(html.as_uri(), wait_until="networkidle")
                # Let entrance animations finish, then force any scroll-reveal content visible
                # by scrolling through the page once.
                page.evaluate(
                    "async () => { for (let y = 0; y < document.body.scrollHeight; y += 400) "
                    "{ window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); } window.scrollTo(0, 0); }"
                )
                page.wait_for_timeout(800)
                target = args.out / f"{label}-{width}.jpg"
                page.screenshot(path=str(target), full_page=True, type="jpeg", quality=85)
                page.close()
                print(f"saved {target}")
        browser.close()
    print("Done. Fill in RESULT.md from benchmark/results/_TEMPLATE.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
