from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_loading_spinner():

    driver = webdriver.Chrome()
    driver.maximize_window()

    # Change this path to your HTML file
    driver.get(r"file:///C:\Users\Sree Sowmya\Desktop\geetha_project\pythonProject1\loading_spinner.html")

    wait = WebDriverWait(driver, 10)

    # Click Load Data button
    driver.find_element(By.ID, "loadBtn").click()

    # Wait until spinner disappears
    wait.until(
        EC.invisibility_of_element_located((By.ID, "spinner"))
    )

    # Verify table is visible
    table = wait.until(
        EC.visibility_of_element_located((By.ID, "dataTable"))
    )

    assert table.is_displayed()

    print("Table is Visible")

    # Print first row
    first_row = driver.find_element(
        By.XPATH,
        "//table[@id='dataTable']/tbody/tr[2]"
    ).text

    print("First Row:", first_row)

    driver.quit()