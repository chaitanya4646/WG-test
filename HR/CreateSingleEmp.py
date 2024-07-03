import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def login(driver, email, password):
    try:
        driver.get("https://wg.bicsinfotech.com")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#name'))).send_keys(email)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))).send_keys(password)
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.p-5.align-items-center.surface-900.text-white.p-button.p-component.p-button-icon-only.p-button-rounded')))
        login_button.click()
        logger.info("Logged in successfully.")
    except TimeoutException as e:
        logger.error("Timeout occurred during login: %s", e)
        driver.quit()

def main():
    driver = init_driver()
    try:
        login(driver, "hrAdmin", "Pass@1234")

        # Wait until Master menu appears
        logger.info("Waiting for Master menu...")
        master_menu = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Master')]")))
        master_menu.click()
        logger.info("Clicked on Master menu.")

        # Click on Employee Master submenu
        logger.info("Waiting for Employee Master submenu...")
        employee_master_submenu = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Employee master")))
        employee_master_submenu.click()
        logger.info("Clicked on Employee Master submenu.")

        # Click on New Employee button
        logger.info("Waiting for New Employee button...")
        new_employee_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='New Employee']")))
        new_employee_button.click()
        logger.info("Clicked on New Employee button.")

        # Wait for the Employee Information page to load
        logger.info("Waiting for Employee Information page...")
        employee_info_page = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Employee Information')]")))
        logger.info("Employee Information page loaded.")

        # Assertion to verify if Employee Information text is present
        assert "Employee Information" in employee_info_page.text

        # Enter employee name
        driver.find_element(By.CSS_SELECTOR, "#employeeName").send_keys("Automation user")
        logger.info("Entered employee name.")

        # Click on Gender dropdown to expand it
        logger.info("Waiting for Gender dropdown...")
        gender_dropdown = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Select Gender'] svg")))
        gender_dropdown.click()
        logger.info("Clicked on Gender dropdown.")

        # Selecting the gender
        logger.info("Waiting for Male option...")
        male_option = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'p-dropdown-item')]//span[contains(text(), 'Male')]")))
        male_option.click()
        logger.info("Selected Male option.")

        # Employee type selection
        logger.info("Waiting for Employee Type dropdown...")
        emp_type_dropdown = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Select an Employee Type')]")))
        emp_type_dropdown.click()
        logger.info("Clicked on Employee Type dropdown.")

        # Retrieve all elements matching the XPath "//*[@class='p-dropdown-item']"
        emp_type_elements = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@class='p-dropdown-item']")))

        # Create an empty list to store the text values of the elements
        emp_type_texts = []

        # Iterate through each element in the list
        for emp_type_element in emp_type_elements:
            # Retrieve the text of the element
            emp_type_text = emp_type_element.text.strip()
            # Append the text to the list
            emp_type_texts.append(emp_type_text)

        # Print the list of text values
        logger.info("Text values of Employee Type elements: %s", emp_type_texts)

        # Perform further actions based on the text values, for example:
        # Click on the element with text "Quality" if it exists
        if "Quality" in emp_type_texts:
            quality_element = emp_type_elements[emp_type_texts.index("Quality")]
            quality_element.click()
            logger.info("Selected Quality employee type.")
        else:
            logger.error("Quality employee type not found.")

        # You can add more conditions and actions based on the text values as needed.

        # Plant selection
        logger.info("Waiting for Plant dropdown...")
        plant_dropdown = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Select a Plant')]")))
        plant_dropdown.click()
        logger.info("Clicked on Plant dropdown.")

        # Selecting the plant
        logger.info("Waiting for Plant option...")
        plant_option = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'p-dropdown-item')]//span[contains(text(), 'b')]")))
        plant_option.click()
        logger.info("Selected plant 'b'.")

        # Department selection
        logger.info("Waiting for Department dropdown...")
        department_dropdown = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Select'] svg")))
        department_dropdown.click()
        logger.info("Clicked on Department dropdown.")

        # Retrieve all elements matching the XPath "//*[@class='p-dropdown-item']"
        department_elements = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,".p-dropdown-item")))

        # Create an empty list to store the text values of the elements
        department_texts = []

        # Iterate through each element in the list
        for department_element in department_elements:
            # Retrieve the text of the element
            department_text = department_element.text.strip()
            # Append the text to the list
            department_texts.append(department_text)

        # Print the list of text values
        logger.info("Text values of Department elements: %s", department_texts)

        # Perform further actions based on the text values, for example:
        # Click on the element with text "Sales" if it exists
        if "Sales" in department_texts:
            sales_element = department_elements[department_texts.index("Sales")]
            sales_element.click()
            logger.info("Selected Sales department.")
        else:
            logger.error("Sales department not found.")

        # You can add more conditions and actions based on the text values as needed.

        # Designation selection
        logger.info("Waiting for Designation dropdown...")
        designation_dropdown = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(3)")))
        designation_dropdown.click()
        logger.info("Clicked on Designation dropdown.")
        time.sleep(2)
        # Retrieve all elements matching the XPath "//*[@class='p-dropdown-item']"
        designation_elements = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-dropdown-item")))

        # Create an empty list to store the text values of the elements
        designation_texts = []

        # Iterate through each element in the list
        for designation_element in designation_elements:
            try:
                # Retrieve the text of the element
                designation_text = designation_element.text.strip()
                # Append the text to the list
                designation_texts.append(designation_text)
            except StaleElementReferenceException:
                # If the element is stale, re-locate it
                designation_element = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@class='p-dropdown-item']")))
                designation_text = designation_element.text.strip()
                designation_texts.append(designation_text)

        # Print the list of text values
        logger.info("Text values of Designation elements: %s", designation_texts)

        # Perform further actions based on the text values, for example:
        # Click on the element with text "VP" if it exists
        if "VP" in designation_texts:
            vp_index = designation_texts.index("VP")
            vp_element = designation_elements[vp_index]
            vp_element.click()
            logger.info("Selected VP designation.")
        else:
            logger.error("VP designation not found.")

        # Date of joining

        # calendar_icon = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Select Date of Joining']")
        # calendar_icon.click()
        # logger.info("Date picker opened")
        # time.sleep(2)
        # select_date = driver.find_element(By.XPATH,"//tbody/tr[1]/td[7]")
        # select_date.click()
        # select_date.click()
        # logger.info("Selected date")
        # time.sleep(5)

        # DOJ
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div/div[2]/div[3]/div/div[2]/span/input").send_keys('01-06-2024')

        # Permanent Address
        Permanent_address = driver.find_element(By.CSS_SELECTOR,"#permanentAddress")
        Permanent_address.send_keys("abcd")

        # Communication address
        comunication_addr = driver.find_element(By.CSS_SELECTOR,"#communicationAddress")
        comunication_addr.send_keys("pqr")

        # Conatct no1

        contact_no = driver.find_element(By.CSS_SELECTOR,"#contactNumber1")
        contact_no.send_keys("1818181888")

        # Contact no2

        contact_no2 = driver.find_element(By.CSS_SELECTOR,"#contactNumber2")
        contact_no2.send_keys("8787878788")

        # email

        email = driver.find_element(By.CSS_SELECTOR,"#email1")
        email.send_keys("automation@yopmail.com")


        # Adharcard
        Adharcard = driver.find_element(By.CSS_SELECTOR,"#aadharNumber")
        Adharcard.send_keys("111111111111")
        logger.info("Entered adhar no")

        #Pancard
        Pancard = driver.find_element(By.CSS_SELECTOR,"#panNumber")
        Pancard.send_keys("ABCTY1234D")
        logger.info("entered PAN")

        #Bank Name
        bankname = driver.find_element(By.CSS_SELECTOR,"#bankName")
        bankname.send_keys("HDFC")
        logger.info("Entered bank account")

        #IFSC
        ifsc = driver.find_element(By.CSS_SELECTOR,"#ifscCode")
        ifsc.send_keys("ABCD0123450")
        logger.info("IFSC entered")

        #UAN
        uanno = driver.find_element(By.CSS_SELECTOR,"#uanNumber")
        uanno.send_keys("122233232322")
        logger.info("UAN enetered")

        #ESIC
        esic = driver.find_element(By.CSS_SELECTOR,"#esicNumber")
        esic.send_keys("11111111111111111")
        logger.info("ESIC entered")

        #account no
        accno = driver.find_element(By.CSS_SELECTOR,"#bankAccountNumber")
        accno.send_keys("122233232322")
        logger.info("Account no enetred")

        # submit form
        submit = driver.find_element(By.CSS_SELECTOR,"button[id='save'] span[class='p-button-label p-c']")
        submit.click()
        logger.info("Submitted form")

        time.sleep(3)

    except TimeoutException as e:
        logger.error("Timeout occurred during the process: %s", e)
    except NoSuchElementException as e:
        logger.error("Element not found: %s", e)
    except WebDriverException as e:
        logger.error("WebDriver exception occurred: %s", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
