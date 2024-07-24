import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Define Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start Chrome maximized

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Set the implicitly wait time
driver.implicitly_wait(10)  # seconds

# Navigate to the target URL
driver.get("https://wg.bicsinfotech.com")

# Perform login
email_input = driver.find_element(By.CSS_SELECTOR, "#name")
email_input.send_keys("hradmin")
password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
password.send_keys("Pass@1234")  # Add the correct password here
login_button = driver.find_element(By.CSS_SELECTOR, ".p-5.align-items-center.surface-900.text-white.p-button.p-component.p-button-icon-only.p-button-rounded")

try:
    login_button.click()
    print("Login successful")
except Exception as e:
    print("Login failed:", e)
    driver.quit()
    exit()

# Load employee data from JSON file
with open('employee_data.json') as f:
    employee_data_list = json.load(f)

for employee_data in employee_data_list:
    try:
        # Wait until Master menu appears
        master_menu = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Master')]"))
        )

        # Click on Master menu
        master_menu.click()

        # Click on Employee Master submenu
        employee_master_submenu = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Employee master"))
        )
        employee_master_submenu.click()

        # Click on New Employee button
        new_employee_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='New Employee']"))
        )
        new_employee_button.click()

        # Wait for the Employee Information page to load
        employee_info_page = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Employee Information')]"))
        )

        # Assertion to verify if Employee Information text is present
        assert "Employee Information" in employee_info_page.text

        # Fill out the employee details
        driver.find_element(By.CSS_SELECTOR, "#employeeName").send_keys(employee_data["employeeName"])

        # Click on Gender dropdown and select option
        gender_dropdown = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Select Gender')]"))
        )
        gender_dropdown.click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(),'{employee_data['gender']}')]"))
        ).click()

        # Employee type selection
        emp_type_dropdown = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Select an Employee Type')]"))
        )
        emp_type_dropdown.click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(),'{employee_data['employeeType']}')]"))
        ).click()

        # Plant
        plant_dropdown = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Select a Plant']"))
        )
        plant_dropdown.click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(),'{employee_data['plant']}')]"))
        ).click()

        # Department
        department_dropdown = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)"))
        )
        department_dropdown.click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(),'{employee_data['department']}')]"))
        ).click()

        # Designation
        designation_dropdown = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)"))
        )
        designation_dropdown.click()
        # Click on the Designation dropdown and select the option
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f"//li[contains(@class, 'p-dropdown-item') and contains(text(), '{employee_data['designation']}')]")
            )
        ).click()

        # Select Date of Joining
        doj = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Select Date of Joining']")
        doj.send_keys(employee_data["dateOfJoining"])

        # Enter other details
        driver.find_element(By.CSS_SELECTOR, "#permanentAddress").send_keys(employee_data["permanentAddress"])
        driver.find_element(By.CSS_SELECTOR, "#communicationAddress").send_keys(employee_data["communicationAddress"])
        driver.find_element(By.CSS_SELECTOR, "#contactNumber1").send_keys(employee_data["contactNumber1"])
        driver.find_element(By.CSS_SELECTOR, "#contactNumber2").send_keys(employee_data["contactNumber2"])
        driver.find_element(By.CSS_SELECTOR, "#emergencyContact").send_keys(employee_data["emrtcontact"])
        driver.find_element(By.CSS_SELECTOR, "#email1").send_keys(employee_data["email"])
        driver.find_element(By.CSS_SELECTOR, "#aadharNumber").send_keys(employee_data["aadharNumber"])
        driver.find_element(By.CSS_SELECTOR, "#panNumber").send_keys(employee_data["panNumber"])

        bank_dropdown = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='p-field'] span[class='p-dropdown-label p-inputtext p-placeholder']"))
        )
        bank_dropdown.click()

        # Click on the Bank Name option
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f"//li[contains(@class, 'p-dropdown-item') and contains(text(), '{employee_data['bankName']}')]")
            )
        ).click()

        driver.find_element(By.CSS_SELECTOR, "#ifscCode").send_keys(employee_data["ifscCode"])
        driver.find_element(By.CSS_SELECTOR, "#bankAccountNumber").send_keys(employee_data["bankAccountNumber"])

        # Save the record
        driver.find_element(By.CSS_SELECTOR, "#save").click()

        print(f"Employee {employee_data['employeeName']} created successfully.")

    except TimeoutException as e:
        print(f"An element was not found in the expected time frame for employee {employee_data['employeeName']}:", e)
    except Exception as e:
        print(f"An error occurred for employee {employee_data['employeeName']}:", e)

    # Add a delay if needed
    time.sleep(5)

# Quit the browser
driver.quit()