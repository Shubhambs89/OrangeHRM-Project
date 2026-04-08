from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)  # Increased wait time to 15s

        #Locators
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.forgot_password_link = (By.XPATH, "//p[normalize-space()='Forgot your password?']")

        #Reset Password Locators
        self.reset_username_input = (By.NAME, "username")
        self.reset_button = (By.XPATH, "//button[@type='submit']")

        #Logout Locators
        self.user_dropdown = (By.CLASS_NAME, "oxd-userdropdown-name")
        self.logout_link = (By.LINK_TEXT, "Logout")

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.user_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable(self.logout_link)).click()
        self.wait.until(EC.url_contains("login"))

    def get_current_url(self):
        return self.driver.current_url

    def is_username_field_visible(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_field)).is_displayed()

    def is_password_field_visible(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.password_field)).is_displayed()
        except:
            return False

    #Forgot Password Helpers
    def click_forgot_password(self):
        self.wait.until(EC.element_to_be_clickable(self.forgot_password_link)).click()

    def reset_password(self, username):
        #Input field to be ready
        user_input = self.wait.until(EC.element_to_be_clickable(self.reset_username_input))

        #Click and Clear using keyboard shortcuts
        user_input.click()
        user_input.send_keys(Keys.CONTROL + "a")
        user_input.send_keys(Keys.BACKSPACE)

        user_input.send_keys(username)
        user_input.send_keys(Keys.ENTER)

    def is_reset_page_displayed(self):
        try:
            return self.wait.until(EC.url_contains("requestPasswordResetCode"))
        except:
            return False