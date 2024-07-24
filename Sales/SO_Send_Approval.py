import time
import logging
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, NoSuchElementException

# Initialize the logger
logging.basicConfig(filename='sales_order_automation.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

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

# Set up a range for iterations
num_sales_orders = 10  # Example: Change this number as needed

for order_number in range(1, num_sales_orders + 1):
    try:
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

        # Enter details like customer name, transporter, etc.
        customer_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Select Customer']"))
        )
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
        Cust_PO = f"PO{order_number:04d}"  # Unique customer PO for each iteration, formatted as PO0001, PO0002, etc.
        driver.find_element(By.CSS_SELECTOR, "#customerPONumber").send_keys(Cust_PO)
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Select Customer PO Date']").send_keys('01-06-2024')

        # Add items in the sales order
        num_items = 2  # Example: Change this number as needed

        for i in range(num_items):
            # Retry logic for clicking the add item button
            add_item_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Add Item'] span[class='p-button-label p-c']"))
            )
            while True:
                try:
                    add_item_button.click()
                    break
                except ElementClickInterceptedException:
                    time.sleep(1)

            # Select product type (example)
            driver.find_element(By.CSS_SELECTOR,
                                "body > div:nth-child(18) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(3)").click()

            # Wait for dropdown options to appear
            time.sleep(1)
            dropdown_type_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item")))

            # Select desired product type from dropdown
            for result in dropdown_type_results:
                if "Top loading Arm" in result.text:
                    result.click()
                    break

            # Product
            driver.find_element(By.CSS_SELECTOR, "#product").send_keys("Loading arms")

            # Order type
            order_type = driver.find_element(By.CSS_SELECTOR,
                                             "body > div:nth-child(18) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(3)")
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

            # Description
            driver.find_element(By.CSS_SELECTOR, "#description").send_keys("Marine loading arm")

            # Unit rate
            driver.find_element(By.CSS_SELECTOR, "#unitRate").send_keys("50000000")

            # Extended rate
            driver.find_element(By.CSS_SELECTOR, "#extendedRate").send_keys("50000100")

            # Quantity
            driver.find_element(By.CSS_SELECTOR, "#quantity").send_keys("5")

            # Delivery type
            delivery_type = driver.find_element(By.CSS_SELECTOR, "div[class='grid '] span[class='p-dropdown-label p-inputtext p-placeholder']")
            delivery_type.click()

            # Wait for dropdown options to appear
            time.sleep(1)
            dropdown_type_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item")))

            # Select desired product type from dropdown
            for result in dropdown_type_results:
                if "Longest Lead Time of an Item = Delivery Date of Product" in result.text:
                    result.click()
                    break
            driver.find_element(By.CSS_SELECTOR,"input[placeholder='Select Delivery Date']").click()

            element_to_double_click = driver.find_element(By.CSS_SELECTOR, "td[aria-label='24']")

            # Create an ActionChains object
            actions = ActionChains(driver)

            # Perform double-click on the element
            actions.double_click(element_to_double_click).perform()

            # Optional: Add a small delay for demonstration purposes
            time.sleep(1)

            driver.find_element(By.CSS_SELECTOR, "#qualityRemark").send_keys("Must tested with Iron")

            # Optional: Add a small delay between iterations
            time.sleep(1)

            # Save item
            driver.find_element(By.XPATH, "//button[@aria-label='Save']").click()
            time.sleep(1)

        # Checklist
        Check_list = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Checklist']"))
        )
        Check_list.click()

        time.sleep(1)

        # Checklist check one by one
        driver.find_element(By.CSS_SELECTOR, ".p-checkbox-box[data-p-highlight='false'][data-p-disabled='false']").click()
        driver.find_element(By.CSS_SELECTOR,
                            ".p-checkbox-box[data-p-highlight='false'][data-p-disabled='false']").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR,
                            "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)").click()
        driver.find_element(By.XPATH,
                            "//div[contains(@data-p-disabled,'false')]//div[contains(@data-p-highlight,'false')]").click()
        driver.find_element(By.XPATH,
                            "//div[@class='p-checkbox-box']").click()
        driver.find_element(By.CSS_SELECTOR,
                            ".p-checkbox-box[data-p-highlight='false'][data-p-disabled='false']").click()
        driver.find_element(By.CSS_SELECTOR,
                            ".p-checkbox-box[data-p-highlight='false'][data-p-disabled='false']").click()
        driver.find_element(By.CSS_SELECTOR,
                            ".p-checkbox-box[data-p-highlight='false'][data-p-disabled='false']").click()
        driver.find_element(By.CSS_SELECTOR,
                            ".p-checkbox-box[data-p-highlight='false'][data-p-disabled='false']").click()
        driver.find_element(By.XPATH,
                            "//div[contains(@data-p-disabled,'false')]//div[contains(@data-p-highlight,'false')]").click()
        driver.find_element(By.XPATH,
                            "//div[contains(@data-p-disabled,'false')]//div[contains(@data-p-highlight,'false')]").click()
        driver.find_element(By.XPATH,
                            "//div[contains(@data-p-disabled,'false')]//div[contains(@data-p-highlight,'false')]").click()

        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Save']").click()

        # Assert whether the created Customer PO is showing in the listing or not
        # Wait for the table to load and locate the table row elements that contain the Customer PO numbers
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))

        def get_po_list():
            try:
                list_of_PO_elements = driver.find_elements(By.CSS_SELECTOR, "tbody tr td:nth-child(2)")
                return [element.text for element in list_of_PO_elements]
            except StaleElementReferenceException:
                return get_po_list()

        # Get the list of POs
        list_of_PO = get_po_list()

        # Print the list for debugging
        logging.info(f"List of POs: {list_of_PO}")

        # Check if the Customer PO is in the list
        if Cust_PO in list_of_PO:
            logging.info(f"Success: SO created successfully with PO {Cust_PO}")
        else:
            logging.error(f"Error: SO with PO {Cust_PO} not created")

        # Optional: Add a small delay before starting the next iteration
        time.sleep(1)

    except NoSuchElementException as e:
        logging.error(f"NoSuchElementException encountered: {e}")
        continue
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        continue

# Close the WebDriver
driver.quit()