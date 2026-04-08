import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield driver
    driver.quit()

# Test case 5 Create and Verify user
def test_case_5_create_and_verify_user(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    admin_pg = AdminPage(driver)
    wait = WebDriverWait(driver, 20)

    #Login as Admin
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    wait.until(EC.url_contains("dashboard"))

    #Navigate to Admin Menu
    wait.until(EC.element_to_be_clickable(dashboard.menu_admin)).click()

    #Creating a New User
    new_username = f"TestUser{int(time.time())}"
    admin_pg.create_user("a", new_username, "Password123!")

    #Logout
    login.logout()

    #Verify login with new user
    login.enter_username(new_username)
    login.enter_password("Password123!")
    login.click_login()

    #Final Validation
    wait.until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url.lower()