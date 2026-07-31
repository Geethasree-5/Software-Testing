from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import (
    expected_conditions as EC
)

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException
)

import os
import time


# -----------------------------------------
# Create screenshot folder
# -----------------------------------------

os.makedirs(
    "screenshots",
    exist_ok=True
)


# -----------------------------------------
# Open Chrome browser
# -----------------------------------------

driver = webdriver.Chrome()


# -----------------------------------------
# Create explicit wait
# -----------------------------------------

wait = WebDriverWait(
    driver,
    15
)


try:


    # -----------------------------------------
    # 1. Open the local website
    # -----------------------------------------

    driver.get(

        "http://127.0.0.1:5000/"

    )


    driver.maximize_window()


    print(

        "Website opened successfully"

    )


    # -----------------------------------------
    # 2. Store original window
    # -----------------------------------------

    original_window = (

        driver.current_window_handle

    )


    print(

        "Original window stored"

    )


    # -----------------------------------------
    # 3. Find View Details button
    # -----------------------------------------

    view_details_button = (

        wait.until(

            EC.element_to_be_clickable(

                (

                    By.ID,

                    "view-details"

                )

            )

        )

    )


    # -----------------------------------------
    # 4. Click View Details
    # -----------------------------------------

    view_details_button.click()


    print(

        "View Details button clicked"

    )


    # -----------------------------------------
    # 5. Wait for new tab
    # -----------------------------------------

    wait.until(

        EC.number_of_windows_to_be(

            2

        )

    )


    print(

        "New browser tab opened"

    )


    # -----------------------------------------
    # 6. Switch to new tab
    # -----------------------------------------

    for window in (

        driver.window_handles

    ):

        if window != original_window:

            driver.switch_to.window(

                window

            )

            break


    print(

        "Switched to new tab"

    )


    # -----------------------------------------
    # 7. Wait for loading spinner to disappear
    # -----------------------------------------

    wait.until(

        EC.invisibility_of_element_located(

            (

                By.ID,

                "loading-spinner"

            )

        )

    )


    print(

        "Loading spinner disappeared"

    )


    # -----------------------------------------
    # 8. Wait for product name
    # -----------------------------------------

    product_name_element = (

        wait.until(

            EC.visibility_of_element_located(

                (

                    By.ID,

                    "product-name"

                )

            )

        )

    )


    # -----------------------------------------
    # 9. Wait for product rating
    # -----------------------------------------

    product_rating_element = (

        wait.until(

            EC.visibility_of_element_located(

                (

                    By.ID,

                    "product-rating"

                )

            )

        )

    )


    # -----------------------------------------
    # 10. Extract product information
    # -----------------------------------------

    product_name = (

        product_name_element.text.strip()

    )


    product_rating = (

        product_rating_element.text.strip()

    )


    print()

    print(

        "Product Name:",

        product_name

    )


    print(

        "Product Rating:",

        product_rating

    )


    # -----------------------------------------
    # 11. Close new tab
    # -----------------------------------------

    driver.close()


    print()

    print(

        "Product details tab closed"

    )


    # -----------------------------------------
    # 12. Return to original window
    # -----------------------------------------

    driver.switch_to.window(

        original_window

    )


    print(

        "Returned to original window"

    )


    print()

    print(

        "TEST PASSED SUCCESSFULLY"

    )


# -----------------------------------------
# Take screenshot if element is not found
# -----------------------------------------

except (

    TimeoutException,

    NoSuchElementException

) as error:


    print()

    print(

        "ELEMENT NOT FOUND"

    )


    print(

        "Error:",

        error

    )


    # Screenshot name

    screenshot_file = (

        "screenshots/"

        "element_not_found_"

        + str(

            int(

                time.time()

            )

        )

        + ".png"

    )


    # Take screenshot

    driver.save_screenshot(

        screenshot_file

    )


    print()

    print(

        "Screenshot saved at:"

    )


    print(

        screenshot_file

    )


# -----------------------------------------
# Handle unexpected errors
# -----------------------------------------

except Exception as error:


    print()

    print(

        "UNEXPECTED ERROR"

    )


    print(

        error

    )


# -----------------------------------------
# Close browser
# -----------------------------------------

finally:


    # Keep browser open for 5 seconds

    time.sleep(5)


    driver.quit()