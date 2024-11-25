import os
import subprocess
import time

# Path ke direktori scrcpy
# scrcpy_dir = os.path.expanduser(r"~\OneDrive\Desktop\scrcpy-win64-v2.7")
current_dir = os.path.dirname(os.path.abspath(__file__))
scrcpy_dir = os.path.join(current_dir, "scrcpy-win64-v2.7")
os.chdir(scrcpy_dir)
os.chdir(scrcpy_dir)

# Dapatkan daftar perangkat dari adb
result = subprocess.check_output("adb devices", shell=True).decode()
devices = [line.split()[0] for line in result.splitlines() if "\tdevice" in line]

for device in devices:
    subprocess.Popen(f".\\scrcpy.exe -s {device}")
    time.sleep(1)  # Jeda 1 detik
