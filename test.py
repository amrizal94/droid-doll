import subprocess

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
            model = part.split(":")[1]
            devices.append((serial, model))

# Cetak hasil
for serial, model in devices:
    print(f"Serial: {serial}, Model: {model}")