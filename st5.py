from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

# Replace with your actual file path
driver.get(r"file:///C:\Users\Sree Sowmya\Desktop\geetha_project\pythonProject1\index.html")

# Store original window
original_window = driver.current_window_handle

# Click the button
driver.find_element(By.TAG_NAME, "button").click()

# Wait until the second window opens
WebDriverWait(driver, 10).until(
    lambda d: len(d.window_handles) == 2
)

# Switch to new window
for window in driver.window_handles:
    if window != original_window:
        driver.switch_to.window(window)
        break

# Verify title contains Dashboard
assert "Dashboard" in driver.title
print("New Window Title:", driver.title)

# Close new window
driver.close()

# Switch back
driver.switch_to.window(original_window)

# Print original title
print("Original Window Title:", driver.title)

driver.quit()