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

    # Enter employee name
    driver.find_element(By.CSS_SELECTOR, "#employeeName").send_keys("Automation user")

    # Click on Gender dropdown to expand it
    gender_dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Select Gender')]"))
    )
    gender_dropdown.click()

    # Click on the Male option
    male_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Male')]"))
    )
    male_option.click()

    # Employee type selection
    emp_type_dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Select an Employee Type')]"))
    )
    emp_type_dropdown.click()

    dropdown_wrapper = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, ".//div[contains(@class,'p-dropdown-items-wrapper')]"))
    )

    emp_type_list = dropdown_wrapper.find_elements(By.XPATH, ".//li[contains(@class, 'p-dropdown-item')]")
    emp_type_text_list = [item.text for item in emp_type_list]

    for item in emp_type_list:
        if item.text == "Management":
            item.click()
            break

    # Plant
    plant_dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Select a Plant']"))
    )
    plant_dropdown.click()

    plant_list_wrapper = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".p-dropdown-items-wrapper"))
    )

    plant_list = plant_list_wrapper.find_elements(By.XPATH, ".//li[contains(@class, 'p-dropdown-item')]")
    plant_text_list = [plant.text for plant in plant_list]

    print(plant_text_list)

    for plant in plant_list:
        if plant.text == "b":
            plant.click()
            break

    # Department
    department_dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]"))
    )
    department_dropdown.click()

    department_list_wrapper = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".p-dropdown-items-wrapper"))
    )

    department_list = department_list_wrapper.find_elements(By.XPATH, ".//li[contains(@class, 'p-dropdown-item')]")
    department_text_list = [department.text for department in department_list]

    print(department_text_list)

    for department in department_list:
        if department.text == "Sales":
            department.click()
            break
    # designation
    designation_dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)"))
    )
    designation_dropdown.click()

    designation_list_wrapper = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".p-dropdown-items-wrapper"))
    )

    designation_list = designation_list_wrapper.find_elements(By.CSS_SELECTOR, ".p-dropdown-item")
    designation_text_list = [designation.text for designation in designation_list]

    print(designation_text_list)

    for designation in designation_list:
        if designation.text == "VP":
            designation.click()
            break

    doj = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Select Date of Joining']")
    doj.send_keys("10-07-2024")

# Communication detail

# Entering other details
    driver.find_element(By.CSS_SELECTOR, "#permanentAddress").send_keys("abcd")
    driver.find_element(By.CSS_SELECTOR, "#communicationAddress").send_keys("pqr")
    driver.find_element(By.CSS_SELECTOR, "#contactNumber1").send_keys("8999999999")
    driver.find_element(By.CSS_SELECTOR, "#contactNumber2").send_keys("8999999999")
    driver.find_element(By.CSS_SELECTOR, "#emergencyContact").send_keys("8999999999")
    driver.find_element(By.CSS_SELECTOR, "#email1").send_keys("salesautomation@yopmail.com")
    driver.find_element(By.CSS_SELECTOR, "#aadharNumber").send_keys("998888776655")
    driver.find_element(By.CSS_SELECTOR, "#panNumber").send_keys("LPPPP0871J")
    driver.find_element(By.CSS_SELECTOR,"#ifscCode").send_keys("ABCD0123450")
    driver.find_element(By.CSS_SELECTOR,"#bankAccountNumber").send_keys("8884447676")

#     Save action

    driver.find_element(By.CSS_SELECTOR,"#save").click()

except TimeoutException as e:
    print("An element was not found in the expected time frame:", e)
except Exception as e:
    print("An error occurred:", e)
finally:
    time.sleep(5)
    driver.quit()