from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import (
    expected_conditions as EC
)

from selenium.common.exceptions import (
    TimeoutException
)


# Open Google Chrome
driver = webdriver.Chrome()


# Create an explicit wait
wait = WebDriverWait(
    driver,
    15
)


try:

    # Open the local e-commerce dashboard
    driver.get(
        "http://127.0.0.1:5000/"
    )


    # Maximize the browser
    driver.maximize_window()


    print(
        "E-commerce dashboard opened"
    )


    # Find the search box
    search_box = wait.until(

        EC.visibility_of_element_located(

            (
                By.ID,
                "product-search"
            )

        )

    )


    # Search for Wireless Mouse
    search_box.clear()

    search_box.send_keys(
        "Wireless Mouse"
    )


    print(
        "Searched for Wireless Mouse"
    )


    # Find the Wireless Mouse row
    product_row = wait.until(

        EC.visibility_of_element_located(

            (

                By.XPATH,

                "//tr["
                ".//td[contains("
                "normalize-space(), "
                "'Wireless Mouse'"
                ")]"
                "]"

            )

        )

    )


    # Find the stock status
    stock_status = (

        product_row

        .find_element(

            By.CLASS_NAME,

            "stock"

        )

        .text

        .strip()

    )


    # Verify stock status
    assert (

        stock_status

        .lower()

        ==

        "in stock"

    ), (

        "Expected: In Stock, "

        "but found: "

        + stock_status

    )


    print(
        "Stock status verified: "
        + stock_status
    )


    # Find the Edit button
    edit_button = (

        product_row

        .find_element(

            By.CLASS_NAME,

            "edit-button"

        )

    )


    # Click Edit
    edit_button.click()


    print(
        "Edit button clicked"
    )


    # Wait until edit form appears
    edit_form = wait.until(

        EC.visibility_of_element_located(

            (
                By.ID,
                "edit-form"
            )

        )

    )


    # Wait for the price field
    price_input = wait.until(

        EC.visibility_of_element_located(

            (
                By.ID,
                "product-price"
            )

        )

    )


    # Clear old price
    price_input.clear()


    # Enter the new price
    price_input.send_keys(
        "29.99"
    )


    print(
        "Price changed to $29.99"
    )


    # Find the Save button
    save_button = wait.until(

        EC.element_to_be_clickable(

            (
                By.ID,
                "save-product"
            )

        )

    )


    # Save the product
    save_button.click()


    print(
        "Save button clicked"
    )


    # Wait for success message
    success_message = wait.until(

        EC.visibility_of_element_located(

            (

                By.CLASS_NAME,

                "success-message"

            )

        )

    )


    # Read the success message
    message_text = (

        success_message

        .text

        .strip()

    )


    # Verify the message
    assert (

        "successfully"

        in

        message_text.lower()

    ), (

        "Success message "

        "was not displayed"

    )


    print(
        "Success message verified:"
    )

    print(
        message_text
    )


    # Verify updated price
    updated_price = (

        product_row

        .find_element(

            By.CLASS_NAME,

            "product-price"

        )

        .text

        .strip()

    )


    assert (

        updated_price

        ==

        "$29.99"

    ), (

        "Price update failed. "

        "Current price: "

        + updated_price

    )


    print(
        "Updated price verified:"
        " $29.99"
    )


    print()

    print(
        "TEST PASSED SUCCESSFULLY"
    )


except TimeoutException:

    print()

    print(
        "TEST FAILED:"
    )

    print(
        "The required webpage "
        "element was not found."
    )


except AssertionError as error:

    print()

    print(
        "TEST FAILED:"
    )

    print(
        error
    )


except Exception as error:

    print()

    print(
        "UNEXPECTED ERROR:"
    )

    print(
        error
    )


finally:

    # Keep browser open for 5 seconds
    import time

    time.sleep(5)


    # Close the browser
    driver.quit()