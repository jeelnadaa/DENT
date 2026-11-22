#!/usr/bin/env python3
"""DENT video kit score: an original, beat-locked score and sound design from timeline.json (no samples, no licences).

  python score.py                     # -> out/score.wav (stereo), mastered to -14 LUFS, true peak <= -1.5 dBTP
  python score.py --voice vo.wav      # also mixes a narration stem (from tts.py post) and ducks the music under it

timeline.json fields (all times in seconds):
  "music": {"from", "to", "key_hz" (root note in Hz, e.g. 146.83 = D3), "progression": one list per bar of semitone offsets
            from key_hz (e.g. [0,3,7,10] = minor 7th), "style": pulse|cinematic|playful|minimal|<registered>,
            "drop": [[start, end], …] silences, "lift": time where the arrangement opens up}
  "sfx":   [{"t", "kind", "dur"?, "gain"?, "hz"?}, …] designed sounds exactly on picture events; kinds include hits, ticks,
           risers (end on t) and material families (paper_rip, paper_flick, riffle, glass, liquid_drop, rain, cloth_swish)
  "vo":    [{"t", "file"}, …] narration lines placed at chosen times (lines from tts.py say, mastered or raw) The presets are instruments and arrangements to build from, not a house
sound: shape them to the film bible's sound world (references/video/video-creative-direction.md §3).
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


# ------------------------------------------------------------------ building blocks
def T(dur):
    return np.arange(int(dur * SR)) / SR


def adsr(n, a=.005, d=.08, s=.6, r=.15):
    t = np.arange(n) / SR
    tot = n / SR
    e = np.where(t < a, t / max(a, 1e-6), np.where(t < a + d, 1 - (1 - s) * (t - a) / max(d, 1e-6), s))
    return e * np.clip((tot - t) / max(r, 1e-6), 0, 1)


def lp(x, cutoff):
    """One-pole low-pass, vectorised in blocks via cumulative filtering."""
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(0, len(x), 2048):
        seg = x[i:i + 2048]
        out = np.empty_like(seg)
        for j, v in enumerate(seg):
            acc = (1 - a) * v + a * acc
            out[j] = acc
        y[i:i + 2048] = out
    return y


def fm(f, dur, ratio=2.0, index=3.0, decay=4.0, vol=.25):
    """Two-operator FM: bells (ratio 3.5, high index), electric piano (ratio 1, index 2), bass (ratio 1, index 1.5)."""
    t = T(dur)
    mod_env = np.exp(-t * decay * 1.5)
    return vol * np.sin(2 * np.pi * f * t + index * mod_env * np.sin(2 * np.pi * f * ratio * t)) * np.exp(-t * decay)


def pluck(f, dur=.5, vol=.25, bright=6000):
    """Karplus-Strong string/marimba-ish pluck."""
    n, p = int(dur * SR), max(2, int(SR / f))
    buf = rng.uniform(-1, 1, p)
    out = np.empty(n)
    for i in range(n):
        out[i] = buf[i % p]
        buf[i % p] = .5 * (buf[i % p] + buf[(i + 1) % p]) * .996
    return vol * lp(out, bright)


def pad(freqs, dur, vol=.06, cutoff=1400, detune=.004):
    t = T(dur)
    sig = sum(np.sign(np.sin(2 * np.pi * f * (1 + d) * t)) * .3 + (2 * ((t * f * (1 + d)) % 1) - 1) * .7
              for f in freqs for d in (-detune, 0, detune))
    return vol * lp(sig, cutoff) * adsr(len(t), .6, .4, .85, min(1.2, dur * .4))


def kick(vol=.9, punch=110):
    t = T(.5)
    f = 42 + punch * np.exp(-t * 30)
    return vol * (np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7) + .25 * rng.standard_normal(len(t)) * np.exp(-t * 300))


def snare(vol=.45):
    t = T(.35)
    noise = rng.standard_normal(len(t))
    return vol * (.65 * (noise - lp(noise, 1500)) * np.exp(-t * 18) + .45 * np.sin(2 * np.pi * 190 * t) * np.exp(-t * 25))


def hat(vol=.08, open_=False):
    t = T(.3 if open_ else .06)
    n = rng.standard_normal(len(t))
    return vol * (n - lp(n, 7000)) * np.exp(-t * (12 if open_ else 70))


def taiko(vol=.8):
    t = T(1.2)
    f = 60 + 40 * np.exp(-t * 12)
    return vol * (np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 3.5) + .3 * lp(rng.standard_normal(len(t)), 800) * np.exp(-t * 20))


def riser(dur, vol=.18):
    t = T(dur)
    n = rng.standard_normal(len(t))
    sweep = np.sin(2 * np.pi * np.cumsum(200 * (8 ** (t / dur))) / SR)
    return vol * (t / dur) ** 2 * (.6 * (n - lp(n, 3000)) + .4 * sweep)


def layer(*sigs):
    out = np.zeros(max(len(x) for x in sigs))
    for x in sigs:
        out[: len(x)] += x
    return out


def reverb(x, mix=.22, room=.84):
    """Schroeder reverb: four combs + two all-passes. Returns (left, right) with decorrelated tails."""
    def comb(sig, d, g):
        y = np.copy(sig)
        for i in range(d, len(sig)):
            y[i] += g * y[i - d]
        return y

    def allpass(sig, d, g=.5):
        y = np.zeros_like(sig)
        for i in range(len(sig)):
            xd = sig[i - d] if i >= d else 0.0
            yd = y[i - d] if i >= d else 0.0
            y[i] = -g * sig[i] + xd + g * yd
        return y
    small = x[::4]                       # run the tail at 12 kHz for speed, then upsample
    outs = []
    for offs in ((1116, 1188, 1277, 1356), (1139, 1211, 1300, 1379)):
        wet = sum(comb(small, d // 4, room) for d in offs) / 4
        wet = allpass(allpass(wet, 556 // 4), 441 // 4)
        outs.append(np.repeat(wet, 4)[: len(x)])
    return x * (1 - mix) + outs[0] * mix, x * (1 - mix) + outs[1] * mix


# ------------------------------------------------------------------ designed SFX (picture events)
# Every kind takes the event dict (t, dur, any extra keys). Materials give each film its own sound world:
# pick the family that matches the bible's WORLD & MATERIAL, then register your own with register_sfx().
def _paper_rip(dur=.45):
    t = T(dur)
    n = rng.standard_normal(len(t))
    crackle = (rng.random(len(t)) < .02) * rng.standard_normal(len(t)) * 2
    return .35 * (n - lp(n, 2500) + crackle) * np.minimum(1, t / .01) * np.exp(-t * 4) * (.6 + .4 * np.sin(2 * np.pi * 37 * t))


def _paper_flick(dur=.12):
    t = T(dur)
    n = rng.standard_normal(len(t))
    return .3 * (n - lp(n, 1800)) * np.exp(-t * 45)


def _glass(f=2093.0, dur=1.6):
    return layer(fm(f, dur, 2.76, 1.2, 3.0, .12), fm(f * 1.5, dur, 3.9, .8, 4.0, .06))


def _drop(dur=.35):
    t = T(dur)
    f = 1400 * np.exp(-t * 18) + 380
    return .3 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 14)


def _swish(dur=.5):
    t = T(dur)
    n = lp(rng.standard_normal(len(t)), 1200)
    return .35 * n * np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 2


SFX = {
    # hits and accents
    "hit": lambda e: layer(kick(.8, 140), snare(.25)),
    "stab": lambda e: fm(e.get("hz", 293.66), .8, 1.0, 2.5, 3.5, .3),
    "impact": lambda e: layer(taiko(1.0), kick(.9, 60), fm(98, 2.5, 3.5, 6, 1.2, .25)),
    "thud": lambda e: taiko(.6),
    "tick": lambda e: fm(e.get("hz", 1760), .15, 3.5, 2, 18, .15),
    "pop": lambda e: pluck(e.get("hz", 880), .25, .3),
    "riser": lambda e: riser(e.get("dur", 1.5)),
    "air": lambda e: lp(rng.standard_normal(int(e.get("dur", .7) * SR)), 2500) * np.sin(np.linspace(0, np.pi, int(e.get("dur", .7) * SR))) * .3,
    "logo": lambda e: layer(*[np.pad(fm(f, 2.6, 3.5, 4, 1.8, .2), (int(i * .19 * SR), 0)) for i, f in enumerate(e.get("notes", (587.33, 880, 1174.66)))]),
    # materials
    "paper_rip": lambda e: _paper_rip(e.get("dur", .45)),
    "paper_flick": lambda e: _paper_flick(e.get("dur", .12)),
    "glass": lambda e: _glass(e.get("hz", 2093.0), e.get("dur", 1.6)),
    "liquid_drop": lambda e: _drop(e.get("dur", .35)),
    "cloth_swish": lambda e: _swish(e.get("dur", .5)),
    "key": lambda e: rng.standard_normal(int(.012 * SR)) * np.exp(-T(.012) * 300) * .18,
}
# kinds that repeat over a duration (dur seconds at rate per second)
REPEAT = {"type": ("key", 14), "riffle": ("paper_flick", 22), "rain": ("liquid_drop", 9)}
STYLES = {}  # name -> function(m, bt, N, chord_at) returning a music array; see register_style()


def register_sfx(name, fn):
    """Add a sound for this film: fn(event_dict) -> mono numpy array at 48 kHz. Then use {"t": .., "kind": name} in timeline.json."""
    SFX[name] = fn


def register_style(name, fn):
    """Add an arrangement: fn(m, bt, N) -> mono numpy array (len N). Use "style": name in timeline.json "music".
    Recommended path for a film's own score: a small score_<film>.py that does `import score as K`, registers its sounds
    and styles with K's instruments (K.fm, K.pluck, K.pad, K.kick, K.snare, K.taiko, K.riser, K.reverb...), then calls K.main()."""
    STYLES[name] = fn


def place(buf, sig, t):
    s = int(t * SR)
    if s < 0 or s >= len(buf):
        return
    e = min(len(buf), s + len(sig))
    buf[s:e] += sig[: e - s]


# ------------------------------------------------------------------ arrangements (presets to shape, not a house sound)
def arrange(m, bt, N):
    style = m.get("style", "pulse")
    if style in STYLES:
        return STYLES[style](m, bt, N)
    music, side = np.zeros(N), np.ones(N)
    t, bar = m["from"], 0
    lift = m.get("lift", 1e9)
    while t < m["to"] - 1e-6:
        chord = [m["key_hz"] * 2 ** (s / 12) for s in m["progression"][bar % len(m["progression"])]]
        root, opened = chord[0], t >= lift
        bar_len = 4 * bt
        place(music, pad(chord, bar_len + .4, .05 if style != "minimal" else .03, 900 if not opened else 2200), t)
        for b in range(8):                                  # eighth notes
            tb = t + b * bt / 2
            if tb >= m["to"]:
                break
            if style in ("pulse", "playful"):
                if b in (0, 4) or (opened and b == 6):
                    place(music, kick(.75), tb)
                    s0, s1 = int(tb * SR), int((tb + .22) * SR)
                    side[s0:s1] = np.minimum(side[s0:s1], .35 + .65 * np.linspace(0, 1, max(1, s1 - s0)))
                if b in (2, 6):
                    place(music, snare(.35 if style == "pulse" else .25), tb)
                place(music, hat(.06, open_=(b == 7 and opened)), tb)
                bass = fm(root / 2, bt / 2 * .9, 1.0, 1.6, 5, .28) if style == "pulse" else pluck(root, bt / 2, .22, 2500)
                if b % 2 == 0 or opened:
                    place(music, bass, tb)
                if style == "playful" and b % 2 == 1:
                    place(music, pluck(chord[(b // 2) % len(chord)] * 2, .4, .16, 5000), tb)
                if style == "pulse" and opened and b % 2 == 1:
                    place(music, fm(chord[(b // 2) % len(chord)] * 2, .3, 3.5, 1.5, 6, .07), tb)
            elif style == "cinematic":
                if b == 0:
                    place(music, taiko(.55 if not opened else .8), tb)
                    place(music, fm(root / 2, bar_len, 1.0, 1.2, .8, .22), tb)
                if opened and b in (3, 6):
                    place(music, taiko(.35), tb)
                if b % 2 == 0:
                    place(music, fm(chord[(b // 2) % len(chord)] * 2, .9, 2.0, 1.2, 2.5, .06), tb)
            elif style == "minimal":
                if b in (0, 3, 5) or (opened and b == 7):
                    place(music, fm(chord[b % len(chord)] * 2, 1.4, 1.0, 1.0, 1.6, .14), tb)   # e-piano-like
        t += bar_len
        bar += 1
    music *= side
    for s0, s1 in m.get("drop", []):                         # deliberate silences, with short fades
        a, b = int(s0 * SR), int(s1 * SR)
        f = int(.03 * SR)
        music[a:b] *= 0.0
        music[max(0, a - f):a] *= np.linspace(1, 0, a - max(0, a - f))
    return music


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice")
    a = ap.parse_args()
    tl = json.loads((HERE / "timeline.json").read_text(encoding="utf-8"))
    N = int(tl["duration"] * SR) + 2 * SR
    bt = 60 / tl["bpm"]
    music = arrange(tl["music"], bt, N) if tl.get("music") else np.zeros(N)
    sfx = np.zeros(N)
    unknown = set()
    for ev in tl.get("sfx", []):
        k = ev["kind"]
        if k in REPEAT:
            base, rate = REPEAT[k]
            for i in range(int(ev.get("dur", 1) * rate)):
                place(sfx, SFX[base](ev) * ev.get("gain", 1.0), ev["t"] + i / rate + rng.uniform(-.01, .01))
        elif k == "riser":   # a riser ends ON its event
            place(sfx, SFX[k](ev) * ev.get("gain", 1.0), ev["t"] - ev.get("dur", 1.5))
        elif k in SFX:
            place(sfx, SFX[k](ev) * ev.get("gain", 1.0), ev["t"])
        else:
            unknown.add(k)
    if unknown:
        print(f"warning: no sound registered for {sorted(unknown)} (register_sfx, or one of {sorted(SFX) + sorted(REPEAT)})")
    def read_mono(path):
        with wave.open(str(path)) as w:
            x = np.frombuffer(w.readframes(w.getnframes()), "<i2").astype(float) / 32768
            if w.getnchannels() == 2:
                x = x.reshape(-1, 2).mean(axis=1)
            if w.getframerate() != SR:
                x = np.interp(np.arange(0, len(x), w.getframerate() / SR), np.arange(len(x)), x)
        return x
    v = np.zeros(N)
    if a.voice:   # one finished narration file (from tts.py post), starting at 0
        x = read_mono(a.voice)
        v[: min(N, len(x))] += x[:N]
    for line in tl.get("vo", []):   # or each line placed at its own time: "vo": [{"t": 0.45, "file": "vo/lines/line_001.wav"}, ...]
        place(v, read_mono(HERE / line["file"]) * line.get("gain", 1.0), line["t"])
    if v.any():
        env = np.convolve(np.abs(v), np.ones(4800) / 4800, mode="same")
        music = music * (1 - .7 * np.clip(env / (env.max() + 1e-9) * 3, 0, 1))
    bed_l, bed_r = reverb(music * .9 + sfx * .35, mix=.2)
    left, right = bed_l + sfx * .65 + v, bed_r + sfx * .65 + v
    end = int(tl["duration"] * SR)
    st = np.stack([left[:end], right[:end]], axis=1)
    fade = int(.6 * SR)
    st[-fade:] *= np.linspace(1, 0, fade)[:, None]
    st = st / (np.abs(st).max() + 1e-9) * .7
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    pre = out / "score_pre.wav"
    with wave.open(str(pre), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((np.clip(st, -1, 1) * 32767).astype("<i2").tobytes())

    def measure(p):
        r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-af", "loudnorm=I=-14:TP=-1.5:print_format=json", "-f", "null", "-"],
                           capture_output=True, text=True)
        return json.loads(r.stderr[r.stderr.rfind("{"): r.stderr.rfind("}") + 1])
    gain = -14 - float(measure(pre)["input_i"])
    dst = out / "score.wav"
    # The WAV keeps true peak <= -2 dBTP so the AAC encode (which adds up to ~1 dB of overshoot) still lands under -1 dBTP.
    ceiling = -3.0
    for _ in range(6):  # gain + 4x oversampled limiter; correct loudness, and tighten the ceiling if true peak overshoots
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(pre), "-af",
                        f"volume={gain:.2f}dB,aresample=192000,alimiter=limit={10 ** (ceiling / 20):.4f}:attack=2:release=60:level=false,aresample=48000",
                        str(dst)])
        m_ = measure(dst)
        lufs_ok, tp_ok = abs(float(m_["input_i"]) + 14) <= .5, float(m_["input_tp"]) <= -2.0
        if lufs_ok and tp_ok:
            break
        if not tp_ok:
            ceiling -= float(m_["input_tp"]) + 2.0 + .2
        gain += -14 - float(m_["input_i"])
    pre.unlink(missing_ok=True)
    print(f"wrote {dst}: {m_['input_i']} LUFS, true peak {m_['input_tp']} dBTP (WAV ceiling -2 dBTP leaves room for AAC; "
          f"style: {tl.get('music', {}).get('style', 'none')}). "
          "Have a person listen before calling the sound done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
