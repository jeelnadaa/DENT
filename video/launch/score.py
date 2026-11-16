"""Original score + sound design for the DENT launch film, synthesised from scratch (no samples, no licences needed).

Every cue is read from timeline.js, the same file the picture uses, so cuts and hits stay frame-locked.
Key: D minor (the generic world) resolving to D major on the sonic logo (the dent). 120 BPM.

  python score.py            -> out/score_raw.wav, then loudness-normalised out/score.wav (-14 LUFS, TP <= -1 dBTP)
"""
import json, re, subprocess
from pathlib import Path
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile

HERE = Path(__file__).resolve().parent
OUT = HERE / "out"; OUT.mkdir(exist_ok=True)
T = json.loads(re.search(r"window\.TL\s*=\s*(\{.*\})", (HERE / "timeline.js").read_text(), re.S).group(1))
SR = 48000
DUR = T["duration"]
N = int(DUR * SR)
rng = np.random.default_rng(7)

# ---------------------------------------------------------------- buses
dry = np.zeros((2, N + SR * 3))
verb = np.zeros_like(dry)        # reverb send
duck = np.ones(N + SR * 3)       # sidechain gain for music (from kicks)
music = np.zeros_like(dry)       # music bus (ducked by kick)


def hz(m): return 440.0 * 2 ** ((m - 69) / 12)
def tt(d): return np.arange(int(d * SR)) / SR


def place(bus, sig, t0, g=1.0, pan=0.0):
    i = int(round(t0 * SR))
    if i >= bus.shape[1]: return
    sig = sig[: bus.shape[1] - i]
    if sig.ndim == 1:
        l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
        bus[0, i:i + len(sig)] += sig * g * l * 1.4142
        bus[1, i:i + len(sig)] += sig * g * r * 1.4142
    else:
        bus[:, i:i + sig.shape[1]] += sig * g


def filt(x, f, kind="low", order=2):
    if kind == "band": sos = butter(order, f, btype="band", fs=SR, output="sos")
    else: sos = butter(order, f, btype=kind, fs=SR, output="sos")
    return sosfilt(sos, x)


def noise(d): return rng.standard_normal(int(d * SR))


# ---------------------------------------------------------------- instruments
def kick(d=.55, f0=46, f1=150, punch=28, decay=7.0):
    t = tt(d); f = f0 + (f1 - f0) * np.exp(-t * punch)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-t * decay)
    click = filt(noise(d), 3000, "high") * np.exp(-t * 400) * .35
    return np.tanh(1.6 * (body + click)) * .9


def clap(d=.35):
    t = tt(d); n = filt(noise(d), [900, 2600], "band")
    env = np.zeros_like(t)
    for o in (0, .011, .022): env += (t >= o) * np.exp(-(t - o).clip(0) * 220)
    env += (t >= .03) * np.exp(-(t - .03).clip(0) * 18) * .5
    return n * env * .55


def hat(d=.08, open_=False):
    t = tt(d if not open_ else .3); n = filt(noise(len(t) / SR), 7500, "high")
    return n * np.exp(-t * (55 if not open_ else 11)) * .35


def shaker(d=.09):
    t = tt(d); n = filt(noise(d), [5000, 9000], "band")
    return n * (1 - np.exp(-t * 300)) * np.exp(-t * 45) * .25


def saw(f, d, detune=0.0):
    t = tt(d); ph = (f * (1 + detune) * t + rng.random()) % 1.0
    return 2 * ph - 1


def pad(notes, d, cutoff=1600, att=.35, rel=.9):
    t = tt(d + rel); x = np.zeros((2, len(t)))
    for m in notes:
        f = hz(m)
        for dt, side in ((-.004, 0), (.004, 1), (0.0, None)):
            s = saw(f, d + rel, dt)
            if side is None: x += s * .5
            else: x[side] += s
    x = np.stack([filt(x[0], cutoff), filt(x[1], cutoff)])
    env = np.minimum(1, t / att) * np.where(t < d, 1, np.exp(-(t - d) * (6 / rel)))
    return x * env / (len(notes) * 1.8)


def stab(notes, d=.32, cutoff=3200):
    t = tt(d); x = np.zeros((2, len(t)))
    for m in notes:
        f = hz(m); x[0] += saw(f, d, -.003); x[1] += saw(f, d, .003)
    x = np.stack([filt(x[0], cutoff), filt(x[1], cutoff)])
    return x * np.exp(-t * 9) * (1 - np.exp(-t * 400)) / (len(notes) * 1.2)


def fm(f, d=.8, ratio=1.0, index=3.0, idecay=18, adecay=5.5):
    t = tt(d); mod = np.sin(2 * np.pi * f * ratio * t) * index * np.exp(-t * idecay)
    return np.sin(2 * np.pi * f * t + mod) * np.exp(-t * adecay) * (1 - np.exp(-t * 900))


def pluck(m, d=.7): return fm(hz(m), d, 1.0, 2.6, 22, 6.5) * .5
def bell(m, d=1.6): return fm(hz(m), d, 3.5, 2.2, 7, 3.2) * .38
def marimba(m, d=.6): return (fm(hz(m), d, 4.0, 1.4, 30, 9) * .6 + fm(hz(m), d, 1.0, .6, 20, 8) * .4) * .55


def bass(m, d, glide_from=None):
    t = tt(d + .06); f = np.full(len(t), hz(m))
    if glide_from is not None: f = hz(m) + (hz(glide_from) - hz(m)) * np.exp(-t * 40)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) + .28 * np.sin(2 * ph) + .08 * np.sin(3 * ph)
    env = np.minimum(1, t / .006) * np.where(t < d, 1 - .2 * (t / d), 0.8 * np.exp(-(t - d) * 60))
    return np.tanh(1.3 * x * env) * .55


def tok(m=74, d=.25):  # woodblock: the dot's voice
    t = tt(d); f = hz(m) * (1 + .5 * np.exp(-t * 120))
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) * np.exp(-t * 32) + .5 * np.sin(2.76 * ph) * np.exp(-t * 60)
    x += filt(noise(d), 2500, "high") * np.exp(-t * 500) * .3
    return x * .7


def thunk(weight=1.0, d=.6):  # letterpress stamp: low body + paper crunch
    t = tt(d)
    f = 62 + 70 * np.exp(-t * 35)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)
    mid = np.sin(2 * np.pi * 190 * t) * np.exp(-t * 38) * .4
    paper = filt(noise(d), [600, 3200], "band") * np.exp(-t * 55) * .55
    click = filt(noise(d), 4000, "high") * np.exp(-t * 700) * .3
    return np.tanh(1.5 * (body * weight + mid + paper + click)) * .85


def tick(f=3200, d=.03, g=.3):
    t = tt(d); return filt(noise(d), [f * .7, f * 1.4], "band") * np.exp(-t * 260) * g


def keyclick():
    t = tt(.05)
    x = filt(noise(.05), [1800, 5200], "band") * np.exp(-t * 300) * .5
    x += np.sin(2 * np.pi * 140 * t) * np.exp(-t * 90) * .25
    return x * (0.7 + .5 * rng.random())


def whoosh(d=.6, f0=300, f1=4000, g=.5, peak=.6):
    """Band-limited noise whose band sweeps f0 -> f1; loudest at `peak` (0..1 of d)."""
    t = tt(d); out = np.zeros(len(t)); bands = 10
    for k in range(bands):
        c = f0 * (f1 / f0) ** (k / (bands - 1))
        n = filt(noise(d), [c * .7, min(c * 1.4, SR / 2 - 100)], "band")
        center = d * (k / (bands - 1)); w = d / bands * 1.6
        out += n * np.exp(-((t - center) / w) ** 2)
    shape = np.exp(-((t / d - peak) / .32) ** 2)
    return out * shape * g


def riser(d=2.0, g=.35):
    t = tt(d); p = t / d
    n = filt(noise(d), 1500, "high") * p ** 2.2
    f = 180 * (8 ** p); s = np.sin(2 * np.pi * np.cumsum(f) / SR) * p ** 2 * .3
    return (n * .6 + s) * g


def fall_whistle(d=.62):
    t = tt(d); f = 1900 * (300 / 1900) ** (t / d)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.minimum(1, t / .08) * (1 - (t / d) ** 6)
    return x * .16


def impact(d=3.2):
    t = tt(d)
    f = 30 + 45 * np.exp(-t * 6)
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 1.8)
    crack = filt(noise(d), 3500) * np.exp(-t * 14) * .7
    body = np.sin(2 * np.pi * 110 * t) * np.exp(-t * 16) * .5
    return np.tanh(1.8 * (boom + crack + body)) * .95


def pop(f0=420, f1=980, d=.12):  # glossy UI pop for the generic template (deliberately cheesy)
    t = tt(d); f = f0 + (f1 - f0) * (1 - np.exp(-t * 60))
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 34) * .3


def zip_(d=.18):  # marker strike
    t = tt(d); return whoosh(d, 1200, 7000, .5, .45) + filt(noise(d), [3000, 6000], "band") * np.exp(-t * 25) * .15


def snare_hit(d=.25):
    t = tt(d); return (filt(noise(d), [1200, 7000], "band") * np.exp(-t * 22) * .5 + np.sin(2 * np.pi * 190 * t) * np.exp(-t * 30) * .3)


# ---------------------------------------------------------------- harmony
DM9 = [50, 53, 57, 60, 64]; BB = [46, 50, 53, 57, 60]; FM7 = [53, 57, 60, 64]; CSUS = [48, 55, 62, 64]
PROG = [(DM9, 38), (BB, 34), (FM7, 41), (CSUS, 36)]
DMAJ = [50, 57, 62, 66, 69, 76]  # D major add9 voicing for the resolution
PENT = [74, 77, 79, 81, 84, 86, 89, 91]  # D minor pentatonic, D5 up


def bars(t0, t1):
    b = int(np.floor(t0 / 2 + 1e-9)) * 2.0
    while b < t1 - 1e-9: yield b; b += 2.0


def kick_at(t, g=1.0, music_duck=.55):
    place(dry, kick(), t, g)
    i = int(t * SR); L = int(.4 * SR)
    env = 1 - music_duck * np.exp(-np.arange(L) / SR * 9)
    duck[i:i + L] = np.minimum(duck[i:i + L], env[: len(duck[i:i + L])])


def groove(t0, t1, prog_on=True, clap_on=True, hats=True, bright=1.0, pluck_on=True, shak=True, kick_g=1.0, half=False, lvl=1.0):
    for b in bars(t0, t1):
        k = int(b / 2) % 4
        chord, root = PROG[k]
        for beat in range(4):
            tb = b + beat * .5
            if t0 - 1e-9 <= tb < t1 and not (half and beat in (1, 3)): kick_at(tb, kick_g * lvl)
            if clap_on and beat in (1, 3) and t0 <= tb < t1: place(dry, clap(), tb, .8 * lvl, .05); place(verb, clap(), tb, .25)
            if hats and t0 <= tb + .25 < t1: place(dry, hat(), tb + .25, .9, .25)
            if shak:
                for s in (0, .125, .25, .375):
                    if t0 <= tb + s < t1: place(dry, shaker(), tb + s, .5 + .3 * (s == .25), -.3)
        if prog_on:
            s0 = max(b, t0); seg = min(b + 2.0, t1) - s0
            place(music, pad(chord, seg, 1100 + 900 * bright, att=.35 if s0 == b else .08), s0, .55 * lvl)
            # bass: root on 1, octave pickup on the and-of-2, approach on 4-and
            for (o, m, d) in ((0, root, .45), (.75, root + 12, .2), (1.0, root, .45), (1.75, root + 7, .2)):
                if t0 <= b + o < t1: place(music, bass(m, d), b + o, .62)
            if pluck_on:
                tones = sorted(set([n + 24 for n in chord]))
                pat = [0, 2, 1, 3, 2, 4, 1, 2]
                for j, idx in enumerate(pat):
                    tp = b + j * .25
                    if t0 <= tp < t1:
                        m = tones[idx % len(tones)]
                        sig = pluck(m) * (.55 + .2 * (j % 2 == 0)) * bright
                        place(music, sig, tp, .45, .35 * (1 if j % 2 else -1))
                        place(verb, sig, tp, .18)


# ================================================================ THE CUE SHEET
# S1 hook: words punch in on the beat over a low drone
place(music, pad([26, 38], 7.0, 500, att=1.2, rel=.4), 0.0, .7)
for i, w in enumerate(T["words"]):
    place(dry, thunk(.8, .4), w, .55 + .05 * i)
    place(dry, kick(.35, 50, 120, 30, 10), w, .55)
    place(verb, tok(62 + i * 2), w, .05)
for s in np.arange(.5, 3.0, .25): place(dry, tick(5200, .02, .12), s, 1, .4)
place(dry, keyclick(), T["send"], 1.4)
place(dry, whoosh(.45, 500, 6000, .35, .7), T["send"], 1.0)

# S2 the generic world: glossy pops, a bland 4-on-the-floor, rising tension
for i, b in enumerate(T["build"]): place(dry, pop(380 + 40 * i, 900 + 60 * i), b, .9, (i % 3 - 1) * .4)
for n in T["notes"]: place(dry, tick(2600, .04, .35), n, 1, .5)
for b in np.arange(3.0, 7.0, .5): kick_at(b, .8)
for b in np.arange(3.25, 7.0, .5): place(dry, hat(), b, .7, .2)
place(music, pad([50, 53, 57], 2.0, 2400, .05, .2), 3.0, .4)
place(music, pad([46, 50, 53], 2.0, 2600, .05, .2), 5.0, .45)
for j, tp in enumerate(np.arange(3.0, 7.0, .125)):
    chord = [62, 65, 69, 74] if tp < 5 else [58, 62, 65, 70]
    place(music, pluck(chord[j % 4] + 12) * .7, tp, .35, .5 * np.sin(j))
for r in range(35): place(dry, tick(4500 + 80 * r, .015, .16), T["wall"] + .14 + r * .011, 1, (r % 7 - 3) / 4)
place(dry, riser(2.0, .4), T["wall"], 1.0)

# S3 silence, the dot appears, falls, hits
place(dry, tok(86, .2), T["dotAppear"], .5)
place(dry, fall_whistle(T["impact"] - T["dotFall"] + .02), T["dotFall"], 1.0)
place(dry, whoosh(.6, 200, 2500, .35, .9), T["dotFall"], 1.0)
place(dry, impact(), T["impact"], 1.0)
place(verb, impact(), T["impact"], .55)
for k in range(70):  # paper debris
    tk = T["impact"] + .04 + rng.exponential(.25)
    if tk < T["impact"] + 1.4: place(dry, tick(1500 + rng.random() * 4000, .025, .2 * (1 - (tk - T["impact"]) / 1.4)), tk, 1, rng.uniform(-.9, .9))
place(music, pad([26, 38, 45], 3.0, 400, .5, 1.0), T["impact"], .6)

# S4 the name: hop, four letterpress strikes, the dot presses (motif note 1)
place(dry, whoosh(.45, 400, 3000, .25, .7), T["dotHop"], 1.0)
place(dry, tok(81, .18), T["dotLand"], .5)
for i, s in enumerate(T["stamps"]):
    place(dry, thunk(1.0 + .08 * i), s, .95)
    place(verb, thunk(.6), s, .22)
place(dry, tok(74), T["dotPress"], 1.0); place(verb, tok(74), T["dotPress"], .5)
place(music, bell(74, 2.0), T["dotPress"], .5); place(verb, bell(74, 2.0), T["dotPress"], .4)
place(dry, whoosh(.9, 300, 2000, .14, .5), T["tagline"], 1.0)

# main groove from the dot onward
groove(11.0, 17.0, bright=1.0, lvl=.92)
for i, c in enumerate(T["chips"]): place(dry, pop(700 + 80 * i, 1300 + 90 * i, .08), c, .55, -.6 + .24 * i)
place(dry, whoosh(.7, 300, 3500, .3, .5), T["s5"] - .1, 1.0)

# S6 ink: it asks
place(dry, whoosh(.8, 150, 5000, .45, .55), T["wipe1"] - .45, 1.0); kick_at(T["wipe1"], 1.1)
groove(17.0, 23.0, bright=.65, pluck_on=True, lvl=.85)
cmd = "/dent a landing page for my coffee app"
for i in range(len(cmd)):
    place(dry, keyclick(), T["typeStart"] + i * (T["typeEnd"] - T["typeStart"]) / len(cmd), .55, .3)
place(dry, keyclick(), T["enter"], 1.3); place(dry, thunk(.3, .2), T["enter"], .3)
place(dry, pop(500, 800, .1), T["card"], .6)
for h in T["hover"]: place(dry, tick(3000, .03, .35), h, 1, .3)
place(music, bell(81, 1.4), T["select"], .55); place(music, bell(86, 1.4), T["select"] + .06, .45); place(verb, bell(86), T["select"], .3)
for i, p in enumerate(T["pipe"]):
    place(music, marimba(PENT[i]), p, .6, -.7 + .2 * i); place(verb, marimba(PENT[i]), p, .2)

# S7 paper: it names the cliché, then diverges
place(dry, whoosh(.8, 150, 5000, .45, .55), T["wipe2"] - .45, 1.0); kick_at(T["wipe2"], 1.1)
groove(23.0, 29.0, bright=1.0)
for c in T["cliches"]: place(dry, tick(2400, .03, .25), c, 1, .4)
for s in T["strikes"]: place(dry, zip_(), s, .9, .3)
for k, f in enumerate(T["flaps"]):
    final = k == len(T["flaps"]) - 1
    for c in range(20):
        for r in range(2 if not final else 3):
            place(dry, tick(3800 + rng.random() * 2500, .012, .14), f + c * .009 + r * .03 + rng.random() * .01, 1, (c - 10) / 12)
place(dry, thunk(.5, .3), T["flaps"][-1] + .2, .6)
place(music, stab([62, 65, 69, 72, 76]), T["flaps"][-1] + .2, .7)
place(dry, pop(600, 900, .08), T["stats"], .5)

# S8 ink: it checks its own work
place(dry, whoosh(.8, 150, 5000, .45, .55), T["wipe3"] - .45, 1.0); kick_at(T["wipe3"], 1.1)
groove(29.0, 34.0, bright=.7, half=True, lvl=.85)
for i, w in enumerate(T["widths"]): place(dry, tick(1800 + 260 * i, .05, .5), w, 1, -.3); place(dry, tick(5200, .012, .2), w + .02, 1, .3)
for i, c in enumerate(T["checks"]): place(music, bell(PENT[i + 1] + 12, 1.0), c, .45, .4); place(verb, bell(PENT[i + 1] + 12), c, .25)
place(dry, thunk(1.3, .8), T["passed"], 1.0); place(verb, thunk(1.0), T["passed"], .4)
place(dry, filt(noise(1.2), 4000, "high") * np.exp(-tt(1.2) * 5) * .2, T["passed"], 1.0)

# S9 paper: proof
place(dry, whoosh(.8, 150, 5000, .45, .55), T["wipe4"] - .45, 1.0); kick_at(T["wipe4"], 1.1)
groove(34.0, 37.0, bright=.9)
groove(37.0, 38.0, bright=.9, clap_on=False)
place(dry, thunk(.9, .5) * .6, T["zero"], .7)
for i, c in enumerate(T["count"]): place(music, marimba(PENT[i]), c, .7, -.5 + i * .15); place(dry, tok(PENT[i] - 12, .12), c, .25)
place(music, stab([62, 65, 69, 72, 76], .5), T["countDone"], .75); place(dry, filt(noise(1.0), 5000, "high") * np.exp(-tt(1.0) * 4) * .18, T["countDone"], 1)
place(dry, riser(1.0, .5), T["riser2"], 1.0)
for k in range(16):  # snare roll into the burst
    tr = T["riser2"] + k * (1.0 / 16) * (1 - .0 * k)
    place(dry, snare_hit(), tr, .12 + .03 * k, .1)

# S10 ink: the burst
B = T["burst"]
place(dry, impact(1.6) * .6, B[0], .9)
place(dry, filt(noise(1.5), 4000, "high") * np.exp(-tt(1.5) * 3.5) * .3, B[0], 1)
for b in np.arange(B[0], 41.0, .5): kick_at(b, 1.05, .6)
for b in np.arange(B[0] + .5, 41.0, 1.0): place(dry, clap(), b, .85); place(verb, clap(), b, .25)
for b in np.arange(B[0] + .25, 41.0, .5): place(dry, hat(open_=True), b, .5, .2)
burst_chords = [[50, 57, 62, 65, 69], [46, 53, 58, 62, 65], [41, 53, 57, 60, 64], [43, 55, 58, 62, 67], [45, 57, 61, 64, 69]]
burst_roots = [38, 34, 29, 31, 33]
for i, b in enumerate(B):
    place(music, stab(burst_chords[i], .45, 4200), b, .9)
    place(music, bass(burst_roots[i], .45), b, .7)
place(dry, whoosh(.5, 200, 6000, .4, .4), B[1] - .1, 1.0)               # Motion
place(dry, impact(1.0) * .5, B[2], .8)                                    # 3D
for j, m in enumerate([74, 77, 81, 84, 86, 89]): place(music, pluck(m), B[3] + j * .07, .55, -.5 + j * .2)  # Sound
place(dry, tick(2200, .04, .6), B[4], 1); place(dry, tick(5200, .02, .4), B[4] + .03, 1)  # Video shutter

# S11 paper: breakdown, typing /dent:video
place(dry, whoosh(.9, 150, 4000, .35, .55), T["wipe5"] - .45, 1.0)
place(music, pad([50, 57, 60, 65], 2.5, 900, .4, .5), T["wipe5"], .7)
for b in np.arange(T["wipe5"], T["end"], .5): place(dry, kick(.3, 45, 90, 30, 12), b, .25)
cm = "/dent:video"
for i in range(len(cm)): place(dry, keyclick(), T["typeMeta"][0] + i * (T["typeMeta"][1] - T["typeMeta"][0]) / len(cm), .6)
place(dry, riser(1.0, .25), T["end"] - 1.0, 1.0)

# S12 end card: quick stamps, then the sonic logo: tok, two rising notes, D major resolves
for i, s in enumerate(T["endStamps"]): place(dry, thunk(.7, .35), s, .55, -.3 + .2 * i)
place(dry, tok(74), T["logoTok"], 1.1); place(verb, tok(74), T["logoTok"], .6)
place(dry, kick(.9, 36, 90, 18, 3.5), T["logoTok"], .7)
place(music, bell(81, 2.6), T["logoNotes"][0], .6, -.2); place(verb, bell(81, 2.6), T["logoNotes"][0], .4)
place(music, bell(86, 3.0), T["logoNotes"][1], .6, .2); place(verb, bell(86, 3.0), T["logoNotes"][1], .45)
place(music, pad(DMAJ, 3.0, 2200, .25, 1.0), T["logoTok"], .85)
place(verb, pad(DMAJ, 3.0, 2200, .25, 1.0), T["logoTok"], .3)
place(music, bass(26, 3.2), T["logoTok"], .5)

# ---------------------------------------------------------------- mix
def reverb_ir(rt=1.7, d=2.6):
    t = tt(d); env = np.exp(-6.9 * t / rt)
    ir = np.stack([filt(noise(d), 6000) * env, filt(noise(d), 6000) * env])
    ir[:, : int(.012 * SR)] *= np.linspace(0, 1, int(.012 * SR))
    return ir / np.sqrt((ir ** 2).sum(axis=1, keepdims=True)) * .7

ir = reverb_ir()
wet = np.stack([fftconvolve(verb[c] + .25 * music[c] * duck, ir[c])[: dry.shape[1]] for c in range(2)])
mix = dry + music * duck + wet * .55
mix = filt(mix, 28, "high", 2) if False else np.stack([filt(mix[c], 28, "high") for c in range(2)])
mix = mix[:, :N]
fade = int(.6 * SR); mix[:, -fade:] *= np.linspace(1, 0, fade) ** 2
mix = np.tanh(mix / (np.abs(mix).max() * .9) * 1.2) * .89
raw = OUT / "score_raw.wav"
wavfile.write(raw, SR, (mix.T * 32767).astype(np.int16))

# two-pass loudness normalisation to -14 LUFS integrated, true peak <= -1 dBTP
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(raw), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                   capture_output=True, text=True)
m = json.loads(r.stderr[r.stderr.rfind("{"):r.stderr.rfind("}") + 1])
af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
      f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,aresample=48000")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw), "-af", af, "-ar", "48000", "-c:a", "pcm_s24le", str(OUT / "score.wav")], check=True)
print("measured in:", m["input_i"], "LUFS", m["input_tp"], "dBTP ->", OUT / "score.wav")
