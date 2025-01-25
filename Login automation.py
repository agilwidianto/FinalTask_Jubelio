from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://app2.jubelio.com")

try:
    # Wait for the email input field to be present and enter the email address
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
    email_input.send_keys("lijaajil100@gmail.com")

    # Wait for the password input field to be present and enter the password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
    password_input.send_keys("Qwerty1234!")

    # Wait for the login button to be clickable and click it
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ladda-label']")))
    login_button.click()

    # Wait for the modal to appear and close it
    try:
        # Adjust the selector below to match the close button of your modal
        close_button_locator = (By.XPATH, "//button[@class='close']")  # Replace with the actual locator for the close button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(close_button_locator)).click()
    except Exception as e:
        print("No modal to close or an error occurred:", e)

    # Wait for 10 seconds before closing the browser
    time.sleep(10)

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
    