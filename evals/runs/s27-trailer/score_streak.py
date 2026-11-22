#!/usr/bin/env python3
"""Score + sound design + narration mix for the Streak trailer ("Roots"), built from the kit's instruments in score.py.

Sound world (VIDEO.md bible): act 1 is the checkmark world, dry and clinical (ticks, a buzz, no reverb, no music);
act 2 is underground and organic (woody Karplus-Strong plucks, a low earth drone, a soft heartbeat kick, droplet taps,
root creaks); the climax opens the full arrangement after half a second of silence; act 3 is dawn (high plucks, bells).
Sonic logo: the three-note "sprout" motif (D-A-E rising fifths) plus a bud-pop. 96 bpm; every cue reads timeline.json.

  python score_streak.py      -> out/score.wav (stereo, -14 LUFS, true peak <= -1.5 dBTP) with the narration mixed in
"""
from __future__ import annotations

import json
import subprocess
import wave
from pathlib import Path

import numpy as np

import score as K   # the kit's instruments: fm, pluck, pad, kick, snare, hat, taiko, riser, lp, layer, reverb, place, T

HERE = Path(__file__).resolve().parent
SR = K.SR
tl = json.loads((HERE / "timeline.json").read_text(encoding="utf-8"))
E = tl["events"]
BT = 60 / tl["bpm"]
DUR = tl["duration"]
N = int(DUR * SR) + SR
rng = np.random.default_rng(11)
D = 146.83   # D3: the key of the film
hz = lambda semis, base=D: base * 2 ** (semis / 12)


def buf():
    return np.zeros(N)


# ------------------------------------------------------------------ designed sounds
def tick(i):            # act 1: dry clinical check tick, pitch creeping up as the streak grows
    return K.layer(K.fm(1500 + i * 18, .07, 2.0, 1.2, 40, .12), K.hat(.05))


def buzz():             # the missed day: a flat, nasal FM buzz with a pitch sag
    t = K.T(.42)
    f = 110 * (1 - .12 * t / .42)
    sig = np.sin(2 * np.pi * np.cumsum(f) / SR + 4 * np.sin(2 * np.pi * np.cumsum(f * 3.01) / SR))
    return .32 * np.tanh(2.5 * sig) * np.exp(-t * 4)


def slam():             # "zero": heavy and dull
    return K.layer(K.kick(.95, 70), K.taiko(.6), .3 * K.lp(rng.standard_normal(int(.4 * SR)), 900) * np.exp(-K.T(.4) * 12))


def clatter(n=18):      # the checks falling away: small dry ticks scattered over a second
    out = np.zeros(int(1.4 * SR))
    for k in range(n):
        s = int((rng.uniform(0, 1.1) ** 1.5) * SR)
        x = K.fm(rng.uniform(900, 2200), .05, 3.1, 1.0, 50, .05)
        out[s:s + len(x)] += x[: len(out) - s]
    return out


def whistle(dur):       # the falling check: descending sine
    t = K.T(dur)
    f = 1400 * (0.35 ** (t / dur))
    return .09 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.minimum(1, t / .05) * np.minimum(1, (dur - t) / .05)


def thud_soil():        # landing in soil: soft low thud + crumbly noise
    n = rng.standard_normal(int(.5 * SR))
    return K.layer(K.kick(.55, 40), .25 * K.lp(n, 1200) * np.exp(-K.T(.5) * 9))


def droplet():          # a watering tap: a pitched "plip"
    t = K.T(.18)
    f = 1800 * np.exp(-t * 22) + 500
    return .16 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 26)


def creak(dur=1.2):     # roots pushing through soil: filtered, gritty, slowly rising
    t = K.T(dur)
    n = rng.standard_normal(len(t))
    grains = (rng.random(len(t)) < .004).astype(float)
    g = np.convolve(grains, np.exp(-np.arange(200) / 30), mode="same")
    return .22 * K.lp(n * g, 1600) * np.sin(np.pi * t / dur)


def drone(dur, f=D / 2, vol=.08):
    t = K.T(dur)
    sig = np.sin(2 * np.pi * f * t) + .5 * np.sin(2 * np.pi * f * 1.5 * t + .3) + .25 * np.sin(2 * np.pi * f * 2.01 * t)
    return vol * sig * np.minimum(1, t / 1.0) * np.minimum(1, (dur - t) / 1.0)


def bloom(dur=2.6):     # the sonic logo's pad
    return K.pad([hz(0, D), hz(7, D), hz(14, D), hz(16, D)], dur, .05, 1800)


MOTIF = [0, 7, 14]      # D, A, E: rising fifths = growth


# ------------------------------------------------------------------ build
music, sfx = buf(), buf()
P = K.place

# act 1 (0–4.4): ticks, no music. 29 ticks match the picture's accelerating schedule.
tick_t = [.18 + 2.9 * (i / 28) ** .8 for i in range(29)]
for i, t in enumerate(tick_t):
    P(sfx, tick(i), t)
P(music, drone(4.6, D / 4, .05), 0.0)                      # a cold low hum under the sterile grid
P(sfx, buzz(), E["miss"])
P(sfx, slam(), E["reset"])
P(sfx, clatter(), E["reset"] + .02)
# the fall + the turn
P(sfx, whistle(E["land"] - E["fall"]), E["fall"])
P(sfx, thud_soil(), E["land"])
for k, s in enumerate(MOTIF):                              # the motif is born when the check becomes a seedling
    P(music, K.pluck(hz(s, D * 2), 1.2, .26, 5000), E["land"] + .35 + k * BT / 2)
P(sfx, creak(1.4), 6.2)
# act 2 underground (6.25–10): earth drone + plucked arpeggio as the name is written
P(music, drone(4.2, D / 2, .07), 6.0)
for i in range(6):                                          # one pluck per letter, rising
    P(music, K.pluck(hz([0, 2, 4, 7, 9, 12][i], D * 2), .9, .22, 4500), E["name"] + i * .27)
P(sfx, K.SFX["pop"](), E["name"] + 5 * .27 + .3)           # the leaf on the k opens


def groove(t0, t1, opened=False, thin=False):
    """Organic groove: heartbeat kick (1 and the 'and' of 2), woody plucks on eighths, FM bass; pads per bar."""
    prog = [[0, 7, 10, 15], [-4, 3, 7, 12], [-2, 5, 9, 14], [-7, 0, 3, 7]]    # Dm  Bb  C  G/D-ish: earthy, hopeful
    t, bar = t0, 0
    while t < t1 - 1e-6:
        chord = [hz(s) for s in prog[bar % 4]]
        bar_len = min(4 * BT, t1 - t)
        P(music, K.pad(chord, bar_len + .3, .045 if not opened else .06, 900 if not opened else 2400), t)
        for e in range(8):
            tb = t + e * BT / 2
            if tb >= t1:
                break
            if e in (0, 3) or (opened and e in (4, 6)):
                P(music, K.kick(.55 if not thin else .35, 60), tb)
            if opened and e in (2, 6):
                P(music, K.snare(.18), tb)
            if not thin or e % 2 == 0:
                note = chord[[0, 2, 1, 3, 2, 1, 3, 2][e]] * 2
                P(music, K.pluck(note, .45, .14 if not opened else .17, 3800 if not opened else 6000), tb)
            if e % 4 == 0:
                P(music, K.fm(chord[0] / 2, BT * 1.8, 1.0, 1.4, 2.5, .2), tb)
            if opened and e % 2 == 1:
                P(music, K.fm(chord[e // 2 % 4] * 4, .25, 3.5, 1.5, 9, .045), tb)
        t += 4 * BT
        bar += 1


groove(10.0, 20.0)
for k in ("tap1", "tap2", "tap3", "tap4"):
    P(sfx, droplet(), E[k])
    P(music, K.pluck(hz(14, D * 2), .6, .18, 6000), E[k] + .12)    # leaf unfurl
P(sfx, K.layer(K.SFX["tick"](), droplet() * .3), E["garden"])                          # tab tap: a UI click, not a whoosh
for i in range(24):                                                    # time-lapse: arpeggio accelerating
    tt = E["lapse"] + 3.6 * (i / 24) ** 1.25
    P(music, K.pluck(hz([0, 7, 12, 14, 19, 24][i % 6], D * 2), .35, .1, 7000), tt)
P(sfx, creak(3.0) * .7, E["lapse"])
groove(20.0, 24.4, thin=True)
P(sfx, K.fm(hz(7, D), 1.4, 1.0, 1.2, 2.0, .16) * np.linspace(1, .4, int(1.4 * SR)), E["miss2"] + .3)    # the wilt
P(music, K.pluck(hz(5, D), .8, .2, 2500), E["miss2"] + .5)
P(sfx, K.layer(K.kick(.5, 50), K.fm(hz(-12), .5, 1, 1, 6, .2)), E["w2"])                                  # "It wilts."
P(sfx, K.layer(K.kick(.65, 50), K.fm(hz(-12), .6, 1, 1.3, 5, .25)), E["w3"])                              # "No reset."
P(sfx, K.riser(1.3) * .7, 24.4 - 1.3)
# 24.4–24.95: silence before the payoff (the drop below clears everything)
# climax: through the screen into the roots
P(sfx, K.SFX["impact"](), E["impact"])
P(sfx, K.SFX["whoosh"](), E["impact"] - .25)
P(sfx, creak(2.5), E["impact"] + .1)
groove(25.0, 32.5, opened=True)
P(sfx, K.layer(K.taiko(.9), K.fm(hz(12), 2.4, 3.5, 5, 1.4, .2)), E["title"])                             # title at the peak
P(sfx, K.riser(1.0) * .6, E["title"] - 1.0)
P(music, bloom(3.2), E["title"] + .1)
# act 3 dawn
P(sfx, creak(1.1), 32.5)                                               # rising out of the soil: earth, not air
t = 32.5
while t < 40.0 - 1e-6:                                                 # high, bright plucks + bells, light kick
    for e in range(8):
        tb = t + e * BT / 2
        if tb >= 40.0:
            break
        P(music, K.pluck(hz([12, 19, 24, 19, 14, 19, 26, 19][e]), .5, .12, 7000), tb)
        if e in (0, 4):
            P(music, K.kick(.4, 70), tb)
        if e in (2, 6):
            P(music, K.hat(.05), tb)
    P(music, K.pad([hz(s) for s in (0, 7, 12, 16)], 4 * BT + .3, .045, 2600), t)
    t += 4 * BT
P(sfx, droplet(), E["water"])
P(music, K.pluck(hz(19, D * 2), .7, .2, 6000), E["water"] + .3)        # the wilted plant perks up
P(sfx, K.SFX["pop"](), E["widget"])
P(sfx, creak(.8) * .7, 40.0)
# end: callback pops (the grid sprouts), then the sonic logo
for i in range(10):
    P(sfx, K.pluck(hz([24, 26, 28, 31, 33][i % 5], D * 2), .2, .05, 8000), 40.35 + i * .045)
for k, s in enumerate(MOTIF):
    P(music, K.fm(hz(s, D * 2), 2.4, 3.5, 3, 1.6, .16), E["logo"] + k * .19)
    P(music, K.pluck(hz(s, D * 2), 1.2, .2, 6000), E["logo"] + k * .19)
P(sfx, K.SFX["pop"](), E["logo"] + .6)
P(music, bloom(1.4), E["logo"] + .05)
P(music, drone(5.0, D / 2, .05), 40.0)

# deliberate silence before the payoff
a, b = int(24.4 * SR), int(24.95 * SR)
for x in (music, sfx):
    x[a:b] *= 0.0
    f = int(.04 * SR)
    x[a - f:a] *= np.linspace(1, 0, f)

# ------------------------------------------------------------------ narration placed on the grid, music ducked
with wave.open(str(HERE / "vo/narration.wav")) as w:
    sr = w.getframerate()
    v_src = np.frombuffer(w.readframes(w.getnframes()), "<i2").astype(float) / 32768
    if w.getnchannels() == 2:
        v_src = v_src.reshape(-1, 2).mean(axis=1)
if sr != SR:
    v_src = np.interp(np.arange(int(len(v_src) * SR / sr)) / SR, np.arange(len(v_src)) / sr, v_src)
voice = buf()
for ln in tl["vo"]:
    seg = v_src[int(ln["src_start"] * SR): int(ln["src_end"] * SR)]
    P(voice, seg, ln["at"])
env = np.convolve(np.abs(voice), np.ones(4800) / 4800, mode="same")
duck = 1 - .72 * np.clip(env / (env.max() + 1e-9) * 4, 0, 1)
music *= duck
sfx *= (1 - .35 * (1 - duck))

bed_l, bed_r = K.reverb(music * .9 + sfx * .25, mix=.24, room=.86)
# act 1 stays dry: remove the reverb tail before 4.4 s by crossfading to the dry signal
dry_end = int(4.4 * SR)
for bed in (bed_l, bed_r):
    bed[:dry_end] = music[:dry_end] * .9 + sfx[:dry_end] * .25
left = bed_l + sfx * .7 + voice * 1.0
right = bed_r + sfx * .7 + voice * 1.0
end = int(DUR * SR)
st = np.stack([left[:end], right[:end]], axis=1)
fade = int(.5 * SR)
st[-fade:] *= np.linspace(1, 0, fade)[:, None]
st = st / (np.abs(st).max() + 1e-9) * .7
out = HERE / "out"
out.mkdir(exist_ok=True)
pre = out / "score_pre.wav"
with wave.open(str(pre), "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(st, -1, 1) * 32767).astype("<i2").tobytes())


def measure(p):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-af", "loudnorm=I=-14:TP=-1.5:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    return json.loads(r.stderr[r.stderr.rfind("{"): r.stderr.rfind("}") + 1])


gain = -14 - float(measure(pre)["input_i"])
dst = out / "score.wav"
for _ in range(4):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(pre), "-af",
                    f"volume={gain:.2f}dB,aresample=192000,alimiter=limit={10 ** (-1.8 / 20):.4f}:attack=3:release=60:level=false,aresample=48000",
                    str(dst)])
    m_ = measure(dst)
    if abs(float(m_["input_i"]) + 14) <= .5:
        break
    gain += -14 - float(m_["input_i"])
pre.unlink(missing_ok=True)
print(f"wrote {dst}: {m_['input_i']} LUFS, true peak {m_['input_tp']} dBTP. Not heard by a person: sound is unverified.")
