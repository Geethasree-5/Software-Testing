import pandas as pd
import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from openpyxl import Workbook

# =====================================
# START TIME
# =====================================

start_time = datetime.now()

# =====================================
# CREATE SCREENSHOT FOLDER
# =====================================

if not os.path.exists("Screenshots"):
    os.makedirs("Screenshots")

# =====================================
# READ EXCEL
# =====================================

df = pd.read_excel("TestCases.xlsx")

# =====================================
# LAUNCH BROWSER
# =====================================

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)

# =====================================
# VARIABLES
# =====================================

results = []

passed = 0
failed = 0

# =====================================
# EXECUTE TEST CASES
# =====================================

for index, row in df.iterrows():

    tc_id = row["TC_ID"]
    url = row["URL"]
    execute = row["Execute"]

    if str(execute).upper() != "Y":
        continue

    print(f"\nExecuting Test Case : {tc_id}")

    retry_count = 0
    status = "FAIL"
    screenshot_path = ""

    while retry_count < 3:

        try:

            driver.get(url)

            page_title = driver.title

            print("Title :", page_title)

            status = "PASS"

            passed += 1

            break

        except Exception as e:

            retry_count += 1

            print(
                f"Attempt {retry_count} Failed"
            )

            screenshot_path = (
                f"Screenshots/"
                f"{tc_id}_Retry_{retry_count}.png"
            )

            driver.save_screenshot(
                screenshot_path
            )

            print(
                "Screenshot Saved :",
                screenshot_path
            )

            if retry_count == 3:

                status = "FAIL"

                failed += 1

    results.append([
        tc_id,
        status,
        retry_count,
        screenshot_path
    ])

# =====================================
# CLOSE BROWSER
# =====================================

driver.quit()

# =====================================
# END TIME
# =====================================

end_time = datetime.now()

execution_time = (
    end_time - start_time
).total_seconds()

# =====================================
# TOTALS
# =====================================

total_testcases = len(results)

if total_testcases > 0:

    pass_percentage = (
        passed /
        total_testcases
    ) * 100

    fail_percentage = (
        failed /
        total_testcases
    ) * 100

else:

    pass_percentage = 0
    fail_percentage = 0

# =====================================
# EXCEL REPORT
# =====================================

wb = Workbook()

sheet = wb.active

sheet.title = "Execution Report"

sheet.append([
    "TC_ID",
    "Status",
    "Retries",
    "Screenshot"
])

for result in results:

    sheet.append(result)

sheet.append([])

sheet.append([
    "Total Test Cases",
    total_testcases
])

sheet.append([
    "Passed",
    passed
])

sheet.append([
    "Failed",
    failed
])

sheet.append([
    "Pass Percentage",
    f"{round(pass_percentage,2)}%"
])

sheet.append([
    "Fail Percentage",
    f"{round(fail_percentage,2)}%"
])

sheet.append([
    "Execution Time",
    f"{execution_time} Seconds"
])

wb.save(
    "Execution_Report.xlsx"
)

# =====================================
# HTML REPORT
# =====================================

html_content = f"""
<html>
<head>
<title>Automation Report</title>
</head>

<body>

<h1>Automation Execution Report</h1>

<h3>Summary</h3>

<p>Total Test Cases : {total_testcases}</p>

<p>Passed : {passed}</p>

<p>Failed : {failed}</p>

<p>Pass Percentage : {round(pass_percentage,2)}%</p>

<p>Fail Percentage : {round(fail_percentage,2)}%</p>

<p>Execution Time : {execution_time} Seconds</p>

<table border="1">

<tr>
<th>TC_ID</th>
<th>Status</th>
<th>Retries</th>
<th>Screenshot</th>
</tr>
"""

for result in results:

    html_content += f"""
    <tr>
    <td>{result[0]}</td>
    <td>{result[1]}</td>
    <td>{result[2]}</td>
    <td>{result[3]}</td>
    </tr>
    """

html_content += """
</table>

</body>
</html>
"""

with open(
        "HTML_Report.html",
        "w",
        encoding="utf-8"
) as report:

    report.write(html_content)

# =====================================
# CONSOLE SUMMARY
# =====================================

print("\n")
print("=" * 50)

print("AUTOMATION EXECUTION SUMMARY")

print("=" * 50)

print("Total Test Cases :", total_testcases)

print("Passed :", passed)

print("Failed :", failed)

print(
    "Pass Percentage :",
    round(pass_percentage, 2),
    "%"
)

print(
    "Fail Percentage :",
    round(fail_percentage, 2),
    "%"
)

print(
    "Execution Time :",
    execution_time,
    "Seconds"
)

print("=" * 50)

print("Excel Report Generated")

print("HTML Report Generated")