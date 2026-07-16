from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/tables")

# Get Last Name column values
def get_last_names():
    rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
    return [row.find_element(By.XPATH, "./td[1]").text for row in rows]

# ---------------------------
# STEP 1: Capture original data
# ---------------------------
original_data = get_last_names()
print("Original:", original_data)

# ---------------------------
# STEP 2: Click Last Name header (ASC)
# ---------------------------
last_name_header = driver.find_element(By.XPATH, "//table[@id='table1']//span[text()='Last Name']")
last_name_header.click()

wait.until(lambda d: get_last_names() != original_data)

asc_data = get_last_names()
print("Ascending:", asc_data)

# Validate ascending order
assert asc_data == sorted(asc_data), "Ascending sort failed!"

# ---------------------------
# STEP 3: Click again (DESC)
# ---------------------------
last_name_header.click()

wait.until(lambda d: get_last_names() != asc_data)

desc_data = get_last_names()
print("Descending:", desc_data)

# Validate descending order
assert desc_data == sorted(desc_data, reverse=True), "Descending sort failed!"

print("Sorting Verification Passed Successfully!")

driver.quit()