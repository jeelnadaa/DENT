#!/usr/bin/env python3
"""DENT narration tool: one interface over many TTS engines, plus mastering and captions.

  python tts.py engines                                   # what is installed, what this machine can run
  python tts.py install qwen3                             # print the install commands (add --yes to run them)
  python tts.py say --engine qwen3 --script vo.txt --out vo/ --voice Ryan --instruct "warm, unhurried"
  python tts.py post --in vo/ --out narration.wav --lufs -16 --gap 0.35 --srt narration.srt --vtt narration.vtt [--tempo 0.85]
  python tts.py compare --engines qwen3,chatterbox,kokoro --text "Meet Quill." --out ab/   # blind A/B set

Engines
  local : qwen3 (Qwen3-TTS, Apache-2.0) · kitten2 (Kitten TTS 2, Stellon Community Licence) · chatterbox (MIT)
          · kokoro (Apache-2.0) · piper (GPL engine, per-voice licences) · system (OS voices: SAPI / say / espeak-ng)
  cloud : openai (OPENAI_API_KEY) · elevenlabs (ELEVENLABS_API_KEY) · http (any OpenAI-compatible /v1/audio/speech
          endpoint: --base-url + --key-env; covers self-hosted servers such as vLLM serving Voxtral, and gateways)
  other : any provider not listed: write a small adapter that saves one WAV per line as line_001.wav... into a folder,
          then run `post` on that folder (references/audio/voice-and-narration.md §5.6).

Each local engine lives in its own virtual environment (their PyTorch/Transformers pins conflict) under
$DENT_TTS_HOME, else the folder registered with `tts.py home <folder>` (~/.dent/tts-home.txt), else ~/.dent/tts.
`say` re-runs itself inside that environment automatically.
Script file: one line of narration per line (blank lines and lines starting with # are ignored). Inline pauses
`[pause 0.6]` split a line into parts with silence between them.

Nothing here spends money or installs software without an explicit flag (`--yes`), and API keys are only read
from environment variables. Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import argparse
import json
import os
import platform
import random
import re
import shutil
import subprocess
import sys
import urllib.request
import wave
from pathlib import Path

POINTER = Path(os.environ.get("DENT_TTS_POINTER", Path.home() / ".dent" / "tts-home.txt"))  # remembers a custom engine folder across sessions


def _home() -> Path:
    """$DENT_TTS_HOME, else the folder registered in ~/.dent/tts-home.txt, else ~/.dent/tts."""
    if os.environ.get("DENT_TTS_HOME"):
        return Path(os.environ["DENT_TTS_HOME"])
    try:
        reg = POINTER.read_text(encoding="utf-8").strip()
        if reg and Path(reg).is_dir():
            return Path(reg)
    except OSError:
        pass
    return Path.home() / ".dent" / "tts"


HOME = _home()
TORCH = "torch torchaudio --index-url https://download.pytorch.org/whl/cu124"

ENGINES = {
    "qwen3": {"pip": "qwen-tts soundfile", "torch": True, "module": "qwen_tts", "licence": "Apache-2.0 (code and weights)",
              "commercial": "yes", "size": "~3 GB torch + ~4.5 GB weights (1.7B) / ~1.5 GB (0.6B)", "hw": "NVIDIA GPU with 6-8 GB+ (1.7B) or 4 GB (0.6B); CPU is very slow",
              "note": "rank 1 in DENT's measured + blind test (cleanest signal, on-target pace); voice design from text; 9 presets; 3 s cloning"},
    "kitten2": {"pip": "kittenml soundfile", "torch": True, "module": "kittenml", "licence": "Stellon Labs Community Licence (code Apache-2.0)",
                "commercial": "only under USD 1M revenue AND 1M funding, after registering, with 'Powered by Stellon Labs' credit",
                "size": "~3 GB torch + ~0.5-1 GB weights", "hw": "CPU with ~6 GB RAM, or an 8 GB GPU",
                "note": "rank 4 in DENT's test (audible artefacts); runs on CPU, 20 languages, good with numbers; read the licence before commercial use"},
    "chatterbox": {"pip": "chatterbox-tts soundfile", "torch": True, "module": "chatterbox", "licence": "MIT",
                   "commercial": "yes (output carries a Perth watermark)", "size": "~3 GB torch + ~2 GB weights", "hw": "NVIDIA GPU recommended",
                   "note": "rank 2 in DENT's test (most expressive) but fast: master with post --tempo 0.85; zero-shot cloning; English-first"},
    "kokoro": {"pip": "kokoro>=0.9 soundfile", "torch": True, "module": "kokoro", "licence": "Apache-2.0",
               "commercial": "yes", "size": "~3 GB torch + ~330 MB weights", "hw": "CPU is fine",
               "note": "rank 3 in DENT's test: clean but flat; the best CPU-only choice"},
    "piper": {"pip": "piper-tts", "torch": False, "module": "piper", "licence": "GPL-3.0 engine; each voice has its own licence",
              "commercial": "output yes; check the voice's licence", "size": "~60 MB per voice", "hw": "any CPU",
              "note": "fast offline fallback; sounds synthetic next to the engines above"},
    "system": {"pip": "", "torch": False, "module": None, "licence": "OS voices", "commercial": "check the OS vendor's terms",
               "size": "none", "hw": "any", "note": "last resort for drafts and timing; never for a produced video"},
    "openai": {"cloud": True, "key": "OPENAI_API_KEY", "licence": "provider terms", "commercial": "per plan; disclose AI voice",
               "note": "paid API; steerable delivery via instructions"},
    "elevenlabs": {"cloud": True, "key": "ELEVENLABS_API_KEY", "licence": "provider terms", "commercial": "paid plans",
                   "note": "free plan is non-commercial with attribution"},
    "http": {"cloud": True, "key": "(--key-env)", "licence": "depends on the server/provider", "commercial": "check",
             "note": "any OpenAI-compatible /v1/audio/speech endpoint, e.g. a vLLM server running Voxtral"},
}


# ---------------------------------------------------------------- helpers

def out(msg: str) -> None:
    print(msg, flush=True)


def gpu() -> str:
    try:
        r = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"], capture_output=True, text=True, timeout=10)
        return r.stdout.strip() or "none detected"
    except Exception:  # noqa: BLE001
        return "none detected (no nvidia-smi)" if platform.system() != "Darwin" else "Apple silicon / Metal (check per engine)"


def venv_python(engine: str) -> Path:
    d = HOME / engine
    return d / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def has_module(python: str | Path, module: str) -> bool:
    try:
        r = subprocess.run([str(python), "-c", f"import importlib.util,sys;sys.exit(0 if importlib.util.find_spec('{module}') else 1)"],
                           capture_output=True, timeout=60)
        return r.returncode == 0
    except Exception:  # noqa: BLE001
        return False


def engine_python(engine: str) -> str | None:
    meta = ENGINES[engine]
    if meta.get("cloud") or engine == "system":
        return sys.executable
    if engine == "piper" and shutil.which("piper"):
        return sys.executable
    if has_module(sys.executable, meta["module"]):
        return sys.executable
    vp = venv_python(engine)
    if vp.is_file() and has_module(vp, meta["module"]):
        return str(vp)
    return None


def read_script(path: str | None, text: str | None) -> list[str]:
    raw = Path(path).read_text(encoding="utf-8") if path else (text or "")
    return [ln.strip() for ln in raw.splitlines() if ln.strip() and not ln.strip().startswith("#")]


def split_pauses(line: str) -> list[tuple[str, float]]:
    """'Hello. [pause 0.5] World.' -> [('Hello.', 0.5), ('World.', 0.0)]"""
    parts, rest = [], line
    for m in re.finditer(r"(.*?)\[pause\s+([\d.]+)s?\]", line):
        parts.append((m.group(1).strip(), float(m.group(2))))
        rest = line[m.end():]
    parts.append((rest.strip(), 0.0))
    return [(t, p) for t, p in parts if t or p]


def write_wav(path: Path, audio, sr: int) -> None:
    import numpy as np  # available in every engine venv
    a = np.asarray(audio, dtype="float32").reshape(-1)
    a = np.clip(a, -1, 1)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((a * 32767).astype("<i2").tobytes())


def wav_duration(path: Path) -> float:
    with wave.open(str(path), "rb") as w:
        return w.getnframes() / float(w.getframerate())


# ---------------------------------------------------------------- engines (run inside the engine's environment)

def render_local(engine: str, lines: list[str], outdir: Path, a: argparse.Namespace) -> list[Path]:
    import numpy as np
    outdir.mkdir(parents=True, exist_ok=True)
    random.seed(a.seed)
    try:
        import torch
        torch.manual_seed(a.seed)
        dev = "cuda" if torch.cuda.is_available() else ("mps" if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available() else "cpu")
    except Exception:  # noqa: BLE001
        dev = "cpu"
    synth = None
    if engine == "qwen3":
        import torch
        from qwen_tts import Qwen3TTSModel
        size = a.model or "1.7B"
        mode = "Base" if a.ref else ("VoiceDesign" if (a.design and not a.voice) else "CustomVoice")
        repo = size if "/" in size else f"Qwen/Qwen3-TTS-12Hz-{size}-{mode}"
        out(f"loading {repo} on {dev}")
        m = Qwen3TTSModel.from_pretrained(repo, device_map=dev if dev != "mps" else "cpu",
                                          dtype=torch.bfloat16 if dev == "cuda" else torch.float32)
        lang = a.lang or "Auto"
        if mode == "CustomVoice":
            speakers = m.get_supported_speakers() or []
            voice = a.voice or ("ryan" if "ryan" in speakers else (speakers[0] if speakers else None))
            out(f"voice {voice} (available: {', '.join(speakers)})")

            def synth(t):
                w, sr = m.generate_custom_voice(text=t, speaker=voice, language=lang, instruct=a.instruct or None)
                return w[0], sr
        elif mode == "VoiceDesign":
            def synth(t):
                w, sr = m.generate_voice_design(text=t, instruct=a.design, language=lang)
                return w[0], sr
        else:
            def synth(t):
                w, sr = m.generate_voice_clone(text=t, language=lang, ref_audio=a.ref, ref_text=a.ref_text,
                                               x_vector_only_mode=not a.ref_text)
                return w[0], sr
    elif engine == "kitten2":
        from kittenml import KittenTTS
        m = KittenTTS(a.model or "KittenML/kitten-tts-2")
        voices = list(getattr(m, "available_voices", []) or [])
        narrator = [v for v in ("AudiobookNarratorFemale", "FrenchDocumentary", "NewsAnchorFemale") if v in voices]
        voice = a.voice or (narrator[0] if narrator else (voices[0] if voices else None))
        out(f"voice {voice} ({len(voices)} available: {', '.join(voices)})")

        def synth(t):
            kw = {"reference": a.ref} if a.ref else {"voice": voice}
            return m.generate(t, **kw), m.sample_rate
    elif engine == "chatterbox":
        from chatterbox.tts import ChatterboxTTS
        m = ChatterboxTTS.from_pretrained(device=dev)

        def synth(t):
            w = m.generate(t, audio_prompt_path=a.ref, exaggeration=a.exaggeration, cfg_weight=a.cfg)
            return w.squeeze(0).cpu().numpy(), m.sr
    elif engine == "kokoro":
        from kokoro import KPipeline
        voice = a.voice or "af_heart"
        pipe = KPipeline(lang_code=a.lang or voice[0])

        def synth(t):
            chunks = [np.asarray(audio) for _, _, audio in pipe(t, voice=voice, speed=a.speed)]
            return np.concatenate(chunks) if chunks else np.zeros(1), 24000
    elif engine == "piper":
        if not a.voice:
            sys.exit("piper needs --voice <path to .onnx voice model>")

        def synth(t):
            tmp = outdir / "_piper.wav"
            subprocess.run(["piper", "-m", a.voice, "-f", str(tmp)], input=t, text=True, check=True, capture_output=True)
            with wave.open(str(tmp), "rb") as w:
                sr = w.getframerate()
                data = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype("float32") / 32767
            tmp.unlink()
            return data, sr
    elif engine == "system":
        def synth(t):
            tmp = outdir / "_sys.wav"
            if os.name == "nt":
                ps = ("Add-Type -AssemblyName System.Speech; $s=New-Object System.Speech.Synthesis.SpeechSynthesizer;"
                      f"$s.SetOutputToWaveFile('{tmp}'); $s.Speak([Console]::In.ReadToEnd()); $s.Dispose()")
                subprocess.run(["powershell", "-NoProfile", "-Command", ps], input=t, text=True, check=True, capture_output=True)
            elif platform.system() == "Darwin":
                subprocess.run(["say", "-o", str(tmp), "--data-format=LEI16@22050", t], check=True)
            else:
                subprocess.run(["espeak-ng", "-w", str(tmp), t], check=True)
            with wave.open(str(tmp), "rb") as w:
                sr, ch = w.getframerate(), w.getnchannels()
                data = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype("float32") / 32767
            tmp.unlink()
            return (data.reshape(-1, ch).mean(axis=1) if ch > 1 else data), sr
    return render_lines(synth, lines, outdir)


def render_lines(synth, lines: list[str], outdir: Path) -> list[Path]:
    import numpy as np
    paths = []
    for i, line in enumerate(lines, 1):
        pieces, sr = [], 24000
        for text, pause in split_pauses(line):
            if text:
                audio, sr = synth(text)
                pieces.append(np.asarray(audio, dtype="float32").reshape(-1))
            if pause:
                pieces.append(np.zeros(int(sr * pause), dtype="float32"))
        p = outdir / f"line_{i:03d}.wav"
        write_wav(p, np.concatenate(pieces) if pieces else np.zeros(1), sr)
        (outdir / f"line_{i:03d}.txt").write_text(re.sub(r"\[pause[^\]]*\]", " ", line).strip(), encoding="utf-8")
        out(f"  {p.name}  {wav_duration(p):.2f}s  {line[:60]}")
        paths.append(p)
    return paths


def render_cloud(engine: str, lines: list[str], outdir: Path, a: argparse.Namespace) -> list[Path]:
    outdir.mkdir(parents=True, exist_ok=True)
    key_env = {"openai": "OPENAI_API_KEY", "elevenlabs": "ELEVENLABS_API_KEY"}.get(engine, a.key_env)
    key = os.environ.get(key_env or "")
    if not key:
        sys.exit(f"{engine}: set the API key in the environment variable {key_env} yourself (never paste it into chat).")
    paths = []
    for i, line in enumerate(lines, 1):
        text = re.sub(r"\[pause[^\]]*\]", " … ", line)
        if engine == "elevenlabs":
            voice = a.voice or "JBFqnCBsd6RMkjVDRZzb"
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=pcm_24000"
            body = {"text": text, "model_id": a.model or "eleven_multilingual_v2"}
            headers = {"xi-api-key": key, "Content-Type": "application/json"}
        else:
            base = "https://api.openai.com/v1" if engine == "openai" else a.base_url.rstrip("/")
            url = f"{base}/audio/speech"
            body = {"model": a.model or "gpt-4o-mini-tts", "voice": a.voice or "alloy", "input": text, "response_format": "pcm"}
            if a.instruct:
                body["instructions"] = a.instruct
            headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
        req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=120) as r:
            pcm = r.read()
        p = outdir / f"line_{i:03d}.wav"
        with wave.open(str(p), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(24000)
            w.writeframes(pcm)
        (outdir / f"line_{i:03d}.txt").write_text(re.sub(r"\[pause[^\]]*\]", " ", line).strip(), encoding="utf-8")
        out(f"  {p.name}  {wav_duration(p):.2f}s  {line[:60]}")
        paths.append(p)
    return paths


# ---------------------------------------------------------------- commands

def cmd_home(a) -> int:
    folder = Path(a.folder).expanduser().resolve()
    if not folder.is_dir():
        out(f"{folder} is not a folder")
        return 1
    POINTER.parent.mkdir(parents=True, exist_ok=True)
    POINTER.write_text(str(folder), encoding="utf-8")
    found = [e for e in ENGINES if not ENGINES[e].get("cloud") and e != "system" and (folder / e).is_dir()]
    out(f"registered {folder} in {POINTER}; engine folders found: {', '.join(found) or 'none yet'}")
    return 0


def cmd_engines(_a) -> int:
    out(f"machine: {platform.system()} {platform.machine()}, GPU: {gpu()}, ffmpeg: {'yes' if shutil.which('ffmpeg') else 'NO (needed for post)'}")
    src = "DENT_TTS_HOME" if os.environ.get("DENT_TTS_HOME") else ("registered in ~/.dent/tts-home.txt" if POINTER.is_file() else "default")
    out(f"engine environments: {HOME}  ({src}; `tts.py home <folder>` registers another)")
    for name, m in ENGINES.items():
        if m.get("cloud"):
            state = "key set" if os.environ.get(m["key"], "") else f"needs {m['key']}"
            out(f"- {name:<10} cloud   {state:<24} licence: {m['licence']}; commercial: {m['commercial']}. {m['note']}")
            continue
        py = engine_python(name)
        state = f"installed ({'this python' if py == sys.executable else 'venv'})" if py else "not installed"
        out(f"- {name:<10} local   {state:<24} licence: {m['licence']}; commercial: {m['commercial']}; "
            f"needs: {m['hw']}; download: {m['size']}. {m['note']}")
    return 0


def install_commands(engine: str) -> list[list[str]]:
    m = ENGINES[engine]
    vp = venv_python(engine)
    cmds = [[sys.executable, "-m", "venv", str(HOME / engine)], [str(vp), "-m", "pip", "install", "--upgrade", "pip"]]
    if m.get("torch"):
        torch = TORCH if (os.name == "nt" or platform.system() == "Linux") and "none" not in gpu() else "torch torchaudio"
        cmds.append([str(vp), "-m", "pip", "install", *torch.split()])
    cmds.append([str(vp), "-m", "pip", "install", *m["pip"].split()])
    return cmds


def cmd_install(a) -> int:
    m = ENGINES[a.engine]
    if m.get("cloud") or a.engine == "system":
        out(f"{a.engine}: nothing to install. Cloud engines need an account and an API key in the environment, which the user sets up.")
        return 0
    out(f"{a.engine}: licence {m['licence']}; commercial use: {m['commercial']}")
    out(f"download: {m['size']}; needs: {m['hw']}; into {HOME / a.engine}")
    cmds = install_commands(a.engine)
    for c in cmds:
        out("  " + " ".join(f'"{x}"' if " " in x else x for x in c))
    if not a.yes:
        out("Not installed. Ask the user first; re-run with --yes after they agree.")
        return 2
    HOME.mkdir(parents=True, exist_ok=True)
    if HOME != Path.home() / ".dent" / "tts":   # remember a custom location for later sessions
        POINTER.parent.mkdir(parents=True, exist_ok=True)
        POINTER.write_text(str(HOME), encoding="utf-8")
    for c in cmds:
        r = subprocess.run(c)
        if r.returncode:
            out(f"FAILED: {' '.join(c)}")
            return r.returncode
    ok = has_module(venv_python(a.engine), m["module"])
    out("installed and importable" if ok else "installed, but the module does not import: check the output above")
    return 0 if ok else 1


def cmd_say(a) -> int:
    lines = read_script(a.script, a.text)
    if not lines:
        sys.exit("nothing to say: give --script or --text")
    outdir = Path(a.out)
    meta = ENGINES[a.engine]
    if meta.get("cloud"):
        render_cloud(a.engine, lines, outdir, a)
        return 0
    py = engine_python(a.engine)
    if not py:
        out(f"{a.engine} is not installed. Run: python tts.py install {a.engine}   (ask the user first; it downloads {meta['size']})")
        return 2
    if py != sys.executable and not a._inner:
        argv = [py, str(Path(__file__).resolve()), *sys.argv[1:], "--_inner"]
        return subprocess.run(argv).returncode
    render_local(a.engine, lines, outdir, a)
    (outdir / "engine.json").write_text(json.dumps({"engine": a.engine, "model": a.model, "voice": a.voice, "instruct": a.instruct,
                                                    "design": a.design, "seed": a.seed, "licence": meta["licence"]}, indent=2), encoding="utf-8")
    return 0


def ffmpeg(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-y", *args], capture_output=True, text=True)


def measure(path: Path, lufs: float = -16.0, tp: float = -1.5) -> dict:
    r = ffmpeg("-i", str(path), "-af", f"loudnorm=I={lufs}:TP={tp}:LRA=11:print_format=json", "-f", "null", "-")
    js = r.stderr[r.stderr.rfind("{"): r.stderr.rfind("}") + 1]
    return json.loads(js)


def fmt_ts(t: float, sep: str) -> str:
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d}{sep}{int(round((s % 1) * 1000)) % 1000:03d}"


def caption_cues(text: str, start: float, end: float, max_chars: int = 42) -> list[tuple[float, float, str]]:
    """Split one line into cues of <= 2 lines x max_chars, timed by character share."""
    words = text.split()
    n = max(1, -(-len(text) // (max_chars * 2)))  # cues needed
    target = len(text) / n
    chunks, cur = [], ""
    for w in words:  # balanced cues: no 1-word orphan cue at the end
        if cur and len(cur) + 1 + len(w) > target and len(chunks) < n - 1:
            chunks.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        chunks.append(cur)
    total = sum(len(c) for c in chunks) or 1
    cues, t = [], start
    for c in chunks:
        d = (end - start) * len(c) / total
        if len(c) <= max_chars:
            lines = [c]
        else:  # two balanced lines, broken at the space nearest the middle
            spaces = [i for i, ch in enumerate(c) if ch == " "]
            cut = min(spaces, key=lambda i: abs(i - len(c) / 2)) if spaces else len(c) // 2
            lines = [c[:cut].strip(), c[cut:].strip()]
        cues.append((t, t + d, "\n".join(lines[:2])))
        t += d
    return cues


def cmd_post(a) -> int:
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg is required for post (https://ffmpeg.org)")
    if not 0.5 <= a.tempo <= 2.0:
        sys.exit("--tempo must be between 0.5 and 2.0")
    src = Path(a.inp)
    wavs = sorted(src.glob("line_*.wav"))
    if not wavs:
        sys.exit(f"no line_*.wav files in {src}")
    work = Path(a.out).with_suffix("")
    work.parent.mkdir(parents=True, exist_ok=True)
    tmp = work.parent / f"_{work.name}_concat.txt"
    sil = work.parent / f"_{work.name}_gap.wav"
    ffmpeg("-f", "lavfi", "-i", f"anullsrc=r=48000:cl=mono", "-t", str(a.gap), str(sil))
    cues, t, entries = [], a.lead, []
    lead = work.parent / f"_{work.name}_lead.wav"
    ffmpeg("-f", "lavfi", "-i", f"anullsrc=r=48000:cl=mono", "-t", str(max(a.lead, 0.01)), str(lead))
    entries.append(lead)
    timing = []
    for i, w in enumerate(wavs):
        norm = work.parent / f"_{work.name}_{w.stem}.wav"
        # trim leading/trailing silence, resample to 48 kHz mono
        tempo = f",atempo={a.tempo:.3f}" if abs(a.tempo - 1.0) > 1e-3 else ""
        ffmpeg("-i", str(w), "-af", "silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse" + tempo,
               "-ar", "48000", "-ac", "1", str(norm))
        d = wav_duration(norm)
        txt_file = w.with_suffix(".txt")
        text = txt_file.read_text(encoding="utf-8").strip() if txt_file.is_file() else ""
        timing.append({"line": i + 1, "start": round(t, 3), "end": round(t + d, 3), "text": text})
        cues += caption_cues(text, t, t + d) if text else []
        entries.append(norm)
        t += d
        if i < len(wavs) - 1:
            entries.append(sil)
            t += a.gap
    tmp.write_text("".join(f"file '{p.resolve().as_posix()}'\n" for p in entries), encoding="utf-8")
    raw = work.parent / f"_{work.name}_raw.wav"
    ffmpeg("-f", "concat", "-safe", "0", "-i", str(tmp), "-c", "pcm_s16le", str(raw))
    m = measure(raw, a.lufs, a.tp)
    final, mode = None, ""
    hit = lambda f: abs(float(f["input_i"]) - a.lufs) <= 0.5 and float(f["input_tp"]) <= a.tp + 0.2  # noqa: E731
    # 1) Linear gain keeps the voice's dynamics intact.
    chain = (f"highpass=f=70,loudnorm=I={a.lufs}:TP={a.tp}:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
             f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    r = ffmpeg("-i", str(raw), "-af", chain, "-ar", "48000", str(a.out))
    if r.returncode:
        sys.exit(r.stderr[-2000:])
    final, mode = measure(Path(a.out), a.lufs, a.tp), "linear"
    if not hit(final):
        # 2) When the true-peak ceiling blocks the gain (common at -14 LUFS), add gain and catch the peaks with a
        #    limiter (4x oversampled, so inter-sample peaks are caught too), correcting the gain until it lands.
        gain = a.lufs - float(m["input_i"])
        ceiling = 10 ** ((a.tp - 0.3) / 20)
        for _ in range(4):
            chain = (f"highpass=f=70,volume={gain:.2f}dB,aresample=192000,"
                     f"alimiter=limit={ceiling:.4f}:attack=3:release=60:level=false,aresample=48000")
            r = ffmpeg("-i", str(raw), "-af", chain, "-ar", "48000", str(a.out))
            if r.returncode:
                sys.exit(r.stderr[-2000:])
            final, mode = measure(Path(a.out), a.lufs, a.tp), "gain + true-peak limiter"
            if hit(final):
                break
            gain += a.lufs - float(final["input_i"])
    for p in [tmp, sil, lead, raw, *work.parent.glob(f"_{work.name}_line_*.wav")]:
        p.unlink(missing_ok=True)
    if a.srt:
        Path(a.srt).write_text("".join(f"{n}\n{fmt_ts(s, ',')} --> {fmt_ts(e, ',')}\n{c}\n\n" for n, (s, e, c) in enumerate(cues, 1)), encoding="utf-8")
    if a.vtt:
        Path(a.vtt).write_text("WEBVTT\n\n" + "".join(f"{fmt_ts(s, '.')} --> {fmt_ts(e, '.')}\n{c}\n\n" for s, e, c in cues), encoding="utf-8")
    Path(a.out).with_suffix(".timing.json").write_text(json.dumps(timing, indent=2), encoding="utf-8")
    li, tp = float(final["input_i"]), float(final["input_tp"])
    ok = abs(li - a.lufs) <= 1.0 and tp <= a.tp + 0.2
    out(f"{a.out}: {wav_duration(Path(a.out)):.2f}s, {li:.1f} LUFS integrated (target {a.lufs}), true peak {tp:.1f} dBTP "
        f"(limit {a.tp}), {mode} normalisation -> {'PASS' if ok else 'FAIL'}; {len(cues)} caption cues; timing in {Path(a.out).with_suffix('.timing.json').name}")
    return 0 if ok else 1


def cmd_compare(a) -> int:
    """Render the same text with several engines into anonymised files for a blind listen."""
    outdir = Path(a.out)
    outdir.mkdir(parents=True, exist_ok=True)
    engines = [e.strip() for e in a.engines.split(",") if e.strip()]
    letters = list("ABCDEFGH")[: len(engines)]
    random.seed(a.seed)
    random.shuffle(letters)
    key = {}
    for eng, letter in zip(engines, letters):
        d = outdir / f"_{eng}"
        argv = [sys.executable, str(Path(__file__).resolve()), "say", "--engine", eng, "--text", a.text, "--out", str(d), "--seed", str(a.seed)]
        if eng == "qwen3" and a.instruct:
            argv += ["--instruct", a.instruct]
        r = subprocess.run(argv)
        src = d / "line_001.wav"
        if r.returncode or not src.is_file():
            out(f"{eng}: failed or not installed (skipped)")
            continue
        shutil.copy(src, outdir / f"sample_{letter}.wav")
        key[letter] = eng
    (outdir / "KEY.json").write_text(json.dumps(key, indent=2), encoding="utf-8")
    out(f"blind set in {outdir}: {', '.join(f'sample_{k}.wav' for k in sorted(key))}; answers in KEY.json (open after listening)")
    return 0


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("engines")
    hm = sub.add_parser("home", help="register the folder that holds the engine environments (remembered for every session)")
    hm.add_argument("folder")
    i = sub.add_parser("install")
    i.add_argument("engine", choices=sorted(ENGINES))
    i.add_argument("--yes", action="store_true", help="actually install (only after the user agreed)")
    s = sub.add_parser("say")
    s.add_argument("--engine", choices=sorted(ENGINES), required=True)
    s.add_argument("--script")
    s.add_argument("--text")
    s.add_argument("--out", required=True)
    s.add_argument("--voice", help="preset/speaker name, ElevenLabs voice id, or piper .onnx path")
    s.add_argument("--instruct", help="delivery instruction (qwen3 CustomVoice, openai)")
    s.add_argument("--design", help="qwen3 VoiceDesign: describe the voice in words")
    s.add_argument("--ref", help="reference audio for cloning (consent required)")
    s.add_argument("--ref-text", help="transcript of the reference audio (better qwen3 clones)")
    s.add_argument("--model", help="model size/id (qwen3: 1.7B or 0.6B; cloud model name)")
    s.add_argument("--lang", help="language (qwen3: English, Chinese, ... or Auto; kokoro: lang code)")
    s.add_argument("--speed", type=float, default=1.0)
    s.add_argument("--exaggeration", type=float, default=0.5, help="chatterbox emotion 0.25-2")
    s.add_argument("--cfg", type=float, default=0.5, help="chatterbox pacing/cfg weight")
    s.add_argument("--seed", type=int, default=7)
    s.add_argument("--base-url", default="", help="http engine: base URL ending in /v1")
    s.add_argument("--key-env", default="", help="http engine: name of the env var holding the key")
    s.add_argument("--_inner", action="store_true", help=argparse.SUPPRESS)
    p = sub.add_parser("post")
    p.add_argument("--in", dest="inp", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--lufs", type=float, default=-16.0, help="-16 web/podcast, -14 social video, -23 broadcast")
    p.add_argument("--tp", type=float, default=-1.5, help="true-peak ceiling dBTP")
    p.add_argument("--gap", type=float, default=0.35, help="seconds between lines")
    p.add_argument("--lead", type=float, default=0.25, help="silence before the first line")
    p.add_argument("--tempo", type=float, default=1.0, help="pitch-preserving speed change, 0.5-2.0 (e.g. 0.85 to calm a fast engine)")
    p.add_argument("--srt")
    p.add_argument("--vtt")
    c = sub.add_parser("compare")
    c.add_argument("--engines", required=True)
    c.add_argument("--text", required=True)
    c.add_argument("--instruct")
    c.add_argument("--out", required=True)
    c.add_argument("--seed", type=int, default=7)
    a = ap.parse_args()
    return {"engines": cmd_engines, "install": cmd_install, "say": cmd_say, "post": cmd_post, "compare": cmd_compare, "home": cmd_home}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
