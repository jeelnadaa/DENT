/* DENT video kit: technique modules. Deterministic (everything is a function of t), browser-native, no dependencies
   except the optional Three.js loader. Combine them as your film bible says; none of them is a "look" by itself.
   Each module is demonstrated and tested in techniques.html (python render.py stills --page techniques ...).
   Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0. */
(function (G) {
  const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  const P = (t, s, d) => clamp((t - s) / d);
  const eOut = (x) => 1 - Math.pow(1 - clamp(x), 4);
  const eIO = (x) => { x = clamp(x); return x < .5 ? 8 * x ** 4 : 1 - Math.pow(-2 * x + 2, 4) / 2; };
  // seeded random (mulberry32) so every render is identical
  const rand = (seed) => () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let r = Math.imul(seed ^ seed >>> 15, 1 | seed); r = r + Math.imul(r ^ r >>> 7, 61 | r) ^ r; return ((r ^ r >>> 14) >>> 0) / 4294967296; };

  /* 1. Custom lettering: draw SVG letter paths stroke-first, then flood the fill.
        <svg><path class="glyph" d="…"/>…</svg>; give paths stroke + fill colours in CSS. */
  function lettering(svg, t, start, { draw = .9, stagger = .12, fill = .35 } = {}) {
    svg.querySelectorAll('path').forEach((p, i) => {
      const L = p.__len || (p.__len = p.getTotalLength());
      const s = start + i * stagger, k = eIO(P(t, s, draw));
      p.style.strokeDasharray = L; p.style.strokeDashoffset = L * (1 - k);
      p.style.fillOpacity = eOut(P(t, s + draw * .7, fill));
    });
  }

  /* 2. Kinetic type with variable-font axes: split text into letters once, then drive wght/wdth per letter
        as a wave that travels across the word. Needs a variable font with those axes. */
  function splitLetters(el) {
    if (el.__letters) return el.__letters;
    const txt = el.textContent; el.textContent = '';
    el.__letters = [...txt].map(ch => { const s = document.createElement('span'); s.textContent = ch; s.style.display = 'inline-block'; s.style.whiteSpace = 'pre'; el.append(s); return s; });
    return el.__letters;
  }
  function axisWave(el, t, { start = 0, speed = 1.2, wMin = 100, wMax = 900, dMin = 50, dMax = 150, spread = .16 } = {}) {
    splitLetters(el).forEach((s, i) => {
      const ph = clamp((t - start) * speed - i * spread, 0, 1e9);
      const k = .5 - .5 * Math.cos(ph * Math.PI * 2);
      s.style.fontVariationSettings = `"wght" ${Math.round(wMin + (wMax - wMin) * k)}, "wdth" ${Math.round(dMin + (dMax - dMin) * k)}`;
    });
  }

  /* 3. Hand-made "boil": re-seed an SVG turbulence displacement on twos/threes so lines wobble like
        frame-by-frame animation. Put filter="url(#boil)" on the element; call each frame. */
  function boilFilter(svgDefsHost, id = 'boil', scale = 3) {
    const ns = 'http://www.w3.org/2000/svg', svg = document.createElementNS(ns, 'svg');
    svg.setAttribute('width', 0); svg.setAttribute('height', 0); svg.style.position = 'absolute';
    svg.innerHTML = `<filter id="${id}"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="1"/><feDisplacementMap in="SourceGraphic" scale="${scale}"/></filter>`;
    svgDefsHost.append(svg); return svg.querySelector('feTurbulence');
  }
  function boil(turb, t, fps = 12) { turb.setAttribute('seed', 1 + Math.floor(t * fps) % 7); }

  /* 4. Morph: interpolate two SVG paths that share the same command structure (same commands, same count).
        Draw both shapes with matching points; DENT checks the structure and throws if it differs. */
  function morph(pathEl, fromD, toD, k) {
    const num = /-?\d*\.?\d+(?:e-?\d+)?/gi, a = fromD.match(num), b = toD.match(num);
    if (!a || !b || a.length !== b.length || fromD.replace(num, '') !== toD.replace(num, '')) throw new Error('morph: paths must share structure');
    let i = 0; const e = eIO(k);
    pathEl.setAttribute('d', fromD.replace(num, () => { const v = +a[i] + (+b[i] - +a[i]) * e; i++; return v.toFixed(2); }));
  }

  /* 5. Parallax depth camera: layers with a depth z (1 = screen plane, bigger = further away). The camera moves in
        world space; nearer layers move more. Rack focus blurs layers by their distance from the focus plane. */
  function camera(layers, { x = 0, y = 0, zoom = 1, focus = 1, aperture = 3 }) {
    layers.forEach(({ el, z }) => {
      const k = 1 / z;
      el.style.transform = `translate(${-x * k}px,${-y * k}px) scale(${1 + (zoom - 1) * k})`;
      const blur = Math.abs(1 / z - 1 / focus) * aperture * 6;
      el.style.filter = blur > .1 ? `blur(${blur.toFixed(2)}px)` : 'none';
    });
  }

  /* 6. Glitch: RGB channel split + horizontal slice offsets, deterministic per frame. amount 0..1.
        Keep bursts short; never flash light/dark more than 3 times per second. */
  function glitch(el, t, amount, seed = 7) {
    if (amount <= 0) { el.style.textShadow = el.style.clipPath = ''; el.style.translate = ''; return; }   // uses `translate`, so the element's own transform is kept
    const r = rand(seed + Math.floor(t * 24)), dx = (r() - .5) * 24 * amount;
    el.style.textShadow = `${(4 + 10 * amount).toFixed(1)}px 0 rgba(255,0,80,.85), ${(-4 - 10 * amount).toFixed(1)}px 0 rgba(0,220,255,.85)`;
    const y0 = r() * 80, h = 6 + r() * 18;
    el.style.clipPath = amount > .5 ? `polygon(0 0,100% 0,100% ${y0}%,0 ${y0}%,0 ${y0 + h}%,100% ${y0 + h}%,100% 100%,0 100%)` : '';
    el.style.translate = `${dx.toFixed(1)}px 0`;
  }

  /* 7. Physics: a ball/object dropped from h with restitution; returns y (0 = floor) and squash/stretch scales. */
  function bounce(t, start, { h = 600, g = 4000, e = .45 } = {}) {
    let dt = t - start; if (dt < 0) return { y: -h, sx: 1, sy: 1 };
    let v0 = Math.sqrt(2 * g * h), tFall = v0 / g;           // first fall from rest
    if (dt < tFall) { const y = -h + .5 * g * dt * dt, v = g * dt; const st = Math.min(.35, v / 9000); return { y, sx: 1 - st, sy: 1 + st }; }
    dt -= tFall; let v = v0 * e;
    while (v > 40) {
      const flight = 2 * v / g;
      if (dt < flight) { const y = -(v * dt - .5 * g * dt * dt); const sq = Math.max(0, .3 * (1 - dt / .06)); return { y, sx: 1 + sq, sy: 1 - sq }; }
      dt -= flight; v *= e;
    }
    return { y: 0, sx: 1, sy: 1 };
  }
  function shockwave(ring, t, at, { maxR = 900, dur = .9 } = {}) {
    const k = P(t, at, dur); ring.style.opacity = k > 0 && k < 1 ? (1 - k) : 0;
    const r = eOut(k) * maxR; ring.style.width = ring.style.height = 2 * r + 'px'; ring.style.marginLeft = ring.style.marginTop = -r + 'px';
    ring.style.borderWidth = Math.max(1, 18 * (1 - k)) + 'px';
  }

  /* 8. Collage: torn-paper edge (seeded jagged polygon) and a halftone overlay. */
  function tornEdge(el, seed = 3, teeth = 38, depth = 2.2) {
    const r = rand(seed), pts = [];
    for (let i = 0; i <= teeth; i++) pts.push(`${(i / teeth * 100).toFixed(2)}% ${(r() * depth).toFixed(2)}%`);
    for (let i = teeth; i >= 0; i--) pts.push(`${(i / teeth * 100).toFixed(2)}% ${(100 - r() * depth).toFixed(2)}%`);
    el.style.clipPath = `polygon(${pts.join(',')})`;
  }
  function halftone(el, { size = 9, color = 'rgba(0,0,0,.55)', angle = 30 } = {}) {
    el.style.backgroundImage = `radial-gradient(circle at center, ${color} 32%, transparent 34%)`;
    el.style.backgroundSize = `${size}px ${size}px`; el.style.transform = `rotate(${angle}deg) scale(1.6)`;
  }

  /* 9. Data: count a real number up with tabular figures and draw a line chart from real values. */
  function count(el, t, start, dur, value, { decimals = 0, prefix = '', suffix = '' } = {}) {
    el.style.fontVariantNumeric = 'tabular-nums';
    el.textContent = prefix + (value * eOut(P(t, start, dur))).toFixed(decimals) + suffix;
  }
  function lineChart(svg, values, t, start, dur, { w = 800, h = 300, pad = 10 } = {}) {
    if (!svg.__path) {
      const lo = Math.min(...values), hi = Math.max(...values);
      const d = values.map((v, i) => `${i ? 'L' : 'M'}${(pad + i / (values.length - 1) * (w - 2 * pad)).toFixed(1)} ${(h - pad - (v - lo) / (hi - lo || 1) * (h - 2 * pad)).toFixed(1)}`).join(' ');
      svg.setAttribute('viewBox', `0 0 ${w} ${h}`);
      svg.innerHTML = `<path d="${d}" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>`;
      svg.__path = svg.firstChild;
    }
    const p = svg.__path, L = p.__len || (p.__len = p.getTotalLength());
    p.style.strokeDasharray = L; p.style.strokeDashoffset = L * (1 - eIO(P(t, start, dur)));
  }

  /* 10. 3D: a Three.js scene whose clock is t (never real time). Load three as an ES module first:
         <script type="module">import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js'; window.THREE = THREE;</script>
         Then: const s = scene3d(container, W, H); each frame: s.render(t, (root, t) => { root.rotation.y = t * .6; }); */
  function scene3d(container, w, h, { background = null } = {}) {
    const T = G.THREE; if (!T) throw new Error('scene3d: load three.js first');
    const renderer = new T.WebGLRenderer({ antialias: true, alpha: background === null, preserveDrawingBuffer: true });
    renderer.setSize(w, h); renderer.setPixelRatio(1); container.append(renderer.domElement);
    const scene = new T.Scene(); if (background) scene.background = new T.Color(background);
    const cam = new T.PerspectiveCamera(35, w / h, .1, 100); cam.position.set(0, 0, 6);
    scene.add(new T.AmbientLight(0xffffff, .5)); const key = new T.DirectionalLight(0xffffff, 1.6); key.position.set(3, 4, 5); scene.add(key);
    const root = new T.Group(); scene.add(root);
    return { T, scene, camera: cam, root, render(t, update) { update && update(root, t, cam); renderer.render(scene, cam); } };
  }

  G.DENTFX = { clamp, P, eOut, eIO, rand, lettering, splitLetters, axisWave, boilFilter, boil, morph, camera, glitch, bounce, shockwave, tornEdge, halftone, count, lineChart, scene3d };
})(window);
