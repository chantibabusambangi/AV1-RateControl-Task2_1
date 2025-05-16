import os
import subprocess
import time
import psutil
import pandas as pd

# Input and output paths
INPUT_FILE = os.path.expanduser("~/input.yuv")  # Adjust if needed
WIDTH, HEIGHT, FPS = 480, 270, 30
FRAMES = 900
RESULTS_DIR = "results/logs"
CSV_FILE = "results/encoding_summary.csv"
os.makedirs(RESULTS_DIR, exist_ok=True)

# RC modes and values
rc_modes = {
    0: {"name": "Constant QP", "param": "--qp", "values": [20, 32, 40]},
    1: {"name": "Constant Bitrate", "param": "--bitrate", "values": [500, 1000, 2000]},
    2: {"name": "Constrained Quality", "param": "--cq-level", "values": [20, 32, 40]},
}

results = []

# Loop over RC modes and parameters
for rc, info in rc_modes.items():
    for value in info["values"]:
        output_file = f"{RESULTS_DIR}/rc{rc}_{value}.ivf"
        log_file = f"{RESULTS_DIR}/rc{rc}_{value}.txt"

        cmd = [
            "SvtAv1EncApp",
            "-i", INPUT_FILE,
            "--input-width", str(WIDTH),
            "--input-height", str(HEIGHT),
            "--fps", str(FPS),
            "--rc", str(rc),
            info["param"], str(value),
            "--frames", str(FRAMES),
            "-b", output_file
        ]

        print(f"\n▶ Running: {' '.join(cmd)}")

        # Measure CPU & Memory usage
        start_time = time.time()
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        pid = process.pid
        ps_proc = psutil.Process(pid)
        peak_memory = 0.0

        while process.poll() is None:
            try:
                mem = ps_proc.memory_info().rss / (1024 * 1024)
                peak_memory = max(peak_memory, mem)
            except psutil.NoSuchProcess:
                break
            time.sleep(0.5)

        end_time = time.time()
        duration = end_time - start_time
        fps = round(FRAMES / duration, 2)

        # Save output log
        stdout, stderr = process.communicate()
        with open(log_file, "w") as f:
            f.write(stdout)
            f.write(stderr)

        # Save result row
        results.append({
            "RC Mode": info["name"],
            "Parameter": value,
            "FPS": fps,
            "Peak Memory (MB)": round(peak_memory, 2),
            "Time (s)": round(duration, 2)
        })

# Save all to CSV
df = pd.DataFrame(results)
df.to_csv(CSV_FILE, index=False)
print(f"\n✅ Summary saved to {CSV_FILE}")
