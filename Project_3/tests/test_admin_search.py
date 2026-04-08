import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")

    login = LoginPage(driver)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()
    yield driver
    driver.quit()

# Test case 6 Search user
def test_case_6_search_user_in_admin(driver):
    dashboard = DashboardPage(driver)
    admin_pg = AdminPage(driver)

    #Navigate to Admin
    driver.find_element(*dashboard.menu_admin).click()

    #Search for the default 'Admin' user
    target_user = "Admin"
    admin_pg.search_for_user(target_user)

    #Verify the result in the table matches
    result_name = admin_pg.get_first_result_username()
    assert result_name == target_user, f"Expected {target_user} but found {result_name}"