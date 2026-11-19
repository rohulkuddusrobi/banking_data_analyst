
import subprocess
import sys
import time

print("BANKING AUTOMATION STARTED!", flush=True)

scripts = [
    "business_insights.py",
    "export_reports.py",
    "save_charts.py",
    "automated_quality_report.py"
]

for script in scripts:

    print(f"\nStarting: {script}", flush=True)

    result = subprocess.run(
        [sys.executable, "-u", script],
        capture_output=True,
        text=True
    )

    print("OUTPUT:", flush=True)
    print(result.stdout, flush=True)

    if result.stderr:
        print("ERROR / WARNING:", flush=True)
        print(result.stderr, flush=True)

    if result.returncode == 0:
        print(f"SUCCESS: {script}", flush=True)
    else:
        print(f"FAILED: {script}", flush=True)
        break

print("\nAUTOMATION FINISHED!", flush=True)
