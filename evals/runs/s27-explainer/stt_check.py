"""Speech-to-text pass over every narration line (faster-whisper), word error vs the script, pace, word times."""
import json, re, sys, glob, os
from faster_whisper import WhisperModel
d = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else None
m = WhisperModel("small.en", device="cpu", compute_type="int8")
norm = lambda s: re.sub(r"[^a-z' ]", " ", s.lower().replace("’", "'")).split()
def wer(r, h):
    D = [[i + j if i * j == 0 else 0 for j in range(len(h) + 1)] for i in range(len(r) + 1)]
    for i in range(1, len(r) + 1):
        for j in range(1, len(h) + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (r[i-1] != h[j-1]))
    return D[-1][-1] / max(1, len(r))
rep, tot_e, tot_w = [], 0, 0
for wav in sorted(glob.glob(os.path.join(d, "*.wav"))):
    ref = open(wav[:-4] + ".txt", encoding="utf-8").read().strip()
    segs, info = m.transcribe(wav, language="en", word_timestamps=True, beam_size=5)
    words = [w for s in segs for w in s.words]
    hyp = "".join(w.word for w in words).strip()
    e = wer(norm(ref), norm(hyp)); tot_e += e * len(norm(ref)); tot_w += len(norm(ref))
    span = (words[-1].end - words[0].start) if words else 0
    rep.append({"file": os.path.basename(wav), "ref": ref, "heard": hyp, "wer": round(e, 3),
                "words_per_s": round(len(norm(ref)) / span, 2) if span else None,
                "words": [[w.word.strip(), round(w.start, 3), round(w.end, 3)] for w in words]})
    print(f"{os.path.basename(wav)}  WER {e:5.1%}  {rep[-1]['words_per_s']} w/s\n   ref:   {ref}\n   heard: {hyp}")
print(f"TOTAL WER {tot_e / tot_w:.1%} over {tot_w} words")
if out: json.dump(rep, open(out, "w", encoding="utf-8"), indent=1)
