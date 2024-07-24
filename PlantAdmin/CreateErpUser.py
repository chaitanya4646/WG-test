import time
import json
import logging
from venv import logger

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (assuming Chrome in this example)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://wg.bicsinfotech.com")
driver.maximize_window()

# Set implicit wait
driver.implicitly_wait(10)

# Find the login input fields and enter credentials
username = driver.find_element(By.CSS_SELECTOR, "#name")
username.send_keys("plantadmin01")

password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
password.send_keys("Pass@1234")

# Find and click the login button
login_button = driver.find_element(By.CSS_SELECTOR, ".p-5")
login_button.click()

# redirect to create ERP user page
driver.find_element(By.CSS_SELECTOR,"li[aria-label='Create Plant User'] a[class='p-menuitem-link']").click()

# add user
driver.find_element(By.CSS_SELECTOR,"button[aria-label='Add User'] span[class='p-button-label p-c']").click()

# empname
def create_erp_user(driver, employee_data)

    emp_data = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='New Employee']")))
    emp_data.click()
    logger.info("Clicked on New Employee button.")