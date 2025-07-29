from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import LoginPageLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        username_field = self.wait.until(EC.presence_of_element_located(LoginPageLocators.USERNAME_FIELD))
        password_field = self.wait.until(EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD))
        login_button = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    def is_login_successful(self):
        try:
            user_dropdown = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "p.oxd-userdropdown-name"))
            )
            return user_dropdown.is_displayed()
        except:
            return False