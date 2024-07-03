import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
email_input.send_keys("hrAdmin")
password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
password.send_keys("Pass@1234")  # Add the correct password here
login_button = driver.find_element(By.CSS_SELECTOR, ".p-5.align-items-center.surface-900.text-white.p-button.p-component.p-button-icon-only.p-button-rounded")
try:
    login_button.click()
    print("Login successful")
except Exception as e:
    print("Login failed:", e)

# Wait until Master menu appears
master_menu = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > div:nth-child(1) > a:nth-child(1) > span:nth-child(1)"))
)

# Click on Master menu
master_menu.click()

# Click on Employee Master submenu
employee_master_submenu = driver.find_element(By.CSS_SELECTOR, "li[aria-label='Employee master'] span[class='p-menuitem-text']")
employee_master_submenu.click()

# Click on New Employee button
new_employee_button = driver.find_element(By.CSS_SELECTOR, "#addNewEmployee")
new_employee_button.click()

# Wait for the Employee Information page to load
employee_info_page = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Employee Information')]"))
)
time.sleep(2)
# Assertion to verify if Employee Information text is present
assert "Employee Information" in employee_info_page.text

# Enter employee name
driver.find_element(By.CSS_SELECTOR, "#employeeName").send_keys("Automation user")

# Click on Gender dropdown to expand it
gender_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Select Gender')]"))
)
gender_dropdown.click()

# Click on the Male option
male_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Male')]"))
)
male_option.click()

# Employee type selection
# Click on Employee Type dropdown to expand it
emp_type_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Select an Employee Type')]"))
)
emp_type_dropdown.click()

# Find the dropdown wrapper that contains the list items
dropdown_wrapper = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, ".//div[contains(@class,'p-dropdown-items-wrapper')]"))
)

# Find all the list item elements within this wrapper
emp_type_list = dropdown_wrapper.find_elements(By.XPATH, ".//li[contains(@class, 'p-dropdown-item')]")

# Extract the text from each list item and store it into a list
emp_type_text_list = [item.text for item in emp_type_list]

# Optionally, click on the Manager option if it is present
for item in emp_type_list:
    if item.text == "Management":
        item.click()
        break

# Plant
plant_dropdown = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Select a Plant']"))
)
plant_dropdown.click()

# Wait for the plant dropdown options to appear
plant_list_wrapper = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".p-dropdown-items-wrapper"))
)

# Find all the list item elements within this wrapper
plant_list = plant_list_wrapper.find_elements(By.XPATH, ".//li[contains(@class, 'p-dropdown-item')]")

# Extract the text from each list item and store it into a list
plant_text_list = [plant.text for plant in plant_list]

# Print the list of plants
print(plant_text_list)

# Optionally, click on the specific plant option if it is present
for plant in plant_list:
    if plant.text == "b":  # Replace "b" with the actual plant name you want to select
        plant.click()
        break
    else:
        print("No plant found")

# Department
department_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Select']"))
)
department_dropdown.click()

# Wait for the department dropdown options to appear
department_list_wrapper = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".p-dropdown-items-wrapper"))
)

# Find all the list item elements within this wrapper
department_list = department_list_wrapper.find_elements(By.XPATH, ".//li[contains(@class, 'p-dropdown-item')]")

# Extract the text from each list item and store it into a list
department_text_list = [department.text for department in department_list]

# Print the list of departments
print(department_text_list)

# Optionally, click on the specific department option if it is present
for department in department_list:
    if department.text == "Sales":  # Replace "Sales" with the actual department name you want to select
        department.click()
        break

time.sleep(5)

designation_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='p-fluid pt-2'] span[class='p-dropdown-label p-inputtext p-placeholder']"))
)
designation_dropdown.click()

# Wait for the designation dropdown options to appear
designation_list_wrapper = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".p-dropdown-items-wrapper"))
)

# Find all the list item elements within this wrapper
designation_list = designation_list_wrapper.find_elements(By.CSS_SELECTOR, ".p-dropdown-item")

# Extract the text from each list item and store it into a list
designation_text_list = [designation.text for designation in designation_list]

# Print the list of designations
print(designation_text_list)

# Optionally, click on the specific designation option if it is present
for designation in designation_list:
    if designation.text == "VP":  # Replace "Your_Designation_Name" with the actual designation name you want to select
        designation.click()
        break


time.sleep(5)

# Quit the browser
driver.quit()
