from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Constants
LOGIN_URL = "https://nexxeuat.gep.com"
UPLOAD_FILE_PATH = "utils/upload/rules.json"

# Define users list (Modify as needed)
users = [
    {"username": "user1@example.com", "password": "password1", "clientName": "clientA"},
    {"username": "user2@example.com", "password": "password2", "clientName": "clientB"},
]

# XPaths
USER_NAME = '//input[@id="UserName"]'
PASSWORD_FIELD = '//input[@id="Password"]'
LOGIN_BUTTON = '//input[@id="login"]'
TITLE = '//div[@id="breadcrumbDescriptionId"]'
USER_ICON = '//div[@id="user-image-border"]'
LOGOUT_BUTTON = '//button[@id="Platform_UserProfile_Logout"]'

# Run script for each user
for user in users:
    driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
    driver.maximize_window()
    
    upload_file = os.path.abspath(UPLOAD_FILE_PATH)
    print(f"\nStarting automation for: {user['username']} - Client: {user['clientName']}")
    
    # Step 1: Open login page
    driver.get(LOGIN_URL)

    # Step 2: Enter credentials and login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, USER_NAME))).send_keys(user["username"])
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(user["password"], Keys.RETURN)
    
    # Wait until page loads after login
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, TITLE)))
    time.sleep(5)

    # Step 3: Navigate to Rules Engine page (Dynamically setting clientName)
    RULES_ENGINE_URL = f"https://quantumuat.gep.com/{user['clientName']}/#/manage-rules-v2/categoryworkbench"
    driver.get(RULES_ENGINE_URL)
    time.sleep(5)

    # Upload file (Step 4)
    file_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    file_input.send_keys(upload_file)
    time.sleep(10)
    driver.refresh()
    time.sleep(5)

    # Step 5: Change page size to 100
    page_size_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='pagination-select']")))
    page_size_dropdown.click()
    page_size_dropdown.send_keys("100", Keys.RETURN)

    # Step 6: Click "Select All"
    select_all_checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='selectAllMangeRules']")))
    select_all_checkbox.click()

    # Step 7: Click "Active"
    active_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//toggle-switch[@class='toggle-switch']")))
    active_button.click()

    # Step 8: Check for notification modal and click "Back" if present
    try:
        modal_footer = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "notification-modal-footer"))
        )
        back_button = modal_footer.find_element(By.XPATH, "//span[contains(@class,'plain-btn') and text()='Back']")
        back_button.click()
        print("Clicked 'Back' button.")
    except:
        print("No notification modal found, continuing execution...")

    print("Automation Completed Successfully!")

    # Step 9: Logout process
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, USER_ICON))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, LOGOUT_BUTTON))).click()
    print(f"Logged out successfully for: {user['username']}")

    # Close browser for this user
    driver.quit()

print("\n✅ Automation completed for all users.")
