from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import threading
import time
import pandas as pd

# Store Results
results = []


def execute_test(browser_name):

    start_time = time.time()

    status = "PASS"

    driver = None

    try:

        if browser_name == "Chrome":

            driver = webdriver.Chrome(
                service=ChromeService(
                    ChromeDriverManager().install()
                )
            )

        elif browser_name == "Firefox":

            driver = webdriver.Firefox(
                service=FirefoxService(
                    GeckoDriverManager().install()
                )
            )

        elif browser_name == "Edge":

            driver = webdriver.Edge(
                service=EdgeService(
                    EdgeChromiumDriverManager().install()
                )
            )

        driver.maximize_window()

        # Open Website
        driver.get(
            "https://www.google.com"
        )

        # Search
        search_box = driver.find_element(
            By.NAME,
            "q"
        )

        search_box.send_keys(
            "Software Testing"
        )

        search_box.send_keys(
            Keys.RETURN
        )

        time.sleep(3)

        # Screenshot
        driver.save_screenshot(
            f"{browser_name}.png"
        )

    except Exception as e:

        status = "FAIL"

        print(
            browser_name,
            "Error:",
            str(e)
        )

    finally:

        execution_time = round(
            time.time() - start_time,
            2
        )

        results.append([
            browser_name,
            execution_time,
            status
        ])

        if driver:
            driver.quit()


# Threads
chrome_thread = threading.Thread(
    target=execute_test,
    args=("Chrome",)
)

firefox_thread = threading.Thread(
    target=execute_test,
    args=("Firefox",)
)

edge_thread = threading.Thread(
    target=execute_test,
    args=("Edge",)
)

# Start All Browsers
chrome_thread.start()
firefox_thread.start()
edge_thread.start()

# Wait For Completion
chrome_thread.join()
firefox_thread.join()
edge_thread.join()

# Generate Report
report = pd.DataFrame(
    results,
    columns=[
        "Browser Name",
        "Execution Time (Sec)",
        "Status"
    ]
)

report.to_excel(
    "Browser_Test_Report.xlsx",
    index=False
)

print("\n===== SUMMARY REPORT =====")

print(report)

print(
    "\nExcel Report Generated Successfully"
)