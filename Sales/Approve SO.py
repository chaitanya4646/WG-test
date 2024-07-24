import time
import colorlog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Logging configuration
formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)s: %(message)s",
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Initialize the WebDriver (assuming Chrome in this example)
driver = webdriver.Chrome()

try:
    # Open the webpage
    driver.get("https://wg.bicsinfotech.com")
    driver.maximize_window()

    # Set implicit wait
    driver.implicitly_wait(10)

    # Find the login input fields and enter credentials
    try:
        username = driver.find_element(By.CSS_SELECTOR, "#name")
        username.send_keys("SalesHead")
        password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
        password.send_keys("Pass@1234")
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '.p-5.align-items-center.surface-900.text-white.p-button.p-component.p-button-icon-only.p-button-rounded')))
        login_button.click()
        logger.info("Logged in successfully.")
    except Exception as e:
        logger.error(f"Error during login: {e}")
        driver.quit()
        exit()

    # Click on dashboard
    try:
        approveBlock = driver.find_element(By.CSS_SELECTOR, "li[aria-label='Dashboard'] a[class='p-menuitem-link']")
        approveBlock.click()
        logger.info(f"Clicked on dashboard: {approveBlock.text}")
    except Exception as e:
        logger.error(f"Error clicking on dashboard: {e}")
        driver.quit()
        exit()

    # Click on Approve Block
    try:
        SO_block = driver.find_element(By.CSS_SELECTOR, ".cursor-pointer.font-family-roboto.dashboard-box.bg-primary.mx-3.my-3.font-semibold")
        SO_block.click()
        logger.info("Clicked on Approve Block")
    except Exception as e:
        logger.error(f"Error clicking on Approve Block: {e}")
        driver.quit()
        exit()

    # Select checkboxes and approve
    approvecount = 10
    for _ in range(approvecount):
        try:
            checkboxes = driver.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(1) td:nth-child(1) div:nth-child(1) div:nth-child(1)")
            for checkbox in checkboxes:
                if not checkbox.is_selected():
                    checkbox.click()

            # Locate the 'Approve' button and click it
            approve_button = driver.find_element(By.CSS_SELECTOR, ".text-100.bg-green-500.p-button.p-component")
            approve_button.click()

            # Handle popup
            pop_up = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Yes'] span[class='p-button-label p-c']")
            pop_up.click()

            # Optionally, wait for any confirmation message or the page to update
            time.sleep(3)
        except Exception as e:
            logger.error(f"Error during approval process: {e}")
            driver.quit()
            exit()

    # Verify success message
    try:
        closeable_message_locator = (By.CSS_SELECTOR, "div[class='p-toast p-component p-toast-bottom-center custom-toast p-ripple-disabled'] div")
        wait = WebDriverWait(driver, 10)
        closeable_message_element = wait.until(EC.visibility_of_element_located(closeable_message_locator))

        # Verify the message content
        expected_content = "success"
        if expected_content in closeable_message_element.text.lower():
            logger.info(f"Success message found: {closeable_message_element.text}")
        else:
            logger.warning("Expected success message not found.")
    except Exception as e:
        logger.error(f"Error verifying success message: {e}")
finally:
    # Quit the WebDriver session
    driver.quit()