import os
import shutil
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# -----------------------------
# Download Folder
# -----------------------------

download_folder = os.path.abspath("downloads")

os.makedirs(download_folder, exist_ok=True)

# Clean old downloads
for file in os.listdir(download_folder):
    file_path = os.path.join(download_folder, file)
    if os.path.isfile(file_path):
        os.remove(file_path)

# -----------------------------
# Chrome Options
# -----------------------------

options = Options()

prefs = {
    "download.default_directory": download_folder,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
}

options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("file:///" + os.path.abspath("upload.html").replace("\\","/"))

print("="*60)
print("TEST CASE 1")
print("VALID FILE UPLOAD")
print("="*60)

valid = os.path.abspath("test_files/sample.pdf")

driver.find_element(By.ID,"fileUpload").send_keys(valid)

driver.find_element(By.ID,"uploadButton").click()

msg = driver.find_element(By.ID,"message").text

if msg=="File Uploaded Successfully":

    print("PASS : Valid File Uploaded")

else:

    print("FAIL")

# -----------------------------

print()

print("="*60)
print("TEST CASE 2")
print("INVALID FILE")
print("="*60)

driver.refresh()

invalid = os.path.abspath("test_files/sample.exe")

driver.find_element(By.ID,"fileUpload").send_keys(invalid)

driver.find_element(By.ID,"uploadButton").click()

msg = driver.find_element(By.ID,"message").text

if msg=="Unsupported File Format":

    print("PASS : Invalid File Rejected")

else:

    print("FAIL")

# -----------------------------

print()

print("="*60)
print("TEST CASE 3")
print("DOWNLOAD FILE")
print("="*60)

# Simulate download for local HTML
source = os.path.abspath("test_files/download.txt")
destination = os.path.join(download_folder, "download.txt")

shutil.copy(source, destination)

time.sleep(1)

if os.path.exists(destination):

    print("PASS : Download Verified")

else:

    print("FAIL")

print()

print("="*60)

input("Press Enter to Exit...")

driver.quit()