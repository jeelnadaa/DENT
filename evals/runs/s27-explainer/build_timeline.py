#!/usr/bin/env python3
"""Build timeline.json from the narration: scene cuts = line starts, events = every spoken word (aligned from a
faster-whisper pass over the mastered narration), captions = narration.srt, SFX on picture events, the score's map.

  <whisper-python> build_timeline.py           (needs faster_whisper; run with the eval venv's python)
"""
import difflib
import json
import re
from pathlib import Path

from faster_whisper import WhisperModel

HERE = Path(__file__).resolve().parent
VO = HERE / "vo"
norm = lambda s: re.sub(r"[^a-z0-9' ]", " ", s.lower().replace("’", "'")).split()

timing = json.loads((VO / "narration.timing.json").read_text(encoding="utf-8"))
m = WhisperModel("small.en", device="cpu", compute_type="int8")
segs, _ = m.transcribe(str(VO / "narration.wav"), language="en", word_timestamps=True, beam_size=5)
heard = [(w.word.strip(), w.start, w.end) for s in segs for w in s.words]
htok = [norm(w)[0] if norm(w) else "" for w, _, _ in heard]

# script tokens with their line number
stok, sline = [], []
for ln in timing:
    for w in norm(re.sub(r"\[pause[^\]]*\]", " ", ln["text"])):
        stok.append(w); sline.append(ln["line"])
sm = difflib.SequenceMatcher(a=stok, b=htok, autojunk=False)
times = [None] * len(stok)
for a, b, n in sm.get_matching_blocks():
    for i in range(n):
        times[a + i] = heard[b + i][1]
# unmatched script words: interpolate inside their line
missing = [stok[i] for i, t in enumerate(times) if t is None]
for i, t in enumerate(times):
    if t is None:
        prev = next((times[j] for j in range(i - 1, -1, -1) if times[j] is not None), timing[0]["start"])
        nxt = next((times[j] for j in range(i + 1, len(times)) if times[j] is not None), prev + .4)
        times[i] = prev + (nxt - prev) * .5

events, seen = {}, {}
for w, ln, t in zip(stok, sline, times):
    key = f"L{ln}.{w}"
    seen[key] = seen.get(key, 0) + 1
    events[key if seen[key] == 1 else f"{key}#{seen[key]}"] = round(t, 3)

starts = [ln["start"] for ln in timing]
scenes = [0.0] + [round(s - .25, 3) for s in starts[1:]]
end = timing[-1]["end"]
duration = round(end + 3.6, 2)
events["cut8"] = round(events["L8.a"] - .62, 3)            # hard cut into the lookalike, inside the inserted silence
events["act1"], events["act2"], events["act3"], events["act4"] = 0.0, scenes[2], scenes[7], scenes[8]
events["act2b"], events["act2c"], events["act2d"] = scenes[4], scenes[5], scenes[6]

# captions from the narration's SRT
def srt_time(s):
    h, mi, rest = s.split(":"); se, ms = rest.split(",")
    return int(h) * 3600 + int(mi) * 60 + int(se) + int(ms) / 1000
cues = []
for block in (VO / "narration.srt").read_text(encoding="utf-8").strip().split("\n\n"):
    lines = block.strip().splitlines()
    a, b = lines[1].split(" --> ")
    cues.append({"s": round(srt_time(a), 3), "e": round(srt_time(b), 3), "t": "
".join(lines[2:])})

E = events
sfx = [{"t": 0.0, "kind": "room"}, {"t": 0.02, "kind": "keys", "dur": .54}, {"t": 0.56, "kind": "keys", "dur": .54}]
sfx += [{"t": round(s - .3, 3), "kind": "slide"} for s in scenes[1:]]                       # every morph transition
sfx += [{"t": E["L1.secret"] + .1, "kind": "pen", "dur": .9}]                                 # pen underlines "secret"
sfx += [{"t": round(E["L1.site"] + i * .16 - .2, 3), "kind": "card"} for i in range(5)]      # five sites
sfx += [{"t": round(E["L1.every#2"] + i * .12, 3), "kind": "tick"} for i in range(5)]
sfx += [{"t": round(E["L2.copies"] - .2 + i * .14, 3), "kind": "tick"} for i in range(5)]
sfx += [{"t": E["L2.fake"] - .1, "kind": "card"}, {"t": E["L2.ask"], "kind": "keys", "dur": .55}]
sfx += [{"t": round(E["L3.passkey"] - .2 + i * .16, 3), "kind": "pen", "dur": .75} for i in range(7)]   # lettering, per letter
sfx += [{"t": E["L3.share"] + .35, "kind": "strike"}]
sfx += [{"t": E["L4.pair"], "kind": "digits", "dur": 1.1}, {"t": E["L4.never"], "kind": "thud"}]
sfx += [{"t": E[k] - .1, "kind": "pen", "dur": .7} for k in ("L4.face", "L4.fingerprint", "L4.or")]
sfx += [{"t": E["L5.keeps"] - .1, "kind": "send"}, {"t": E["L5.check"] + .1, "kind": "chime"},
        {"t": E["L5.forge"] - .5, "kind": "scratchfail", "dur": .9}]
sfx += [{"t": E["L6.fresh"], "kind": "digits", "dur": .7}, {"t": E["L6.sends"] - .1, "kind": "send"},
        {"t": E["L6.signs"], "kind": "pen", "dur": .6}, {"t": E["L6.and"] - .1, "kind": "send"}, {"t": E["L6.checks"], "kind": "chime"}]
sfx += [{"t": round(E["L7.crosses"] + i * .25, 3), "kind": "tick"} for i in range(3)]
sfx += [{"t": E["L7.stolen"] - .1, "kind": "card"}, {"t": E["L7.signs"], "kind": "hollow"}]
sfx += [{"t": E["L8.bound"] - .1, "kind": "pen", "dur": .9}, {"t": E["cut8"], "kind": "cut"}, {"t": E["L8.nothing"], "kind": "hollow"}]
sfx += [{"t": round(scenes[8] + .1 + i * .35, 3), "kind": "pen", "dur": .8} for i in range(3)]
sfx += [{"t": E["L9.syncs"], "kind": "chime"}]
sfx += [{"t": round(E["L10.look"] - .3 + i * .12, 3), "kind": "pen", "dur": .6} for i in range(7)]
sfx += [{"t": E["L10.create"] - .1, "kind": "logo"}]
sfx = sorted(({**s, "t": round(s["t"], 3)} for s in sfx), key=lambda s: s["t"])

tl = {
    "_doc": "Generated by build_timeline.py from vo/narration.* (word times from a faster-whisper pass). Picture events and "
            "SFX land on spoken word times; the score is a bar grid at 80 bpm underneath.",
    "bpm": 80, "fps": 60, "duration": duration, "scenes": scenes, "events": events,
    "blur": [[round(E["L5.keeps"] - .1, 2), round(E["L5.keeps"] + .8, 2)], [round(E["L6.sends"] - .1, 2), round(E["L6.sends"] + 1.0, 2)],
             [round(E["L6.and"] - .1, 2), round(E["L6.and"] + .8, 2)]] + [[round(s - .4, 2), round(s + .4, 2)] for s in scenes[1:]],
    "sfx": sfx,
    "music": {"style": "drafting", "from": 0.0, "to": round(end + 3.2, 2), "key_hz": 174.61, "lift": scenes[2],
              "night": [scenes[7], scenes[8]], "drop": [[round(E["cut8"] - .05, 2), round(E["L8.a"] - .02, 2)]],
              "progression": [[0, 4, 7, 14], [-3, 0, 4, 7], [-7, -3, 0, 4], [-5, -1, 2, 9]]},
    "cues": cues,
}
(HERE / "timeline.json").write_text(json.dumps(tl, indent=1), encoding="utf-8")
print(f"timeline.json: {duration}s, {len(scenes)} scenes, {len(events)} word events, {len(sfx)} sfx, {len(cues)} cues; "
      f"script words not heard by whisper (time interpolated): {missing or 'none'}")
print("scene starts:", scenes)
