
from pathlib import Path

project = Path(__file__).parent
reports = project / "reports"

files = [
    "banking_summary.csv",
    "banking_analysis.xlsx",
    "data_quality_report.csv",
    "data_quality_report.xlsx",
]

charts = [
    "customers_by_city.png",
    "account_type.png",
    "account_balance.png",
    "transaction_type.png",
    "transaction_channel.png",
    "loan_status.png",
    "loan_amount.png",
]

print("\n===== REPORTS VERIFICATION =====")

all_passed = True

for filename in files:
    path = reports / filename

    if path.exists():
        print(f"[PASS] {filename} ({path.stat().st_size:,} bytes)")
    else:
        print(f"[MISSING] {filename}")
        all_passed = False

print("\n===== CHARTS VERIFICATION =====")

for filename in charts:
    path = reports / "charts" / filename

    if path.exists():
        print(f"[PASS] {filename}")
    else:
        print(f"[MISSING] {filename}")
        all_passed = False

print("\n===== FINAL RESULT =====")

if all_passed:
    print("ALL REPORTS AND CHARTS VERIFIED!")
else:
    print("SOME FILES ARE MISSING. PLEASE CHECK.")
