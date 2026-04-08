import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(("css selector", "button[type='submit']")))
    yield driver
    driver.quit()

# Test case 2 url accessibility
def test_case_2_url_accessibility(driver):
    current_url = driver.current_url.lower()

    assert "orangehrmlive.com" in current_url
    assert "login" in current_url

# Test case 3 login field visibility
def test_case_3_login_fields_visibility(driver):
    login = LoginPage(driver)
    assert login.is_username_field_visible(), "Username field is NOT visible"