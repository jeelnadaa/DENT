#!/usr/bin/env python3
"""DENT video kit score: an original, beat-locked score and sound design from timeline.json (no samples, no licences).

  python score.py                     # -> out/score.wav, mastered to -14 LUFS, true peak <= -1.5 dBTP
  python score.py --voice vo.wav      # also mixes a narration stem (from tts.py post) and ducks the music under it

Every timeline "sfx" event gets a sound on its exact time; the music bed plays the "music" progression on the bpm grid
and drops out where the picture needs silence. Extend the palette below for your film's concept.
Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import wave
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SR = 48000
rng = np.random.default_rng(3)


def env(n, a=.004, r=8.0):
    t = np.arange(n) / SR
    return np.minimum(1, t / a) * np.exp(-t * r)


def tone(f, dur, partials=((1, 1),), decay=6.0, vol=.3):
    n = int(dur * SR)
    t = np.arange(n) / SR
    return vol * sum(a * np.sin(2 * np.pi * f * k * t) * np.exp(-t * decay * (1 + .3 * k)) for k, a in partials)


def noise(dur, decay=30.0, vol=.3, lp=0.0):
    n = int(dur * SR)
    x = rng.standard_normal(n)
    if lp:
        x = np.convolve(x, np.ones(int(lp)) / lp, mode="same")
    return vol * x * env(n, .002, decay)


def layer(*sigs):
    """Sum sounds of different lengths."""
    out = np.zeros(max(len(x) for x in sigs))
    for x in sigs:
        out[: len(x)] += x
    return out


PALETTE = {
    "hit": lambda: layer(tone(55, .5, ((1, 1), (2, .3)), 7, .7), noise(.5, 40, .15)),
    "stab": lambda: tone(293.66, .6, ((1, 1), (2, .4), (3, .2)), 5, .25),
    "whoosh": lambda: noise(.7, 3, .18, 40) * np.sin(np.linspace(0, np.pi, int(.7 * SR))),
    "type": lambda: noise(.012, 300, .18),
    "impact": lambda: layer(tone(40, 2.2, ((1, 1), (1.5, .4)), 1.8, .9), noise(.4, 25, .4), tone(196, 2.5, ((1, .3), (2.76, .2), (5.4, .1)), .9, .5)),
    "logo": lambda: layer(*[np.pad(tone(f, 2.5, ((1, 1), (2.76, .4), (5.4, .2)), 2.2, .18), (int(i * .2 * SR), 0)) for i, f in enumerate((587.33, 880, 1174.66))]),
}


def place(buf, sig, t):
    s = int(t * SR)
    e = min(len(buf), s + len(sig))
    if 0 <= s < len(buf):
        buf[s:e] += sig[: e - s]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice")
    a = ap.parse_args()
    tl = json.loads((HERE / "timeline.json").read_text(encoding="utf-8"))
    N = int(tl["duration"] * SR) + SR
    music, sfx = np.zeros(N), np.zeros(N)
    bt = 60 / tl["bpm"]
    m = tl.get("music")
    if m:  # kick on 1 and 3, hats on the off-beats, a pad per bar, sidechained to the kick
        t, bar = m["from"], 0
        side = np.ones(N)
        while t < m["to"]:
            chord = m["progression"][bar % len(m["progression"])]
            for b in range(4):
                tb = t + b * bt
                if tb >= m["to"]:
                    break
                if b in (0, 2):
                    place(music, tone(50, .4, ((1, 1),), 9, .55), tb)
                    s, e = int(tb * SR), int((tb + .25) * SR)
                    side[s:e] = np.minimum(side[s:e], .35 + .65 * np.linspace(0, 1, e - s))
                place(music, noise(.05, 70, .05), tb + bt / 2)
            n = int(4 * bt * SR)
            pad = sum(np.sin(2 * np.pi * m["key_hz"] * 2 ** (s / 12) * np.arange(n) / SR) for s in chord) * .025
            place(music, pad * np.minimum(1, np.arange(n) / (.3 * SR)) * np.minimum(1, (n - np.arange(n)) / (.3 * SR)), t)
            t += 4 * bt
            bar += 1
        music *= side
    for ev in tl.get("sfx", []):
        k = ev["kind"]
        if k == "type":  # a burst of key clicks
            for i in range(int(ev.get("dur", 1) * 14)):
                place(sfx, PALETTE["type"](), ev["t"] + i / 14 + rng.uniform(-.01, .01))
        elif k in PALETTE:
            place(sfx, PALETTE[k](), ev["t"])
    mix = music + sfx
    if a.voice:
        with wave.open(a.voice) as w:
            v = np.frombuffer(w.readframes(w.getnframes()), "<i2").astype(float) / 32768
        v = v[:N] if len(v) >= N else np.pad(v, (0, N - len(v)))
        e = np.convolve(np.abs(v), np.ones(4800) / 4800, mode="same")
        duck = 1 - .7 * np.clip(e / (e.max() + 1e-9) * 3, 0, 1)
        mix = music * duck + sfx + v
    mix = mix[: int(tl["duration"] * SR)]
    mix = mix / (np.abs(mix).max() + 1e-9) * .7
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    pre = out / "score_pre.wav"
    with wave.open(str(pre), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((np.clip(mix, -1, 1) * 32767).astype("<i2").tobytes())

    def measure(p):
        r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-af", "loudnorm=I=-14:TP=-1.5:print_format=json", "-f", "null", "-"],
                           capture_output=True, text=True)
        return json.loads(r.stderr[r.stderr.rfind("{"): r.stderr.rfind("}") + 1])
    gain = -14 - float(measure(pre)["input_i"])
    dst = out / "score.wav"
    for _ in range(4):  # gain + oversampled true-peak limiter, corrected until it lands
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(pre), "-af",
                        f"volume={gain:.2f}dB,aresample=192000,alimiter=limit={10 ** (-1.8 / 20):.4f}:attack=3:release=60:level=false,aresample=48000",
                        "-ac", "2", str(dst)])
        m_ = measure(dst)
        if abs(float(m_["input_i"]) + 14) <= .5:
            break
        gain += -14 - float(m_["input_i"])
    pre.unlink(missing_ok=True)
    print(f"wrote {dst}: {m_['input_i']} LUFS, true peak {m_['input_tp']} dBTP")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
