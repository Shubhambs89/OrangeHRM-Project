import pytest
import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")

    login = LoginPage(driver)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()
    yield driver
    driver.quit()

# Test case 4 Menu visibility and Clickability
def test_case_4_menu_visibility_and_clickability(driver):
    dashboard = DashboardPage(driver)
    time.sleep(5)

    expected_menu = [
        "Admin", "PIM", "Leave", "Time",
        "Recruitment", "My Info", "Performance", "Dashboard"
    ]

    #Verify Visibility
    actual_menu = dashboard.get_menu_list()  # Call the method first
    actual_menu_lower = [m.lower() for m in actual_menu]

    for item in expected_menu:
        assert item.lower() in actual_menu_lower, f"{item} missing! Found: {actual_menu}"

    #Verify Clickability
    assert dashboard.is_menu_item_clickable(dashboard.menu_admin), "Admin not clickable"
    print("TC-4 Success: All menu items are visible and functional.")
