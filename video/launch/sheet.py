"""Contact sheet of review stills: python sheet.py out/sheet.png a.png b.png ... (3 columns)."""
import subprocess, sys
out, files = sys.argv[1], sys.argv[2:]
cols = 3; rows = (len(files) + cols - 1) // cols
inputs = sum((["-i", f] for f in files), [])
n = len(files)
pads = n
filt = "".join(f"[{i}:v]scale=640:360[v{i}];" for i in range(n))
while pads < rows * cols:
    filt += f"color=c=black:s=640x360:d=1[v{pads}];"; pads += 1
layout = "|".join(f"{(i % cols) * 640}_{(i // cols) * 360}" for i in range(rows * cols))
filt += "".join(f"[v{i}]" for i in range(rows * cols)) + f"xstack=inputs={rows*cols}:layout={layout}[o]"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", filt, "-map", "[o]", "-frames:v", "1", out], check=True)
print(out)
