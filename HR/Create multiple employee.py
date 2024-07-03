import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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


def create_employee_record(driver):
    """ Create a single employee record """
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
        driver.find_element(By.CSS_SELECTOR, "#employeeName").send_keys("Automation user")

        # Click on Gender dropdown to expand it
        gender_dropdown = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Select Gender'] svg")))
        gender_dropdown.click()

        # Selecting Male option
        male_option = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "//li[contains(@class, 'p-dropdown-item')]//span[contains(text(), 'Male')]")))
        male_option.click()

        # Selecting Employee Type (assuming 'Quality' option is available)
        emp_type_dropdown = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Select an Employee Type')]")))
        emp_type_dropdown.click()

        emp_type_elements = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@class='p-dropdown-item']")))
        emp_type_texts = [element.text.strip() for element in emp_type_elements]

        if "Quality" in emp_type_texts:
            quality_element = emp_type_elements[emp_type_texts.index("Quality")]
            quality_element.click()
            logger.info("Selected Quality employee type.")
        else:
            logger.error("Quality employee type not found.")

        # Selecting Plant (assuming 'b' option is available)
        plant_dropdown = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Select a Plant')]")))
        plant_dropdown.click()

        plant_option = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "//li[contains(@class, 'p-dropdown-item')]//span[contains(text(), 'b')]")))
        plant_option.click()

        # Selecting Department (assuming 'Sales' option is available)
        department_dropdown = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Select'] svg")))
        department_dropdown.click()

        department_elements = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item")))
        department_texts = [element.text.strip() for element in department_elements]

        if "Sales" in department_texts:
            sales_element = department_elements[department_texts.index("Sales")]
            sales_element.click()
            logger.info("Selected Sales department.")
        else:
            logger.error("Sales department not found.")

        # Selecting Designation (assuming 'VP' option is available)
        designation_dropdown = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                           "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(3)")))
        designation_dropdown.click()

        time.sleep(2)  # Waiting for dropdown to populate

        designation_elements = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item")))
        designation_texts = [element.text.strip() for element in designation_elements]

        if "VP" in designation_texts:
            vp_index = designation_texts.index("VP")
            vp_element = designation_elements[vp_index]
            vp_element.click()
            logger.info("Selected VP designation.")
        else:
            logger.error("VP designation not found.")

        # Entering Date of Joining (DOJ)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div/div[2]/div[3]/div/div[2]/span/input").send_keys(
            '01-06-2024')

        # Entering Permanent Address
        driver.find_element(By.CSS_SELECTOR, "#permanentAddress").send_keys("abcd")

        # Entering Communication Address
        driver.find_element(By.CSS_SELECTOR, "#communicationAddress").send_keys("pqr")

        # Entering Contact Number 1
        driver.find_element(By.CSS_SELECTOR, "#contactNumber1").send_keys("1818181888")

        # Entering Contact Number 2
        driver.find_element(By.CSS_SELECTOR, "#contactNumber2").send_keys("8787878788")

        # Entering Email
        driver.find_element(By.CSS_SELECTOR, "#email1").send_keys("automation@yopmail.com")

        # Entering Aadhar Card Number
        driver.find_element(By.CSS_SELECTOR, "#aadharNumber").send_keys("111111111111")

        logger.info("Entered Aadhar number.")

        # Entering PAN Card Number
        driver.find_element(By.CSS_SELECTOR, "#panNumber").send_keys("ABCTY1234D")
        logger.info("Entered PAN number.")

        # Entering Bank Name
        driver.find_element(By.CSS_SELECTOR, "#bankName").send_keys("HDFC")
        logger.info("Entered bank name.")

        # Entering IFSC Code
        driver.find_element(By.CSS_SELECTOR, "#ifscCode").send_keys("ABCD0123450")
        logger.info("Entered IFSC code.")

        # Entering UAN Number
        driver.find_element(By.CSS_SELECTOR, "#uanNumber").send_keys("122233232322")
        logger.info("Entered UAN number.")

        # Entering ESIC Number
        driver.find_element(By.CSS_SELECTOR, "#esicNumber").send_keys("11111111111111111")
        logger.info("Entered ESIC number.")

        # Entering Bank Account Number
        driver.find_element(By.CSS_SELECTOR, "#bankAccountNumber").send_keys("122233232322")
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
    """ Main function to automate creation of 10 employee records """
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

        # Creating 10 employee records
        for _ in range(10):
            create_employee_record(driver)
            logger.info("Created an employee record.")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
