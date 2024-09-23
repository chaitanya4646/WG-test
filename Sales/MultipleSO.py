import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

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
password.send_keys("Pass@123")

# Find and click the login button
login_button = driver.find_element(By.CSS_SELECTOR, ".p-5")
login_button.click()

# Set up a range for iterations
num_sales_orders = 1  # Example: Change this number as needed

for order_number in range(1, num_sales_orders + 1):
    # Redirect to sales order page
    sales_order_menu_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li[aria-label='Sales Order'] span[class='p-menuitem-text']"))
    )
    sales_order_menu_item.click()

    # Click 'Create Sales Order' button
    create_so_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Create Sales Order'] span[class='p-button-label p-c']"))
    )
    create_so_button.click()

    # Handle StaleElementReferenceException for IWO Type
    try:
        iwotype = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Select an IWO Type']"))
        )
        iwotype.click()

        iworesults = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item"))
        )

        for selectiwo in iworesults:
            if "Export" in selectiwo.text:
                selectiwo.click()
                break

    except StaleElementReferenceException:
        print("Stale element encountered, retrying...")

    salesperson = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Select an Sales Person']"))
    )
    salesperson.click()

    salespersonresult = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item"))
    )

    for sperson in salespersonresult:
        if "ssk" in sperson.text:
            sperson.click()
            break

    # Delivery term
    delivery_term = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Select an Delivery term']"))
    )
    delivery_term.click()

    delivery_terms = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item"))
    )

    for determ in delivery_terms:
        if "Ex Works (EXW)" in determ.text:
            determ.click()
            break

    # Enter customer details
    customer_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Select Customer']"))
    )
    customer_input.send_keys("Usa Customer")

    # Wait for dropdown options to appear and select desired customer
    dropdown_results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul[role='listbox'] li"))
    )
    for result in dropdown_results:
        if "Usa Customer" in result.text:
            result.click()
            break

    # Fill other fields
    driver.find_element(By.CSS_SELECTOR, "input[id='insurance,']").send_keys("WG")
    driver.find_element(By.CSS_SELECTOR, "input[id='contactPerson,']").send_keys("CSS")
    driver.find_element(By.CSS_SELECTOR, "#shippingAddress").send_keys("Nagar")
    driver.find_element(By.CSS_SELECTOR, "#qualityRemark").send_keys("T&C testing certificate")
    driver.find_element(By.CSS_SELECTOR, "#offerRemarks").send_keys("No")
    driver.find_element(By.CSS_SELECTOR, "#transporter").send_keys("VRL")
    driver.find_element(By.CSS_SELECTOR, "#modeOfTransport").send_keys("Air")
    driver.find_element(By.CSS_SELECTOR, "#destination").send_keys("Pune")
    Cust_PO = f"WSIL_SPAI12{order_number:04d}"  # Unique customer PO for each iteration
    driver.find_element(By.CSS_SELECTOR, "#customerPONumber").send_keys(Cust_PO)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Select Customer PO Date']").send_keys('01-06-2024')

    # Warranty term
    warrantyterms = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Select WarrantyTerm list']"))
    )
    warrantyterms.click()

    wresults = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item"))
    )

    for weterm in wresults:
        if "Option for Particular date should be there" in weterm.text:
            weterm.click()
            break

    # Add items in the sales order
    num_items = 5  # Example: Change this number as needed
    for i in range(num_items):
        add_item_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Add Item'] span[class='p-button-label p-c']"))
        )
        add_item_button.click()

        # Product type
        product_type = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='productType'] span[class='p-dropdown-label p-inputtext p-placeholder']"))
        )
        product_type.click()

        dropdown_type_results = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item"))
        )

        for result in dropdown_type_results:
            if "Bottom loading/ unloading Arm with Accessories" in result.text:
                result.click()
                break

        driver.find_element(By.CSS_SELECTOR, "#product").send_keys("Loading ARM with joints parts")
        driver.find_element(By.CSS_SELECTOR,"#service").send_keys("Oil")
        driver.find_element(By.CSS_SELECTOR, "#description").send_keys("Loading ARM with joints parts for oil product")
        driver.find_element(By.CSS_SELECTOR, "#unitRate").send_keys("500000")

        # Order type
        ordertype = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='orderType'] span[class='p-dropdown-label p-inputtext p-placeholder']"))
        )
        ordertype.click()

        ordertypes = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item"))
        )

        for orderresult in ordertypes:
            if "Service" in orderresult.text:
                orderresult.click()
                break

        # Quality checkbox (if applicable)
        docrequired = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='documentation'] div[class='p-checkbox-box']"))
        )
        docrequired.click()

        driver.find_element(By.CSS_SELECTOR, "#quantity").send_keys("2")
        time.sleep(2)
        # Delivery type
        deliverytype = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='deliveryType'] span[class='p-dropdown-label p-inputtext p-placeholder']"))
        )
        deliverytype.click()

        deliverytyresults = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item"))
        )

        for dtype in deliverytyresults:
            if "Delivery date based on approval of document" in dtype.text:
                dtype.click()
                break

        weeks = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#deliveryWeeks"))
        )
        weeks.send_keys("2")

        # Scroll to the qualityterms element before interacting
        qualityterms_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "(//textarea[@id='qualityRemark'])[2]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", qualityterms_element)
        qualityterms_element.send_keys("STANDERD TESTING")

        # Click save item button
        save_item_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#save"))
        )
        save_item_button.click()

    # checklist
    checklist_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#saveAsDraft"))
    )
    checklist_button.click()

    time.sleep(2)  # Adding a short delay to ensure the order is saved before moving to the next iteration

# Close the WebDriver
driver.quit()