import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

        #Creation Locators
        self.add_button = (By.XPATH, "//button[contains(.,'Add')]")
        self.user_role_dropdown = (By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
        self.status_dropdown = (By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")
        self.employee_name_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.username_input = (By.XPATH, "(//input[contains(@class, 'oxd-input')])[2]")
        self.password_input = (By.XPATH, "(//input[@type='password'])[1]")
        self.confirm_password_input = (By.XPATH, "(//input[@type='password'])[2]")
        self.save_button = (By.XPATH, "//button[@type='submit']")

        #Search Locators
        self.search_username_input = (By.XPATH, "//div[label[text()='Username']]//following-sibling::div//input")
        self.search_button = (By.XPATH, "//button[@type='submit']")
        self.cell_username = (By.XPATH, "//div[@role='table']//div[@role='row'][1]//div[@role='cell'][2]")

    def create_user(self, emp_hint, new_user, new_pwd):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()

        #Select User Role: Admin
        self.wait.until(EC.element_to_be_clickable(self.user_role_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Admin')]"))).click()

        #Employee Name using hint
        emp_field = self.wait.until(EC.visibility_of_element_located(self.employee_name_input))
        emp_field.send_keys(emp_hint)
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//div[1]"))).click()

        #Status: Enabled
        self.wait.until(EC.element_to_be_clickable(self.status_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Enabled')]"))).click()

        #Credentials
        self.driver.find_element(*self.username_input).send_keys(new_user)
        self.driver.find_element(*self.password_input).send_keys(new_pwd)
        self.driver.find_element(*self.confirm_password_input).send_keys(new_pwd)

        #Save and Wait for Success
        self.driver.find_element(*self.save_button).click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-toast")))

    def search_for_user(self, username):

        search_field = self.wait.until(EC.visibility_of_element_located(self.search_username_input))
        search_field.clear()
        search_field.send_keys(username)
        self.driver.find_element(*self.search_button).click()
        time.sleep(2)

    def get_first_result_username(self):
        return self.wait.until(EC.visibility_of_element_located(self.cell_username)).text

    def get_top_nav_items(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//nav[@aria-label='Topbar Menu']")))
        items = self.driver.find_elements(By.XPATH, "//nav[@aria-label='Topbar Menu']//li")
        return [item.text.strip() for item in items if item.text.strip() != ""]