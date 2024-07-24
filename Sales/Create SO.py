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

# Set implicit wait
driver.implicitly_wait(10)

# Find the login input fields and enter credentials
username = driver.find_element(By.CSS_SELECTOR, "#name")
username.send_keys("SalesExecutive")

password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
password.send_keys("Pass@1234")

# Find and click the login button
login_button = driver.find_element(By.CSS_SELECTOR, ".p-5")
login_button.click()

# Wait for the page to load after login (optional)
# time.sleep(2)  # Consider using WebDriverWait instead

# Redirect to sales order page
sales_order_menu_item = driver.find_element(By.CSS_SELECTOR, "li[aria-label='Sales Order'] span[class='p-menuitem-text']")
sales_order_menu_item.click()

# Wait for the page to load (optional)
# time.sleep(2)  # Consider using WebDriverWait instead

# Click 'Create Sales Order' button
create_so_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Create Sales Order'] span[class='p-button-label p-c']")
create_so_button.click()

# Wait for elements to load (optional)
# time.sleep(2)  # Consider using WebDriverWait instead

# Enter details like customer name, transporter, etc.
customer_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Select Customer']")
customer_input.send_keys("NHPC")

# Wait for dropdown options to appear
wait = WebDriverWait(driver, 10)
dropdown_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul[role='listbox'] li")))

# Select desired customer from dropdown
for result in dropdown_results:
    if "NHPC" in result.text:
        result.click()
        break

# Continue with other inputs like transporter, mode of transport, etc.
driver.find_element(By.CSS_SELECTOR, "#transporter").send_keys("VRL")
driver.find_element(By.CSS_SELECTOR, "#modeOfTransport").send_keys("Air")
driver.find_element(By.CSS_SELECTOR, "#destination").send_keys("Pune")
driver.find_element(By.CSS_SELECTOR, "#customerPONumber").send_keys("PO00001")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Select Customer PO Date']").send_keys('01-06-2024')

# Add an item
add_item_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Add Item'] span[class='p-button-label p-c']")
add_item_button.click()

# Select product type (example)
driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(17) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4)").click()
# Wait for dropdown options to appear
time.sleep(1)
dropdown_type_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item")))

# Select desired product type from dropdown
for result in dropdown_type_results:
    if "Top Loading arm" in result.text:
        result.click()
        break

# Product

driver.find_element(By.CSS_SELECTOR,"#product").send_keys("Top Loading arm")

# Order type

order_type = driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(17) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4)")
order_type.click()

# Wait for dropdown options to appear
time.sleep(1)
dropdown_type_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item")))

# Select desired product type from dropdown
for result in dropdown_type_results:
    if "Overseas" in result.text:
        result.click()
        break
time.sleep(2)
# description

driver.find_element(By.CSS_SELECTOR,"#description").send_keys("Marine loading arm")

# Unit rate

driver.find_element(By.CSS_SELECTOR,"#unitRate").send_keys("50000000")

# Exrended rate

driver.find_element(By.CSS_SELECTOR,"#extendedRate").send_keys("50000100")

# Qty
driver.find_element(By.CSS_SELECTOR,"#quantity").send_keys("5")

# Delivery type
delivery_type = driver.find_element(By.CSS_SELECTOR,"div[aria-label='Select Delivery Type']")
delivery_type.click()

# Wait for dropdown options to appear
time.sleep(1)
dropdown_type_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item")))

# Select desired product type from dropdown
for result in dropdown_type_results:
    if "Delivery Date based on “Approval of Documents”" in result.text:
        result.click()
        break

# Delivery days

driver.find_element(By.ID,"deliveryDays").send_keys("10")

driver.find_element(By.CSS_SELECTOR,"#qualityRemark").send_keys("Must tested with Iron")

# Submit

driver.find_element(By.CSS_SELECTOR,"button[aria-label='Save'] span[class='p-button-label p-c']").click()

# save & draft

driver.find_element(By.CSS_SELECTOR,"button[aria-label='Save As Draft']").click()


# Close the WebDriver
driver.quit()
