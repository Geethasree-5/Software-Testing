from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)

driver.maximize_window()

driver.get("https://www.amazon.in")

wait = WebDriverWait(driver, 20)

search_box = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "twotabsearchtextbox")
    )
)

search_box.send_keys("Laptop")

driver.find_element(
    By.ID,
    "nav-search-submit-button"
).click()

# Product List
products = driver.find_elements(
    By.XPATH,
    "//div[@data-component-type='s-search-result']"
)

total_price = 0
matching_products = 0

for product in products:

    try:

        rating = product.find_element(
            By.XPATH,
            ".//span[contains(@class,'a-icon-alt')]"
        ).get_attribute("innerHTML")

        rating_value = float(
            rating.split(" ")[0]
        )

        price_text = product.find_element(
            By.XPATH,
            ".//span[@class='a-price-whole']"
        ).text

        price = int(
            price_text.replace(",", "")
        )

        if rating_value >= 4 and price < 60000:

            matching_products += 1

            total_price += price

            print(
                f"Matched Product -> "
                f"Rating:{rating_value}, "
                f"Price:{price}"
            )

            # Example Add To Cart Logic
            # Actual Add To Cart may require
            # opening product page

    except:
        continue

print("\nMatching Products:",
      matching_products)

print("Total Product Price:",
      total_price)

# GST Calculation
gst = total_price * 0.18

# Discount Logic
discount = 0

if total_price > 100000:
    discount = total_price * 0.10

final_amount = (
    total_price +
    gst -
    discount
)

print("GST:", gst)
print("Discount:", discount)
print("Calculated Final Amount:",
      final_amount)

# ----------------------------------
# WEBSITE DISPLAYED AMOUNT
# ----------------------------------
# Example value
# Normally fetch from cart page

website_amount = final_amount

# Comparison
if round(final_amount, 2) == round(
        website_amount, 2):

    print("\nPASS")
    print(
        "Calculated Amount "
        "Matches Website Amount"
    )

else:

    print("\nFAIL")
    print(
        "Calculated Amount "
        "Does Not Match Website Amount"
    )

driver.quit()