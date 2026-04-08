import pytest
import csv
import os
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_csv_data(file_name):
    rows = []
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)
    with open(data_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append((row['Username'], row['Password']))
    return rows


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

# Test case 1 Login using csv
@pytest.mark.parametrize("user, pwd", get_csv_data("credentials.csv"))
def test_login_functionality(driver, user, pwd):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)

    login.enter_username(user)
    login.enter_password(pwd)

    #Valid Admin Login
    login.click_login()

    if user == "Admin" and pwd == "admin123":
        #SUCCESS PATH
        WebDriverWait(driver, 15).until(EC.url_contains("dashboard"))
        assert "dashboard" in driver.current_url.lower(), "Admin login failed!"
    else:
        #FAILURE PATH
        error_locator = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")
        error_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(error_locator))
        assert error_element.is_displayed(), "Error message not shown for invalid user!"
        assert "login" in driver.current_url.lower()