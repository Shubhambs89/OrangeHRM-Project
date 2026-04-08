from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_items_xpath = "//ul[@class='oxd-main-menu']//li//span"

        #specific locators for each menu item
        self.menu_admin = (By.XPATH, "//span[text()='Admin']")
        self.menu_pim = (By.XPATH, "//span[text()='PIM']")
        self.menu_leave = (By.XPATH, "//span[text()='Leave']")
        self.menu_time = (By.XPATH, "//span[text()='Time']")
        self.menu_recruitment = (By.XPATH, "//span[text()='Recruitment']")
        self.menu_my_info = (By.XPATH, "//span[text()='My Info']")
        self.menu_performance = (By.XPATH, "//span[text()='Performance']")
        self.menu_dashboard = (By.XPATH, "//span[text()='Dashboard']")
        self.menu_maintenance = (By.XPATH, "//span[text()='Maintenance']")

    def get_menu_list(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, self.menu_items_xpath)))
        elements = self.driver.find_elements(By.XPATH, self.menu_items_xpath)
        menu_text_list = [el.get_attribute("textContent").strip() for el in elements]

        #Clearing the empty strings
        menu_text_list = [item for item in menu_text_list if item]
        print(f"DEBUG: Found menu items: {menu_text_list}")
        return menu_text_list

    def is_menu_item_clickable(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        return element.is_displayed()

    def click_maintenance(self):
        self.driver.find_element(*self.menu_maintenance).click()