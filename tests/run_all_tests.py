import glob
import subprocess

test_scripts = glob.glob("test_*.py")

for script in test_scripts:
    print("=" * 70)
    print(f"Executing test script [{script}]")
    print("=" * 70)
    subprocess.run(["python", script])
