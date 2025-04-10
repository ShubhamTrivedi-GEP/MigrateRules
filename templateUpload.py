from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests 
import time
import os

# Constants
LOGIN_URL = "https://nexxeuat.gep.com"
UPLOAD_EXECUTIVE_SUMMARY_FILE_PATH = "utils/upload/Executive Summary - ICM&MI - All.docx"
UPLOAD_DETAIL_CATEGORY_SUMMARY_FILE_PATH = "utils/upload/Detail Category Summary - ICM&MI - All.docx"

# Define users list (Modify as needed)
users = [
    # {"username": "user2@example.com", "password": "password2", "clientName": "clientB"}
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
    
    upload_executive_file = os.path.abspath(UPLOAD_EXECUTIVE_SUMMARY_FILE_PATH)
    upload_detail_file = os.path.abspath(UPLOAD_DETAIL_CATEGORY_SUMMARY_FILE_PATH)
    # print(upload_file)
    print(f"\nStarting automation for: {user['username']} - Client: {user['clientName']}")
    try:
        # Step 1: Open login page
        driver.get(LOGIN_URL)

        # Step 2: Enter credentials and login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, USER_NAME))).send_keys(user["username"])
        driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(user["password"], Keys.RETURN)
        
        # Wait until page loads after login
        time.sleep(5)

        # Step 3: Retrieve `userInfo` data from the page
        user_info_script = "return window.userInfo;"  # JavaScript to get userInfo
        user_info = driver.execute_script(user_info_script)
        if user_info:
            # print("Retrieved userInfo:", user_info)
            # Access token and baseUrl from userInfo
            token = user_info.get("Token")
            base_url = user_info.get("LeoAPIBaseURL")
            subscription_key = user_info.get("LeoAPIMSubscriptionKey")
            # print(f"Token: {token}, Base URL: {base_url}, Subscription Key: {subscription_key}")

            # Prepare POST request
            api_endpoint = f"{base_url}/leo-cwb-coreservices-api/api/v2/Template/ConfigureExportTemplateWithFile"  # Replace with the actual API endpoint
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {token}",  # Use the token for authorization
                "Ocp-Apim-Subscription-Key": subscription_key
            }

            # For the first file (Execution Summary)
            try:
                with open(upload_executive_file, "rb") as file:
                    files = {
                        "file": file  # The key "file" matches the backend's expectation
                    }
                    data = {
                        "name": "Execution Summary",  # Replace with the actual value for "name"
                        "code": "0",  # Replace with the actual value for "code"
                    }
                    response = requests.post(api_endpoint, headers=headers, files=files, data=data)
                    if response.status_code == 200:
                        print("POST request successful:", response.json())
                    else:
                        print(f"POST request failed with status code {response.status_code}: {response.text}")
            except Exception as e:
                print(f"An error occurred while making the POST request for Execution Summary: {e}")

            # For the second file (Detail Category Report)
            try:
                with open(upload_detail_file, "rb") as file:
                    files = {
                        "file": file  # The key "file" matches the backend's expectation
                    }
                    data = {
                        "name": "Detail Category Report",  # Replace with the actual value for "name"
                        "code": "1",  # Replace with the actual value for "code"
                    }
                    response = requests.post(api_endpoint, headers=headers, files=files, data=data)
                    if response.status_code == 200:
                        print("POST request successful:", response.json())
                    else:
                        print(f"POST request failed with status code {response.status_code}: {response.text}")
            except Exception as e:
                print(f"An error occurred while making the POST request for Detail Category Report: {e}")
        else:
            print("userInfo is not available on the page.")

        # Additional steps...
        print("Automation Completed Successfully!")
        
    except Exception as e:
        print(f"An error occurred for {user['username']}: {e}")

    # Close browser for this user
    driver.quit()

print("\n✅ Automation completed for all users.")