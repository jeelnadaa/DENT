#!/usr/bin/env python3
"""Build DENT's README visuals (no dependencies).

Outputs (light + dark variants, used via <picture> in README.md):
  assets/hero-light.svg, assets/hero-dark.svg       animated kinetic-type hero (CSS animation inside SVG)
  assets/workflow-light.svg, assets/workflow-dark.svg  static diagram of the DENT 2.0 system

Concept (Monolith + Swiss Machine): a generic AI-template layout (three equal cards, a violet gradient
blob, an eyebrow pill, "Unlock the power of" lines) is hit by one orange dot. The template scatters and the
DENT wordmark rises in its place; the dot becomes the full stop. Plays once (~5.5 s) and holds.
prefers-reduced-motion: shows the final composition immediately. Text is system fonts or paths, because
SVGs rendered as images on GitHub cannot load web fonts or run scripts.

Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent

THEMES = {
    "light": {"bg": "#F3F0E8", "ink": "#121212", "muted": "#5B5850", "ghost": "#D8D3C7", "ghost2": "#C9C3B5",
              "accent": "#E8461E", "rule": "#CFC8B8", "card": "#FBFAF6", "line": "#121212"},
    "dark": {"bg": "#0E0E0C", "ink": "#F3F0E8", "muted": "#B3AEA3", "ghost": "#2A2925", "ghost2": "#34322D",
             "accent": "#FF5A1F", "rule": "#3A3832", "card": "#171714", "line": "#F3F0E8"},
}

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
SERIF = "Georgia, 'Times New Roman', Times, serif"
SANS = "system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

# Geometric wordmark paths (cell height 220, baseline at y=0 after translate)
LETTERS = {
    "D": "M0 0H92A110 110 0 0 1 92 220H0ZM46 46V174H90A64 64 0 0 0 90 46Z",
    "E": "M0 0H150V46H46V88H132V132H46V174H150V220H0Z",
    "N": "M0 0H46L110 128V0H156V220H110L46 92V220H0Z",
    "T": "M0 0H160V46H103V220H57V46H0Z",
}
LETTER_X = {"D": 120, "E": 350, "N": 530, "T": 716}


def hero(t: dict) -> str:
    letters = "".join(
        f'<g class="l l{i}"><path transform="translate({LETTER_X[k]} 140)" d="{d}" fill="{t["ink"]}" fill-rule="evenodd"/></g>'
        for i, (k, d) in enumerate(LETTERS.items()))
    steps = ["01  ROUTE", "02  PLAN + AUDIT", "03  DIRECT", "04  BUILD", "05  VERIFY", "06  SCORE"]
    workflow = "".join(
        f'<g class="w w{i}"><rect x="1000" y="{162 + i * 34}" width="8" height="8" fill="{t["accent"] if i == 4 else t["ink"]}"/>'
        f'<text x="1020" y="{170 + i * 34}" font-family="{MONO}" font-size="14" letter-spacing="2" fill="{t["ink"]}">{s}</text></g>'
        for i, s in enumerate(steps))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 480" width="1280" height="480" role="img" aria-labelledby="t d">
<title id="t">DENT 2.0</title>
<desc id="d">Animated banner: a generic AI-template layout is hit by an orange dot and replaced by the DENT wordmark, the tagline "Make a dent with your product's design." and the workflow route, plan and audit, direct, build, verify, score.</desc>
<defs>
  <radialGradient id="blob" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#8B6CFF"/><stop offset=".55" stop-color="#4F7DF5"/><stop offset="1" stop-color="#4F7DF5" stop-opacity="0"/></radialGradient>
  <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="28"/></filter>
  <clipPath id="rise"><rect x="100" y="120" width="880" height="242"/></clipPath>
  <clipPath id="type"><rect class="typemask" x="118" y="392" width="700" height="56"/></clipPath>
</defs>
<style>
  .tpl, .ball, .ring, .l, .w, .typemask, .rule, .label, .tag {{ transform-box: fill-box; }}
  .tpl {{ animation: scatter .7s cubic-bezier(.7,0,.84,0) 1.55s both; transform-origin: 50% 50%; }}
  .t1 {{ --x:-240px; --y:-60px; --r:-14deg; }} .t2 {{ --x:0px; --y:-220px; --r:6deg; }} .t3 {{ --x:260px; --y:-40px; --r:16deg; }}
  .t4 {{ --x:0px; --y:120px; --r:0deg; }} .t5 {{ --x:-60px; --y:-160px; --r:-4deg; }} .t6 {{ --x:40px; --y:160px; --r:8deg; }}
  @keyframes scatter {{ to {{ transform: translate(var(--x), var(--y)) rotate(var(--r)) scale(.85); opacity: 0; }} }}
  .blob {{ animation: vanish .6s cubic-bezier(.7,0,.84,0) 1.55s both; transform-origin: 50% 50%; }}
  @keyframes vanish {{ to {{ transform: scale(0); opacity: 0; }} }}
  .ball {{ transform-origin: 50% 100%; animation: dropsquash 1.12s .9s both; }}
  @keyframes dropsquash {{
    0% {{ transform: translateY(-440px); animation-timing-function: cubic-bezier(.55,0,1,.45); }}
    55% {{ transform: translateY(0) scale(1,1); animation-timing-function: cubic-bezier(.16,1,.3,1); }}
    64% {{ transform: scale(1.35,.7); animation-timing-function: cubic-bezier(.16,1,.3,1); }}
    82% {{ transform: scale(.92,1.08); }}
    100% {{ transform: none; }}
  }}
  .ring {{ transform-origin: 50% 50%; opacity: 0; animation: ring .75s cubic-bezier(.16,1,.3,1) 1.52s forwards; }}
  @keyframes ring {{ 0% {{ opacity: .9; transform: scale(1); }} 100% {{ opacity: 0; transform: scale(9); }} }}
  .l {{ animation: rise .9s cubic-bezier(.16,1,.3,1) both; }}
  .l0 {{ animation-delay: 1.9s; }} .l1 {{ animation-delay: 1.99s; }} .l2 {{ animation-delay: 2.08s; }} .l3 {{ animation-delay: 2.17s; }}
  @keyframes rise {{ from {{ transform: translateY(250px); }} to {{ transform: translateY(0); }} }}
  .typemask {{ transform-origin: 0 50%; animation: wipe 1.1s cubic-bezier(.65,0,.35,1) 2.9s both; }}
  @keyframes wipe {{ from {{ transform: scaleX(0); }} to {{ transform: scaleX(1); }} }}
  .rule {{ transform-origin: 0 50%; animation: wipe .8s cubic-bezier(.65,0,.35,1) 3.7s both; }}
  .label {{ animation: fade .6s ease-out 2.6s both; }}
  .w {{ animation: slide .5s cubic-bezier(.16,1,.3,1) both; }}
  .w0 {{ animation-delay: 4.0s; }} .w1 {{ animation-delay: 4.12s; }} .w2 {{ animation-delay: 4.24s; }} .w3 {{ animation-delay: 4.36s; }} .w4 {{ animation-delay: 4.48s; }} .w5 {{ animation-delay: 4.6s; }}
  @keyframes slide {{ from {{ opacity: 0; transform: translateX(24px); }} to {{ opacity: 1; transform: none; }} }}
  @keyframes fade {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
  .tpl, .blob {{ opacity: 1; }}
  @media (prefers-reduced-motion: reduce) {{
    *, .tpl, .blob, .ball, .ring, .l, .w, .typemask, .rule, .label {{ animation: none !important; }}
    .tpl, .blob, .ring {{ opacity: 0 !important; }}
  }}
</style>
<rect width="1280" height="480" fill="{t["bg"]}"/>

<!-- The generic template (what DENT replaces) -->
<g class="blob"><circle cx="640" cy="250" r="190" fill="url(#blob)" opacity=".55" filter="url(#soft)"/></g>
<g class="tpl t5"><rect x="548" y="86" width="184" height="30" rx="15" fill="{t["ghost2"]}"/><text x="640" y="106" text-anchor="middle" font-family="{SANS}" font-size="13" fill="{t["muted"]}">&#10022; New: AI-powered</text></g>
<g class="tpl t4"><rect x="400" y="136" width="480" height="18" rx="9" fill="{t["ghost2"]}"/><rect x="460" y="166" width="360" height="14" rx="7" fill="{t["ghost"]}"/></g>
<g class="tpl t1"><rect x="160" y="208" width="290" height="190" rx="22" fill="{t["card"]}" stroke="{t["ghost"]}"/><circle cx="200" cy="248" r="16" fill="{t["ghost2"]}"/><rect x="184" y="282" width="180" height="14" rx="7" fill="{t["ghost2"]}"/><rect x="184" y="308" width="230" height="10" rx="5" fill="{t["ghost"]}"/><rect x="184" y="326" width="200" height="10" rx="5" fill="{t["ghost"]}"/></g>
<g class="tpl t2"><rect x="495" y="208" width="290" height="190" rx="22" fill="{t["card"]}" stroke="{t["ghost"]}"/><circle cx="535" cy="248" r="16" fill="{t["ghost2"]}"/><rect x="519" y="282" width="180" height="14" rx="7" fill="{t["ghost2"]}"/><rect x="519" y="308" width="230" height="10" rx="5" fill="{t["ghost"]}"/><rect x="519" y="326" width="200" height="10" rx="5" fill="{t["ghost"]}"/></g>
<g class="tpl t3"><rect x="830" y="208" width="290" height="190" rx="22" fill="{t["card"]}" stroke="{t["ghost"]}"/><circle cx="870" cy="248" r="16" fill="{t["ghost2"]}"/><rect x="854" y="282" width="180" height="14" rx="7" fill="{t["ghost2"]}"/><rect x="854" y="308" width="230" height="10" rx="5" fill="{t["ghost"]}"/><rect x="854" y="326" width="200" height="10" rx="5" fill="{t["ghost"]}"/></g>
<g class="tpl t6"><rect x="560" y="420" width="160" height="40" rx="20" fill="{t["ghost2"]}"/></g>

<!-- DENT -->
<text class="label" x="120" y="96" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{t["muted"]}">DENT 2.0 &#8212; OPEN-SOURCE DESIGN ENGINEERING FOR AI AGENTS</text>
<g clip-path="url(#rise)">{letters}</g>
<circle class="ring" cx="926" cy="334" r="26" fill="none" stroke="{t["accent"]}" stroke-width="3"/>
<g class="ball"><circle cx="926" cy="334" r="26" fill="{t["accent"]}"/></g>
<g clip-path="url(#type)"><text x="120" y="432" font-family="{SERIF}" font-style="italic" font-size="34" fill="{t["ink"]}">Make a dent with your product&#8217;s design.</text></g>
<rect class="rule" x="120" y="450" width="660" height="2" fill="{t["accent"]}"/>
{workflow}
</svg>
'''


def workflow(t: dict) -> str:
    W, H = 1280, 560
    pipe = ["ROUTE", "PLAN", "AUDIT", "DIRECT", "BUILD", "VERIFY", "SCORE", "IMPROVE"]
    x0, w, gap, y = 64, 128, 16, 196
    boxes = []
    for i, s in enumerate(pipe):
        x = x0 + i * (w + gap)
        hot = s in ("VERIFY", "SCORE")
        boxes.append(f'<rect x="{x}" y="{y}" width="{w}" height="64" fill="{t["accent"] if hot else t["card"]}" stroke="{t["line"]}" stroke-width="1.5"/>'
                     f'<text x="{x + 14}" y="{y + 24}" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{t["bg"] if hot else t["muted"]}">{i + 1:02d}</text>'
                     f'<text x="{x + 14}" y="{y + 48}" font-family="{SANS}" font-weight="700" font-size="16" fill="{t["bg"] if hot else t["ink"]}">{s}</text>')
        if i < len(pipe) - 1:
            boxes.append(f'<path d="M{x + w} {y + 32}h{gap}" stroke="{t["line"]}" stroke-width="1.5"/>')
    pillars = [
        ("KNOWLEDGE", ["41 aesthetic styles", "Creative directions library", "Hero typography system", "Laws, patterns, platforms"]),
        ("CATALOGUES", ["UI components & primitives", "Motion, 3D & creative code", "Audio, voice & music", "Video tools & assets"]),
        ("QUALITY", ["Gates G1–G12", "verify_page.py + contrast.py", "Self-score with evidence", "All-out sweeps"]),
        ("MEMORY", ["DESIGN.md source of truth", "Decision Log + attribution", "PLAN / MOTION / SOUND / VIDEO", "Licence table"]),
    ]
    cols = []
    pw, pgap = 265, 25
    for i, (title, items) in enumerate(pillars):
        x = 64 + i * (pw + pgap)
        rows = "".join(f'<text x="{x + 18}" y="{372 + j * 30}" font-family="{SANS}" font-size="15" fill="{t["ink"]}">{escape(it)}</text>' for j, it in enumerate(items))
        cols.append(f'<rect x="{x}" y="318" width="{pw}" height="180" fill="{t["card"]}" stroke="{t["rule"]}"/>'
                    f'<text x="{x + 18}" y="344" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{t["accent"]}">{title}</text>{rows}')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">How DENT 2.0 works</title>
<desc id="d">A request goes into the /dent router, which builds a pipeline: route, plan, audit, direct, build, verify, score, improve. It draws on four pillars: knowledge, catalogues, quality and memory.</desc>
<rect width="{W}" height="{H}" fill="{t["bg"]}"/>
<text x="64" y="70" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{t["muted"]}">ANY REQUEST &#8594; /dent</text>
<text x="64" y="118" font-family="{SERIF}" font-size="38" fill="{t["ink"]}">One command. The right pipeline. Verified.</text>
<text x="64" y="160" font-family="{SANS}" font-size="16" fill="{t["muted"]}">The router reads what you want, chains the right sub-commands, and never skips verification or the score.</text>
{''.join(boxes)}
<text x="64" y="296" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{t["muted"]}">POWERED BY</text>
{''.join(cols)}
<text x="64" y="536" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{t["muted"]}">31 COMMANDS &#183; 4 EFFORT LEVELS &#183; 4 TASK DEPTHS &#183; WORKS IN ANY AGENT THAT READS SKILL.MD</text>
</svg>
'''


def main() -> None:
    import xml.dom.minidom
    for name, t in THEMES.items():
        for svg in (hero(t), workflow(t)):
            xml.dom.minidom.parseString(svg)  # fail loudly on malformed XML (GitHub would show a broken image)
        (OUT / f"hero-{name}.svg").write_text(hero(t), encoding="utf-8")
        (OUT / f"workflow-{name}.svg").write_text(workflow(t), encoding="utf-8")
    print("Wrote hero-{light,dark}.svg and workflow-{light,dark}.svg")


if __name__ == "__main__":
    main()
