AV1 Rate Control Parameter Exploration (Task 2)
This project explores different AV1 rate control modes using the SvtAv1EncApp encoder. It automates encoding over various parameters, collects system resource metrics, and summarizes the results.

📁 Directory Structure
av1_task2/
├── input.yuv                    # Raw input video
├── task2_av1_experiments.py    # Automation script
├── plot_results.py             # Bonus: Plot generation
├── results/
│   ├── logs/                   # .ivf output + .txt logs
│   ├── encoding_summary.csv    # Summary of all results
│   └── plots/                  # FPS/Memory vs Param plots
├── report/
│   └── Task2_Report.pdf        # Final 1–2 page report
└── README.md                   # This file

⚙️ Requirements

Python 3.10+

psutil, pandas, matplotlib

SvtAv1EncApp (AV1 encoder)

Install dependencies inside a virtual environment:

python3 -m venv .venv
source .venv/bin/activate
pip install psutil pandas matplotlib

▶️ How to Run

1. Make sure input.yuv is in the root directory.

2. Run the encoding experiment:

python task2_av1_experiments.py

This will:

Encode using 3 RC modes

Loop through QP/CQ/bitrate values

Measure FPS, memory, and time

Save logs and a summary CSV

3. Generate plots (optional bonus):

python plot_results.py

📊 Output

All encoding logs: results/logs/*.txt

Encoded videos: results/logs/*.ivf

Summary of results: results/encoding_summary.csv

Plots: results/plots/*.png

Final report: report/Task2_Report.pdf

Author: Chanti Babu Sambangi  Roll No: CS22B2037
