import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the summary CSV
df = pd.read_csv("results/encoding_summary.csv")

# Create output folder for plots
os.makedirs("results/plots", exist_ok=True)

# Plot Encoding Speed (FPS) vs Parameter Value
plt.figure(figsize=(8, 5))
for mode in df["RC Mode"].unique():
    sub = df[df["RC Mode"] == mode]
    plt.plot(sub["Parameter"], sub["FPS"], marker='o', label=mode)

plt.title("Encoding Speed vs Parameter Value")
plt.xlabel("QP / Bitrate / CQ-Level")
plt.ylabel("Encoding Speed (FPS)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("results/plots/fps_vs_param.png")
plt.close()

# Plot Memory Usage vs Parameter Value
plt.figure(figsize=(8, 5))
for mode in df["RC Mode"].unique():
    sub = df[df["RC Mode"] == mode]
    plt.plot(sub["Parameter"], sub["Peak Memory (MB)"], marker='s', label=mode)

plt.title("Peak Memory Usage vs Parameter Value")
plt.xlabel("QP / Bitrate / CQ-Level")
plt.ylabel("Peak Memory (MB)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("results/plots/memory_vs_param.png")
plt.close()

print("✅ Plots saved in results/plots/")
