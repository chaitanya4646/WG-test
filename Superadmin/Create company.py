import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

from faker import Faker

fake = Faker()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def login(driver, email, password):
    try:
        driver.get("https://wg.bicsinfotech.com")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#name'))).send_keys(email)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))).send_keys(password)
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '.p-5.align-items-center.surface-900.text-white.p-button.p-component.p-button-icon-only.p-button-rounded')))
        login_button.click()
        logger.info("Logged in successfully.")
    except TimeoutException as e:
        logger.error("Timeout occurred during login: %s", e)
        driver.quit()

def create_company(driver, company_details):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[aria-label='Create Company'] span[class='p-button-label p-c']"))).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#companyName"))).send_keys(
            company_details['name'])

        driver.find_element(By.CSS_SELECTOR, "#address1").send_keys(company_details['address1'])
        driver.find_element(By.CSS_SELECTOR, "#address2").send_keys(company_details['address2'])
        driver.find_element(By.CSS_SELECTOR, "#address3").send_keys(company_details['address3'])
        driver.find_element(By.CSS_SELECTOR, "#city").send_keys(company_details['city'])
        driver.find_element(By.CSS_SELECTOR, "#tel").send_keys(company_details['tel'])
        driver.find_element(By.CSS_SELECTOR, "#dist").send_keys(company_details['dist'])
        driver.find_element(By.CSS_SELECTOR, "#pinCode").send_keys(company_details['pinCode'])
        driver.find_element(By.CSS_SELECTOR, "#state").send_keys(company_details['state'])
        driver.find_element(By.CSS_SELECTOR, "#country").send_keys(company_details['country'])
        driver.find_element(By.CSS_SELECTOR, "#phoneNumber").send_keys(company_details['phoneNumber'])
        driver.find_element(By.CSS_SELECTOR, "#fax").send_keys(company_details['fax'])
        driver.find_element(By.CSS_SELECTOR, "#email").send_keys(company_details['email'])
        driver.find_element(By.CSS_SELECTOR, "#gstNumber").send_keys(company_details['gstNumber'])
        driver.find_element(By.CSS_SELECTOR, "#panNumber").send_keys(company_details['panNumber'])
        driver.find_element(By.CSS_SELECTOR, "#cinNumber").send_keys(company_details['cinNumber'])

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[aria-label='Save'] span[class='p-button-label p-c']"))).click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'Ok Noted')]"))).click()

        verify_company(driver, company_details['name'])
        return True  # Indicate success
    except TimeoutException as e:
        logger.error("Timeout occurred during company creation: %s", e)
    except WebDriverException as e:
        logger.error("WebDriver exception occurred: %s", e)
    return False  # Indicate failure

def verify_company(driver, company_name):
    try:
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search']")))
        search_input.send_keys(company_name)
        time.sleep(2)  # Allow time for search results to update
        try:
            company_row = driver.find_element(By.XPATH, f"//td[normalize-space()='{company_name}']")
            assert company_row is not None
            logger.info(f"Company '{company_name}' created successfully.")
        except NoSuchElementException:
            logger.error(f"Failed to create company '{company_name}'.")
    except TimeoutException as e:
        logger.error("Timeout occurred during company verification: %s", e)

def generate_company_details(index):
    company_name = f"Automation_Companys{index}"
    return {
        'name': company_name,
        'address1': 'Asangoan1',
        'address2': 'PQR',
        'address3': 'XYZ',
        'city': 'Thane',
        'tel': '1919191919',
        'dist': 'Thane',
        'pinCode': '919199',
        'state': 'Maharashtra',
        'country': 'India',
        'phoneNumber': '8989899999',
        'fax': '1111111111',
        'email': f'Automation_Companys{index}@yopmail.com',
        'gstNumber': '22AAAAA8888A1Z5',
        'panNumber': 'ABCTY1234D',
        'cinNumber': 'L17110MH1973PLC019786'
    }

def main():
    driver = init_driver()
    try:
        login(driver, "superAdmin", "Pass@1234")
        success_count = 0
        for i in range(1, 20):  # Change this range to create more companies
            company_details = generate_company_details(i)
            if create_company(driver, company_details):
                success_count += 1
        logger.info(f"Process done. Created {success_count} companies.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
