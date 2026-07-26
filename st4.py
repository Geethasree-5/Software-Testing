from selenium import webdriver
from selenium.webdriver.common.by import By

def test_employee_table():

    driver = webdriver.Chrome()
    driver.maximize_window()

    # Change the path according to your computer
    driver.get(r"file:///C:\Users\Sree Sowmya\Desktop\geetha_project\pythonProject1\employee_table.html")

    rows = driver.find_elements(By.XPATH, "//table[@id='employeeTable']/tbody/tr")

    found = False

    for row in rows[1:]:
        columns = row.find_elements(By.TAG_NAME, "td")
        name = columns[0].text.strip()

        print("Found Name:", repr(name))

        if name == "Johndoe":
            print("Employee Name :", name)
            print("Department :", columns[1].text)
            print("Salary :", columns[2].text)
            found = True
            break

    if not found:
        print("Employee not found")

    driver.quit()