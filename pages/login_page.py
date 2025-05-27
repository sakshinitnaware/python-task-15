from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as Svc
from webdriver_manager.chrome import ChromeDriverManager as CDM
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://v2.zenclass.in/login")
        self.wait = WebDriverWait(driver, 30)  
        self.USERNAME = (By.XPATH, "//input[@placeholder='Enter your mail']")
        self.PASSWORD = (By.XPATH, "//input[@placeholder='Enter your password ']")
        self.LOGIN_BUTTON = (By.XPATH, "//button[text()='Sign in']")
        self.ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'MuiFormHelperText-root') and contains(@class, 'Mui-error')]")
        self.LOGOUT_BUTTON = (By.XPATH, "//div[@class='user-avatar-menu' and text()='Log out']")
        self.PROFILE_MENU = (By.ID, "profile-click-icon")
        self.DASHBOARD_TEXT = (By.CSS_SELECTOR, 'p.header-name')

    def is_logout_button_enabled(self):
        close_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'custom-close-button') and @aria-label='Close popup']")))
        try:
            close_btn.click()
        except Exception as E :
            print("popup dint close",E)
        profile_menu = self.wait.until(EC.presence_of_element_located(self.PROFILE_MENU))
        profile_menu.click()
        return self.wait.until(EC.presence_of_element_located(self.LOGOUT_BUTTON)).is_enabled()

    def check_dashboard_text(self):
        return self.wait.until(EC.presence_of_element_located(self.DASHBOARD_TEXT))

    def logout(self):
        close_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'custom-close-button') and @aria-label='Close popup']")))
        try:
            close_btn.click()
        except Exception as E :
            print("popup dint close",E)
        profile_menu = self.wait.until(EC.presence_of_element_located(self.PROFILE_MENU))
        profile_menu.click()
        logout_button = self.wait.until(EC.presence_of_element_located(self.LOGOUT_BUTTON))
        if logout_button.is_enabled():
            logout_button.click()

    def enter_username(self, username):
        user= self.wait.until(EC.presence_of_element_located(self.USERNAME))
        user.send_keys(username)

    def username_field_enabled(self):
        return self.wait.until(EC.presence_of_element_located(self.USERNAME)).is_enabled()

    def enter_password(self, password):
        passw = self.wait.until(EC.presence_of_element_located(self.PASSWORD))
        passw.send_keys(password)

    def password_field_enabled(self):
        return self.wait.until(EC.presence_of_element_located(self.PASSWORD)).is_enabled()

    def click_login(self):
        login_button = self.wait.until(EC.presence_of_element_located(self.LOGIN_BUTTON))
        login_button.click()
    
    def is_login_button_clickable(self):
        return self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
    
    def error_msg(self) :
        try :
            msg = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
            return msg.is_displayed(), "Error message is not displayed"
        except TimeoutException:
            print("Error message not found within the timeout")
            return False# Import Selenium WebDriver for browser automation
from selenium import webdriver 
# Import By class to locate elements
from selenium.webdriver.common.by import By 
# Import WebDriverWait for explicit waits
from selenium.webdriver.support.ui import WebDriverWait
# Import expected conditions to define wait criteria
from selenium.webdriver.support import expected_conditions as EC
# Import Service class to initiate ChromeDriver
from selenium.webdriver.chrome.service import Service as Svc
# Import ChromeDriverManager to automatically manage driver binaries
from webdriver_manager.chrome import ChromeDriverManager as CDM
# Import Options to set browser options
from selenium.webdriver.chrome.options import Options
# Import TimeoutException to handle wait timeouts
from selenium.common.exceptions import TimeoutException



# Define the LoginPage class using the Page Object Model
class LoginPage:
    # Constructor to initialize the class with the driver
    def __init__(self, driver):
        # Store the WebDriver instance
        self.driver = driver
        # Open the Zen login page
        self.driver.get("https://v2.zenclass.in/login")
        # Set up explicit wait with 30 seconds timeout
        self.wait = WebDriverWait(driver, 30)  
        # Define the locator for the username field
        self.USERNAME = (By.XPATH, "//input[@placeholder='Enter your mail']")
        # Define the locator for the password field
        self.PASSWORD = (By.XPATH, "//input[@placeholder='Enter your password ']")
        # Define the locator for the login button
        self.LOGIN_BUTTON = (By.XPATH, "//button[text()='Sign in']")
        # Define the locator for the login error message
        self.ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'MuiFormHelperText-root') and contains(@class, 'Mui-error')]")
        # Define the locator for the logout button
        self.LOGOUT_BUTTON = (By.XPATH, "//div[@class='user-avatar-menu' and text()='Log out']")
        # Define the locator for the profile menu icon
        self.PROFILE_MENU = (By.ID, "profile-click-icon")
        # Define the locator for dashboard verification text
        self.DASHBOARD_TEXT = (By.CSS_SELECTOR, 'p.header-name')

    # Method to check if logout button is enabled after opening profile menu
    def is_logout_button_enabled(self):
        # Wait for and find the close popup button
        close_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'custom-close-button') and @aria-label='Close popup']")))
        try:
            # Attempt to close the popup
            close_btn.click()
        except Exception as E :
            # Print error if popup cannot be closed
            print("popup dint close",E)
        # Wait for and click the profile menu
        profile_menu = self.wait.until(EC.presence_of_element_located(self.PROFILE_MENU))
        profile_menu.click()
        # Check and return if the logout button is enabled
        return self.wait.until(EC.presence_of_element_located(self.LOGOUT_BUTTON)).is_enabled()

    # Method to return the dashboard text element after login
    def check_dashboard_text(self):
        return self.wait.until(EC.presence_of_element_located(self.DASHBOARD_TEXT))

    # Method to log out from the application
    def logout(self):
        # Wait for and find the close popup button
        close_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'custom-close-button') and @aria-label='Close popup']")))
        try:
            # Attempt to close the popup
            close_btn.click()
        except Exception as E :
            # Print error if popup cannot be closed
            print("popup dint close",E)
        # Wait for and click the profile menu
        profile_menu = self.wait.until(EC.presence_of_element_located(self.PROFILE_MENU))
        profile_menu.click()
        # Wait for the logout button and click if enabled
        logout_button = self.wait.until(EC.presence_of_element_located(self.LOGOUT_BUTTON))
        if logout_button.is_enabled():
            logout_button.click()

    # Method to input the username
    def enter_username(self, username):
        # Wait for username field and send input
        user= self.wait.until(EC.presence_of_element_located(self.USERNAME))
        user.send_keys(username)

    # Method to check if username field is enabled
    def username_field_enabled(self):
        return self.wait.until(EC.presence_of_element_located(self.USERNAME)).is_enabled()

    # Method to input the password
    def enter_password(self, password):
        # Wait for password field and send input
        passw = self.wait.until(EC.presence_of_element_located(self.PASSWORD))
        passw.send_keys(password)

    # Method to check if password field is enabled
    def password_field_enabled(self):
        return self.wait.until(EC.presence_of_element_located(self.PASSWORD)).is_enabled()

    # Method to click on the login button
    def click_login(self):
        # Wait for login button and click
        login_button = self.wait.until(EC.presence_of_element_located(self.LOGIN_BUTTON))
        login_button.click()
    
    # Method to check if the login button is clickable
    def is_login_button_clickable(self):
        return self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
    
    # Method to verify if error message is displayed for invalid login
    def error_msg(self) :
        try :
            # Wait for error message and return its visibility
            msg = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
            return msg.is_displayed(), "Error message is not displayed"
        except TimeoutException:
            # Print error if message does not appear in time
            print("Error message not found within the timeout")
            return False
