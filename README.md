# Selenium Automation for GEP Rules Engine

## 📌 Project Description

This project automates the login and rule management process for multiple users in the GEP Rules Engine using Selenium WebDriver. The script:

- Logs in with multiple user accounts.
- Navigates to the Rules Engine page dynamically based on `clientName`.
- Uploads rule files.
- Adjusts page settings and selects rules.
- Activates selected rules and handles notifications.
- Logs out and repeats the process for the next user.

## 🚀 Features

- ✅ Automated login and navigation.
- ✅ Dynamic handling of multiple users.
- ✅ File upload and page adjustments.
- ✅ Modal detection and interaction.
- ✅ Automatic logout after execution.

## 🛠️ Installation & Setup

### 1️⃣ Prerequisites

Ensure you have the following installed:

- **Python (>=3.8)** → [Download Here](https://www.python.org/downloads/)
- **Google Chrome** → [Download Here](https://www.google.com/chrome/)
- **ChromeDriver** → [Download Here](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### 2️⃣ Install Required Dependencies

Run the following command to install dependencies:

```bash
pip install selenium
```

### 3️⃣ Configure ChromeDriver

Ensure ChromeDriver is in your system PATH. If not, place it in the project directory and specify its path in the script.

### 📌 Usage Guide

### Run the Script

Edit the users list in the script to add user credentials.

Ensure the `UPLOAD_FILE_PATH` is set correctly.

Run the script using:

```bash
python automation_script.py
```

### ⚙️ Configuration

#### User Credentials

Modify the users list in the script with the correct username, password, and client name:

```python
users = [
    {"username": "user1@example.com", "password": "password1", "clientName": "clientA"},
    {"username": "user2@example.com", "password": "password2", "clientName": "clientB"},
]
```

#### File Upload Path

Ensure the rule file is in the correct path and update:

```python
UPLOAD_FILE_PATH = "utils/upload/rules.json"
```

## 🛠️ Troubleshooting

### 1️⃣ WebDriver Issues

If you get an error related to ChromeDriver:

- Ensure ChromeDriver version matches your Chrome version.
- Reinstall ChromeDriver and place it in the system PATH.

### 2️⃣ Element Not Found Errors

- Check if the XPaths in the script match the latest version of the web page.
- Increase the WebDriverWait timeout if the page loads slowly.

### 3️⃣ File Upload Not Working

- Verify that the file path exists.
- Ensure the input field type is file and supports Selenium’s `.send_keys()` method.

## 👤 Author

**Shubham Trivedi**  
🚀 Passionate about automation and software testing.  
📧 Reach me at: [shubham.trivedi@gep.com](mailto:shubham.trivedi@gep.com)

## 📝 License

This project is licensed under the MIT License.

## 🌟 Acknowledgments

- Selenium WebDriver for making automation easy.
- GEP Team for providing the test environment.
- Open-source contributors for their amazing work!

📢 Found this project useful? Give it a ⭐ on GitHub!