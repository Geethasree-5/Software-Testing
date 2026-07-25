from faker import Faker
import os

fake = Faker()

folder = "test_files"

os.makedirs(folder, exist_ok=True)

# ------------------------
# Valid PDF
# ------------------------

pdf = os.path.join(folder, "sample.pdf")

with open(pdf, "wb") as f:

    f.write(b"%PDF-1.4\n")
    f.write(fake.text().encode())
    f.write(b"\n%%EOF")

print("PDF Created")

# ------------------------
# Invalid EXE
# ------------------------

exe = os.path.join(folder, "sample.exe")

with open(exe, "w") as f:

    f.write(fake.text())

print("EXE Created")

# ------------------------
# Download File
# ------------------------

download = os.path.join(folder, "download.txt")

with open(download, "w") as f:

    f.write(fake.paragraph())

print("Download File Created")

print("All Test Files Generated Successfully")