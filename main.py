import os
import subprocess
import time
import pyautogui

# Path ke direktori scrcpy
current_dir = os.path.dirname(os.path.abspath(__file__))
scrcpy_dir = os.path.join(current_dir, "scrcpy-win64-v2.7")
os.chdir(scrcpy_dir)

# Jalankan perintah adb devices -l
output = subprocess.check_output(["adb", "devices", "-l"], text=True)

# Pisahkan output per baris
lines = output.strip().split("\n")

# Filter baris dengan informasi perangkat (tidak termasuk header)
device_lines = [line for line in lines if "model:" in line]

# Ambil model dari setiap perangkat
devices = []
for line in device_lines:
    parts = line.split()
    serial = parts[0]  # Serial perangkat
    for part in parts:
        if part.startswith("model:"):
            model = part.split(":")[1].replace("_", " ")  # Ganti _ dengan spasi
            devices.append((serial, model))

# Fungsi untuk memindahkan jendela
def move_window(title, x, y, width, height):
    win = pyautogui.getWindowsWithTitle(title)
    if win:
        win[0].moveTo(x, y)
        win[0].resizeTo(width, height)

# Hitung posisi jendela untuk satu baris, empat kolom
screen_width, screen_height = pyautogui.size()
columns = 4
window_width = screen_width // columns
window_height = screen_height  # Jendela penuh tinggi layar
positions = [(i * window_width, 0, window_width, window_height) for i in range(columns)]

# Pastikan jumlah perangkat tidak melebihi jumlah kolom
if len(devices) > columns:
    print("Jumlah perangkat melebihi kolom yang tersedia. Tambahkan logika untuk baris tambahan jika diperlukan.")
    exit()

# Jalankan scrcpy untuk setiap perangkat dan pindahkan jendela
for idx, (serial, model) in enumerate(devices):
    position = positions[idx]
    subprocess.Popen(f".\\scrcpy.exe -s {serial}")
    time.sleep(3)  # Jeda untuk memastikan jendela muncul
    move_window(model, *position)
    time.sleep(1) 
