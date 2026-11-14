#!/usr/bin/env python3
"""DENT verify_page: automated gate checks for a web page (file or URL).

Checks (DENT gates in SKILL.md §3):
  G2  horizontal overflow at each width, with the offending elements
  G3  sampled text contrast (computed colors; skips text over images/gradients)
  G4  unlabeled form controls, unnamed buttons/links, images without alt, missing lang
  G10 animations still running under prefers-reduced-motion: reduce
  G11 audio started before any user gesture (Web Audio sources or unmuted media); early AudioContext creation is reported as info
  +   motion inventory (keyframes, transitions, hover, scroll-driven, view transitions, motion libraries)
  +   console errors, page errors; full-page screenshots per width

Usage:
  python verify_page.py index.html --out .dent/verify
  python verify_page.py http://localhost:3000 --widths 320 375 390 768 1024 1440 --out out
  python verify_page.py page.html --channel chrome      # use installed Chrome/Edge instead of Playwright's Chromium

Requires: pip install playwright && python -m playwright install chromium   (or --channel chrome|msedge)
Exit code: 0 all gates passed, 1 a gate failed, 2 could not run.
It finds mechanical defects only. Always look at the screenshots yourself.

Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DEFAULT_WIDTHS = [320, 375, 390, 768, 1024, 1440]

INIT_SCRIPT = r"""
(() => {
  const D = window.__dent = { gesture: false, ctxBeforeGesture: 0, mediaPlayBeforeGesture: [], };
  const mark = () => { D.gesture = true; };
  addEventListener('pointerdown', mark, true); addEventListener('keydown', mark, true); addEventListener('touchstart', mark, true);
  for (const name of ['AudioContext', 'webkitAudioContext']) {
    const Orig = window[name]; if (!Orig) continue;
    window[name] = function (...a) { const c = new Orig(...a); if (!D.gesture) D.ctxBeforeGesture++; (D.ctxs ||= []).push(c); return c; };
    window[name].prototype = Orig.prototype;
  }
  if (window.AudioScheduledSourceNode) {
    const start = AudioScheduledSourceNode.prototype.start;
    AudioScheduledSourceNode.prototype.start = function (...a) { if (!D.gesture) D.sourcesBeforeGesture = (D.sourcesBeforeGesture || 0) + 1; return start.apply(this, a); };
  }
  const play = HTMLMediaElement.prototype.play;
  HTMLMediaElement.prototype.play = function (...a) {
    if (!D.gesture) D.mediaPlayBeforeGesture.push({ tag: this.tagName.toLowerCase(), muted: this.muted, src: (this.currentSrc || this.src || '').slice(-60) });
    return play.apply(this, a);
  };
})();
"""

OVERFLOW_JS = r"""
() => {
  const W = document.documentElement.clientWidth;
  const sw = Math.max(document.documentElement.scrollWidth, document.body ? document.body.scrollWidth : 0);
  const clips = (el) => { for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) {
      const s = getComputedStyle(p); if (['hidden','clip','auto','scroll'].includes(s.overflowX)) return true; } return false; };
  const bad = [];
  for (const el of document.body.querySelectorAll('*')) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    if ((r.right > W + 1 || r.left < -1) && !clips(el)) {
      if (bad.some(b => b.el.contains(el))) continue;
      const cls = typeof el.className === 'string' ? el.className.trim().split(/\s+/).slice(0, 2).join('.') : '';
      bad.push({ el, desc: el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (cls ? '.' + cls : ''), right: Math.round(r.right), left: Math.round(r.left) });
    }
  }
  return { viewport: W, scrollWidth: sw, overflow: sw > W + 1, offenders: bad.slice(0, 12).map(b => ({ element: b.desc, left: b.left, right: b.right })) };
}
"""

A11Y_JS = r"""
() => {
  const visible = el => { const s = getComputedStyle(el); const r = el.getBoundingClientRect();
    return s.display !== 'none' && s.visibility !== 'hidden' && (r.width > 0 || r.height > 0); };
  const name = el => (el.getAttribute('aria-label') || '').trim() || (el.getAttribute('aria-labelledby') ? 'labelledby' : '')
    || (el.getAttribute('title') || '').trim() || (el.textContent || '').trim() || (el.querySelector('img[alt]:not([alt=""])') ? 'img-alt' : '')
    || (el.querySelector('svg title') ? 'svg-title' : '');
  const desc = el => { const cls = typeof el.className === 'string' ? el.className.trim().split(/\s+/)[0] : '';
    return el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (cls ? '.' + cls : '') + (el.name ? `[name=${el.name}]` : '') + (el.type ? `[type=${el.type}]` : ''); };
  const allControls = [...document.querySelectorAll('input:not([type=hidden]):not([type=submit]):not([type=button]):not([type=reset]), select, textarea')];
  const isUnlabeled = c => !(c.labels && c.labels.length) && !c.getAttribute('aria-label') && !c.getAttribute('aria-labelledby') && !c.getAttribute('title');
  const unlabeled = allControls.filter(visible).filter(isUnlabeled).map(desc);
  const unlabeledHidden = allControls.filter(c => !visible(c)).filter(isUnlabeled).map(desc);
  const buttons = [...document.querySelectorAll('button, [role=button], a[href]')].filter(visible);
  const unnamed = buttons.filter(b => !name(b)).map(desc);
  const imgs = [...document.querySelectorAll('img')].filter(i => !i.hasAttribute('alt')).map(i => (i.currentSrc || i.src || '').slice(-50));
  const deadLinks = [...document.querySelectorAll('a[href="#"], a[href=""]')].filter(visible).map(desc);
  const hs = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(visible).map(h => +h.tagName[1]);
  const skips = []; for (let i = 1; i < hs.length; i++) if (hs[i] > hs[i-1] + 1) skips.push(`h${hs[i-1]}->h${hs[i]}`);
  return { unlabeledHiddenControls: unlabeledHidden, lang: document.documentElement.getAttribute('lang') || '', h1: hs.filter(h => h === 1).length, headingSkips: [...new Set(skips)],
           unlabeledControls: unlabeled, unnamedButtonsLinks: unnamed.slice(0, 20), imagesWithoutAlt: imgs, deadLinks: deadLinks.slice(0, 20),
           autoplayMedia: [...document.querySelectorAll('audio[autoplay], video[autoplay]')].filter(m => !m.muted).map(m => m.tagName.toLowerCase()) };
}
"""

CONTRAST_JS = r"""
() => {
  const parse = c => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const p = m[1].split(/[ ,\/]+/).filter(Boolean).map(Number);
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 }; };
  const lum = ({r,g,b}) => { const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
    return 0.2126*f(r) + 0.7152*f(g) + 0.0722*f(b); };
  const blend = (top, bot) => ({ r: top.r*top.a + bot.r*(1-top.a), g: top.g*top.a + bot.g*(1-top.a), b: top.b*top.a + bot.b*(1-top.a), a: 1 });
  const bgOf = el => { let layers = []; for (let p = el; p; p = p.parentElement) { const s = getComputedStyle(p);
      if (s.backgroundImage && s.backgroundImage !== 'none') return { unknown: true };
      const c = parse(s.backgroundColor); if (c && c.a > 0) { layers.push(c); if (c.a >= 1) break; } }
    let base = { r: 255, g: 255, b: 255, a: 1 }; for (let i = layers.length - 1; i >= 0; i--) base = blend(layers[i], base); return base; };
  const out = []; const seen = new Set();
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) {
    const t = walker.currentNode; if (!t.textContent.trim()) continue; const el = t.parentElement; if (!el) continue;
    const s = getComputedStyle(el); if (s.visibility === 'hidden' || s.display === 'none' || +s.opacity === 0) continue;
    const r = el.getBoundingClientRect(); if (!r.width || !r.height) continue;
    if (el.closest('[aria-hidden=true]')) continue;
    const fg = parse(s.color); if (!fg) continue; const bg = bgOf(el); if (bg.unknown) continue;
    const f = blend(fg, bg); const L1 = lum(f), L2 = lum(bg); const ratio = (Math.max(L1,L2)+0.05)/(Math.min(L1,L2)+0.05);
    const size = parseFloat(s.fontSize), bold = +s.fontWeight >= 700; const large = size >= 24 || (bold && size >= 18.66);
    const need = large ? 3 : 4.5; const key = s.color + '|' + JSON.stringify(bg) + '|' + large;
    if (ratio < need && !seen.has(key)) { seen.add(key);
      out.push({ text: t.textContent.trim().slice(0, 40), ratio: Math.round(ratio*100)/100, need, fontSize: size, color: s.color }); }
  }
  return out.slice(0, 25);
}
"""

ANIM_JS = r"""
() => (document.getAnimations ? document.getAnimations() : []).filter(a => a.playState === 'running').map(a => {
  const t = a.effect && a.effect.getTiming ? a.effect.getTiming() : {};
  const tgt = a.effect && a.effect.target; const cls = tgt && typeof tgt.className === 'string' ? tgt.className.split(' ')[0] : '';
  return { name: a.animationName || a.constructor.name, target: tgt ? tgt.tagName.toLowerCase() + (cls ? '.' + cls : '') : '', iterations: String(t.iterations), duration: t.duration };
})
"""

INVENTORY_JS = r"""
() => {
  const inv = { keyframes: 0, transitionRules: 0, hoverRules: 0, hoverGuarded: 0, scrollDriven: 0, viewTransitions: 0,
                reducedMotionQueries: 0, svgAnimations: document.querySelectorAll('animate, animateTransform, animateMotion').length,
                videos: document.querySelectorAll('video').length, canvases: document.querySelectorAll('canvas').length, libraries: [] };
  const walk = (rules, inHoverMedia) => {
    for (const r of rules) {
      const t = r.cssText || '';
      if (r.type === CSSRule.KEYFRAMES_RULE) { inv.keyframes++; continue; }
      if (r.media) {
        const m = r.media.mediaText || '';
        if (m.includes('prefers-reduced-motion')) inv.reducedMotionQueries++;
        walk(r.cssRules, inHoverMedia || m.includes('hover: hover') || m.includes('hover:hover'));
        continue;
      }
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, inHoverMedia);
      if (/transition\s*:\s*(?!none|all 0s)/.test(t) || /transition-property/.test(t)) inv.transitionRules++;
      if (/:hover/.test(r.selectorText || '')) { inv.hoverRules++; if (inHoverMedia) inv.hoverGuarded++; }
      if (/animation-timeline/.test(t)) inv.scrollDriven++;
      if (/view-transition/.test(t)) inv.viewTransitions++;
    }
  };
  for (const sh of document.styleSheets) { try { walk(sh.cssRules, false); } catch (e) {} }
  const srcs = [...document.scripts].map(s => (s.src || '') + ' ' + (s.textContent || '').slice(0, 20000)).join(' ').toLowerCase();
  const libs = { gsap: !!window.gsap || /gsap/.test(srcs), scrolltrigger: !!window.ScrollTrigger || /scrolltrigger/.test(srcs),
                 motion: /framer-motion|motion\.dev|cdn\.jsdelivr\.net\/npm\/motion|\bmotion@/.test(srcs), lenis: !!window.Lenis || /lenis/.test(srcs),
                 lottie: !!window.lottie || /lottie/.test(srcs), rive: /rive-app|@rive/.test(srcs), three: !!window.THREE || /three(\.module)?(\.min)?\.js|from ['"]three['"]/.test(srcs),
                 anime: !!window.anime || /animejs|anime\.min/.test(srcs), intersectionObserver: /intersectionobserver/.test(srcs),
                 webAnimations: /\.animate\(/.test(srcs), viewTransitionsApi: /startviewtransition/.test(srcs) };
  inv.libraries = Object.entries(libs).filter(([, v]) => v).map(([k]) => k);
  return inv;
}
"""

SCROLL_JS = "async () => { for (let y = 0; y < document.body.scrollHeight; y += 500) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 40)); } window.scrollTo(0, 0); }"


def target_url(t: str) -> str:
    p = Path(t)
    return p.resolve().as_uri() if p.exists() else t


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", help="HTML file path or URL")
    ap.add_argument("--out", default=".dent/verify", help="output folder for screenshots and report.json")
    ap.add_argument("--widths", type=int, nargs="+", default=DEFAULT_WIDTHS)
    ap.add_argument("--height", type=int, default=900)
    ap.add_argument("--channel", default=None, help="use an installed browser: chrome, msedge")
    ap.add_argument("--no-screenshots", action="store_true")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright missing: pip install playwright && python -m playwright install chromium  (or use --channel chrome)")
        return 2

    url = target_url(args.target)
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    report: dict = {"target": args.target, "widths": {}, "gates": {}}
    console_errors: list[str] = []

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(channel=args.channel) if args.channel else p.chromium.launch()
        except Exception as e:  # noqa: BLE001
            print(f"Could not launch browser: {e}")
            return 2

        def new_page(width, reduced=False):
            ctx = browser.new_context(viewport={"width": width, "height": args.height}, device_scale_factor=1,
                                      reduced_motion="reduce" if reduced else "no-preference")
            ctx.add_init_script(INIT_SCRIPT)
            pg = ctx.new_page()
            pg.on("console", lambda m: console_errors.append(m.text[:200]) if m.type == "error" else None)
            pg.on("pageerror", lambda e: console_errors.append(str(e)[:200]))
            pg.goto(url, wait_until="networkidle", timeout=60000)
            pg.wait_for_timeout(400)
            return ctx, pg

        # G2 layout per width (+ screenshots)
        for w in args.widths:
            ctx, pg = new_page(w)
            pg.evaluate(SCROLL_JS); pg.wait_for_timeout(500)
            r = pg.evaluate(OVERFLOW_JS)
            if not args.no_screenshots:
                shot = out / f"page-{w}.jpg"
                pg.screenshot(path=str(shot), full_page=True, type="jpeg", quality=80)
                r["screenshot"] = str(shot)
            report["widths"][w] = r
            ctx.close()

        # G3, G4, G11 at the widest width; G10 reduced motion
        wide = max(args.widths)
        ctx, pg = new_page(wide)
        report["a11y"] = pg.evaluate(A11Y_JS)
        pg.evaluate(SCROLL_JS); pg.wait_for_timeout(300)
        report["contrast_failures"] = pg.evaluate(CONTRAST_JS)
        pg.wait_for_timeout(1200)
        audio = pg.evaluate("() => ({ sourcesBeforeGesture: window.__dent.sourcesBeforeGesture || 0, ctxBeforeGesture: window.__dent.ctxBeforeGesture, runningCtx: (window.__dent.ctxs||[]).filter(c => c.state === 'running').length, mediaPlayBeforeGesture: window.__dent.mediaPlayBeforeGesture })")
        report["audio"] = audio
        normal_anims = pg.evaluate(ANIM_JS)
        report["motion_inventory"] = pg.evaluate(INVENTORY_JS)
        ctx.close()
        ctx, pg = new_page(wide, reduced=True)
        pg.wait_for_timeout(1200)
        reduced_anims = pg.evaluate(ANIM_JS)
        ctx.close()
        report["motion"] = {"running_normal": len(normal_anims), "running_reduced": len(reduced_anims), "reduced_examples": reduced_anims[:8]}
        browser.close()

    report["console_errors"] = sorted(set(console_errors))[:20]

    # Gate verdicts
    g = report["gates"]
    over = {w: r for w, r in report["widths"].items() if r["overflow"]}
    g["G2_layout"] = "Failed" if over else "Passed"
    g["G3_contrast_sample"] = "Failed" if report["contrast_failures"] else "Passed"
    a = report["a11y"]
    g4_fail = a["unlabeledControls"] or a["unlabeledHiddenControls"] or a["unnamedButtonsLinks"] or a["imagesWithoutAlt"] or not a["lang"]
    g["G4_operability_auto"] = "Failed" if g4_fail else "Passed"
    loops_reduced = [x for x in reduced_anims if x["iterations"] in ("Infinity", "inf")]
    g["G10_reduced_motion"] = "Failed" if loops_reduced or len(reduced_anims) > max(2, len(normal_anims) // 4) else "Passed"
    au = report["audio"]
    audible_media = [m for m in au["mediaPlayBeforeGesture"] if not m["muted"]] + a["autoplayMedia"]
    g["G11_no_autoplay_audio"] = "Failed" if audible_media or au["sourcesBeforeGesture"] else "Passed"
    report["note"] = "Automated checks find mechanical defects only. Inspect the screenshots, tab through the page, and test interactions yourself."

    (out / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    # Human-readable summary
    print(f"DENT verify: {args.target}")
    for w, r in report["widths"].items():
        flag = "OVERFLOW" if r["overflow"] else "ok"
        print(f"  {w:>5}px  scrollWidth={r['scrollWidth']:<5} {flag}" + (f"  e.g. {', '.join(o['element'] for o in r['offenders'][:4])}" if r["overflow"] else ""))
    print(f"  lang='{a['lang']}'  h1={a['h1']}  heading skips={a['headingSkips'] or 'none'}")
    print(f"  unlabeled controls: {a['unlabeledControls'] or 'none'}")
    if a["unlabeledHiddenControls"]:
        print(f"  unlabeled controls in hidden panels/tabs (fail when shown): {a['unlabeledHiddenControls']}")
    print(f"  unnamed buttons/links: {a['unnamedButtonsLinks'] or 'none'}")
    print(f"  images without alt: {len(a['imagesWithoutAlt'])}   dead '#' links: {len(a['deadLinks'])}")
    cf = report["contrast_failures"]
    print(f"  contrast failures (sampled): {len(cf)}" + "".join(f"\n      {c['ratio']}:1 < {c['need']}  '{c['text']}'" for c in cf[:6]))
    print(f"  animations running: normal={len(normal_anims)} reduced-motion={len(reduced_anims)}")
    mi = report["motion_inventory"]
    print(f"  motion inventory: keyframes={mi['keyframes']} transition-rules={mi['transitionRules']} hover-rules={mi['hoverRules']} "
          f"(pointer-guarded {mi['hoverGuarded']}) scroll-driven={mi['scrollDriven']} view-transitions={mi['viewTransitions']} "
          f"svg-anim={mi['svgAnimations']} reduced-motion-queries={mi['reducedMotionQueries']} libraries={', '.join(mi['libraries']) or 'none'}")
    if mi["hoverRules"] >= 3 and mi["hoverGuarded"] * 2 < mi["hoverRules"]:
        print(f"  warning: {mi['hoverRules'] - mi['hoverGuarded']} hover rules aren't inside @media (hover:hover) and (pointer:fine); "
              "hover effects that move or reveal things will stick after a tap on phones.")
    if mi["keyframes"] + mi["transitionRules"] + mi["scrollDriven"] < 3 and not mi["libraries"]:
        print("  note: very little motion detected. If the effort is Standard+ this is probably under-animated (motion-menu.md §2).")
    print(f"  audio before gesture: sounds started={au['sourcesBeforeGesture']} audible media={len(audible_media)} (contexts created={au['ctxBeforeGesture']}, running={au['runningCtx']}: info only)")
    print(f"  console errors: {len(report['console_errors'])}")
    print("  gates: " + "  ".join(f"{k}={v}" for k, v in g.items()))
    print(f"  report: {out / 'report.json'}")
    return 1 if any(v == "Failed" for v in g.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
