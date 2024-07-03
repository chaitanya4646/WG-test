
import time
import json
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
import colorlog

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

def init_driver():
    """ Initialize Chrome WebDriver with options """
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def login(driver, email, password):
    """ Perform login with provided credentials """
    try:
        driver.get("https://wg.bicsinfotech.com")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#name'))).send_keys(email)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))).send_keys(password)
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '.p-5.align-items-center.surface-900.text-white.p-button.p-component.p-button-icon-only.p-button-rounded')))
        login_button.click()
        logger.info("Logged in successfully.")
    except TimeoutException as e:
        logger.error("Timeout occurred during login: %s", e)
        driver.quit()

def create_employee_record(driver, employee_data):
    """ Create a single employee record using provided data """
    try:
        # Click on New Employee button
        new_employee_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='New Employee']")))
        new_employee_button.click()
        logger.info("Clicked on New Employee button.")

        # Wait for the Employee Information page to load
        employee_info_page = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Employee Information')]")))
        logger.info("Employee Information page loaded.")

        # Assertion to verify if Employee Information text is present
        assert "Employee Information" in employee_info_page.text

        # Enter employee name
        driver.find_element(By.CSS_SELECTOR, "#employeeName").send_keys(employee_data['employeeName'])

        # Click on Gender dropdown to expand it
        gender_dropdown = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Select Gender'] svg")))
        gender_dropdown.click()

        # Selecting Gender option
        gender_option = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, f"//li[contains(@class, 'p-dropdown-item')]//span[contains(text(), '{employee_data['gender']}')]")))
        gender_option.click()

        # Selecting Employee Type
        emp_type_dropdown = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Select an Employee Type')]")))
        emp_type_dropdown.click()

        emp_type_option = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, f"//li[contains(@class, 'p-dropdown-item')]//span[contains(text(), '{employee_data['employeeType']}')]")))
        emp_type_option.click()

        # Selecting Plant
        plant_dropdown = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Select a Plant')]")))
        plant_dropdown.click()

        plant_option = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, f"//li[contains(@class, 'p-dropdown-item')]//span[contains(text(), '{employee_data['plant']}')]")))
        plant_option.click()

        # Selecting Department
        department_dropdown = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Select'] svg")))
        department_dropdown.click()

        department_option = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, f"//li[contains(@class, 'p-dropdown-item')]//span[contains(text(), '{employee_data['department']}')]")))
        department_option.click()

        # Selecting Designation
        designation_dropdown = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                           "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(3)")))
        designation_dropdown.click()

        time.sleep(2)  # Waiting for dropdown to populate

        designation_option = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, f"//li[contains(@class, 'p-dropdown-item')]//span[contains(text(), '{employee_data['designation']}')]")))
        designation_option.click()

        # Entering Date of Joining (DOJ)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div/div[2]/div[3]/div/div[2]/span/input").send_keys(
            employee_data['dateOfJoining'])

        # Entering Permanent Address
        driver.find_element(By.CSS_SELECTOR, "#permanentAddress").send_keys(employee_data['permanentAddress'])

        # Entering Communication Address
        driver.find_element(By.CSS_SELECTOR, "#communicationAddress").send_keys(employee_data['communicationAddress'])

        # Entering Contact Number 1
        driver.find_element(By.CSS_SELECTOR, "#contactNumber1").send_keys(employee_data['contactNumber1'])

        # Entering Contact Number 2
        driver.find_element(By.CSS_SELECTOR, "#contactNumber2").send_keys(employee_data['contactNumber2'])

        # Entering Email
        driver.find_element(By.CSS_SELECTOR, "#email1").send_keys(employee_data['email'])

        # Entering Aadhar Card Number
        driver.find_element(By.CSS_SELECTOR, "#aadharNumber").send_keys(employee_data['aadharNumber'])
        logger.info("Entered Aadhar number.")

        # Entering PAN Card Number
        driver.find_element(By.CSS_SELECTOR, "#panNumber").send_keys(employee_data['panNumber'])
        logger.info("Entered PAN number.")

        # Entering Bank Name
        driver.find_element(By.CSS_SELECTOR, "#bankName").send_keys(employee_data['bankName'])
        logger.info("Entered bank name.")

        # Entering IFSC Code
        driver.find_element(By.CSS_SELECTOR, "#ifscCode").send_keys(employee_data['ifscCode'])
        logger.info("Entered IFSC code.")

        # Entering UAN Number
        driver.find_element(By.CSS_SELECTOR, "#uanNumber").send_keys(employee_data['uanNumber'])
        logger.info("Entered UAN number.")

        # Entering ESIC Number
        driver.find_element(By.CSS_SELECTOR, "#esicNumber").send_keys(employee_data['esicNumber'])
        logger.info("Entered ESIC number.")

        # Entering Bank Account Number
        driver.find_element(By.CSS_SELECTOR, "#bankAccountNumber").send_keys(employee_data['bankAccountNumber'])
        logger.info("Entered bank account number.")

        # Submitting the form
        submit_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='save'] span[class='p-button-label p-c']")))
        submit_button.click()
        logger.info("Submitted form.")

        time.sleep(3)  # Adding a delay for stability

    except TimeoutException as e:
        logger.error("Timeout occurred during the process: %s", e)
    except NoSuchElementException as e:
        logger.error("Element not found: %s", e)
    except WebDriverException as e:
        logger.error("WebDriver exception occurred: %s", e)

def main():
    """ Main function to automate creation of employee records from JSON data """
    driver = init_driver()
    try:
        login(driver, "hrAdmin", "Pass@1234")

        # Wait until Master menu appears
        logger.info("Waiting for Master menu...")
        master_menu = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Master')]")))
        master_menu.click()
        logger.info("Clicked on Master menu.")

        # Click on Employee Master submenu


        logger.info("Waiting for Employee Master submenu...")
        employee_master_submenu = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Employee master")))
        employee_master_submenu.click()
        logger.info("Clicked on Employee Master submenu.")

        # Read employee data from JSON file
        with open("employee_data.json", "r") as file:
            employee_data_list = json.load(file)

        # Creating employee records from JSON data
        for employee_data in employee_data_list:
            create_employee_record(driver, employee_data)
            logger.info("Created an employee record for: %s", employee_data['employeeName'])

    finally:
        driver.quit()

if __name__ == "__main__":
    main()

