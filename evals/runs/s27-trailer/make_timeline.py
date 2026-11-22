"""Builds timeline.json for the Streak trailer: one source of timing for picture, narration, captions and score.
Beat grid: 96 bpm (beat = 0.625 s, bar = 2.5 s, 18 bars = 45 s). Narration lines are placed on the grid by hand
(VO_AT) and their lengths come from vo/narration.timing.json (tts.py post)."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
BPM = 96; B = 60 / BPM
b = lambda n: round(n * B, 4)
ev = {"miss": b(5), "reset": b(7), "fall": b(8.5), "land": b(9.5), "name": 7.5,
      "tap1": b(18), "tap2": b(20), "tap3": b(21), "tap4": b(22), "garden": b(24), "lapse": b(25), "roots": 24.95,
      "miss2": b(32), "w2": b(34.5), "w3": b(36), "impact": b(40), "title": b(46), "water": b(55), "widget": b(58),
      "endname": b(66), "logo": b(70)}
VO_AT = [0.45, 2.95, 5.95, 8.6, 10.6, 15.4, 20.4, 25.9, 33.4, 40.9]
timing = json.loads((HERE / "vo/narration.timing.json").read_text(encoding="utf-8"))
vo, cues = [], []
for at, ln in zip(VO_AT, timing):
    dur = ln["end"] - ln["start"]
    vo.append({"at": at, "src_start": ln["start"], "src_end": ln["end"], "text": ln["text"]})
    words = ln["text"].split()
    if len(ln["text"]) <= 42:
        cues.append({"s": round(at, 2), "e": round(at + max(dur, 1.0) + .25, 2), "t": ln["text"]})
    else:  # split at the sentence break nearest the middle, time by character share
        parts = ln["text"].replace(". ", ".|").split("|") if ". " in ln["text"] else [" ".join(words[:len(words)//2]), " ".join(words[len(words)//2:])]
        if len(parts) > 2: parts = [parts[0], " ".join(parts[1:])]
        share = len(parts[0]) / len(ln["text"]); mid = at + dur * share
        cues.append({"s": round(at, 2), "e": round(mid, 2), "t": parts[0]})
        cues.append({"s": round(mid, 2), "e": round(at + dur + .25, 2), "t": parts[1]})
tl = {
 "_doc": "Single source of timing for picture (composition.html), narration placement and score (score_streak.py). 96 bpm grid.",
 "bpm": BPM, "fps": 60, "duration": 45.0,
 "scenes": [0, 4.35, 7.4, 10.0, 15.0, 20.0, 24.95, 32.5, 40.0],
 "events": ev,
 "blur": [[3.1, 3.4], [4.35, 5.0], [5.3, 6.0], [6.4, 7.2], [10.0, 10.9], [24.9, 25.5], [28.7, 29.2], [32.5, 33.4], [40.0, 40.75]],
 "vo": vo, "cues": cues,
}
(HERE / "timeline.json").write_text(json.dumps(tl, indent=1), encoding="utf-8")
def ts(x): h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60; return f"{h:02}:{m:02}:{int(s):02},{int(round((s % 1) * 1000)):03}"
def wrap(x, n=42):  # captions: <= 42 characters per line, 2 lines max, break at the space nearest the middle
    if len(x) <= n: return x
    sp = [i for i, ch in enumerate(x) if ch == " "]; k = min(sp, key=lambda i: abs(i - len(x) / 2))
    return x[:k] + "\n" + x[k + 1:]
(HERE / "film.srt").write_text("".join(f"{i+1}\n{ts(c['s'])} --> {ts(c['e'])}\n{wrap(c['t'])}\n\n" for i, c in enumerate(cues)), encoding="utf-8")
print(json.dumps(ev)); print(*[f"{c['s']:6.2f}-{c['e']:6.2f} {c['t']}" for c in cues], sep="\n")
