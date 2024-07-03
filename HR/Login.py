import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (assuming Chrome in this example)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://wg.bicsinfotech.com")
driver.maximize_window()
time.sleep(1)
# Find the login input field and enter the email
login = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]')
login.send_keys("superadmin@yopmail.com")

# Find and click the login button
login_button = driver.find_element(By.CSS_SELECTOR, '.p-5.align-items-center.surface-900.text-white.p-button.p-component.p-button-icon-only.p-button-rounded')
login_button.click()

# Add a small delay for the page to load (optional)
time.sleep(2)

# Close the browser (optional)
# driver.quit()
    