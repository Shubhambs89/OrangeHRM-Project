from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

# Test case 7 Forgot password
def test_case_7_forgot_password_validation(driver):
    login_page = LoginPage(driver)
    driver.get("https://opensource-demo.orangehrmlive.com/")


    login_page.click_forgot_password()
    WebDriverWait(driver, 10).until(EC.url_contains("requestPasswordResetCode"))

    #Enter username and submit
    login_page.reset_password("manager@guvi.in")

    #Verify the confirmation message appears
    success_xpath = "//h6[contains(@class, 'orangehrm-forgot-password-title')]"
    success_msg = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, success_xpath)))
    assert "Reset Password link sent" in success_msg.text
