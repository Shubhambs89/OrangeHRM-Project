from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage

# Test Case 9 Admin
def test_case_9_admin_tabs(driver):
    """Scenario: Verify Admin page top navigation headers"""
    driver.get("https://opensource-demo.orangehrmlive.com/")

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    admin_pg = AdminPage(driver)

    #Login
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    #Click Admin Menu
    driver.find_element(*dashboard.menu_admin).click()

    #Get Headers
    tabs = admin_pg.get_top_nav_items()

    #Validation
    expected_tabs = ["User Management", "Job", "Organization", "Qualifications"]
    for tab in expected_tabs:
        assert tab in tabs, f"Header {tab} not found in Admin page!"

# Test case 10 Maintenance
def test_case_10_maintenance_validation(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    dashboard = DashboardPage(driver)

    #Click Maintenance
    dashboard.click_maintenance()

    #Verify the "Administrator Access"
    header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "h6")))
    assert "Administrator Access" in header.text