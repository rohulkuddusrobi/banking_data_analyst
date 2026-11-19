
from pathlib import Path

project = Path(__file__).parent

checks = {
    ".env": project / ".env",
    ".gitignore": project / ".gitignore",
    "requirements.txt": project / "requirements.txt",
    "README.md": project / "README.md",
    "db_connection.py": project / "db_connection.py",
}

print("\n===== PROJECT SECURITY CHECK =====")

all_passed = True

for name, path in checks.items():
    exists = path.exists()

    print(f"[{'PASS' if exists else 'FAIL'}] {name}")

    if not exists:
        all_passed = False

# Check whether .env is ignored by Git
gitignore = project / ".gitignore"

if gitignore.exists():
    lines = gitignore.read_text(encoding="utf-8").splitlines()
    env_ignored = any(line.strip() == ".env" for line in lines)

    print(
        f"[{'PASS' if env_ignored else 'FAIL'}] .env ignored by Git"
    )

    if not env_ignored:
        all_passed = False

print("\n===== FINAL SECURITY RESULT =====")

if all_passed:
    print("PROJECT CONFIGURATION VERIFIED!")
else:
    print("PLEASE CHECK THE FAILED ITEMS.")
