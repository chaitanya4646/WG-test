import schedule  # Import the schedule module
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def run_selenium_script():
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    try:
        # Open the initial login page
        driver.get("https://teamunity.bicsinfotech.com/login")

        # Click the login button to initiate the SSO process
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".button"))
        )
        login_button.click()

        # Wait for the SSO login page to load and enter email
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "i0116"))
        )
        email_field.send_keys("chaitanya.sharma@bicsinfotech.com")

        # Click the Next button
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "idSIButton9"))
        )
        next_button.click()

        # Wait for the password field to load and enter the password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "i0118"))
        )
        password_field.send_keys("Darshan11*")

        # Click the Sign-in button
        signin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "idSIButton9"))
        )
        signin_button.click()

        # Optionally, handle the 'Stay signed in' prompt
        stay_signed_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "idSIButton9"))
        )
        stay_signed_in_button.click()

        # Wait for the next page to load after SSO login
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.sidebar.open"))
        )

        # Navigate to the desired page
        desired_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.sidebar.open div:nth-child(2) div:nth-child(1) ul.nav-list li:nth-child(6) > div:nth-child(1)"))
        )
        desired_element.click()

        # Wait for the page to load
        time.sleep(1)  # Adjust or remove this as necessary

    finally:
        # Close the driver when done
        driver.quit()

# Schedule the task to run at 8:50 AM daily
schedule.every().day.at("08:50").do(run_selenium_script)

while True:
    schedule.run_pending()
    time.sleep(1)
