from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

# Test case 8 my info sub menu
def test_case_8_my_info_sub_menu_presence(driver):
    login_page = LoginPage(driver)
    wait = WebDriverWait(driver, 10)

    #Login with valid credentials
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    #Navigate to "My Info" section from the main sidebar
    my_info_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='My Info']")))
    my_info_link.click()

    #Expected sub-menu items (tabs on the left/top of My Info)
    expected_items = [
        "Personal Details",
        "Contact Details",
        "Emergency Contacts",
        "Dependents",
        "Immigration",
        "Job",
        "Salary",
        "Report-to",
        "Qualifications",
        "Memberships"
    ]

    # Find all tab elements
    tabs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "orangehrm-tabs-item")))
    actual_items = [tab.text.strip() for tab in tabs]

    #Validation
    for item in expected_items:
        assert item in actual_items, f"Sub-menu item '{item}' was not found!"